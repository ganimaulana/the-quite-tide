# THE UNCARVED SEAL — PRIVATE CONTRACT UI — PROPOSAL

**Mode:** SYSTEM DESIGN + CANON COMPATIBILITY AUDIT
**Status:** PROPOSED / NON-CANON
**No canon changes. No lock changes. Nothing locked.**
**Date:** 2026-09-23 (documentation date; story year calibrated to 2024)

Label discipline: **[CANON-COMPATIBLE]** canon-consistent · **[PROPOSED]** new design, author decision required · **[ABSTRACT EXAMPLE]** synthetic illustration, assigns nothing to any canon Contract · **[DEFERRED]** undecided · **[CONFLICT]** contradicts canon, must not be adopted · **[AUTHOR DECISION REQUIRED]** needs explicit author choice.

Working vocabulary: **the Private UI** (final name **[AUTHOR DECISION REQUIRED]** — §21.1).

---

## 1. Purpose

The Private UI answers one question: **"What have I received?"** **[PROPOSED]**

A Contract is a *stored relationship* — settled terms witnessed and held by the Repository, the Seal's contract function: "a medium that witnesses, binds, and stores contracts... notary and vault, not a mind. It does not judge, advise, or intervene" **[CANON-COMPATIBLE]** (`CONTRACT_SYSTEM_MASTERS.md` §1). The UI is the notary's clerk-window, visible to Arthur alone.

What it must never answer: **"How do I perfectly exploit it?"** Information arrives progressively — settled terms at binding, discoveries only after world-certification, consequences only as priced events. A confirmation/interface system, not a walkthrough system. **[PROPOSED]**

> **The UI tells him what the binding says. The world tells him what the binding means. The first is the notary's job; the second is his.** **[PROPOSED]**

---

## 2. Interface philosophy

Three rules govern every line **[PROPOSED]**:

1. **Report what was witnessed.** Every line traces to a witnessed term, a timestamped prediction, a certified outcome, or a priced event. The UI invents nothing.
2. **Confirm only what the world certified.** Entry requires the locked grammar: falsifiable prediction, recorded *before* the test, phenomenon behaves as predicted — "the world is the certifier; the Repository is only the notary" **[CANON-COMPATIBLE]** (`CONTRACT_SYSTEM_MASTERS.md` §0.3).
3. **Say nothing about what comes next.** No recommendations, no warnings of what *might* happen, no highlighted lines. The UI has no forward gear.

The UI performs **no reasoning** — it displays; it never advises, judges, warns, encourages, or explains. Its tone is the notary's: terse, stamped, neutral, never celebratory — the Repository "is not a moral agent" **[CANON-COMPATIBLE]** (`CONTRACT_SYSTEM_MASTERS.md` Q115).

---

## 3. Visibility

**Private to Arthur, absolutely** — perceivable by no instrument and no other person **[PROPOSED; CANON-COMPATIBLE]** with Laggard masking (instruments log nothing anomalous) and the locked rule that formation emits only a brief *unclassifiable pressure signature*: witnesses may feel pressure, but there is nothing to read **[CANON-COMPATIBLE]** (LOCK 12 Layer 3).

**Event-driven, never a HUD.** The UI appears at the §4 triggers, delivers its lines, and fades — it does not persist, and cannot be summoned at will **[PROPOSED]**. Between triggers Arthur relies on his own records; re-reading settled terms is *his* work. (The summonable alternative: **[AUTHOR DECISION REQUIRED]** — §21.4.)

**Reader visibility:** the reader sees the UI only when Arthur does, as brief stamped lines inside normal novel prose — no status window, no stat block, no game pop-up grammar. **[PROPOSED]**

One honest cost: *using* the UI is itself observable. A witness who sees Arthur go still, eyes tracking nothing, has seen a man reading something that isn't there. The UI leaves no record — but its use is a secrecy event **[PROPOSED]**.

---

## 4. Trigger conditions

The UI surfaces **only** at these events **[PROPOSED]**:

1. **Contract formation** — at SETTLING the Repository "presents the terms as a pattern"; at BINDING it witnesses: records the terms, banks the Toll, spends the signing Depth, assigns the Mooring **[CANON-COMPATIBLE]**. The UI shows the §6 display once.
2. **Contract invocation** — a priced event is recorded: which Contract was addressed, that Depth was spent (event, no amount — §12), that no new Toll was banked.
3. **Contract consequence** — Toll banked at signing; temporary penalties as they land (e.g., "Mooring locked for stated cooldown" on condition-breach); permanent consequences as they occur (face-scar, scorch). Each reported once, as an event.
4. **New property discovery** — only after world-certification (§8).
5. **Contract development** — outcome-state changes, if ever designed (PARTIAL→FULL is **[DEFERRED]** — the UI pre-answers nothing).
6. **Artifact reaction** — refusal to witness, cooling/dormancy, micro-fracture accumulation crossing noticeability. Reported as *events*, never explained — the UI says the artifact refused; it never says why. Origin is fenced.
7. **Major resonance event** — a new binding's provenance, recorded once.
8. **Important restriction activation** — a restriction *firing* is reported as it happens. Activations, **never predictions**: no "this invocation would breach" warnings. A predictive warning is strategic advice — a walkthrough element, fenced as **[CONFLICT]** with §2.3. (Alternative: **[AUTHOR DECISION REQUIRED]** — §21.5.)

The UI never highlights which lines matter, suggests a next move, or summarizes "what this means for you." The reading is Arthur's. **[PROPOSED]**

---

## 5. Information hierarchy

Every line carries its certainty rank, highest first **[PROPOSED]**:

1. **SETTLED** — witnessed at binding; the terms as the Grantor settled them.
2. **RECORDED** — Arthur's own stated predictions, timestamped by the notary, awaiting the world's answer.
3. **CERTIFIED** — discoveries the world confirmed (§8). The map, as trued.
4. **PRICED** — costs paid: Depth events, banked Tolls, penalties landed, consequences incurred. The invoice record.
5. **UNRESOLVED** — known gaps: the binding implies terms that were never settled (the PARTIAL gap is the boundary instance).
6. **UNKNOWN** — never settled, never recorded, never priced. Honest silence.

A SETTLED restriction and a CERTIFIED discovery look different on the page; the reader learns to trust only what the hierarchy certifies. **[PROPOSED]**

---

## 6. Contract display model

At formation the UI presents this working field set. **Field names are illustrative, NOT locked** — final terminology is **[AUTHOR DECISION REQUIRED]** (§21.2) unless canon justifies a name. Each field carries its §7 state **[PROPOSED]**:

- **[CONTRACT FORMED]** — Slot/Mooring position; outcome (FULL / PARTIAL / FRAGMENT / FAILED) **[CANON-COMPATIBLE]** (locked outcome vocabulary, LOCK 8).
- **Authority** — who settled the terms: the phenomenon's Rule (non-sapient SETTLING) or a named Sapient Grantor.
- **Effect** — what the Contract *does*, as settled. Demonstrated terms only; nothing inferred.
- **Condition** — what must hold for invocation. (One confirmed demonstrated condition is the Contract #1 boundary: "it cannot cross what is bound" **[CANON-COMPATIBLE]**.)
- **Restriction** — what the Contract cannot do, or may only do under conditions. The UI lists them; converting them to leverage is Arthur's work.
- **Cost** — the price shape as settled: signing price, per-use pricing class, toll banked. Qualitative only — no numbers, ever (LOCK 8 numeric veto) **[CANON-COMPATIBLE]**.
- **Duration** — the duration class as settled, or UNRESOLVED. **[PROPOSED]** (duration mechanics are a future-Contract capability class, never Contract #1's.)
- **Compatibility** — which physical media the rules admit, or UNKNOWN. Validity is discovered by test, never read off the UI **[CANON-COMPATIBLE with the proposed design]** (weapon/medium proposal §2.2). The UI records *discovered* validity; it never *proposes* a medium.
- **Unresolved Properties** — count of known-but-unsettled gaps, never their content (§7).

The display is a *transcript of the binding*, shown once at formation, then gone. **[PROPOSED]**

---

## 7. Unknown/partial information

Six fog states **[PROPOSED]**:

- **KNOWN** — settled and witnessed.
- **PARTIALLY KNOWN** — settled in part; the settled part shown, the gap marked.
- **UNKNOWN** — never settled; the field shows with no content rather than omitted. Absence is information.
- **UNRESOLVED** — the binding *implies* content never settled. The UI may show a count ("1 UNRESOLVED") — a structural fact, like the PARTIAL gap-stroke — never the content.
- **UNCLASSIFIED** — content not fitting the field set; held aside, not forced into a field.
- **INSUFFICIENT DATA** — the answer to fenced material: Artifact origin, ERROR/UNDEFINED, future Contracts. Not "classified" (which implies someone knows) — *insufficient*: the notary genuinely has nothing to transcribe. **TRUE FUNCTION: UNKNOWN** is a legitimate permanent state.

Two fences. **(1) The notary never invents content** — where nothing was settled, the UI is silent or shows a fog state; silence is the honest answer and keeps the UI from becoming an oracle. **(2) Sapient Grantor omissions are preserved** — "the Repository never hides clauses; Sapient Grantors may omit what Arthur doesn't ask — adversarial disclosure" **[CANON-COMPATIBLE]** (`CONTRACT_SYSTEM_MASTERS.md` Q122). The UI transcribes only what was *settled*; the UI must never fill the omission, or negotiation becomes decorative. **[PROPOSED]**

---

## 8. Discovery confirmation

A proposition passing the locked certification grammar earns one confirmation line **[PROPOSED]**:

**[PROPERTY DISCOVERED]** — category (rule / restriction / application / failure-mode / interaction / efficiency / control / compatibility — mastery proposal §3 **[PROPOSED]**) — the proposition, as certified.

1. **No certification, no confirmation.** Luck banks nothing ("accidental solves do not count" **[CANON-COMPATIBLE]**); the UI stays silent. His confidence is not evidence.
2. **The UI never validates a misreading.** Felt-certainty — the knock *confirming a misreading with full conviction* **[CANON-COMPATIBLE]** (LOCK 8) — is the Contract's behavior, not the UI's. The UI reports only what the world certified; it will not correct him *before* the world does, nor confirm him *instead of* the world.
3. **A record line, not a level-up.** No fanfare, no reward. The map is truer; nothing else changed. Entries append under their category.
4. **Recording a prediction.** When Arthur states a falsifiable prediction for timestamping, one minor line appears: "Prediction recorded — awaiting the world's answer." Record information, not advice. **[PROPOSED]**

The loop the UI serves — OBSERVE → HYPOTHESIS → TEST → RESULT → UPDATED HYPOTHESIS → SECOND TEST → DISCOVERY — keeps Arthur the solver: the UI is the scoreboard the *world* writes on, never the coach. **[PROPOSED]**

---

## 9. Artifact relationship

THE UNCARVED SEAL → provides access/interface → stores/anchors Contracts through Slots **[CANON-COMPATIBLE]** (LOCK 8: 12 faces → 6 active Contract slots maximum). The UI is the *read interface* to what the Repository witnessed and recorded — it adds no content of its own. **[PROPOSED]**

**Slot/Face inventory.** Faces carve as impressions bind, visible in the stone **[CANON-COMPATIBLE]**. The UI may report *structural* facts ("Slot 2: FREE — unbound capacity") — witnessed facts, not power. But it never meters: no progress bars, no "slot progress," no unlock countdown. Slot #2 opens end-Nov 2024 and stays EMPTY in Arc I **[CANON-COMPATIBLE]** (LOCK 8) — reported as a structural event, not solicited. An empty slot is not a quest. **[PROPOSED]**

**The 13th face.** One permanent line: **UNREADABLE** — never elaborated. The thirteenth face is NOT a slot; its function is a budgeted mystery **[CANON-COMPATIBLE]** (LOCK 8). Any UI content implying a thirteenth function is **[CONFLICT]**. **[PROPOSED]**

**Refusal.** The artifact refuses V/I-flag sources, un-addressable phenomena, suicide-terms — "the refusal list doubles as a mystery engine" **[CANON-COMPATIBLE]**. The UI reports the event ("the Repository declined to witness these terms") and offers no reason — the reason would explain the artifact, which is fenced. **[PROPOSED]**

---

## 10. Body Pattern relationship

The separation is exact **[PROPOSED]**: **PRIVATE UI** → information · **ARTIFACT PATTERN** → Contract/Slot structural manifestation · **BODY PATTERN** → physical manifestation/record/consequence · **ARTHUR** → interpretation and application.

The pattern is a *record* — grants nothing, meters nothing **[PROPOSED; consistent with the body-pattern proposal]**. The UI never displays pattern state as a progress readout. It may *reference* the pattern where the channels touch one event (e.g., at binding: "Seed-motif registered — SENSED"; stages UNREGISTERED → SENSED → TRACED → LEGIBLE → INTEGRATED are the pattern proposal's vocabulary **[PROPOSED]**), but pattern clarity is the body's business. **[PROPOSED]**

**Channel discipline: Toll = FELT; pattern = SEEN** **[PROPOSED]** (cost proposal §8). The UI reports "Toll banked: 1 mark" once at signing and never narrates the ache — chronic symptoms belong to Toll, locked. It reports pattern-affecting events (scorch, weathering) as *consequence* lines, never as meters. The UI is the clerk-window onto the two channels, not a third one. **[PROPOSED]**

**Not a second power system:** no scene may have the UI *do* what the Contract underneath doesn't do (pattern proposal §8.1). A UI line granting capability is **[CONFLICT]**. **[PROPOSED]**

---

## 11. Resonance relationship

RESONANCE = the event/state necessary for Contract formation — **not a currency** **[CANON-COMPATIBLE]** (LOCK 8; LOCK 12 Layer 4):

- At formation, one provenance line: the binding exists because a genuine firsthand solve occurred (ANOMALY → SOLVED → RESONANCE → CONTRACT FORMATION **[CANON-COMPATIBLE]**). Provenance, not points.
- The UI never shows "Resonance" as quantity, level, or progress bar — no "Resonance Level 1/2/3." The superseded "Current/Lifetime Resonance" vocabulary is **forbidden** in the UI; its appearance is **[CONFLICT]** (LOCK 12 §2: SUPERSEDED). **[PROPOSED]**
- Invocations do not "spend Resonance" — the invocation record (§12) names DEPTH, never Resonance. **[PROPOSED]**

Resonance is the *reason there is a binding to display*; it is never displayed as a resource. **[PROPOSED]**

---

## 12. DEPTH relationship

DEPTH = the invocation resource — Current (spendable, refillable only through new certified solves) and Lifetime (cumulative, **never decreases**) **[CANON-COMPATIBLE]** (LOCK 8; LOCK 12 Layer 4). UI reporting is built for the deferred visibility question:

- **Event records, never amounts.** "Signing priced — Depth spent (event)"; "Invocation priced — Depth spent (event)"; "Invalid attempt priced — Depth spent, no effect" (weapon/medium proposal §2.3 **[PROPOSED]**). No numbers, ever — numeric veto locked (LOCK 8); gauge visibility **[DEFERRED]** (AD-12-3).
- **Visibility-model independence.** Works under either surviving candidate model (infer-only or visible): the UI records that a price was paid without showing a balance, and never implements an "after-the-fact only" display (UNSAFE/CONTRADICTORY TO LOCK 8 per AD-12-3). **[PROPOSED]**
- **Lifetime Depth** is never totaled, never gates anything, never appears as a threshold — "a historical measure, never a currency" **[CANON-COMPATIBLE]** (LOCK 8 §1). As a spendable number it is **[CONFLICT]**.
- **DEPTH is never XP.** No bars, no "+10," no thresholds. A priced event is an invoice line, not a reward. **[PROPOSED]**

The UI is *Depth-honest without being Depth-visible*: reader and Arthur always know a price was paid; neither is shown a balance. **[PROPOSED]**

---

## 13. Cost / Toll relationship

The five tiers — RULE / COST / TOLL / TEMPORARY PENALTY / PERMANENT CONSEQUENCE — stay distinct; the UI never aggregates them into "total cost" **[PROPOSED; CANON-COMPATIBLE with the cost architecture]**:

| Tier | UI treatment |
|---|---|
| **1. RULE** | The §6 field set — the shape of the possible. Never labeled a cost. |
| **2. COST** | Depth events per §12. Sunk, never refunded on misread (ch15) **[CANON-COMPATIBLE]**. |
| **3. TOLL** | One line per signing: "Toll banked: 1 mark — permanent." No countdown, no currency, no trade — the invoice he cannot negotiate down **[CANON-COMPATIBLE]** (LOCK 8). |
| **4. TEMPORARY PENALTY** | Events with stated terms: "Mooring locked for stated cooldown" (condition-breach) **[CANON-COMPATIBLE]** (LOCK 8 L8-6); watchlist notes; exposure events. Temporary in mechanism — the lost opportunity is not. |
| **5. PERMANENT CONSEQUENCE** | Reported once, never reversed: kill-scarred face ("never to hold another impression") **[CANON-COMPATIBLE]** (LOCK 8 L8-5); scorch; weathering. The UI records; it does not mourn. |

**Paying more never buys more** — no trade loop, no "spend X for Y," no price-proportional benefit. The invoice is permanent where it matters (Toll, Tier 5), temporary where it heals (Tier 4), always upstream of the benefit **[CANON-COMPATIBLE]** (price-upstream doctrine). **[PROPOSED]**

---

## 14. Anti-LitRPG safeguards

Fenced at the design level **[PROPOSED]**:

1. **Blacklisted vocabulary:** HP, MP, STR, DEX or any attribute; LEVEL or numeric holder-rank; XP or progress percentages; QUEST / MISSION / OBJECTIVE lines; SKILL POINTS or advancement tokens; kill-counts or quotas; rarity tiers; "NEW SKILL UNLOCKED" or grant language. Any appearance is **[CONFLICT]** unless a future author decision independently justifies it.
2. **No objectives issued.** An empty Slot is a structural fact, not a prompt. A fog state is a record, not a hint.
3. **No optimal strategy.** Restrictions are listed, never ranked, never highlighted, never turned into suggested applications. Strategy is the solver's job.
4. **No numbers as progress.** Counts appear only as *structural* facts (Slots held, PARTIAL-implied gaps) — never as advancement. A count that reads as "progress toward" something is cut.
5. **No gamified voice.** No congratulations, no warnings, no familiar address. Celebration would imply the system *wants* something from him — it doesn't.
6. **No pop-ups outside triggers.** §4 is exhaustive. Training, studying, ordinary life never summon the UI.
7. **Discoveries budgeted like revelations, not loot** — ~one load-bearing discovery per arc-segment, each priced visibly (progression proposal §9 **[PROPOSED]**). The confirmation line must never arrive often enough to feel like drops.

---

## 15. Anti-omniscience safeguards

The UI is bounded by what the Repository witnessed — **not omniscient** **[PROPOSED]**:

1. The artifact may not understand everything: where the binding never settled content, the UI shows fog states (§7). "The notary transcribes; it does not investigate."
2. **Never the origin.** Artifact origin: INSUFFICIENT DATA, permanently, until the author decides otherwise. No origin theory is implied.
3. **Never ERROR/UNDEFINED.** No line explains his classification, his Seal compatibility, or why the evaluation broke (fenced: LOCK 12 §6). A line touching them is **[CONFLICT]**.
4. **Never future Contracts.** The UI knows only bound Contracts — no hints about the next binding, what Slot #2 is "for," or what phenomena await. Slot #2's opening is structural (§9), not a preview.
5. **Never the Grantor's mind.** Settled terms are transcribed; intent and omissions are not. Adversarial disclosure survives the UI intact (§7.2).
6. **Never unverified structure.** The unrevealed Under-pattern is noise, not a puzzle preview (pattern proposal §8.4 **[PROPOSED]**). The UI never sketches the whole figure.
7. **TRUE FUNCTION: UNKNOWN is terminal.** Some lines never resolve — that is the design, not a bug.

---

## 16. Contract #1 compatibility

THE POLITE KNOCK stays exactly what LOCK 8 locks: **Contract #1, PARTIAL, foundational, weak combat utility** — presence-only, demonstrated-only, one-knock-per-phenomenon-ever, one confirmed demonstrated condition ("it cannot cross what is bound"), per-use tier-scaled Depth, signing = FIRST WATER + Depth + 1 toll-mark ("his knuckles ache before it rains"), binding ≈ ch12 / 25 Sept 2024 **[CANON-COMPATIBLE]**. Nothing here redesigns it. Its formation readout — illustrative, locked facts only **[PROPOSED rendering of CANON-COMPATIBLE content]**:

> **[CONTRACT FORMED]**
> Slot 1 — Mooring HELD. Outcome: **PARTIAL**.
> **Authority:** KNOWN — settled with the phenomenon's Rule (non-sapient; the Repository presented the terms as a pattern; the Rule stabilized into them).
> **Effect:** KNOWN — one confirmed sentence of demonstrated terms: *"it cannot cross what is bound."*
> **Condition:** KNOWN — one confirmed demonstrated condition; PARTIALLY KNOWN — invocation through the unresolved gap carries hazard (AD-1).
> **Restriction:** KNOWN — demonstrated-only; presence-only; one-knock-per-phenomenon-ever; non-sapient targets.
> **Cost:** KNOWN — signing: FIRST WATER + Depth + 1 toll-mark. Per-use Depth, tier-scaled. Qualitative only.
> **Duration:** UNRESOLVED — no duration class settled.
> **Compatibility:** UNKNOWN — zero-medium; the knock's channel is presence itself. Any medium assignment is **[CONFLICT]** (weapon/medium proposal §1.4).
> **Unresolved Properties:** 1 — the PARTIAL gap. Terms exist that were never settled.
> **Toll banked:** 1 mark — permanent. *"His knuckles ache before it rains."*
> **TRUE FUNCTION:** UNKNOWN.

The gap is the point: Contract #1's UI is *visibly incomplete from the first day* — the reader sees the hole long before Arthur maps around it. **[PROPOSED reading of locked facts]**

What the UI does **not** show for #1: no strategy, no "recommended phenomena," no reason for the gap, no hint it is mappable. Felt-certainty (ch15) remains fully possible *under* this UI — it will not save him from his own misreading, because it confirms only what the world certified (§8.2). **[PROPOSED; CANON-COMPATIBLE]**

---

## 17. Contract #2 protection

Contract #2 is **UNDESIGNED / UNDECIDED** **[CANON-COMPATIBLE]** (AD-12-1), protected structurally **[PROPOSED]**:

1. **No field presumes a future Contract** — every §6 field is content-agnostic.
2. **Slot #2's UI behavior is content-free:** at opening (end-Nov 2024, EMPTY in Arc I **[CANON-COMPATIBLE]**) the UI reports one structural line — "Slot 2: FREE — unbound capacity" — and nothing else. No prompt, no countdown.
3. **§18's examples are synthetic** — labeled **[ABSTRACT EXAMPLE]**, capability-class illustrations only. They assign nothing to any real Contract.
4. **The UI cannot preview** — no "next Contract" line, no phenomenon scan, no Grantor radar. Acquisition happens in the world; the UI meets it at the binding, never before.

---

## 18. Example abstract UI states

**[ABSTRACT EXAMPLE]** — synthetic, grammar illustrations only. Not Contract #2, not Contract #1, not any designed Contract. Resemblance to future content is coincidental and must be discarded at design time.

**A — formation (synthetic; duration-class + medium illustration):**

> **[CONTRACT FORMED]**
> Slot 3 — Mooring HELD. Outcome: FULL.
> **Authority:** KNOWN — settled with the phenomenon's Rule (non-sapient; SETTLING).
> **Effect:** KNOWN — [abstract: "marks what the holder's hand has touched while the mark holds"].
> **Condition:** KNOWN — [abstract: "the holder must be touching the mark's surface"].
> **Restriction:** KNOWN — [abstract: "one phenomenon per mark; marks fade at tide-turn"].
> **Cost:** KNOWN — signing priced (Depth event); Toll banked: 1 mark — permanent.
> **Duration:** PARTIALLY KNOWN — [abstract: "persists while the marked surface endures"; end-conditions UNRESOLVED].
> **Compatibility:** PARTIALLY KNOWN — [abstract: "one medium class discovered by test"; others UNKNOWN].
> **Unresolved Properties:** 0 — all offered terms settled.
> **TRUE FUNCTION:** UNKNOWN.

**B — invocation priced:**

> **[INVOCATION]**
> Contract: [abstract — Slot 3]. Addressed through [abstract: a medium of the discovered class].
> **Price:** paid — Depth spent (event recorded; no amount shown).
> **Toll:** none re-banked. Toll is banked once, at signing.
> **Restrictions:** none triggered.
> The world answers. The phenomenon's behavior is the only record that matters.

**C — discovery confirmed:**

> **[PROPERTY DISCOVERED]**
> Category: Restriction — [abstract: "the effect does not cross running water"].
> Certification: prediction recorded before the test; phenomenon behaved as predicted.
> The map is truer. Nothing else changed.

Stamped, terse, no address, no celebration, no advice: a clerk stamping the notary's book — the drama is in what the lines *mean*, and meaning is Arthur's work. **[PROPOSED]**

---

## 19. Risks

| # | Risk | Mitigation — [PROPOSED] |
|---|---|---|
| 1 | **Tutorializer drift** — explaining becomes advising becomes guiding. | §2's rules + §4's no-predictive-warning fence. Any advisory line is CONFLICT. |
| 2 | **[PROPERTY DISCOVERED] reads as level-up.** | Record-line presentation; discovery budgeting; no reward language, ever. |
| 3 | **Fog counts become meters** ("2 UNRESOLVED" as progress bar). | Counts only where the binding structurally implies incompleteness; never summed across Contracts. |
| 4 | **Mysteries resolved by implication** — a placed UNKNOWN tells too much. | §15.6: the unrevealed is noise, not a puzzle preview; fog placement reviewed per beat. |
| 5 | **UI voice becomes a character.** | Stamped register, no address, no humor. The notary is furniture. |
| 6 | **UI–pattern channel blur.** | §10: the UI references pattern events, never tracks pattern state; chronic symptoms stay with Toll. |
| 7 | **Interrogation risk** — someone realizes he reads *something*. | Detection-economy consequence: no external record, but use is observable (§3). His cover story is a character problem. |
| 8 | **The UI narrates the Contract system** instead of dramatizing it. | The UI transcribes *his* Contracts only; system exposition stays in prose and institutions. |

---

## 20. Canon compatibility

### 20.1 LOCK 8 — COMPATIBLE

Terminology verbatim (RESONANCE = event/state; DEPTH = resource, Lifetime never decreases; FULL/PARTIAL/FRAGMENT/FAILED; one toll-mark per FULL/PARTIAL); Contract #1 as boundary only, zero-medium, no redesign; no Academy auto-detection (private UI; unclassifiable pressure signature); 6-active-slot maximum; 12 physical faces/markers remain separate from active-slot count; the 13th face is not an active Contract slot. **[CANON-COMPATIBLE]**

### 20.2 LOCK 12 — COMPATIBLE

The iron rule POWER ≠ CONTRACT ≠ DEPTH ≠ INSTITUTIONAL ≠ CHARACTER holds. The UI is **not a sixth layer and not a currency**: an information interface to the Contract layer, epistemic like Mastery, spendable by no one, granting nothing. It never moves Rank, grants channeling, makes Depth XP, or converts Toll to leverage. **[PROPOSED placement; CANON-COMPATIBLE]**

### 20.3 Repository canon — COMPATIBLE BY CONSTRUCTION

"The Repository is only the notary that timestamps the prediction"; "a medium that witnesses, binds, and stores contracts... It does not judge, advise, or intervene" **[CANON-COMPATIBLE]** (`CONTRACT_SYSTEM_MASTERS.md` §§0.3, 1). The UI is the read interface to exactly that function. "The Repository never hides clauses; Sapient Grantors may omit what Arthur doesn't ask" **[CANON-COMPATIBLE]** (Q122) — preserved in §7.

### 20.4 Sibling proposals — COMPATIBLE

Progression (six-concept separation untouched) · Mastery (UI confirms only loop-certified discoveries; the eight categories are its filing vocabulary) · Cost/consequence (five tiers distinct; Toll = FELT, pattern = SEEN, UI = clerk-window) · Body pattern (record-only; never metered) · Weapon/medium (validity recorded only after discovery by test; knock stays zero-medium). **[PROPOSED]**

### 20.5 Parallel audits — NOT DEPENDED ON

The integration and Assessment Array audits run in parallel by other agents. Where this proposal touches their subject matter it is marked **[PROPOSED]** or **[DEFERRED]** and assumes nothing of their outcomes — no conflict by construction: the UI is private to Arthur and orthogonal to institutional systems. **[PROPOSED]**

---

## 21. Deferred decisions

1. Final interface name (candidates: *the Impression*, *the Answering*, *the Quiet Terms*).
2. Final §6 field names (illustrative in this proposal).
3. Modality — recommended: *the pressed impression* (terms pressed into awareness: brief, private, fading; seal-ontology fit). Alternatives unevaluated.
4. Summonability — recommended: event-driven only; alternative: on-demand re-reading.
5. Predictive warnings — recommended: never (CONFLICT with anti-walkthrough); alternative: imminent-breach warnings.
6. Depth visibility model — AD-12-3 deferred; this design needs no numeric display under any candidate model.
7. Slot/face inventory display — recommended: structural facts only; alternative: silence on Slots.
8. Solve-grade disclosure scaling (PROPOSED Q122) — not adopted; would govern §6's initial fog distribution if ratified.
9. "Prediction recorded" lines — recommended: shown; alternative: silent timestamps.
10. FRAGMENT/FAILED UI behavior — reporting granularity for failed formation attempts.

---

## 22. AUTHOR DECISION REQUIRED

1. The **notary read-interface thesis** (§§1–2) — or an alternative conception.
2. The **§6 field set** (Authority / Effect / Condition / Restriction / Cost / Duration / Compatibility / Unresolved Properties) — or replacement names.
3. The **event-driven, non-summonable** visibility model (§3) — or on-demand re-reading.
4. The **fog-state taxonomy** (KNOWN / PARTIALLY KNOWN / UNKNOWN / UNRESOLVED / UNCLASSIFIED / INSUFFICIENT DATA) — or an alternative.
5. The **no-predictive-warnings** fence (§4) — or permitted imminent-breach warnings.
6. The **event-record Depth reporting** (§12) — or a different treatment.
7. The **modality recommendation** (*the pressed impression*) — or an alternative.
8. The **canonical interface name** (§21.1).
9. The **[PROPERTY DISCOVERED] grammar** (§8), including "Prediction recorded" lines.
10. The **Contract #1 worked rendering** (§16) as the prose template for formation readouts.

---

## Final Status

**PROPOSED / NON-CANON. AUTHOR DECISION REQUIRED.**

No canon changed. No lock changed. LOCK 1–14 untouched. FINAL_WORLD_BIBLE untouched. No chapter prose. Contract #1 as locked boundary only. Contract #2 not designed — not named, not hinted, not previewed. Artifact origin unresolved. ERROR/UNDEFINED unresolved.

**The UI is the notary's clerk-window — it tells Arthur what the binding says, the world tells him what it means, and a truer map is the only upgrade the system will ever offer.**


