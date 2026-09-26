# DIALOGUE NATURALNESS — ROOT-CAUSE AUDIT
## THE QUIET TIDE · why dialogue reads unnatural

> **Mode:** AUDIT ONLY. No dialogue rewritten. No engine modified. No canon/lock changed.
> **Scope:** spoken exchange only (narration is covered in `PROSE_NATURALNESS_ROOT_CAUSE_AUDIT.md`).
> **Sources:** `THE_QUIET_TIDE_WRITING_ENGINE.md` Module 09 (+ Module 01 dialogue rules), `TNE_STYLE_GAP_ANALYSIS_FINAL.md` (D50–D55), `NARRATIVE_STYLE_BIBLE.md` §16, `NATIVE_ENGLISH_CALIBRATION_REPORT.md` §3, `GENERATION/CHAPTERS/001_ERROR_UNDEFINED.md`, legacy `001_The_Three-Second_Shadow.md` (REFERENCE ONLY), `CH002/CH003` continuity prose excerpts (reference).

---

## 1. WHAT THE PROBLEM IS

Dialogue in the corpus splits into two failure bands:

1. **Data-entry dialogue** — institutional readouts spoken as field:value pairs ("Subject, age seventeen. Classification, Irregular."). Some of this is *justifiable* procedural readout; the risk is that the generator generalizes the cadence to ordinary conversation.
2. **Exposition disguised as dialogue** — a character explains a system or a relationship in a summary cadence rather than responding to what was just said (Margaret's ch3 explanation; Hayes's institutional lines are the deliberate exception).

The underlying cause: the engine imports **D50 (attribution starvation)**, **D54 (no adverbial tags)**, and the **"compressed exchange"** example, and frames them as *default dialogue hygiene*. A generator satisfying those defaults clips every exchange, then — because clipping removes connective tissue — fills the gaps with factual statements, producing report-like speech. The engine's own dialogue test ("would this person actually say this?") exists (Module 01 Dialogue Reconstruction; Module 09 checklist; NPE-06/NPE-15) but is a **QA pass after generation**, not a composition constraint.

---

## 2. SECTION G — THE AUTHOR-DIRECTED DIALOGUE TEST (recorded)

For every exchange:
1. Would a real person say this?
2. Is the speaker responding to what was actually said?
3. Is the sentence appropriate to the relationship?
4. Is the information being delivered naturally?
5. Could the same meaning be expressed more naturally?
6. Is the character speaking because they have a reason to speak, rather than because the author needs to explain something?

**Do NOT make all dialogue casual. Military/institutional characters can be formal — formal does not mean unnatural.**

---

## 3. ROOT CAUSES SPECIFIC TO DIALOGUE

| Cause | Engine source | Distortion |
|---|---|---|
| Compression treated as default | Module 09 §2–3 ("attribution economy"; "compressed exchange" example) | Every exchange clipped; speech loses natural connective words |
| Attribution starvation generalized | D50 ADOPT / P14 ADAPT | Speaker identity/relationship signals vanish, so lines read as text blocks |
| "No adverbial tags" over-applied | Module 09 §6 / D54 | Behavior is dropped with the tags, so lines carry no subtext and become statements |
| Documentation-first exposition | Module 14 (route worldbuilding through documents) | Characters deliver document content in speech |
| Register rigidity | Module 09 §7 + Module 18 institutional register | Institutional speakers sound uniformly clipped/formal even in ordinary moments |
| No composition-time spokenness rule | Module 01/09 tests are QA | Generator writes for the checklist, then is asked to "reconstruct" — the fix is late |

