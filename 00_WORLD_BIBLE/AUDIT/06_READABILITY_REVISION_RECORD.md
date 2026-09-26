# AUDIT VOL. 06 — Phase 18 Readability Revision Record (report + worklogs + diffs) — THE QUIET TIDE

> **Phase 20 repository consolidation (2026-09-21, v3.0).** This numbered volume merges 26 source files **verbatim** into one file. No content was changed, rewritten, or summarized — only this header, the source register below, and per-section attribution separators were added. To find a document's new location, see `AUDIT/00_CONSOLIDATION_MAP.md`.

## Source register

| # | Original file | Words | sha256 (pre-merge) |
|---|---|---|---|
| 1 | `AUDIT/READABILITY_REVISION_REPORT_001_020.md` | 1,689 | `a72af1b7376d1d43…` |
| 2 | `AUDIT/READABILITY_WORKLOG_BLOCK_A.md` | 2,795 | `9ae29a0ccc939740…` |
| 3 | `AUDIT/READABILITY_WORKLOG_BLOCK_B.md` | 3,393 | `66c535a6f0b70bbb…` |
| 4 | `AUDIT/READABILITY_WORKLOG_BLOCK_C.md` | 2,725 | `c944fd9f8c09be73…` |
| 5 | `AUDIT/READABILITY_WORKLOG_BLOCK_D.md` | 2,830 | `20e6a6179d7dbf98…` |
| 6 | `AUDIT/_BASEmessaging app_READABILITY.txt` | 87 | `d92beb2eb97c6f09…` |
| 7 | `AUDIT/READABILITY_DIFFS/001_The_Three-Second_Shadow.diff` | 193 | `f0e2d6301714a981…` |
| 8 | `AUDIT/READABILITY_DIFFS/002_Willowmere.diff` | 296 | `e48c8daf1c938169…` |
| 9 | `AUDIT/READABILITY_DIFFS/003_Sunday_Dinner.diff` | 0 | `e3b0c44298fc1c14…` |
| 10 | `AUDIT/READABILITY_DIFFS/004_The_Measurement.diff` | 204 | `8f3be50adbe8ce0e…` |
| 11 | `AUDIT/READABILITY_DIFFS/005_Saitos_Test.diff` | 92 | `fac5a2cf9ae51c42…` |
| 12 | `AUDIT/READABILITY_DIFFS/006_Dark_Water.diff` | 803 | `553bd37a3c09a28f…` |
| 13 | `AUDIT/READABILITY_DIFFS/007_No_Category.diff` | 527 | `0d9cda3f0d8d1525…` |
| 14 | `AUDIT/READABILITY_DIFFS/008_Melon_Pan.diff` | 0 | `e3b0c44298fc1c14…` |
| 15 | `AUDIT/READABILITY_DIFFS/009_Impossible_Constancy.diff` | 404 | `e5a6e16a1df1805b…` |
| 16 | `AUDIT/READABILITY_DIFFS/010_The_Cordon.diff` | 287 | `8eadac78be01565d…` |
| 17 | `AUDIT/READABILITY_DIFFS/011_Aftershock.diff` | 1,113 | `82fffd41a2ffe92a…` |
| 18 | `AUDIT/READABILITY_DIFFS/012_The_Private_Ledger.diff` | 0 | `e3b0c44298fc1c14…` |
| 19 | `AUDIT/READABILITY_DIFFS/013_The_Night_Keeps.diff` | 0 | `e3b0c44298fc1c14…` |
| 20 | `AUDIT/READABILITY_DIFFS/014_Three_Point_One.diff` | 191 | `2242cfa06ec83e8c…` |
| 21 | `AUDIT/READABILITY_DIFFS/015_Rent_Day_Arithmetic.diff` | 0 | `e3b0c44298fc1c14…` |
| 22 | `AUDIT/READABILITY_DIFFS/016_Sunday_Dinner_Again.diff` | 863 | `c292bdcce1a38426…` |
| 23 | `AUDIT/READABILITY_DIFFS/017_The_Badge_Log.diff` | 673 | `7be622182a5973af…` |
| 24 | `AUDIT/READABILITY_DIFFS/018_The_Unwritten_Rule.diff` | 243 | `743e3289a65dc931…` |
| 25 | `AUDIT/READABILITY_DIFFS/019_The_Photograph.diff` | 192 | `c111d01c0c85a7fe…` |
| 26 | `AUDIT/READABILITY_DIFFS/020_Method.diff` | 0 | `e3b0c44298fc1c14…` |

---


---

## SECTION: `AUDIT/READABILITY_REVISION_REPORT_001_020.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/READABILITY_REVISION_REPORT_001_020.md` · sha256 `a72af1b7376d1d43d6e3a953e8fd11a42c70869ccd4cf08c23a0e310ec3d5ff0` · 1,689 words. No content changed.

# READABILITY REVISION REPORT — CHAPTERS 001–020

**Phase:** 18 — Non-Native Readability Revision Pass
**Date:** 2026-09-21 (WIB)
**Governing standard:** NON-NATIVE READABILITY & ACCESSIBILITY STANDARD, Retention SOP Part II (§§37–50); integrated 2026-09-21
**Scope:** CHAPTERS/001–020 prose only. No canon, blueprint, architecture, or audit-history files modified. No Chapters 021+.
**Principle applied:** SIMPLIFY THE DELIVERY, NOT THE IDEA ("Easy words + deep ideas")
**Verdict:** PASS — all 20 chapters pass the §50 Readability Audit and the §35 gate pairing. Zero FAILs, zero structural changes.

---

## 1. OVERALL

| Metric | Value |
|---|---|
| Chapters processed | 20 |
| Chapters PASS | 20 |
| Chapters WATCH | 0 |
| Chapters FAIL | 0 |
| Total sentences reviewed | 3,154 |
| Total sentences changed | 29 (0.9%) |
| Total edits (classified) | 31 |
| Total words before | 44,321 |
| Total words after | 44,309 |
| Net word change | −12 (−0.03%) |
| Chapters edited | 15 |
| Chapters zero-edit (honest zeros) | 5 (003, 008, 012, 013, 015) |
| Diff lines across 20 unified diffs | 273 (headers + context + changes) |

The near-zero net word change is deliberate, not inaction: this was a polish pass over prose that had already undergone two full revision phases. Workers applied the §8 sentence test to every candidate change and kept only edits that passed the final gate ("easier for a non-native reader WITHOUT making the story easier to understand?"). Where prose already met the standard — ordinary actions in plain English, no rare-synonym hits, no "not X, but Y" inflation — workers recorded honest zeros rather than inventing changes. Diffs: `AUDIT/READABILITY_DIFFS/`.

### Edits by taxonomy (§19)

| Taxonomy | Count |
|---|---|
| CLEARER_WORDING | 20 |
| SENTENCE_SIMPLIFICATION | 7 |
| AMBIGUITY_REDUCTION | 2 |
| IDIOM_CLARIFICATION | 1 |
| CONTEXTUAL_ANCHOR | 1 |

### §50 item totals (15 items × 20 chapters = 300)

| Result | Count |
|---|---|
| PASS | 297 |
| WATCH | 3 (all deliberate non-changes: ch.006 perceptual idiom, ch.008 closing idiom, ch.009 doctrine vocabulary — see §6) |
| FAIL | 0 |

---

## 2. VOCABULARY

- **Unnecessary difficult vocabulary simplified:** ordinary-action friction words (e.g., "performing normalcy" → "acting normal"; "insofar as" → "as far as"; "absolution" → "forgiveness"; "inquest" → "questioning"; "noise of assent" → "murmur of agreement"; "the doing it" → "doing it"). Rare-synonym sweeps found near-zero hits: no "proceeded/utilized/subsequently/commenced" patterns existed in the prose.
- **Specialized vocabulary preserved:** manifest, discrepancy, requisition, reshelve, finding aid, marginalia, unclassified, cordon, afterimage, falsification, temporal component, delta, baseline, claimant. Per §38 Level 3 and §48 tension resolution: rotation ≠ removal. One stacking case (ch.007 "pulling manifests, reading finding aids, checking the labels' own marginalia") was unstacked by sentence split — terms kept, density reduced.
- **Cultural vocabulary preserved:** convenience store, rice ball, protective charm, messaging app, nikujaga, natto, vocational-gakko, Indonesian register elements (Nadia). No Westernization; contextual anchoring retained.
- **Contextual anchoring improvements:** "did not check himself in the shoebox door" → "did not check his reflection in the shoebox door" (002); "before the absence of it registered" → "before he noticed it was missing" (017); ambiguous-pronoun fix (001, see below).

---

## 3. ACCESSIBILITY (1–10, honest scoring)

| Dimension | Score | Basis |
|---|---|---|
| Vocabulary accessibility | 8 | Ordinary actions in simple English; specialized terms preserved by design but context-anchored |
| Sentence clarity | 8 | Unnecessarily convoluted sentences simplified; deliberately idea-complex sentences retained |
| Dialogue clarity | 9 | Dialogue was already natural; only delivery friction touched |
| Idiom accessibility | 8 | Confusing idioms clarified; inferable voice idioms kept with contextual support |
| Metaphor accessibility | 8 | Stacked/difficult metaphors reduced; meaningful ones retained |
| Cultural accessibility | 9 | Cultural terms preserved with anchoring; never Westernized |
| **Overall non-native accessibility** | **8** | Reader can understand every sentence's literal meaning without a dictionary; the story's underlying meaning remains as demanding as ever |

Scores are not inflated: an 8 reflects the intentional design target — "understand every sentence, but not necessarily what is happening underneath those sentences." Deliberately retained voice, metaphor, and doctrine vocabulary keep this from being a 9.

---

## 4. STRUCTURAL SAFETY

Confirmed via per-chapter diff against pristine originals (FINAL_WORLD_BIBLE pre-pass):

- Canon unchanged: YES
- Story architecture unchanged: YES
- Mystery architecture unchanged: YES
- Chapter order unchanged: YES
- Plot unchanged: YES
- Character decisions unchanged: YES
- Timeline unchanged: YES
- Blueprint unchanged: YES (no blueprint file touched)
- Three truth layers preserved in every edited passage: YES
- Mystery 001 unresolved / Mystery 002 slow-seed / Mystery 013 doctrine-only: YES
- WATCH items untouched: 9/18 overlap UNDETERMINED; Saito's two-second glance UNRESOLVED
- Arthur: Stage 1, zero Fathom, ordinary, accessible — not simplified: YES
- Retention functions (curiosity / movement / residue) preserved: YES
- Word-count stability (largest single-chapter delta: 014, +3 words; 005, −2): YES

---

## 5. CHAPTER TABLE

| Chapter | Before Words | After Words | Sentences Changed | Readability (PASS/WATCH/FAIL) | Status |
|---|---|---|---|---|---|
| 001 The Three-Second Shadow | 2,516 | 2,512 | 1 | 15/0/0 | PASS |
| 002 Willowmere | 2,391 | 2,392 | 1 | 15/0/0 | PASS |
| 003 Sunday Dinner | 2,273 | 2,273 | 0 | 15/0/0 | PASS |
| 004 The Measurement | 1,988 | 1,983 | 1 | 15/0/0 | PASS |
| 005 Saito's Test | 2,257 | 2,255 | 1 | 15/0/0 | PASS |
| 006 Dark Water | 2,037 | 2,035 | 3 | 14/1/0 | PASS |
| 007 No Category | 2,497 | 2,501 | 2 | 15/0/0 | PASS |
| 008 Melon Pan | 2,249 | 2,249 | 0 | 14/1/0 | PASS |
| 009 Impossible Constancy | 2,033 | 2,032 | 2 | 14/1/0 | PASS |
| 010 The Cordon | 2,042 | 2,043 | 1 | 15/0/0 | PASS |
| 011 Aftershock | 2,480 | 2,476 | 6 | 15/0/0 | PASS |
| 012 The Private Ledger | 2,491 | 2,491 | 0 | 15/0/0 | PASS |
| 013 The Night Keeps | 1,984 | 1,984 | 0 | 15/0/0 | PASS |
| 014 Three Point One | 2,711 | 2,714 | 1 | 15/0/0 | PASS |
| 015 Rent Day Arithmetic | 2,496 | 2,496 | 0 | 15/0/0 | PASS |
| 016 Sunday Dinner, Again | 1,938 | 1,937 | 5 | 15/0/0 | PASS |
| 017 The Badge Log | 1,840 | 1,838 | 3 | 15/0/0 | PASS |
| 018 The Unwritten Rule | 2,006 | 2,006 | 1 | 15/0/0 | PASS |
| 019 The Photograph | 2,024 | 2,024 | 1 | 15/0/0 | PASS |
| 020 Method | 2,068 | 2,068 | 0 | 15/0/0 | PASS |

Note on 020 "Method": zero edits were made — its thesis lines, four open questions, and ARC I closing framing were deliberately left byte-identical per the task boundary.

---

## 6. WATCH ITEMS — deliberate non-changes

Every item below was considered and deliberately preserved. Changing it would risk atmosphere, mystery, character voice, canon, cultural authenticity, or specialized terminology. Full per-chapter ledgers with reasons are in `AUDIT/READABILITY_WORKLOG_BLOCK_A.md` / `_B` / `_C` / `_D`.

### Atmosphere / mystery-beat phrasing (kept because difficulty is intentional)
- 016: "Nothing arriving late, nothing kept back." — mystery-beat phrasing at the 001 boundary
- 019: "The asymmetry itself would be the violation." — fully context-anchored; ch.019's negative-evidence beats kept byte-identical
- C-block metaphors: "The night air had teeth", "rinsed the ghost of heat" — selective literary sentences with narrative payoff
- 020: unresolved ledger glance; the ending and "understanding is the project" framing untouched

