# THE QUIET TIDE — WRITING PRODUCTION PROTOCOL / CHAPTER REVISION PIPEmessaging app

**Status: LOCKED — AUTHOR APPROVED**
**Date: 2026-09-23**

> This document is LOCKED — AUTHOR APPROVED 2026-09-23. It is the authoritative chapter-production
> and chapter-revision workflow under the locked Writing Engine v1.0. It operationalizes locked
> rules. It creates no canon, modifies no lock, resolves no fence, and revises no chapter.
> It does NOT modify Writing Engine v1.0.

---

## 0. DOCUMENT IDENTITY AND AUTHORITY

### 0.1 What this document is

The Writing Production Protocol is the **OPERATIONAL CHAPTER-WORK PIPEmessaging app** of The Quiet Tide.
It tells an AI worker, step by step, how to take an existing chapter (or a future chapter draft)
and audit → plan → revise → validate it, without violating canon, locks, mystery fences,
power boundaries, POV architecture, or the Quiet Tide identity.

Every important behavior is stated as an executable instruction, not as advice.

### 0.2 What this document is NOT

- It is NOT canon. It does not create, change, or resolve story content.
- It is NOT a lock. It cannot override any lock or the Writing Engine.
- It does NOT modify LOCK 1–14.
- It does NOT modify FINAL_WORLD_BIBLE.
- It does NOT modify Writing Engine v1.0.
- It does NOT design future Contracts or resolve deferred mystery fences.
- It does NOT revise any existing chapter. No chapter prose changes are executed by this document.

### 0.3 Authority hierarchy (descending, binding)

1. **LOCK 1–14** — always wins on conflict. If any rule below contradicts a lock, the lock prevails.
2. **Existing Quiet Tide canon** (as carried by the locks).
3. **FAST_PACE_DEEP_MYSTERY_RETENTION_SOP.md** (Parts I–III, §§1–60).
4. **DATABASE/NARRATIVE_STYLE_BIBLE.md** (CANON-ADJACENT / EDITORIAL LOCK; subordinates itself to the SOP on overlap).
5. **TNE Style Gap Analysis** — `03_WRITING_ENGINE/TNE_STYLE_GAP_ANALYSIS_FINAL.md` (FINAL — SOURCE FOR WRITING ENGINE v1.0, 2026-09-23; 15 ADOPT / 46 ADAPT / 4 REJECT / 5 DEFER / 20 ALREADY CANON). Source document only: not canon, not a lock, does not override LOCK 1–14.
6. **WRITING ENGINE v1.0 — LOCKED — AUTHOR APPROVED 2026-09-23** — the authoritative writing-production layer. This protocol is subordinate to it. If any protocol instruction contradicts the engine, the engine prevails.
7. **THIS PROTOCOL** — the operational pipeline, below all of the above.

Authority inversion is a protocol-breaking violation: this protocol may never be used to argue
for overriding any of the six layers above it.

### 0.4 Canonical facts the protocol must never disturb

The following are carried from LOCK 1–14 and are restated here only as operational guards.
The protocol creates none of them and may change none of them:

- Contract #1 = **THE POLITE KNOCK**; outcome = **PARTIAL** (never upgraded).
- Contract #2 = **UNDESIGNED / UNDECIDED**. No future Contract mechanics may be invented to "fix" a weak chapter.
- 12 = maximum lifetime Contract capacity, not unlocked slots. No numeric unlock threshold.
- Lifetime Depth is cumulative and never decreases. Resonance = event/state; DEPTH = invocation resource.
- Arthur Reed: permanently **Rank F**; **Irregular** classification; **ERROR–UNDEFINED**; conventionally Esper-weak; no conventional Esper Ability. Competence never moves Rank or Classification. Victories are priced. Blind spots remain. "Weak by label but secretly strongest" is a master violation.
- POV = Controlled Hybrid POV (11-point spec): Close Third default; Arthur First Person loans selective; other-character Close Third only when structurally necessary; one scene = one POV consciousness; hard scene cuts; no head-hopping; no cosmetic switching; information-function test; sealed fences cannot be opened through POV loans. FP monopoly (V42) rejected in all forms.
- Mystery fences: 9/18 UNDETERMINED; Saito UNRESOLVED; Pram identity DEFERRED; Contract #2 UNDESIGNED; DEPTH gauge visibility DEFERRED; ERROR "strongest" interpretation fenced; LOCK 8 boundaries; incident/13th-face/previous-holder horizons. The protocol may guard them; it may never resolve them.
- Deferred TNE decisions: S1 (sentence-length numeric calibration), K28/D55 (typography conventions), I36 (permanent-open-loop policy), R73 (vulnerability-rationing formula), X3 (romance module). None may be resolved by chapter work.
- Romance = UNLOCKED / parked. No romance configuration may be added unless a canon or author decision permits it.

### 0.5 Objective

Design a repeatable pipeline for taking an existing chapter and producing a revised chapter that is:

- canon-safe
- continuity-safe
- mystery-fair
- readable
- fast-moving
- information-dense
- emotionally controlled
- compatible with Controlled Hybrid POV
- compatible with the TNE-derived mechanisms
- faithful to Quiet Tide's own identity
- compatible with the 30-chapter architecture

The pipeline supports BOTH:

- **A. Revision of existing chapters** (primary use).
- **B. Future drafting of new chapters** (operational variant; see §12 for the drafting adaptation).

This document designs both modes. It executes neither.

---

## 1. PIPEmessaging app STAGES 0–15

Each stage is defined by: **Purpose · Inputs · Checks · Outputs · Prohibitions.**

Stages 0–10 are the AUDIT + PLAN phase (read-only on the chapter except for recording).
Stage 11 is the EXECUTION phase (designed, not run here).
Stages 12–15 are the POST-REVISION QA phase (designed, not run here).

**Stage dependency rule:** no stage may be skipped. Stage 10 (revision plan) may not be
produced until Stages 0–9 are complete. Stage 11 may not begin until the Stage 10 plan is
author-approved (see §4). Stages 12–15 run in order after Stage 11.

---

### STAGE 0 — SOURCE FREEZE

**Purpose.** Capture the chapter's current state before any editing. Establish the
before/after baseline for the Stage 12 diff audit.

**Inputs.** The chapter file as it exists. Nothing else.

**Checks / recording.** Produce the Source Freeze Record, containing exactly:

- chapter number
- current title
- current word count (use `LC_ALL=C.UTF-8 wc -w`; the POSIX `wc -w` undercounts multibyte files)
- current scene count and, per scene, start/end markers
- POV per scene (Close Third / Arthur FP / other-character Close Third)
- characters present
- location(s)
- timeline position (date + position relative to LOCK 2 events)
- events (one line each, factual)
- anomalies present
- clues introduced
- questions opened
- questions answered
- consequences created
- canon dependencies (which LOCK / canon element each fact depends on)

**Outputs.** The Source Freeze Record. This record is the canonical "before" snapshot;
every later diff and audit compares against it.

**Prohibitions.** No editing. No improvement suggestions. No judgment about quality.
Recording is mechanical.

---

### STAGE 1 — CANON / LOCK AUDIT

**Purpose.** Verify the chapter does not contradict LOCK 1–14 or existing canon before any
stylistic work begins. A chapter cannot be made "better written" while it is canon-broken.

**Inputs.** Source Freeze Record + LOCK 1–14 files + relevant canon references.

**Checks.** Every recorded fact in the Source Freeze Record is checked against:

- LOCK 1–14 (each: no violation)
- L-28 Writing Engine v1.0 (as writing rules, never as canon claims)
- character canon (identity, age, Rank, classification, relationships, status)
- timeline (LOCK 2; event dates; age consistency — e.g., Arthur is 17 until 2024-09-20, 18 from 2024-09-20)
- Academy structure (Divisions, curriculum, Irregular classification mechanics)
- Division / curriculum / classification terminology (no "Irregular Division"; T1–T7 = Threat Tier; L3-T1–L3-T6 = institutional triggers)
- Home Team / Joint Team rules (Home Team ≠ Joint Team; joint teams temporary and mission-specific)
- Contract rules (slot cap 12 max; Contract #1 POLITE KNOCK / PARTIAL; no Contract #2 content; RESONANCE/DEPTH terminology; FULL/PARTIAL/FRAGMENT/FAILED; SOLVED is not a Contract outcome; lifetime Depth cumulative)
- anomaly rules (as carried by locks; no on-page contradiction of anomaly behavior)
- mystery fences (chapter does not resolve or reinterpret a fenced item)

**Outputs.** Per item: PASS, or REQUIRED REPAIR with the exact lock violated and the
exact factual conflict. Chapter-level verdict: **PASS** or **REQUIRED REPAIR**.

**Prohibitions.** Never silently repair a canon contradiction. A contradiction must be
surfaced as REQUIRED REPAIR with its lock citation, never quietly rewritten. If the
contradiction can only be resolved by an author decision (e.g., an event contradicts a
locked event), it is escalated as AUTHOR DECISION REQUIRED, not "fixed."

---

### STAGE 2 — CHAPTER FUNCTION AUDIT

**Purpose.** Determine what the chapter actually does in the architecture before deciding
what it should become.

**Inputs.** Source Freeze Record.

**Checks.** Identify:

- primary narrative function (one sentence)
- secondary functions (as many as real)
- state changes (every tracked state that moves; a chapter should change at least one tracked state per the locked Chapter Engine)
- information gained (reader, Arthur, other characters — separately)
- information lost (access, cover, advantage)
- relationship movement (each significant relationship: direction and magnitude)
- institutional movement (academy, Division, team, record)
- anomaly movement (status change of any anomaly)
- mystery movement (questions opened/answered; clue progress)
- consequences created (cost paid, debt incurred, setup planted)
- next-chapter setup (what this chapter hands forward)

**Outputs.** The Function Ledger. Chapter-function verdict: FUNCTIONAL or
**FLAGGED — NO MEANINGFUL STATE CHANGE**.

**Prohibitions.** A chapter with no meaningful state change must be flagged, not
automatically deleted. Deletion is a structural decision with architectural consequences
(timeline, pacing of 30 chapters, question debt); it is never automatic. The flag and its
options (compress, merge, restructure, rebuild) become inputs to Stage 10, where the
author decides.

---

### STAGE 3 — SCENE MAP

**Purpose.** Decompose the chapter into its working units before any prose is touched.

**Inputs.** Source Freeze Record.

**Checks.** For each scene, record:

- POV
- immediate situation
- want / function (what the scene is trying to do)
- information asymmetry (who knows what, who doesn't)
- conflict / friction (real conflict, not decoration)
- key beat sequence (5–10 beats maximum per scene)
- turn (what changes inside the scene)
- decision (who decides what)
- consequence (cost paid or debt incurred)
- exit condition (why the scene ends here)
- questions opened
- questions answered
- clues introduced
- clues paid off
- character movement (who moved emotionally, relationally, or positionally)

**Outputs.** The Scene Map, with each scene classified:

- **KEEP** — scene works; prose-level improvement only
- **COMPRESS** — scene's function survives at reduced length
- **RESTRUCTURE** — scene's function survives with reordered beats or changed entry/exit
- **REPLACE** — scene's function must be re-executed by a materially different scene
- **REMOVE** — scene has no surviving function and its removal does not strand downstream dependencies

**Prohibitions.** No rewriting. Classification is judgment about function, not prose quality.
REMOVE requires a downstream-dependency check: nothing later in the 30-chapter arc may
depend on information, consequence, or setup that only this scene provides.

---

### STAGE 4 — POV AUDIT

**Purpose.** Apply the LOCKED Controlled Hybrid POV rules (Writing Engine Module 02,
the 11-point spec) to every scene before any prose change.

**Inputs.** Scene Map.

**Checks.** For every scene:

1. What consciousness owns the scene?
2. Is Close Third sufficient? (Apply the Close-Third Test: if yes, First Person may not be used.)
3. If First Person is used, does the Close-Third Test fail — i.e., does subjective processing materially improve the scene?
4. If another character's POV is used, what structurally necessary information is unavailable to Arthur? (Information-function test; name it exactly.)
5. Is there any head-hopping — any paragraph, line, or sentence that shifts consciousness without a hard scene cut?
6. Is every POV switch executed with a hard scene cut?
7. Is every POV switch functional rather than cosmetic?
8. Does the scene touch a sealed mystery fence through an illegal POV loan? (A POV loan can never open a sealed fence; attempted access is a violation.)

**Outputs.** Per scene: POV PASS or REPAIR REQUIRED with the exact rule violated.
Chapter-level: **POV PASS** or **REPAIR REQUIRED**.

**Prohibitions.** Do not "fix" POV by converting a scene to first person for flair.
Do not allow a POV loan to carry information Arthur could not legitimately possess.
Do not use a POV switch to manufacture a mystery resolution or emotional shortcut.

---

### STAGE 5 — INFORMATION / MYSTERY AUDIT

**Purpose.** Verify the chapter's information handling is fair, provenance-clean, and
fence-safe.

**Inputs.** Scene Map + POV audit results.

**Checks.**

**Knowledge layers.** For each major information item, record the four-layer state:

- reader knows
- Arthur knows
- other character(s) know
- unknown

**Provenance chain.** For each major information item, determine:

- SOURCE (where the information came from)
- ACQUISITION (how it entered a character's possession — observed, told, deduced, documented)
- INTERPRETATION (what the character concluded, and whether the conclusion is warranted)
- CONSEQUENCE (what changed because of it)

**Mystery grammar.** Where the chapter performs investigation, apply the locked grammar
(OBSERVATION → HYPOTHESIS → TEST → RESULT → UPDATED HYPOTHESIS → SECOND TEST →
RESOLUTION / FAILURE) and verify the on-page sequence matches it.

**Fair-play checks:**

- no narrative fiat (a conclusion appears without its supporting sequence)
- no artifact whisper (an object "communicates" what it has no mechanism to communicate)
- no unexplained intuition (a character knows what they could not know)
- no retroactive omniscience (a later conclusion rewrites what was legitimately knowable earlier)
- no hidden information Arthur should not possess
- no artificial withholding of an on-page solve (a LOCK-mandated on-page solve, e.g. the
  Chapter 11 genuine solve, may not be converted into a permanent mystery for suspense)
- no accidental resolution of a mystery fence

**Outputs.** The Information Ledger with per-item provenance chains, fair-play verdicts,
and the knowledge-layer map. **MYSTERY PASS** or **REPAIR REQUIRED**.

**Prohibitions.** Withholding the center while showing the edges (I38) is the approved
discipline; withholding to conceal information Arthur legitimately acquired is a
violation. Never resolve a fence to "improve" a chapter's mystery.

---

### STAGE 6 — PACING / MOVEMENT AUDIT

**Purpose.** Verify the chapter moves at Quiet Tide pace: fast locally, deep globally —
per the locked Writing Engine (Modules 05, 06).

**Inputs.** Scene Map.

**Checks.**

- The opening enters with a meaningful situation (Writing Engine Module 06 opening rules).
- Unnecessary setup is identified for removal.
- Friction appears early when the scene's function requires it (C21 calibration:
  a friction signal within approximately the first 3–5 sentences when naturally possible;
  never a mandatory formula; never forced into ordinary-life scenes, quiet investigation,
  deliberate orientation, aftermath, or inherently non-confrontational scenes).
- Decisions replace unnecessary reflection.
- Consequences remain visible on-page.
- Transitions do not become bridge prose; meaningful time jumps get a declared temporal
  marker (PC30), ordinary transitions are not eliminated to imitate TNE.
- Ordinary-life material is retained when it is functionally load-bearing (contrast,
  characterization, recovery, relationships, consequences, emotional processing, world
  texture — per the locked engine).
- No two adjacent scenes repeat the same movement pattern without function.

**Outputs.** Pacing verdict: **PACING PASS** or **REPAIR REQUIRED** with per-scene notes.

**Prohibitions.** Do NOT force a cliffhanger. Do NOT force first-person. Do NOT force
a question. Do NOT force a scene count. K27 (terminal-hook absolutism) is permanently
excluded; the 12-ending-type rotation remains.

---

### STAGE 7 — PROSE / READABILITY AUDIT

**Purpose.** Verify prose readability per the locked Writing Engine (Modules 03, 04, 22)
and the SOP §39 10–20 word band as a default, not a rigid restriction.

**Inputs.** The chapter's prose (read, not rewritten).

**Checks.**

- simple English, not simple writing
- natural English phrasing
- complete meaning in each sentence
- minimal mental reconstruction required of the reader
- concrete verbs over abstract nominalization
- controlled modifiers (no modifier pileups)
- readable paragraph shapes
- dialogue clarity (attribution, voice separation, subtext)
- limited jargon; institutional terms only where canon establishes them
- tactical thought clarity (the preferred QUESTION → INFERENCE → OPTIONS → DECISION
  grammar as a default, not a mandatory shape; every thought beat must do work)
- description filtered through the scene's POV consciousness
- exclamation rationing per S8 (tension register, not default punctuation; no quota)

**Outputs.** Readability verdict: **PROSE PASS** or **REPAIR REQUIRED** with concrete
examples (line references, not rewrites).

**Prohibitions.** Do NOT optimize toward TNE's ~8.7-word average. Do NOT make prose
mechanically staccato. Do NOT imitate the TNE surface voice. Do NOT "prettify" prose
without a functional reason (see §2, revision safety).

---

### STAGE 8 — CHARACTER / EMOTION AUDIT

**Purpose.** Verify character behavior, emotional processing, and power boundaries.

**Inputs.** Scene Map + Information Ledger.

**Checks.**

- character agency (characters act; they are not moved by the plot)
- behavior > explanation (show first, explain only when the engine permits)
- reactions are earned (the setup exists on-page)
- emotional processing is controlled (Module 12 rules; H67/H69 comedy rules as QT wording)
- no artificial melodrama
- no emotional reset after major consequences (consequences persist)
- contempt/presentation dynamics remain within the locked model
- victories carry cost (priced wins)
- blind spots remain (Arthur is not retroactively made perceptive everywhere)
- relationships actually move (or their stasis is meaningful and noted)
- Arthur power boundaries: no hidden ability, no sudden combat competence, no
  competence that moves Rank, no "secretly strongest" framing, no omniscience drift

**Outputs.** Character verdict: **CHARACTER PASS** or **REPAIR REQUIRED**.

**Prohibitions.** Do not add romance unless canon or an author decision permits it
(romance is UNLOCKED / parked; X3 deferred). Do not heal a relationship, resolve a
conflict, or grant a victory to make a chapter "feel better" — consequences are
load-bearing.

---

### STAGE 9 — WORLD / INSTITUTION AUDIT

**Purpose.** Verify institutional and world accuracy, and that worldbuilding is delivered
through the locked channels, not exposition dumps.

**Inputs.** Scene Map + Source Freeze Record.

**Checks.**

- Division (names, behavior, jurisdiction)
- Curriculum (Intelligence Operations as curriculum; correct placement)
- Classification (Irregular classification mechanics; no invented classifications)
- Home Team doctrine (permanent team) vs. Joint Team doctrine (temporary, mission-specific)
- Academy mission structure and institutional behavior
- anomaly handling procedures as canon establishes them
- documentation and records (the institutional trace: consequence → document/report →
  dialogue → concise narration)

**Worldbuilding-delivery check.** Worldbuilding should appear through consequence,
document/report, dialogue, and concise narration — in that preference order. Institutional
behavior over exposition dumps. A paragraph that explains the world to the reader
without any character or institutional need is flagged.

**Outputs.** World verdict: **WORLD PASS** or **REPAIR REQUIRED**.

**Prohibitions.** Do not invent institutional detail to "enrich" a chapter. Do not
promote a background rule into a foreground plot device unless the revision plan
identifies a canon-safe reason. Do not resolve a deferred institution (e.g., anything
depending on S1/K28/I36/R73 typography or gauge decisions).

---

### STAGE 10 — REVISION PLAN

**Purpose.** Convert all audit findings into a single executable, traceable plan.
This is the last stage that may run without author approval of its own output.

**Inputs.** All outputs of Stages 0–9.

**Prerequisite.** Stages 0–9 must be complete. A revision plan may not be drafted from
a partial audit.

**Format.** Every proposed change is one plan item with exactly these fields:

- **CHANGE ID** — unique identifier (e.g., `CH07-03-01`: chapter 07, scene 03, item 01)
- **LOCATION** — scene and line range
- **CURRENT PROBLEM** — what is wrong, with evidence
- **PROPOSED CHANGE** — what to change, concretely
- **PURPOSE** — which audit finding this serves
- **AUTHORITY** — the locked rule that authorizes it (LOCK number / engine module /
  SOP section). A change with no authority may not be proposed.
- **RISK** — what could go wrong (canon impact, fence proximity, dependency impact)
- **EXPECTED EFFECT** — the concrete improvement predicted

**Classification.** Every item is classified:

- **CANON-SAFE** — prose, pacing, structure, or information-delivery change with no
  canon impact (e.g., compress a bridge paragraph, sharpen a dialogue exchange).
- **CANON-SENSITIVE** — touches an event, fact, timeline, relationship state, or
  institutional behavior (e.g., move an event's time, change who witnesses an anomaly).
  Canon-sensitive items require the Stage 13 re-audit to pass before the chapter can
  reach AUTHOR REVIEW.
- **AUTHOR DECISION REQUIRED** — anything that would resolve a fence, create canon,
  change a locked event, design a Contract, configure romance, or otherwise exceed
  the locked authority. Such items are proposed for decision, never executed by default.

**Outputs.** The Revision Plan. Chapter state moves to **PLAN READY** only when the plan
is complete and every item has a classification.

**Prohibitions.** Do not execute changes. Do not bundle multiple unrelated changes into
one item to hide a canon-sensitive change inside a canon-safe one. Do not propose a
change whose authority is "it reads better" — authority must cite a locked rule.

---

### STAGE 11 — DRAFT REVISION (DESIGNED, NOT EXECUTED)

**Purpose.** Execute the author-approved Revision Plan, and only the approved plan.

**Prerequisite.** The Revision Plan has been reviewed and its execution authorized by
the author. Unauthorized execution is a protocol violation.

**Rules of execution:**

- Preserve locked events unless the revision plan explicitly identifies a continuity
  repair (and that repair is CANON-SENSITIVE with a cited lock authority).
- Preserve character identity.
- Preserve mystery fences.
- Preserve chronology.
- Preserve Contract boundaries.
- Preserve chapter architecture (the chapter's place in the 30-chapter arc).
- Change prose only when it improves function.
- Avoid cosmetic rewriting: if a sentence already does its work, it stays.
- Do not add a new subplot merely to improve prose.
- Do not solve a weak chapter by inventing canon: a weak chapter is fixed by structure,
  movement, information, and prose — never by adding story content the locks did not
  authorize.
- Every substantive change must map back to an approved revision-plan item. A change
  with no plan item is a protocol violation.

**Outputs.** The revised chapter draft + an execution log mapping each substantive
change to its CHANGE ID.

**Prohibitions.** No plan-item invention during execution. If execution reveals a problem
the plan did not cover, stop and return the chapter to PLAN READY with a plan amendment
for author review — do not improvise.

---

### STAGE 12 — DIFF AUDIT

**Purpose.** Make the revision transparent and auditable against the Source Freeze Record.

**Inputs.** Source Freeze Record (Stage 0) + revised draft + execution log.

**Checks.** Report, as exact figures and item lists:

- word count delta (before → after)
- scene delta (scenes added / removed / merged / split)
- POV delta (any scene whose POV changed, and why)
- event delta (events added / removed / moved)
- information delta (questions opened/answered, clues introduced/paid — before → after)
- character delta (who appears/disappears; relationship-state changes)
- canon-sensitive changes (every CANON-SENSITIVE plan item, with its resolution)
- deleted material (what was removed, per REMOVE/REPLACE classification)
- added material (what was added, and which plan item authorized it)

**Outputs.** The Diff Report. Any delta without an authorizing plan item is flagged as
an unauthorized change and must be reverted or escalated.

**Prohibitions.** No silent deltas. "Improved" material that cannot be traced to a plan
item is treated as an error, not an enhancement.

---

### STAGE 13 — LOCK / CONTINUITY AUDIT

**Purpose.** Re-verify the revised chapter against the full lock and canon stack.
This is the second canon gate; the chapter may not proceed to author review without it.

**Inputs.** Revised draft + Diff Report.

**Checks.** Re-run, in full, against the revised text:

- LOCK 1–14 (every lock)
- L-28 Writing Engine v1.0 (writing rules, as rules)
- timeline consistency
- character canon consistency
- mystery ledger (question debt accounting; debt ceiling respected; no fence opened)
- Contract ledger (Contract #1 boundaries; no Contract #2 content; no slot/depth terminology drift)
- Academy mission architecture consistency

**Outputs.** **LOCK PASS** or **REQUIRED REPAIR**. No silent contradiction is allowed:
any contradiction found here returns the chapter to REPAIR REQUIRED with the exact
conflict cited.

**Prohibitions.** Never waive a lock finding because "the prose is better now."
A chapter that fails Stage 13 may not reach Stage 15.

---

### STAGE 14 — WRITING ENGINE QA

**Purpose.** Run the locked Writing Engine's own checks against the revised chapter,
as the engine itself defines them.

**Inputs.** Revised draft.

**Checks.** Per Writing Engine v1.0 (do not reinterpret; run the engine's own
detection checklists):

- POV (Module 02 checklist)
- readability (Modules 03, 04, 22)
- information movement (Module 07)
- mystery fair play (Module 08)
- pacing (Modules 05, 06)
- dialogue (Module 09)
- internal thought (Module 10)
- action (Module 11)
- emotion (Module 12)
- description (Module 13)
- worldbuilding (Module 14)
- anti-cloning (the four REJECTs + the ten negatives — no 8.7 target, no mandatory
  cliffhanger, no FP monopoly, no ordinary-life deletion, no TNE action grammar,
  no TNE personality imitation, no TNE romance graft, no system-UI requirement)
- anti-formula (no accidental mandatory patterns — see §10)
- Arthur power boundaries (no hidden ability, no sudden competence, priced wins,
  blind spots, Rank F immobility)

**Outputs.** Engine QA report: per-area PASS / REPAIR NOTE.

**Prohibitions.** Do not "tune" the engine to pass. The engine is locked; a chapter
that fails an engine check is revised, not the check.

---

### STAGE 15 — FINAL CHAPTER QA

**Purpose.** Classify the chapter's final disposition.

**Inputs.** All stage outputs.

**Classification.** Exactly one of:

- **PASS** — chapter is ready for AUTHOR REVIEW.
- **MINOR REPAIR** — small, canon-safe fixes remain; return to REVISION IN PROGRESS
  with a bounded repair list (no new plan required, but the repair list is recorded).
- **MAJOR REPAIR** — structural or canon-sensitive issues remain; return to
  REPAIR REQUIRED → REVISION IN PROGRESS with a plan amendment.
- **AUTHOR DECISION REQUIRED** — the chapter needs an author decision (fence, canon,
  romance, Contract, locked event). **Stop.** Do not automatically revise again.

**Prohibitions.** Do not automatically revise again after a QA classification. Each
revision cycle must be explicitly re-authorized or bounded by the classification above.

---

## 2. REVISION SAFETY — THE HARD PREVENTION LIST

The protocol must explicitly prevent the following. Each is a named violation class;
any occurrence during any stage is a hard stop for that chapter's pipeline:

1. **Accidental canon creation** — any new story fact introduced without a canon
   authority and without an author decision.
2. **Accidental power escalation** — any change that makes Arthur (or any character)
   more capable than the locks allow, however subtly (competence creep, cost removal,
   blind-spot removal).
3. **Accidental Contract design** — any invented Contract mechanic, slot, resonance
   behavior, or depth behavior beyond LOCK 8/12.
4. **Accidental mystery resolution** — any fence resolved, reinterpreted, or "softly
   answered" through prose, POV, dialogue, or documentation.
5. **Accidental romance insertion** — any romantic configuration added while romance
   remains UNLOCKED / parked and X3 deferred.
6. **POV head-hopping** — any consciousness shift without a hard scene cut.
7. **TNE surface imitation** — any import of TNE rhythm, voice, persona, or surface
   device not classified ADOPT/ADAPT in the gap analysis.
8. **Chapter formula repetition** — the same opening mode / movement / ending type /
   beat shape repeated mechanically across chapters (see §10).
9. **Deletion of functional ordinary life** — ordinary-life material removed merely
   because it "slows" the chapter, when the Stage 2/6 audits found it load-bearing
   (PC32 rejected permanently).
10. **Exposition inflation** — worldbuilding added as explanation rather than
    delivered through consequence, document, dialogue, or concise narration.
11. **Prose beautification without function** — rewriting that improves sound without
    improving a function identified in an audit stage.
12. **Changing locked events for readability** — altering what happens because the
    new version "reads better." Locked events are preserved; only the telling may change.

---

## 3. CHAPTER REVISION STATES — STATE MACHINE

### 3.1 States

- **UNTOUCHED** — chapter exists; no pipeline work has begun.
- **AUDITED** — Stages 0–9 complete; audits recorded.
- **PLAN READY** — Stage 10 complete; Revision Plan exists and is complete.
- **AUTHOR DECISION REQUIRED** — a decision gate is open; pipeline is stopped.
- **REVISION IN PROGRESS** — Stage 11 executing an authorized plan.
- **REPAIR REQUIRED** — a QA or audit gate failed; bounded repair defined.
- **REVISION COMPLETE** — Stage 11 finished; execution log complete.
- **QA** — Stages 12–15 running.
- **AUTHOR REVIEW** — chapter and all reports submitted to the author.
- **APPROVED** — author approved. Terminal state.

### 3.2 Transitions

```
UNTOUCHED
  → AUDITED                    (Stages 0–9 complete)

AUDITED
  → PLAN READY                 (Stage 10 complete)
  → AUTHOR DECISION REQUIRED   (audit surfaced a canon/fence/Contract/romance decision)

PLAN READY
  → REVISION IN PROGRESS       (author authorized execution of the plan)
  → AUTHOR DECISION REQUIRED   (plan contains items awaiting author decision)

REVISION IN PROGRESS
  → REVISION COMPLETE          (Stage 11 finished; execution log complete)
  → AUTHOR DECISION REQUIRED   (execution revealed an unplanned problem)

REVISION COMPLETE
  → QA                         (Stages 12–15 begin)

QA
  → AUTHOR REVIEW              (Stage 15 = PASS)
  → REPAIR REQUIRED            (Stage 15 = MINOR REPAIR or MAJOR REPAIR)
  → AUTHOR DECISION REQUIRED   (Stage 15 = AUTHOR DECISION REQUIRED)

REPAIR REQUIRED
  → REVISION IN PROGRESS       (bounded repair list authorized)

AUTHOR REVIEW
  → APPROVED                   (author approves)
  → REPAIR REQUIRED            (author requests changes)

AUTHOR DECISION REQUIRED
  → STOP                       (terminal until the author decides; the author's decision
                                determines the next state)

APPROVED
  → (terminal; no further transitions)
```

**State integrity rule:** a chapter's current state must always be known and recorded.
A chapter may never be in two states, and may never transition backward except through
the explicit REPAIR REQUIRED path.

---

## 4. AUTHOR APPROVAL GATE

### 4.1 What the worker may do

- audit (Stages 0–9)
- analyze (all audit outputs)
- propose (Stage 10 revision plan)
- revise **only after authorized execution** (Stage 11, only when the author has
  authorized the specific plan)

### 4.2 What the worker may NOT do

- decide canon
- resolve fences
- invent Contract #2
- decide romance
- change locked character architecture
- silently rewrite story direction
- execute a revision plan without explicit author authorization
- treat a QA classification as authorization for another revision cycle

### 4.3 Gate locations

Author authorization is required at exactly two gates:

1. **PLAN → EXECUTION GATE** — the Stage 10 Revision Plan must be approved before
   Stage 11 begins.
2. **FINAL APPROVAL GATE** — the chapter at AUTHOR REVIEW may only reach APPROVED
   by author approval.

Everything else (audits, plans, diffs, QA reports) is worker-executed and worker-reported.

---

## 5. MULTI-PASS REVISION — PASS DESIGN

The conceptual passes map onto the pipeline stages. They are **sequential by default**,
because each pass's output is the next pass's input, and because canon safety must be
established before structure is touched and structure before prose.

| Pass | Name | Stages | Sequential? | Notes |
|---|---|---|---|---|
| A | Canon / continuity | 0–1 | Always first, always standalone | No later pass may begin until Stage 1 = PASS or its REQUIRED REPAIR items are resolved/decided. |
| B | Structure / movement | 2–3, 6 | Sequential after A | Function audit (2) informs the scene map (3); pacing (6) reads the map. May run as one working session. |
| C | Information / mystery | 4–5 | Sequential after B (scene-dependent) | POV (4) and information (5) are scene-granular; they require the Stage 3 map. Combined into one pass to avoid re-reading each scene twice. |
| D | POV / prose | 7 (prose read) | Sequential after C | Prose readability is audited, never rewritten, in this pass. |
| E | Character / emotion + World / institution | 8–9 | Sequential after D; 8 and 9 combined | Both read the scene map; running them together avoids a second full-chapter read. |
| F | Plan + final QA | 10–15 | Sequential after E; execution (11) gated | Stage 10 is the pass output; Stages 11–15 are the gated execution and QA cycle. |

**Conditional combination rule.** Passes B+C may be combined into a single scene-granular
working session when the chapter is short (≤3 scenes), because all three read the same
scene map. Passes D+E may always be combined for the same reason. Pass A may never be
combined with any later pass: canon safety is the foundation, and its verdict must be
known before any structural judgment is made.

**Redundant-read rule.** The chapter file is read in full exactly twice per cycle:
once for the Source Freeze (Stage 0) and once for the Stage 11 execution baseline.
All audit stages read from the Source Freeze Record and Scene Map, not from the raw
file — except when a stage must verify a quoted line, in which case it cites the line
and moves on. This is deliberate: it keeps the audits anchored to recorded facts
instead of drifting impressions.

---

## 6. CHAPTER-SCALE TARGETS (LOCKED ENGINE CONSTRAINTS)

These targets are carried from Writing Engine v1.0 Modules 06 and 01. The protocol does
not set them; it applies them exactly as the engine defines them — as constraints
and calibrations, never as mandatory formulas:

- approximately **1,800–2,500 words** per chapter (QT-native band; not the TNE 8.7-word average)
- typically **2–4 scenes** (not mandatory)
- **≥1 meaningful state change** per chapter (tracked-state movement; Stage 2 verifies)
- **12 ending types** available in rotation (K27 terminal-hook absolutism rejected)
- **no mandatory cliffhanger**
- **no mandatory question**
- **question debt ≤3 by Chapter 30** (debt ceiling with budgeted horizons)
- **ordinary-life scenes allowed when functionally load-bearing** (SOP §15; PC32 rejected)

A chapter outside the word band or scene range is flagged for review, not automatically
failed — the engine defines these as writing constraints/calibrations, and the protocol
respects that definition.

---

## 7. ANTI-FORMULA TEST

**Purpose.** Prevent mechanical repetition across chapters while allowing functional
repetition.

**Method.** For each chapter under revision, compare against the **previous three
chapters** where available, on ten dimensions:

1. opening mode
2. dominant movement
3. POV pattern
4. information delivery
5. conflict type
6. anomaly presence
7. emotional register
8. ending type
9. scene rhythm
10. decision/consequence pattern

**Judgment rule.** Flag sequences where **three or more dimensions repeat identically
across three consecutive chapters** without a functional reason. Do NOT reject
repetition merely because a structural pattern repeats: determine whether the
repetition is **functional** (the story requires the same shape — e.g., a run of
institutional briefings during an arc's procedural phase) or **mechanical** (the
same shape used because it is easy). Functional repetition is kept; mechanical
repetition becomes a Stage 10 plan item (RESTRUCTURE or REPLACE at the scene level).

The anti-formula test runs at Stage 6 (pacing audit) and is re-verified at Stage 14.

---

## 8. DRAFTING MODE — NEW-CHAPTER ADAPTATION

The pipeline supports future drafting of new chapters (mode B) with these adaptations:

- **Stage 0** becomes the **Draft Freeze**: the draft is frozen as the baseline the
  moment drafting stops; all later stages read the freeze.
- **Stage 1** runs identically (canon/lock audit of the draft).
- **Stage 2** runs identically, with one addition: the draft must declare its intended
  function **before** the audit (the draft's own statement of purpose becomes the first
  thing the audit checks against reality).
- **Stages 3–9** run identically on the draft.
- **Stage 10** becomes the **Draft Improvement Plan** (same fields, same classifications).
- **Stage 11** executes the improvement plan (same rules; "preserve locked events"
  applies to any locked event the draft touches).
- **Stages 12–15** run identically.

No chapter — revised or drafted — reaches APPROVED without passing Stage 13 and
Stage 14.

---

## 9. HARD-STOP CONDITIONS

The pipeline stops immediately (chapter state → AUTHOR DECISION REQUIRED → STOP) when
any of the following occurs:

1. A canon contradiction is found that cannot be repaired within the locks.
2. A revision would require resolving a mystery fence.
3. A revision would require designing Contract #2 or any new Contract mechanic.
4. A revision would require configuring romance.
5. A revision would change a locked event, a locked character fact, or locked
   institutional architecture.
6. A revision would resolve a deferred TNE decision (S1, K28/D55, I36, R73, X3).
7. A POV loan is found to touch a sealed fence.
8. An engine check fails and the failure cannot be repaired without violating a lock.
9. The author has not authorized Stage 11 execution.
10. Stage 15 classifies the chapter AUTHOR DECISION REQUIRED.

A hard stop is never overridden by schedule, by "it reads better," or by any
lower authority.

---

## 10. WHAT THIS PROTOCOL DOES NOT DO

For the avoidance of doubt:

- It does not revise any chapter.
- It does not create canon.
- It does not modify LOCK 1–14.
- It does not modify Writing Engine v1.0.
- It does not modify FINAL_WORLD_BIBLE.
- It does not lock itself (it was locked by explicit author approval 2026-09-23; status is LOCKED — AUTHOR APPROVED).
- It does not resolve deferred decisions.
- It does not design Contract #2.
- It does not configure romance.
- It does not override any of the six authority layers above it.

---

*End of DRAFT — Writing Production Protocol / Chapter Revision Pipeline.*
