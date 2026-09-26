# PROSE NATURALNESS — ROOT-CAUSE AUDIT
## THE QUIET TIDE · why the engine produced TNE-overfit prose

> **Mode:** AUDIT ONLY. No prose rewritten or patched. No engine modified. No canon/lock changed. No Chapter 005 generated.
> **Sources audited:** `THE_QUIET_TIDE_WRITING_ENGINE.md` (Modules 01–23), `TNE_STYLE_GAP_ANALYSIS_FINAL.md`, `NARRATIVE_STYLE_BIBLE.md`, `NATIVE_ENGLISH_CALIBRATION_REPORT.md`, `FINAL_NATURAL_ENGLISH_REFINEMENT_REPORT.md`, `GENERATION/CHAPTERS/001_ERROR_UNDEFINED.md`, legacy `00_WORLD_BIBLE/CHAPTERS/001_The_Three-Second_Shadow.md` (REFERENCE ONLY).
> **Companion:** `DIALOGUE_NATURALNESS_ROOT_CAUSE_AUDIT.md`, `GENERATION_AUTHORITY_AUDIT.md`, `CH001_GENERATION_SOURCE_TRACE.md`, `REQUIRED_AUTHOR_DECISIONS.md`.

---

## 1. WHAT THE PROBLEM IS

The whole of the concern in one line: **the engine treats TNE's surface mechanisms as generation defaults instead of as gated registers, so the generator optimizes mechanism-density and produces prose that reads like an imitation of The Novel's Extra rather than naturally-written English.**

This is **not** a missing-rule problem. The engine already contains the correct naturalness rules (Module 01 Native English Gate; Module 22 readability; Module 23 NPE checks). It is an **ordering-and-framing problem**: the mechanism modules (03 Sentence, 04 Paragraph, 09 Dialogue, 13 Description) are written as executable checklists, while the naturalness gate is written as a downstream detection/reconstruction pass. A generator satisfying the checklists first will produce the TNE surface and only then be asked to "reconstruct" it — which is why the engine's own calibration examples keep reappearing.

---

## 2. SECTION D — ROOT-CAUSE MAPPING (TNE → QT distortion)

The task asked whether the engine has accidentally converted each TNE input into a distortion. Findings:

| TNE input | What the engine did | Distortion produced | Engine cause | Verdict |
|---|---|---|---|---|
| **TNE observation** (close, concrete noticing) | Imported P13 (one beat/paragraph), C25 (hard cuts), DV79 (functional detail) as ADOPT | **Sentence fragmentation** — normal actions split into staccato pieces ("Folder in. Reading. Form out.") | Module 03 §2–3 + Module 04 §1/§4; S3 fragments ADAPT with no rarity gate at composition time | **CONFIRMED** |
| **TNE economy** (inferable = unstated) | Imported Module 16 cut rules + concision guidance + "fast locally" | **Unnatural compression** — meaning thinned into clauses; aphoristic summaries replace explanation ("The work was the work. It fit.") | Module 16 cut rules; Module 03 concision priority; SOP short-sentence preference | **CONFIRMED** |
| **TNE tactical thought** (question→inference→options→decision) | Imported T46 as ADOPT, a "preferred default" shape | **Artificial slogan-like narration** — the thought grammar migrates from interiority into the *narration* as thesis lines ("The room allowed no doubt.") | Module 10 §1; Module 03 §4 concrete-verb/abstract-noun ban applied to the wrong target | **CONFIRMED** |
| **TNE dialogue economy** (compressed exchange) | Imported D50 (attribution starvation), P14, dialogue compression example | **Exposition disguised as dialogue** — clipped readouts and data-entry lines ("Family keepsake… Appraised 1987 — the record's attached.") | Module 09 §2–3; the "Three months."/"You're sure?" example trains clipping | **CONFIRMED** |
| **TNE minimal description** | Imported DV79 + "1–2 details per beat" + DV80 rationing | **Synthetic metaphor** — with detail rationed, the generator reaches for a striking comparison ("the way a punch clock takes its picture") | Module 13 §1–5; Module 01 patch detector is a QA pass, not a generation block | **CONFIRMED** |
| **TNE short sentences** | Repeatedly cites ~8.7 words; anti-drift "<10 words" threshold | **Mandatory short rhythm** — sentence-length variation collapses toward short declaratives | Module 03 §1 band vs. anti-drift #1; Gap Analysis S1 (DEFER) cited as 8.7 | **CONFIRMED** |

