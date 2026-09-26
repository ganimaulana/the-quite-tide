# CH001–CH002 DESCRIPTIVE PROSE REPAIR REPORT

> **Scope:** exactly the **3 SHOULD FIX** targets from `QA/CH001_004_DESCRIPTIVE_PROSE_AUDIT.md` (F1-03, F2-04, F2-05). CH003/CH004 untouched. The 19 OPTIONAL findings untouched. No Division/canon/lock/engine changes. No plot or factual changes.

---

## A. Exact passages repaired

| ID | File | Location | Audit target |
|---|---|---|---|
| F1-03 | `CHAPTERS/001_ERROR_UNDEFINED.md` | L68 | "full of ordinary August noise" (abstract/negative atmosphere) |
| F2-04 | `CHAPTERS/002_NO_TAKERS.md` | L58 | "the machine could not decide…" + "None of them… None of them… None of them…" (comparison + thesis/anaphora stack) |
| F2-05 | `CHAPTERS/002_NO_TAKERS.md` | L66 | "the thing the Academy did…" + "It did not… It did not…" (institutional personification/thesis) |

## B. Before / After

### F1-03 — CH001 L68
- **BEFORE:** "The district processing office was three days later, small and bright and full of ordinary August noise."
- **AFTER:** "The district processing office was three days later, small and bright, with the smell of paper and floor wax."

### F2-04 — CH002 L58
- **BEFORE:** "They were not what the word had made him expect. He had thought it would be a room full of people like him — unreadable, undefined, standing at the edge of a machine that could not decide what they were. It was not that. It was a room full of people the machine had decided about, all in different ways, none of them flattering. None of them secret. None of them waiting for a power to wake up and fix things."
- **AFTER:** "They were not what the word had made him expect. He had thought he would find people like himself, unreadable and undefined. Instead the Academy had decided what each of them was, and none of the decisions were kind. None of it was secret. Nobody at the table was waiting for a power to wake up and fix things."

### F2-05 — CH002 L66
- **BEFORE:** "That was his table, then: four of them at one table, in a room of hundreds. Arthur looked at each of them in turn and understood, with a clarity that surprised him, that he was looking at the thing the Academy did with people it could not use. It did not throw them out. It did not punish them. It gave them a word and a table near the bins and a job at the bottom of the pile and left them there, politely, for as long as they lasted."
- **AFTER:** "That was his table, then: four of them at one table, in a room of hundreds. Arthur looked at each of them in turn and understood, with a clarity that surprised him, that none of them had been thrown out or punished. They had been given a word, a table near the bins, and a job at the bottom of the pile, and left there, politely, for as long as they lasted."

## C. Why each revision improves naturalness

- **F1-03:** "full of ordinary August noise" was an abstract atmosphere bucket the reader could not hear. It is replaced by one concrete sensory anchor ("paper and floor wax") the reader can picture immediately. Vocabulary stays at the surrounding register; nothing ornate added.
- **F2-04:** the original stacked comparison into an interpretive thesis and closed on a three-beat anaphora ("None of them… ×3"). The revision states the same observation in plain sentences: expected (people undefined like him) vs actual (the Academy had decided each one; the decisions were not kind). The anaphora is gone; one short sentence ("None of it was secret.") replaces the three.
- **F2-05:** the original narrated the Academy as a person ("the thing the Academy did… It did not… It did not… It gave…"). The revision shifts to what Arthur actually sees ("none of them had been thrown out or punished… They had been given…"), removing the personified thesis and the anaphora while keeping his realization beat ("with a clarity that surprised him").

## D. Information content unchanged — confirmation

- **F1-03:** the office is still introduced as small, bright, and situated three days later; only the atmosphere phrasing changed. No new fact, object, or quantity added.
- **F2-04:** preserved — (i) the table was not what "Irregular" had made him expect; (ii) he expected people like himself, undefined/unreadable; (iii) instead the institution had decided what they were; (iv) those decisions were unflattering; (v) none of it was secret; (vi) none of them was waiting for a power to fix things.
- **F2-05:** preserved — (i) four of them at one table in a room of hundreds; (ii) his surprised clarity; (iii) they were neither expelled nor punished; (iv) they were given a classification/word, a table near the bins, and a bottom-of-the-pile job; (v) they were left there, politely, indefinitely.

No new information, symbolism, subplot, or worldbuilding was introduced in any of the three repairs.

## E. Confirmation that no other passages were modified

Only the three target passages changed (one in CH001, two in CH002). Immediately preceding and following paragraphs were read for continuity and left unmodified. No other paragraph in CH001 or CH002 was touched.

## F. Final status

**PASS.**

## G. Issues that could not be safely repaired without changing meaning

**None.** All three targets were repairable without altering information, POV, chronology, character facts, or surrounding prose. ("politely" was retained in F2-05 because removing it would have dropped a nuance of meaning.)

---

## FINAL VERIFICATION

- Exactly **3 SHOULD FIX targets** addressed: **YES** (F1-03, F2-04, F2-05).
- **19 OPTIONAL findings** remain untouched: **YES**.
- **CH003 / CH004** unchanged: **YES**.
- **Writing Engine** files unchanged: **YES**.
- **Division / canon** files unchanged: **YES**.
- **Plot or factual changes:** **NO**.
- POV / chronology / character facts / Contract / EAR: **unchanged**.
- No dialogue changes (the repaired passages are narration): **confirmed**.

**Files modified:**
1. `03_WRITING_ENGINE/GENERATION/CHAPTERS/001_ERROR_UNDEFINED.md` (one sentence — L68)
2. `03_WRITING_ENGINE/GENERATION/CHAPTERS/002_NO_TAKERS.md` (two paragraphs — L58, L66)
3. `03_WRITING_ENGINE/GENERATION/QA/CH001_002_DESCRIPTIVE_PROSE_REPAIR_REPORT.md` (this report)

*End of report.*
