#!/usr/bin/env python3
"""Validate a Behavioral Communications Audit export.

Stdlib only. Checks the things a machine can settle: schema shape, that scores are 5/3/1,
that the findings table is within limits and severity-ordered, that flagged quotes are
verbatim in the source, and that a recommended revision has not introduced a date, URL,
phone number, email, or figure the source never contained.

What it cannot check: whether a score is RIGHT. An audit that rates everything 5 is
well-formed and wrong. That judgment stays with the reviewer.

Usage:
    validate.py audit.json [--source comm.txt] [--stamp]
    validate.py campaign.json --campaign [--source-dir DIR]
"""

import argparse
import json
import os
import re
import sys
import unicodedata
from datetime import datetime, timezone

PRINCIPLES = [
    ("attention", "salience", "Salience"),
    ("attention", "relevance_personalization", "Relevance & Personalization"),
    ("attention", "credibility_identity_alignment", "Credibility & Identity Alignment"),
    ("intention", "clarity_simplicity_brevity", "Clarity, Simplicity & Brevity"),
    ("intention", "support_self_efficacy", "Support & Self-Efficacy"),
    ("intention", "social", "Social"),
    ("intention", "persuasion_cost_benefit_value", "Persuasion & Cost-Benefit Value"),
    ("action", "clear_cta_focus", "Clear Call-to-Action & Focus"),
    ("action", "ease_hassle_reduction", "Ease & Hassle Reduction"),
    ("action", "timeliness_urgency", "Timeliness & Urgency"),
]
STAGES = ["attention", "intention", "action"]
BY_STAGE = {s: [k for st, k, _ in PRINCIPLES if st == s] for s in STAGES}
NAMES = {n for _, _, n in PRINCIPLES}
KEYS = {k for _, k, _ in PRINCIPLES}
SEV_RANK = {"High": 0, "Medium": 1, "Low": 2}
CHANNELS = {"email", "sms", "chat", "call_script", "web_page", "print", "push", "other"}
MODES = {"AUDIT", "AUDIT_LITE", "TAG_ONLY", "REDRAFT_ONLY", "CAMPAIGN_SCAN", "CAMPAIGN_FULL"}
TOP = ["metadata", "communication", "behavioral_scores", "stage_summary", "findings",
       "findings_omitted", "categorization", "analysis_summary", "assumptions", "placeholders_used"]
FACTS = [
    (re.compile(r"https?://[^\s)\]'\"]+"), "a URL"),
    (re.compile(r"[\w.+-]+@[\w-]+\.\w{2,}"), "an email address"),
    (re.compile(r"\(?\b\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}\b"), "a phone number"),
    (re.compile(r"\b\d[\d,]{1,}(?:\.\d+)?%?\b"), "a number"),
]


def norm(text):
    """Normalize for comparison only; never mutates what is emitted.

    Pasted email and PDF text carry NBSPs and curly quotes that make a byte-exact match
    fail on text a human would call identical.
    """
    t = unicodedata.normalize("NFKC", text or "")
    for a, b in (("‘", "'"), ("’", "'"), ("“", '"'), ("”", '"'),
                 ("–", "-"), ("—", "-")):
        t = t.replace(a, b)
    return re.sub(r"\s+", " ", t)


