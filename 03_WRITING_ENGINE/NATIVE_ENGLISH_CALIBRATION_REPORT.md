# Native English Calibration Report — Chapters 001–004

## Final Status

**CALIBRATION PASS WITH STYLE GAPS — ENGINE NEEDS ONE MORE REVISION**

## 1. Executive Summary

This was a read-only style calibration of the current flow-repaired Chapter 001–004 prose
against the Native English Naturalness Gate and Natural Prose Reconstruction rules. The
seven historical examples are recognized by explicit engine examples or checks. The engine
also catches several remaining style-only drifts in the current corpus, including
compressed metaphors, unusually elevated narration, dialogue with a report-like cadence,
and compressed figurative summary.

The main gap is operational calibration, not an absent category of rule: the engine names
patch detection, continuous authorship, thought/register continuity, natural dialogue, and
paragraph-level reconstruction, but a few sample passages still survive in the corpus
despite matching those diagnostics. The current gate therefore detects the problems in
principle but does not yet reliably cause a fail on borderline literary-compression and
discourse-rhythm examples. One additional style-only revision should sharpen the paragraph
decision threshold and give calibration examples from the current corpus. No story or author
decision is required for the cited findings.

No prose was changed. This report is the only file created or modified for this test.

## 2. Seven Historical Example Tests

| # | Example | Classification | Detection and rationale |
|---|---|---|---|
| 1 | `"Family keepsake," he said. "Stone seal, uncarved. Appraised 1987 — the record's attached."` | **FAIL — SENTENCE RECONSTRUCTION** | The Module 01 reconstruction calibration gives this exact dialogue as a data-entry-like example. Dialogue Reconstruction and NPE-06 also catch speech that sounds like a database entry rather than something said aloud. The exchange can be reconstructed as natural speech without changing its facts. |
| 2 | `Arthur watched the order of it. Folder in. Reading. Form out.` | **FAIL — SENTENCE RECONSTRUCTION** | The exact fragment sequence is flagged in Module 01 and Module 03. The staccato rule says fragments are not a metric; Patch Detection catches a formula fragment, and NPE-05 requires rejection when forced. As an isolated fragment group, sentence-group reconstruction suffices; with its following sentences, evaluate the whole paragraph. |
| 3 | `Whatever the instruments did, they did it the same way every time, the way a punch clock takes its picture.` | **FAIL — SENTENCE RECONSTRUCTION** | Module 01 names the exact punch-clock simile under literary patching. The phrase adds an unnatural metaphor without necessary information; use a literal sentence if the meaning is needed. NPE-07 and the Native Reading Test catch the register/continuity mismatch. |
| 4 | `the boys around him — seventeen, all of them, intake folders clutched like rail tickets` | **FAIL — PARAGRAPH RECONSTRUCTION** | The full assessment-hall excerpt and this exact phrase are in Module 01's reconstruction calibration. The age insertion and rail-ticket simile make the line feel constructed within otherwise direct description. Patch Detection, NPE-01, NPE-02, NPE-07, and the Native Reading Test require reading and reconstructing the whole sentence/paragraph, not replacing one collocation. |
| 5 | `She hung up, delivering the actual ritual — not the text, but the dinner.` | **FAIL — SENTENCE RECONSTRUCTION** | The exact example appears in the Native English calibration block. Collocation/MTL smell catches `delivering the actual ritual`; literary patching and NPE-03/NPE-08 catch the translated abstraction. The simple actions can carry the intended meaning. |
| 6 | `And your father is going to ask about your job, so prepare a sentence.` | **FAIL — SENTENCE RECONSTRUCTION** | The exact example is paired with a natural alternative in Module 01. The collocation check flags `prepare a sentence`; the dialogue test flags a literal, overly constructed casual line. NPE-06/NPE-08 are direct checks. |
| 7 | `You'll actually come. Not the thing where you say yes and sleep until midnight.` | **FAIL — SENTENCE RECONSTRUCTION** | The exact example appears in Module 01's calibration table. MTL smell and translation-shadow checks flag the `the thing where` construction and the unusually split question/statement cadence. One-Read may pass, but the Native Reading Test and NPE-03/NPE-06 should fail it for naturalness. |

These are calibration classifications only. No example was edited or treated as canon.

## 3. Chapter 001–004 Sample Tests

Status abbreviations: **P** = pass; **D** = drift/failure detected by the current engine. For
each sample, the 12 results are listed in NPE order (01 through 12). “D” is a style-only
finding, not a chapter acceptance decision. Institutional terms and purposeful
understatement were not penalized.