**Secondary causes:**
- **The four REJECTs are correctly excluded** (V42, K27, PC32, A59), so the problem is **not** the rejected absolutes; it is the **61 ADOPT/ADAPT mechanisms** being applied as surface devices.
- **The engine's calibration examples are the failure output.** `NATIVE_ENGLISH_CALIBRATION_REPORT.md` §2 lists seven historical examples as FAIL — the same examples that appear in the corpus. A gate that reliably *detects* but does not *prevent* indicates the gate is positioned after generation.
- **"Natural English" appears as a *priority list* but not as a *composition instruction*.** Module 01 states "NATURAL ENGLISH > CLEAR MEANING > …", but no module tells the sentence generator to *begin* from the natural sentence. Module 23's reconstruction rules are framed as repair.
- **Contrast-template residue.** Module 21 drift #2 bans "not X, but Y" and "He did not X. He Y." Yet the corpus shows the family repeatedly ("It was not a punishment. It was closer to filing."; "Informed, not consulted."). The rule exists but is a *drift check*, not a generation block.

---

## 3. SECTION E — THE NEW PROSE PRINCIPLE (AUTHOR DIRECTION — recorded, not yet engine-applied)

> **TNE is a STRUCTURAL INFLUENCE, NOT A SURFACE VOICE.** The Quiet Tide prose must read as naturally written English first.
> Do **NOT** force: 8.7-word average · short sentences merely because TNE uses them · fragments merely because TNE uses them · one-line paragraphs merely because TNE uses them · punchline-like narration · artificial staccato · compressed metaphors · gamer-like internal commentary · interface-like prose outside actual interfaces · slogan-like observations.
> Natural sentence length must vary according to meaning. A paragraph may contain short → medium → longer → short when that is how natural English communicates the thought. The reader should never feel "the author is trying to make this sentence short"; the reader should feel "this is simply how the character/narrator would say it."

**Engine implication (not applied here):** this principle must become the **first** instruction of the prose-composition modules, with the TNE mechanisms listed *under* it as optional registers.

---

## 4. SECTION H — DIAGNOSTIC CORPUS (15 CHAPTER-001 EXAMPLES)

Sources: `R` = reboot-generated `GENERATION/CHAPTERS/001_ERROR_UNDEFINED.md`; `L` = legacy `00_WORLD_BIBLE/CHAPTERS/001_The_Three-Second_Shadow.md` (REFERENCE ONLY). **No example is rewritten in this audit.** "What rule should replace it" names the replacement *rule*, not replacement prose.

---

**Example 1** `[R, L16]`
- **ORIGINAL:** "No one looked pleased and no one looked afraid. That was the part Arthur watched. The room was not frightening. It was not even cold. The room allowed no doubt."
- **PROBLEM TYPE:** Slogan-like thesis narration / clipped negative stack.
- **WHY UNNATURAL:** the final line states the scene's meaning as an aphorism; five short beats stack, so the paragraph reads as constructed emphasis rather than a person noticing.
- **WHICH ENGINE RULE CAUSED IT:** Module 03 §2–3 (staccato/fragments as tension register applied outside tension); Module 01 patch detector (abrupt essayistic register) is a downstream check, not a block.
- **WHAT RULE SHOULD REPLACE IT:** composition-order rule — narration must stay at the surrounding natural length; meaning is carried by concrete observation and behavior, and *no* thesis-slogan sentence may state what the scene should show.

---

**Example 2** `[R, L84]`
- **ORIGINAL:** "It was not a punishment. It was closer to filing. A thing that could not be sorted into the usual trays was sorted into the tray marked otherwise, and the tray was sent somewhere it would do no harm."
- **PROBLEM TYPE:** Extended metaphor chain / over-explanation.
- **WHY UNNATURAL:** the tray analogy is stretched over three sentences until it feels authored; the human inference ("it was not a punishment") is restated by the metaphor instead of left to the reader.
- **WHICH ENGINE RULE CAUSED IT:** Module 01 REWRITE-IN-PLACE / patch detector (paragraph-level) applied as post-hoc; Module 13 "functional description" gives no cap on metaphor chains.
- **WHAT RULE SHOULD REPLACE IT:** one natural statement of the inference; default literal phrasing; a comparison may appear only if it is natural to the POV and does not lengthen the idea.