def validate_audit(a, source=None, label="audit", allow_ts=False, stats=None):
    errs, warns = [], []
    st = stats if stats is not None else {}

    def e(m):
        errs.append(f"[{label}] {m}")

    if not isinstance(a, dict):
        return [f"[{label}] not a JSON object"], warns

    for k in TOP:
        if k not in a and k != "findings_omitted":
            e(f"required field {k!r} is missing")
    for k in a:
        if k not in TOP:
            e(f"unexpected top-level field {k!r}")

    meta = a.get("metadata") or {}
    if meta.get("schema_version") != "1.2":
        e(f"metadata.schema_version must be '1.2', got {meta.get('schema_version')!r}")
    if meta.get("mode") not in MODES:
        e(f"metadata.mode {meta.get('mode')!r} is not a valid mode")
    if not str(meta.get("comm_id") or "").strip():
        e("metadata.comm_id is empty")
    if not allow_ts and meta.get("processing_timestamp") is not None:
        e("metadata.processing_timestamp must be null on emit; validate.py --stamp writes it")

    comm = a.get("communication") or {}
    for k in ("label", "channel", "audience_segment", "primary_goal", "source"):
        if not str(comm.get(k) or "").strip():
            e(f"communication.{k} is empty")
    if comm.get("channel") not in CHANNELS:
        e(f"communication.channel {comm.get('channel')!r} is invalid")

    # --- ten principle scores
    bs = a.get("behavioral_scores") or {}
    for k in bs:
        if k not in STAGES:
            e(f"behavioral_scores has unexpected stage {k!r}")
    scored = {}
    for stage in STAGES:
        block = bs.get(stage)
        if not isinstance(block, dict):
            e(f"behavioral_scores.{stage} is missing")
            continue
        for k in block:
            if k not in BY_STAGE[stage]:
                e(f"behavioral_scores.{stage} has unexpected principle {k!r}")
        for k in BY_STAGE[stage]:
            if k not in block:
                e(f"behavioral_scores.{stage}.{k} is missing")
                continue
            v = block[k]
            if isinstance(v, bool) or v not in (5, 3, 1, None):
                e(f"{k}: score {v!r} must be 5, 3, 1, or null")
            elif v is not None:
                scored[k] = v
    st["scored"] = st.get("scored", 0) + len(scored)
    st["na"] = st.get("na", 0) + (10 - len(scored))

    ss = a.get("stage_summary") or {}
    for stage in STAGES:
        if ss.get(stage) not in ("pass", "weak", "fail"):
            e(f"stage_summary.{stage} must be pass, weak, or fail (got {ss.get(stage)!r})")

    # --- findings
    f = a.get("findings")
    if not isinstance(f, list):
        e("findings must be a list")
        return errs, warns
    if len(f) > 10:
        e(f"findings has {len(f)} rows; the maximum is 10")
    fo = a.get("findings_omitted", 0)
    if isinstance(fo, bool) or not isinstance(fo, int) or fo < 0:
        e(f"findings_omitted must be a non-negative integer, got {fo!r}")

    ranks, n_ok = [], 0
    for i, row in enumerate(f, start=1):
        if not isinstance(row, dict):
            e(f"finding {i} is not an object")
            continue
        pid = row.get("problem_id")
        if pid != f"P{i}":
            e(f"finding {i}: problem_id is {pid!r}, expected 'P{i}'")
        if row.get("principle") not in NAMES:
            e(f"{pid}: principle {row.get('principle')!r} is not an exact framework name")
        if row.get("severity") not in SEV_RANK:
            e(f"{pid}: severity {row.get('severity')!r} must be High, Medium, or Low")
        else:
            ranks.append(SEV_RANK[row["severity"]])
        for k in ("why", "recommended_revision"):
            if not str(row.get(k) or "").strip():
                e(f"{pid}: {k} is empty")
        q = row.get("flagged_quote")
        if not isinstance(q, str) or not q.strip():
            e(f"{pid}: flagged_quote is missing or empty")
        elif source is not None and norm(q) not in norm(source):
            e(f"{pid}: flagged_quote is not verbatim in the source: {q[:70]!r}")
        elif source is not None:
            n_ok += 1
        # a revision may not introduce a fact the source never had, unless bracketed
        rev = str(row.get("recommended_revision") or "")
        if source is not None and rev:
            bare = re.sub(r"\[[^\[\]]*\]", " ", rev)
            for pat, kind in FACTS:
                for hit in pat.findall(bare):
                    if len(str(hit).strip()) > 1 and norm(str(hit)) not in norm(source):
                        e(f"{pid}: recommended_revision introduces {kind} ({str(hit)[:40]!r}) "
                          f"absent from the source — bracket it as a [Placeholder]")
    if ranks != sorted(ranks):
        e("findings are not ordered by severity (High, then Medium, then Low)")
    st["quotes"] = st.get("quotes", 0) + n_ok
    st["findings"] = st.get("findings", 0) + len(f)

    for ph in a.get("placeholders_used") or []:
        if not isinstance(ph, str) or not re.fullmatch(r"\[[^\[\]]+\]", ph):
            e(f"placeholders_used entry {ph!r} must be a single bracketed token")
    used = set()
    for row in f:
        if isinstance(row, dict):
            used |= set(re.findall(r"\[[^\[\]]+\]", str(row.get("recommended_revision") or "")))
    for ph in sorted(used - set(a.get("placeholders_used") or [])):
        e(f"placeholder {ph} appears in a revision but is not listed in placeholders_used")

    pw = (a.get("analysis_summary") or {}).get("primary_weakness")
    if pw not in KEYS | {"none"}:
        e(f"analysis_summary.primary_weakness {pw!r} is not a principle key or 'none'")
    elif scored and pw != "none" and scored.get(pw, 9) != min(scored.values()):
        warns.append(f"[{label}] primary_weakness is {pw!r} but the lowest score is "
                     f"{min(scored.values())}; confirm that is deliberate")
    if not str((a.get("analysis_summary") or {}).get("key_findings") or "").strip():
        e("analysis_summary.key_findings is empty")

    if source is None:
        warns.append(f"[{label}] no source supplied — {len(f)} quote(s) were NOT checked")
    elif scored and min(scored.values()) == 5:
        warns.append(f"[{label}] every scored principle is 5; a clean sweep deserves a second look")
    return errs, warns


