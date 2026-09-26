# Final Natural English Refinement Report

**Date:** 2026-09-24
**Status:** FINAL NATURAL ENGLISH REFINEMENT COMPLETE — AWAITING AUTHOR REVIEW

---

## 1. Previous Calibration Findings

The calibration report (`NATIVE_ENGLISH_CALIBRATION_REPORT.md`) concluded:

> **CALIBRATION PASS WITH STYLE GAPS — ENGINE NEEDS ONE MORE REVISION**

It identified two remaining weaknesses requiring a style-only revision:

1. **Borderline literary patches** — literary patching and metaphor rules exist but could
   more explicitly require the Native Reading Test to outweigh cleverness when the surrounding
   register is literal. Two calibration samples illustrate the gap:
   - Sample 4 (Chapter 001, lines 82–86): extended `use/store/file/tray` metaphor chain that
     grows into author-shaped explanation; "the posting where the records lived" and the final
     tray sentence make the paragraph feel assembled around a clever analogy.
   - Sample 14 (Chapter 004, lines 98–118): measurable observation shifts into personified stone
     that "leaned toward a place it could not see," breaking the literal measurement register.

2. **Discourse / register shifts** — prose is individually understandable but shifts into
   aphorism or compressed thesis voice without clear transition. One calibration sample
   illustrates the gap:
   - Sample 15 (Chapter 004, lines 116–122): close-third past observation abruptly shifts to
     second-person `you` plus an aphoristic instruction, risking an inserted stylistic maxim
     rather than Arthur's continuous thought.

---

## 2. Exact Changes Made

All changes were applied to `THE_QUIET_TIDE_WRITING_ENGINE.md` only. No other files were
created or modified. No chapters, no canon, no locks were touched.

### A. New subsections added to Module 01 — NATIVE ENGLISH NATURALNESS GATE

Inserted immediately after the existing "Literary patching, metaphor, and earned observation"
section and before "Dialogue reconstruction":

| Section | Purpose |
|---|---|
| **LITERARY PATCH DETECTOR** | Defines the six-condition test for flagging a phrase as a literary patch: surrounding prose is plain, the phrase suddenly becomes metaphorical/abstract, adds no necessary information, sounds more "written," removing it preserves meaning, and it appears added for atmosphere. Required action: reconstruct the whole sentence in the same register, not just replace one phrase. |
| **REMOVAL TEST** | Provides a concrete procedure: temporarily remove a suspicious phrase and ask whether the paragraph loses necessary information, character voice, useful atmosphere, emotional meaning, or tactical information. If not, it is decorative. Explicitly NOT a blanket anti-description rule. |
| **REWRITE-IN-PLACE TEST** | Replaces the question "Can this sentence be made more literary?" with "Can this idea be expressed using the same language level as the sentences around it?" Includes the exact "punch clock" calibration example from the existing engine. |
| **REGISTER CONTINUITY TEST** | Defines stable scene registers (casual, family, peer conversation, military/institutional, technical, formal, internal/tactical, emotionally restrained) and lists exactly when a register change is justified (speaker, relationship, authority, situation, institutional document, deliberate character behavior) versus when it is not (author impressiveness, atmosphere, paragraph ending, model variation, TNE compression). Includes the "wrong date / fragile architecture" contrast example. |
| **PARAGRAPH REGISTER COHERENCE** | Establishes the evaluation hierarchy SENTENCE → PARAGRAPH → SCENE. Mandates that vocabulary, syntax, abstraction level, and rhythm belong to the same register within a paragraph. Flags individual sentences that feel more literary/formal/abstract/poetic than their neighbors for paragraph-level review. |
| **DIALOGUE REGISTER TEST** | Requires evaluating dialogue separately from narration using the four-question framework: WHO IS SPEAKING / WHO THEY SPEAK TO / RELATIONSHIP / SITUATION. Clarifies that different characters may use different registers but each individual must remain internally consistent. |
| **NARRATION REGISTER TEST** | For close-third POV, asks whether the prose sounds like the POV character's natural way of noticing the world. Affirms that Arthur can think analytically without every sentence sounding like an academic report. |
| **NATURAL ENGLISH PRIORITY ORDER** | Codifies the full priority order: NATURAL ENGLISH > CLEAR MEANING > CHARACTER/POV REGISTER > SCENE FUNCTION > RHYTHM > TNE STYLIZATION > LITERARY EFFECT. Explicitly states TNE influence is subordinate to natural English. |
| **PROTECT NATURAL STYLISTIC messaging appS** | Lists distinctive but natural prose that must NOT be overcorrected: short sentences, fragments, deadpan observations, dry humor, unusual but natural comparisons, character-specific phrasing, understated emotional lines, deliberate repetition. |

