# THE QUIET TIDE — CH001–CH042 CONTRACT UI / CONSISTENCY AUDIT

**Audit date:** 2026-09-25
**Scope:** CH001–CH042
**Authority:** `00_WORLD_BIBLE/39_CONTRACT_SYSTEM.md`
**UI presentation rule:** horizontal ASCII borders only; no vertical `|`; no Markdown code fences.

## 1. Executive Result

**STATUS: PASS WITH REPAIRS**

The chapter set was audited for Contract UI formatting, Contract/System terminology, active-slot logic, artifact/Contract separation, Motion Sense separation, and Academy ERROR separation.

### Format result
- No ` ```text ` / Markdown code fences remain in CH001–CH042.
- No vertical `|` UI borders remain in CH001–CH042.
- No `===` UI borders remain in CH001–CH042.
- Contract UI now uses horizontal borders only where a UI block is present.
- UI remains concise and does not use RPG stat fields.

### Canon result
The most important inconsistency was the old **12-seat / 12-slot interpretation of the artifact**. Current canon defines **6 maximum active Contract slots**, while the stone/artifact may physically contain twelve hollows. These are now treated as separate layers.

## 2. Current Canon Applied

### Contract UI
- Private to Daichi.
- Minimal information interface.
- Not an RPG status screen.
- No STR/DEX/INT, HP/MP/stamina, levels, generic EXP, rarity, or generalized damage values.
- UI may report known Contract state, integration, restrictions, discovered conditions, and Contract-specific progress.
- UI does not explain the Academy ERROR/UNDEFINED mystery.

### Active Contract capacity
- **Hard maximum: 6 active Contract slots.**
- Slot expansion is not a normal progression mechanic.
- Clearing a slot does not automatically destroy the Contract.
- Contract slots belong to the private Contract System, not automatically to the physical artifact.

### Artifact / stone
- The artifact/stone is not the source of the Contract UI.
- Its physical hollows/markers are a separate mystery layer.
- A physical marker changing must not be described as proof that the artifact contains twelve Contract slots.

### Motion Sense
- Natural/inherent ability.
- Not a Contract.
- Not precognition.
- UI must keep it separate from Contract-derived effects.

## 3. Repairs Applied

### CH016 — THE CORRECTION LOOP
- Replaced the stale wording that the "Seal" directly gave Daichi the confirmed sentence.
- Contract #1 is now the source of the Contract sentence in prose.
- Added a private Contract UI after Daichi's methodological audit.
- UI reports THE POLITE KNOCK as PARTIAL and separates known/unknown information.

### CH017 — SLOT-CAP FAIR-PLAY
- Preserved the artifact's twelve physical hollows.
- Removed the interpretation that the twelve hollows are twelve Contract seats.
- Added explicit uncertainty between physical artifact markers and private Contract capacity.
- Added private UI showing **1 / 6 ACTIVE**.
- UI does not mention the artifact's twelve hollows.

### CH030 — END-I: SLOT 2 AND THE HOOK
- Academy gauge wording no longer claims to measure a private Contract slot directly.
- "Slot two available" was changed to a **secondary capacity marker** to preserve the Academy's limited knowledge.
- Added private UI showing **1 / 6 ACTIVE, 5 AVAILABLE**.
- The chapter still retains its Slot 2 title as the narrative hook for the next Contract-capacity development; the prose does not equate the artifact marker with the private UI slot system.

### CH032 — INSTITUTE CONTACT
- Stale "slot" reference changed to **capacity marker** where it referred to the artifact.

### CH033 — CONTRACT TWO SURFACES
- Artifact recognition is explicitly kept separate from Contract formation.
- Added private UI confirming THE POLITE KNOCK remains PARTIAL and **No new Contract detected**.
- Removed stale "spent seat" interpretation.

### CH035 — SECOND FAILURE
- Artifact response remains a response, not a Contract binding.
- Physical marker language is separated from Contract-slot language.
- Added private UI confirming **No new Contract detected** and artifact response **UNRESOLVED**.

### CH036 — RIVAL INTRODUCTION
- Stale "seat spent" wording changed to **no new Contract formed**.

### CH001–CH015
- Existing UI blocks were normalized to horizontal-border-only presentation.
- All Markdown ` ```text ` fences and vertical borders were removed.
- Existing UI content was preserved except where later canon required terminology separation.

## 4. UI Coverage Decision

Not every chapter should display the UI.

A UI appearance is appropriate when Daichi actively checks, receives, or verifies Contract information. It is **not** required every time the word "Contract" appears in prose.

Current meaningful UI checkpoints include:

- CH001 — first private interface manifestation.
- CH002 — privacy test.
- CH005–CH009 — early Contract-state checks.
- CH010, CH012, CH014 — pre-Contract status checks.
- CH015 — Contract #1 offer, acceptance, and invocation states.
- CH016 — post-use methodological audit.
- CH017 — active-slot state versus artifact-marker distinction.
- CH030 — active-slot capacity check.
- CH033 — artifact recognition without new Contract formation.
- CH035 — artifact response confirmed as unresolved and non-binding.

Chapters where no meaningful UI interaction occurs are intentionally not padded with a status box. This preserves the **strong prose payoff** principle.

## 5. Remaining Watch Items

### A. CH030 title
`END-I: SLOT 2 AND THE HOOK` remains as the chapter title. Its prose now distinguishes private Contract slots from the artifact's physical capacity marker. If the title is later considered too ambiguous, it can be renamed during a structural-title pass; this was not changed in this audit to avoid unnecessary chapter-reference churn.

### B. CH017 status metadata
The chapter still states that it is a draft/not locked. This is a workflow-status issue, not a Contract canon issue. It should be resolved by the chapter lock/audit workflow rather than silently changed during a UI pass.

### C. Contract #2
The current Contract System file identifies Contract #2 functionally as the Weapon Amplification / Mastery Contract and allows the formal name **Benkei** to be adopted later. CH030's "second Contract" hook is therefore compatible with the current system architecture, but the actual Contract #2 mechanics must remain authoritative in its own contract file when finalized.

## 6. Final Gates

- [x] UI uses horizontal borders only.
- [x] No vertical UI borders.
- [x] No Markdown UI code fences.
- [x] No RPG stat screen introduced.
- [x] Motion Sense remains natural ability.
- [x] Contract System remains Daichi-exclusive.
- [x] Academy ERROR remains separate from Contract UI.
- [x] Artifact/stone is not treated as the source of UI.
- [x] Twelve physical hollows are not treated as twelve Contract slots.
- [x] Active Contract maximum is six.
- [x] Artifact recognition is not automatically Contract formation.
- [x] UI does not replace Daichi's reasoning.
- [x] UI appearances are used as narrative checkpoints rather than forced every chapter.

**FINAL AUDIT STATUS: PASS WITH REPAIRS — CH001–CH042 Contract UI architecture is aligned with the current author-locked Contract System, with the remaining items explicitly classified as workflow/title watch items rather than hidden canon contradictions.**