### Sample 1 — Chapter 001, opening queue observation (lines 8–16)

> Arthur counted forty-one cadets through the assessment room before they called his name.
> He had not started counting on purpose. The line moved at a steady rate, one cadet every
> few minutes, and after the first ten he had begun checking the rate against the clock to
> see whether it held. It held. The intake was efficient, and that told him more than the
> pamphlet from the district office, which had been mostly photographs.

**NPE:** P, P, P, P, P, P, P, P, P, P, P, P.

**Notes:** Continuous observation → test → inference. `It held` is short but natural and
motivated by the measurement beat, not a TNE formula. “Intake” is context-appropriate. The
repetition is Arthur's measured thought, not inserted summary.

### Sample 2 — Chapter 001, observation of the examiner (lines 30–42)

> He watched the examiner's face, because the examiner was the only part of the procedure
> that could tell him anything. ... Something crossed his face, brief and unreadable, like
> a man who had reached for a drawer and found it empty.

**NPE:** P, **D**, P, P, P, P, **D**, P, P, P, P, P.

**Notes:** The thought path is coherent and restrained. `the only part of the procedure
that could tell him anything` is mildly over-abstract, and the drawer simile is more
literary than surrounding procedural prose; the latter risks feeling inserted. Patch
Detection and the Native Reading Test should flag this for a sentence/group pass. The simile
is not inherently prohibited, but its POV motivation and register fit are weak here.
**STYLE-ONLY.**

### Sample 3 — Chapter 001, counter conversation (lines 72–96)

> "Subject, age seventeen. Classification, Irregular." ... "Division, Intelligence.
> Curriculum, Intelligence Operations." ... "That's what it says." ... "Is the ERROR
> re-measured?" / "Annual re-examination. It's on the sheet."

**NPE:** P, P, P, P, P, P, P, P, P, P, P, P.

**Notes:** The clerk's clipped speech belongs to the readout task and is intentionally
procedural; it is not casual dialogue pretending to be natural conversation. Locked labels
and formal terms are justified. Arthur's question is plain. Register remains stable within
the exchange.

### Sample 4 — Chapter 001, classification inference (lines 82–86)

> The machine had measured nothing it could use, so the system had stopped trying to use him
> and started trying to store him. It had put him in the division that read things, the
> curriculum that read things, and the posting where the records lived. It was not a
> punishment. It was closer to filing. A thing that could not be sorted into the usual trays
> was sorted into the tray marked otherwise, and the tray was sent somewhere it would do no
> harm.

**NPE:** **D**, **D**, P, P, P, P, **D**, **D**, **D**, P, P, P.

**Notes:** The central insight is in character, but the repeated `use/store/file/tray`
metaphor chain grows into an extended author-shaped explanation. “The posting where the
records lived” and the final tray sentence make the paragraph feel assembled around a
clever analogy. Patch Detection, thought continuity, and Native Reading Test should trigger
paragraph reconstruction while preserving the institutional inference. **STYLE-ONLY.**

### Sample 5 — Chapter 002, work observation and analysis (lines 14–26)

> He counted the shelves and the folders on one shelf and stopped, because the number was
> not the problem. The problem was the rule. ... Date was how you found a thing once you knew
> what it was. It was not how you decided where a thing belonged.

**NPE:** P, P, P, P, P, P, P, P, P, P, P, P.

**Notes:** Repeated “the problem” is deliberate emphasis and immediately followed by a
specific explanation. The paragraph tracks observation → inference → action, and the
fragments are not forced. “Date-sorter” is a useful concrete label, not unnecessary
technicality.

### Sample 6 — Chapter 002, social scene and dialogue (lines 72–92)

> "First week?" — friendly, almost kind — and then he saw Arthur's badge. His tone stayed
> friendly, but the friendliness no longer included Arthur. ... "I was reading the room."

**NPE:** P, P, **D**, P, P, P, **D**, P, P, P, P, P.

**Notes:** The dialogue is spoken and situational. `his tone stayed friendly, but the
friendliness no longer included Arthur` repeats the same abstraction and risks an
inserted-literary feel. It resembles the engine's own diagnostic pattern “the friendliness
stopped being for him.” Patch Detection and collocation/narration tests catch it; a local
sentence or group reconstruction is sufficient unless read with adjacent explanatory
sentences, in which case judge the full paragraph. **STYLE-ONLY.**