### B. New NPE checks added to Module 23 — Triple-Gate QA Protocol

Added after NPE-12 in the NATIVE PROSE EVALUATION checklist:

- **NPE-13:** Does any phrase feel inserted mainly to sound literary?
- **NPE-14:** Does the paragraph maintain a coherent language register?
- **NPE-15:** Does the dialogue fit the speaker, relationship, and situation?
- **NPE-16:** Does narration sound like the established POV rather than an author's commentary?

Added the repair-size requirement:

> A failure in NPE-13 or NPE-14 requires paragraph-level reconstruction.
> A failure in NPE-15 requires dialogue reconstruction.
> A failure in NPE-16 requires POV-level sentence reconstruction.

### C. Updated NATURAL PROSE RECONSTRUCTION paragraph in Module 23

Updated the production QA paragraph to:
- Include NPE-13, NPE-14, NPE-15, and NPE-16 in the list of checks requiring paragraph-level
  or thought-unit reconstruction.
- Add the calibration-report-mandated fail threshold: "When the Native Reading Test says the
  paragraph feels patched, a plausible POV metaphor is not enough to pass: reconstruct the
  thought-unit unless the register shift is clearly motivated."

---

## 3. Literary Patch Coverage

The two calibration samples flagged as borderline literary patches are now directly addressed:

| Sample | Issue | New Rule Coverage |
|---|---|---|
| Sample 4 (Ch 001, lines 82–86) | Extended metaphor chain (`use/store/file/tray`) that feels assembled around a clever analogy | **LITERARY PATCH DETECTOR** (conditions 1, 4, 5, 6 met); **REMOVAL TEST** (metaphor chain fails the natural-reading test); **REWRITE-IN-PLACE TEST** (the idea can be expressed in literal institutional language); **NPE-13** added as a production check |
| Sample 14 (Ch 004, lines 98–118) | Measurable observation breaks into personified stone metaphor | **REGISTER CONTINUITY TEST** (the personification breaks the literal measurement register without character/situation justification); **REMOVAL TEST**; **NPE-13** and **NPE-14** added as production checks |

---

## 4. Register-Shift Coverage

The one calibration sample flagged as a register/discourse shift is now directly addressed:

| Sample | Issue | New Rule Coverage |
|---|---|---|
| Sample 15 (Ch 004, lines 116–122) | Close-third past observation shifts to second-person `you` + aphoristic instruction | **REGISTER CONTINUITY TEST** (the second-person shift is not justified by speaker, relationship, authority, situation, or character behavior); **PARAGRAPH REGISTER COHERENCE** (the sentence feels more literary/formal than its neighbors — evaluates sentence → paragraph → scene); **REMOVAL TEST** (the aphorism is decorative); **NPE-14** and **NPE-16** added as production checks |

---

## 5. Preserved Rules

The following existing rules and sections remain **unchanged and intact**:

- All NATIVE ENGLISH NATURALNESS GATE subsections except the additions above
- NATIVE ENGLISH CHECK checklist (13 items) — unchanged
- All Module 01–22 operational rules and checklists
- Triple-Gate QA Protocol structure (Three Gates A/B/C) — unchanged
- All 12 existing NPE checks (NPE-01 through NPE-12) — unchanged
- The **A–F edit-response classification** — unchanged
- The **NATURAL → CLEAR → CHARACTER-APPROPRIATE → RHYTHM → CONCISION** hierarchy — preserved
  and now referenced by the new priority order
- All 7 seven additional audits (POV, Mystery-fence, Five-layer, Contract terminology,
  Hook-rotation, Anti-drift, Knowledge-provenance)
- Readability checkpoints (SOP §45)
- Gate rule and revision priority order

---

## 6. Protected Files

The following files were **NOT modified** during this revision:

| Category | Files |
|---|---|
| Chapters | CHAPTER 001, CHAPTER 002, CHAPTER 003, CHAPTER 004 |
| Canon / Locks | LOCK 1–14 |
| Canon documents | 37_FINAL_WORLD_BIBLE.md, academy architecture, character architecture |
| Contracts | Contract #1, Contract #2 status |
| Mystery | mystery fences, Locked Hybrids, LOCK 8 / LOCK 9 content |
| Style / SOP | FAST_PACE_DEEP_MYSTERY_RETENTION_SOP.md, NARRATIVE_STYLE_BIBLE.md |
| Gap Analysis | TNE_STYLE_GAP_ANALYSIS_FINAL.md |
| Other engine modules | All modules 02–23 unchanged |
| Calibration | NATIVE_ENGLISH_CALIBRATION_REPORT.md (source of truth, not modified) |
| Prose generation | No chapter files generated or rewritten |

---

## 7. Validation Results

| Check | Result |
|---|---|
| 1. Both identified gaps (literary patches, register shifts) directly addressed | **PASS** — LITERARY PATCH DETECTOR, REMOVAL TEST, REWRITE-IN-PLACE TEST cover patches; REGISTER CONTINUITY TEST, PARAGRAPH REGISTER COHERENCE, DIALOGUE REGISTER TEST, NARRATION REGISTER TEST cover register shifts |
| 2. No new contradiction introduced | **PASS** — all new rules explicitly defer to LOCK 1–14 and existing canon; new priority order places TNE stanchioning below natural English |
| 3. Existing Natural English rules remain intact | **PASS** — NATIVE ENGLISH CHECK, One-Read Test, Patch Detection, Native Reading Test, Vocabulary and Narration, Prose Quality Hierarchy, and all calibration examples unchanged |
| 4. TNE quantitative guidance remains intact | **PASS** — no new sentence-length quotas, paragraph quotas, metaphor quotas, vocabulary scores, percentages, or word-count rules introduced |
| 5. Controlled Hybrid POV remains intact | **PASS** — Module 02 (POV Engine) unchanged; no POV rules modified |
| 6. No chapter files changed | **PASS** — only THE_QUIET_TIDE_WRITING_ENGINE.md modified; no chapter files touched |
| 7. No baseline changed | **PASS** — no existing section rewritten or removed; only new subsections appended within Module 01 and new checks added to Module 23 |
| 8. No canon files changed | **PASS** — LOCK 1–14, Contract architecture, mystery fences, academy architecture all untouched |

---

## Final Status

**FINAL NATURAL ENGLISH REFINEMENT COMPLETE — AWAITING AUTHOR REVIEW**

This revision addresses exactly the two weaknesses identified by the calibration report:

1. **Borderline literary patches** → Resolved via LITERARY PATCH DETECTOR, REMOVAL TEST,
   REWRITE-IN-PLACE TEST, and NPE-13.
2. **Discourse / register shifts** → Resolved via REGISTER CONTINUITY TEST, PARAGRAPH REGISTER
   COHERENCE, DIALOGUE REGISTER TEST, NARRATION REGISTER TEST, and NPE-14/15/16.

No prose was generated. No Chapter 005 was created. No canon, lock, or chapter file was
modified.
