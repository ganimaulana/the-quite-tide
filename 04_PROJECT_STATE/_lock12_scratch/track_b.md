# LOCK 12 â€” Track B: Contract System Audit Report (AUDIT ONLY)

**Scope:** `~/workspace/world_bible/work_rar/04_PROJECT_STATE/` â€” Contract system canon, Contract #1 boundaries, slot architecture, DEPTH economy, mandatory stale-terminology tree-wide search.
**Read-only reference:** `~/workspace/world_bible/00_WORLD_BIBLE/` (never modified).
**Status:** AUDIT ONLY. No files rewritten. No chapters rewritten. Contract #2 not designed. Contract #1 not altered. LOCK 1â€“11 not reopened.
**Date:** 2026-09-23. Method: full read of `04_PROJECT_STATE/CONTRACTS/CONTRACT_1_POLITE_KNOCK.md` (501 lines); section reads of `04_PROJECT_STATE/DESIGN/CONTRACT_SYSTEM_MASTERS.md`, `04_PROJECT_STATE/DESIGN/ARTIFACT_DESIGN.md` Â§9, `04_PROJECT_STATE/FINAL_CANON_PROPOSAL/RULESETS.md` R1.2/R2.3, `01_STORY_ARCHITECTURE/00_PACING_AND_30_CHAPTERS.md` Â§1.5/ch30, `01_STORY_ARCHITECTURE/01_FIRST_3_ARCS.md` Arc II beats, `01_STORY_ARCHITECTURE/02_LONG_TERM_ROADMAP.md` Â§2; tree-wide ripgrep (66 files) for 20 mandated terms.

**Tag discipline (per directive):** carried-forward findings tagged `[CARRIED FORWARD â€” LOCK n]`; new audit judgments tagged `[PROPOSED]`; open items tagged `[DEFERRED]` / `[AUTHOR DECISION]` / `[UNKNOWN]`. `[CANON]` is never used standing alone.

---

## EXECUTIVE SUMMARY

The Contract system is **structurally sound and the locked terminology holds in all load-bearing files**. The chain ANOMALY â†’ SOLVED â†’ RESONANCE â†’ CONTRACT FORMATION â†’ OUTCOME is preserved everywhere it appears; no document collapses SOLVED into FULL; no live XP/level/power-tier framing of DEPTH exists; the 12-slot cap is consistently stated; the 13th side is never a slot; slot 2 opens late Nov 2024 and stays EMPTY; "second threshold" language is dead (one explicit negation, zero live uses).

The audit found **11 live stale/metadata instances requiring repair** (none of them rewrites of locked content â€” all banner/wording repairs needing author approval), **4 contradictions or near-contradictions**, and **6 structural gaps / author decisions**. The most significant:

1. **[PROPOSED â€” CONTRADICTION]** `04_PROJECT_STATE/CONTRACTS/CONTRACT_1_POLITE_KNOCK.md` Â§10 (L8-9, a LOCKED section) contains an unlabeled sentence: *"Contract #2 (Ledger) and Contract #3â€“4 (Brine) are designed as its sequels"* â€” asserting Contract #2's identity inside locked content, against the lock "Contract #2 UNDESIGNED/UNDECIDED". Needs an author decision (recommend: banner the sentence [PROPOSED]).
2. **[PROPOSED â€” UNSAFE/STALE]** `04_PROJECT_STATE/DESIGN/ARTIFACT_DESIGN.md:134` states a numeric claim â€” *"Slot-unlock thresholds rise ~3Ã— per face"* â€” inside a section whose LOCK 8 banner defers "exact numeric threshold values". Internal inconsistency with the banner and with LOCK 9's "no numeric threshold was named" finding.
3. **[PROPOSED â€” STALE METADATA]** Four files missed by LOCK 9's R-2 threshold-causality sweep: `01_STORY_ARCHITECTURE/00_PACING_AND_30_CHAPTERS.md:67` ("lifetime threshold crossed"), `:73` ("threshold audit ch25"), `02_ACADEMY/13_ACADEMY_RESTRUCTURE_REPORT.md:169` ("gauge threshold"), `01_STORY_ARCHITECTURE/01_FIRST_3_ARCS.md:69` ("Slot 4 unlocks (lifetime threshold...)").
4. **[PROPOSED â€” CONTRADICTION]** `04_PROJECT_STATE/DESIGN/CONTRACT_SYSTEM_MASTERS.md` Â§7:232 asserts a visibility decision ("after-the-fact only") while LOCK 8 defers gauge visibility entirely; Â§7:233 uses the unlocked term "Mooring tier" with a numeric gauge ceiling.
5. **[PROPOSED â€” AMBIGUOUS/STALE]** `01_STORY_ARCHITECTURE/00_PACING_AND_30_CHAPTERS.md:26` (Â§1.5): the LOCK 8 note supersedes the "except by failure" clause, but the body still says "failure drains" (which ledger?) and "Lifetime Depth ... unlocks slots" (causal unlock language superseded by LOCK 9's scheduled-event wording).

---

## A) CONTRACT SYSTEM AUDIT (VI)

**Verdict: PASS.** The rulebook and all lock files preserve the required chain. Granularity note only.

### Chain verification

- [CARRIED FORWARD â€” LOCK 8] `04_PROJECT_STATE/DESIGN/CONTRACT_SYSTEM_MASTERS.md:116` (banner, Â§3.1): *"contract outcomes are **FULL / PARTIAL / FRAGMENT / FAILED**. 'SOLVED' is an **investigative state**, not a contract outcome: Anomaly â†’ SOLVED â†’ RESONANCE â†’ Contract formation â†’ FULL / PARTIAL / FRAGMENT / FAILED â€” therefore **SOLVED â‰  FULL CONTRACT**."* The banner explicitly maps the superseded names (BINDINGâ†’FULL, HALF-HITCHâ†’PARTIAL, FLOTSAMâ†’FRAGMENT, FOUNDERINGâ†’FAILED) and instructs: *"Later prose in this file still uses the old names; read them through this map."* â€” residual old-name uses in Â§2.1 (FLOTSAM/FOUNDERING), Â§2.3 (FLOTSAM), Â§3.2 ("BINDING on false premises"), Â§5.3 ("Each BINDING or HALF-HITCH") are therefore [SUPERSEDED]-with-active-banner, no repair needed.
- [CARRIED FORWARD â€” LOCK 8] `04_PROJECT_STATE/CONTRACTS/CONTRACT_1_POLITE_KNOCK.md:158` (Â§6): the chain stated with RESONANCE as event/state: *"Anomaly â†’ SOLVED â†’ **RESONANCE** â†’ Contract formation â†’ FULL / PARTIAL / FRAGMENT / FAILED. For Contract #1, RESONANCE occurs at **ch11's empirically certified solve**."*
- [CARRIED FORWARD â€” LOCK 9] `01_STORY_ARCHITECTURE/LOCK_9_ARC_I_ARCHITECTURE.md:168` (Â§9.1): *"The conceptual chain ANOMALY â†’ SOLVED â†’ RESONANCE â†’ CONTRACT FORMATION â†’ FULL/PARTIAL/FRAGMENT/FAILED fires in order"* â€” with a sanctioned sequencing nuance (ch10's unanswered offer precedes ch11's solve; LOCK 8 F-07 sanctions this as grammar-performance with no answer firing).
- [CARRIED FORWARD â€” LOCK 10] `01_STORY_ARCHITECTURE/LOCK_10_ACADEMY_MISSION_ANOMALY_INTEGRATION.md:396` (AD-1): *"Canonical chain: ANOMALY â†’ SOLVED â†’ RESONANCE â†’ CONTRACT FORMATION â†’ PARTIAL (LOCK 8 outcome vocabulary; SOLVED â‰  FULL CONTRACT preserved)."*
- The knock file's Â§19 contradiction audit (F-05) resolved the duplicate outcome vocabularies; F-11 resolved the three senses of "resonance" (gauge-currencyâ†’superseded/now DEPTH; Esper-physics usageâ†’kept; loop-stage eventâ†’LOCKED). [CARRIED FORWARD â€” LOCK 8]

### No state-collapsing found

- Targeted search for SOLVED-collapsed-as-FULL returned only affirmations of SOLVED â‰  FULL (rulebook banner, knock Â§6, LOCK 9 Â§9.1, LOCK 10 AD-1). No document treats SOLVED as a contract outcome.
- The rulebook's acquisition sequence (`04_PROJECT_STATE/DESIGN/CONTRACT_SYSTEM_MASTERS.md:90-100`, Â§2.1) reads OBSERVE â†’ SOLVE â†’ OFFER â†’ ACCEPTANCE (SETTLING) â†’ BINDING. RESONANCE is not a named step in Â§2.1 (it appears only in the Â§3.1 banner's chain formula). **[PROPOSED]** classification: compatible granularity difference, not a contradiction â€” but a one-line coherence note could relabel Â§2.1 step 1â†’2 as OBSERVEâ†’SOLVEâ†’RESONANCEâ†’OFFER for full chain fidelity in a future pass. No repair required now.
- DEPTH â‰  Resonance/XP/Rank: guardrails verified live in the rulebook banner (`:28`), `ARTIFACT_DESIGN.md:124`, `00_EXECUTIVE_VERDICT.md:100`, knock `:15/:159/:172/:233/:426`, `15_ACADEMY_30_CHAPTER_RESTRUCTURE.md:265`, `01_ARTHUR_TIMEmessaging app.md:35`. **Zero** live XP/level/power-tier framings of DEPTH in the tree (see Â§E table). [CARRIED FORWARD â€” LOCK 8]
- Solve-certification stays empirical (rulebook Â§0.3): falsifiable prediction, recorded before the test, world-confirms; accidental solves and self-certification void. [CARRIED FORWARD â€” LOCK 8]
- The iron rule CONTRACT PROGRESSION â‰  DEPTH PROGRESSION â‰  POWER PROGRESSION: upheld structurally â€” slot unlocks are scheduled events (LOCK 9 R-2), Lifetime Depth is a non-causal historical measure, and the power-curve analysis (knock Â§16) grants options not stats. [CARRIED FORWARD â€” LOCK 8/9]

### Structural gap (minor)

- [PROPOSED] G-VI-1: the knock file's six-field schema (Authority/Condition/Restriction/Cost/Duration/Compatibility) is noted as not existing in the tree (knock Â§1) and is [DEFERRED â€” FUTURE CONTRACT SYSTEMS PASS]. The 12-field candidate format and the rulebook's signing content (Â§2.1 + Â§11) coexist without a filing-format decision. Carried as a deferred item; not a contradiction.

---

## B) CONTRACT #1 BOUNDARY AUDIT (VII)

**Verdict: PASS.** No inflation of THE POLITE KNOCK found anywhere in the tree. Every reference file either restates the locked boundaries or adds explicit anti-inflation verdicts.

### Positive controls (all [CARRIED FORWARD â€” LOCK 8/9/10])