---

**Example 3** `[R, L42]`
- **ORIGINAL:** "Something crossed his face, brief and unreadable, like a man who had reached for a drawer and found it empty."
- **PROBLEM TYPE:** Synthetic literary simile (register bump).
- **WHY UNNATURAL:** the simile is more literary than the surrounding procedural prose; it does emotional work the scene has not earned and reads as inserted.
- **WHICH ENGINE RULE CAUSED IT:** Module 01 literary-patch detector as QA; Module 13 DV80 rationing (leaves the simile permitted once "rationed," without requiring POV motivation).
- **WHAT RULE SHOULD REPLACE IT:** description must pass the four-step filter (noticed → why → what it tells him → what changes); a simile is allowed only if it is the way *this* POV would naturally see it.

---

**Example 4** `[R, L20, L28, L72, L124]`
- **ORIGINAL:** "the way a person stops noticing a clock that runs fast" / "the way pressure comes before weather" / "the way a person reads a shopping list" / "the way a person sounds when he has already heard a word and decided what it means."
- **PROBLEM TYPE:** Recurring simile tic ("the way X…").
- **WHY UNNATURAL:** four-plus instances across one chapter make "the way" a crutch; the construction substitutes a comparison for a concrete detail.
- **WHICH ENGINE RULE CAUSED IT:** Module 03 §5 tic set addresses "quietly/slowly/carefully" but not "the way X"; Module 21 drift #2 names templates but not this one.
- **WHAT RULE SHOULD REPLACE IT:** add "the way X…" simile tics to the banned-tic list; prefer the literal construction; ration comparisons per scene.

---

**Example 5** `[R, L38]`
- **ORIGINAL:** "Whatever was happening was happening in the machine, and the machine was being polite about it."
- **PROBLEM TYPE:** Artificial "cool" aphoristic narration.
- **WHY UNNATURAL:** the line is the author being clever, not Arthur observing; "polite" personifies the instrument and resolves the moment into a witticism.
- **WHICH ENGINE RULE CAUSED IT:** Module 10 T46 thought grammar applied at narration scale; Module 03 §4 (abstract/clever) not gated.
- **WHAT RULE SHOULD REPLACE IT:** narration = POV's natural noticing; no "clever line" whose only function is a strong paragraph ending (Module 01: "needed a stronger ending" is not a valid register reason).

---

**Example 6** `[R, L128]`
- **ORIGINAL:** "It had measured what it could measure. It had not pretended to measure more."
- **PROBLEM TYPE:** Parallel-declarative aphorism / "not X" contrast family.
- **WHY UNNATURAL:** the anaphora is a rhetorical device, not a filing clerk's plain inference.
- **WHICH ENGINE RULE CAUSED IT:** Module 03 §7 coordination preference; Module 21 drift #2 (contrast template) is only a drift check.
- **WHAT RULE SHOULD REPLACE IT:** state the inference once, plainly; treat "not X, but Y" / echo-declarative constructions as a generation-time block, not a QA flag.

---

**Example 7** `[R, L64]`
- **ORIGINAL:** "He noticed." (isolated as a one-line paragraph)
- **PROBLEM TYPE:** Forced one-line paragraph / emphasis fragment.
- **WHY UNNATURAL:** two words are isolated for drama; the emphasis is manufactured, not a real scene turn; it mimics TNE's isolated-beat habit.
- **WHICH ENGINE RULE CAUSED IT:** Module 03 §9 + Module 04 §6 (one-line paragraphs ≤2/scene) — the cap permits it, but no rule requires the sentence to *be* a scene turn.
- **WHAT RULE SHOULD REPLACE IT:** a one-line paragraph is allowed only for a genuine scene-turning/decision/silence beat; otherwise fold the sentence into its neighbor. Emphasis never purchased by layout alone.

---