### Sample 7 — Chapter 002, Hayes's institutional warning (lines 108–120)

> "A records clerk," he said, "auditing a war." ... "Instruments hesitate for all kinds of
> reasons." The last sentence landed oddly — too specific, or perhaps not specific enough —
> and Arthur could not tell whether Hayes knew about the three beats or was simply talking
> about the general case...

**NPE:** P, P, P, P, P, P, P, P, P, P, P, P.

**Notes:** Hayes's `auditing a war` is a deliberate institutional insult and character
voice, not an accidental metaphor to normalize. His formal line fits his role. Arthur's
uncertainty follows directly from the dialogue and preserves mystery. No style failure is
shown by this sample.

### Sample 8 — Chapter 002, mission-board passage (lines 126–138)

> It was old, like the building, and covered in layers of paper going back years... The
> paper was clean but the ink had had time to dry a shade... He looked at the date, and the
> deadline, and the composition, and then at the blank space beneath, and he made himself a
> theory...

**NPE:** P, **D**, P, P, P, P, P, P, P, P, P, P.

**Notes:** The paperwork is correctly foregrounded. `the ink had had time to dry a shade` is
an oddly constructed, low-value detail and momentarily sounds like an inserted literary
observation. It need not be treated as a hard failure, but the Native Reading Test and
NPE-02 should flag it for review. The subsequent theory-making is continuous and
character-appropriate. **STYLE-ONLY.**

### Sample 9 — Chapter 003, requisition and casual conversation (lines 8–28)

> "Exceptional Aptitude Review. Report to Administration block, room two this morning. It
> says automatic." ... "That's what the cadets call it. Exceptional Aptitude Review." ...
> "The pile is still here when you come back."

**NPE:** P, P, P, P, P, **D**, P, P, P, P, P, P.

**Notes:** Timeline orientation is clear. Margaret's “They send everyone whose file does not
close properly” and “sealed file that nobody reads” are unusually explanatory for dialogue
with a new worker and read partly like institutional summary. Her reply is clipped and
believable. Dialogue Reconstruction/ NPE-06 should flag only the exposition-shaped portion;
the register is justified but could be made more like speech without changing facts.
**STYLE-ONLY.**

### Sample 10 — Chapter 003, formal station instruction and assessment report (lines 74–80)

> "You have until two o'clock to finish," the deputy commandant said. "Begin at station one.
> Proceed in order. You may not skip. You may ask for clarification once per station. Use it
> well." ... "Event occurred between 0310 and 0340. Witness A saw the secondary effect..."

**NPE:** P, P, P, P, P, P, P, P, P, P, P, P.

**Notes:** This is intentionally formal procedural speech and a written assessment response,
not casual dialogue. “Proceed” and “clarification” are justified by the institution. Arthur's
report register is appropriate to the task; the short commands are not TNE imitation.

### Sample 11 — Chapter 003, Station Seven (line 102)

> Under pressure, he hedged. He saw himself doing it and did not stop. The third answer was
> right, but he knew the test would record the second option, which he had written first.

**NPE:** P, P, P, P, P, P, P, P, P, P, P, P.

**Notes:** The short sentences mark self-observation and consequence; they are natural,
continuous, and not formula fragments. The final sentence clearly differentiates the correct
answer from the recorded one. No unnecessary advanced vocabulary or register break.

### Sample 12 — Chapter 004, file error explanation (lines 14–18)

> The report said nothing about a living entity. It said: sound-bleed, localized to one
> annex, duration three seconds, recurring at irregular intervals, no observed movement, no
> biological trace, no appetite. The correct protocol was R-4 — phenomenon-class,
> stationary. ... The wrong Rule would have sent an organism-response team...

**NPE:** P, P, P, P, P, P, P, P, P, P, P, P.

**Notes:** The list-like record language is intentional and grounded in the report/Arthur's
work. R-4/R-7 are necessary terminology. His explanation follows the evidence and carries
the institutional consequence clearly. It is not a dialogue/register error.

### Sample 13 — Chapter 004, compliance exchange (lines 54–84)

> "This was already responded to," he said. / "Under the wrong Rule," Arthur said. ...
> "Noted," he said. ... "Then they will send the organism team again."

**NPE:** P, P, P, P, P, P, P, P, P, P, P, P.

**Notes:** The exchange sounds intentionally formal and bureaucratic. “Responded to” and
“Noted” belong to the clerk's institutional register; repeated responses from Arthur reflect
his deliberate paper-based tactic. Do not simplify away the procedural power imbalance.