- `04_PROJECT_STATE/CONTRACTS/CONTRACT_1_POLITE_KNOCK.md` Â§10: all seven R6 forbidden categories avoided (no omniscience, no universal detection, no automatic truth detection, no unrestricted anomaly control, no generic teleportation, no generic barrier, no unrestricted combat enhancement); "felt-certainty counter" disclosed as the failure mode; *"Weak in combat, foundational in method."*
- `01_STORY_ARCHITECTURE/LOCK_10_ACADEMY_MISSION_ANOMALY_INTEGRATION.md:267`: ***"Boundary verdict: the knock never becomes a universal detector, omniscience, investigation-bypass, or auto-solver."*** Its most powerful Arc I moments are its failures (ch15) and near-failures (ch27).
- Same file `:264`: *"Not a universal detector (it gave a wrong-feeling-true answer), not omniscience, not investigation-bypass (ch18 + mission #4 were required)."*
- `01_STORY_ARCHITECTURE/LOCK_9_ARC_I_ARCHITECTURE.md:180` (Â§9.7): philosophy preserved â€” *"Arthur receives a Contract because he understands something others could not, not because he defeats something stronger"*; EVENT-100 resolved *before* the knock's shape is revealed, by analysis + team, never by the contract.
- LOCK 8 interface banners (identical text, 2026-09-23) in `02_ACADEMY/10_TEAM_DOCTRINE.md:243`, `02_ACADEMY/11_JOINT_TEAM_DOCTRINE.md:216`, `02_ACADEMY/12_MIXED_MISSION_SYSTEM.md:274`, `02_ACADEMY/08_IO_LADDER.md:251`, `02_ACADEMY/04_IRREGULAR_MECHANICS.md:231`, `02_ACADEMY/07_EAR_DESIGN.md:184`: *"Rank remains F; Classification remains Irregular; **no leadership and no Academy recognition granted by the Contract**."*
- Knock file Â§13: the Academy does NOT automatically know about the Contract (Laggard masking, instruments log nothing anomalous â€” ch15). Knock file Â§14: Contract #1 does NOT automatically trigger L3-T1 (knock-shaped trigger, not auto-unlock; re-validation condition).
- Knock file Â§19 F-12 (five sub-categories) and Â§19 explicit non-findings: no Rank/Classification change, no automatic L3-T1 or leadership grant, no Contract #2 in Arc I, no Academy auto-detection, no ERROR-grants-contract, no destined-solver, no EAR-as-destiny. [CARRIED FORWARD â€” LOCK 8]

### Targeted inflation-pattern search: zero hits

- ripgrep for knock-adjacent inflation language (omniscient / universal detector / auto-solve / combat ability / rank source / classification source / leadership mechanism / "solves everything") returned **no genuine inflation instances** â€” only anti-inflation statements (the LOCK 10 verdict, TOP_3's anti-auto-solve table, the knock file's own restrictions table).
- `04_PROJECT_STATE/CONTRACT_DESIGN/CONTRACT_1_TOP_3.md:30` even warns in the opposite direction: *"if drafts soften [the Depth-scaling-by-tier and one-tap rules], the Knock becomes a Rule-extraction service and E7/E8-class exploits reopen."* â€” a guardrail, not an inflation.

### Stale-label instances (not inflation; banner-level)

- [PROPOSED â€” STALE METADATA] Several worker files still tag Contract #1 as `"[PROPOSED â€” pending user lock]"`: `02_ACADEMY/12_MIXED_MISSION_SYSTEM.md:193` (*"THE POLITE KNOCK requires **presence** (CONTRACT_1_RECOMMENDATION.md [PROPOSED â€” pending user lock])"*), `:235` (*"Contract #1 = THE POLITE KNOCK | [PROPOSED â€” pending user lock]"*), `02_ACADEMY/18_SOCIAL_HIERARCHY_PROGRESSION.md:227`, `02_ACADEMY/05_IRREGULAR_DARK_HORSE_ARC.md:192`, `04_PROJECT_STATE/FINAL_CANON_PROPOSAL/HISTORIES_AND_TIMEmessaging app.md:114` (labels identity `"[PROPOSED â€” LOCK 8]"` though LOCK 8 locked it). The knock file's own lock record declares surviving "PENDING USER LOCK" phrasing [SUPERSEDED]. These are label lag, not boundary violations â€” but they contradict the lock record and belong on the deferred F-03/F-09/F-10 annotation sweep (LOCK 9 Â§15.5 already catalogued `15_ACADEMY_30_CHAPTER_RESTRUCTURE.md` Â§4's instance; LOCK 10 G-5/R-9 cover it too).

---

## C) SLOT ARCHITECTURE AUDIT (VIII)

**Verdict: PASS on substance; 3 stale-wording instances need repair.** The 12 physical-marker capacity / 6 active Contract slots, the 13th-side rule, capacityâ‰ unlocked, slot-2-empty, and Contract-#2-absent rules are consistently stated. No implied 7-slot cap, 13th Contract, automatic unlock, Contract-per-Rank, Contract-per-chapter, or Contract-per-DEPTH-threshold found.

### Locked statements verified ([CARRIED FORWARD â€” LOCK 8/9])

- 12 physical-marker capacity / 6 active Contract slots: `04_PROJECT_STATE/DESIGN/CONTRACT_SYSTEM_MASTERS.md:57` (MOORING row â€” *"twelve physical binding faces/markers; active Contract capacity: **6**, inspectable, diegetic"*, with the F-04 revision note); `04_PROJECT_STATE/FINAL_CANON_PROPOSAL/RULESETS.md:68` (R2.3 â€” *"**12 physical faces/markers; 6 active Contract slots maximum** ... [REVISED 2026-09-23 â€” LOCK 8 F-04: the seven-slot maximum is **[SUPERSEDED]**]"*); `04_PROJECT_STATE/CONTRACTS/CONTRACT_1_POLITE_KNOCK.md:14` (author decision 2); `04_PROJECT_STATE/RISKS_AND_DECISIONS/TOP_50_REMAINING_RISKS.md:268`; `02_ACADEMY/00_DECISION_LOCK_ACADEMY.md:392`.
- 13th side â‰  slot #13: rulebook `:57` (*"The **thirteenth face** is NOT a Mooring â€” it is a separate/special artifact function ... do NOT treat it as Contract Slot #13"*); knock `:14`; RISKS `:268`; DECISION_LOCK `:392`. Zero hits for "13th slot"/"13th contract" in the tree.
- Capacity â‰  unlocked: rulebook `:57` (*"**Maximum capacity â‰  availability:** Arthur starts with **one** open Mooring; additional faces become available only through the locked slot-unlock timing (slot 2 opens late November 2024 and remains EMPTY â€” capacity â‰  acquisition)"*); knock `:14`; `02_ACADEMY/15_ACADEMY_30_CHAPTER_RESTRUCTURE.md:265`; `02_ACADEMY/01_ARTHUR_TIMEmessaging app.md:35` (T-16); `01_STORY_ARCHITECTURE/LOCK_9_ARC_I_ARCHITECTURE.md:86` (ch30 table: *"Slot 2 unlocks but remains EMPTY (LOCK 8: capacity â‰  acquisition; the reader waits)"*).
- Old 7-slot stays SUPERSEDED, not revived: all 5 "7 slots"/"7-slot" hits are annotated resolutions/records (see Â§E). No live 7-slot claim.