**Example 8** `[R, L84]`
- **ORIGINAL:** "He let that sit."
- **PROBLEM TYPE:** Vague compressed reaction beat.
- **WHY UNNATURAL:** "let that sit" is a stock phrase that replaces a concrete physical/mental action; the reader cannot see what he does.
- **WHICH ENGINE RULE CAUSED IT:** Module 16 economy + Module 03 concision → stock compression; Module 01 concrete-verb default not enforced at composition.
- **WHAT RULE SHOULD REPLACE IT:** replace vague reaction beats with a concrete behavior or remove them; "economy" must not license clichés.

---

**Example 9** `[R, L56]`
- **ORIGINAL:** "The other cadets in the line had talked about the pressure, the pull, the first time the world had answered them. No one had ever answered him."
- **PROBLEM TYPE:** Lyrical-antithesis cadence / mild melodrama.
- **WHY UNNATURAL:** the closing antithesis lands as a written flourish; it lifts the register above the plain narration around it.
- **WHICH ENGINE RULE CAUSED IT:** Module 12 §3 undercutting imported as cadence; Module 13 lyrical register rationed but not restricted by POV.
- **WHAT RULE SHOULD REPLACE IT:** keep emotional lines flat and concrete (Module 10 §4 / Module 12 §1); avoid antithesis as a sentence-shape default.

---

**Example 10** `[R, L100]`
- **ORIGINAL:** "warm and quiet and entirely unexplained"
- **PROBLEM TYPE:** Modifier stack on a non-peak beat / light personification.
- **WHY UNNATURAL:** three modifiers cluster where the prose is otherwise plain; "quiet" softly personifies a stone.
- **WHICH ENGINE RULE CAUSED IT:** Module 03 §5 modifier scarcity (spend on peaks only) not enforced; Module 13.
- **WHAT RULE SHOULD REPLACE IT:** one concrete factual detail instead of a modifier stack; modifiers reserved for genuine emotional peaks.

---

**Example 11** `[L, L13]` *(engine calibration example #2)*
- **ORIGINAL:** "Arthur watched the order of it. Folder in. Reading. Form out."
- **PROBLEM TYPE:** Forced TNE fragments.
- **WHY UNNATURAL:** nominal fragments compress a normal process into a quasi-technical chant; the order carries meaning but the shape is a formula, not natural English.
- **WHICH ENGINE RULE CAUSED IT:** S3 fragments (ADAPT) + Module 03 §3 + P13 one-beat paragraphs applied as default.
- **WHAT RULE SHOULD REPLACE IT:** describe the process in complete, naturally-linked sentences; use a fragment only as a rare, motivated emphasis after complete-sentence stacks, never to "compress or imitate TNE."

---

**Example 12** `[L, L13]` *(engine calibration example #3)*
- **ORIGINAL:** "…the way a punch clock takes its picture."
- **PROBLEM TYPE:** Synthetic metaphor / decorative atmosphere.
- **WHY UNNATURAL:** the simile adds no necessary information and is more literary than its surroundings; it exists to create atmosphere.
- **WHICH ENGINE RULE CAUSED IT:** Module 01 literary-patch detector (post-hoc); Module 13 DV80; SOP §44 atmosphere guidance.
- **WHAT RULE SHOULD REPLACE IT:** literal phrasing unless a comparison is natural and adds information; description must pass the four-step filter; no atmospheric slogans.

---

**Example 13** `[L, L74]`
- **ORIGINAL:** "Informed, not consulted. That was the whole conversation."
- **PROBLEM TYPE:** Slogan narration / contrast-template.
- **WHY UNNATURAL:** the line is a crafted maxim; "That was the whole conversation" tells the reader how to weigh the scene instead of showing it.
- **WHICH ENGINE RULE CAUSED IT:** Module 16 economy; Module 21 drift #2 (contrast family) as a check only; Module 18 institutional-refusal rule recasts refusal as a "structural beat," encouraging maxims.
- **WHAT RULE SHOULD REPLACE IT:** show the refusal as behavior/dialogue and let the reader infer the summary; ban the "X, not Y. That was the whole [scene]." shape at composition time.

---

**Example 14** `[L, L120]`
- **ORIGINAL:** "The work was the work. It fit."
- **PROBLEM TYPE:** Tautological slogan / mechanical-prose template.
- **WHY UNNATURAL:** the tautology is an author's cadence; "It fit." states a thematic judgment the scene should earn.
- **WHICH ENGINE RULE CAUSED IT:** Module 21 drift #2 ("X was not the problem. Y was." family); Module 16 economy; Module 12 undercutting.
- **WHAT RULE SHOULD REPLACE IT:** replace the slogan with a concrete action or an in-voice observation; no sentence whose function is a thematic tag.

---

**Example 15** `[R, L128]`
- **ORIGINAL:** "Two readings and a stamp. It was, he thought, a fair system. It had measured what it could measure. It had not pretended to measure more."
- **PROBLEM TYPE:** Summary-motif + echoed declaratives (also flagged in the accepted-baseline do-not-repeat list).
- **WHY UNNATURAL:** the compressed summary and the parallel closing pair read as motif-management rather than thought.
- **WHICH ENGINE RULE CAUSED IT:** Module 16 economy; Module 03 §7; Module 21 drift #2.
- **WHAT RULE SHOULD REPLACE IT:** one plain sentence of inference; do not compact a scene's meaning into a reusable motif.

---

## 5. SECTION F — DESCRIPTION AUDIT

**Author-directed priority (recorded):**
1. what Arthur notices → 2) why he notices it → 3) what it tells him → 4) what changes because of it.