### Sample 14 — Chapter 004, directional warmth observation (lines 98–118)

> The warmth shifted. ... The warmth followed the direction, not the distance. It was not
> the room. It was the stone. ... as if the heat were something inside the stone that leaned
> toward a place it could not see.

**NPE:** **D**, P, P, P, P, P, P, P, **D**, P, P, P.

**Notes:** The short observations are natural and support Arthur's test, but the ending shifts
from measurable orientation to a personified stone that “leaned toward a place it could not
see.” The construction is a possible literary patch and weakens the preceding literal
measurement register. Patch Detection and thought/register continuity should require a
native-reading review of this paragraph; whether the metaphor remains depends on POV
motivation, not canon. **STYLE-ONLY.**

### Sample 15 — Chapter 004, return to the shelf and closing inference (lines 116–122)

> The correction had been made. The correction had been ignored. And the stone had pointed
> toward a place called East Beach. ... You copied it, you set it aside, and you let it point
> until it was time to follow.

**NPE:** **D**, **D**, P, P, **D**, P, **D**, P, P, P, P, P.

**Notes:** The repeated correction lines have a natural, deliberate cadence. The concluding
second-person generalization, however, shifts suddenly from close-third past observation to
`you` plus an aphoristic instruction. It risks reading as an inserted stylistic maxim rather
than Arthur's continuous thought. Patch Detection, register continuity, native-reading, and
NPE-01/NPE-02/NPE-05/NPE-09 should require paragraph-level review. It may be retained only
if the voice shift is clearly motivated. **STYLE-ONLY.**

## 4. NPE Matrix

| Rule | Detection strength | False-positive risk | Notes |
|---|---|---|---|
| NPE-01 — continuously authored | **ADEQUATE** | Medium | Native Reading Test and Patch Detection target this directly. Sample 4 and 15 indicate that borderline extended-metaphor/aphorism cases need a firmer fail threshold. |
| NPE-02 — inserted sentence | **ADEQUATE** | Medium | Patch cues include sudden literary lift and repeated summary. Low-value details can be mistaken for intentional close observation. |
| NPE-03 — translated phrase | **STRONG** | Low | Exact examples and translation-shadow/collocation lists catch all seven historical examples. |
| NPE-04 — advanced vocabulary | **STRONG** | Medium | Common English default and explicit alternatives; false positives possible for justified formal or technical terms. |
| NPE-05 — forced TNE fragment | **STRONG** | Low | Explicitly rejects “Folder in. Reading. Form out.” while allowing motivated fragments (e.g., Chapter 003 Station Seven). |
| NPE-06 — spoken dialogue | **ADEQUATE** | Medium | Dialogue reconstruction catches data-entry and exposition-shaped speech. Institutional speech requires register-sensitive review, not blanket casualization. |
| NPE-07 — natural narration | **ADEQUATE** | Medium | Literary patching and native reading checks apply, but judgment on a close-third metaphor can vary. |
| NPE-08 — natural collocations | **STRONG** | Low | Historical examples 1, 5, 6, and 7 match explicit diagnostics; chapter samples also identify “friendliness no longer included.” |
| NPE-09 — continuous thought movement | **ADEQUATE** | Medium | Notice→think→act test works, but the aphoristic close in Sample 15 shows a discourse-level jump can survive. |
| NPE-10 — first-read comprehension | **STRONG** | Low | One-Read test is concrete; it distinguishes language confusion from mystery. It does not alone establish naturalness. |
| NPE-11 — simple, not childish | **STRONG** | Medium | Existing reader and vocabulary rules support it; beware simplifying intentional character/institution register. |
| NPE-12 — Quiet Tide identity | **STRONG** | Low | Mystery, institutional pressure, restrained emotion, tactics, and asymmetry are explicitly retained and visible in the samples. |

## 5. Remaining Failure Modes

- **Discourse rhythm / paragraph coherence:** Some lines are individually understandable but shift into aphorism or compressed thesis voice without a clear transition (Chapter 004 Sample 15). Detected by NPE-01/NPE-09, but the fail threshold needs a concrete calibration cue.
- **Literary patching / metaphor:** Extended metaphor chains or personification may pass when they are technically POV-compatible, even if they feel inserted (Chapter 001 Sample 4; Chapter 004 Sample 14). Patch Detection names the risk but could more explicitly require the native-reading test to outweigh cleverness when the surrounding register is literal.
- **Dialogue realism:** Chapter 003's Margaret explanation contains factually appropriate but exposition-shaped speech. Existing rules detect this, though they should distinguish concise institutional facts from a character's natural spoken phrasing.
- **Sentence connection:** Sample 8 has an unnatural detail construction, and Sample 2's drawer simile creates a register bump. Current rules flag both as possible patching; they are not systematic MTL syntax errors.