### Implied-pattern check: none found

- No "automatic slot unlock" â€” post-LOCK-9, the ch30 unlock is a scheduled event with the author's mandated wording (*"the scheduled event becomes available once the required conditions are met"*), explicitly not a meter-causality event (LOCK 9 R-2; 00_DECISION_LOCK_ACADEMY.md:81: *"no threshold mechanic is canon"*).
- No Contract-per-Rank, Contract-per-chapter, or Contract-per-DEPTH-threshold implications anywhere.
- Contract #2 in Arc I: absent everywhere (see Â§E term 12). 01_FIRST_3_ARCS.md's "Slot 3 unlocks (ch70)" is Arc II [PROPOSED] roadmap, not a lock.

### Stale-wording instances ([PROPOSED â€” STALE METADATA â†’ REQUIRES REPAIR], banner-only)

These four were missed by LOCK 9's R-2 sweep (which repaired `15_ACADEMY_30_CHAPTER_RESTRUCTURE.md` Â§3 ch30 + Â§3.2, `01_ARTHUR_TIMEmessaging app.md` T-16, `00_PACING_AND_30_CHAPTERS.md` ch25, `01_FIRST_3_ARCS.md` ch64â€“70):

1. `01_STORY_ARCHITECTURE/00_PACING_AND_30_CHAPTERS.md:67` â€” ch30 beat: *"**Slot 2 unlocks** (lifetime threshold crossed â€” gauge milestone PAID, reader-trackable)"* â€” superseded "lifetime threshold" terminology + threshold-causality. Repair with the mandated scheduled-event wording.
2. `01_STORY_ARCHITECTURE/00_PACING_AND_30_CHAPTERS.md:73` â€” "Gauge milestones" summary: *"threshold audit ch25; S2 unlock ch30"* â€” the ch25 beat was repaired but the summary line retains "threshold audit" language.
3. `02_ACADEMY/13_ACADEMY_RESTRUCTURE_REPORT.md:169` â€” *"ch30 â€” END-I: slot 2 unlocks (gauge threshold, paid on-page)"* â€” pre-LOCK-9 "gauge threshold" wording.
4. `01_STORY_ARCHITECTURE/01_FIRST_3_ARCS.md:69` â€” *"**Slot 4 unlocks** (lifetime threshold; paid on-page)"* â€” same stale pattern, Arc III planning.
5. Minor: `02_ACADEMY/15_ACADEMY_30_CHAPTER_RESTRUCTURE.md:40` (Â§4 table): *"(verdict Â§5.5: 'gauge threshold')"* â€” stale parenthetical; the detailed ch30 beat at `:265` was repaired.
6. Minor: `02_ACADEMY/01_ARTHUR_TIMEmessaging app.md:50` â€” historical note preserving *"verdict Â§Â§5.1 ... and 5.5 (currency merge â€” gauge threshold, not lifetime threshold)"* â€” describes the merge distinction; recommend a one-line update to the LOCK 9 wording.

---

## D) DEPTH ECONOMY AUDIT (IX)

**Verdict: PASS.** Acquisition, expenditure, Current-decrease, and Lifetime-cumulativeness rules are consistent and locked. No numeric thresholds, gauges-as-levels, XP, regeneration rules, or numeric pricing are canonically locked. The "second threshold" issue stays dead.

### Locked economy ([CARRIED FORWARD â€” LOCK 8])

- **Acquisition:** certified novel solves only â€” `04_PROJECT_STATE/DESIGN/CONTRACT_SYSTEM_MASTERS.md:167-171` (Â§5.1): *"Depth banks **only** on certified novel solves. **Novelty-weighted yield**: yield scales with *understanding-difficulty* (novel Rule structure), not threat tier ... The gauge **remembers anomaly IDs** ... no double-counting, ever. Re-solves pay **only** at a deeper Solve-Grade ... **Kind-diminishing**: the tenth solved coin-trick pays ~nothing."* Investigation is unpriced-by-the-artifact, priced-by-the-world. DEPTH comes from genuine anomaly interaction â€” empirical certification (rulebook Â§0.3: falsifiable prediction, recorded-before-test, world-confirms).
- **Expenditure:** `04_PROJECT_STATE/DESIGN/CONTRACT_SYSTEM_MASTERS.md:173-180` (Â§5.2): *"**Every invocation spends Depth** ... Drain scales with effect tier and duration. **Signing spends Depth** (the binding price, grade-banded). **Renewal = full-price new signing** ... **Buyout** ... **Quiet-use premium** ... **Per-query pricing for information contracts**."* **No debt:** Â§5.4 â€” *"The Repository **never extends credit**."* Cost-shifting forbidden (Â§5.5): *"Depth is banked understanding; understanding cannot be transferred."*
- **Current DEPTH can decrease:** yes â€” spent by invocation, drains per use, decays slowly when unspent (rulebook Â§7:231; LOCK 8 interpretation: decay applies to CURRENT DEPTH only â€” knock Â§6). Knock ch15: *"Current Depth drains to near-zero."*
- **Lifetime DEPTH is cumulative, never decreases:** knock Â§6 [LOCKED]: *"**LIFETIME DEPTH never decreases** â€” it is a pure cumulative historical measure."* The old "except by failure" clause (`00_PACING_AND_30_CHAPTERS.md` Â§1.5) is [SUPERSEDED]: *"priced failures cost opportunity and blowback, never the lifetime ledger."*
- **DEPTH is NOT:** XP, level, rank, generic mana, conventional Esper energy, Fathoms (*"Mana has zero hits anywhere in the tree"* â€” knock Â§9). Resolved three-senses ruling (knock Â§6 F-11).
- **No numeric thresholds/gauges/bars/levels/tiers/XP/regeneration locked:** *"**No numeric Depth amounts are given anywhere** â€” priced qualitatively only â†’ [DEFERRED â€” FUTURE CONTRACT SYSTEMS PASS]"* (knock Â§9). Refills: *"only through new certified solves â€” **never through rest, never through purchase, never through time**"* (knock Â§6). No regeneration mechanic exists or is implied.

