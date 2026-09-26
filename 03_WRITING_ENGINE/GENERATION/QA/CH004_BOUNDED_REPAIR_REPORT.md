# CH004 BOUNDED REPAIR REPORT — SF-1 + SF-2

> **Scope:** only the two SHOULD FIX items from `CH004_FULL_REVISION_AUDIT.md`. SF-1 applied; SF-2 documented (not repaired). No OPTIONAL item touched. No canon/engine/spec/continuity/baseline change; no CH001–CH003/CH005 change.
> **Chapter file modified:** `03_WRITING_ENGINE\GENERATION\CHAPTERS\004_THE_WRONG_RULE.md` only.
> **Report file created:** this file.

---

## SF-1 — repetitive recap of the misfile cause (applied)

**Original passage (L86):**
> "He left the window with the correction form in his pocket and the zone name still in his head. East Beach Annex, Zone 11. A sound-bleed that played back the wrong day's conversations. **Filed under the wrong Rule because someone had ticked the box for a living entity and never read the description beneath it.**"

**Repaired passage (L86):**
> "He left the window with the correction form in his pocket and the zone name still in his head. East Beach Annex, Zone 11. A sound-bleed that played back the wrong day's conversations."

**Reason:** the trimmed clause restated the misfile cause already established at L16 ("The intake clerk had read the first box, not the description, and filed it under R-7") and restated again at L94 ("filed under R-7 because the clerk who had logged it had checked the wrong box on the form"). Removing the third statement at the scene exit keeps the discovery (L16) and the reflection + "one column over" detail (L94) as the carriers, and leaves the zone-name beat and the scene-out transition intact. No replacement/explanatory sentence was added.

## SF-2 — "Rule" vs R-7/R-4 terminology (NOT repaired; documented)

**Original/context passages:**
- L10: "…then opened the **Rule index** and checked R-7."
- L12: "R-7 was the **response protocol** for living-entity Seep activity."
- L14: "The correct **protocol** was R-4…"
- L24: "…changed the **Rule header** from R-7 to R-4…"
- L86: "…Filed under the wrong **Rule**…" *(removed by SF-1)*
- Title (L1): "THE WRONG **RULE**".

**Reason no safe repair was possible (canon check):**
- The World Bible defines a Seep's **"Rule"** as the anomaly's own governing behaviour: `03_SUPERNATURAL_SYSTEM.md` L13 — "Every Seep follows a **Rule** — alien, but fixed and discoverable"; L45 — "A Seep's Rule optimizes for informational symmetry…"; `02_WORLD_RULES.md` L25 — "Anomaly **Rules**…".
- The World Bible's anomaly-classification terminology is **Containment class (A–E)** and **Threat (T0–T5)** (`05_ANOMALY_CLASSIFICATION.md` L27–L29). It contains **no** "R-7"/"R-4" and **no** "response-protocol" term.
- The project-wide "R-7"/"R-4" in LOCK 9/LOCK 10 are **unrelated** — they are the LOCK 9 §18 coordinator **recommendation IDs** ("R-1–R-7"), not anomaly codes.
- The chapter's R-code filing/response system is established only at the **spec** level (`CHAPTER_004_GENERATION_SPEC.md` §6: "the archive's Rule index maps incident types to response protocols"), not in canon.
- Therefore canon provides **no term** for the R-code protocol system, and inventing one (or repurposing "Containment class"/"Threat") would violate the task constraints ("Do NOT invent a new classification system / new R-code meanings / new archive doctrine"). Per the task's instruction, the affected terminology was **left unchanged** and SF-2 is flagged as requiring a **separate canon/spec reconciliation**.

**Title:** left unchanged — no canon-supported minimal clarification exists.

**Net effect of SF-1 on SF-2:** the L86 "Filed under the wrong Rule" instance was removed, reducing (but not resolving) the "Rule"-as-protocol usage. Remaining instances: L10 "Rule index", L24 "Rule header", title. These await the canon/spec reconciliation.

## Canon sources consulted

`00_WORLD_BIBLE\01_CORE_PREMISE.md` (Seep definition) · `00_WORLD_BIBLE\02_WORLD_RULES.md` (Anomaly Rules) · `00_WORLD_BIBLE\03_SUPERNATURAL_SYSTEM.md` (Seep/Rule; Seep types) · `00_WORLD_BIBLE\05_ANOMALY_CLASSIFICATION.md` (Containment class / Threat) · `01_STORY_ARCHITECTURE\LOCK_9_ARC_I_ARCHITECTURE.md` (R-1–R-7 = recommendation IDs; C-01 Seal schedule) · `01_STORY_ARCHITECTURE\LOCK_10…` · `02_ACADEMY\00_DECISION_LOCK_ACADEMY.md` · `03_WRITING_ENGINE\GENERATION\CHAPTER_SPECS\CHAPTER_004_GENERATION_SPEC.md` §6.

## Verification results

| # | Check | Result |
|---|---|---|
| 1 | SF-1 resolved | **PASS** — the repeated causal clause at L86 is removed; zone-name beat kept; scene transition intact |
| 2 | SF-2 resolved via canon, or documented for reconciliation | **DOCUMENTED** — not safely repairable at prose level; flagged for separate canon/spec reconciliation |
| 3 | No unsupported terminology introduced | **PASS** — no SF-2 edit was made |
| 4 | Seep's "Rule" remains semantically distinct from R-7/R-4 | **PASS (unchanged)** — distinct in canon; chapter's R-code usage remains flagged |
| 5 | Zone-name beat intact | **PASS** — "East Beach Annex, Zone 11" retained (L86, L92, L108, L116) |
| 6 | No OPTIONAL passage changed (L10, L18, L94, L100, L114, L24) | **PASS** — none touched |
| 7 | No plot / chronology / POV change | **PASS** |
| 8 | Only CH004 was modified | **PASS** |

## Files modified

- `03_WRITING_ENGINE\GENERATION\CHAPTERS\004_THE_WRONG_RULE.md` (one bounded edit: L86)

## Files not modified

- CH001 (`001_ERROR_UNDEFINED.md`), CH002 (`002_NO_TAKERS.md`), CH003 (`003_NO_RANK_EFFECT.md`), CH005
- World Bible / all canon files; the Writing Engine
- `CHAPTER_004_GENERATION_SPEC.md`; `CH004_CONTINUITY_STATE.md`; all baselines
- All QA audit reports (only this repair report was created); all OPTIONAL passages

## Final status

**PASS** — SF-1 applied; SF-2 documented as requiring a separate canon/spec reconciliation (no safe prose repair possible without inventing terminology). No further bounded action available in this pass.