The engine has rules for every tested category. Remaining risk is inconsistent application to borderline prose, not a wholly missing category. No new rule is strictly required; the next style-only revision should sharpen the operational gate for borderline NPE-01/NPE-02/NPE-07/NPE-09 cases using the two Chapter 004/001 calibration samples above.

## 6. Engine Coverage Assessment

| Category | Coverage | Evidence |
|---|---|---|
| A. MTL-like sentence structure | Covered | Translation-shadow and first-read tests; all seven historic examples have an applicable detector. |
| B. Unnatural collocations | Covered strongly | Explicit diagnostic patterns and common-English alternatives. |
| C. Unnatural dialogue | Covered | Dialogue Reconstruction and NPE-06; chapter samples expose a borderline institutional exposition line. |
| D. Unnecessarily advanced vocabulary | Covered strongly | Common English default and preferred alternatives with a specialized-term exception. |
| E. Forced TNE fragments | Covered strongly | Explicit fragment example and sentence-engine check. |
| F. Literary patching | Covered, application variable | Explicit examples; current samples still produce two borderline patch findings. |
| G. Paragraph-level insertion feel | Covered, application variable | Patch Detection and Native Reading Test; Sample 15 illustrates threshold gap. |
| H. Abrupt register changes | Covered | Register continuity test; current possible instance in Chapter 004 ending. |
| I. Unnatural metaphors | Covered | Literal-default and metaphor test; POV motivation can be subjective. |
| J. Thought discontinuity | Covered, application variable | Notice-think-act continuity; aphoristic shift remains a borderline case. |
| K. Unnatural sentence transitions | Covered | Patch Detection and thought movement; Sample 8 detail phrasing should be flagged. |
| L. Dialogue as written exposition | Covered | Explicit rejection and dialogue NPE; borderline dialogue remains in sample corpus. |

## 7. False-Positive Risks

- Do not flag the clerk's formal readout, the deputy commandant's instructions, or the
  compliance-window exchange merely for formal vocabulary or clipped syntax; their
  institutional context justifies the register.
- Do not flag “the machine had measured nothing it could use” or related institutional
  framing solely because it is figurative; assess the full metaphor chain and its continuity.
- Do not flatten Arthur's observation-driven voice into generic casual narration.
- Do not reject every fragment: Chapter 003's “Under pressure, he hedged. He saw himself
  doing it and did not stop” is short but natural and motivated.
- Do not treat mystery ambiguity, locked terminology, or understatement as language
  confusion.
- Do not remove Hayes's “auditing a war”; it functions as deliberate character speech.
- Do not infer that metaphor or aphoristic cadence is prohibited. It must be natural,
  earned, and continuous with POV and register.

## 8. Required Changes, If Any

Recommended **STYLE-ONLY** follow-up: add two short current-corpus calibrations for (1) an
aphoristic second-person ending that abruptly leaves close-third observation, and (2) a
metaphor/personification that breaks a literal measurement register. State that when the
Native Reading Test says the paragraph feels patched, a plausible POV metaphor is not
enough to pass: reconstruct the thought-unit unless the register shift is clearly motivated.

No changes are made to the Writing Engine during this calibration. Existing rules caught
the issues when applied; the evidence supports tightening the application criterion rather
than adding a new general category.

## 9. Author Decisions

**None required.** All remaining findings are STYLE-ONLY and can be resolved, if authorized
in a future engine task, through wording and paragraph reconstruction. No finding requires
canon, character behavior, chapter function, plot, mystery, POV architecture, Contract
mechanics, or institutional structure changes. No prose repair is authorized by this test.

## 10. Final Recommendation

The engine robustly detects the seven historical examples and forced TNE fragments. It
does not yet reliably reject every borderline paragraph-level literary patch in the
calibration corpus. Tighten the native-reading fail threshold with current-corpus examples
before using this revision as the sole control for new chapter generation. Do not change
the chapters as part of calibration.

**CALIBRATION PASS WITH STYLE GAPS — ENGINE NEEDS ONE MORE REVISION**
