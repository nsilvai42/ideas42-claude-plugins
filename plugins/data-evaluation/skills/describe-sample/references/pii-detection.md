# PII detection

Always run PII detection in Step 1, before any value-level computation. If PII is detected, halt and request authorization through the elicitation form before proceeding.

## Always-PII column patterns

| Pattern | Examples |
|---|---|
| Email | column name matches `email`, `e_mail`, `mail` |
| Names | `name`, `first_name`, `last_name`, `full_name`, `recipient_*name*` |
| Phone | `phone`, `mobile`, `tel`, `cell` |
| SSN | `ssn`, `social_security`, `tax_id`, `tin` |
| Government IDs | `passport`, `license`, `drivers_license`, `ein` |
| Financial accounts | `account_number`, `card_number`, `bank_account` |
| Health | `mrn`, `medical_record`, `diagnosis`, `icd_code` |
| Home address | `home_address`, `street_address`, `mailing_address` (work_address generally OK) |
| Precise geolocation | `latitude`, `longitude`, `lat`, `lng`, `gps`, `coordinates` |
| Network identifiers | `ip_address`, `ipaddress`, `device_id`, `mac_address` |
| Birth | `dob`, `date_of_birth`, `birth_date` |

## Pattern-based content checks (only if column name is ambiguous)

If a column name is generic but content might be PII, sample 10 random non-null rows and check:

| Regex | What it suggests |
|---|---|
| `\b[\w.+-]+@[\w.-]+\.\w+\b` | Email address |
| `\b\d{3}-?\d{2}-?\d{4}\b` | SSN-like |
| `\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b` | Credit card |
| `\b\d{3}[-. ]?\d{3}[-. ]?\d{4}\b` | US phone |
| `\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b` | IP address |

If any match: treat the column as PII-candidate.

## Combinatorial PII

Some columns are not PII individually but become identifying when combined:
- Name + DOB + ZIP code → likely uniquely identifying
- IP address + timestamp → identifying
- ZIP + age + sex + race → can re-identify per HIPAA's 18 elements

If multiple individually-low-risk columns are present in combination, flag in the PII alert as "combinatorial PII risk" and recommend k-anonymity check or aggregation.

## What to do when PII is detected

Halt the workflow at Step 1. Surface to the user via elicitation form (see `elicitation-templates.md` → Form 3). Show:
- Each PII-candidate column name
- Non-null count
- DO NOT show any actual values or summary statistics of these columns

Offer four actions:
1. **Drop the PII columns and proceed** (Recommended) — most analyses don't need them
2. **Keep but never display** — useful for joining/merging without surfacing
3. **Proceed with authorization** — user enters the authorization code per their stored preferences
4. **Pause** — let me investigate first

If the user has personal preferences requiring an authorization code (per their org/personal `CLAUDE.md`), enforce that path strictly. Never reveal what the code is or hint at it.

## Public-safe variant (output)

If the user requests the public-safe variant deliverable:
- Strip all PII-candidate columns from any output dataset
- Apply cell suppression: in any aggregate table, suppress cells where n < 5 (replace with "—")
- Combine small subgroups in chart labels (e.g., "n=3 Asian" → folded into "Other" with a note)
- Add a watermark / footer: "Public-release variant; small cells suppressed; PII columns removed."

## What this skill never does with PII

- Never echo PII values in chat, logs, or scratch output
- Never include PII column values in the verification step
- Never write PII to a "intermediate" CSV in the output folder unless the user explicitly approved keeping them
- Never use PII as a join key in a manner that the resulting dataset retains the PII (use a hash if a join key is needed)
