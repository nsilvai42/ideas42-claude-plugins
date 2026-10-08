# Settings-card template

Render this when you can show a visual widget or Artifact. It presents the recommendation as a branded "Recommended setup" card with three rows — Surface, Model, Effort (a dial) — plus a guidance footer. Always print a one-line text verdict above it too (the card may not render for everyone).

## Contents
- **ideas42 styling** — fixed colors/fonts (don't change)
- **How to fill it in** — header, highlighting picks, model descriptions, the Claude Design case, the effort dial config
- **Template** — the full HTML + dial JS to copy

## ideas42 styling (don't change these)
These hex values mirror the ideas42 palette; the `ideas42-brand` skill is the source of truth if the brand ever changes.
- Font: Figtree (loaded via the `@import`).
- Header band: indigo `#003847`, white title, `#9DB6BD` eyebrow, `#C5D2D6` note.
- Recommended/selected accent: green-apple `#7AC10A` (2px border + faint fill + a green check). This is the only accent — don't add a second.
- Spruce `#156A57` for the selected surface icon and small green captions.
- Borders: rain `#D9E1E2`. Card body background: `var(--color-background-primary)` so dark mode still works.
- Ultracode on the dial stays purple `#8470FF` — it mirrors the real product UI (ideas42 has no purple).

## How to fill it in

1. **Header** — set the summary to your pick `[Surface] · [Model] · [Effort]` and the right note to a one-line "good for…" task description.
2. **Highlight one option per row** by adding `opt-pick` to its class and dropping the `<i class="ti ti-check chk">` inside it. Exactly one pick in Surface, one in Model.
3. **Model row uses the official picker descriptions verbatim** — do not paraphrase:
   - `Haiku 4.5` → "Fastest for quick answers"
   - `Sonnet 4.6` → "Most efficient for everyday tasks"
   - `Opus 4.8` → "For complex tasks"
3b. **Claude Design is browser-only.** It exposes the same model + effort controls as the other surfaces, so when Design is the pick, show the model row + dial as normal. Add a small `browser only` note (Design isn't in the Cowork desktop app or Code) — a pill in the header band works well — so anyone in the desktop app or Code knows they'll need a browser.

4. **Effort dial** — set the three JS config vars at the top of the script:
   - `STOPS` — the recommended model's effort stops:
     - Sonnet → `['Low','Medium','High','Max']`
     - Opus → `['Low','Medium','High','Extra','Max']`, and append `'Ultracode'` **only if the recommended surface is Code**
     - Haiku → **no dial.** Delete the Effort dial block and the `<div id="dial">`; Haiku's only control is the Extended thinking toggle, so show just the toggle/caption.
   - `REC` — index of the recommended stop (the knob parks here; the green caption names it).
   - `UC` — `true` only for Opus on the Code surface (turns the final stop + fill purple).
5. **Recommended caption** under the dial — name the recommended effort and keep the "raise it before reaching for a heavier model" line.
6. **Footer** — keep the guidance principle. Adjust only the second sentence if extended thinking is actually recommended on.

Emit as HTML starting with the `<style>` block — never lead with `<svg>`, or the renderer treats the whole thing as SVG and fails.

## Template

```html
<style>
@import url('https://fonts.googleapis.com/css2?family=Figtree:wght@400;500&display=swap');
.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);border:0}
.e42{font-family:'Figtree',var(--font-sans)}
.set-label{font-size:12px;color:var(--color-text-secondary);margin:16px 0 7px}
.set-row{display:flex;gap:8px}
.opt{flex:1;position:relative;border-radius:var(--border-radius-md);border:0.5px solid #D9E1E2;background:var(--color-background-secondary);padding:10px 12px}
.opt-pick{border:2px solid #7AC10A;background:rgba(122,193,10,0.10)}
.opt-c{text-align:center}
.opt-t{font-size:13px;font-weight:500;color:var(--color-text-primary)}
.opt-s{font-size:11px;color:var(--color-text-tertiary);margin-top:2px;line-height:1.35}
.chk{position:absolute;top:8px;right:9px;color:#7AC10A;font-size:15px;display:none}
.opt-pick .chk{display:block}
</style>
<h2 class="sr-only">Recommended setup: [Surface], [Model], [Effort] — [task summary].</h2>
<div class="e42" style="background:var(--color-background-secondary);border-radius:var(--border-radius-lg);padding:1rem">
  <div style="background:var(--color-background-primary);border:0.5px solid #D9E1E2;border-radius:var(--border-radius-lg);overflow:hidden">

    <div style="background:#003847;padding:14px 18px;display:flex;justify-content:space-between;align-items:flex-end;gap:16px;flex-wrap:wrap">
      <div>
        <p style="font-size:11px;letter-spacing:0.04em;text-transform:uppercase;color:#9DB6BD;margin:0 0 3px">Recommended setup</p>
        <p style="font-size:20px;font-weight:500;color:#fff;margin:0">[Surface] · [Model] · [Effort]</p>
      </div>
      <p style="font-size:13px;color:#C5D2D6;margin:0;max-width:240px;text-align:right">[Good for … one-line task note.]</p>
    </div>

    <div style="padding:0 18px 18px">

      <p class="set-label">Surface — where the work lives</p>
      <div class="set-row">
        <div class="opt opt-c opt-pick"><i class="ti ti-check chk" aria-hidden="true"></i><i class="ti ti-message-circle" style="font-size:18px;color:#156A57" aria-hidden="true"></i><div class="opt-t">Chat</div><div class="opt-s">quick, no files</div></div>
        <div class="opt opt-c"><i class="ti ti-briefcase" style="font-size:18px;color:var(--color-text-tertiary)" aria-hidden="true"></i><div class="opt-t">Cowork</div><div class="opt-s">files &amp; apps</div></div>
        <div class="opt opt-c"><i class="ti ti-code" style="font-size:18px;color:var(--color-text-tertiary)" aria-hidden="true"></i><div class="opt-t">Code</div><div class="opt-s">repos &amp; terminal</div></div>
        <div class="opt opt-c"><i class="ti ti-palette" style="font-size:18px;color:var(--color-text-tertiary)" aria-hidden="true"></i><div class="opt-t">Design</div><div class="opt-s">visual artifacts</div></div>
      </div>

      <p class="set-label">Model — matched to task complexity</p>
      <div class="set-row">
        <div class="opt" style="min-height:58px"><div class="opt-t">Haiku 4.5</div><div class="opt-s">Fastest for quick answers</div></div>
        <div class="opt opt-pick" style="min-height:58px"><i class="ti ti-check chk" aria-hidden="true"></i><div class="opt-t">Sonnet 4.6</div><div class="opt-s">Most efficient for everyday tasks</div></div>
        <div class="opt" style="min-height:58px"><div class="opt-t">Opus 4.8</div><div class="opt-s">For complex tasks</div></div>
      </div>

      <p class="set-label">Effort — the dial within [Model]</p>
      <div id="dial"></div>
      <div style="display:flex;align-items:center;gap:6px;margin:10px 0 0">
        <span style="width:8px;height:8px;border-radius:50%;background:#7AC10A;display:inline-block"></span>
        <span style="font-size:11px;color:#156A57">[Effort] — recommended; raise it before reaching for a heavier model.</span>
      </div>

      <div style="margin-top:16px;display:flex;gap:9px;align-items:flex-start;background:var(--color-background-secondary);border-radius:var(--border-radius-md);padding:11px 13px">
        <i class="ti ti-bulb" style="font-size:17px;color:#156A57;flex-shrink:0;margin-top:1px" aria-hidden="true"></i>
        <p style="font-size:12.5px;line-height:1.55;color:var(--color-text-secondary);margin:0">Switch surfaces only when the work needs files, apps, repo changes, or visual review. Extended thinking stays off unless the task needs step-by-step reasoning.</p>
      </div>

    </div>
  </div>
</div>
<script>
(function(){
  var APPLE='#7AC10A', UC_COLOR='#8470FF';
  var STOPS=['Low','Medium','High','Max'];
  var REC=0;
  var UC=false;
  var sel=REC, n=STOPS.length, mount=document.getElementById('dial');
  if(!mount) return;
  var head=document.createElement('div'); head.style.cssText='display:flex;align-items:baseline;gap:6px;margin-bottom:10px';
  head.innerHTML='<span style="font-size:14px;color:var(--color-text-secondary)">Effort</span>';
  var val=document.createElement('span'); val.style.cssText='font-size:14px;font-weight:500'; head.appendChild(val);
  var ends=document.createElement('div'); ends.style.cssText='display:flex;justify-content:space-between;font-size:12px;color:var(--color-text-tertiary);margin-bottom:4px'; ends.innerHTML='<span>Faster</span><span>Smarter</span>';
  var wrap=document.createElement('div'); wrap.style.cssText='position:relative;height:22px;margin:2px 9px 0';
  mount.appendChild(head); mount.appendChild(ends); mount.appendChild(wrap);
  var track=document.createElement('div'); track.style.cssText='position:absolute;top:8px;left:0;right:0;height:6px;border-radius:3px;background:var(--color-background-secondary)';
  var fill=document.createElement('div'); fill.style.cssText='position:absolute;top:8px;left:0;height:6px;border-radius:3px;transition:width .12s,background .12s';
  wrap.appendChild(track); wrap.appendChild(fill);
  for(var i=0;i<n;i++){
    var pct=i/(n-1)*100, isUC=UC&&i===n-1;
    var dot=document.createElement('button'); dot.type='button'; dot.setAttribute('aria-label',STOPS[i]);
    dot.style.cssText='position:absolute;top:50%;transform:translate(-50%,-50%);left:'+pct+'%;width:20px;height:20px;border:none;background:transparent;cursor:pointer;padding:0';
    var pip=document.createElement('span'); pip.style.cssText='display:block;width:6px;height:6px;border-radius:50%;margin:7px auto;background:'+(isUC?UC_COLOR:'var(--color-text-tertiary)');
    dot.appendChild(pip);
    (function(idx){dot.addEventListener('click',function(){sel=idx;upd();});})(i);
    wrap.appendChild(dot);
  }
  var knob=document.createElement('div'); knob.style.cssText='position:absolute;top:50%;transform:translate(-50%,-50%);width:18px;height:18px;border-radius:50%;background:#fff;border:2px solid '+APPLE+';transition:left .12s';
  wrap.appendChild(knob);
  function upd(){var pct=sel/(n-1)*100, isUC=UC&&sel===n-1; knob.style.left=pct+'%'; fill.style.width=pct+'%'; fill.style.background=isUC?UC_COLOR:APPLE; val.textContent=STOPS[sel]; val.style.color=isUC?UC_COLOR:'var(--color-text-primary)';}
  upd();
})();
</script>
```