def validate_campaign(c, source_dir=None, allow_ts=False, stats=None):
    errs, warns = [], []
    st = stats if stats is not None else {}
    meta = c.get("metadata") or {}
    if meta.get("schema_version") != "1.2":
        errs.append("[campaign] metadata.schema_version must be '1.2'")
    if meta.get("mode") not in ("CAMPAIGN_SCAN", "CAMPAIGN_FULL"):
        errs.append(f"[campaign] metadata.mode {meta.get('mode')!r} is not a campaign mode")
    if not allow_ts and meta.get("processing_timestamp") is not None:
        errs.append("[campaign] metadata.processing_timestamp must be null on emit")

    inv = c.get("inventory") or []
    audits = c.get("audits") or []
    if not inv:
        errs.append("[campaign] inventory is empty")
    ids = [r.get("comm_id") for r in inv if isinstance(r, dict)]
    if len(set(ids)) != len(ids):
        errs.append("[campaign] duplicate comm_id in inventory")
    if meta.get("comm_count") != len(inv):
        errs.append(f"[campaign] comm_count {meta.get('comm_count')!r} != inventory length {len(inv)}")
    src_of = {r.get("comm_id"): os.path.basename(str(r.get("source") or ""))
              for r in inv if isinstance(r, dict)}

    sources = {}
    for a in audits:
        cid = (a.get("metadata") or {}).get("comm_id")
        if cid not in ids:
            errs.append(f"[campaign] audit comm_id {cid!r} is not in the inventory")
        text = None
        if source_dir and src_of.get(cid):
            p = os.path.join(source_dir, src_of[cid])
            if os.path.isfile(p):
                text = open(p, encoding="utf-8").read()
                sources[cid] = text
            else:
                errs.append(f"[campaign] {cid}: source file {src_of[cid]!r} not found in {source_dir}")
        se, sw = validate_audit(a, text, label=cid or "audit", allow_ts=allow_ts, stats=st)
        errs += se
        warns += sw

    seen = set()
    for x in c.get("consistency_register") or []:
        xid = x.get("conflict_id")
        if xid in seen:
            errs.append(f"[campaign] duplicate conflict_id {xid!r}")
        seen.add(xid)
        if x.get("comm_a") == x.get("comm_b"):
            errs.append(f"[campaign] {xid}: a cross-comm conflict needs two different comms")
        for side, qk in (("comm_a", "quote_a"), ("comm_b", "quote_b")):
            if x.get(side) not in ids:
                errs.append(f"[campaign] {xid}: {side}={x.get(side)!r} not in inventory")
            q = str(x.get(qk) or "")
            if not q.strip():
                errs.append(f"[campaign] {xid}: {qk} is empty — a conflict needs both quotes")
            elif sources.get(x.get(side)) and norm(q) not in norm(sources[x.get(side)]):
                errs.append(f"[campaign] {xid}: {qk} is not verbatim in {x.get(side)}'s source")

    for where, rows, key in (("cadence_flags", c.get("cadence_flags"), "comm_ids"),
                             ("patterns", c.get("patterns"), "failing_comms")):
        for row in rows or []:
            for cid in row.get(key) or []:
                if cid not in ids:
                    errs.append(f"[campaign] {where}: comm_id {cid!r} is not in the inventory")
    for p in c.get("patterns") or []:
        if p.get("principle") not in NAMES:
            errs.append(f"[campaign] {p.get('pattern_id')}: principle "
                        f"{p.get('principle')!r} is not an exact framework name")
    st["comms"] = len(inv)
    st["audited"] = len(audits)
    return errs, warns


def main():
    ap = argparse.ArgumentParser(description="Validate a Behavioral Communications Audit export.")
    ap.add_argument("json_file")
    ap.add_argument("--source", help="plain-text source comm, for verbatim quote checking")
    ap.add_argument("--source-dir", help="directory of source comms, for a campaign export")
    ap.add_argument("--campaign", action="store_true")
    ap.add_argument("--stamp", action="store_true", help="write processing_timestamp in place")
    ap.add_argument("--allow-timestamp", action="store_true",
                    help="permit a non-null timestamp (re-checking a stamped file)")
    args = ap.parse_args()

    data = json.load(open(args.json_file, encoding="utf-8"))
    source = open(args.source, encoding="utf-8").read() if args.source else None
    allow = args.allow_timestamp or args.stamp
    stats = {}
    if args.campaign:
        errs, warns = validate_campaign(data, args.source_dir, allow, stats)
    else:
        errs, warns = validate_audit(data, source, allow_ts=allow, stats=stats)

    for w in warns:
        print(f"  WARN  {w}")
    if errs:
        print(f"\nFAIL — {len(errs)} error(s):")
        for x in errs:
            print(f"  ERROR {x}")
        sys.exit(1)

    if args.stamp:
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        data.setdefault("metadata", {})["processing_timestamp"] = ts
        with open(args.json_file, "w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        print(f"stamped processing_timestamp = {ts}")

    bits = []
    if args.campaign:
        bits.append(f"{stats.get('comms', 0)} comms, {stats.get('audited', 0)} audited")
    bits += [f"{stats.get('scored', 0)} principles scored", f"{stats.get('na', 0)} n/a",
             f"{stats.get('findings', 0)} findings"]
    bits.append(f"{stats.get('quotes', 0)} quotes verified verbatim"
                if (source or args.source_dir) else "no source — quotes unchecked")
    print(f"PASS — {os.path.basename(args.json_file)}: " + " · ".join(bits))
    print("       Checked: shape, scores, ordering, quote fidelity, invented facts. "
          "Not checked: whether a score is correct.")
    sys.exit(0)


if __name__ == "__main__":
    main()
