# NARRATIVE FLOW / READABILITY REPAIR RECOMMENDATIONS
## Chapters 001–004

> **Status:** Recommendations only. No repairs executed. No chapter, baseline, canon, lock, or engine file modified.

## 1. Future Generation Only

Add these mandatory fields to every future chapter specification and scene map:

1. **In-universe date** for every scene.
2. **Approximate time** or a deliberate time-of-day marker.
3. **Opening location** and the location Arthur came from.
4. **Reason for movement** into the scene.
5. **Carried state:** what Arthur knows, holds, owes, or is pursuing.
6. **One-sentence bridge:** `After [previous consequence], Arthur [moves/returns/reports] because [want].`
7. **Exit state:** exact consequence and the next scene's causal trigger.

Add a generation gate:

> **A scene may hard-cut only when the reader can recover date, location, reason for arrival, current want, and carried information within the first three sentences.**

Add a natural-English pass after technical QA:

- Replace compressed idioms with ordinary natural English when they slow parsing.
- Preserve short sentences when they create pressure or emphasis.
- Do not use a short sentence to hide a missing causal bridge.
- Prefer literal verbs for movement and institutional action.
- Read every scene transition without its metadata header; if the sequence becomes unclear, add one orienting clause.

## 2. Existing Chapters — Bounded Polish Candidates

These are recommendations only. Do not apply automatically.

### R-01 — Chapter 004 chronology correction (required)
- **Location:** Opening paragraph.
- **Current:** `Arthur had been working the low pile for six days`.
- **Problem:** Conflicts with 5 September date and the established start of Records work after 1 September.
- **Recommendation:** Replace the duration with a date-safe phrase such as `for several shifts` or `since his first workday`, subject to the project’s preferred exact timeline.
- **Scope:** One sentence; no plot or canon change.
- **Priority:** Required before the four-chapter run is treated as chronology-clean.

### R-02 — Chapter 001 scene/date bridges (optional)
- **Locations:** Processing-office transition and 1 September arrival transition.
- **Problem:** Understandable but header-dependent.
- **Recommendation:** Add one compact bridge at each transition identifying the elapsed time and why Arthur is moving.
- **Scope:** Bounded prose polish; no new event.

### R-03 — Chapter 002 scene/time bridge (optional)
- **Location:** Old-gym scene opening.
- **Problem:** The reader cannot tell whether the gym follows the mess that evening or occurs in the next training block.
- **Recommendation:** Add a single time-of-day or next-day marker and one movement clause.
- **Scope:** Bounded orientation polish.

### R-04 — Chapter 002 natural-English pass (optional)
- **Recommendation:** Smooth only phrases that require non-native idiomatic reconstruction. Preserve the chapter’s institutional voice and imagery where the compression is intentional.

### R-05 — Chapter 003 wording pass (optional)
- **Candidates:** `Fourteenth hour`; `presorting`; the station-seven grading sentence; `made a copy of him`.
- **Recommendation:** Clarify institutional titles and time wording; make the station-seven causal rule explicit; retain the final image only if it remains immediately legible.

### R-06 — Chapter 004 natural-English pass (optional)
- **Candidates:** `trust the feeling`; `arrive at the same place`; `face that suggested...`; `That was its destination`; `they were also the same direction`.
- **Recommendation:** Prefer natural literal phrasing where the sentence makes the reader parse an abstract metaphor before understanding the action.

## 3. Changes That Should NOT Be Made

- Do **not** add travel scenes, meals, dormitory scenes, or routine school events merely to show passage of time.
- Do **not** slow the chapters with exhaustive transitions.
- Do **not** remove every hard cut; justified hard cuts are part of the approved style.
- Do **not** flatten the bureaucratic metaphors that clearly belong to Quiet Tide.
- Do **not** remove tactical cognition or short emphasis sentences wholesale.
- Do **not** alter chapter functions, mystery plants, Seal behavior, or institutional outcomes.
- Do **not** resolve East Beach, the Seep, ERROR/UNDEFINED, or any protected fence.
- Do **not** revise accepted baselines until each bounded change has its own diff and post-polish QA.
- Do **not** modify the Writing Engine globally before separating the concrete Chapter 004 chronology defect from the broader sentence-level pattern.

## 4. Recommended Order of Work

1. Repair Chapter 004's concrete duration contradiction (R-01), then run continuity QA.
2. Perform a bounded transition pass on 001–004 using only one orienting clause where needed (R-02/R-03).
3. Perform a separate natural-English pass (R-04/R-05/R-06), keeping a before/after diff.
4. Re-run the four-chapter flow audit.
5. Only after evidence from the bounded pass, consider a narrow Writing Engine / Production Protocol amendment for bridge requirements and natural-English review.

## Recommendation Status

**Do not generate Chapter 005 yet.** First resolve R-01 and complete the bounded flow/readability pass or explicitly waive it through a separate decision.

*End of NARRATIVE_FLOW_REPAIR_RECOMMENDATIONS.md — recommendations only.*
