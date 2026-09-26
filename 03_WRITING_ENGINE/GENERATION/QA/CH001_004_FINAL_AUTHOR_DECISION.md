# CH001–004 — FINAL AUTHOR DECISION

> **Scope:** contains only decisions that genuinely require the author's choice. No decision is made here.
> **Mode:** audit only. No file modified.

---

## ADR-01 — Chapter 001 annex-reporting / assignment date (1 September vs 2 September 2024)

### What conflicts

Two authorities disagree about when Arthur reports to Records & Archives and when the five-field assignment is posted.

**Authority set 1 — the prose (and its supporting baseline):**
- `CHAPTERS/001_ERROR_UNDEFINED.md` stages the district-office assignment readout (scene 2), then arrival at Ravenhurst and reporting in to the Records and Archives annex (scene 3) on **1 September 2024**, with the first slip filed the same day.
- Supported by the accepted `CH001_FLOW_REPAIRED_BASEmessaging app.md` / `CH001_ACCEPTED_BASEmessaging app.md` (scene 3 = 1 September 2024) and `CONTINUITY_STATE.md` (scene 3 = 1 September 2024), and by LOCK 13's chapter span "25 Aug assessment → 1 Sep entry."

**Authority set 2 — the locked timeline:**
- **LOCK 2 T-08:** "**September 2, 2024** — Assignment order posted — reports to the Intelligence Division's records annex 0600."
- **LOCK 2 registry:** "Records & Archives assignment — **2 September 2024** — LOCKED."
- **`CHAPTER_GENERATION_QUEUE.md`:** "**2 September 2024** — Records & Archives operational."

### Why it matters

Under Authority set 2, the assignment is *posted* on 2 Sep, so the prose's district-office readout (pre-entry, late August) and the 1 Sep annex reporting cannot both predate it. The two readings cannot both be true at once.

### The two options (presented neutrally — do not choose)

**Option A — the prose date governs (annex reporting = 1 September 2024).**
- Requires reopening/moving **LOCK 2 T-08** and the **Queue** "2 September" anchor to 1 September (a canon-date change).
- Chapter 001–004 prose: **no edit needed**; CH001's header ("Late August – 1 September 2024") and the current continuity state stand.
- Downstream: LOCK 2 registry line and the Queue anchor must be updated; CH001 baselines already match.

**Option B — the locked date governs (annex reporting = 2 September 2024).**
- Keeps LOCK 2 T-08 and the Queue anchor unchanged.
- Requires a bounded CH001 edit: keep 1 September as the **intake/arrival + quarters** beat, insert a declared one-line time-skip, and move the **annex reporting + first filing** (CH001 L144–148) to 2 September; CH001's header range extends to 2 September.
- Knock-on checks (bounded): CH002's "The next morning" (= 2 Sep) and the first-work-shift framing (2–3 Sep) must be re-anchored so they follow the moved reporting; `CONTINUITY_STATE.md` and the CH001 baseline record update accordingly.
- Downstream: CH002 opening, CH001 header, CH001 baseline/continuity records.

### Neutral impact comparison

| | Option A | Option B |
|---|---|---|
| LOCK 2 T-08 / Queue change | yes (canon) | no |
| CH001 prose edit | no | yes (bounded, ~2–3 sentences + header) |
| CH002 opening impact | none | one-line re-anchor check |
| Reader-facing effect | current prose unchanged | arrival and reporting split across two days |
| Baselines/continuity updates | LOCK/Queue records | CH001/CH002 records |

### Status
**AUTHOR DECISION REQUIRED.** No choice is made here. Until resolved, this single item stands as the only outstanding matter before the four chapters are treated as final canon-continuous prose.

---

*End of CH001_004_FINAL_AUTHOR_DECISION.md — decision item only.*
