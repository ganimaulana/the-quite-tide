# THE QUIET TIDE — CONSOLIDATED PROJECT

Single authoritative project root: **`C:\Project\QT_FULL\`**

> Consolidated 2026-09-23 (authoring date; in-universe year 2024). This README replaces the former root `README.txt`. It documents structure only — it does not duplicate canon.

## Structure

| Folder | Meaning |
|---|---|
| `00_WORLD_BIBLE\` | **Canonical world / source truth** (the numbered volumes `00_INDEX.md` … `38_MANIFEST.md`, plus `DATABASE\` and `AUDIT\`). |
| `01_STORY_ARCHITECTURE\` | **Story architecture** (arcs, pacing, locks `LOCK_9`…`LOCK_14`, long-term roadmap, foreshadow/payoff map). |
| `02_ACADEMY\` | **Academy-specific canon** (division system, timeline, EAR, Irregular classification/mechanics, doctrines, Academy entry). |
| `03_WRITING_ENGINE\` | **Writing and generation system** (the Writing Engine, Production Protocol, TNE gap analysis, calibration reports, `GENERATION\`, and the engine's internal audits). |
| `04_PROJECT_STATE\` | **Supporting design / state / proposals / decisions** (contracts, artifact, combat, characters, canon proposals, decisions, risks, integration, timelines, scratch). |
| `05_QA\` | **Project-level audits** (`AUDIT\500_QUESTION_AUDIT\`, this folder's migration reports). |

Active chapter prose lives at:

```
03_WRITING_ENGINE\GENERATION\CHAPTERS\
  001_ERROR_UNDEFINED.md
  002_NO_TAKERS.md
  003_NO_RANK_EFFECT.md
  004_THE_WRONG_RULE.md
  005_GENERATION_SPEC.md   (spec; chapters 006–020 not yet written)
```

Numbering: World Bible volumes keep their established `00–38` numbering; previously unnumbered documents received `NN_` prefixes within their folders; **LOCK_9…LOCK_14 and chapter files keep their semantic names unchanged**.

## Preserved invariants (summary — canon lives in the folders above)

- Daichi profile: Classification **IRREGULAR** · Division **OPERATIONS SUPPORT** · Curriculum **TBD** · Assignment **RECORDS & ARCHIVES** · Team **TBD** · Rank **F** · Ability **ERROR / UNDEFINED**. Conventionally Esper-weak; no secret power.
- Contract #1 = **THE POLITE KNOCK** / **PARTIAL**; Contract #2 = **UNDESIGNED**.
- 12 faces / 12 binding points; the 13th side is not Slot #13.
- `RESONANCE` ≠ XP · `DEPTH` ≠ XP · `CONTRACT` ≠ power/weapon · `KNOWLEDGE` ≠ skill.
- "Ledger"/"Brine" = **SUPERSEDED** (LOCK 12 AD-12-1/AD-12-2/AD-12-3).
- Timeline (universe): DOB 20 Sep 2006; Academy entry 1 Sep 2024 (age 17); EAR 4 Sep 2024; Contract #1 binding ~25 Sep 2024; Slot #2 end Nov 2024 (unlocks empty in Arc I).
- LOCK 1–14 remain design-layer locks (Academy, timeline, IO ladder, EAR, Irregular, Home/Joint Team, Contract #1, pacing/mission, character relationships, progression, arc stress test, final consistency).

## Notes

- `03_WRITING_ENGINE\GENERATION\QA\`, `03_WRITING_ENGINE\AUTHORITY_AUDIT\`, and `03_WRITING_ENGINE\PRODUCTION_AUDITS\` intentionally remain inside the Writing Engine (the engine is kept structurally intact). Project-level audits are in `05_QA\`.
- Non-Markdown tools are preserved at `04_PROJECT_STATE\TIMELINE_YEAR_SHIFT\` (`shift_tool.py`, `shift_result.json`, `shift_dryrun.json`).
- A pre-migration backup is retained outside the live root at `C:\Project\QT_FULL_PRE_MIGRATION_BACKUP\` (rollback source; not a second live project).
- Migration record: `05_QA\00_PROJECT_CONSOLIDATION_REPORT.md` and `05_QA\01_PROJECT_FILE_MAPPING.md`.