**Contrast note:** the engine *already* keeps deliberate institutional speech where it belongs (the district clerk readout; Hayes's "A records clerk, auditing a war"). The audit does not recommend casualizing those. The problem is that the **same clipped register leaks into ordinary conversation**, and factual summaries replace response.

---

## 4. SECTION H — DIAGNOSTIC CORPUS (8 DIALOGUE EXAMPLES)

Sources: `R` = reboot-generated `GENERATION/CHAPTERS/001_ERROR_UNDEFINED.md`; `L` = legacy `001_The_Three-Second_Shadow.md`; `C2/C3` = ch2/ch3 reference. **No example is rewritten.** "What rule should replace it" names the rule.

---

**D-1** `[R, L74]`
- **ORIGINAL:** "Subject, age seventeen. Classification, Irregular."
- **PROBLEM TYPE:** Database-entry cadence.
- **WHY UNNATURAL:** spoken as a template readout; no article, no human framing. (Justified as a procedural readout, but it is the model the generator copies.)
- **WHICH ENGINE RULE CAUSED IT:** Module 09 §3 compressed exchange + Module 14 documentation-first (document content delivered as speech).
- **WHAT RULE SHOULD REPLACE IT:** keep procedural readouts procedural but mark them as *readout register*; forbid the generator from reusing the cadence for ordinary talk.

**D-2** `[R, L78]`
- **ORIGINAL:** "Division, Intelligence. Curriculum, Intelligence Operations."
- **PROBLEM TYPE:** Database-entry cadence **+ the Division authority problem** (see `GENERATION_AUTHORITY_AUDIT.md`).
- **WHY UNNATURAL:** same clipped template; also carries the locked Intelligence placement the author direction disputes.
- **WHICH ENGINE RULE CAUSED IT:** Module 09 §3; Module 14; and the L-17 lock chain for the content.
- **WHAT RULE SHOULD REPLACE IT:** readout-register rule; content governed by the author's Division lock decision (separate track).

**D-3** `[L, L17]`
- **ORIGINAL:** "Family keepsake," he said. "Stone seal, uncarved. Appraised 1987 — the record's attached."
- **PROBLEM TYPE:** Data-entry dialogue (the engine's own flagged example).
- **WHY UNNATURAL:** speech shaped like a form field; no person talks about a keepsake this way, even transactionally.
- **WHICH ENGINE RULE CAUSED IT:** Module 09 §3 compression + Module 01's dialogue reconstruction being a QA pass.
- **WHAT RULE SHOULD REPLACE IT:** dialogue must pass "would a person say this aloud"; factual content is preserved but phrased as speech.

**D-4** `[R, L80–82]`
- **ORIGINAL:** "Records and Archives," Arthur said. / "That's what it says."
- **PROBLEM TYPE:** *None — positive calibration.*
- **WHY:** natural, responsive, relationship-appropriate, minimal.
- **WHICH ENGINE RULE CAUSED IT:** Module 09 §2–3 applied correctly.
- **WHAT RULE SHOULD REPLACE IT:** keep this as the model; it shows the compression rules can produce natural exchange.

**D-5** `[R, L124]`
- **ORIGINAL:** "You're Irregular." … "Filing cabinets."
- **PROBLEM TYPE:** *None — positive calibration.*
- **WHY:** functional hostility, responsive, in-world, carries hierarchy without exposition.
- **WHICH ENGINE RULE CAUSED IT:** Module 09 §1 (oblique relational talk) applied correctly.
- **WHAT RULE SHOULD REPLACE IT:** keep; the rule is working here.

**D-6** `[R, L130]`
- **ORIGINAL:** "Annex four," the supervisor said. "Records and Archives. You report there, not to the barracks. Quarters are in the east block."
- **PROBLEM TYPE:** Telegraphic institutional speech (borderline).
- **WHY UNNATURAL:** reads as a sequence of form fields; a supervisor issuing directions would use a connective phrase or two.
- **WHICH ENGINE RULE CAUSED IT:** Module 09 §2/§6 + Module 18 institutional register treated as uniformly clipped.
- **WHAT RULE SHOULD REPLACE IT:** institutional speech may be formal but must remain spoken; allow natural connectives.

**D-7** `[R, L90–92]`
- **ORIGINAL:** "Is the ERROR re-measured?" / "Annual re-examination. It's on the sheet."
- **PROBLEM TYPE:** Acceptable procedural exchange (flagged as borderline, not a failure).
- **WHY:** the question is plain and in-voice; the answer is functional. The clipping fits a counter transaction.
- **WHICH ENGINE RULE CAUSED IT:** Module 09 §3 applied correctly.
- **WHAT RULE SHOULD REPLACE IT:** keep; the rule's "formal ≠ unnatural" distinction applies.

**D-8** `[C3 reference]`
- **ORIGINAL:** Margaret's ch3 explanation of the review / sealed file ("They send everyone whose file does not close properly…").
- **PROBLEM TYPE:** Exposition disguised as dialogue.
- **WHY UNNATURAL:** an experienced clerk summarizes the system for the reader, not for the listener; the reply answers the reader's question rather than the speaker's.
- **WHICH ENGINE RULE CAUSED IT:** Module 14 documentation-first routing that lands in a character's mouth; Module 09 §3 compression removing the *social* reason to speak.
- **WHAT RULE SHOULD REPLACE IT:** dialogue test question 6 — the character must speak because they have a reason to speak, not because the author needs to explain; route system explanation to documents instead.

---

## 5. RECOMMENDED DIALOGUE RULES (NOT APPLIED HERE)

1. **Spokenness is a composition constraint**, not only a QA check: write the line as speech first, then apply attribution/compression hygiene.
2. **Separate registers explicitly:** *readout register* (forms, procedures — permitted), *institutional speech* (formal but connective), *ordinary speech* (Arthur, peers, family). Never let one bleed into another.
3. **Response rule:** every reply must respond to what was actually said (or conspicuously evade it — an evasion is still a response).
4. **Reason-to-speak rule:** no line exists only to inform the reader; exposition goes to documents (Module 14) unless a character has an in-world reason to say it.
5. **Formal ≠ unnatural:** do not casualize officers, clerks, examiners, or family; adjust connective naturalness, not vocabulary level.
6. **Keep the genuine successes** (D-4, D-5, and Hayes's "A records clerk, auditing a war") as calibration models; they prove the rules work when the spokenness constraint is applied first.

---

*End of DIALOGUE_NATURALNESS_ROOT_CAUSE_AUDIT.md — audit only. No dialogue rewritten; no engine modified.*