### Character voice (kept as voice, not friction)
- 001: "personal accounting was coming due" (Arthur's thematic bookkeeping vocabulary), "pocketed it" (metaphor), "stragglers" ×2 (context-clear)
- 002: "professionally, just weather,"; laundry/receipts parallel cadence
- 004: "by the application of labor"; the 60-word corridor long-take (single-occurrence rhythm)
- 005: Saito's "not suspicious" beat verbatim; no doctrine talk introduced
- 006: "didn't read as water" / "The water read wrong" — Arthur's perceptual voice (idiom accessibility: WATCH, context carries meaning)
- 008: "tired to the bone" — deliberate closing beat; long emotional sentences kept (idea-complex, not wording-complex) (WATCH)
- 009: "falsification" — method-doctrine vocabulary, context-anchored (WATCH); 62-word polysyndeton climax kept as single-occurrence rhythm
- C-block: flat comma-punctuated dialogue questions kept as consistent voice choice; "The shift ran its channels", "the wallpaper of the wallpaper", "Opinions rationed tight" kept as deliberate echoes
- 017: family banter and Saito dialogue voice untouched; emotional subtext never explained

### Canon / seed subtlety (kept per canon constraints)
- 003: zero edits — the salt/protective charm must stay unexplained; Yuko's silence kept at seed subtlety
- 012: thesis lines and measurement entries preserved verbatim; the old man's line kept ambient, never a clue; money math exact; Yuko's silence content-free
- 014: measurement readings (3.13, 3.11, 3.09/3.12/3.10, 3.1) untouched
- 010: Saito's two-second glance kept verbatim and UNRESOLVED; "My memory doesn't rot like theirs" verbatim; cordon never attributed; inference stays "working, not firm"; ch.007 ticker stays one line; Hasegawa bottleneck honored; 007/008 day-labels not "fixed" (prior clearance respected)

### STOP-level risks encountered
None. No readability fix required a plot change; no sentence contradicted canon; no metaphor containing foreshadowing had to be altered; no chapter content diverged from its blueprint; all source documents were locatable; no scene rewrites were required.

---

## 7. FILE SAFETY RECORD

- Baseline: `AUDIT/_BASEmessaging app_READABILITY.txt` — sha256 checksums + word counts for all 20 chapters, recorded before any edit.
- After: new checksums and word counts recorded per chapter in the block worklogs (`AUDIT/READABILITY_WORKLOG_BLOCK_A.md`–`_D.md`).
- Diffs: `AUDIT/READABILITY_DIFFS/` — 20 unified diffs against the pre-pass originals; every hunk is readability-only.
- Only the 20 chapter prose files were modified; no canon, blueprint, architecture, or index files were touched during revision.
- Release: working copy synced to `00_WORLD_BIBLE/` (full replace); `00_INDEX.md` → v2.8; `38_MANIFEST.md` → updated file count; `AUDIT/CHANGELOG.md` → Phase 18 entry.


---

## SECTION: `AUDIT/READABILITY_WORKLOG_BLOCK_A.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/READABILITY_WORKLOG_BLOCK_A.md` · sha256 `9ae29a0ccc939740bd44b3bd3520df7f633687ba71cea0467d2eed7e9d0bf5cb` · 2,795 words. No content changed.

# READABILITY WORKLOG — BLOCK A (Chapters 001–005)

**Worker:** Readability Revision Worker (Block A)
**Date:** 2026-09-21
**Scope:** `CHAPTERS/001_The_Three-Second_Shadow.md`, `CHAPTERS/002_Willowmere.md`, `CHAPTERS/003_Sunday_Dinner.md`, `CHAPTERS/004_The_Measurement.md`, `CHAPTERS/005_Saitos_Test.md` in `~/workspace/world_bible/work_readability/` ONLY. No other files touched.
**Standard:** `DATABASE/FAST_PACE_DEEP_MYSTERY_RETENTION_SOP.md` — Part II §§37–50 (lines 1040–1471) + Part I §§13, 14, 34 read in full before work began.
**Guiding rule:** SIMPLIFY THE DELIVERY, NOT THE IDEA ("Easy words + deep ideas").

## BASEmessaging app VERIFICATION

All 5 working-copy checksums matched `AUDIT/_BASEmessaging app_READABILITY.txt` exactly before editing (da9bbe73…, 0df97c62…, 9ef9a0af…, 8590ebb6…, cec53960…). Word counts also matched baseline (2516 / 2391 / 2273 / 1988 / 2257).

## DIFF VERIFICATION (readability-only)

Each chapter was diffed against the pristine copy at `~/workspace/world_bible/00_WORLD_BIBLE/CHAPTERS/`. The complete diffs are exactly the 4 sentence-level changes listed below — no plot, event, decision, motivation, foreshadowing, timeline, or ending changes; no additions or removals of content; no name or vocabulary changes outside the 4 edits.

---

## CHAPTER 001 — "The Three-Second Shadow"

- **Original checksum:** `da9bbe73149796ecf5cf132862e6ce1e8225c8e07498762085ccad082fc7fc3d`
- **New checksum:** `ca68422dc8e8c61ece126df4bfa4c3d532f5bfa826805b3fe7dbec2b0b4d9533`
- **Word count:** 2516 → 2512 (−4)
- **Sentences reviewed / changed:** 191 / 1

### Changes (taxonomy-classified)

1. **AMBIGUITY_REDUCTION + SENTENCE_SIMPLIFICATION** (32 words → 26)
   - BEFORE: "Their workstations faced each other across a gap of about a meter, close enough that Arthur could see the reflection of Saito's monitor in his glasses and Saito could see his."
   - AFTER: "Their workstations faced each other across a gap of about a meter — close enough that each could see the other's monitor reflected in the other's glasses."
   - Reason: pronoun "his" was ambiguous (whose glasses? whose monitor reflection?). §42 accessibility test item on pronoun clarity. Meaning, tone, and cadence preserved; atmosphere and character voice unchanged.

### §50 Readability Audit

| # | Item | Result |
|---|------|--------|
| 1 | Important sentences immediately understandable | PASS |
| 2 | Everyday actions use simple English | PASS |
| 3 | Specialized vocabulary necessary | PASS (discrepancy, requisition, reshelve, manifest, cross-reference — all workplace-precision) |
| 4 | Specialized vocabulary contextually understandable | PASS |
| 5 | Difficult words not unnecessarily stacked | PASS |
| 6 | Sentence complexity serves meaning | PASS (long sentences are sequential/rhythmic: shift rotation list, corridor approach) |
| 7 | Figurative language selective | PASS |
| 8 | Literary language does not dominate | PASS |
| 9 | Mystery remains complex | PASS (Mystery-001: lag observed, dismissed, unresolved) |
| 10 | Atmosphere remains strong | PASS |
| 11 | Character voice intact | PASS |
| 12 | Does not feel childish after simplification | PASS |
| 13 | No dictionary needed for basic comprehension | PASS |
| 14 | Beauty through imagery/behavior/implication | PASS |
| 15 | Language simpler than the story | PASS |

### WATCH items (deliberate non-changes)
- "in the way of anything done at the end of a week when everyone's personal accounting was coming due" — kept: passes §8 (2–3); "accounting" is thematic vocabulary (§14 rotation, not removal), mild and voice-serving.
- "stragglers" (2×) — kept: inferable from context ("the day shift's last stragglers"); mild color, not genuine friction.
- "predated the digitization drive" — kept: context-clear.
- "Arthur cross-referenced, scanned, filed." + imperative chain ("Open the folder. Read the summary…") — kept: character rhythm, single occurrence, readable; §13 permits non-recurring templates.
- "Arthur pocketed it without meaning to" (metaphor) — kept: deliberate; disambiguated by the following "Not a claim. Just the morning"; serves the filing-instinct theme.
- "was gone before he'd finished deciding to be" — kept: intentional ellipsis, atmospheric fade into sleep.
- No rare synonyms for ordinary actions found anywhere in the chapter (grep: proceeded/utilized/subsequently/commenced/ascertained/necessitated — zero hits). No "not X, but Y" inflation.

**Final gate:** Chapter is slightly easier for a non-native reader WITHOUT the story becoming easier to understand → **YES, keep.**

---

## CHAPTER 002 — "Willowmere"

- **Original checksum:** `0df97c62a6adf13c6b1907facbb783e5234bea90f009fc2ed8afa2d62a1b59e6`
- **New checksum:** `8cd831f36f00023e6ade0ee053e4acace926e8f807decd4a2f71033e6c0e52a5`
- **Word count:** 2391 → 2392 (+1)
- **Sentences reviewed / changed:** 160 / 1

### Changes (taxonomy-classified)

1. **AMBIGUITY_REDUCTION** (same length, +1 word)
   - BEFORE: "He straightened them by feel and did not check himself in the shoebox door before leaving; checking had never once improved a day."
   - AFTER: "He straightened them by feel and did not check his reflection in the shoebox door before leaving; checking had never once improved a day."
   - Reason: "check himself in the shoebox door" required outside knowledge (British genkan mirrored shoebox doors) to parse; a non-native reader could stall on the literal image. "check his reflection" makes the intended action explicit without adding new detail. No canon detail invented.

### §50 Readability Audit

| # | Item | Result |
|---|------|--------|
| 1 | Important sentences immediately understandable | PASS |
| 2 | Everyday actions use simple English | PASS |
| 3 | Specialized vocabulary necessary | PASS (inventory/ledger language is Arthur's identity; game terms anchored by context) |
| 4 | Specialized vocabulary contextually understandable | PASS |
| 5 | Difficult words not unnecessarily stacked | PASS |
| 6 | Sentence complexity serves meaning | PASS (parallel lists serve the Saturday-errand rhythm) |
| 7 | Figurative language selective | PASS ("sun as seasoning", "rent left his account like a tide" — one image each, simple words) |
| 8 | Literary language does not dominate | PASS |
| 9 | Mystery remains complex | PASS (n/a: genuinely ordinary chapter; the laughed-off dim room stays texture-only per blueprint) |
| 10 | Atmosphere remains strong | PASS |
| 11 | Character voice intact | PASS |
| 12 | Does not feel childish after simplification | PASS |
| 13 | No dictionary needed for basic comprehension | PASS |
| 14 | Beauty through imagery/behavior/implication | PASS |
| 15 | Language simpler than the story | PASS |

### WATCH items (deliberate non-changes)
- "while his body caught up with the concept of being upright" — kept: dry humor, literally parseable.
- "now it was, professionally, just weather" — kept: character voice (night-worker's wry register).
- "not the absence of errands but the thing the errands were for" — kept: one deliberate "not X, but Y" (the chapter's only one); thematic thesis of the chapter, not inflation.
- "the apartment's humidity had opinions and Arthur had learned to buy it off" — kept: readable anthropomorphism, understated humor preserved.
- Repeated "accumulated" cadence (laundry/receipts/days) — kept: deliberate, readable parallelism; serves the fatigue-ledger theme.
- No rare synonyms for ordinary actions (grep: zero hits). "not X, but Y" appears 2× total in the chapter, spaced, both load-bearing — no inflation.

**Final gate:** Slightly easier to read, story unchanged (and the deliberate unknowns untouched) → **YES, keep.**

---

## CHAPTER 003 — "Sunday Dinner"

- **Original checksum:** `9ef9a0af84d10a5e9207215aaeeccd2a88209c3015ee5ff354cb2c425448aefc`
- **New checksum:** `9ef9a0af84d10a5e9207215aaeeccd2a88209c3015ee5ff354cb2c425448aefc` (unchanged)
- **Word count:** 2273 → 2273 (±0)
- **Sentences reviewed / changed:** 156 / 0

### Changes
None. Full read against §42/§46 and the §8 sentence test found no genuine friction: vocabulary is plain and voice-driven; the chapter's difficulty, where present, is deliberate understatement (Yuko's stillness, the salt dish, the protective charm — canon requires non-explanation; mystery texture must stay subtext). Simplifying further would flatten voice or violate Mystery-010's seed-level subtlety. Making zero edits here is the honest outcome.

### §50 Readability Audit

| # | Item | Result |
|---|------|--------|
| 1 | Important sentences immediately understandable | PASS |
| 2 | Everyday actions use simple English | PASS |
| 3 | Specialized vocabulary necessary | PASS (minimal specialized vocab; all contextual) |
| 4 | Specialized vocabulary contextually understandable | PASS |
| 5 | Difficult words not unnecessarily stacked | PASS |
| 6 | Sentence complexity serves meaning | PASS |
| 7 | Figurative language selective | PASS ("built its peace around it the way you built a house around a load-bearing wall" — one central image) |
| 8 | Literary language does not dominate | PASS |
| 9 | Mystery remains complex | PASS (Yuko's silence, salt, protective charm stay unexplained per canon) |
| 10 | Atmosphere remains strong | PASS |
| 11 | Character voice intact | PASS |
| 12 | Does not feel childish after simplification | PASS (no simplification performed) |
| 13 | No dictionary needed for basic comprehension | PASS |
| 14 | Beauty through imagery/behavior/implication | PASS |
| 15 | Language simpler than the story | PASS |

### WATCH items (deliberate non-changes)
- "in the tone of a man delivering considered counsel" — kept: comic formality is the joke; "counsel" is parseable in context.
- "the way he'd been taught without ever being taught" (salt gesture) — kept: deliberate paradox, readable; the gesture must not be explained (canon: no Court content, no 2018-cleansing ritual exposition).
- "Nobody had ever explained them, and the explaining had never been the point" (protective charm) — kept verbatim: canon requires the folk objects stay unexplained.
- "shooshed" — kept: readable colloquialism, voice.
- "not the mackerel, not the exact wording of Dad-ism forty-eight, but the quality of the noise" — the chapter's only "not X, but Y"; kept (emotional thesis).
- No rare synonyms for ordinary actions (grep: zero hits).

**Final gate:** Nothing to simplify without cost → **keep as-is (no edits).**

---

## CHAPTER 004 — "The Measurement"

- **Original checksum:** `8590ebb69bbc4036fcb37186a8d1e5e9bfb8fb7163434448711944c81312ecb4`
- **New checksum:** `45193866f6a12bb0caa02fbbd7874f5fdc0bd87ab53f2c3cdf60165214e44dff`
- **Word count:** 1988 → 1983 (−5)
- **Sentences reviewed / changed:** 147 / 1

### Changes (taxonomy-classified)

1. **CLEARER_WORDING + SENTENCE_SIMPLIFICATION** (15 words → 10)
   - BEFORE: "Fatigue produced afterimages. Fine. But afterimages were symmetrical things — they belonged to the eye, not the wall."
   - AFTER: "Fatigue produced afterimages. Fine. But afterimages belonged to the eye, not the wall."
   - Reason: "symmetrical things" was an imprecise, mildly technical word doing no work — the plain half of the sentence carried the full meaning (the fatigue-theory argument: lag should follow him everywhere, but it only happens in the corridor). Removed the ornamental clause, not the idea. The mystery argument is preserved intact; 3.0s stays flat per canon (no ratchet measured here).

### §50 Readability Audit

| # | Item | Result |
|---|------|--------|
| 1 | Important sentences immediately understandable | PASS |
| 2 | Everyday actions use simple English | PASS |
| 3 | Specialized vocabulary necessary | PASS (frame count, slow-mo method, cross-check — measurement vocabulary is the chapter's subject) |
| 4 | Specialized vocabulary contextually understandable | PASS |
| 5 | Difficult words not unnecessarily stacked | PASS |
| 6 | Sentence complexity serves meaning | PASS (the 60-word corridor approach sentence is a deliberate sequential long take; reviewed and kept) |
| 7 | Figurative language selective | PASS |
| 8 | Literary language does not dominate | PASS |
| 9 | Mystery remains complex | PASS (3.0s repeatable; "What keeps it at exactly three?" unanswered; fatigue theory survives as honest wrong theory) |
| 10 | Atmosphere remains strong | PASS |
| 11 | Character voice intact | PASS |
| 12 | Does not feel childish after simplification | PASS |
| 13 | No dictionary needed for basic comprehension | PASS |
| 14 | Beauty through imagery/behavior/implication | PASS |
| 15 | Language simpler than the story | PASS |

### WATCH items (deliberate non-changes)
- "He kept the corridor out of his head by the application of labor" — kept: dry pompos humor is intentional (§8 test: understandable, characterful).
- "Location-correlated fatigue was not a thing, but habit-correlated attention was" — kept: Arthur's scientific-voice reasoning; readable; the honest wrong theory must stay plausible per blueprint.
- "His eyes were playing the game eyes played" — kept: dry voice, parseable in context.
- "At 23:17 he walked it…" (60-word approach sentence) — kept: sequential rhythm of walking; splitting would break the long take.
- The "3.0 seconds. Both runs." beat and the final question — untouched: canon-flat measurement, no false precision added.
- No rare synonyms for ordinary actions (grep: zero hits). "not a thing, but…" single occurrence.

**Final gate:** Easier to read, mystery complexity untouched → **YES, keep.**

---

## CHAPTER 005 — "Saito's Test"

- **Original checksum:** `cec539607885173b0996d25a8d3471821793aca72439c8a4584aac9363d76d99`
- **New checksum:** `0e5225ccd4a4628f89cf381bc15d867aeb6138d512e6f6e31178a42dcb8ebec6`
- **Word count:** 2257 → 2255 (−2)
- **Sentences reviewed / changed:** 139 / 1

### Changes (taxonomy-classified)

1. **CLEARER_WORDING** (same length, −2 words)
   - BEFORE: "Saito's hand stayed out for one more second, the grin stayed on for one more second, and then both of them retired, and Saito said, "Facilities asked *you*.""
   - AFTER: "Saito's hand stayed out for one more second, the grin stayed on for one more second, and then both dropped, and Saito said, "Facilities asked *you*.""
   - Reason: "both of them retired" used "retired" in its literary withdrew-sense; a non-native reader's default parse (job retirement) produces momentary confusion in an emotionally load-bearing beat (the lie landing). "both dropped" preserves the image (hand lowers, grin fades) with ordinary words. Saito stays un-suspicious per canon; the lie's wording and cost are untouched.

### §50 Readability Audit

| # | Item | Result |
|---|------|--------|
| 1 | Important sentences immediately understandable | PASS |
| 2 | Everyday actions use simple English | PASS |
| 3 | Specialized vocabulary necessary | PASS (manifest, verification, intake — all workplace-precision) |
| 4 | Specialized vocabulary contextually understandable | PASS |
| 5 | Difficult words not unnecessarily stacked | PASS |
| 6 | Sentence complexity serves meaning | PASS |
| 7 | Figurative language selective | PASS ("interested the way a cat is interested in a moving box flap" — one image; bridge/truck simile — one image) |
| 8 | Literary language does not dominate | PASS |
| 9 | Mystery remains complex | PASS (Mystery-001: no movement by design; the chapter's work is relational) |
| 10 | Atmosphere remains strong | PASS |
| 11 | Character voice intact | PASS (Saito's banter, Hasegawa's dryness, Arthur's clerk-register all preserved) |
| 12 | Does not feel childish after simplification | PASS |
| 13 | No dictionary needed for basic comprehension | PASS |
| 14 | Beauty through imagery/behavior/implication | PASS |
| 15 | Language simpler than the story | PASS |

### WATCH items (deliberate non-changes)
- "the tube flickers… Arthur filmed it. He's facilities' deputy now." / "Deputy of Facilities" running joke — kept: relational engine of the chapter; banter is plain English already.
- Saito's "not suspicious, just turning the thing over" beat — kept verbatim: canon continuity (Saito must not become suspicious yet).
- "It was also, in this specific corridor, at two in the morning, aimed at the one thing Arthur had." — kept: simple words, load-bearing.
- "a lie wasn't a moment. It was a record. Records needed upkeep." — kept: thesis of the chapter; plain language already.
- "in about four seconds, he had decided there was something he would not show Saito" — kept: no doctrine talk (tool-vs-weather never named) per blueprint.
- The deliberate unknowns (9/18 overlap UNDETERMINED; Saito's two-second glance UNRESOLVED) were not encountered as editable material and were not touched.
- No rare synonyms for ordinary actions (grep: zero hits). Zero "not X, but Y" constructions.

**Final gate:** Easier to read, the lie's pricing untouched → **YES, keep.**

---

## SUMMARY

| Ch | Orig SHA | New SHA | Words | Sents rev/changed | §50 PASS | WATCH | FAIL |
|----|----------|---------|-------|-------------------|----------|-------|------|
| 001 | da9bbe73… | ca68422d… | 2516 → 2512 | 191 / 1 | 15 | 0 | 0 |
| 002 | 0df97c62… | 8cd831f3… | 2391 → 2392 | 160 / 1 | 15 | 0 | 0 |
| 003 | 9ef9a0af… | (unchanged) | 2273 → 2273 | 156 / 0 | 15 | 0 | 0 |
| 004 | 8590ebb6… | 45193866… | 1988 → 1983 | 147 / 1 | 15 | 0 | 0 |
| 005 | cec53960… | 0e5225cc… | 2257 → 2255 | 139 / 1 | 15 | 0 | 0 |

**Totals:** 793 sentences reviewed, 4 sentences changed (all single-sentence, minimal edits: 1 AMBIGUITY_REDUCTION + 1 AMBIGUITY_REDUCTION + 1 CLEARER_WORDING/SENTENCE_SIMPLIFICATION + 1 CLEARER_WORDING). Zero plot/character/mystery/timeline/ending changes. All diffs verified against the pristine copy. All 5 chapters pass the §50 audit 15/15 with 0 FAIL; the WATCH ledger above records every deliberate non-change with its reason. Canon boundaries held throughout: 3.0s kept flat (ch. 4), Saito unsuspicious (ch. 5), Yuko's silence unexplained (ch. 3), 9/18 overlap UNDETERMINED, Saito's two-second glance UNRESOLVED, ASCII names unchanged, specialized + cultural vocabulary preserved (rotated, not removed).


---

## SECTION: `AUDIT/READABILITY_WORKLOG_BLOCK_B.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/READABILITY_WORKLOG_BLOCK_B.md` · sha256 `66c535a6f0b70bbb33f84679044a7e77f088bb193bcaf1a2cf9d698244dc4924` · 3,393 words. No content changed.

# READABILITY WORKLOG — BLOCK B (Chapters 006–010)

**Worker:** Readability Revision Worker (Block B)
**Date:** 2026-09-21
**Scope:** `CHAPTERS/006_Dark_Water.md`, `CHAPTERS/007_No_Category.md`, `CHAPTERS/008_Melon_Pan.md`, `CHAPTERS/009_Impossible_Constancy.md`, `CHAPTERS/010_The_Cordon.md` in `~/workspace/world_bible/work_readability/` ONLY. No other files touched.
**Standard:** `DATABASE/FAST_PACE_DEEP_MYSTERY_RETENTION_SOP.md` — Part II §§37–50 (lines 1040–1471) + Part I §§13, 14, 34 read in full before work began.
**Guiding rule:** SIMPLIFY THE DELIVERY, NOT THE IDEA ("Easy words + deep ideas").

## BASEmessaging app VERIFICATION

All 5 working-copy checksums matched `AUDIT/_BASEmessaging app_READABILITY.txt` exactly before editing (a9e52601…, 8b35cb97…, bc9a9d67…, 58576e91…, 9eaf1b83…). Word counts also matched baseline (2037 / 2497 / 2249 / 2033 / 2042).

## DIFF VERIFICATION (readability-only)

Each chapter was diffed against the pristine copy at `~/workspace/world_bible/00_WORLD_BIBLE/CHAPTERS/`. The complete diffs are exactly the sentence-level changes listed below — no plot, event, decision, motivation, foreshadowing, timeline, or ending changes; no additions or removals of content; no character or place renames; specialized and cultural vocabulary preserved (rotated, not removed).

Rare-synonym sweep across all 5 chapters (proceeded/utilized/subsequently/commenced/ascertained/necessitated/endeavor/whilst/amongst): zero hits. "not X, but Y" inflation: zero instances.

---

## CHAPTER 006 — "Dark Water"

- **Original checksum:** `a9e52601444f87687c48fdb00e1f211375674e2246bffee40395a3c108f92755`
- **New checksum:** `2f49a09e62030496919deeb23b6e27fbf20aaabca5067f6cd44547540b31ab1f`
- **Word count:** 2037 → 2035 (−2)
- **Sentences reviewed / changed:** 129 / 3 sentences (4 edits)

### Changes (taxonomy-classified)

1. **SENTENCE_SIMPLIFICATION** (40-word sentence with double em-dash interruption → 2 sentences)
   - BEFORE: "He picked up his phone off the low table — 12:04 now, the alarm still armed and smug for 15:00, never having fired — and opened the notes app, not the dream, just the *facilities flicker log*, the cover heading doing its cover work."
   - AFTER: "He picked up his phone off the low table — 12:04 now, the alarm still armed and smug for 15:00, never having fired — and opened the notes app. Not the dream: just the *facilities flicker log*, the cover heading doing its cover work."
   - Reason: the parenthetical + triple apposition stacked three ideas in one breath; §8(1) first-read comprehension. The fragment "Not the dream:" matches existing chapter rhythm ("Stress." "Two entries."). Humor ("smug") and cover-log meaning preserved.

2. **CLEARER_WORDING** (abstract noun → ordinary verb)
   - BEFORE: "by performing normalcy until it became real"
   - AFTER: "by acting normal until it became real"
   - Reason: "normalcy" is a rare abstract noun for an ordinary idea; "acting normal" says the same thing with Level 1 vocabulary. The performative meaning (he is *performing* coping) is retained by the later parallel "performing the gesture of a person handling it," which was deliberately kept (see WATCH).

3. **CLEARER_WORDING** (article fix; no meaning change)
   - BEFORE: "as non-negotiable budget line in the ledger of being alive"
   - AFTER: "as a non-negotiable budget line in the ledger of being alive"
   - Reason: missing article read as an error, not voice; purely grammatical repair.

4. **CLEARER_WORDING** (unusual word sense → plain sense)
   - BEFORE: "the daytime register of everything the night shift only got the cooled-down version of"
   - AFTER: "the daytime version of everything the night shift only knew cooled-down"
   - Reason: "register" (sense/level) is an uncommon word sense with no tonal function here; "version" is immediately clear. Note: ch. 9's different sense of "register" (speech tone) was simplified separately to "tone".

### §50 Readability Audit

| # | Item | Result |
|---|------|--------|
| 1 | First-read comprehension | PASS |
| 2 | Ordinary vocabulary | PASS |
| 3 | Specialized-vocab necessity | PASS (manifest, un-audited, protective charm — all voice/precision-carrying) |
| 4 | Specialized-vocab density | PASS |
| 5 | Contextual anchoring | PASS |
| 6 | Idiom accessibility | WATCH ("didn't read as water" / "The water read wrong" — perceptual idiom kept as deliberate character voice; meaning recoverable from context) |
| 7 | Metaphor accessibility | PASS (file-drawer simile, "occupied" — simple words, meaning-bearing) |
| 8 | Cultural-vocab accessibility | PASS (convenience store, dorayaki, protective charm, messaging app, 完食 — all context-anchored) |
| 9 | Sentence complexity | PASS (long sentences are idea-complex, e.g. the harbor-water description) |
| 10 | Pronoun clarity | PASS |
| 11 | Dialogue clarity | PASS (minimal dialogue; clear) |
| 12 | Paragraph readability | PASS |
| 13 | Vocabulary repetition | PASS (thematic filing words varied: box, drawer, shelf, label, file) |
| 14 | Atmosphere preservation | PASS (quiet dread, tea-colored light, harbor wrongness all intact) |
| 15 | Character-voice preservation | PASS (clerk-eye rhythm, understated humor intact) |

### WATCH items (deliberate non-changes)
- "an unfiled thing didn't get to be called weather" — kept: Arthur's filing-doctrine voice; passes §8(2–3), creates character meaning. Do not simplify.
- "performing the gesture of a person handling it" — kept: deliberate parallelism with the earlier "performing normalcy" (performance-of-coping motif); simplifying both would flatten the motif.
- "un-audited" (heart doing something un-audited) — kept: archive vocabulary applied to the body; character voice, context-clear.
- "after the split with Saito at the station" — kept: "split" as noun is mildly informal but meaning is recoverable; consistent with ch. 10's "They split at the station".
- "the tribe nod" — kept: series-established term (ch. 2), anchored.
- Standing canon WATCHes respected, untouched: 9/18 overlap UNDETERMINED; Mystery 001 unresolved; Mystery 002 dream-seed only (no entity language — verified: "direction, not shape" preserved).

---

## CHAPTER 007 — "No Category"

- **Original checksum:** `8b35cb979d93d8683fb44c2350be0052a9b694833c875cc93118171e452958b9`
- **New checksum:** `1bd9c28aa67a671f1b281990179a7eb762119ccdda089bdeab35eac14eb2a751`
- **Word count:** 2497 → 2501 (+4)
- **Sentences reviewed / changed:** 159 / 2 sentences (2 edits)

### Changes (taxonomy-classified)

1. **CLEARER_WORDING** (formal connective → plain connective)
   - BEFORE: "It was the institution's memory of the strange, insofar as the strange ever reached the institution."
   - AFTER: "It was the institution's memory of the strange, as far as the strange ever reached the institution."
   - Reason: "insofar as" is formal/academic with no tonal function; "as far as" is the plain equivalent. "That qualifier mattered" still refers cleanly.

2. **SENTENCE_SIMPLIFICATION** (unstacking three specialized terms)
   - BEFORE: "He worked shelf by shelf, pulling manifests, reading finding aids, checking the labels' own marginalia — the little notes archivists left for each other: *water damage, see box 12*; *1996 — reboxed after leak*; *do not reshelve without manifest update*."
   - AFTER: "He worked shelf by shelf, pulling manifests and reading finding aids. Then he checked the labels' own marginalia — the little notes archivists left for each other: *water damage, see box 12*; *1996 — reboxed after leak*; *do not reshelve without manifest update*."
   - Reason: §38 forbids stacking several difficult terms in one sentence; "manifests / finding aids / marginalia" were stacked. Split per §48(a): ROTATE, DO NOT REMOVE — no term removed, no dictionary-style definition inserted (the marginalia's existing self-explanation was kept as the anchor).

### §50 Readability Audit

| # | Item | Result |
|---|------|--------|
| 1 | First-read comprehension | PASS |
| 2 | Ordinary vocabulary | PASS |
| 3 | Specialized-vocab necessity | PASS (reshelve, manifest, marginalia, finding aids — archive-work precision; Hasegawa bottleneck canon intact) |
| 4 | Specialized-vocab density | PASS (stacked instance split; no other stacking) |
| 5 | Contextual anchoring | PASS (marginalia self-explained; kanji search terms glossed inline) |
| 6 | Idiom accessibility | PASS ("come knocking as paperwork," "living the dream" — common, contextual) |
| 7 | Metaphor accessibility | PASS (lighthouse simile, "weather-front of briskness" — concrete) |
| 8 | Cultural-vocab accessibility | PASS (影/遅れ/照明 with English glosses; reshelve as workplace term) |
| 9 | Sentence complexity | PASS |
| 10 | Pronoun clarity | PASS |
| 11 | Dialogue clarity | PASS (Saito/Okada/Hasegawa exchanges clean) |
| 12 | Paragraph readability | PASS |
| 13 | Vocabulary repetition | PASS (index/manifest/register/ledger/boxes rotated; §14 respected) |
| 14 | Atmosphere preservation | PASS (B2–B3 basement quiet, dust, paper — intact) |
| 15 | Character-voice preservation | PASS (clerk-method narration, dry humor intact) |

### WATCH items (deliberate non-changes)
- "a disproof expedition" — kept: playful, context-clear; mild and voice-serving.
- "their familiar since-March complaint" (cart wheels) — kept: compound adjective, recoverable, characterful.
- "the color of old teeth" (yellowed tape) — kept: concrete image, §44-approved beauty.
- "which meant the nothing was institutional" — kept: abstract but simple words; the chapter's thesis line; simplifying would explain the feeling.
- Ticker stays one line, uncommented ("marine agency reports unusual tidal readings…") — canon: MYSTERY-015 texture only, no question posed. Untouched.
- Hasegawa deliberately NOT consulted — canon bottleneck preserved. Untouched.
- Day-label continuity (Thu 9/10 night → Fri 9/11 dawn): investigated and cleared in a prior phase; not "fixed".

---

## CHAPTER 008 — "Melon Pan"

- **Original checksum:** `bc9a9d67e284464693021f32d3042aa16308a17146cb477125092b2149508740`
- **New checksum:** `bc9a9d67e284464693021f32d3042aa16308a17146cb477125092b2149508740` (UNCHANGED)
- **Word count:** 2249 → 2249 (±0)
- **Sentences reviewed / changed:** 159 / 0

### Changes (taxonomy-classified)

None. Full chapter read (all 159 sentences). Every candidate friction point tested against §8 and found deliberate: the long emotional sentences carry idea-complexity (the almost-confession, the cost itemized as loneliness), not wording-complexity; figurative language is selective and meaning-bearing; no rare synonyms for ordinary actions; no formulaic template repetition.

### §50 Readability Audit

| # | Item | Result |
|---|------|--------|
| 1 | First-read comprehension | PASS |
| 2 | Ordinary vocabulary | PASS |
| 3 | Specialized-vocab necessity | PASS |
| 4 | Specialized-vocab density | PASS ("liturgy," "load-bearing," "legible" — single, spaced, context-anchored) |
| 5 | Contextual anchoring | PASS |
| 6 | Idiom accessibility | WATCH ("tired to the bone" — common idiom kept as the deliberate closing beat; guessable from context) |
| 7 | Metaphor accessibility | PASS ("queued up behind his teeth like claims waiting for a stamp" — simple words, core meaning) |
| 8 | Cultural-vocab accessibility | PASS ("Tiga last week, dua this week" / "satu" — Nadia's Indonesian code-switching; numbers anchored by the melon-pan count context; convenience store preserved) |
| 9 | Sentence complexity | PASS (the 62-word "week's real shape" sentence and the "safe sentence" passage are idea-complex; kept per §39) |
| 10 | Pronoun clarity | PASS |
| 11 | Dialogue clarity | PASS (Nadia/Arthur dawn dialogue clean and voiced) |
| 12 | Paragraph readability | PASS |
| 13 | Vocabulary repetition | PASS |
| 14 | Atmosphere preservation | PASS (fluorescent dawn, curb ritual — intact) |
| 15 | Character-voice preservation | PASS (Arthur's ledger-humor; Nadia's bright-fast voice — intact) |

### WATCH items (deliberate non-changes)
- "legible" ("Tired was honest. Tired was legible.") — kept: the honest/legible pairing creates meaning (true + readable-by-others); context anchors it.
- "the liturgy held" — kept: single figurative use, ritual context clear.
- The withheld-confession passage ("He filed it instead. 'Fine,' he said. 'Friday did its usual.'") — kept verbatim: emotional subtext must never be explained; ending and beats unchanged.
- Nadia's dream (extra floors / B4) — Mystery texture; untouched, no interpretation added.

---

## CHAPTER 009 — "Impossible Constancy"

- **Original checksum:** `58576e91e8b40e28c6fde593f133538f62fd2045640d55b7c67510b081da06e3`
- **New checksum:** `19345b052e39f704c416643409ae7c13823a31dc09cea36dc93a94414eb02a2e`
- **Word count:** 2033 → 2032 (−1)
- **Sentences reviewed / changed:** 123 / 2 sentences (2 edits)

### Changes (taxonomy-classified)

1. **SENTENCE_SIMPLIFICATION** (46-word opening sentence with double em-dash delay → 2 sentences)
   - BEFORE: "The alarm went off at 15:00 and he woke at 15:04, which for him counted as punctual, and the first thing he registered — before the room's flat gray gloom, before the wood of the building ticking as it cooled — was that he was rested."
   - AFTER: "The alarm went off at 15:00 and he woke at 15:04, which for him counted as punctual. The first thing he registered was that he was rested — before the room's flat gray gloom, before the wood of the building ticking as it cooled."
   - Reason: the em-dash interruption delayed the main verb across 46 words; the sensory list is preserved in place, only the clause path is shortened. §8(1).

2. **CLEARER_WORDING** (uncommon word sense → plain sense)
   - BEFORE: "point card, no, thank you, the register of people who had done this ten thousand times"
   - AFTER: "point card, no, thank you, in the tone of people who had done this ten thousand times"
   - Reason: "register" as speech-tone is a linguistic term obscure to non-native readers; "tone" is the plain equivalent. (Distinct from ch. 6's "daytime register" → "daytime version"; each sense simplified to its own plain word.)

### §50 Readability Audit

| # | Item | Result |
|---|------|--------|
| 1 | First-read comprehension | PASS |
| 2 | Ordinary vocabulary | PASS |
| 3 | Specialized-vocab necessity | PASS ("falsification" kept as his method-doctrine vocabulary — see WATCH; 240fps/frames are technical but explained in-line) |
| 4 | Specialized-vocab density | PASS |
| 5 | Contextual anchoring | PASS (720 frames = 3 seconds derived on-page) |
| 6 | Idiom accessibility | PASS |
| 7 | Metaphor accessibility | PASS (understudy simile, "rumors of shadows" — concrete, meaning-bearing) |
| 8 | Cultural-vocab accessibility | PASS (natto; おかえりなさい/すみません — situation-anchored) |
| 9 | Sentence complexity | PASS (the 62-word polysyndeton climax is idea-complex; kept per §39 — see WATCH) |
| 10 | Pronoun clarity | PASS |
| 11 | Dialogue clarity | PASS (minimal; clear) |
| 12 | Paragraph readability | PASS |
| 13 | Vocabulary repetition | PASS |
| 14 | Atmosphere preservation | PASS (Saturday-experiment quiet, stairwell dimness — intact) |
| 15 | Character-voice preservation | PASS (premises-first method voice, dry humor intact) |

### WATCH items (deliberate non-changes)
- "So the falsification was simple" — kept: "falsification" is his method vocabulary (Mystery 013 doctrine register), and the sentence immediately operationalizes it ("change the light"); simplifying to "disproving" would lose the audit-method tone. §38 Level 3: keep when precision matters.
- The 62-word closing-build sentence ("…and the day had produced exactly one sentence, and the sentence was a question…") — kept: deliberate ledger-rhythm accumulation; idea-complex, not wording-complex. Per §34, the polysyndeton is a single-occurrence rhythm, not a template.
- Closing question "What casts a shadow independent of light geometry?" — kept verbatim: chapter ending unchanged (canon: QUESTION ending type).
- Inference stays fragile ("working, not firm") — untouched; no THEORY→FACT collapse. Lag stays 3.0s flat (no ratchet; SECRET-003 untouched).

---

## CHAPTER 010 — "The Cordon"

- **Original checksum:** `9eaf1b83e71d17b203eebcd4c418e073bde41b0f226208ebf8e14d2290bb42ef`
- **New checksum:** `f142b9a5d37ecb5957505e1716c52713a943c7a9656f03ec475c7721eaf45b0d`
- **Word count:** 2042 → 2043 (+1)
- **Sentences reviewed / changed:** 138 / 1 sentence (1 edit)

### Changes (taxonomy-classified)

1. **SENTENCE_SIMPLIFICATION** (85-word canon-exposition sentence → 5 sentences)
   - BEFORE: "Back then he'd noticed something small about the second shadow, by accident — it didn't only lag behind him. A moth had crossed the corridor tube once and the moth's flutter had stayed in the shadow a beat after the moth was gone, and he'd understood he could look at the shadow and see again what he'd just seen; he'd tested it on purpose exactly once, the next night — tipped a box slip off the cart and watched the slip's fall kept in the shadow after the slip had settled — then filed it away as a curiosity. He hadn't needed it since."
   - AFTER: "Back then he'd noticed something small about the second shadow, by accident — it didn't only lag behind him. A moth had crossed the corridor tube once, and the moth's flutter had stayed in the shadow a beat after the moth was gone. He'd understood then that he could look at the shadow and see again what he'd just seen. He'd tested it on purpose exactly once, the next night — tipped a box slip off the cart and watched the slip's fall kept in the shadow after the slip had settled — then filed it away as a curiosity. He hadn't needed it since."
   - Reason: 85 words with semicolon-chained beats exceeded §39's target far beyond "when natural"; every canon fact preserved verbatim (moth flutter, one deliberate box-slip test, filed as curiosity). Only clause boundaries changed. Added "then" is a connective, not new content.

### §50 Readability Audit

| # | Item | Result |
|---|------|--------|
| 1 | First-read comprehension | PASS |
| 2 | Ordinary vocabulary | PASS |
| 3 | Specialized-vocab necessity | PASS (cordon, discrepancy — precision terms; Veil/Loud vocabulary correctly absent per canon) |
| 4 | Specialized-vocab density | PASS |
| 5 | Contextual anchoring | PASS |
| 6 | Idiom accessibility | PASS ("Deputy of Detours" — joke title, clear) |
| 7 | Metaphor accessibility | PASS ("bare as a new form," "figures that wouldn't balance" — concrete/accounting, clear) |
| 8 | Cultural-vocab accessibility | PASS (sawhorses, ward seal, Discord — clear) |
| 9 | Sentence complexity | PASS (Use-1 application sentence kept dense deliberately — the mechanism reveal; idea-complex) |
| 10 | Pronoun clarity | PASS |
| 11 | Dialogue clarity | PASS (Saito/Okada/Hasegawa lines clean) |
| 12 | Paragraph readability | PASS |
| 13 | Vocabulary repetition | PASS |
| 14 | Atmosphere preservation | PASS (cordon wrongness: brine, swept street, plain van — intact) |
| 15 | Character-voice preservation | PASS (manifest-itemization voice, dry humor intact) |

### WATCH items (deliberate non-changes)
- Saito's glance ("Saito was glancing at him — or past him, at the van. The glance held a beat too long, and he couldn't tell which of them it was for.") — kept VERBATIM: UNRESOLVED per canon; any clarifying edit would collapse the ambiguity. Also "Saito's glance he left out of the manifest" kept verbatim.
- "My memory doesn't rot like theirs. I am different and must hide it." — kept VERBATIM: the chapter's reversal thesis; no Loud/Veil vocabulary added (canon: concepts unavailable to him).
- "the sea with no harbor" — kept: figurative compression of the brine detail; context-anchored.
- The 62-word Use-1 application sentence ("He turned his head… the side unbroken where a company's mark would go.") — kept: mystery-complexity, idea-dense by design; splitting would dilute the turning-point beat.
- Cordon NEVER attributed — verified: no faction markings added, no identifying language; "Gas leak" official line preserved as-is.
- Chapter ending ("…closed the drawer, and went back to work.") — unchanged. REVERSAL ending type intact.
- "why do I remember what they lose?" — posed, not pursued; untouched.

---

## BLOCK B SUMMARY

| Chapter | Orig → New words | Sentences reviewed | Sentences changed | Edits | §50 PASS | §50 WATCH | §50 FAIL |
|---|---|---|---|---|---|---|---|
| 006 "Dark Water" | 2037 → 2035 | 129 | 3 | 4 | 14 | 1 | 0 |
| 007 "No Category" | 2497 → 2501 | 159 | 2 | 2 | 15 | 0 | 0 |
| 008 "Melon Pan" | 2249 → 2249 | 159 | 0 | 0 | 14 | 1 | 0 |
| 009 "Impossible Constancy" | 2033 → 2032 | 123 | 2 | 2 | 14 | 1 | 0 |
| 010 "The Cordon" | 2042 → 2043 | 138 | 1 | 1 | 15 | 0 | 0 |
| **Total** | **10358 → 10360** | **708** | **8** | **9** | **72** | **3** | **0** |

**Taxonomy breakdown of the 9 edits:** SENTENCE_SIMPLIFICATION ×4, CLEARER_WORDING ×5 (of which 2 are the two senses of "register" → "version"/"tone", 1 article fix, 1 formal-connective fix, 1 abstract-noun fix). No IDIOM_CLARIFICATION, CONTEXTUAL_ANCHOR, AMBIGUITY_REDUCTION, VOCABULARY_ROTATION, PARAGRAPH_FLOW, or RHYTHM_CORRECTION edits were needed — the chapters were already strong on those dimensions.

**Canon integrity:** No plot, event, decision, motivation, foreshadowing, timeline, or ending changes. Truth layers preserved (Mystery 001 unresolved; Mystery 002 dream-seed only, no entity language; Mystery 013 remains Arthur's doctrine, never objective truth). Standing WATCHes respected: 9/18 overlap UNDETERMINED, Saito's two-second glance UNRESOLVED (kept verbatim), 007/008 day-labels not "fixed" (prior phase cleared). ASCII names intact (Saito, Yuko — no non-ASCII names appear in this block). Cultural vocabulary preserved (convenience store, rice ball n/a, messaging app, nikujaga n/a, natto, protective charm, dorayaki). Specialized vocabulary rotated, not removed.

**Final gate (per chapter):** "Is this chapter easier for a non-native reader WITHOUT making the story easier to understand?" — YES for all five (ch. 008 trivially: nothing was hard for the wrong reasons). Atmosphere, mystery depth, character voice, and understated humor verified intact in each chapter's §50 items 14–15.


---

## SECTION: `AUDIT/READABILITY_WORKLOG_BLOCK_C.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/READABILITY_WORKLOG_BLOCK_C.md` · sha256 `c944fd9f8c09be733c6bd3716b0fabac36f01ae1be450036dcf176ec36d75449` · 2,725 words. No content changed.

# READABILITY WORKLOG — BLOCK C (CHAPTERS 011–015)

**Worker:** Readability Revision Worker (block C)
**Date:** 2026-09-21
**Scope:** `~/workspace/world_bible/work_readability/CHAPTERS/` — 5 files only
**Standard:** DATABASE/FAST_PACE_DEEP_MYSTERY_RETENTION_SOP.md Part II §§37–50 (read in full, lines 1040–1471) + Part I §§8, 13, 14, 34 (read in full)
**Governing principle:** SIMPLIFY THE DELIVERY, NOT THE IDEA — "Easy words + deep ideas"
**Blueprint cross-check:** DATABASE/CHAPTER_BLUEPRINT_001_020.md §§ CH-011 through CH-015 (each read in full before revising)

## Baseline verification
- All 5 files matched `AUDIT/_BASEmessaging app_READABILITY.txt` checksums before editing: CONFIRMED.
- Pristine copies in `~/workspace/world_bible/00_WORLD_BIBLE/CHAPTERS/` also matched baseline: CONFIRMED.
- Word counts used the python3 method (`len(open(f,encoding='utf-8').read().split())`), which agrees with the baseline file's counts.
- Sentence counts are approximate (regex split on sentence-terminal punctuation); they measure review coverage, not precision.

---

## CH-011 "Aftershock" — 011_Aftershock.md

- **Original checksum:** `9307b5bcdd2945b208e8ad99a5e95d2c5674733574f049f9d0d2f70f6fc9a2e8`
- **New checksum:** `82cf82baaa90fb6f73751ef028d1f2ca5da111bcc4e32b1c0d41beb0689f88d5`
- **Word count:** 2480 → 2476 (−4)
- **Sentences reviewed:** ~206 | **Sentences changed:** 6
- **Blueprint verified:** purpose = price the aftermath (hypervigilance + reaffirmed silence); no plot/motivation/timeline changes made. Saito's two-second glance stays causally ambiguous. Lag stays at 3.0s.

### Change list (classified by taxonomy)

1. **CLEARER_WORDING**
   - Before: "Just that the doing it, on time, the same as always, required him to decide to do it, and deciding made it a performance."
   - After: "Just that doing it, on time, the same as always, meant deciding to do it, and deciding made it a performance."
   - Reason: "the doing it" noun-phrase was clunky; idea (the ordinariness required a decision = performance) unchanged.

2. **CLEARER_WORDING**
   - Before: "It wasn't that keeping quiet was hard; it was that it kept un-keeping itself, in little installments, at the most ordinary moments — reaching for a folder, waiting for the elevator, watching the second hand sweep."
   - After: "It wasn't that keeping quiet was hard; it was that it kept coming undone, in little installments, at the most ordinary moments — reaching for a folder, waiting for the elevator, watching the second hand sweep."
   - Reason: "un-keeping" is a coinage that costs first-read comprehension; "coming undone" keeps the exact idea. (Also rotated consistently with change 6.)

3. **IDIOM_CLARIFICATION**
   - Before: "It landed flat, between them."
   - After: "It fell flat, between them."
   - Reason: "fell flat" is the standard, recoverable idiom (Saito's "You look tired" failed to land lightly); same meaning.

4. **SENTENCE_SIMPLIFICATION**
   - Before: "At 02:55 he stood up from the terminal, stretched until his back cracked, and volunteered for the 03:00 cart run — a thing he could not quite have justified to himself, except as diligence."
   - After: "At 02:55 he stood up from the terminal, stretched until his back cracked, and volunteered for the 03:00 cart run — he couldn't quite justify it to himself, except as diligence."
   - Reason: "a thing he could not quite have justified" is convoluted nesting for a simple idea.

5. **CLEARER_WORDING**
   - Before: "The old files lived here, boxes with hand-written labels from a decade of gone clerks, the air smelling of dust, cardboard, and the elevator's faint oil."
   - After: "The old files lived here, boxes with hand-written labels from a decade of clerks long since gone, the air smelling of dust, cardboard, and the elevator's faint oil."
   - Reason: "a decade of gone clerks" is an odd adjective placement; plain word order, same image.

6. **CLEARER_WORDING**
   - Before: "He had decided, and the decision would keep un-making itself, and he would keep making it again. That was the work now."
   - After: "He had decided, and the decision would keep coming undone, and he would keep making it again. That was the work now."
   - Reason: same coinage issue as change 2; rotated to match, preserving the bill/invoice motif around it. Chapter ending unchanged.

### §50 audit table (CH-011)

| # | Item | Result |
|---|------|--------|
| 1 | Important sentences immediately understandable | PASS |
| 2 | Everyday actions use simple English | PASS |
| 3 | Specialized vocabulary is necessary | PASS |
| 4 | Specialized vocabulary is contextually understandable | PASS |
| 5 | Difficult words are not unnecessarily stacked | PASS |
| 6 | Sentence complexity serves meaning | PASS |
| 7 | Figurative language is selective | PASS |
| 8 | Literary language does not dominate | PASS |
| 9 | Mystery remains complex | PASS |
| 10 | Atmosphere remains strong | PASS |
| 11 | Character voice remains intact | PASS |
| 12 | Does not feel childish after simplification | PASS |
| 13 | No dictionary needed for basic comprehension | PASS |
| 14 | Beauty through imagery, behavior, implication | PASS |
| 15 | Language is simpler than the underlying story | PASS |

**Final gate:** "Is this chapter easier for a non-native reader WITHOUT making the story easier to understand?" → YES. Keep.

### WATCH items — CH-011 (deliberate non-changes)
- Kept "The night air had teeth." — selective metaphor; creates the B3-run atmosphere; meaning clear.
- Kept "rinsed the ghost of heat from his hands" — selective imagery, single use.
- Kept "Not a sign, but the absence of one, wearing the shape of a sign." — the chapter's thematic beat; creates meaning, not ornament.
- Kept "the meaning billing him at intervals" — bill/invoice thematic vocabulary (rotation, not removal).
- Kept flat comma-punctuated dialogue questions ("What are you reading," / "Then why are you reading it.") — deliberate understated tone; consistent across chapters 011–015; changing it would flatten a voice choice.
- Kept "smiled, unbidden, into his paperwork" — "unbidden" is context-recoverable; preserves cadence.
- Kept "Your funeral when you're late." — common recoverable idiom; dry humor intact.
- Kept "reallocated" (the dread "had been reallocated") — intermediate but context-clear; thematic accounting word.
- No change touched the van/brine replay (memory-texture only, never upgraded to a clue), Saito's glance (causally ambiguous), or the 3.0s lag.

---

## CH-012 "The Private Ledger" — 012_The_Private_Ledger.md

- **Original checksum:** `8ab94dd69e06b69ef22b0669e378706bf9bf27a013975c3e3fdba043febced34`
- **New checksum:** `8ab94dd69e06b69ef22b0669e378706bf9bf27a013975c3e3fdba043febced34` (UNCHANGED)
- **Word count:** 2491 → 2491 (0)
- **Sentences reviewed:** ~171 | **Sentences changed:** 0
- **Blueprint verified:** purpose = convert the ch.11 decision into the ledger system + camouflage thesis; the thesis lines and measurement readings are evidentiary substance — all preserved verbatim, including *Stay small. Stay beneath every instrument.*, *Tier 1. The boring tier. File everything there. If it can't be filed at Tier 1, it doesn't get filed.*, *Cost: the file exists. It can be read. Priced: ordinary frame, on my person, deniable.*, and the three discrepancy entries with *Discrepancy: 3.0*.

### Change list
None. The chapter was read in full and already meets the standard: ordinary actions use plain English, specialized terms (doctrine, manifest, discrepancy, reshelve, camouflage) are necessary and context-anchored, sentences are concrete, figurative language is selective and meaningful. Per §46 ("DO NOT automatically simplify every sentence"), no edits were made. This is an honest zero, not an omission.

### §50 audit table (CH-012) — 15/15 PASS
Items 1–15 all PASS (same table as CH-011; no failures or watches on any item). Mystery intact (001 unmoved; cipher mechanism shown without the key). Atmosphere, Arthur's clerk voice, and the thesis weight all preserved.

**Final gate:** N/A — no changes made; nothing was made easier to understand because nothing needed simplification.

### WATCH items — CH-012 (deliberate non-changes)
- Kept "The shift ran its channels." / "The shift ran its last channels." — deliberate voice phrase (2×); meaning recoverable from context.
- Kept "Opinions rationed tight" — deliberate echo of ch.011's "Opinions rationed like cigarettes" (character texture).
- Kept "the wallpaper of the wallpaper" — deliberate echo of Hasegawa's camouflage thesis; the point is the echo.
- Kept "the way fish knew water" — common idiom.
- Kept "tape yellowed to the color of old teeth" — single vivid simile; clear.
- All thesis lines and measurement entries preserved verbatim per canon boundary.

---

## CH-013 "The Night Keeps" — 013_The_Night_Keeps.md

- **Original checksum:** `dfde77b23a4c267dc01fa898308ea366f90feb71f7606040e18c75545ef77156`
- **New checksum:** `dfde77b23a4c267dc01fa898308ea366f90feb71f7606040e18c75545ef77156` (UNCHANGED)
- **Word count:** 1984 → 1984 (0)
- **Sentences reviewed:** ~165 | **Sentences changed:** 0
- **Blueprint verified:** transition chapter by design (rest with texture; no opposing force). The old man stays unnamed with no lore (not IND-004 on-page); his line "The night keeps what the day drops" functions as ambient texture, never as a clue — untouched. Break-rotation cover stays ordinary; Okada's trust beat intact. Chapter ending (TRANSITION) unchanged.

### Change list
None. Full read confirms the chapter is concrete, sensory, and plain-spoken throughout; its literary moments ("The night keeps what the day drops", "The night didn't decorate", "Rest wasn't savings. It was currency.") are deliberate, selective, and meaning-carrying. Per §46, no edits made.

### §50 audit table (CH-013) — 15/15 PASS
Items 1–15 all PASS. Mystery intact (no movement by design). Atmosphere (the 3 a.m. curb) and character voice preserved; nothing childish; no dictionary needed.

**Final gate:** N/A — no changes made.

### WATCH items — CH-013 (deliberate non-changes)
- Kept "The night keeps what the day drops." — the title line; deliberate, and the blueprint forbids making it function as a clue, not making it simple.
- Kept "a salt-breathe at the bottom of the wind" — single selective figurative phrase; the harbor smell is atmosphere, and the meaning is clear.
- Kept comma-punctuated dialogue questions ("Is the suffering the peeling or the blackmail.") — consistent flat-tone choice with the other chapters.
- Kept "The fatigue had stepped back one pace" — the rest/currency metaphor is the chapter's load-bearing idea, stated plainly nearby.
- Kept the filing-instinct misfire on the old man's kindness ("Weird-old-man talk. That was the filing.") — blueprint character movement; simplifying it would sand down the beat.

---

## CH-014 "Three Point One" — 014_Three_Point_One.md

- **Original checksum:** `69319707c76d2550ab6644b280676616d6af0fc290966d0bc11507ea137bc34b`
- **New checksum:** `1e5222632a65d2b1baed8182c719df061bbc79d9d9a0def4c8a81e71135e495b`
- **Word count:** 2711 → 2714 (+3; the clearer sentence is three words longer — accepted)
- **Sentences reviewed:** ~184 | **Sentences changed:** 1
- **Blueprint verified:** the chapter earns its longer length — the methodical three-pass measurement IS the appraisal beat. Nothing shortened for readability's sake; only one sentence-level friction point was touched. All measurement readings preserved verbatim: 3.13, 3.11, 3.09/3.12/3.10 (avg 3.10), the ledger's "3.1", "a hair past", "past three". The lag's ambient nature preserved (no use, no cost paid — "he spent nothing"). The discovery ending (DISCOVERY type) unchanged. The 9/18 date overlap remains UNDETERMINED — untouched.

### Change list (classified by taxonomy)

1. **SENTENCE_SIMPLIFICATION**
   - Before: "He did it a third time on the landing, because one measurement could lie. The hand stood past three. Past. He stopped counting how much past and just stood there in the dark with his arm at his side, watching the red hand go around and around, taking three seconds longer than it should have to mean anything to him."
   - After: "He did it a third time on the landing, because one measurement could lie. The hand stood past three. Past. He stopped counting how much past and just stood there in the dark with his arm at his side, watching the red hand go around and around, and the shadow coming in past three, every time — and that was what it meant."
   - Reason: the original final clause stacked a participial phrase ("taking…"), a comparison ("than it should have"), and a purpose clause ("to mean anything to him") — it needed a re-read though the idea is simple (the shadow keeps arriving past the 3-second mark, and that delay is the meaning). The revision gives the shadow an explicit subject and states the idea directly, keeping the dread and the "past three" measurement language.

### §50 audit table (CH-014) — 15/15 PASS
Items 1–15 all PASS. Mystery intact and deepened (3.1s measured, price unknown, no rate inferred — the blueprint's "one delta is not a trend" is honored). Atmosphere (low-light aisle, stairwell landing) and the clerk's fact-stubborn voice preserved. Specialized/metrology terms (frames of grace, stopwatch, echo-bracket, discrepancy code) are necessary and context-anchored; none stacked.

**Final gate:** "Is this chapter easier for a non-native reader WITHOUT making the story easier to understand?" → YES. Keep.

### WATCH items — CH-014 (deliberate non-changes)
- Kept "the ledger sat in his trouser pocket like a coin on the tongue" — unusual but recoverable simile (a presence you can't ignore); single use.
- Kept "darker-dark" — deliberate coinage, context-clear (the landing beyond the quarter-power fixtures).
- Kept all measurement readings verbatim (evidentiary substance — never simplified).
- Kept chapter length; the ~2,714-word length is earned by the three-pass method structure, not friction.
- Did not infer a rate, schedule, or cause for the 3.1s; did not frame it as a Use or cost (canon boundary).

---

## CH-015 "Rent Day Arithmetic" — 015_Rent_Day_Arithmetic.md

- **Original checksum:** `7b3dd0fa536329c52b5d58874ae3d6fc416e5ccd2cfc24114aa4cc872898bda4`
- **New checksum:** `7b3dd0fa536329c52b5d58874ae3d6fc416e5ccd2cfc24114aa4cc872898bda4` (UNCHANGED)
- **Word count:** 2496 → 2496 (0)
- **Sentences reviewed:** ~185 | **Sentences changed:** 0
- **Blueprint verified:** money math exact and untouched (¥48,000 rent; ~¥230,000 salary; ~¥461,000 ≈ two months' savings; drift ¥20k–¥40k; one rent payment per month — ch.2's payment, ch.15 reconciles only). Yuko's second silence stays content-free (no interpretation, no Court content; the pause observed only as "a beat longer"). The 3.1s never intrudes — the ledger appears only as a physical object, unopened. Chapter ending (EMOTIONAL) unchanged.

### Change list
None. Full read confirms plain, concrete prose throughout; the money math is stated in exact numbers (the clearest possible delivery); the family dialogue is natural and recoverable; figurative language is selective and tied to meaning ("the numbers are honest", "Thin and known is fine"). Per §46, no edits made.

### §50 audit table (CH-015) — 15/15 PASS
Items 1–15 all PASS. Mystery intact (CHAIN-010 reinforced only as behavioral texture — "a beat longer", content-free). Atmosphere (Saturday-day-off ordinariness) and family voices (Nanami, Takashi, Yuko registers) preserved.

**Final gate:** N/A — no changes made.

### WATCH items — CH-015 (deliberate non-changes)
- Kept "let it say its piece" (alarm) — recoverable idiom, character voice.
- Kept "fifteen hundred hours" — clear in context (15:00 wake-up; night-shift register).
- Kept "The pause had been longer this time... the way you could feel a skipped stair in the dark" — the silence beat must stay observation-only per canon; simplifying the simile would weaken the observation without clarifying it.
- Kept comma-punctuated dialogue questions ("What do you see.", "Are you sleeping.") — consistent flat-tone choice.
- Kept "underlined it twice, aspirationally" — understated humor; clear.

---

## Block totals

| Chapter | Before (words) | After (words) | Sentences reviewed | Sentences changed | §50 PASS | §50 WATCH | §50 FAIL |
|---|---|---|---|---|---|---|---|
| 011 Aftershock | 2480 | 2476 | ~206 | 6 | 15 | 0 | 0 |
| 012 The Private Ledger | 2491 | 2491 | ~171 | 0 | 15 | 0 | 0 |
| 013 The Night Keeps | 1984 | 1984 | ~165 | 0 | 15 | 0 | 0 |
| 014 Three Point One | 2711 | 2714 | ~184 | 1 | 15 | 0 | 0 |
| 015 Rent Day Arithmetic | 2496 | 2496 | ~185 | 0 | 15 | 0 | 0 |
| **Total** | **12162** | **12161** | **~911** | **7** | **75** | **0** | **0** |

Diffs verified sentence-by-sentence against the pristine copies in `~/workspace/world_bible/00_WORLD_BIBLE/CHAPTERS/` — every diff line is a readability-only wording/simplification change; no plot, event, decision, motivation, timeline, foreshadowing, or ending changes anywhere in the block.

## Canon boundaries honored (block-wide)
- Reed Arthur remains 24, ordinary night-shift records clerk, Stage 1, zero Fathom; accessible, not simplified.
- Mystery 001 unresolved (3.1s measured but unexplained); Mystery 002 slow-seed untouched; Mystery 013 stays Arthur's doctrine, never stated as objective truth.
- The three truth layers preserved — no UNKNOWN→KNOWN, THEORY→FACT, or OBSERVATION→INTERPRETATION collapses.
- 9/18 date overlap left UNDETERMINED; Saito's two-second glance left UNRESOLVED; Yuko's silence left content-free.
- ASCII names kept (Saito, Yuko); specialized vocabulary rotated, never removed; cultural vocabulary (convenience store, rice ball, messaging app-implied messaging, nikujaga, protective charm) untouched; no Westernization.
- Ch.012's ledger thesis lines and all measurement readings preserved verbatim.
- No new repetitive simple-sentence patterns introduced; no "not X, but Y" inflation; replacement words rotated (undone ×2 in ch.011 only where the coinage appeared twice — deliberate, not a new template).


---

## SECTION: `AUDIT/READABILITY_WORKLOG_BLOCK_D.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/READABILITY_WORKLOG_BLOCK_D.md` · sha256 `20e6a6179d7dbf98398572ca9a565b79a569356c82e0af9b00bef1417b80fff6` · 2,830 words. No content changed.

# READABILITY WORKLOG — BLOCK D (CH-016 → CH-020)

**Date:** 2026-09-21 (WIB)
**Worker role:** Readability Revision Worker (block D)
**Scope:** `CHAPTERS/016_Sunday_Dinner_Again.md`, `017_The_Badge_Log.md`, `018_The_Unwritten_Rule.md`, `019_The_Photograph.md`, `020_Method.md` only. Nothing else touched.
**Governing standard:** `DATABASE/FAST_PACE_DEEP_MYSTERY_RETENTION_SOP.md` — Part II §§37–50 read in full (lines 1040–1471), plus Part I §§13 (anti-formulaic), 14 (vocabulary rotation), 34 (AI-fingerprint avoidance).
**Control principle:** "SIMPLIFY THE DELIVERY, NOT THE IDEA" / "Easy words + deep ideas."

**Method:** Full-chapter read of each chapter (every line) + its blueprint section in `DATABASE/CHAPTER_BLUEPRINT_001_020.md`. Edits applied only after passing the §8 sentence test and the per-chapter final gate ("Is this chapter easier for a non-native reader WITHOUT making the story easier to understand?"). All diffs verified against the pristine copy at `~/workspace/world_bible/00_WORLD_BIBLE/CHAPTERS/`. Word counts by `python3` whitespace split (matches baseline method).

**Totals:** 742 sentences reviewed across 5 chapters → 10 sentences changed → 732 sentences passed through unchanged. 13 WATCH items recorded (deliberate non-changes). Zero plot/character/mystery/canon alterations.

---

## CH-016 — "Sunday Dinner, Again"

- **Original checksum:** `b320edddd3477af422958848f43309c2cc29946daea5749bcc9d8d1ae800ab0e` (verified against `AUDIT/_BASEmessaging app_READABILITY.txt` — MATCH)
- **New checksum:** `0295e3921e14c5bc0f77bb01994b2cdd9b618105c6410fb0dc57b979b695da8b`
- **Word count:** 1938 → 1937 (−1)
- **Sentences reviewed / changed:** 158 / 5

### Change list (classified)

1. **[CLEARER_WORDING]** "some part of him had been **braced for** a different answer" → "some part of him had been **expecting a worse** answer." ("braced" is above-target vocabulary doing no extra work here; "expecting a worse answer" keeps the shame mechanics — relief proves he feared a finding.)
2. **[SENTENCE_SIMPLIFICATION]** "beyond the occasional **noise of assent**" → "beyond the occasional **murmur of agreement**." ("assent" is unnecessarily rare; the dad-beat humor and the assent rhythm are untouched.)
3. **[CLEARER_WORDING]** "in the tone of a man **delivering considered counsel**" → "in the tone of a man **giving serious advice**." ("counsel" adds sophistication only.)
4. **[CLEARER_WORDING]** "and the **inquest** was over" → "and the **questioning** was over." ("inquest" is a rare synonym for a light family joke; meaning identical.)
5. **[CLEARER_WORDING]** "There was no **absolution** in the drawer either" → "There was no **forgiveness** in the drawer either." ("absolution" is unnecessarily literary for "no one is forgiving him, including himself.")

### §50 Readability Audit (15 items)

| # | Item | Verdict |
|---|------|---------|
| 1 | Important sentences immediately understandable | PASS |
| 2 | Everyday actions use simple English | PASS |
| 3 | Specialized vocabulary necessary | PASS (manifest, ledger, file, cordon, catalogued — all story-functional; none removed) |
| 4 | Specialized vocabulary contextually understandable | PASS |
| 5 | Difficult words not unnecessarily stacked | PASS |
| 6 | Sentence complexity serves meaning | PASS |
| 7 | Figurative language selective | PASS |
| 8 | Literary language does not dominate | PASS |
| 9 | Mystery remains complex | PASS (MYSTERY-001: no movement; doorway check finds ordinary shadows; ambiguity intact) |
| 10 | Atmosphere remains strong | PASS |
| 11 | Character voice intact | PASS (family banter, Nanami's teasing, Takashi's Dad-isms untouched) |
| 12 | Chapter does not feel childish after simplification | PASS |
| 13 | No dictionary needed for basic comprehension | PASS |
| 14 | Beauty through imagery, behavior, implication | PASS |
| 15 | Language simpler than the story | PASS |

**PASS 15 / WATCH 0 / FAIL 0.**

---

## CH-017 — "The Badge Log"

- **Original checksum:** `474e49d581d696a8ee1ff5721efdda42730c4ce707f5f3e7a329fc721c33fc33` (verified against baseline — MATCH)
- **New checksum:** `cbdf83f54d4c7f337862ced13df5cf1403c18b2894ed26a5c2ed38b9bccfe5ef`
- **Word count:** 1840 → 1838 (−2)
- **Sentences reviewed / changed:** 139 / 3

### Change list (classified)

1. **[CLEARER_WORDING]** "Arthur **serviced** it the way you **serviced** anything with a maintenance schedule" → "Arthur **maintained** it the way you **maintained** anything with a maintenance schedule." ("serviced" is an off-register verb choice; "maintained a lie" is natural and keeps the maintenance-schedule metaphor.)
2. **[CLEARER_WORDING]** "before **the absence of it registered**" → "before **he noticed it was missing**." (Abstract-noun construction for a simple idea; the mundane cause of the double badge — the mug — is now literal on first read, which the blueprint's CONTINUITY RISK (1) requires: no ambiguity around the double badge.)
3. **[CLEARER_WORDING]** "A man didn't freeze over a badge log unless **there was something under the freeze**" → "A man didn't freeze over a badge log unless **he was hiding something**." (Decorative phrasing for a simple deduction; Saitō's inference stays explicitly "fragile, ordinary, unprovable" — no truth-layer change.)

### §50 Readability Audit (15 items)

| # | Item | Verdict |
|---|------|---------|
| 1 | Important sentences immediately understandable | PASS |
| 2 | Everyday actions use simple English | PASS |
| 3 | Specialized vocabulary necessary | PASS (reconciliation, audit, manifest, discrepancy, reshelve, annotate — all workplace-necessary; all kept) |
| 4 | Specialized vocabulary contextually understandable | PASS ("ran the log against the shift sheets" glosses "reconciliation") |
| 5 | Difficult words not unnecessarily stacked | PASS |
| 6 | Sentence complexity serves meaning | PASS |
| 7 | Figurative language selective | PASS |
| 8 | Literary language does not dominate | PASS |
| 9 | Mystery remains complex | PASS (no MYSTERY movement; double badge stays mundane; Saitō's cover stays reflexive and unknowing per blueprint) |
| 10 | Atmosphere remains strong | PASS |
| 11 | Character voice intact | PASS (Saitō's dry register, Okada's paperwork register, workplace banter untouched) |
| 12 | Chapter does not feel childish after simplification | PASS |
| 13 | No dictionary needed for basic comprehension | PASS |
| 14 | Beauty through imagery, behavior, implication | PASS |
| 15 | Language simpler than the story | PASS |

**PASS 15 / WATCH 0 / FAIL 0.**

---

## CH-018 — "The Unwritten Rule"

- **Original checksum:** `e6d82bce16d950a9c9839d9683d7753894a684177860a244b2dfa1848a01b4b4` (verified against baseline — MATCH)
- **New checksum:** `dd787f41dd9c33e34b6dfd91fcd3e3f64dfa4ed1e604db874f97eb603f3db0bf`
- **Word count:** 2004 → 2004 (±0)
- **Sentences reviewed / changed:** 135 / 1

### Change list (classified)

1. **[CLEARER_WORDING]** "the spines squared **against the rank**" → "the spines squared **in their rows**." ("rank" = row of shelving is a specialist sense with no in-sentence anchor; surrounding simple language now carries it. Ch-019's "between the shelving ranks" was deliberately NOT changed — see WATCH item W-12 — because "shelving" anchors it there.)

### §50 Readability Audit (15 items)

| # | Item | Verdict |
|---|------|---------|
| 1 | Important sentences immediately understandable | PASS |
| 2 | Everyday actions use simple English | PASS |
| 3 | Specialized vocabulary necessary | PASS (retrieval, reshelve, ledger, intake — all Arthur-register; kept) |
| 4 | Specialized vocabulary contextually understandable | PASS |
| 5 | Difficult words not unnecessarily stacked | PASS |
| 6 | Sentence complexity serves meaning | PASS (long mirror-sequence sentences serve the avoidance rhythm) |
| 7 | Figurative language selective | PASS |
| 8 | Literary language does not dominate | PASS |
| 9 | Mystery remains complex | PASS (Mystery-013: the no-mirrors rule is named but its reason is deliberately unfiled; doctrine, not explanation — untouched) |
| 10 | Atmosphere remains strong | PASS (mirror-unease preserved entirely through behavior: eyes on the brake lever, stairs taken) |
| 11 | Character voice intact | PASS (Saitō's "File it under E. For exercise and eyeballs." untouched) |
| 12 | Chapter does not feel childish after simplification | PASS |
| 13 | No dictionary needed for basic comprehension | PASS |
| 14 | Beauty through imagery, behavior, implication | PASS |
| 15 | Language simpler than the story | PASS |

**PASS 15 / WATCH 0 / FAIL 0.**

---

## CH-019 — "The Photograph"

- **Original checksum:** `937a263fa8ea773e95c0be138d10b19eeb7026fca3a18616e51308bd3e3a3595` (verified against baseline — MATCH)
- **New checksum:** `8a75c6d94ad96c8051c54f1673d1287070aa779501ad1233be8af0c83ca24546`
- **Word count:** 2022 → 2022 (±0)
- **Sentences reviewed / changed:** 146 / 1

### Change list (classified)

1. **[CLEARER_WORDING]** "catching up, three seconds behind **the flesh**" → "catching up, three seconds behind **his body**." ("the flesh" is a literary synonym doing no work the observation doesn't already do; the 3.1s lag observation itself is untouched — same truth layer, same ambiguity.)

No other changes. The chapter's core mystery machinery was deliberately left byte-identical: "exactly where his arm was. Not where his eyes said the shadow was. Where the physics said it was." / "The frame showed a normal, unlagged shadow. His eyes, at the same instant, had seen the lag." / "no instrument the world owned could capture the temporal component" / "The echo was the exception: audio he could record, but only his ears heard it as his shadow's." / ledger line "proof is a dead end." / the final question "If no camera could see it, what did it mean that his eyes could?" Any wording change here would risk shifting OBSERVATION toward INTERPRETATION.

### §50 Readability Audit (15 items)

| # | Item | Verdict |
|---|------|---------|
| 1 | Important sentences immediately understandable | PASS |
| 2 | Everyday actions use simple English | PASS |
| 3 | Specialized vocabulary necessary | PASS ("temporal component" is precise and anchored by "a three-second delay" two sentences earlier; kept per §38 Level 3) |
| 4 | Specialized vocabulary contextually understandable | PASS |
| 5 | Difficult words not unnecessarily stacked | PASS |
| 6 | Sentence complexity serves meaning | PASS |
| 7 | Figurative language selective | PASS |
| 8 | Literary language does not dominate | PASS |
| 9 | Mystery remains complex | PASS (MYSTERY-001 negative evidence: camera shows normal shadow while eyes see lag; the echo exception stays unexplicated; nothing resolved) |
| 10 | Atmosphere remains strong | PASS |
| 11 | Character voice intact | PASS (clerk-register, the convenience store-curb scene with Nadia untouched) |
| 12 | Chapter does not feel childish after simplification | PASS |
| 13 | No dictionary needed for basic comprehension | PASS |
| 14 | Beauty through imagery, behavior, implication | PASS |
| 15 | Language simpler than the story | PASS |

**PASS 15 / WATCH 0 / FAIL 0.**

---

## CH-020 — "Method"

- **Original checksum:** `dc354d833ffe875c403f149bda7bb55aaa2a1de933d0da5d9e984e227d26792f` (verified against baseline — MATCH)
- **New checksum:** `dc354d833ffe875c403f149bda7bb55aaa2a1de933d0da5d9e984e227d26792f` (identical — no edits)
- **Word count:** 2068 → 2068 (±0)
- **Sentences reviewed / changed:** 164 / 0

### Change list

None. The chapter passed the full §8 sentence test as written: every sentence either parses literally on first read or earns its difficulty through meaning (the thesis lines, the method trio, the dream-logic discipline, the unresolved ledger glance, the four open questions). Because ch-020 closes ARC I / P1, and its ending, thesis lines ("Measure. Don't tell. Stay beneath instruments." / "It wasn't a truth. It was a procedure." / "a clerk didn't close a file before the data did"), and the "understanding is the project now" framing are boundary-locked, the conservative call was zero edits rather than risking tone or substance drift. The final gate ("easier to read WITHOUT making the story easier to understand") returns YES: no sentence needed a re-read for wording alone.

### §50 Readability Audit (15 items)

| # | Item | Verdict |
|---|------|---------|
| 1 | Important sentences immediately understandable | PASS |
| 2 | Everyday actions use simple English | PASS |
| 3 | Specialized vocabulary necessary | PASS (cipher, discrepancy code, audit cadence, delta, baseline, instrument floor, Tier 1 — all method-register; the chapter itself translates them into plain words, satisfying §38 anchoring) |
| 4 | Specialized vocabulary contextually understandable | PASS |
| 5 | Difficult words not unnecessarily stacked | PASS |
| 6 | Sentence complexity serves meaning | PASS |
| 7 | Figurative language selective | PASS |
| 8 | Literary language does not dominate | PASS |
| 9 | Mystery remains complex | PASS (dream recurrence filed as dream-logic-not-data, per Arthur's doctrine — unresolved; Saitō's glance over the open ledger left unresolvable by design; four questions stay open) |
| 10 | Atmosphere remains strong | PASS |
| 11 | Character voice intact | PASS |
| 12 | Chapter does not feel childish after simplification | PASS |
| 13 | No dictionary needed for basic comprehension | PASS |
| 14 | Beauty through imagery, behavior, implication | PASS |
| 15 | Language simpler than the story | PASS |

**PASS 15 / WATCH 0 / FAIL 0.**

---

## WATCH ITEMS (deliberate non-changes + reason)

**CH-016**
- **W-1.** "Nothing arriving late, nothing kept back." — kept. Mystery-001-adjacent beat (shadow timing logic); the clipped phrasing mirrors the anomaly's cadence. Simplifying would risk touching the UNKNOWN boundary. (§8 test 3: creates mystery.)
- **W-2.** "The knowing sat in his chest next to the relief, and neither one erased the other." — kept. Abstract noun is deliberate; all words are simple; simplifying would explain feelings (explicitly forbidden: emotional subtext never explained).
- **W-3.** "He could not un-look. He could not un-file." — kept. Neologism pair is character voice and meaning-bearing (the habit is irreversible); single occurrence, not a template.

**CH-017**
- **W-4.** "something older than the knowing got there first" — kept. Marks the instinct-vs-knowledge distinction the chapter's theme (freeze before thought) requires; simple words, context-anchored.
- **W-5.** "The audit closed the way a drawer closed — not slammed, not eased, just closed, because that was what drawers were for." — kept. Single-occurrence rhythm beat; "not X, not Y" pattern is not a repetition here (no other instance in the chapter).
- **W-6.** "The watching went with him" / "The owing went with him" (ch-016/ch-017 parallel) — kept. Deliberate cross-chapter voice echo; varying one side would break the parallel the blueprint's NEXT-CHAPTER DEPENDENCY relies on.

**CH-018**
- **W-7.** "the on-purpose of it was the part he didn't examine" — kept. Unusual nouning is deliberate voice marking his unexamined avoidance; meaning recoverable from the sentence itself ("keep your eyes down on purpose").
- **W-8.** "The fluorescents do my eyes in too." (Saitō dialogue) — kept. Character voice; "do X in" is anchored by the preceding clause ("It's the light down there").

**CH-019**
- **W-9.** "The asymmetry itself would be the violation." — kept. The concept is fully explained by the four preceding sentences (context anchoring per §38); simplifying to "unevenness" would flatten the ethical thesis without aiding comprehension.
- **W-10.** "between the shelving ranks" — kept. Self-anchored ("shelving"), unlike ch-018's unanchored "against the rank" which was simplified (see §14 ROTATE-DO-NOT-REMOVE tension: the term survives where context carries it).

**CH-020**
- **W-11.** "He wasn't braver than he'd been yesterday. He wasn't stronger." — kept. Thesis beat (anti power-fantasy: no level-up); single occurrence; altering it would change tone at the ARC I close.
- **W-12.** The no-mirrors-after-midnight rule block ("The unwritten-ness was the lock… The rule was doctrine, not explanation.") — kept byte-identical. Mystery-013: Arthur's private doctrine, not objective truth; naming without reason is the intended state.
- **W-13.** Saitō's glance over the open ledger ("Or it had found nothing legible. Or it had landed, and Saito had filed it under nothing…") — kept byte-identical. The WATCH on Saito's glance resolution forbids any clarification; the not-knowing is the priced beat.

**No STOP-level canon risks were encountered.** No change made touched plot, events, decisions, motivations, foreshadowing, timelines, endings, truth layers, or the unresolved WATCHes (9/18 overlap, Saito's two-second glance, Mystery-001, Mystery-002, Mystery-013 status).

---

## SUMMARY TABLE

| Chapter | Orig. sha256 (8) | New sha256 (8) | Words before → after | Reviewed / changed | §50 PASS / WATCH / FAIL |
|---------|------------------|----------------|----------------------|--------------------|--------------------------|
| 016 Sunday Dinner, Again | b320eddd | 0295e392 | 1938 → 1937 | 158 / 5 | 15 / 0 / 0 |
| 017 The Badge Log | 474e49d5 | cbdf83f5 | 1840 → 1838 | 139 / 3 | 15 / 0 / 0 |
| 018 The Unwritten Rule | e6d82bce | dd787f41 | 2004 → 2004 | 135 / 1 | 15 / 0 / 0 |
| 019 The Photograph | 937a263f | 8a75c6d9 | 2022 → 2022 | 146 / 1 | 15 / 0 / 0 |
| 020 Method | dc354d83 | dc354d83 | 2068 → 2068 | 164 / 0 | 15 / 0 / 0 |
| **Total** | | | **9876 → 9873** | **742 / 10** | **75 / 0 / 0** |

**Diff verification:** every diff hunk against `~/workspace/world_bible/00_WORLD_BIBLE/CHAPTERS/` is a single-phrase substitution within one sentence. No sentences added or removed, no paragraph restructuring, no scene changes, no ending changes.

**Change taxonomy tally (10 changes):** CLEARER_WORDING ×9, SENTENCE_SIMPLIFICATION ×1, IDIOM_CLARIFICATION ×0, CONTEXTUAL_ANCHOR ×0, AMBIGUITY_REDUCTION ×0, VOCABULARY_ROTATION ×0, PARAGRAPH_FLOW ×0, RHYTHM_CORRECTION ×0. (All changes were word/phrase-level; no sentence- or paragraph-level surgery was needed, which the SOP prefers.)

**Files edited (working copy only):** `~/workspace/world_bible/work_readability/CHAPTERS/016_Sunday_Dinner_Again.md`, `017_The_Badge_Log.md`, `018_The_Unwritten_Rule.md`, `019_The_Photograph.md`, `020_Method.md`. All other files — blueprints, canon, other chapters, indexes — untouched.


---

## SECTION: `AUDIT/_BASEmessaging app_READABILITY.txt`

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/_BASEmessaging app_READABILITY.txt` · sha256 `d92beb2eb97c6f096df2c8dcb18b16eb94789da6a11f33a6a68be25c2a60b0ea` · 87 words. No content changed.

BASEmessaging app CHECKSUMS + WORD COUNTS (2026-09-21, pre-readability-revision)

da9bbe73149796ecf5cf132862e6ce1e8225c8e07498762085ccad082fc7fc3d  001_The_Three-Second_Shadow.md
0df97c62a6adf13c6b1907facbb783e5234bea90f009fc2ed8afa2d62a1b59e6  002_Willowmere.md
9ef9a0af84d10a5e9207215aaeeccd2a88209c3015ee5ff354cb2c425448aefc  003_Sunday_Dinner.md
8590ebb69bbc4036fcb37186a8d1e5e9bfb8fb7163434448711944c81312ecb4  004_The_Measurement.md
cec539607885173b0996d25a8d3471821793aca72439c8a4584aac9363d76d99  005_Saitos_Test.md
a9e52601444f87687c48fdb00e1f211375674e2246bffee40395a3c108f92755  006_Dark_Water.md
8b35cb979d93d8683fb44c2350be0052a9b694833c875cc93118171e452958b9  007_No_Category.md
bc9a9d67e284464693021f32d3042aa16308a17146cb477125092b2149508740  008_Melon_Pan.md
58576e91e8b40e28c6fde593f133538f62fd2045640d55b7c67510b081da06e3  009_Impossible_Constancy.md
9eaf1b83e71d17b203eebcd4c418e073bde41b0f226208ebf8e14d2290bb42ef  010_The_Cordon.md
9307b5bcdd2945b208e8ad99a5e95d2c5674733574f049f9d0d2f70f6fc9a2e8  011_Aftershock.md
8ab94dd69e06b69ef22b0669e378706bf9bf27a013975c3e3fdba043febced34  012_The_Private_Ledger.md
dfde77b23a4c267dc01fa898308ea366f90feb71f7606040e18c75545ef77156  013_The_Night_Keeps.md
69319707c76d2550ab6644b280676616d6af0fc290966d0bc11507ea137bc34b  014_Three_Point_One.md
7b3dd0fa536329c52b5d58874ae3d6fc416e5ccd2cfc24114aa4cc872898bda4  015_Rent_Day_Arithmetic.md
b320edddd3477af422958848f43309c2cc29946daea5749bcc9d8d1ae800ab0e  016_Sunday_Dinner_Again.md
474e49d581d696a8ee1ff5721efdda42730c4ce707f5f3e7a329fc721c33fc33  017_The_Badge_Log.md
e6d82bce16d950a9c9839d9683d7753894a684177860a244b2dfa1848a01b4b4  018_The_Unwritten_Rule.md
937a263fa8ea773e95c0be138d10b19eeb7026fca3a18616e51308bd3e3a3595  019_The_Photograph.md
dc354d833ffe875c403f149bda7bb55aaa2a1de933d0da5d9e984e227d26792f  020_Method.md
2516 001_The_Three-Second_Shadow.md
2391 002_Willowmere.md
2273 003_Sunday_Dinner.md
1988 004_The_Measurement.md
2257 005_Saitos_Test.md
2037 006_Dark_Water.md
2497 007_No_Category.md
2249 008_Melon_Pan.md
2033 009_Impossible_Constancy.md
2042 010_The_Cordon.md
2480 011_Aftershock.md
2491 012_The_Private_Ledger.md
1984 013_The_Night_Keeps.md
2711 014_Three_Point_One.md
2496 015_Rent_Day_Arithmetic.md
1938 016_Sunday_Dinner_Again.md
1840 017_The_Badge_Log.md
2006 018_The_Unwritten_Rule.md
2024 019_The_Photograph.md
2068 020_Method.md


---

## SECTION: `AUDIT/READABILITY_DIFFS/001_The_Three-Second_Shadow.diff` (unified diff — merged as fenced code)

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/READABILITY_DIFFS/001_The_Three-Second_Shadow.diff` · sha256 `f0e2d6301714a981291f885fe3ccbe7bb90dd515a1c98711b2e9136040b6231e` · 193 words.

```diff
--- 00_WORLD_BIBLE/CHAPTERS/001_The_Three-Second_Shadow.md	2026-09-20 23:24:45.319018809 +0000
+++ work_readability/CHAPTERS/001_The_Three-Second_Shadow.md	2026-09-20 23:35:39.375374236 +0000
@@ -12,7 +12,7 @@
 
 "Understood," he said, and took the tray past Saito's desk.
 
-Saito was late — twenty seconds, according to the wall clock Arthur didn't mean to check. He came down the stairs two at a time with his shirt half untucked, nodded once at Arthur, and sat. Their workstations faced each other across a gap of about a meter, close enough that Arthur could see the reflection of Saito's monitor in his glasses and Saito could see his. Two years of night shifts had taught them both to keep their voices low and their opinions lower.
+Saito was late — twenty seconds, according to the wall clock Arthur didn't mean to check. He came down the stairs two at a time with his shirt half untucked, nodded once at Arthur, and sat. Their workstations faced each other across a gap of about a meter — close enough that each could see the other's monitor reflected in the other's glasses. Two years of night shifts had taught them both to keep their voices low and their opinions lower.
 
 "Evening," Saito said.
 
```


---

## SECTION: `AUDIT/READABILITY_DIFFS/002_Willowmere.diff` (unified diff — merged as fenced code)

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/READABILITY_DIFFS/002_Willowmere.diff` · sha256 `e48c8daf1c93816948836947d699bac919504eaf55a9e62f69e93f1061fbfa76` · 296 words.

```diff
--- 00_WORLD_BIBLE/CHAPTERS/002_Willowmere.md	2026-09-20 23:24:45.319160933 +0000
+++ work_readability/CHAPTERS/002_Willowmere.md	2026-09-20 23:35:39.376962059 +0000
@@ -12,7 +12,7 @@
 
 Shower first. The unit bath was exactly one person wide if that person did not inhale too much. He stood under the water until his face felt like a face again, brushed his teeth one-handed, and held the showerhead with the other like a man operating machinery, because that is what it was. The dark circles did not move. They never moved.
 
-Windbreaker off the hook, jeans from the floor, glasses cleaned on his shirt, the free-ish frames from the two-for-one campaign sitting a little crooked on his nose. He straightened them by feel and did not check himself in the shoebox door before leaving; checking had never once improved a day.
+Windbreaker off the hook, jeans from the floor, glasses cleaned on his shirt, the free-ish frames from the two-for-one campaign sitting a little crooked on his nose. He straightened them by feel and did not check his reflection in the shoebox door before leaving; checking had never once improved a day.
 
 The laundry bag was by the door, pre-packed last night in the thirty seconds between coming home and falling asleep. He had learned that if he did not pack it before sleep, Saturday Arthur would negotiate with Friday Arthur, and Friday Arthur always lost. One load. Three hundred yen. A week of night shifts produced exactly one laundry bag's worth of a person, measured precisely: two sets of work clothes rotated across five nights, one convenience store-break hoodie, gym-wear-quality socks, the towel from the unit bath. Three hundred yen washed all of it. He had never once needed the big machine. Not frugality: calibration. He was proud of it the way a clerk is proud of a ledger that balances.
 
```


---

## SECTION: `AUDIT/READABILITY_DIFFS/003_Sunday_Dinner.diff` (unified diff — merged as fenced code)

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/READABILITY_DIFFS/003_Sunday_Dinner.diff` · sha256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` · 0 words.

> _(The source diff file was empty — this chapter had zero changes in that revision pass.)_


---

## SECTION: `AUDIT/READABILITY_DIFFS/004_The_Measurement.diff` (unified diff — merged as fenced code)

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/READABILITY_DIFFS/004_The_Measurement.diff` · sha256 `8f3be50adbe8ce0ea5654ad456aa7785f8ef5ec97ca03c533444b9c7abc2368c` · 204 words.

```diff
--- 00_WORLD_BIBLE/CHAPTERS/004_The_Measurement.md	2026-09-20 23:24:45.319430257 +0000
+++ work_readability/CHAPTERS/004_The_Measurement.md	2026-09-20 23:35:39.378374236 +0000
@@ -70,7 +70,7 @@
 
 The reason was embarrassingly simple: the honest explanation had a flaw, and Arthur's mind, left unoccupied between two filing runs, found the flaw the way a hand finds a crack in a shelf.
 
-Fatigue produced afterimages. Fine. But afterimages were symmetrical things — they belonged to the eye, not the wall. If his eyes were tired, the lag should follow him everywhere: the records hall, the break room, the train home. It didn't. It happened in the corridor. Twice now. Both times under the same fluorescents, the same clock.
+Fatigue produced afterimages. Fine. But afterimages belonged to the eye, not the wall. If his eyes were tired, the lag should follow him everywhere: the records hall, the break room, the train home. It didn't. It happened in the corridor. Twice now. Both times under the same fluorescents, the same clock.
 
 That didn't disprove fatigue. Location-correlated fatigue was not a thing, but habit-correlated attention was — maybe he only *noticed* in the corridor because the corridor was where he'd first noticed. The eye went where the eye had learned to go. That was also documented, which meant it was also deniable.
 
```


---

## SECTION: `AUDIT/READABILITY_DIFFS/005_Saitos_Test.diff` (unified diff — merged as fenced code)

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/READABILITY_DIFFS/005_Saitos_Test.diff` · sha256 `fac5a2cf9ae51c4222c9533201e4edafd4aaf8ea05dcc45353d689a2dfc0a0b0` · 92 words.

```diff
--- 00_WORLD_BIBLE/CHAPTERS/005_Saitos_Test.md	2026-09-20 23:24:45.319609686 +0000
+++ work_readability/CHAPTERS/005_Saitos_Test.md	2026-09-20 23:35:39.375374236 +0000
@@ -82,7 +82,7 @@
 
 He put the phone in his pocket to prove it.
 
-Saito's hand stayed out for one more second, the grin stayed on for one more second, and then both of them retired, and Saito said, "Facilities asked *you*."
+Saito's hand stayed out for one more second, the grin stayed on for one more second, and then both dropped, and Saito said, "Facilities asked *you*."
 
 "They asked the night shift. I was the night shift who was standing up."
 
```


---

## SECTION: `AUDIT/READABILITY_DIFFS/006_Dark_Water.diff` (unified diff — merged as fenced code)

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/READABILITY_DIFFS/006_Dark_Water.diff` · sha256 `553bd37a3c09a28f2d04a4ad562aa5e453bd925621fee9dcf2fe7fcf9800a215` · 803 words.

```diff
--- 00_WORLD_BIBLE/CHAPTERS/006_Dark_Water.md	2026-09-20 23:24:45.319799831 +0000
+++ work_readability/CHAPTERS/006_Dark_Water.md	2026-09-20 23:34:58.221372639 +0000
@@ -24,11 +24,11 @@
 
 Exhibit one: the lie, sitting in Saito's head, false, to be maintained. *Filming for facilities.* Saito had believed it instantly, because Saito looked at things until they gave up and he had decided, in his own low-volume way, that there was nothing to look at.
 
-Exhibit two: the question. He picked up his phone off the low table — 12:04 now, the alarm still armed and smug for 15:00, never having fired — and opened the notes app, not the dream, just the *facilities flicker log*, the cover heading doing its cover work. Two entries. Below them, unwritten, the question that had been waiting under everything since Monday night's slow-motion test: what kept it at exactly three. He had the number twice. It was the only certain thing in the file, and it had no filing code anywhere in the archive — two years inside it, and he knew what it catalogued and what it didn't.
+Exhibit two: the question. He picked up his phone off the low table — 12:04 now, the alarm still armed and smug for 15:00, never having fired — and opened the notes app. Not the dream: just the *facilities flicker log*, the cover heading doing its cover work. Two entries. Below them, unwritten, the question that had been waiting under everything since Monday night's slow-motion test: what kept it at exactly three. He had the number twice. It was the only certain thing in the file, and it had no filing code anywhere in the archive — two years inside it, and he knew what it catalogued and what it didn't.
 
 Exhibit three: the ordinary arithmetic of a body run on five hours of sleep. The fatigue never lifted; it accumulated, the way it always did.
 
-So: stress. The verdict felt honest, which was the point of verdicts. Arthur got up, folded the futon with hospital corners because folding it properly was free, and went about the afternoon the way you got through an afternoon that had started three hours early — by performing normalcy until it became real.
+So: stress. The verdict felt honest, which was the point of verdicts. Arthur got up, folded the futon with hospital corners because folding it properly was free, and went about the afternoon the way you got through an afternoon that had started three hours early — by acting normal until it became real.
 
 The convenience store was the same convenience store. At noon the lights were just lights, not a promise; the clerk was the day-shift clerk, who didn't do the tribe nod. Arthur bought lunch with the ¥600 he always spent at midday — a rice ball, a can of hot coffee, a small sweet bread he would regret by evening and eat anyway. He ate at the curbside spot out of habit, watching a delivery truck idle at the intersection, the canned coffee warming his hands through the paper sleeve. Nobody else's dream was anybody's business. It was September and the air had the end-of-summer weight to it, damp and tired. Ordinary. This was the secondary function of lunch: to prove, via receipts, that the day was continuing.
 
@@ -36,7 +36,7 @@
 
 At 14:00 he did the walk.
 
-The port road was the one hobby that cost nothing, and Arthur had defended it the way he defended the ¥600 lunch: as non-negotiable budget line in the ledger of being alive. He took the bicycle, then decided against the bicycle — the afternoon was too still for the bicycle — and walked, out past the shrine and the shuttered print shop, down toward the harbor district where the claims in the archive came from and where the air changed its mind. September on the port road smelled like salt and diesel and water on concrete, the daytime register of everything the night shift only got the cooled-down version of. Gulls did their accounting overhead. A trawler's horn went off somewhere out of sight, flat and certain.
+The port road was the one hobby that cost nothing, and Arthur had defended it the way he defended the ¥600 lunch: as a non-negotiable budget line in the ledger of being alive. He took the bicycle, then decided against the bicycle — the afternoon was too still for the bicycle — and walked, out past the shrine and the shuttered print shop, down toward the harbor district where the claims in the archive came from and where the air changed its mind. September on the port road smelled like salt and diesel and water on concrete, the daytime version of everything the night shift only knew cooled-down. Gulls did their accounting overhead. A trawler's horn went off somewhere out of sight, flat and certain.
 
 The water read wrong.
 
```


---

## SECTION: `AUDIT/READABILITY_DIFFS/007_No_Category.diff` (unified diff — merged as fenced code)

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/READABILITY_DIFFS/007_No_Category.diff` · sha256 `0d9cda3f0d8d1525361ccc6742b5b170d813fe4b8192c7e8d90a7740413c67f7` · 527 words.

```diff
--- 00_WORLD_BIBLE/CHAPTERS/007_No_Category.md	2026-09-20 23:24:45.319913222 +0000
+++ work_readability/CHAPTERS/007_No_Category.md	2026-09-20 23:35:17.449373385 +0000
@@ -50,7 +50,7 @@
 
 He started with what was reachable from his own chair.
 
-The branch claims index went back six years, searchable from the records terminal — every claim the branch had filed, every claimant's description typed in, every category assigned by the adjusters. It was the institution's memory of the strange, insofar as the strange ever reached the institution. That qualifier mattered. He read the coverage before he read the null.
+The branch claims index went back six years, searchable from the records terminal — every claim the branch had filed, every claimant's description typed in, every category assigned by the adjusters. It was the institution's memory of the strange, as far as the strange ever reached the institution. That qualifier mattered. He read the coverage before he read the null.
 
 He ran the searches methodically, no theater.
 
@@ -78,7 +78,7 @@
 
 The question had been asked already, on Monday and Tuesday nights, measured twice at 3.0 seconds. Tonight was the paper's turn to answer. The tape on the door had yellowed to the color of old teeth. He went in under the handwriting that said *old — touch nothing unless chief says*, because the chief had said.
 
-The Jakarta boxes filled the back room's third row: forty years of the branch's closed files — claims routed through the Jakarta office over the decades, boxed when the old building's paper had outgrown its shelves. Forty years. The manifests were typed on index stock in three different handwritings across the decades, the box labels in felt pen gone brown at the edges. He worked shelf by shelf, pulling manifests, reading finding aids, checking the labels' own marginalia — the little notes archivists left for each other: *water damage, see box 12*; *1996 — reboxed after leak*; *do not reshelve without manifest update*.
+The Jakarta boxes filled the back room's third row: forty years of the branch's closed files — claims routed through the Jakarta office over the decades, boxed when the old building's paper had outgrown its shelves. Forty years. The manifests were typed on index stock in three different handwritings across the decades, the box labels in felt pen gone brown at the edges. He worked shelf by shelf, pulling manifests and reading finding aids. Then he checked the labels' own marginalia — the little notes archivists left for each other: *water damage, see box 12*; *1996 — reboxed after leak*; *do not reshelve without manifest update*.
 
 Forty years of the strange, if the strange had ever been filed. He read for the same terms, translated into adjuster vocabulary this time: shadow, lag, lighting anomalies, anything a claimant in 1987 might have called *the light moved wrong*. The manifests spoke a poorer language than he did — *claimant reports damage while premises unoccupied*, *timeline unclear*, *settled* — but poorer languages could still hold a word he needed. He checked the misfiled drawer, the one every archive had, the box of boxes that had missed their decade. He re-ran the whole row with variant phrasings, because one search was a guess and two were a verification.
 
```


---

## SECTION: `AUDIT/READABILITY_DIFFS/008_Melon_Pan.diff` (unified diff — merged as fenced code)

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/READABILITY_DIFFS/008_Melon_Pan.diff` · sha256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` · 0 words.

> _(The source diff file was empty — this chapter had zero changes in that revision pass.)_


---

## SECTION: `AUDIT/READABILITY_DIFFS/009_Impossible_Constancy.diff` (unified diff — merged as fenced code)

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/READABILITY_DIFFS/009_Impossible_Constancy.diff` · sha256 `e5a6e16a1df1805bc4b78fdd37a3f36e1ffc295f28d3e4556bf359e28147f10b` · 404 words.

```diff
--- 00_WORLD_BIBLE/CHAPTERS/009_Impossible_Constancy.md	2026-09-20 23:24:45.320243427 +0000
+++ work_readability/CHAPTERS/009_Impossible_Constancy.md	2026-09-20 23:35:48.813374602 +0000
@@ -1,6 +1,6 @@
 # CHAPTER 009 — "Impossible Constancy"
 
-The alarm went off at 15:00 and he woke at 15:04, which for him counted as punctual, and the first thing he registered — before the room's flat gray gloom, before the wood of the building ticking as it cooled — was that he was rested. Properly rested. The kind of rested that made him briefly suspicious of it, the way you eyed a ledger that balanced on the first try.
+The alarm went off at 15:00 and he woke at 15:04, which for him counted as punctual. The first thing he registered was that he was rested — before the room's flat gray gloom, before the wood of the building ticking as it cooled. Properly rested. The kind of rested that made him briefly suspicious of it, the way you eyed a ledger that balanced on the first try.
 
 Saturday. Off-shift. The pre-packed laundry bag was by the door and the coin case was in its place. He had a plan for the day. It had been sitting in his head since Monday night's measurement, and it had survived the whole week — the dream he'd filed as stress, the archive's two hours of nothing, the dawn at the convenience store with Nadia — without getting smaller. That usually meant it was either a good plan or a debt. Plans and debts felt the same from the inside. The difference was what they cost.
 
@@ -48,7 +48,7 @@
 
 Take two was aborted by a salaryman reaching past him for the natto, his shadow crossing the frame like a third party joining a meeting uninvited. Fieldwork had occupational hazards. He nodded at him, he nodded back, and they conducted the entire exchange at the volume of two men who had agreed the convenience store was a library.
 
-Take three was clean. He paid for the coffee — point card, no, thank you, the register of people who had done this ten thousand times — and counted frames on the bench outside with the coffee going warm in his hand.
+Take three was clean. He paid for the coffee — point card, no, thank you, in the tone of people who had done this ten thousand times — and counted frames on the bench outside with the coffee going warm in his hand.
 
 Seven hundred and twenty.
 
```


---

## SECTION: `AUDIT/READABILITY_DIFFS/010_The_Cordon.diff` (unified diff — merged as fenced code)

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/READABILITY_DIFFS/010_The_Cordon.diff` · sha256 `8eadac78be01565dfe20ea9c6168a87fe6f29f38a3137e62a351f25682a14160` · 287 words.

```diff
--- 00_WORLD_BIBLE/CHAPTERS/010_The_Cordon.md	2026-09-20 23:24:45.320360413 +0000
+++ work_readability/CHAPTERS/010_The_Cordon.md	2026-09-20 23:36:04.160375198 +0000
@@ -56,7 +56,7 @@
 
 The plain side bothered him the way an unbalanced figure bothered a clerk, and before the bother had a name he was doing something he hadn't done since his first year on the job.
 
-Back then he'd noticed something small about the second shadow, by accident — it didn't only lag behind him. A moth had crossed the corridor tube once and the moth's flutter had stayed in the shadow a beat after the moth was gone, and he'd understood he could look at the shadow and see again what he'd just seen; he'd tested it on purpose exactly once, the next night — tipped a box slip off the cart and watched the slip's fall kept in the shadow after the slip had settled — then filed it away as a curiosity. He hadn't needed it since.
+Back then he'd noticed something small about the second shadow, by accident — it didn't only lag behind him. A moth had crossed the corridor tube once, and the moth's flutter had stayed in the shadow a beat after the moth was gone. He'd understood then that he could look at the shadow and see again what he'd just seen. He'd tested it on purpose exactly once, the next night — tipped a box slip off the cart and watched the slip's fall kept in the shadow after the slip had settled — then filed it away as a curiosity. He hadn't needed it since.
 
 He needed it now. Saturday had killed the last ordinary explanation — not optics, real enough to trust — and trust, in his filing system, was something you acted on.
 
```


---

## SECTION: `AUDIT/READABILITY_DIFFS/011_Aftershock.diff` (unified diff — merged as fenced code)

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/READABILITY_DIFFS/011_Aftershock.diff` · sha256 `82fffd41a2ffe92a40bcb827e422f2217f2f168eae7a626b15ab3a52da5c79a6` · 1,113 words.

```diff
--- 00_WORLD_BIBLE/CHAPTERS/011_Aftershock.md	2026-09-20 23:24:45.320475485 +0000
+++ work_readability/CHAPTERS/011_Aftershock.md	2026-09-20 23:35:49.374374624 +0000
@@ -4,7 +4,7 @@
 
 The blackout curtains held the afternoon at bay, the room at the even gray of a television left on mute, and when the alarm went off at 19:40 he woke the way a man wakes on an ordinary day — a little stiff, a little slow, standing too long in the shower until the hot water made his ears ring. The empty plant pot sat on the desk. The protective charm from his mother was where it always was. Nothing in the apartment had moved overnight, and that was the point. He checked the clock twice, the way he always did, and ate rice ball from the fridge, and left his one-room apartment in Willowmere at 21:02, exactly on time, exactly as usual.
 
-That was the first lie of the shift. Not that he did anything wrong. Just that the doing it, on time, the same as always, required him to decide to do it, and deciding made it a performance. He had slept fine. He had woken fine. The ordinariness had needed his help.
+That was the first lie of the shift. Not that he did anything wrong. Just that doing it, on time, the same as always, meant deciding to do it, and deciding made it a performance. He had slept fine. He had woken fine. The ordinariness had needed his help.
 
 The train ran on time. The platform smelled like rain that had already given up. He straightened his glasses by feel, and the key-ring zipper pull on his windbreaker clicked once against the handrail. It was Tuesday. Tuesday night into Wednesday morning. His shift was 22:00 to 06:00, and there was nothing to be afraid of inside it.
 
@@ -20,7 +20,7 @@
 
 At 00:14 he caught himself counting the seconds between the tube's flickers, and stopped, and went back to the cart. He had decided this already — yesterday, or the night before; time had gone soft around the edges, and he refused to examine it. He had decided: tell no one. Not Saito. Not the chief. Nobody. He'd gone through the reasons once, in the records room with the door shut, the way a man pays a bill in full rather than letting it run.
 
-He was paying it again now. The decision did not want to stay made. That was the work nobody had warned him about. It wasn't that keeping quiet was hard; it was that it kept un-keeping itself, in little installments, at the most ordinary moments — reaching for a folder, waiting for the elevator, watching the second hand sweep. He would find himself mid-thought, mid-sentence to no one, explaining. And then he would stop.
+He was paying it again now. The decision did not want to stay made. That was the work nobody had warned him about. It wasn't that keeping quiet was hard; it was that it kept coming undone, in little installments, at the most ordinary moments — reaching for a folder, waiting for the elevator, watching the second hand sweep. He would find himself mid-thought, mid-sentence to no one, explaining. And then he would stop.
 
 *Telling would make a file.*
 
@@ -66,7 +66,7 @@
 
 "Because it's Tuesday," Saito said, "and the tradecraft being terrible is the entertainment." He shelved the folder and reached for the next. "You look tired, by the way."
 
-It landed flat, between them. Arthur felt his hands continue their work — take, check, slide, square — as if supervised by someone else.
+It fell flat, between them. Arthur felt his hands continue their work — take, check, slide, square — as if supervised by someone else.
 
 "Didn't sleep great," he said. It wasn't true. He'd slept fine. The lie was small and instant and he hated it immediately, and he kept it, because the alternative was a longer lie or the truth, and both of those were files.
 
@@ -88,11 +88,11 @@
 
 The nothing was doing its job too well. It kept needing him to notice it.
 
-At 02:55 he stood up from the terminal, stretched until his back cracked, and volunteered for the 03:00 cart run — a thing he could not quite have justified to himself, except as diligence.
+At 02:55 he stood up from the terminal, stretched until his back cracked, and volunteered for the 03:00 cart run — he couldn't quite justify it to himself, except as diligence.
 
 The cart run to B3 — the old files, the deep archive, the run that filled the middle of the night with something to push and something to do — rotated informally, and tonight it fell to nobody in particular. Usually nobody felt like it until the carts backed up. Arthur felt like it. He loaded the cart, tallied it, wheeled it to the service elevator, and rode down to B3 with the cage's old chains rattling.
 
-B3 was colder. It always was. The old files lived here, boxes with hand-written labels from a decade of gone clerks, the air smelling of dust, cardboard, and the elevator's faint oil. He pushed the cart down the aisle between the tall ranks, shelving returns box by box, and the work was heavier and slower and demanded his hands in a way B2's rhythm didn't. That was why he'd volunteered. Hands busy. Mind — not empty, but narrowed. The replay still ran, but it ran quieter when his shoulders were working.
+B3 was colder. It always was. The old files lived here, boxes with hand-written labels from a decade of clerks long since gone, the air smelling of dust, cardboard, and the elevator's faint oil. He pushed the cart down the aisle between the tall ranks, shelving returns box by box, and the work was heavier and slower and demanded his hands in a way B2's rhythm didn't. That was why he'd volunteered. Hands busy. Mind — not empty, but narrowed. The replay still ran, but it ran quieter when his shoulders were working.
 
 Brine. Three streets from the water. He shelved a box labeled 2017–Q2 and moved on. The smell had been wrong for the distance. He knew that street. Everyone who'd lived in Ravenscroft knew that street. He shelved another box.
 
@@ -124,6 +124,6 @@
 
 Telling would make a file. So he would not tell.
 
-He would hold it. He had decided, and the decision would keep un-making itself, and he would keep making it again. That was the work now.
+He would hold it. He had decided, and the decision would keep coming undone, and he would keep making it again. That was the work now.
 
 He got on the train home.
```


---

## SECTION: `AUDIT/READABILITY_DIFFS/012_The_Private_Ledger.diff` (unified diff — merged as fenced code)

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/READABILITY_DIFFS/012_The_Private_Ledger.diff` · sha256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` · 0 words.

> _(The source diff file was empty — this chapter had zero changes in that revision pass.)_


---

## SECTION: `AUDIT/READABILITY_DIFFS/013_The_Night_Keeps.diff` (unified diff — merged as fenced code)

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/READABILITY_DIFFS/013_The_Night_Keeps.diff` · sha256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` · 0 words.

> _(The source diff file was empty — this chapter had zero changes in that revision pass.)_


---

## SECTION: `AUDIT/READABILITY_DIFFS/014_Three_Point_One.diff` (unified diff — merged as fenced code)

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/READABILITY_DIFFS/014_Three_Point_One.diff` · sha256 `2242cfa06ec83e8c62533f58fd3c6e32793fdc6ff73c06847a3bc95a2c835354` · 191 words.

```diff
--- 00_WORLD_BIBLE/CHAPTERS/014_Three_Point_One.md	2026-09-20 23:24:45.320921104 +0000
+++ work_readability/CHAPTERS/014_Three_Point_One.md	2026-09-20 23:35:50.384374663 +0000
@@ -118,7 +118,7 @@
 
 A breath past. He could have rounded down. He'd rounded down his whole life — that was what rounding was for. The clerk's margin wasn't in the instrument this time. The instrument was his eyes, and his eyes said the hand had gone past three by the width of its own red line.
 
-He did it a third time on the landing, because one measurement could lie. The hand stood past three. Past. He stopped counting how much past and just stood there in the dark with his arm at his side, watching the red hand go around and around, taking three seconds longer than it should have to mean anything to him.
+He did it a third time on the landing, because one measurement could lie. The hand stood past three. Past. He stopped counting how much past and just stood there in the dark with his arm at his side, watching the red hand go around and around, and the shadow coming in past three, every time — and that was what it meant.
 
 ---
 
```


---

## SECTION: `AUDIT/READABILITY_DIFFS/015_Rent_Day_Arithmetic.diff` (unified diff — merged as fenced code)

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/READABILITY_DIFFS/015_Rent_Day_Arithmetic.diff` · sha256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` · 0 words.

> _(The source diff file was empty — this chapter had zero changes in that revision pass.)_


---

## SECTION: `AUDIT/READABILITY_DIFFS/016_Sunday_Dinner_Again.diff` (unified diff — merged as fenced code)

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/READABILITY_DIFFS/016_Sunday_Dinner_Again.diff` · sha256 `c292bdcce1a384266375568a31d0582b31ab1f3941411f03adfbf77848bebae3` · 863 words.

```diff
--- 00_WORLD_BIBLE/CHAPTERS/016_Sunday_Dinner_Again.md	2026-09-20 23:24:45.321241615 +0000
+++ work_readability/CHAPTERS/016_Sunday_Dinner_Again.md	2026-09-20 23:35:22.500373581 +0000
@@ -18,7 +18,7 @@
 
 Nobody saw. His mother was already taking the bag ("You brought it. The good one. Good."), and Nanami was already talking from the hallway ("He brought detergent, the romance of this family is officially dead"), and the news was going in the living room, and the glance was over, filed, and the shame arrived right behind it like the second half of a sentence he hadn't meant to start.
 
-He had checked his family's shadows. The way he checked the corridor tube. The way he'd checked Saito's face on Tuesday, and the wall clock, and the far-end fluorescents. He had stood in his parents' doorway and run the check over the people he loved, and the check had found nothing, and he was relieved — and the relief was the worst of it, worse than the checking, because the relief meant some part of him had been braced for a different answer.
+He had checked his family's shadows. The way he checked the corridor tube. The way he'd checked Saito's face on Tuesday, and the wall clock, and the far-end fluorescents. He had stood in his parents' doorway and run the check over the people he loved, and the check had found nothing, and he was relieved — and the relief was the worst of it, worse than the checking, because the relief meant some part of him had been expecting a worse answer.
 
 He didn't know why he'd done it. He only knew he hadn't decided to, and that he hated it. The knowing sat in his chest next to the relief, and neither one erased the other.
 
@@ -48,7 +48,7 @@
 
 "Noted," Arthur said, sitting down. "I'll inform the roof."
 
-His father grunted approvingly and went back to the graphic, and Arthur settled into the comfortable noise of it — the news as weather, his father's commentary as commentary on the weather, none of it requiring anything from him beyond the occasional noise of assent. The every-other-Sunday machinery, running on time. The second one. They were a series now.
+His father grunted approvingly and went back to the graphic, and Arthur settled into the comfortable noise of it — the news as weather, his father's commentary as commentary on the weather, none of it requiring anything from him beyond the occasional murmur of agreement. The every-other-Sunday machinery, running on time. The second one. They were a series now.
 
 Dinner was nikujaga — plenty, his mother's word, the pot still on the stove like it was feeding six — and rice, extra, and miso soup, and the pickles she was visibly proud of. They ate. For a while there was only chopsticks and the television gone soft, and Arthur felt the evening doing what these evenings did: loosening something in his chest he hadn't known was tight.
 
@@ -96,9 +96,9 @@
 
 "He's married to the streak," Nanami said. "Four years, two months. I saw the crown sticker. It's serious."
 
-Takashi cleared his throat, in the tone of a man delivering considered counsel: "No pressure, son."
+Takashi cleared his throat, in the tone of a man giving serious advice: "No pressure, son."
 
-"I'm only asking," Yuko said, and got up for more rice, and the inquest was over, the way it always was — light, a beat, nobody's feelings in it. Arthur felt the familiar small gratitude for that: the question asked, the answer accepted, the machinery moving on.
+"I'm only asking," Yuko said, and got up for more rice, and the questioning was over, the way it always was — light, a beat, nobody's feelings in it. Arthur felt the familiar small gratitude for that: the question asked, the answer accepted, the machinery moving on.
 
 Nobody asked about the archive. Nobody ever did. The peace was the point of these Sundays, and he knew his part in it.
 
@@ -110,7 +110,7 @@
 
 He hadn't decided any of it. That was the worst of it, and the truest: the watching had become the way he looked at everything, including the people he would never, ever put in a file — and there they were, in the file, because he couldn't look at them any other way anymore.
 
-He could not un-look. He could not un-file. There was no absolution in the drawer either — he'd checked, the way a clerk checks. There was only this: keep coming. Keep the peace load-bearing. Keep not telling. For the second dinner running, that was the choice, and it would be the choice next time, and the time after, for as long as the Sundays came.
+He could not un-look. He could not un-file. There was no forgiveness in the drawer either — he'd checked, the way a clerk checks. There was only this: keep coming. Keep the peace load-bearing. Keep not telling. For the second dinner running, that was the choice, and it would be the choice next time, and the time after, for as long as the Sundays came.
 
 The cost of presence had a new line item. He added it up the way he added up everything, and kept eating.
 
```


---

## SECTION: `AUDIT/READABILITY_DIFFS/017_The_Badge_Log.diff` (unified diff — merged as fenced code)

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/READABILITY_DIFFS/017_The_Badge_Log.diff` · sha256 `7be622182a5973afae5f2ec2e3fb7acfb94b156e544b6421a90df6a104d9ebda` · 673 words.

```diff
--- 00_WORLD_BIBLE/CHAPTERS/017_The_Badge_Log.md	2026-09-20 23:24:45.321340433 +0000
+++ work_readability/CHAPTERS/017_The_Badge_Log.md	2026-09-20 23:35:23.537373621 +0000
@@ -22,7 +22,7 @@
 
 "There's only one list." Saito put the headphones on, which was Saito for *conversation filed*.
 
-The lie sat between them, filed and false, the way it had sat for almost two weeks. *Arthur filmed the flicker for facilities.* Saito believed it the way Saito believed anything boring: completely, and without further interest. Arthur serviced it the way you serviced anything with a maintenance schedule — a sentence when asked, no volunteering — and the guilt went with him into the cart the way it always did — familiar by now, and carried anyway.
+The lie sat between them, filed and false, the way it had sat for almost two weeks. *Arthur filmed the flicker for facilities.* Saito believed it the way Saito believed anything boring: completely, and without further interest. Arthur maintained it the way you maintained anything with a maintenance schedule — a sentence when asked, no volunteering — and the guilt went with him into the cart the way it always did — familiar by now, and carried anyway.
 
 He worked. Cross-reference, scan, file. A fender bender in Nakamachi, photographed from four angles by a man who clearly didn't trust the other three. A warehouse inventory discrepancy — carton count off by four on a Thursday shipment, the adjuster noting *likely miscount at origin* in the handwriting of a man who had written that sentence before. The cart came down one claim at a time, and the rhythm of it was the best part of the job, the part that had carried him through two years of nights.
 
@@ -50,7 +50,7 @@
 
 He looked at the line. Two entries. His name. 03:40, twice.
 
-The answer was ready before the question had finished landing. Thursday's run. He'd carried the mug down — set it on the cart brake at the B3 landing while he worked the aisle, gone in, gotten ten steps down the low-light aisle before the absence of it registered, come back out, picked it up, badged in again. The mug's fault. The whole of it, ordinary down to the chip in the handle.
+The answer was ready before the question had finished landing. Thursday's run. He'd carried the mug down — set it on the cart brake at the B3 landing while he worked the aisle, gone in, gotten ten steps down the low-light aisle before he noticed it was missing, come back out, picked it up, badged in again. The mug's fault. The whole of it, ordinary down to the chip in the handle.
 
 He opened his mouth.
 
@@ -78,7 +78,7 @@
 
 Saito put the headphone back on. He didn't look at Arthur. He didn't ask.
 
-That was the thing Arthur carried back to his station with him, heavier than the cart had been: Saito had seen the half-second. A man didn't freeze over a badge log unless there was something under the freeze, and Saito had done that arithmetic the way anyone would — fragile, ordinary, unprovable — and he had lied anyway. Without being asked. Without knowing what for.
+That was the thing Arthur carried back to his station with him, heavier than the cart had been: Saito had seen the half-second. A man didn't freeze over a badge log unless he was hiding something, and Saito had done that arithmetic the way anyone would — fragile, ordinary, unprovable — and he had lied anyway. Without being asked. Without knowing what for.
 
 He'd almost said thanks, on the walk back. The word had been right there, warm and ready and completely wrong. Thanks would have been a receipt. Receipts were for things that closed. This wasn't closed. This was the opposite of closed — it was a thing that would sit open between them now, compounding the way all his unpaid things compounded, except this one he couldn't pay honestly, because honest payment would mean telling Saito what the half-second had been about, and that was the one currency he wasn't spending.
 
```


---

## SECTION: `AUDIT/READABILITY_DIFFS/018_The_Unwritten_Rule.diff` (unified diff — merged as fenced code)

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/READABILITY_DIFFS/018_The_Unwritten_Rule.diff` · sha256 `743e3289a65dc931d047572e6ac9824b4d489ec26be144751a97964a84c3008f` · 243 words.

```diff
--- 00_WORLD_BIBLE/CHAPTERS/018_The_Unwritten_Rule.md	2026-09-20 23:24:45.321439582 +0000
+++ work_readability/CHAPTERS/018_The_Unwritten_Rule.md	2026-09-20 23:35:25.073373681 +0000
@@ -58,7 +58,7 @@
 
 B3. The doors opened. He pushed the cart out into the cold and didn't look back, because not looking back was part of it now, the way not looking had been.
 
-The aisle took him. He worked the three boxes — serial checks, shelf numbers, the spines squared against the rank — and the work was ordinary and the ordinariness was the point, and the cold got into his cuffs the way B3 cold always did. The low-light aisle ran its length between the conditioning banks and the dead compact shelving, the overheads at their quarter-power dim, and his hands moved through the blue-gray the way they moved through everything: check, slide, square. A clerk killing time between carts. Nothing to see.
+The aisle took him. He worked the three boxes — serial checks, shelf numbers, the spines squared in their rows — and the work was ordinary and the ordinariness was the point, and the cold got into his cuffs the way B3 cold always did. The low-light aisle ran its length between the conditioning banks and the dead compact shelving, the overheads at their quarter-power dim, and his hands moved through the blue-gray the way they moved through everything: check, slide, square. A clerk killing time between carts. Nothing to see.
 
 The mirrored car waited twenty meters away at the head of the aisle, doors closed, patient.
 
```


---

## SECTION: `AUDIT/READABILITY_DIFFS/019_The_Photograph.diff` (unified diff — merged as fenced code)

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/READABILITY_DIFFS/019_The_Photograph.diff` · sha256 `c111d01c0c85a7fe55dd6181598a08b85f947a76723ea1758c93256abff6f5c8` · 192 words.

```diff
--- 00_WORLD_BIBLE/CHAPTERS/019_The_Photograph.md	2026-09-20 23:24:45.321538340 +0000
+++ work_readability/CHAPTERS/019_The_Photograph.md	2026-09-20 23:35:25.071373681 +0000
@@ -18,7 +18,7 @@
 
 Hasegawa's squeal was on B2, doing the periodicals. Far enough.
 
-He framed the floor. His shadow lay across the concrete between the shelving ranks, long in the dim, ordinary. He raised his right arm — elbow bent, hand open, the way he'd raised it a hundred times for the measurements — and held it there. He steadied his breathing the way the three-pass protocol had taught him: the body was part of the instrument. With his eyes he watched the second shadow's arm still mid-raise, catching up, three seconds behind the flesh.
+He framed the floor. His shadow lay across the concrete between the shelving ranks, long in the dim, ordinary. He raised his right arm — elbow bent, hand open, the way he'd raised it a hundred times for the measurements — and held it there. He steadied his breathing the way the three-pass protocol had taught him: the body was part of the instrument. With his eyes he watched the second shadow's arm still mid-raise, catching up, three seconds behind his body.
 
 He pressed the shutter.
 
```


---

## SECTION: `AUDIT/READABILITY_DIFFS/020_Method.diff` (unified diff — merged as fenced code)

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/READABILITY_DIFFS/020_Method.diff` · sha256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` · 0 words.

> _(The source diff file was empty — this chapter had zero changes in that revision pass.)_