**Audit findings against the corpus:**
- The generator's default is **observational detail → immediate meaning**, often skipping step 2 (why this detail registers for *him*) and reaching for step 3 as a **summary** rather than a consequence.
- Description is not the main problem; the problem is that when the engine **rations** description, the generator compensates with **one synthetic comparison** per scene (Examples 3, 12) instead of more functional detail.
- **No automatic** literary metaphors, symbolic comparisons, "the way X…" constructions, poetic personification, or compressed atmospheric slogans should be permitted unless genuinely natural to Arthur's perception.

**Replacement rule:** every descriptive detail must pass the four-step filter. If a detail has no function (clue, positioning, characterization, cost), cut it rather than decorate it. Atmosphere comes from observation, silence, behavior, and pacing — never from a rare simile.

---

## 6. SECTION I(2) — QUANTITATIVE TNE MEASUREMENTS (never hard targets)

| TNE measurement | Where it appears | QT status | Generation rule |
|---|---|---|---|
| ~8.7 words/sentence | Engine Modules 03/23 + Gap Analysis S1 | **DEFERRED / STYLE CALIBRATION** | Must never be a target; "do not adopt 8.7" must be stated at composition time, not only in QA |
| 34.2% short sentences | TNE observation | **STYLE CALIBRATION** | Not adopted; no percentage target |
| 3–5 scenes | TNE chapter shape | **STYLE CALIBRATION** | QT's 2–4 typical (non-mandatory) band governs |
| 46% hook categories | TNE hook observation | **STYLE CALIBRATION** | QT's 12-ending-type rotation governs |
| Mandatory one-line paragraphs / fragments / staccato | TNE surface | **NOT ADOPTED** | Rationed devices only; never mandated |
| Anti-drift "<10 words" threshold | Engine Module 21 #1 | **DETECTION CUE ONLY** | Must be reframed as a cue with a "natural variation" qualifier; not a length goal |

---

## 7. RECOMMENDED ENGINE CHANGES (NOT APPLIED HERE)

1. **Composition-order rule** at the head of Modules 03/04/09/13: choose the natural sentence first; apply a TNE mechanism only if the sentence remains natural.
2. **Promote the Native English Gate** from Module 23 QA into the generation-time instruction sequence (before mechanism checklists).
3. **Demote S2/S3/S4/P13/C25/D50/D53** from default devices to **rarity-gated registers**.
4. **Add** "the way X…" simile tics and the contrast-template family to the generation-time block list.
5. **Remove/relabel numeric residue** (8.7, <10 words) as calibration/detection only.
6. **Frame economy** (Module 16) explicitly: concision never outranks natural flow; stock phrases are not economy.
7. **Add a "register-first" dialogue rule** (see dialogue audit).

---

*End of PROSE_NATURALNESS_ROOT_CAUSE_AUDIT.md — audit only. No prose rewritten; no engine modified.*