### Exceptions / flags ([PROPOSED])

1. **D-1 â€” UNSAFE numeric remnant:** `04_PROJECT_STATE/DESIGN/ARTIFACT_DESIGN.md:134` â€” *"Slot-unlock thresholds rise ~3Ã— per face (porting 04.4's exponential cost curve â€” Q009 solution 1)"*. This is a **numeric threshold claim** surviving inside Â§9, whose own LOCK 8 banner (`:124`) defers *"exact numeric threshold values"* and whose file sits under LOCK 9's finding *"No numeric threshold was named ... anywhere in the tree."* Internal inconsistency: either the banner must be extended to cover "~3Ã— per face" as [SUPERSEDED]/deferred, or the line must go. [AUTHOR DECISION] in the future Contract Systems pass.
2. **D-2 â€” STALE relock mechanics:** `04_PROJECT_STATE/FINAL_CANON_PROPOSAL/RULESETS.md:27` (R1.2): *"If the gauge drops below a slot's unlock threshold, that slot **relocks** until re-earned"* â€” pre-LOCK-8 terminology ("the gauge", "resonance" at `:27`'s "spent resonance must be re-earned") with no LOCK 8 banner on the section; the relock mechanic itself was never examined by LOCK 8/9 and sits uneasily with the scheduled-event slot-unlock model. Same relock language at `04_PROJECT_STATE/DESIGN/ARTIFACT_DESIGN.md:138` and `00_EXECUTIVE_VERDICT.md:109`. [PROPOSED] classification: SUPERSEDED on terminology; the relock *mechanic* is [DEFERRED]/[AUTHOR DECISION] â€” keep, revise, or remove.
3. **D-3 â€” "woundable by failure" contradiction:** `00_EXECUTIVE_VERDICT.md:109` â€” *"Lifetime Resonance (cumulative earned; slot-unlock thresholds; **woundable by priced failures** â€” J ch19's 'lifetime drain')"*. The Â§5.5 banner at `:100` supersedes terminology only (*"The story logic ... is [KEEP]"*) and does not cover the mechanics; LOCK 8 F-11 removed the "except by failure" clause entirely. The banner should be extended or `:109` revised. [PROPOSED â€” CONTRADICTION, banner-level repair]
4. **D-4 â€” ambiguous "failure drains":** `01_STORY_ARCHITECTURE/00_PACING_AND_30_CHAPTERS.md:26` (Â§1.5): the LOCK 8 note correctly supersedes the exception clause, but the body still reads *"failure drains (Q379/Q393)"* (which ledger? â€” must mean Current Depth only) and *"Lifetime Depth ... unlocks slots"* (causal unlock language superseded by LOCK 9's scheduled-event wording). [PROPOSED â€” STALE METADATA â†’ REQUIRES REPAIR] (banner clarification, no content redesign).
5. **D-5 â€” "second threshold" stays dead:** confirmed. Single tree hit is the explicit negation at `01_STORY_ARCHITECTURE/LOCK_10_ACADEMY_MISSION_ANOMALY_INTEGRATION.md:42` (*"no 'second threshold' language anywhere"*); LOCK 9 R-2 repaired the historical "second/third threshold" phrasing. [CARRIED FORWARD â€” LOCK 9]

---

## E) MANDATORY TREE-WIDE SEARCH (XXXI)

66 files searched. Term-by-term findings. "L3-T1" (IO-ladder institutional triggers, trigger-first doctrine â€” `02_ACADEMY/08_IO_LADDER.md`) and "Band" (arc-structure bands, e.g. Q351_400:491's "Band 6") are **explicitly excluded** as DEPTH thresholds â€” neither is ever framed as a DEPTH mechanic; no DEPTH-threshold reading of either term exists in the tree.

| # | Term | Hits | Findings (file:line â€” quote â€” classification) |
|---|---|---|---|
| 1 | "7 slots" | 2 | `04_PROJECT_STATE/RISKS_AND_DECISIONS/TOP_50_REMAINING_RISKS.md:268` â€” "all active 7-slot references [SUPERSEDED]" â€” SUPERSEDED (correctly annotated). `02_ACADEMY/00_DECISION_LOCK_ACADEMY.md:392` â€” "F-04 RESOLVED (12-slot max capacity ... all 7-slot references [SUPERSEDED])" â€” SUPERSEDED (lock record). |
| 2 | "7-slot" | 3 | `04_PROJECT_STATE/CONTRACTS/CONTRACT_1_POLITE_KNOCK.md:14` â€” 'Old "7-slot maximum" references = [SUPERSEDED] (F-04 resolved)' â€” SUPERSEDED (locked ruling). `:17` â€” "all 7-slot sources marked [SUPERSEDED] or revised" â€” SUPERSEDED. `:413` (F-04 row) â€” "7 Moorings/knots" vs "Twelve is canonical" â†’ RESOLVED â€” SUPERSEDED. |
| 3 | "second threshold" | 1 | `01_STORY_ARCHITECTURE/LOCK_10_ACADEMY_MISSION_ANOMALY_INTEGRATION.md:42` â€” "no 'second threshold' language anywhere" â€” explicit negation; the term **stays dead**. [CARRIED FORWARD â€” LOCK 9/10] |
| 4 | "threshold" | 99 | **Clean/canon senses** (no action): Threshold agencies / Civic Annex / Threshold-adjacent employment (`GEOGRAPHY_ECONOMY_SOCIETY_GOVERNMENT.md`, `MASTER_WORLD_BIBLE.md:63/:67`, `HISTORIES_AND_TIMEmessaging app.md:47`, `14_ACADEMY_RESTRUCTURE.md:108/:190`); dormancy/pressure thresholds as cosmology (`ARTIFACT_DESIGN.md:75/:77/:88`, `HISTORIES_AND_TIMEmessaging app.md:63`, `ARTHUR_CHARACTER_BIBLE.md:66`, `CANON_CHANGE_LABELS.md:39`); reporting/handling/T3+ thresholds as classification taxonomy (`ANOMALY_DESIGN.md:72/:265`, `MISSION_TASK_SYSTEM.md:42`, `STORY_ENGINES.md:37`); "demonstrated-only threshold" qualitative staging notes (`LOCK_10_ACADEMY_MISSION_ANOMALY_INTEGRATION.md:380/:413` â€” fine, not numeric); audit deliberation history (`AUDIT/500_QUESTION_AUDIT/*` â€” SUPERSEDED proposal-history, intentionally preserved); date-quarantine "threshold" (`00_EXECUTIVE_VERDICT.md:77/:85` â€” fine). **Flagged:** see C-stale list and D-1â€“D-4 (Â§C items 1â€“6; Â§D items 1â€“4). |
| 5 | "gauge" | 304 | **Legitimate locked senses** (no action): "spendable gauge currency" (`CONTRACT_SYSTEM_MASTERS.md:61`, knock Â§9 â€” LOCKED vocabulary); "the gauge **opens** ('twelve hollows, eleven empty')" as the consequence-of-understanding texture (knock Â§6/Â§12, `LOCK_9_ARC_I_ARCHITECTURE.md:67`); reader-trackability texture in ch13/ch15 beats, annotated by LOCK 9 R-9 as staged-for-visible-meter with infer-only fallback. **Flagged:** `00_PACING_AND_30_CHAPTERS.md:26` (Â§1.5 â€” see D-4); Q-audit pre-lock "gauge" language (deliberation history). Gauge **visibility** remains [DEFERRED â€” FUTURE CONTRACT SYSTEMS PASS] (LOCK 8; `ARTIFACT_DESIGN.md` Â§9 infer-only vs `00_PACING_AND_30_CHAPTERS.md` Â§1.5 visible â€” unresolved deliberately). |
| 6 | "meter" | 38 | All uses are reader-trackability texture ("the reader tracks the meter" â€” ch13/ch15 beats, annotated DEFERRED-compatible) or audit deliberation ("progression meter [REWRITE]" â€” audit history); `05_IRREGULAR_DARK_HORSE_ARC.md:27` ("meter like ammunition" â€” Sophie Ward, unrelated to DEPTH). **No DEPTH-as-meter-level system exists.** Clean. |
| 7 | "XP" | 15 (incl. "experience points" 0, "level up" in-text) | **All 15 are guardrail negations:** "NOT XP" (rulebook `:28`, `ARTIFACT_DESIGN.md:124`, `00_EXECUTIVE_VERDICT.md:100`, knock `:15/:159/:172`, `15_ACADEMY_30_CHAPTER_RESTRUCTURE.md:265`, `01_ARTHUR_TIMEmessaging app.md:35`); "Resonance is NOT XP" (knock Â§6); "never an implicit leveling system" (knock `:15/:159`); "GREATER BREAKTHROUGH must be *defined* or it becomes 'a level-up with better marketing'" (`04_PROJECT_STATE/ANALYSIS/ARTHUR_POWER_DESIGN.md:98` â€” warning, [PROPOSED]). **Zero live XP framing.** Clean. |
| 8 | "level" | 180 | "contract level": **0 hits.** Remaining uses: threat/filed levels, IO-ladder levels, world/arc/phase levels, "street-level" â€” none attach to DEPTH or Contracts as progression levels. Clean. |
| 9 | "tier" | 279 | Canon senses only: anomaly filed tiers (T0â€“T4), Esper tiers, **"tier-scaled DEPTH"** (LOCKED knock per-use pricing), "tier-mirroring" observability (`ARTIFACT_DESIGN.md` Â§9), "sapient-tier gating" as story-gating (`ARTIFACT_DESIGN.md:182`). No "contract tier"/"contract level" system. **Flag:** "per Mooring tier" (`CONTRACT_SYSTEM_MASTERS.md:233` â€” unlocked vocabulary, see D-1 note / Â§F). Otherwise clean. |
| 10 | "power level" | 7 | All meta-analytical negations: "not power levels" as doctrine (`AUDIT/Q001_050.md:288` quoting 04.7); "'outside classification' excuses any power level" as risk language (`TOP_50_REMAINING_RISKS.md:157`, `TOP_50_DESIGN_DECISIONS_TO_LOCK.md:69`); "never a power level" endgame discussion (`Q451_500.md:337`, `02_LONG_TERM_ROADMAP.md:91`). Clean. |
| 11 | "contract level" | 0 | Clean. |
| 12 | "resonance points" / "resonance XP" | 0 | Clean. |
| 13 | "lifetime resonance" / "current resonance" | 11 | All inside LOCK 8 supersession banners or guardrails: rulebook `:28`, `ARTIFACT_DESIGN.md:124`, `00_EXECUTIVE_VERDICT.md:100` (banner â€” but body `:107/:109` flagged, see D-3), knock `:15/:159/:172/:420/:426`, `15_ACADEMY_30_CHAPTER_RESTRUCTURE.md:265`, `01_ARTHUR_TIMEmessaging app.md:35`, `02_ACADEMY/00_DECISION_LOCK_ACADEMY.md:392`, `04_PROJECT_STATE/RISKS_AND_DECISIONS/TOP_50_REMAINING_RISKS.md:268`. Correctly marked [SUPERSEDED] wherever live. |
| 14 | "Contract #2" / "Contract 2" | 58 | **Clean locked statements:** "Contract #2 remains completely UNDESIGNED and UNDECIDED â€” not assigned to any lock" (`04_PROJECT_STATE/RISKS_AND_DECISIONS/TOP_50_REMAINING_RISKS.md:276` â€” LOCK 9 finalization note); "No Contract #2" hard fences (LOCK 10 `:10`, LOCK 11 `:12`); "no Contract #2" mystery boundary (knock header); "Contract #2 does NOT occur in Arc I" [LOCKED] (`02_ACADEMY/01_ARTHUR_TIMEmessaging app.md` Â§4); "Contract #2's capability and timing are not assigned to any lock" (`02_ACADEMY/00_DECISION_LOCK_ACADEMY.md:15`); knock Â§15 pacing ("Late Nov 2024 â€” Slot 2 unlocks but remains EMPTY"). **PROPOSED (not locked) roadmap/analysis content:** `01_STORY_ARCHITECTURE/01_FIRST_3_ARCS.md:43` ("Contract #2's phenomenon surfaces"), `:48` ("Contract #2 forms at CLIMAX (ch64â€“70)" â€” "remainder-housing", "continuation" price), `:51` ("What Arthur gains: Contract #2 ... Slot 3"); `04_PROJECT_STATE/ANALYSIS/ARTHUR_POWER_DESIGN.md:49-71` (Â§3 "Contract #2 â€” the escalation": ward-noise sense, recognition ledger, half-second "looks away", pre-paid escape â€” [INFERENCE]/[PROPOSED]); `04_PROJECT_STATE/CONTRACT_DESIGN/CONTRACT_1_RECOMMENDATION.md:46` ("Contract #2 (recommended): The Ledger of Small Debts (Candidate 9)" â€” pre-lock recommendation); `00_EXECUTIVE_VERDICT.md:147` ("recommended #2 (Ledger) / #3â€“4 (Brine) placement" â€” pre-lock verdict). **CONTRADICTION:** knock Â§10 (see Â§F). |
| 15 | "slot 2" / "slot #2" | 40 | Substantively consistent: unlocks late Nov 2024, remains EMPTY, capacity â‰  acquisition (`15_ACADEMY_30_CHAPTER_RESTRUCTURE.md:264-265` repaired; `01_ARTHUR_TIMEmessaging app.md:35`; `LOCK_9_ARC_I_ARCHITECTURE.md:86`; knock Â§15). Stale-wording instances flagged in Â§C. No automatic unlock, no acquisition, no Contract #2. |
| 16 | "13th slot" / "13th contract" | 0 | Clean. Positive locked statements ("13th side â‰  slot #13") in rulebook `:57`, knock `:14`, RISKS `:268`, DECISION_LOCK `:392`. |
| 17 | "Irregular Division" | 28 | **All 28 are negations or bannered [SUPERSEDED]:** LOCK 10/11 hard fences ("No Irregular Division/barracks/curriculum"); `02_ACADEMY/06_DIVISION_SYSTEM.md:242` (Â§9 [SUPERSEDED] in its entirety); `02_ACADEMY/02_ARTHUR_ACADEMY_ENTRY.md:196` (Â§196 amendment supersedes Â§Â§59/70â€“71/82/95); `02_ACADEMY/03_IRREGULAR_CLASSIFICATION.md` (Â§1 rewritten as classification, not division); `02_ACADEMY/19_TERMINOLOGY_AUDIT_CLERK.md` (catalogue); `02_ACADEMY/04_IRREGULAR_MECHANICS.md:177-180` (C-1/C-2/C-4); `02_ACADEMY/10_TEAM_DOCTRINE.md:214-217` (T-3/T-6); `02_ACADEMY/11_JOINT_TEAM_DOCTRINE.md:43` (nine negations: "Irregular â‰  Division Â· Irregular â‰  Team Â· Irregular â‰  Command Â· Irregular â‰  Power Tier"); `04_PROJECT_STATE/RISKS_AND_DECISIONS/TOP_50_REMAINING_RISKS.md:239/:244`. Clean. |

### FINAL_WORLD_BIBLE cross-check (read-only, reference only)

- "7 slots"/"7-slot": 0 hits. "XP"/"experience points": 0 hits. "Contract #2": 0 hits.
- The old bible's "Resonance" (`04_POWER_SYSTEM.md`: *"Every Resonance falls into one discipline"*) is the old Esper-physics usage â€” the sense LOCK 8 Â§6 explicitly keeps as *"the Esper-physics usage, unrelated to the contract event."* No conflict.
- "power levels" in old 04.7 (*"Resonances interact through Rule interference, not power levels"*) is the old anti-power-level doctrine, consistent with the reboot's direction. No redesign terminology has leaked into the old bible (expected â€” it pre-dates the reboot and is untouched).

---

## SUMMARY

### [CARRIED FORWARD â€” LOCK 8]
- CF-1: The chain ANOMALY â†’ SOLVED â†’ RESONANCE â†’ CONTRACT FORMATION â†’ OUTCOME (FULL/PARTIAL/FRAGMENT/FAILED) with SOLVED â‰  FULL CONTRACT â€” preserved in the rulebook banner, the knock file, LOCK 9 Â§9.1, LOCK 10 AD-1.
- CF-2: Terminology settlement â€” RESONANCE = event/state, DEPTH = resource, CURRENT DEPTH = available, LIFETIME DEPTH = cumulative-never-decreases; "Current/Lifetime Resonance" [SUPERSEDED]; verdict Â§5.5 merge [SUPERSEDED] on terminology.
- CF-3: Outcome vocabulary FULL / PARTIAL / FRAGMENT / FAILED; old names [SUPERSEDED] with synonym map; residual old-name prose covered by the rulebook Â§3.1 banner.
- CF-4: Contract #1 boundaries â€” presence-only, one-knock-per-phenomenon-ever, one confirmed sentence, tier-scaled DEPTH, signing = FIRST WATER + DEPTH + 1 toll-mark; Rank F stays; Irregular stays; no leadership, no auto-T1, no auto-detection, no Contract #2 in Arc I; R6 all pass.
- CF-5: 12 physical-marker capacity / 6 active Contract slots; 13th side â‰  slot #13; capacity â‰  unlocked; slot 2 opens late Nov 2024 and stays EMPTY.
- CF-6: DEPTH economy â€” novel-solve income only; every invocation spends; no debt; Current decreases; Lifetime never decreases; "except by failure" removed; refills only via new certified solves.
- CF-7: The "second threshold" issue is dead (explicit negation at LOCK 10:42; LOCK 9 R-2 repaired the historical phrasing).
- CF-8: Zero live XP/level/power-tier framings of DEPTH; zero "contract level"/"resonance points"/"13th slot" claims.

### [PROPOSED] (new audit judgments)
- P-1: 11 stale-metadata instances require banner/wording repair (listed in Â§C items 1â€“6 and Â§D items 2â€“4) â€” all banner-level, none requiring locked-content changes.
- P-2: 4 contradictions/near-contradictions: (a) knock Â§10's unlabeled "Contract #2 (Ledger)" sentence vs UNDESIGNED/UNDECIDED; (b) `ARTIFACT_DESIGN.md:134` "~3Ã— per face" vs the :124 deferral banner and LOCK 9's no-numerics finding; (c) rulebook Â§7:232 visibility "after-the-fact only" vs LOCK 8's visibility deferral; (d) knock Â§20's deferred "slot thresholds" numerics vs DECISION_LOCK_ACADEMY:81's "no threshold mechanic is canon."
- P-3: Rulebook Â§2.1's sequence omits RESONANCE as a named step (granularity note only â€” compatible, no contradiction).
- P-4: Audit Q&A files' pre-lock proposal language is deliberation history, intentionally preserved â€” do not "repair" it; it is the audit trail.
- P-5: "L3-T1" and "Band" terms are explicitly excluded as DEPTH thresholds â€” no DEPTH-threshold reading of either exists.

### [DEFERRED] / [AUTHOR DECISION] / [UNKNOWN]
- [DEFERRED â€” FUTURE CONTRACT SYSTEMS PASS] (carried): knock duration class; ch12 toll-mark vs ch15 mark #1; numeric DEPTH amounts; gauge visibility to Arthur; Depth decay schedule detail; six-field schema adoption; Toll-kind taxonomy; stale-file annotation sweep (F-03/F-09/F-10) â€” knock Â§20.
- [AUTHOR DECISION] AD-T1: knock Â§10 "Contract #2 (Ledger)" â€” banner as [PROPOSED] (recommended) or lock Ledger as Contract #2's identity. The lock context says UNDESIGNED/UNDECIDED; the sentence sits unlabeled inside a LOCKED section.
- [AUTHOR DECISION] AD-T2: the slot-relock mechanic (`RULESETS.md` R1.2, `ARTIFACT_DESIGN.md:138`, verdict Â§5.5) â€” keep, revise, or remove; reconcile with the scheduled-event unlock model.
- [AUTHOR DECISION] AD-T3: "slot thresholds" as deferred numerics (knock Â§20 #3) vs "no threshold mechanic is canon" (DECISION_LOCK_ACADEMY:81) â€” reconcile: permanently off the table, or a live deferred design item.
- [AUTHOR DECISION] AD-T4: rulebook Â§7:232's "after-the-fact only" visibility decision vs the LOCK 8 deferral â€” banner as one option under the deferral or supersede.
- [AUTHOR DECISION] AD-T5: `00_EXECUTIVE_VERDICT.md:109` "woundable by priced failures" â€” extend the `:100` banner to mechanics or revise `:109` per LOCK 8 F-11.
- [AUTHOR DECISION] AD-T6: Arc II Contract #2 beats in `01_FIRST_3_ARCS.md:43-51` and `04_PROJECT_STATE/ANALYSIS/ARTHUR_POWER_DESIGN.md:49-71` â€” PROPOSED roadmap/analysis that the 2026-09-23 "UNDESIGNED/UNDECIDED" ruling leaves uncommitted; confirm they stay non-committal until an author decision.
- [UNKNOWN]: none new. (The two standing fences â€” 9/18 UNDETERMINED, SaitÅ's glance UNRESOLVED â€” untouched by this audit.)

### Structural gaps
- G-1: Relock mechanics unexamined by any lock (see AD-T2).
- G-2: "Mooring tier" vocabulary (`CONTRACT_SYSTEM_MASTERS.md:233`) is unlocked and paired with a numeric gauge ceiling â€” needs a banner or removal.
- G-3: Stale "[PROPOSED â€” pending user lock]" labels on Contract #1 in `12_MIXED_MISSION_SYSTEM.md:193/:235`, `18_SOCIAL_HIERARCHY_PROGRESSION.md:227`, `05_IRREGULAR_DARK_HORSE_ARC.md:192`, `HISTORIES_AND_TIMEmessaging app.md:114` â€” extend the deferred F-03/F-09/F-10 annotation sweep to cover them.
- G-4: `01_README_AND_INDEX.md:102-103` fix list predates LOCK 9 R-2 (item 5's "â†’ gauge threshold" fix is itself stale) â€” index needs a one-line update.
- G-5: No gauge-visibility decision â€” carried as deferred; ch13/ch15 beats are annotated staged-for-visible-meter with infer-only fallback (LOCK 9 R-9). No action until the future systems pass.

### Coordinator recommendations (need author approval before any file change)
- CR-1: Apply the author's mandated scheduled-event wording (*"the scheduled event becomes available once the required conditions are met â†’ Slot N unlocks (EMPTY; capacity â‰  acquisition)"*) to `00_PACING_AND_30_CHAPTERS.md:67/:73/:26`, `13_ACADEMY_RESTRUCTURE_REPORT.md:169`, `01_FIRST_3_ARCS.md:69`, `15_ACADEMY_30_CHAPTER_RESTRUCTURE.md:40`, `02_LONG_TERM_ROADMAP.md:25`, `01_README_AND_INDEX.md:103`.
- CR-2: Add one-line banners: `RULESETS.md` R1.2 (terminology superseded; relock mechanics deferred to AD-T2), `ARTIFACT_DESIGN.md:134` (numeric claim deferred/superseded under the :124 banner), `CONTRACT_SYSTEM_MASTERS.md` Â§7 (visibility option vs deferral; "Mooring tier" vocabulary).
- CR-3: Banner knock Â§10's "Contract #2 (Ledger)" sentence as [PROPOSED â€” not locked] per AD-T1 (recommended).
- CR-4: Extend verdict `:100` banner to cover `:109`'s mechanics per AD-T5.
- CR-5: Do not touch `AUDIT/500_QUESTION_AUDIT/*` â€” deliberation history, intentionally preserved.

**Files produced:** [track_b.md](sandbox://workspace/world_bible/work_rar/04_PROJECT_STATE/_lock12_scratch/track_b.md) (this report).
**Files modified:** none. **00_WORLD_BIBLE/** untouched.

