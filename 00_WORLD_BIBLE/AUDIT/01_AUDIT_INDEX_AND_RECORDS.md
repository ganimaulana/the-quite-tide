# AUDIT VOL. 01 — Audit Index, Change History & Coordinator Records — THE QUIET TIDE

> **Phase 20 repository consolidation (2026-09-21, v3.0).** This numbered volume merges 5 source files **verbatim** into one file. No content was changed, rewritten, or summarized — only this header, the source register below, and per-section attribution separators were added. To find a document's new location, see `AUDIT/00_CONSOLIDATION_MAP.md`.

## Source register

| # | Original file | Words | sha256 (pre-merge) |
|---|---|---|---|
| 1 | `AUDIT/00_AUDIT_INDEX.md` | 668 | `14331e3d9d83ee10…` |
| 2 | `AUDIT/CHANGELOG.md` | 30,796 | `3efc80a6cc2b44d1…` |
| 3 | `AUDIT/_DECISIONS.md` | 2,199 | `170ab4f2a30f0322…` |
| 4 | `AUDIT/_rename_registry.md` | 1,376 | `37ad919a2480d7fc…` |
| 5 | `AUDIT/REMAINING_RISKS.md` | 709 | `f52fb8e9f26df56c…` |

---


---

## SECTION: `AUDIT/00_AUDIT_INDEX.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/00_AUDIT_INDEX.md` · sha256 `14331e3d9d83ee10b6195ba09eb15e77c0b3ea0b333bcbbf024ea09ac3368880` · 668 words. No content changed.

# AUDIT INDEX — THE QUIET TIDE v1.2 (Albion-primary) forensic audit

**Consolidated:** 2026-09-19 · **Scope:** 16 worker audit files + consolidated issue list
**Reading order:** this index → `ISSUES.md` (the 123 consolidated issues) → `_DECISIONS.md` (coordinator calls)
→ `01_CANON_MODEL.md` (the canon reference the patch agent writes against).

**Status convention:** every source audit is COMPLETE. Raw worker counts below are *as filed*
(severity vocabularies differ per file: ECON uses Major/Minor, FACTION uses Critical/Major/Minor,
the rest CRITICAL/HIGH/MEDIUM/LOW — normalized in consolidation). 7 findings were excluded at
consolidation (verified / hold / no-action): POL-004, MIL-007, INFO-001, INFO-002, TECH-002, SOC-006, SOC-007.

## Source audits

| # | File | Status | Raw findings | Consolidated into |
|---|---|---|---|---|
| 1 | `POWER_SYSTEM_AUDIT.md` | COMPLETE | 14 (0C/5H/6M/3L) | POWER-001..014 (1:1) |
| 2 | `PROTAGONIST_AUDIT.md` | COMPLETE | 7 (0C/0H/3M/4L) | PROTAG-001, PROTAG-004, PROTAG-009..012, HIST-001 |
| 3 | `GOVERNMENT_AUDIT.md` | COMPLETE | 7 (0C/0H/2M/5L; 1 excluded) | POL-001..007 (POL-004 excluded — verified) |
| 4 | `MILITARY_AUDIT.md` | COMPLETE | 7 (0C/0H/3M/4L; 1 verification-only) | MIL-001..006 (MIL-007 verification only) |
| 5 | `LEGAL_AUDIT.md` | COMPLETE | 7 (0C/0H/4M/3L) | LAW-001..004, POL-001, POL-002 |
| 6 | `INFORMATION_AUDIT.md` | COMPLETE | 5 (0C/0H/2M/3L; 2 excluded) | INFO-001..003 |
| 7 | `TECHNOLOGY_AUDIT.md` | COMPLETE | 7 (0C/0H/3M/4L; 1 hold) | TECH-001..005 (TECH-002 held per worker note) |
| 8 | `ECONOMIC_AUDIT.md` | COMPLETE | 16 (11 Major/5 Minor) | ECON-001..016 |
| 9 | `FACTION_AUDIT.md` | COMPLETE | 31 (3 Critical/13 Major/15 Minor) | FAC-001..024, LAW-001, NAR-001, NAR-003, REL-001..003 |
| 10 | `GEOGRAPHICAL_AUDIT.md` | COMPLETE | 9 (1H/3M/5L) | GEO-001..009 (1:1) |
| 11 | `HISTORICAL_AUDIT.md` | COMPLETE | 7 (3H/2M/2L) | HIST-001..004, REL-001 |
| 12 | `RELIGION_AUDIT.md` | COMPLETE | 6 (2H/1M/3L) | REL-001..006 |
| 13 | `SOCIAL_AUDIT.md` | COMPLETE | 7 (1H/2M/4L; 2 excluded) | SOC-001..004, HIST-001 |
| 14 | `NARRATIVE_AUDIT.md` | COMPLETE | 5 (0C/0H/4M/1L) | NAR-001..004, HIST-002 |
| 15 | `SERIALIZATION_AUDIT.md` | COMPLETE | 5 (0C/0H/3M/2L) | SER-001, SER-002, PROTAG-001..003 |
| 16 | `RED_TEAM.md` | COMPLETE | 21 (0C/4H/12M/5L; 10 overlap / 11 new) | all absorbed — see mapping |
| 17 | `ISSUES.md` | COMPLETE | **123 consolidated** (3 CRITICAL / 36 HIGH / 33 MEDIUM / 51 LOW) | — |

**Raw total:** 161 worker findings → 7 excluded → 154 → 31 net merge-reductions → **123 consolidated issues**.

## Consolidated totals

- **CRITICAL: 3** — LAW-001 (Factor trafficking + tether legal vacuum), FAC-001 (SUP-004 dual identity), FAC-002 (private Attuned armies vs CANON rule)
- **HIGH: 36** — incl. the four vector-vs-prose classification breaks (POWER-001..004), Gilded Cradle's two Rules (POWER-005), the escrow mechanism gap (PROTAG-002), 11 economic issues (ECON-001..011), EVENT-092 relocation residue (HIST-001), index staleness (HIST-002), Loud-adult contradiction (NAR-001), file custody (NAR-002), Uses 13+ (SER-001), Garden/Choir/Clergy religion breaks (REL-001..003)
- **MEDIUM: 33** — Laggard filing (POWER-007), ratchet math (PROTAG-001), flare permanence (PROTAG-003), SSW visa (SOC-001), Pram destination (NAR-003), romance configs (SER-002), and 27 more
- **LOW: 51** — copy/index/terminology fixes incl. Fukushima Rule drift (HIST-005), Odaiba Wound rename (GEO-003, decision (g))

## Red-team totals (verified — no discrepancy)

RED_TEAM.md §P reports **570 asked / 543 answered / 21 patch-required / 6 intentional mystery**;
543 + 21 + 6 = 570. These match the task brief exactly. The 21 patch-required findings are all
absorbed into `ISSUES.md` (full original→merged mapping at the end of that file); the 6 intentional
mysteries are registered in `01_CANON_MODEL.md` and were not converted to issues.

## Patch-blocking decisions

Three issues cannot be patched until the coordinator decides — see `_DECISIONS.md`:
**(a)** SUP-004 identity (FAC-001) · **(f)** Gilded Cradle Rule (POWER-005) · **(b)** faction registry 36 vs 22 (FAC-007).
Decisions (c), (d), (e), (g), (h), (i), (j), (k), (l), (m), (n), (o), (p) are recommended calls the patch
agent may treat as decided unless it finds a contradiction.

## Canon reference

`01_CANON_MODEL.md` is the patch agent's authority file: CANON-LOCKED hard rules, ratified soft canon,
explicit UNKNOWNs, and the CONTRADICTIONS table (CRITICAL+HIGH only — the patch order).


---

## SECTION: `AUDIT/CHANGELOG.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/CHANGELOG.md` · sha256 `3efc80a6cc2b44d1ed6d0e501ea2ba126da318ebaac25d22a175456ac514ee1a` · 30,796 words. No content changed.

# CHANGELOG — THE QUIET TIDE World Bible

Format per entry: VERSION · DATE/CYCLE · PROBLEM · DISCOVERY · CHANGE · REASON · AFFECTED FILES · NEW RISK · STATUS.

---

## v3.0 — 2026-09-21 — Phase 20: Repository consolidation (AUDIT/ + DATABASE/ merged into numbered volumes)

- **Problem:** AUDIT/ (77 files) and DATABASE/ (38 files) had grown into 115 small files; AI readers had to traverse many files and the owner had to hunt for reports. Related documents (audit families, database domains, per-chapter diffs) were scattered.
- **Discovery:** Full inventory (checksums + word counts) of all 115 files showed clean grouping: databases by domain, audits by family, revision records by phase. The two governance files (CHAPTER_ENGINE.md, FAST_PACE_DEEP_MYSTERY_RETENTION_SOP.md §§1–60) reference each other by filename, so they were deliberately kept standalone and byte-identical rather than merged.
- **Change:** Merged verbatim (no content changed, rewritten, or summarized) into numbered volumes. DATABASE/: 38 → 7 files (00_DATABASE_INDEX.md catalog; 01_CANON_DATABASES.md = 13 convenience-view databases; 02_STORY_AND_ARC.md = 5; 03_TRACKERS.md = 9; 04_BLUEPRINTS_AND_STATE.md = 9; CHAPTER_ENGINE.md and FAST_PACE_DEEP_MYSTERY_RETENTION_SOP.md kept standalone, byte-identical). AUDIT/: 77 → 9 files (00_CONSOLIDATION_MAP.md old→new map; 01_AUDIT_INDEX_AND_RECORDS.md = index + this CHANGELOG + decisions + rename registry + remaining risks; 02_CANON_DOMAIN_AUDITS.md = 14 domain audits; 03_CHARACTER_STORY_AUDITS.md = 10; 04_FORENSIC_AND_REVIEW.md = final reports + ISSUES + RED_TEAM; 05_PROSE_AND_CHAPTER_AUDITS.md = 9 chapter/prose audits; 06_READABILITY_REVISION_RECORD.md = Phase 18 report + 4 worklogs + baseline + 20 chapter diffs; 07_NARRATIVE_QUALITY_REVISION_RECORD.md = Phase 19 report + ch018 diff; 08_HOUSEKEEPING_LOGS.md = relocation logs + protagonist patch log). CHAPTERS/ untouched (checksums verified). Root canon files untouched.
- **Reason:** Tidy, efficient repository: fewer files to traverse for AI reading; numbered ordering (00_, 01_, …) for the owner; every moved file traceable via AUDIT/00_CONSOLIDATION_MAP.md. Zero canon risk: verbatim concatenation with source-attribution separators; word-count and substring verification per volume.
- **Affected files:** All of AUDIT/ and DATABASE/ restructured; 00_INDEX.md (v3.0 + new file-structure map); 38_MANIFEST.md regenerated.
- **New risk:** None to canon. Navigational references inside historical report text that name old filenames (e.g. DATABASE/JAPANESE_CHARACTER_NAMES.md inside the retention SOP) were intentionally left verbatim; resolve via 00_CONSOLIDATION_MAP.md.
- **Status:** CONSOLIDATION COMPLETE 2026-09-21. Repo: 174 → 75 files (the v2.9 MANIFEST's "152" was an undercount — verified by full file walk: 115 AUDIT+DATABASE + 39 root + 20 CHAPTERS = 174).

---
## v2.3 — 2026-09-20 — Phase 13: Prose chapters 011–015 (ARC I, P1)

- **Problem:** Chapters 011–015 were blueprinted (Phase 10) but had no prose; chapters 001–010 were now active narrative continuity that the new batch had to remember exactly, including the latent 010→011 seam (active concealment stance, Saitō's ambiguous glance, unattributed cordon, the unpursued "why do I remember" question).
- **Discovery:** Two extraction briefs (full-read narrative state of ch 001–010 prose; binding blueprint specs for ch 011–015 with continuity warnings) grounded five parallel drafters writing directly into the working copy. Coordinator's full read of all five drafts + targeted automated scans (hidden-vocabulary, meta-language, terminology-leak, power, timeline, character-knowledge, repetition, cross-batch style) found zero FAILs at draft stage. 5 prose-only patches: (1) ch.14 "ch.4" authorial reference removed; (2) ch.14 ledger series page clarified as backfilled from phone notes (resolves "going back years" vs. ch.12's newly-bought notebook); (3) ch.14 ledger pocket standardized to trouser pocket (4 occurrences, matching ch.12/13); (4) ch.15 "ch.2"/"ch.15" authorial references removed; (5) ch.13 "in the batch" authorial framing softened. Canon, blueprints, and chapters 001–010 were read-only throughout.
- **Change:** Added 8 new files: CHAPTERS/011_Aftershock.md (2,558w), CHAPTERS/012_The_Private_Ledger.md (2,588w), CHAPTERS/013_The_Night_Keeps.md (1,990w), CHAPTERS/014_Three_Point_One.md (2,720w), CHAPTERS/015_Rent_Day_Arithmetic.md (2,618w), DATABASE/CHAPTER_011_015_STATE_SNAPSHOT.md (end-of-ch-15 baseline for ch 16+), DATABASE/CHAPTER_011_015_CAUSALITY.md (10→16 seam chain), AUDIT/PROSE_011_015_AUDIT.md (14-dimension verdicts per chapter; 5 prose-only patches; 0 FAIL). Updated 00_INDEX.md (v2.3), 38_MANIFEST.md (127 → 135 files), AUDIT/CHANGELOG.md.
- **Reason:** Third controlled prose batch: the 010→011 seam picked up exactly (the invoice comes due; silence re-priced nightly); the ledger system built as camouflage discipline ("Stay small. Stay beneath every instrument."); one genuinely ordinary night (ch.13); the 3.0→3.1 lengthening measured three ways and filed without inference beyond lengthening (MYSTERY-001 advances, 0 resolved, 0 L3+ truth; new sub-question "what pays for the tenth?" posed, unanswered); the batch closes on domestic arithmetic and the loaded 9/20 dinner. Arthur at Stage 1 throughout; zero Fathoms; "Tier 1" verified as his private mundane filing shorthand only.
- **[PROSE] (prose-only corrections — canon NOT redesigned):** 5 patches listed under Discovery above.
- **Affected files:** 8 new files; 00_INDEX.md; 38_MANIFEST.md; AUDIT/CHANGELOG.md.
- **New risk:** 3 accepted WATCH items handed to batch 016–020: (1) ch.11's 19:40 post-cordon sleep-in must not drift into a routine change; vary chapter-method patterns naturally; (2) the ledger is live tracked state (on the shelf at home as of ch.15) — every future chapter must know where it is; it is a discoverable risk; (3) Nadia's Friday 9/18 dawn overlap was not depicted in ch.13 — do not assume it occurred; place her deliberately. All documented in AUDIT/PROSE_011_015_AUDIT.md.
- **Status:** PROSE FINAL 2026-09-20. Canon unchanged (all eight systems remain CANON-LOCKED). Chapters 001–015 READY for batch 016–020.

---

## v2.2 — 2026-09-20 — Phase 12: Prose chapters 006–010 (ARC I, P1)

- **Problem:** Chapters 006–010 were blueprinted (Phase 10) but had no prose; chapters 001–005 were now active narrative continuity that the new batch had to remember exactly.
- **Discovery:** Two extraction briefs (full-read narrative state of ch 001–005 prose; binding blueprint specs for ch 006–010) grounded five parallel drafters. Two independent audit passes found: factual audit 66 PASS / 3 WATCH / 2 FAIL (both FAIL = POV person break in ch 009/010 drafts, written first-person against the batch's close-third convention); craft audit 26 findings (7 HIGH: the same POV break, identical openings 009/010 and 007/008, 010's declaimed ending, "Jakarta boxes" justification, didactic drift in 009/010). All resolved by 41 prose-only patches, including full POV rewrites of 009/010 into close third-person past. Zero class-(A) canon contradictions. Canon, blueprint, and chapters 001–005 were read-only throughout (verified by diff: working tree differs by additions only).
- **Change:** Added 8 new files: CHAPTERS/006_Dark_Water.md (2,123w), CHAPTERS/007_No_Category.md (2,552w), CHAPTERS/008_Melon_Pan.md (2,292w), CHAPTERS/009_Impossible_Constancy.md (2,069w), CHAPTERS/010_The_Cordon.md (2,050w), DATABASE/CHAPTER_006_010_STATE_SNAPSHOT.md (end-of-ch-10 baseline for ch 11+), DATABASE/CHAPTER_006_010_CAUSALITY.md (6→11 seam chain), AUDIT/PROSE_006_010_AUDIT.md (14-dimension verdicts per chapter; 0 FAIL remaining post-patch). Updated 00_INDEX.md (v2.2), 38_MANIFEST.md (119 → 127 files), AUDIT/CHANGELOG.md.
- **Reason:** Second controlled prose batch: consequence-first writing (every major event traceable to ch 1–5), mystery advanced without solving (001: constancy datum, archive null, Use-1 cross-check; 002 seeded; 0 resolved; 0 L3+ truth), Arthur at Stage 1 throughout, romance unforced (A-seed one-sided; E-friendship with compounding lie), batch closes on its single REVERSAL (ch.10: "my memory doesn't rot like theirs" — active concealment stance).
- **[PROSE] (prose-only corrections — canon NOT redesigned):** 41 patches incl. (1) ch 009/010 POV first→close-third rewrite; (2) 010 opening rewritten (identical 19-word opening with 009 removed); (3) 008 opening rewritten off the punch clock; (4) 010 ending declamation trimmed, REVERSAL kept legible; (5) 2022 recall kept in 010 per the §12.5 canon adjudication (blueprint-binding; the "seed it in 009" proposal rejected as a blueprint deviation), tightened to 3 sentences with the ch.9→10 motivation bridge; (6) plant pot shelf→desk; sleep figure→five hours; corridor endpoint de-pinned; "nine days"→"ten days"; (7) tic passes ("the way" density, "a clerk who" aphorism tic, filing-idiom thinning, turning-point announcements cut, repeated images singled).
- **Affected files:** 8 new files; 00_INDEX.md; 38_MANIFEST.md; AUDIT/CHANGELOG.md.
- **New risk:** 5 accepted WATCH items handed to batch 011–015 (ch.7's slow method-chapter pattern must vary; ch.10 residual "the way" density; the 010→011 latent seam — active concealment, Saitō's glance, unattributed cordon, unpursued question — must be picked up exactly; the Saitō lie keeps compounding; false-belief bookkeeping must persist) — all documented in AUDIT/PROSE_006_010_AUDIT.md §12.
- **Status:** PROSE FINAL 2026-09-20. Canon unchanged (all eight systems remain CANON-LOCKED). Chapters 001–010 READY for batch 011–015.

---

## v2.1 — 2026-09-20 — Phase 10: Chapter blueprints 1–20 (ARC I, P1)

- **Problem:** Canon complete through Phase 9 (all eight systems CANON-LOCKED; ~140 Chapter Engine rules); no chapter-level plans existed. Phase 10 required detailed blueprints for Chapters 1–20 — planning only, no prose — without reopening canon.
- **Discovery:** Four extraction briefs (story/arc, mystery, character, engine) grounded two drafting batches (ch 1–10, ch 11–20); an independent audit ran the full 20×10 Chapter Engine test and found 2 FAIL (mechanical timestamp defects) + 25 WATCH, zero class-(A) canon contradictions. All defects were patched in the blueprints; canon was read-only throughout.
- **Change:** Added 4 new files: DATABASE/CHAPTER_BLUEPRINT_001_020.md (all 20 chapter plans, post-patch final), DATABASE/CHAPTER_001_020_CAUSALITY.md (19-seam chain, §21), DATABASE/CHAPTER_001_020_STATE_SNAPSHOT.md (end-of-ch-20 baseline, §22), AUDIT/CHAPTER_BLUEPRINT_001_020_AUDIT.md (20-section audit; engine test 20/20 PASS post-patch). Updated 00_INDEX.md, 38_MANIFEST.md (109 → 113 files).
- **Reason:** ARC I's first quarter needed executable, continuity-verified plans (timeline, causality, knowledge states, mystery/chain movement, power/faction/romance continuity) before any prose generation.
- **[BLUEPRINT PATCH] (planning corrections — canon NOT redesigned):** (1) ch 13 timestamp Thu 9/17 ~03:00 → Fri 9/18 ~03:00 (was inside ch 12's shift window); (2) ch 18 timestamp Tue 9/22 ~00:40 → Wed 9/23 ~00:40 (~21h before its shift); (3) CHAIN-013 rule-naming moved ch 18 → ch 20 (canon window ch. 20–40; ch 18 keeps unease only); (4) ch 11 "containment van" → "unmarked van"; cordon truth-state rewritten (unattributed — the "Veil-management perimeter (ch 10 canon)" citation was false); (5) ch 14 terminology reconciled (3.0s defended measurements stand; 3.1s is the first defended *lengthening*); (6) ch 15 double rent payment removed (reconciliation only); (7) ch 19 "she is Quiet" → observed-asymmetry language; "only instrument" qualified (voice-memo echo excepted); photo negative narrowed (temporal lag invisible in a still; meter-lying exposure wrongness is canon texture) + 2020 discharge-paper verification beat added; (8) ch 20 dream's "new detail" corrected (recurrence is the datum; direction-not-shape unchanged from ch 6); dream moved ~16:00 → ~14:00–14:30 (inside sleep hours); shift end completed → Fri 9/25 06:00; (9) structural strengthenings — ch 13 break-rotation cover, ch 11 cart-run beat, ch 2 camouflage-as-temperament label (no new facts/characters/mystery movement); (10) header bookkeeping — "USE 1 DISCOVERED" → "first deliberately applied (discovered 2022)"; "≈5:1" → honest counts (8 questions, 0 resolved, 0 L3+); unsourced "ordinary beats ≥4" quota dropped; Nadia's windows standardized (work overlap 04:00–06:00; convenience store after 06:00).
- **Affected files:** 4 new files; 00_INDEX.md; 38_MANIFEST.md; AUDIT/CHANGELOG.md.
- **New risk:** 7 accepted risks handed to the prose phase (quiet-chapter thinness; ch 18's uninterpreted avoidance; ch 19's fine-distinction negative; ch 20's open questions must stay open; the Saitō debt has no deadline; the ledger's unfired tripwire; hidden-world vocabulary must stay out of on-page text before its windows) — all documented in the audit §20.
- **Status:** BLUEPRINT FINAL 2026-09-20. Canon unchanged (all eight systems remain CANON-LOCKED). No prose, dialogue, narrative, scenes, or finished chapters generated.

---

## v0.1 — 2026-09-19 — Phase 1: Core ontology established
- **Problem:** No shared foundation; parallel drafters would diverge.
- **Discovery:** N/A (initial construction).
- **Change:** Wrote 00_INDEX, 01_CORE_PREMISE, 02_WORLD_RULES, 03_SUPERNATURAL_SYSTEM, 04_POWER_SYSTEM, 36_TERMINOLOGY. Locked metaphysical hard rules (no resurrection, no permanent created matter, no past alteration, no direct mind control, no power copying, anchored Slipping, irreversible Erosion), economic hard rules (non-fungible anomalies, Seismograph visibility, borrowed wealth reverts, information as the scarce resource), and secrecy hard rules (Veil Reflex, static rot, deepfake dividend).
- **Reason:** Every subsystem must obey one ontology; objective truth vs human theories kept distinct.
- **Affected files:** 00, 01, 02, 03, 04, 36.
- **New risk:** Drafters may still drift on tone; mitigated by mandatory Phase-1 read + registry.
- **Status:** CANON-LOCKED (02), CANON (others).

## v0.2 — 2026-09-19 — Phase 2a: State-power draft (Drafter A)
- **Problem:** Needed governments, classification, international system, military, law, information control.
- **Discovery:** Drafted cleanly against Phase-1 rules.
- **Change:** Added 05_ANOMALY_CLASSIFICATION (Meridian Vector system), 06_GOVERNMENTS (13 countries), 07_INTERNATIONAL_RELATIONS (Compact/Tribunal/Ledger/Seismograph Authority), 13_MILITARY, 14_LAW_ENFORCEMENT, 26_INFORMATION_CONTROL. New IDs: GOV-008..013, CHAR-002..011, CASE-001..006.
- **Reason:** Per spec §§5–9, 13–14, 23.
- **Affected files:** 05, 06, 07, 13, 14, 26; _registry.md.
- **New risk:** EVENT-041/062/073 are PROVISIONAL placeholders pending Drafter D's timeline; minor officials unnamed (CHAR-012+ open).
- **Status:** CANON (provisional flags in-file).

## v0.3 — 2026-09-19 — Phase 2b: Society-economy draft (Drafter B)
- **Problem:** Needed economy, currencies, religions, corporations, education, medicine, media, civilian life, classes, technology.
- **Discovery:** Drafted cleanly; Arthur's records-clerk job made structurally load-bearing (human verification layer of NQA's claims-ML detection pipeline).
- **Change:** Added 08_ECONOMY, 09_CURRENCIES (the "sounding" SND settlement unit), 10_RELIGIONS, 11_CORPORATIONS (CORP-001..012), 15_EDUCATION, 16_MEDICINE, 17_MEDIA_AND_INTERNET, 18_CIVILIAN_LIFE, 19_SOCIAL_CLASSES, 27_TECHNOLOGY. New IDs: CORP-012, ACAD-001..003, MED-001/002, NET-001/002. Ten new glossary terms appended to 36_TERMINOLOGY.
- **Reason:** Per spec §§7, 10–11, 15–19, 24–25.
- **Affected files:** 08, 09, 10, 11, 15, 16, 17, 18, 19, 27, 36; _registry.md.
- **New risk:** Market sizes/salary bands marked PROVISIONAL; corporate leadership names in-file only (no CHAR IDs — flagged for Drafter D).
- **Status:** CANON (provisional flags in-file).

## v0.4 — 2026-09-19 — REGIONAL DIRECTIVE (user): East Asia / Pacific Rim primary
- **Problem:** Original draft weighted the world globally-flat with the protagonist in Jakarta; user requires a primary narrative region (East Asia/Pacific Rim), one primary country selected by structural suitability (not fame), ~60–70% of early geographic detail on it, one fictional major metro as the protagonist's environment (20+ districts), secondary regions (China, South Korea, Albion, Taiwan, Russia's Far East), SE Asia as modern states with Indonesia strategically important but not overpowered, global regions lighter, HOME→CITY→COUNTRY→REGION→WORLD scale discipline, one global supernatural system across regions, and 50 new regional conflicts (10 international / 10 regional-supernatural / 10 corporate / 10 intelligence / 10 anomaly-related) in 31_CONFLICT_ENGINE + 34_FACTION_RELATIONSHIPS.
- **Discovery:** Country evaluation (12 criteria: urban density, infrastructure, economy, corporate environment, government structure, historical depth, folklore, religious diversity, international connections, containment suitability, underground-org suitability, serialized-storytelling suitability). Albion/SK/Taiwan/China assigned secondary by the directive itself (Albion also overused in fiction — not picked by fame). Remaining: Philippines / Vietnam / Malaysia. **Philippines selected:** archipelagic seep geography (volcanic belt + maritime stress), deepest folklore of the three, Catholic/Muslim/animist diversity, uneven modernity (more story surface), diaspora + alliance + South China Sea stakes (international connections), democratic cycles with strongman interludes (government variance → underground-org suitability). Vietnam second, Malaysia third.
- **Change:**
  1. Primary country = the Philippines (COUNTRY-026). Fictional primary metro = **LIWANAG CITY** (CITY-021): coastal Luzon megacity, ~9.2M, financial/tech capital ("liwanag" = light — thematic counterpoint to the shadow anomaly).
  2. Protagonist relocated: CHAR-001 Reed Arthur is now an **Indonesian migrant worker in Liwanag City**, night-shift records clerk at NQA's Liwanag branch (HQ stays Jakarta). Deepens "weak and overlooked" foundation; preserves Indonesian identity and NQA's Indonesian corporate presence.
  3. Drafters C and D redirected mid-draft (interrupt + new brief): C rebalances 20/21/22/23 + 12/34 around the hierarchy and builds Liwanag City's 20+ districts; D relocates Arthur in 29, adds Philippine history depth in 24/25, and authors RC-001..050 in 31_CONFLICT_ENGINE (C references them in 34).
  4. New IDs claimed: COUNTRY-026..030 (Philippines, Malaysia, Thailand, Vietnam, Taiwan), CITY-021..032 (Liwanag City, Manila, Cebu, Davao, Shanghai, Taipei, Vladivostok, Kuala Lumpur, Bangkok, Ho Chi Minh City, Hanoi, Osaka), RC-001..050.
  5. Regional consistency rule locked: one supernatural system; regions differ only in interpretation/regulation/containment/exploitation.
- **Reason:** User directive; also structurally improves serialized storytelling (single deep home base vs flat global survey).
- **Affected files:** 01 (premise + regional directive section), 20, 21, 22, 23, 24, 25, 29, 30, 31, 32, 33, 34, 12; _registry.md. (18_CIVILIAN_LIFE and 11_CORPORATIONS CORP-011 to be patched post-draft for the relocation.)
- **New risk:** B's 18_CIVILIAN_LIFE day-in-the-life is still Jakarta-based (patch scheduled); A's 06_GOVERNMENTS lacks a Philippines profile (patch scheduled); C/D redirect applied mid-draft — verify no structural duplication in assembly.
- **Status:** CANON (directive); implementation in progress.

## v0.5 — 2026-09-19 — Phase 2c/d verification: gaps found, repair dispatched
- **Problem:** Verification of the Drafter D completion handoff against disk revealed: (1) the handoff was mislabeled "Drafter C" (content describes C's files; authorship ambiguous — logged, not fatal); (2) 35_CANON_DATABASE.md was never written despite being D's assignment and referenced by registry notes; (3) 31_CONFLICT_ENGINE.md retains 24× "SUP-001" mislabeling the Meridian Compact (registry: INTL-001; SUP-001 = the Drowned Choir) plus invalid file links (08_CORPORATIONS, 09_RELIGIONS, 13_RESEARCH_ACADEMIA, 14_INTERNATIONAL_LAW — none exist); (4) 21_CITIES.md's CITY-021 Liwanag section is 43 lines — the "22 districts" claim is not met; district-level detail required by the regional directive is missing; (5) 34_FACTION_RELATIONSHIPS.md references only 10 of 50 RC IDs; (6) 06_GOVERNMENTS.md has no Philippines/GOV-014 profile; (7) 18_CIVILIAN_LIFE.md's Arthur day-in-the-life is still Jakarta-based; (8) CORP-011 profile predates the Liwanag branch.
- **Discovery:** Disk inspection (grep/awk), not agent claims. Confirmed present and good: RC-001..050 all defined in 31 Part IV (full generator format), 29's relocation canon, 28's ANOMALY-001 cross-ref, registry's new-ID blocks (CORP-013, REL-008, INTL-008/009, RES-006/007, IND-006/007/010, SUP-011, GOV-014..016, CRIM-006, CHAR-012..034, CASE-001..006).
- **Change:** Dispatched three repair agents: E (Liwanag City 20+ district expansion → scratch file for later splice), F1 (31 ID/link repair), F2 (18/11/06 relocation patches + 35_CANON_DATABASE.md creation + RC interlock supplement scratch). C-owned files (21, 34) not edited directly until C's agent confirms done.
- **Reason:** Assembly cannot proceed on unverified claims; gaps are structural (missing file, missing district detail mandated by user directive).
- **Affected files:** 31, 18, 11, 06, 35 (new), 21 (pending splice), 34 (pending merge); _registry.md.
- **New risk:** C's agent still running — merge conflicts if it edits 21/34 concurrently; mitigated via scratch files.
- **Status:** In progress.

## v0.6 — 2026-09-19 — Phase 3 assembly: Liwanag splice, RC merge, relocation patches verified
- **Problem:** CITY-021 was a 43-line stub (district mandate unmet); 34 covered only 30/50 RCs individually; 18/11/06 predated the relocation; 22/23 global-heavy vs the 60–70% regional weighting.
- **Discovery:** Agent E delivered a 295-line CITY-021 replacement (22 districts × 11 fields, city systems, faction footprint, hooks, RC wiring).
- **Change:**
  1. Spliced E's expansion into 21_CITIES.md (lines 11–53 replaced; verified 22 district headings + systems/footprint/atmosphere/hooks sections).
  2. Merged F2's RC_INTERLOCK_SUPPLEMENT.md into 34_FACTION_RELATIONSHIPS.md as §34.6 (RC-011..030 individual interlocks); 34 now covers all 50 RCs.
  3. F2's patches verified on disk: 18 §18.1 Liwanag day-in-the-life; 11 CORP-011 (HQ Jakarta + Liwanag branch); 06 COUNTRY-026 Philippines + GOV-014 KNF full profile + GOV-015/016 provisional stubs; 35 normalized (22 namespaces).
  4. F1's 31 repair verified: 1 genuine fix (RC-035 RES-005→RES-007); D's prior collision-repair confirmed; 4 remaining SUP-001 refs are legitimate Drowned Choir uses.
  5. Dispatched Agent G to rebalance 22/23 by conversion (~8 LOC, ~4 ZONE, ~4 SITE → Philippines/regional), preserving counts and IDs.
- **Reason:** Assembly integrity before red-team audits; auditors must attack the final regional structure.
- **Affected files:** 21, 34, 18, 11, 06, 35, 31, 22, 23 (pending G).
- **New risk:** None new; G's conversions must not break 31/34 cross-refs (briefed to stay consistent).
- **Status:** In progress (G running).

## v0.7 — 2026-09-19 — Phase 3 closeout: G rebalance landed + stale-reference repairs
- **Problem:** Agent G's conversions orphaned 4 cross-references; 35's 16 converted rows were stale.
- **Discovery:** G's own report flagged them (verified on disk).
- **Change:**
  1. 28_ANOMALY.md ANOMALY-010: "Vaulted at SITE-003 (UK)" → "Vaulted at SITE-003 (the Moon Vault, Pampang) under Ledger escrow" (the bribed-guard story now fits better — Combine-operated vault).
  2. 12_FACTIONS.md CRIM-004 secret: "built SITE-009" → "built SITE-006's storage protocols"; 23's SITE-006 parenthetical updated to match (was pointing at the old SITE-009 secret).
  3. 34 JCC row: "SITE-006/008/009/010" → operates 006/008, liaisons at 010 (Station Habagat); SITE-009 (Isla Cuarentena) KNF-run, "the JCC calls this temporary; the KNF does not return the calls."
  4. 35: all 16 converted LOC/ZONE/SITE rows updated to new names + one-liners (16/16).
- **Reason:** No orphaned references allowed in the draft bible.
- **Affected files:** 28, 12, 23, 34, 35.
- **New risk:** None.
- **Status:** CANON. Draft bible structurally complete — entering Phase 4 red-team audits.

## v0.8 — 2026-09-19 — Phase 4 red-team: Audit 2 received (economy/society/secrecy)
- **Problem:** No substantive red-team had attacked the economy/society/secrecy layers.
- **Discovery:** External audit report delivered (report-only; no files edited).
- **Change:** Report saved as AUDIT/AUDIT_02_ECONOMY_SOCIETY_SECRECY.md. Findings: 0 CRITICAL / 3 HIGH / 7 MEDIUM / 9 LOW; 30 skeptical-reader questions (22 answered from canon, 8 flagged). Patching deferred until Audits 1 and 3 land (patch all findings together to avoid contradictions).
- **Affected files:** AUDIT/AUDIT_02_ECONOMY_SOCIETY_SECRECY.md (new).
- **New risk:** None.
- **Status:** AUDIT REPORT (not canon).

## v0.9 — 2026-09-19 — Phase 4 red-team: Audit 1 received (supernatural/power)
- **Problem:** No substantive red-team had attacked the power system or the protagonist anomaly.
- **Discovery:** External audit report delivered (report-only; no files edited).
- **Change:** Report saved as AUDIT/AUDIT_01_SUPERNATURAL_POWER.md. Findings: 0 CRITICAL / 2 HIGH / 10 MEDIUM / 8 LOW; 58 attacks; 30 skeptical-reader questions (22 answered, 8 flagged). Key: Laggard transfer farmable (F-H1), out-of-phase wall-phasing undefined (F-H2), 9 vector inconsistencies across 05/28/29/01 (F-M4), Erosion micro-costs unmodeled (F-M2). Patching deferred until Audit 3 lands.
- **Affected files:** AUDIT/AUDIT_01_SUPERNATURAL_POWER.md (new).
- **New risk:** None.
- **Status:** AUDIT REPORT (not canon).

## v0.10 — 2026-09-19 — Phase 4 complete: Audit 3 received, consolidated patch dispatched
- **Problem:** State/faction/history/geography layers unattacked.
- **Discovery:** Audit 3 report delivered (report-only; no files edited).
- **Change:** Report saved as AUDIT/AUDIT_03_STATE_FACTIONS_HISTORY.md. Findings: 0 CRITICAL / 4 HIGH / 5 MEDIUM / 4 LOW; 38 attacks; 30 reader questions (23 answered, 7 flagged). **Phase 4 totals: 124 attacks · 52 findings (0 CRITICAL / 9 HIGH / 22 MEDIUM / 21 LOW) · 90 skeptical-reader questions (67 answered from canon, 23 flagged).**
- **Verification:** Coordinator independently verified the highest-stakes claims on disk before dispatching patches: treaty chronology (F1), Choir/Ledger founding dates (F2), Tunguska (F4), EVENT-075 miscitation (F10), and all nine vector inconsistencies (F-M4) — all real.
- **Change:** A single Patch Agent dispatched with a consolidated 44-item patch order covering all 52 findings (overlaps merged: Choir/elections, Drowndust, Laggard wards). Instructions: verify each auditor claim on disk before editing; use auditor-recommended fixes; no CANON-LOCKED meaning changes except two approved scoping edits; invented numbers must be internally consistent and marked CANON; log everything as CHANGELOG v1.0 with a findings-patched table.
- **Affected files:** AUDIT/AUDIT_03_STATE_FACTIONS_HISTORY.md (new); patch target files TBD by Patch Agent.
- **New risk:** None (audit reports are not canon).
- **Status:** PHASE 4 AUDITS COMPLETE — patching in progress.

## v1.0 — Phase 4 red-team patches
- **Problem:** 52 red-team findings (0 CRITICAL / 9 HIGH / 22 MEDIUM / 21 LOW) across three audits; overlapping fixes consolidated into a 44-item patch order (P1–P44).
- **Discovery:** Coordinator verified highest-stakes claims on disk before patching (treaty chronology, Choir/Ledger founding dates, Tunguska, EVENT-075 miscitation, all nine vector inconsistencies — all real). Patch Agent re-verified each claim against source before editing.
- **Change:** All 52 findings patched in P1→P44 order. Two CANON-LOCKED edits applied under explicit authorization: (a) 02 causal-bubble caps scoped to *Attuned channeling*, with a CANON-LOCKED anomaly-Rule proportional-cost exception added (preserves ANOMALY-020); (b) mind-control sentence replaced with the approved wording verbatim. All newly invented quantities marked CANON and kept consistent with: ~90,000 T2s · ~8,700 T3+ · hidden economy $140–200B/yr · Seep frequency ~3× since 2000 · EVENT-090's 900+ events/day (Jan 2024). Cleanup fixes: P15/P16 CANON markers made explicit and clean; P10 Drowndust parenthetical corrected (Quiet/Loud non-Attuned unaffected; Attuned-only); P20/P22 mid-paragraph CANON markers reformatted as clean blockquotes. F-M10 (Vesper treatment boundary) added as a one-line guardrail in this pass.
- **Reason:** Close every red-team gap while preserving CANON-LOCKED meaning.
- **Affected files:** 02, 03, 04, 05, 06, 07, 08, 09, 11, 13, 14, 16, 17, 23, 24, 25, 26, 27, 28, 29, 31, 34.
- **New risk:** None — invented numbers are arithmetic-checked against existing canon.
- **Status:** CANON-LOCKED (02 edits) + CANON (all additions).

### Findings → patches table

| Finding (audit) | Severity | Patch | Files changed | Change summary |
|---|---|---|---|---|
| F-H1 (A1) | HIGH | P1 | 29 | Laggard transfer: requires unforced death/Drowning + naturally present Loud witness; engineered/staged transfer or positioned witness → tether dissipates; no witness → dissipation; Ilsa→Yusuf→Arthur preserved; journals carry the anti-engineering rule |
| F-H2 (A1) | HIGH | P2 | 29 | Out-of-phase: Arthur moves normally; solid matter blocks; "intangible" = no touch/contact/force exchange only, not wall-phasing |
| F-M1 (A1) | MED | P25 | 02 | Causal-bubble caps scoped to *Attuned channeling* (CANON-LOCKED); added CANON-LOCKED anomaly-Rule proportional-cost exception |
| F-M2 (A1) | MED | P21 | 04 | Routine-work Erosion model: ~0.005–0.02 Fathoms/day; ~5 Fathoms/yr career budget; serious uses individually rationed |
| F-M3 (A1) | MED | P22 | 04 | Pattern theft: thief inherits victim's accumulated Fathoms; thief's own accumulation rate doubles |
| F-M4 (A1) | MED | P4 | 05, 28, 29, 01 | Vector reconciliation: 006, 007, 012, 013, 020, 025, 029, 030 synced to 05 §5.5; ANOMALY-001 = MV-T1/C-A/—/Local/Unknown; old Reactive/None readings flagged as in-world examiner dodge |
| F-M5 (A1) + M-5 (A2) | MED | P27 | 04, 14 (ref 07) | Choir use in elections/referenda = Accords/Tribunal offense; campaigns Lantern-monitored; voidability cross-ref |
| F-M6 (A1) | MED | P26 | 14 | Person-attached anomalies cannot be Ledger-titled; sale of the holder = trafficking under Accords law |
| F-M7 (A1) | MED | P23 | 02 | Pattern capture only during collapse; requires T3+ Lantern; Seismograph-visible; consent or Tribunal warrant required |
| F-M8 (A1) | MED | P3 | 29 | Wards dampen Laggard effects but cannot sever tether; deep use inside wards possible but louder to the entity; clean-recording dead-man's-switch escrow across multiple recipients |
| F-M9 (A1) | MED | P24 | 02 | Mind-control sentence replaced with approved wording verbatim |
| F-M10 (A1) | MED | P44 | 16 | Vesper guardrail: "treated" = slowed only; any reversal claim = fraud or canon-break requiring CHANGELOG |
| F-L1 (A1) | LOW | P42-1 | 02 | "Someone who knows you" = another living person (not self/echo/recording) |
| F-L2 (A1) | LOW | P42-2 | 28 | ANOMALY-008: coin reveals, never edits — no verified case of a changed death-year |
| F-L3 (A1) | LOW | P37 | 08, 11 | Large Quiet claims Lantern-adjusted; fraud priced into loss ratio; payouts service-denominated (anti-fraud design) |
| F-L4 (A1) | LOW | P42-4 | 29 | Loud non-Attuned status creates no registration duty; Census registers Attuned, not Loudness |
| F-L5 (A1) | LOW | P42-5 | 02, 09 | Slip-c courier chains legal but economically dead (Erosion compounds past cargo value within three hops) |
| F-L6 (A1) | LOW | P42-6 | 02, 04 | Hardened wards shred all non-whitelisted arrivals; recognition decays with time/inaccuracy |
| F-L7 (A1) | LOW | P42-7 | 16 (ref 10, 08) | Pastoral fraud controls for "echo visits": Majelis 2001 ruling as doctrinal firewall; Lantern-verified chaplaincy licensing; unlicensed echo mediums prosecuted as fraud; bereavement payouts in appointments, not cash |
| F-L8 (A1) | LOW | P42-8 | 28 | ANOMALY-011: settlement runs through the debt writer's own agency — as though only the debt writer could have settled it while alive |
| H-1 (A2) | HIGH | P5 | 05, 26 | Sweeper capacity arithmetic (CANON): 2000 ~110k events/yr, ~4,500 T3+, ~31k Sweepers; 2024 ~330k events/yr, ~13.5k T3+, ~48k Sweepers; cost-per-tier curve; voted-down 60% expansion; ~60% coverage assumption; voted-down Council funding gap |
| H-2 (A2) | HIGH | P6 | 03, 16 | Loudness = stable vivid Seep-event retention only, not general eidetic memory; Arthur's detail-recall exceptional even among Loud |
| H-3 (A2) | HIGH | P7 | 17 | Infohazard race doctrine: Seismograph → Lantern → JCC race; 100,000-reader lost-race threshold; 11-of-13 race wins since 2000 (CANON); ISP severing, content-hash orders, chain-breaking; counter-pattern "vaccines" rejected as standing doctrine |
| M-1 (A2) | MED | P28 | 02, 08 | Licensed conjuration contracting: real trade, Seismograph-visible, Erosion-priced, regulated; usually uneconomic vs mundane alternatives |
| M-2 (A2) | MED | P29 | 09 | Precognition mechanics: reads present informational traces/probability branches; observer reflexivity; ~0.1–0.5 Fathoms/trade; crypto compliance via Ledger banking leverage; two crypto-precog desks Drowned since 2019 |
| M-3 (A2) | MED | P30 | 09, 11 | Wards suppress acoustic/thermal/RF + Tide; High Tide degradation raises customs risk; Kestrel High Tide surcharge |
| M-4 (A2) | MED | P10 | 04, 13, 25 | Drowndust = processed Drowning-site residue; supply capped by Drownings; Quiet unaffected (Attuned-only); weak forensic verification; SITE-006 counter-stockpile; industrial Drowning = Compact casus belli; Kyiv 2022 remains disputed, no confirmed civilian mass-signature |
| M-6 (A2) | MED | P31 | 08 (ref 11) | Auditors audit numbers, not causes; threshold-agency liaison manages 40+ regulators; Meridian Re's strategic tedium as doctrine |
| M-7 (A2) | MED | P32 | 27 | Clerk sampling math: ~4,000 flags/day vs ~400–600 confirmations; recall-over-precision tuning; clerks as label-production function; GIGO; Arthur beats the sampling bound |
| L-1 (A2) | LOW | P33 | 14, 08 | Licensed commercial Choir: pattern-of-outcome audits; influenced contracts voidable; CASE-002 precedent; counterparty screening as standard M&A warranty |
| L-2 (A2) | LOW | P34 | 08, 16 | Erosion-care liability ~$2B/yr buried in defense/health line items; fastest-growing unacknowledged liability |
| L-3 (A2) | LOW | P35 | 26 | Loud-staffed archives; paper-over-video doctrine; I-flag handling (summaries only, originals destroyed); Archivists' role; Drowned-archivist protocol |
| L-4 (A2) | LOW | P36 | 16, 11 | Stillwater's mundane indication: approved anxiolytic/sedative with real trials/patients; graywater ER coding as benzodiazepine-adjacent sedative overdose |
| L-5 (A2) | LOW | P37 | 08, 11 | Quiet payouts service-denominated, not cash (structural anti-fraud); large cash claims Lantern-adjusted; fraud priced into loss ratio |
| L-6 (A2) | LOW | P38 | 26 | "Mutually assured disclosure" named; 1983 near-miss; Memorandum Group's hostage-exchange role |
| L-7 (A2) | LOW | P39 | 26 | Seizure doctrine for unregistered Seep materials; quiet-visit escalation ladder (visit → audit → seizure → Tribunal referral) |
| L-8 (A2) | LOW | P40 | 27 | ML proposes Rule hypotheses; confirmation remains human; training-hygiene bound retained |
| L-9 (A2) | LOW | P41 | 08 (ref 19) | Hidden-world billions require unpowered multigenerational capital; Pale Court as worked example; Ledger moat as new-entrant barrier; criminal elites top out at millions |
| F1 (A3) | HIGH | P8 | 07, 13, 24, 25 | Treaty chronology: 1949 charter/principles → 1963–68 Seismograph build → 1977 revision (Quiet Night) → 1979 Second Protocols (Tribunal/JCC, re-ratification); four revisions named in 07; Drowndust "1977 Accords" wording corrected |
| F2 (A3) | HIGH | P9 | 06, 24 | Origins reconciliation table: Choir (Marseille 1953; Adler 1965 merger); Ledger (1683 escrow lineage → 1975 predecessor → 1977 syndicate); SMD (occupation origin → 1980s rebuild → 1995 recharter); artificial-Awakening count closed at three state lineages + one corporate (Vermilion experimental, excluded) |
| F3 (A3) | HIGH | P10 | 04, 13, 25 | Drowndust mechanics (see M-4 above); Kyiv 2022 deployment forensically disputed, sealed Tribunal case |
| F4 (A3) | HIGH | P11 | 24, 25 | Tunguska: dormant and unwatched 1989–97; "continuously contained" = Compact fiction; remains oldest known Seep |
| F5 (A3) | MED | P12 | 14 | Lantern forensics: residue + low-fidelity surface impressions only; no deep replay; archives store written reports, not impressions |
| F6 (A3) | MED | P13 | 13 | 90-second rule clarified: applies to sustained engagements; raids decided pre-entry via intel/ward survey/planning |
| F7 (A3) | MED | P14 | 28 | ANOMALY-010 title dispute among UK threshold bureau, Compact Claims Office, Ferrymen salvage claim; Ledger escrow pending |
| F8 (A3) | MED | P15 | 14 | Seeding desks: friction-over-punishment deterrence; inoculation briefings, backlash-mark screening, post-incident audits; 4–8 Lanterns / ~200 screenings/yr (CANON); 2009 Okafor, 2017 Meridian House, 2020 Santara cases |
| F9 (A3) | MED | P16 | 06, 23, 34 | SITE-009: KNF sovereignty fiction; Compact co-funds ~40% (CANON); twelve JCC secondees (CANON); cross-referenced in KNF profile + relationship file |
| F10 (A3) | LOW | P17 | 24 | Deepfake dividend citation corrected EVENT-075 → EVENT-076 (verified: 075 = 2015 Paris Static) |
| F11 (A3) | LOW | P18 | 34 | Matrix corrections: Koi vs Compact UNAWARE → WARY; Garden bombings attributed to Ninth Bell, not Immersionists; Bell members accept Drowning as an outcome, not all already Drowned |
| F12 (A3) | LOW | P19 | 14, 31, 26, 29 | Liwanag/KNF retargeting: Aisha's team KNF-contracted (not BPF); Aisha removed from BPF mole hunt; Liwanag quiet desk framing; "best-informed weak man" → Liwanag; Arthur's employer location updated in 26. Legitimate Jakarta/BPF hooks untouched |
| F13 (A3) | LOW | P20 | 14 | CASE-003: Ledger froze Marchetti's escrow; Sahel protectors sold him; joint French/Ledger arrest pressure; surrender for calibrated (not fatal) depth-adjusted sentence |

### Unpatched findings

**None.** All 52 findings were patched. No finding was skipped. Merges (not skips): F-M5/A2-M-5 were patched once under P27 (Choir in elections covers both audits' asks; A2-M-5's voidability ask is addressed under P33); A1-F-L3's core (service-denominated payouts) was patched under P37 and merged with P42's sweep.

## v1.1 — 2026-09-19 — Phase 5 simulations: 9 HOLDS / 1 STRAINS / 0 BREAKS
- **Problem:** Sim E (rot-free T3+ capture) relied on analogy rather than canonical precedent.
- **Discovery:** Simulation Agent ran A–J against the v1.0-patched bible. 9 HOLDS; Sim E STRAINS ("no rot on a T3" tensions 02.III's CANON-LOCKED rot proportionality); 0 BREAKS. F/G honest survival verdicts: the bible gives Arthur leverage, not safety; a "Arthur dies here" branch is canon-supported. Vesper device (Sim D) does not break the F-M10 guardrail. Sim J defeats itself by canon (T5 rot melts sensors). L5-2 leaned on in F/G — confirmed stays a mystery.
- **Change:** 17 §17.4: added Case 4 ("The T3 that didn't rot," 2023) — membrane-darkness phase explains the clean capture; deepfake dividend + Veil + shelving contained it; the CANON line now names the Loudness-inducing-infohazard exception handled by the race doctrine.
- **Affected files:** 17_MEDIA_AND_INTERNET.md.
- **New risk:** None.
- **Status:** CANON. Phase 5 complete — entering Phase 6 final assembly.

## v1.2 — 2026-09-19 — [RELOCATION] Albion primary (user directive supersedes v0.4 regional selection)

- **Problem:** On 2026-09-19 the user corrected the setting direction: the primary country/city must be **Albion**, not the Philippines. v0.4 had selected the Philippines (COUNTRY-026) and Liwanag City (CITY-021) as the primary stage; the entire relocation-caused surface had to move to Albion while demoting — never deleting — Philippine canon.
- **Discovery:** The relocation touched geography, protagonist premise, state power, economy/factions, history/timeline, locations/facilities, and the full ID registry. Six parallel relocation writers (R-A..R-F) handled the files; the coordinator reconciled cross-file drift, regenerated the master document, and rebuilt the manifest.
- **Change:**
  1. **[RELOCATION] R-E (protagonist/premise/civilian life/romance):** `01_CORE_PREMISE.md`, `18_CIVILIAN_LIFE.md`, `29_PROTAGONIST_ANOMALY.md`, `30_POWER_HIERARCHY.md`, `32_ROMANCE_FRAMEWORK.md`. Reed Arthur (CHAR-001) keeps identity, age, Loud-but-unAttuned status, and ANOMALY-001 mechanics untouched; he is now an Indonesian SSW migrant worker, night-shift records clerk at NQA's **Ravenscroft** branch (HQ stays Jakarta), remitting to Tebet. Romance cast moved: Saitō/Nadia → NQA Ravenscroft, Kira → Ravenscroft, Aisha → GOV-006-contracted Ravenscroft Sweeper lead (recruited 2023), Pram → Ravenscroft 2026-09. Full log: `AUDIT/_RELOC-E.md`.
  2. **[RELOCATION] R-B (governments/military/law):** `06_GOVERNMENTS.md`, `13_MILITARY.md`, `14_LAW_ENFORCEMENT.md`. GOV-006 (Special Measures Division) expanded to full primary-agency depth (1949 origin, 1977 Quiet Night trauma, 1980s rebuild, 1995 recharter, Ravenscroft field office, Ravenshire PP friction, SSW blind spot, Blackwater Syndicate port understanding, unacknowledged SSW watchlist). KNF/GOV-014 demoted to secondary, profile retained. JSDF "Quiet Disaster Relief" doctrine added; street level moved to the Ravenshire quiet desk. Full log: `AUDIT/_RELOC-B.md`.
  3. **[RELOCATION] R-C (corporations/factions/relations):** `11_CORPORATIONS.md`, `12_FACTIONS.md`, `34_FACTION_RELATIONSHIPS.md`. NQA operational branch → Ravenscroft; new **CRIM-007 Blackwater Syndicate** (17-field profile); Lantern Bearers' Ravenscroft cell **"Akari"**; Ferrymen relay now Vladivostok–Ravenscroft; Ravenscroft chapters for Choir/Cartographers/Garden/Bell/Night Clerks/Koi/Alon Combine; matrix expanded. Full log: `AUDIT/_RELOC-C.md`.
  4. **[RELOCATION] R-A (geography/cities):** `20_GEOGRAPHY.md`, `21_CITIES.md`. §20.2 rewritten as "Why Albion seeps (primary narrative region)"; Luzon reframed as §20.2a (former primary lens, still top-decile). New **CITY-033 Ravenscroft City** mega-section: 22 districts × 11 fields (verified programmatically), city systems, faction footprint, atmosphere, 3 hooks. CITY-021 demoted to secondary metro, content preserved. Full log: `AUDIT/_RELOC-A.md`.
  5. **[RELOCATION] R-D (history/timeline/conflicts):** `24_HISTORY.md`, `25_TIMEmessaging app.md`, `31_CONFLICT_ENGINE.md`. EVENT-092 → Ravenscroft's Old Quay (ID/date/causal role preserved); EVENT-064/071 converted to Ravenscroft/Albion entries; timeline holds at **100 events**, RCs at **50** (10/10/10/10/10). Full log: `AUDIT/_RELOC-D.md`.
  6. **[RELOCATION] R-F (locations/facilities/registry):** `22_SUPERNATURAL_LOCATIONS.md`, `23_SECRET_FACILITIES.md`, `28_ANOMALIES.md`, `26_INFORMATION_CONTROL.md`, `10_RELIGIONS.md`, `35_CANON_DATABASE.md`, `00_INDEX.md`, all `DATABASE/` views. 8 LOC + 3 ZONE + 3 SITE conversions (SITE-010 → Station Kuroshio); registry mirrored row-for-row; master declares **412 IDs, no duplicates**. Full log: `AUDIT/_RELOC-F.md`.
  7. **[RELOCATION] Coordinator integration pass:** canonical Aisha phrasing fixed in `35_CANON_DATABASE.md` + `DATABASE/CHARACTERS.md` ("formerly KNF Liwanag, recruited 2023, GOV-006-contracted"); SITE-010 name synced in `34`; Quiet Acres Watch alignment in `23`; EVENT-060 recharter wording; EVENT-093 inquiry → Ravenscroft in `24`; RC-024 factions +CRIM-007/CRIM-006; RC-026 "SMD file"; `DATABASE/EVENTS.md` EVENT-064/071 titles; CITY-021 section scrubbed of 24 stale Arthur-in-Liwanag beats (reframed as secondary-stage mirrors); `37_FINAL_WORLD_BIBLE.md` regenerated; `38_MANIFEST.md` rebuilt with computed counts.
- **Reason:** Direct user override (2026-09-19): "harusnya settingnya jepang saja." Minimal-change rule: only geography and relocation-caused consequences changed; supernatural ontology, power system, classification, mystery layers, protagonist anomaly mechanics, and economic/secrecy rules untouched.
- **Affected files:** 28 files changed (01, 06, 10, 11, 12, 13, 14, 18, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32, 34, 35, 00, DATABASE/×6), 6 new audit fragments, 37_FINAL_WORLD_BIBLE.md + 38_MANIFEST.md regenerated.
- **New risk:** (1) Ravenscroft Bay and Luzon both read "~4× global mean" — primacy is distinguished by per-capita Place Seep registration canon + table placement; a future pass may want distinct figures. (2) GOV-006's unacknowledged SSW watchlist is fresh canon — needs forensic review in the audit phase. (3) Salonga/Liwanag vs Kuroda/Ravenscroft port-politics threads are intentionally distinct — future drafts must keep them separate.
- **Status:** APPLIED. Post-pass verification: 412 unique IDs, zero unresolvable ID references, zero broken file links, all counts hold (30 countries / 33 cities / 20 LOC / 10 ZONE / 10 SITE / 30 anomalies / 35 characters / 100 events / 50 RCs / 52 CGs).

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: FAC-001 (CRITICAL) — SUP-004 identity resolved per decision (a)

[WORLD AUDIT PATCH]

Issue: FAC-001 — SUP-004 is two irreconcilable factions (Code-bound PMC in 12 vs gray-market auctioneer in 6 files).

Previous Canon: 12_FACTIONS.md described the Red Ledger as a Code-bound mercenary company that refuses anomaly-trafficking contracts and returns fees with interest; six other files (14, 24, 25/EVENT-084/093, 29, 31/CG-043/CG-048, 35) described a gray-market auction house whose Factor brokers person-attached anomalies. The Code as written forbade the Factor's entire business.

Problem: The novel's central market thread (EVENT-093 → CG-043 → CG-048) was impossible under the PMC reading; the 12 profile made the Factor's conduct a Code violation with no acknowledgment.

New Canon: The Red Ledger is a private military company (public face) with a genuine Code-bound operating ethic AND an active gray-market brokerage — the Factor's (CHAR-027) black book — that the Partners do not acknowledge. The Code survives as the PMC division's real ethic and public brand; the black book brokers Code-violating deals (Rule auctions, provenance escrow, the Laggard inquiry) through three cutout layers. The hypocrisy is the business model — and plot fuel.

Reason: Coordinator decision (a), option 2: the gray-market identity is load-bearing for the market thread; rewriting one profile is cheaper than rewriting six files of staged beats. The 12 "black book" infrastructure already existed; the patch makes it the brokerage.

Affected Files: 12_FACTIONS.md (SUP-004 Type, Ideology, Secrets, Anomaly relationship; Resources force-size line also patched under FAC-002).

Secondary Consequences: 24_HISTORY.md, 25_TIMEmessaging app.md (EVENT-084/093), 29_PROTAGONIST_ANOMALY.md (§B.9), 31_CONFLICT_ENGINE.md (CG-043/048), 35_CANON_DATABASE.md (SUP-004 row) now need attribution language ("black-book brokerage," not "the Ledger") — covered in LAW-001's patch and the final 35 rebuild. ECON-009's arithmetic and FAC-002's handful rule resolved consistently via the force-size cut in the same profile.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: FAC-002 (CRITICAL) — five private Attuned forces vs handful CANON

[WORLD AUDIT PATCH]

Issue: FAC-002 — Five factions field private Attuned forces in violation of a CANON hard rule (08 §8.8: no private force above a handful of combat-licensed Attuned).

Previous Canon: SUP-004 ~2,400 operators (70% Attuned); SUP-001 Tideguard 300 Attuned; CORP-001 ~400 licensed Attuned; CRIM-002 ~80 Attuned enforcers; CRIM-006 ~40 Attuned malalim — all stated as forces, against the handful rule.

Problem: A CANON rule with five numbered exceptions; the largest exceeded most national threshold establishments. The rule or the rosters had to change.

New Canon: The rule stands; the rosters change. All five forces are restated as handful-scale *combat-licensed* cadres, with the rest reclassified as non-combat-licensed Attuned (medics, Lantern examiners, counselors, engineers, technicians) or unlicensed muscle. 08 gains an audit-clarification line: the Compact counts combat licenses, not Attuned heads.

Reason: Enforcing the rule (rather than amending a CANON-LOCKED-style economy hard rule) is the minimal change; the reclassification uses the bible's own license categories, so no new lore is invented. This also heals ECON-009 automatically ($900M funds a handful-scale elite cadre easily).

Affected Files: 12_FACTIONS.md (SUP-004 Resources, SUP-001 Members, CRIM-002 Resources, CRIM-006 Resources), 11_CORPORATIONS.md (CORP-001 Resources), 08_ECONOMY.md (§8.8 audit clarification).

Secondary Consequences: Any file citing the old force sizes as combat strength (34_FACTION_RELATIONSHIPS.md stance cells, 13_MILITARY.md force comparisons, 35_CANON_DATABASE.md rows) must be read as handful-scale cadres — flagged for the tier-end re-read. ECON-009 marked resolved-by-this-patch.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: LAW-001 (CRITICAL) — Factor's Laggard brokering recognized as trafficking; tether-succession vacuum named

[WORLD AUDIT PATCH]

Issue: LAW-001 — The Factor's Laggard brokering was an unrecognized trafficking crime under 14 §14.3(2); the real transfer mechanism sat outside every statute.

Previous Canon: EVENT-093 staged the Factor's circulated Laggard inquiry with no legal characterization; 14 §14.3(2) criminalized "sale" of person-attached anomalies as trafficking without noting the physics voids every such transaction; no file acknowledged that tether succession (death-proximity transfer, 29 §B.8) is legally invisible.

Problem: Three stacked failures — (1) the novel's inciting market transaction was trafficking in a person that no file treated as trafficking; (2) the trafficking statute misdescribed its own example (the Laggard cannot be transferred even in principle); (3) the real transfer mechanism sat in a complete legal vacuum.

New Canon: (1) EVENT-093's inquiry is now a deniable cutout-chain circulation, explicitly logged by the SMD's Quiet Desk as *attempted* trafficking; (2) 14 §14.3(2) now states the offense is necessarily *attempted* trafficking (physics voids the transaction, not the crime; completed harm prosecuted as crimes against the person); (3) the decision-(c) acknowledgment clause: non-severable tether succession is *legally invisible* — no title, no probate (CASE-004 excludes non-property), no license category, no recipient duty; the Division's C-A filing is an administrative convenience, not a legal regime; (4) CG-043's Pale Court "wedding gift" bid is now explicitly a person-trafficking contract by a rogue cadet branch; (5) EVENT-084/24-history attributions now read "the Factor's black-book brokerage," consistent with FAC-001's resolved identity.

Reason: Coordinator decisions (a) + (c): with the Ledger's black-book brokerage now canon, the Factor's conduct is Code-violating-by-design but still trafficking under Accords law — the files must recognize it as such rather than reframe it. The illegality-is-the-point option, combined with the cutout-chain insulation.

Affected Files: 25_TIMEmessaging app.md (EVENT-093, EVENT-084), 31_CONFLICT_ENGINE.md (CG-043), 14_LAW_ENFORCEMENT.md (§14.3(2)), 24_HISTORY.md (market-heats entry), 29_PROTAGONIST_ANOMALY.md (§B.9).

Secondary Consequences: 29 §B.8 unchanged (the transfer physics stands; the cross-reference now runs both ways). 35_CANON_DATABASE.md's EVENT-093/CG-043 rows need the trafficking characterization at the final rebuild. The Quiet Desk's logged-but-inactive posture is a deliberate plot engine (why no raid yet), not a gap.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: POWER-001/002/003/004/006 (HIGH) — classification per-case rule, decision (h)

[WORLD AUDIT PATCH]

Issue: POWER-001 (ANOMALY-006: ratified C-C vs D prose) · POWER-002 (ANOMALY-012: ratified C-D vs E prose) · POWER-003 (ANOMALY-013: ratified C-B vs D prose) · POWER-004 (ANOMALY-030: ratified C-C vs D prose) · POWER-006 (ANOMALY-004: ratified None vs Reactive prose).

Previous Canon: 05.5's Compact-ratified vectors disagreed with 28's field-catalog "Current status" prose on five anomalies; the JCC could not downgrade a ratified filing by posture revision, the Seismograph Authority's unfiled E proposal was stated as a status, and the Salt Garden entry misunderstood threat/containment orthogonality.

Problem: Five filings disagreed on which document governs; drafters could not tell whether the vector or the prose was authoritative, and the disagreements had budget/legal consequences (Compact funding, reporting triggers).

New Canon: Per decision (h) — the ratified vector is the *legal* filing (budgets, triggers, JCC posture); 28's prose is *field truth* the Classification Office hasn't reconciled. Each disputed filing now carries a Classification Office dispute note (05.3) instead of a silent conformity: ANOMALY-006 keeps C-C (the 2002 revision lowered posture, not classification); ANOMALY-012 keeps C-D (the 2022 E proposal is an unfiled dispute note); ANOMALY-013 keeps C-B ("cannot be vaulted" replaces "cannot be sealed"; the C axis measures the standing perimeter effort); ANOMALY-030 keeps C-C (the 1996 Charter was a rejected filing proposal — which also preserves the Compact funding the rotation protocol needs). ANOMALY-004: 28's field truth wins; 05.5 corrected from None to Reactive (one word; the stair counts back).

Reason: Decision (h) option 3, with the per-case calls made by the coordinator. The teaching examples (013's orthogonality) and the funding dependencies (030's rotation) survive; the disputes are now visible to drafters instead of being silent contradictions.

Affected Files: 05_ANOMALY_CLASSIFICATION.md (ANOMALY-004 vector + note), 28_ANOMALIES.md (ANOMALY-006/012/013/030 status prose + dispute notes).

Secondary Consequences: Verified: 33_MYSTERIES.md contains no Thursday Rain L4-2 entry (the issue's quoted text is stale against the current 33 — no patch needed). 35_CANON_DATABASE.md anomaly rows verified at final rebuild (registry table in 28 already carried the ratified vectors).

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: POWER-005 (HIGH) — Gilded Cradle Rule unified, decision (f)

[WORLD AUDIT PATCH]

Issue: POWER-005 — The Gilded Cradle had two incompatible Rules (28's Erosion-transfer cradle vs 30's "keeps what is placed in it" object).

Previous Canon: 28_ANOMALIES.md (ANOMALY-015) described the Erosion-transfer Rule — eleven uses, eleven children, Tribunal prohibition on a twelfth; 30_POWER_HIERARCHY.md's Scenario 3 described the old "keeps what is placed in it" Rule with a Tribunal "exception clause" for Sweepers. The two Rules generated different threats, containment, and stories.

Problem: One anomaly, two Rules; the scenario's exception-clause beat could not coexist with the prohibition-order Rule.

New Canon: 28's Erosion-transfer Rule survives (per decision (f) option 1). 30's Scenario 3 is rewritten around it: a Sweeper team responds to an unauthorized *twelfth* use — a desperate T4 rocking the cradle with a stolen infant — and wins by fighting the Rule's conditions (the Tribunal prohibition makes the use the crime; the transfer completes only when the rocker wakes; interrupt the rocking before the hour completes). The exception-clause beat dies; the twelfth-use scenario replaces it (arguably the better story).

Reason: Decision (f): 28's Rule is the richer, more load-bearing design (trolley problem, Tribunal order, four factions' positions). POWER-010's Fathom-reification is resolved consistently with the surviving Rule — the Compact's "Fathom-debt" language is bookkeeping for transferred Erosion (see the POWER-010 patch).

Affected Files: 30_POWER_HIERARCHY.md (Scenario 3).

Secondary Consequences: 35_CANON_DATABASE.md and DATABASE/ANOMALIES.md rows for ANOMALY-015 still read "keeps what is placed in it" — fixed at the final 35 rebuild (last in patch order). No other file cited the old Rule (verified by grep).

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: PROTAG-002 (HIGH) — dead-man's-switch escrow gets mechanism, limits, reliability model; Use-7 ceiling stated

[WORLD AUDIT PATCH]

Issue: PROTAG-002 — The dead-man's-switch escrow had no mechanism, no limits, and no reliability model; Use 7's shadow storage had no capacity ceiling or failure mode.

Previous Canon: 29's escrow was "copies of the clean recordings, keyed to multiple faction and civilian recipients (a Cartographers' waystation drop, a Night Clerks dead drop, a lawyer's sealed envelope), released automatically if he fails to check in" — no holder, no sync mechanism, no seizure model, no failure rate. Use 7 was "tiny capacity, total loss risk" with no numbers.

Problem: The novel's primary deterrent was a handwave; the auto-sync had no mechanism (Use 7 is shadow-storage, not shadow-transmission); rational actors discount threats they can verify as bluffs.

New Canon: The escrow now has (1) a named mechanism — lawyer-held sealed affidavit with a standing check-in-triggered instruction + dead-man's publication split across two mutually-ignorant Loud journalists (key halves) + Night Clerks dead drop (Cartographers' waystation as distrusted backup); (2) an auto-sync mechanism — new entries are photographed and dropped into Use-7 shadow-storage at deep lag, held out-of-phase until the weekly check-in handoff (the weekly cadence is *why* — the storage window is the lag window); (3) stated limits — court orders open the box (journalists' halves survive), seizure triggers the switch by design, the switch deters only rational actors; (4) a load-bearing reliability model — the Quiet Desk assesses ~30% failure odds and knows Arthur knows, so deterrence works through uncertainty; the switch being *tested* is a registered mid-series arc. Use 7's ceiling: ~one night of record per deep-lag session; failure mode = partial, read-only, edge-corrupted return (Ilsa's "unwrapped" mouse as the extreme case) — the archive degrades before it disappears, so Arthur never stores the only copy in the shadow.

Reason: Proposed solutions 1+2+3 combined: name the mechanism, make the unreliability load-bearing (uncertainty-as-deterrence is stronger than a perfect switch and gives the series a testable beat), state Use 7's ceiling and failure mode explicitly.

Affected Files: 29_PROTAGONIST_ANOMALY.md (Use 7 rules; the escrow CANON block).

Secondary Consequences: PROTAG-009 (LOW — the escrow deters only rational actors) is now cross-referenced in the escrow's limits; its patch states the residual Choir-facing risk explicitly. 35_CANON_DATABASE.md rows for Arthur's uses verified at final rebuild.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: ECON-001 (HIGH) — Meridian Re premium reconciled with sector total and economy size

[WORLD AUDIT PATCH]

Issue: ECON-001 — The anomaly-insurance line ($28–35B sector) was the same size as Meridian Re's implied premium pool; a reinsurer's book cannot rival the primary market it backstops.

Previous Canon: 08's sector table sized anomaly insurance at $28–35B; 11's CORP-004 showed ~$41B gross written premium, ~70% supernatural-attributable (~$28.7B) — effectively the whole sector.

Problem: Double-counting: Meridian Re's assumed book was sized as if it *were* the primary market rather than a cession of it.

New Canon: 08 8.2.1 now carries the CANON loss triangle — ~2.1M Quiet claims/year × ~$11k mean severity → ~$23B aggregate loss → ~$28–35B gross primary premium. Meridian Re assumes ~60% of the *risk* at ~18% average cession: ~$5B assumed supernatural premium, ~2–4% of the $140–200B supernatural-adjacent economy. Reinsurance's power is leverage (~$1 capital backstops ~$8 primary risk), not premium volume. CORP-004's revenue line is now "~$41B gross written premium (~$5B supernatural-attributable — the Quiet book; the ordinary book is diversification and camouflage)"; its Origin line is adjusted (its *purpose* has never been anything else — the ordinary book is the camouflage the purpose requires).

Reason: Proposed solution 1 — publish the loss triangle and back-solve the premium to ~2–4% of the economy.

Affected Files: 08_ECONOMY.md (8.2.1 loss triangle); 11_CORPORATIONS.md (CORP-004 revenue + origin).

Secondary Consequences: None beyond the numbers. The cat-bond leg of the issue's premise (cat-bond pricing implying ~6% yield) is moot: the relocation already removed the cat-bond example from canon; no patch needed there.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: ECON-002 (HIGH) — RC-026 payer waterfall published

[WORLD AUDIT PATCH]

Issue: ECON-002 — RC-026's "billions in reclamation financing" had no payer: no primary carrier, reinsurer, national guarantee, or Compact backstop named.

Previous Canon: RC-026's Setup named the dispute (place vs. event) but not who pays at any layer.

Problem: A recurring conflict generator whose stakes ("billions") float without a payer order is unusable in serialized plotting — the money's path is the plot.

New Canon: RC-026's Setup now carries the CANON payer waterfall: NQA's primary Quiet policy (service-denominated, rupiah bridge advances — 09) → Meridian Re's reinsurance pool (sounding-denominated) → Albion's national supernatural-guarantee facility (the yen leg — reclamation financing is domestic) → the Compact Catastrophe Backstop (the rupiah leg — NQA's Jakarta treaty pulls the Indonesian facility in when the British one is exhausted). The yen/rupiah split is why two treasuries, two regulators, and one Tribunal are in the room.

Reason: Proposed solution 1 — publish the full waterfall with the yen/rupiah split.

Affected Files: 31_CONFLICT_ENGINE.md (RC-026).

Secondary Consequences: None. The national-guarantee and Compact-backstop instruments are new canonical instruments introduced by this patch (the issue's proposed solution); 35/DATABASE rows to be added at final rebuild.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: ECON-003 (HIGH) — NQA rupiah payments reframed as bridge advances against service-denominated claims

[WORLD AUDIT PATCH]

Issue: ECON-003 — 08 says Quiet payouts are service-denominated (CANON); 09 said NQA "pays claims in rupiah" — a direct contradiction on the economy's load-bearing payment rule.

Previous Canon: 09_CURRENCIES.md 9.1: "Nusantara Quiet Assurance pays claims in rupiah."

Problem: Cash settlement of Quiet claims breaks the service-denomination anti-fraud design (08 8.2.1).

New Canon: 09 9.1 now says NQA *advances* rupiah against Quiet claims — a bridge loan, not the settlement: the claim settles in services, and the cash advance is booked as a recoverable draw against the service obligation. 08 8.2.1's Lantern-adjusted-exception line now names CORP-011's rupiah bridge advances as the exception's most common form, closing the 08↔09 loop.

Reason: Proposed solution 1 — reframe as a bridge advance against a service-denominated claim.

Affected Files: 09_CURRENCIES.md (9.1); 08_ECONOMY.md (8.2.1 cross-reference).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: ECON-004 (HIGH) — broker/underwriter-side fraud doctrine added

[WORLD AUDIT PATCH]

Issue: ECON-004 — The fraud model policed claimants only, while the bible's documented frauds (EVENT-084's auctioned Rule, the Factor's inquiry book, Meridian Re's Gray Market retrocession) are all broker/underwriter-side.

Previous Canon: 08 8.2.1's anti-fraud CANON block addressed claimant fraud only ("you cannot get rich faking a Seep exposure").

Problem: The economy's actual fraud surface (misfiled vectors, mispriced risk) was unpoliced in canon.

New Canon: 08 8.2.1 now carries the broker/underwriter-side fraud doctrine: the Classification Appeals Panel (CASE-001) as the venue for misfiled-vector fraud; license revocation and sounding-denominated Tribunal fines; Meridian Re's standing fraud loading in every treaty for misfiled-vector risk; under-classification named as the system's known weak point (05 5.3). Claimant fraud is shoplifting; broker fraud is arson, and the industry insures accordingly.

Reason: Proposed solution 1 — add broker/underwriter-side fraud doctrine to 08.

Affected Files: 08_ECONOMY.md (8.2.1).

Secondary Consequences: Cross-references CASE-001, 05 5.3, CORP-004 secret 3, EVENT-084 — all existing canon.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: ECON-005 (HIGH) — sounding numeraire anchored (already defined; cross-references closed)

[WORLD AUDIT PATCH]

Issue: ECON-005 — 08 priced Quiet obligations in service units while sounding rates were quoted in dollars, with no stated unit of account linking them.

Previous Canon: 09_CURRENCIES.md 9.2 already defines the numeraire — 1 SND = one standard T2-object containment-week, with a PROVISIONAL quarterly dollar reference band ($12–16k, 2024). The 17_MEDIA "dollar quotes" leg of the premise is stale: the relocation removed sounding mentions from 17 entirely.

Problem: 08's settlement paragraph pointed at 09 but never stated the definition inline, leaving the 08↔09 link implicit.

New Canon: 08's settlement paragraph (8.9-equivalent) now states the definition inline — 1 SND = one standard T2-object containment-week; the Ledger's quarterly $12–16k reference band — with the 09 9.2 pointer. No numeraire change; this is a cross-reference closure.

Reason: Proposed solution 1's substance (a stated numeraire) was already canon in 09.2; the patch closes the loop.

Affected Files: 08_ECONOMY.md (settlement paragraph).

Secondary Consequences: None.

Status: Patched (cross-reference closure). Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: ECON-006 (HIGH) — the fiat firewall conversion protocol published

[WORLD AUDIT PATCH]

Issue: ECON-006 — The fiat firewall (Quiet↔ordinary money boundary) had no leak protocol: Kurogane's sales into ordinary supply chains and the rupiah claim advances crossed it with no stated mechanism.

Previous Canon: 09 9.2 quarantined soundings inside the Ledger's closed system; the Quiet/ordinary *money* boundary had no protocol.

Problem: Every Quiet→ordinary flow was either illegal or unexplained — including licensed, load-bearing ones.

New Canon: New 09 §9.7 publishes the conversion protocol: (1) seven Ledger-licensed member banks (Argent Vault chief) as the only legal converters; (2) the SND quarterly reference band as the published rate anchor; (3) mandatory Ledger reporting, plus Seismograph Authority reporting above threshold; (4) licensed retail-edge crossings — ordinary payroll, NQA bridge advances, Kurogane's resonant-material sales (SMD-licensed conversion path, GOV-006); (5) unlicensed conversion prosecuted as supernatural financial crime under the Accords' market-manipulation provisions (the Gray Market's founding business — IND-006).

Reason: Proposed solution 1 — write the firewall protocol (licensed converters, published rate, mandatory reporting).

Affected Files: 09_CURRENCIES.md (new §9.7).

Secondary Consequences: Gives the legal footing for CORP-003's Ravenscroft sales (ECON-008's resonant-materials patch) and CORP-011's advances (ECON-003).

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: ECON-007 (HIGH) — the provenance premium gets its mechanism: the seal-chained registry

[WORLD AUDIT PATCH]

Issue: ECON-007 — The provenance premium was handwaved; no authentication mechanism justified why a documented Rule commands more than an undocumented one.

Previous Canon: 08 8.2.5 discussed auctions and the reversion clause; provenance had no mechanism.

Problem: Without an authentication mechanism, the auction economy's price dispersion is arbitrary.

New Canon: 08 8.2.5 now establishes the Ledger's (INTL-003) **seal-chained provenance registry**: auctioned anomalies' Rule documentation is Lantern-examined and seal-chained (each link bound to the last); CORP-008's authentication team are the registry's principal examiners; a seal-chained lot commands the premium because the chain is the only defense against Rule-drift in custody (CORP-008, secret 2). The registry is the most-forged and most-attacked database in the hidden world — a standing plot objective.

Reason: Proposed solution 1 — the Compact provenance registry (Lantern-examined, seal-chained); the registry becomes a plot target.

Affected Files: 08_ECONOMY.md (8.2.5).

Secondary Consequences: Cross-references INTL-003, CORP-008, 09 9.7 — all existing canon. 35/DATABASE row for the registry to be added at final rebuild.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: ECON-008 (HIGH) — Kurogane's grown materials capped as resonant, not anomalous

[WORLD AUDIT PATCH]

Issue: ECON-008 — Kurogane "grows" anomalous materials and sells them into ordinary supply chains, contradicting non-fungibility (02, II) and the firewall.

Previous Canon: 11 CORP-003, secret (2): Dr. Sato's division cultivates Object Seeps under controlled Tide pressure.

Problem: True Object Seeps with Rules cannot be fungible industrial feedstock.

New Canon: The grown materials are **resonant, not anomalous** — Tide-touched matter with useful properties, not true Object Seeps: no Rules, only *temper*. That is why they can be sold into ordinary supply chains under the licensed conversion path (09 9.7) instead of being vaulted. The legal department's terror is now precise: the resonant/anomalous line is thin and pressure-dependent, and the 2017 eversteel write-down is what happens when a batch crosses it.

Reason: Proposed solution 1 — cap as resonant materials (Tide-touched, not true anomalies).

Affected Files: 11_CORPORATIONS.md (CORP-003, secret 2).

Secondary Consequences: Consistent with 09 9.7's licensed retail-edge crossings. 35/DATABASE rows for CORP-003's grown materials verified at final rebuild.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: ECON-009 (HIGH) — resolved by FAC-002 (CRITICAL)

[WORLD AUDIT PATCH]

Issue: ECON-009 — If ~2,400 Red Ledger personnel are Attuned, the Attuned salary bands cannot price them.

Status: Resolved by FAC-002's CRITICAL patch (this changelog, v1.3): the Compact licenses count *combat* licenses, not total Attuned heads; the Ledger's ~2,400 are overwhelmingly support/noncombat Attuned, and 08 §8.8 now states the rule. No separate ECON-009 patch required.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: ECON-010 (HIGH) — the Ravenscroft berth waterfall published

[WORLD AUDIT PATCH]

Issue: ECON-010 — The berth concession (Quiet revenue from Ravenscroft's port) had no waterfall: no split between the port authority, the SMD, and the Blackwater Syndicate.

Previous Canon: 12 CRIM-007's Resources named berth control through licensed front firms; the money's path was unstated. (The issue's §8.10 premise is stale — the relocation's 08 has no berth-concession section; the gap is real in 12.)

Problem: The Blackwater Syndicate truce (06) had no price.

New Canon: CRIM-007's Resources now carry the CANON berth waterfall: pier/concession fees → the prefectural port authority (the ordinary, audited leg) → the SMD containment levy (the Quiet leg — the Ravenscroft understanding's price) → the federation's "cooperation" payments to berth-holders. The split is the control: the ordinary money is clean and visible; the Quiet money is where the truce lives.

Reason: Proposed solution 1 — publish the waterfall (concession fees → port authority → SMD containment levy → Blackwater Syndicate cooperation payments, Quiet/ordinary split).

Affected Files: 12_FACTIONS.md (CRIM-007 Resources).

Secondary Consequences: Prices the 06 Ravenscroft understanding. 35/DATABASE rows for the berth waterfall verified at final rebuild.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: ECON-011 (HIGH) — the seasoning rule: borrowed gold cannot clear

[WORLD AUDIT PATCH]

Issue: ECON-011 — Borrowed gold could clear T+2 inside the 72-hour reversion window; 09 9.5 documented the exploit but had no preventive rule.

Previous Canon: 09 9.5: "Financial settlement clears on T+2 at the fastest; by the time the receiving bank's assay finishes, the gold is gone" — deterrence by anecdote (the 2009 Zurich reversion).

Problem: Deterrence by anecdote is not a control; a fast assay beats T+2.

New Canon: New 09 §9.7 states the **seasoning rule (CANON)**: Quiet-adjacent physical deliveries are value-dated **T+5**, outside the 72-hour reversion window (02, I); delivery-versus-payment inside T+5 carries a mandatory **72-hour clawback** — if the matter reverts, the trade unwinds automatically, and the reversion leaves a forensic Tide-mark. Borrowed gold cannot clear, because the settlement system now assumes it is borrowed until the window closes.

Reason: Proposed solution 1 — the seasoning rule (T+5 / 72-hour clawback), combined with 2's forensic-signature deterrence (already canon via the Zurich reversion).

Affected Files: 09_CURRENCIES.md (§9.7).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: FAC-003 (HIGH) — CRIM-002 leadership: no patch needed (premise stale)

[WORLD AUDIT PATCH]

Issue: FAC-003 — CRIM-002's leadership: 12 named Salonga; the issue alleged 24 named "Alon Dimalanta" with a death date and 12 named the same man as a predecessor's contact.

Finding: The premise is stale against the relocated canon. "Alon Dimalanta" appears nowhere in 12 or 24; 24 names no CRIM-002 leadership at all; the "2022 Ravenscroft pier agreement" appears nowhere in 24/25/12. 12's CRIM-002 profile names "Kapitan" Rudy Salonga (leadership: the Kapitan plus mga pangulo; Lena Salonga the open-secret heir) with no contradiction anywhere in canon.

New Canon: None — 12's Salonga leadership stands uncontradicted.

Reason: No contradiction exists to reconcile; patching would invent one.

Affected Files: None.

Status: Closed — resolved by the Albion relocation (worker reconciliation already in canon). Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: FAC-004 (HIGH) — Halcyon Analytics named as the precog desk's cover story

[WORLD AUDIT PATCH]

Issue: FAC-004 — Halcyon's corporate structure: the issue alleged 12 described "Halcyon Analytics" as a separate org while 11 showed one company.

Finding: The separate-org premise is stale — "Halcyon Analytics" appears nowhere in current 11 or 12; CORP-001 is already one company.

New Canon: 11 CORP-001's Resources now name the **Halcyon Analytics** division explicitly — one company, one division, and the cover story's name for the precog desk (the 1973 Oil Seep's T3 analyst, 24_HISTORY.md, sat at an early version of it). This locks the decided resolution so no future drafter can re-split it.

Reason: Decision: Halcyon is one company; its analytics division is the cover story's name for the precog desk.

Affected Files: 11_CORPORATIONS.md (CORP-001 Resources).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: FAC-005 (HIGH) — Santara analyst: no patch needed (premise stale)

[WORLD AUDIT PATCH]

Issue: FAC-005 — Santara's analyst: the issue alleged 24 named an analyst "Budi Santoso" with a 2017 detection while 11's CORP-012 claimed total unawareness.

Finding: The premise is stale. No "Budi Santoso" appears in 24 or anywhere in canon; 11's CORP-012 profile is already the decided resolution — "Anomaly relationship: **none — and that is load-bearing**" with the CANON block stating CORP-012 is completely unaware of the hidden world (the control group that proves the masquerade works). The statistical-noise detection beat the issue proposed is subsumed: Santara's trucks drove through Seep perimeters and "filed it under weather" — detection without comprehension, which is the Veil Reflex working as designed.

New Canon: None.

Reason: The relocation already implemented the decided outcome (anonymous, unaware Santara).

Affected Files: None.

Status: Closed — resolved by the Albion relocation. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: FAC-006 (HIGH) — REL-001's name: no patch needed (premise stale)

[WORLD AUDIT PATCH]

Issue: FAC-006 — REL-001's founder: the issue alleged 10's founder canon vs. 29's "Rin."

Finding: The premise is stale. No "Rin" appears in 29; 10's REL-001 (Order of the Veil) names no founder — it is a Vatican dicastery founded in its modern form in 1951, inheriting four centuries of predecessor archives. There is no founder to contradict.

New Canon: None.

Reason: No contradiction exists.

Affected Files: None.

Status: Closed — resolved by the Albion relocation. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: FAC-007 (HIGH) — faction registry reconciled: 22 profiles confirmed, namespaces reserved, REL-008 profiled

[WORLD AUDIT PATCH]

Issue: FAC-007 — Faction count mismatch: 12's table claimed twelve factions while 34 counted 22 profiled.

Previous Canon: 12's registry pointer tables were complete but the registry carried no cap statement; REL-008 (Church of the Open Eye) had staged beats (RC-019, RC-030, 21_CITIES.md, 34) but no profile — referenced from the database only.

New Canon: (1) 12 now carries the CANON registry cap: **22 fully profiled factions** (SUP-001..010, CRIM-001..007, IND-001..005); unused namespaces (no SUP-011+, no CRIM-008+, IND-008/009 unclaimed) are **reserved, not empty** — nothing new may be filed under them without a registry amendment. (2) 10 now carries the short **REL-008 — Church of the Open Eye** profile: Seep-venerating revelationists (founded 1989, Liwanag), Tide-marks as scripture, witness books, open-eye vigils, fiesta-tide processions (RC-019), CORP-006 content partnership (RC-030), doctrine war with REL-001, revelationist convergence with SUP-007 (34), watched by the KNF. (3) 12's REL pointer table gains the REL-008 row; 10's landscape table gains the REL-008 row.

Reason: Decision (b) — reduce to 22 profiled factions, reserve unused namespaces, write the short REL-008 profile.

Affected Files: 12_FACTIONS.md (registry cap; REL table); 10_RELIGIONS.md (REL-008 profile; landscape table).

Secondary Consequences: 35_CANON_DATABASE.md's REL-008 row (currently a bare database entry) to be expanded at final rebuild. No new namespaces opened.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: FAC-008 (HIGH) — KNF mandate: no patch needed (premise stale)

[WORLD AUDIT PATCH]

Issue: FAC-008 — GOV-014's mandate: the issue alleged 06 described the KNF as "the anti-smuggling unit."

Finding: The premise is stale. 06's GOV-014 profile already describes the KNF as a full civilian threshold bureau (Kawanihan ng Fenomena, under the Office of the President, 1949 Accords signatory desk, rechartered 2001) — with the anti-smuggling *unit* correctly placed *inside* it (Internal conflicts: "the anti-smuggling unit vs. the Daungan understanding"). 12's CRIM-006 references to "the KNF's anti-smuggling unit" are consistent with this.

New Canon: None.

Reason: The relocation already implemented the decided outcome (full threshold agency).

Affected Files: None.

Status: Closed — resolved by the Albion relocation. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: FAC-009 (HIGH) — SMD internal units reconciled: three arms named

[WORLD AUDIT PATCH]

Issue: FAC-009 — GOV-006's internal units: the issue alleged 06 named three divisions plus a "Night Section" while 14 named four different units.

Finding: The contradiction premise is stale — neither file currently lists SMD internal units. 06's Leadership line already named three deputies (operations, Census administration, liaison); 14's SMD material is street-level (quiet desks, field offices, liaison officers) with no conflicting roster.

New Canon: 06 GOV-006 now formalizes the three deputies' arms — **Operations, Census Administration, Liaison** — as the Division's org chart, and states that everything the street sees reports through one of the three. 14 14.1 now carries the cross-reference: the org-chart view is in 06 (GOV-006); 14 is the street-level view of the same body. The issue's proposed solution 1 (org-chart vs. street-level reconciliation) is implemented structurally.

Reason: Proposed solution 1 — reconcile by making 14's roster a street-level view of 06's org-chart view.

Affected Files: 06_GOVERNMENTS.md (GOV-006 Leadership); 14_LAW_ENFORCEMENT.md (14.1 cross-reference).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: FAC-010 (HIGH) — GOV-003's posture: no patch needed (premise stale)

[WORLD AUDIT PATCH]

Issue: FAC-010 — GOV-003's posture: the issue alleged 06's Russia section had Department 12 as FSB-adjacent while 24's timeline named GRU Unit 29155.

Finding: The premise is stale. 24 names no "Unit 29155" anywhere in current canon. 06's GOV-003 profile is internally consistent: Department 12 (Отдел-12), under the General Staff, with FSB liaison — military-run, the only great-power agency formally inside the armed forces — led by a GRU-background general (Volkov, CHAR-004).

New Canon: None.

Reason: No contradiction exists.

Affected Files: None.

Status: Closed — resolved by the Albion relocation. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: GEO-001 (HIGH) — SITE-009 location: no patch needed (premise stale)

[WORLD AUDIT PATCH]

Issue: GEO-001 — SITE-009's location: the issue alleged 22's facility profile placed SITE-009 "on the Kola Peninsula."

Finding: The premise is stale. 22 carries no SITE-009 profile; 23's SITE-009 is "Isla Cuarentena (Liwanag Bay, Philippines)"; 35's SITE-009 row reads "Isla Cuarentena (Liwanag Bay)" — full agreement. No "Kola" appears anywhere in canon. The Red Ledger's Kola anchorage is a separate unnumbered facility and was never SITE-009.

New Canon: None.

Reason: No contradiction exists.

Affected Files: None.

Status: Closed — resolved by the Albion relocation. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: HIST-001 (HIGH) — the 100 events are notable events, not all events; era map published

[WORLD AUDIT PATCH]

Issue: HIST-001 — 24's seven named eras vs 25's 100 events without era tags.

Previous Canon: 25's header described the master event ledger without stating the 100 events' relationship to 24's periodization or to the unlisted total.

New Canon: 25's header now carries the CANON era map — I: EVENT-001–003 · II: EVENT-004–033 · III: EVENT-022–034 · IV: EVENT-034–047 · V: EVENT-047–049 · VI: EVENT-050–079 · VII: EVENT-079–100 — with two load-bearing caveats: (1) the 100 are *notable* events, not *all* events (the complete record would be ten thousand entries and mostly weather); (2) the eras overlap by design — historiographic lenses, not partitions (Eras II and III both cover 1908–1948, from opposite ends).

Reason: Proposed solution — align the seven eras with event-count language and state the notable-not-all caveat.

Affected Files: 25_TIMEmessaging app.md (header).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: HIST-002 (HIGH) — queued for final database rebuild

[WORLD AUDIT PATCH]

Issue: HIST-002 — 35's rebuilt rows vs 24's narrative (database/narrative drift).

Disposition: This issue is addressed by the final 35_CANON_DATABASE.md/DATABASE rebuild, which runs after all canon source patches (per the audit task protocol: database work last). The rebuild will regenerate every row from the patched sources, including the REL-008 expansion, the registry cap, the COUNTRY-001/005 swap, and decision (p)'s ninth-site row fix.

Status: Queued — resolved at final rebuild (v1.3 verification).

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: HIST-003 (HIGH) — COUNTRY-001 becomes Albion; the US renumbered to COUNTRY-005

[WORLD AUDIT PATCH]

Issue: HIST-003 — 24's CANON relocation update named "JAPAN (COUNTRY-001)" while the registry (06, 35, DATABASE/COUNTRIES.md) named COUNTRY-001 as the United States — a numbering collision from the relocation. (35's own relocation note already said "COUNTRY-001 now Primary country" — the intent was recorded but the rows were never swapped.)

Previous Canon: COUNTRY-001 = United States; COUNTRY-005 = Albion; 24:149 contradicted the registry.

New Canon: **COUNTRY-001 = Albion** (primary country; SMD GOV-006; Ravenscroft City CITY-033); **COUNTRY-005 = United States** (BTA GOV-001). Swapped in 06_GOVERNMENTS.md, 35_CANON_DATABASE.md, DATABASE/COUNTRIES.md, 00_INDEX.md, 01_CORE_PREMISE.md, 29_PROTAGONIST_ANOMALY.md. 24_HISTORY.md:149 ("JAPAN (COUNTRY-001)") was already the target state and needed no change. Range headers (COUNTRY-001..030) untouched; GOV IDs unchanged (GOV-001 stays BTA, GOV-006 stays SMD).

Reason: Proposed solution — COUNTRY-001 must become Albion, consistent with the Albion-primary directive; renumber the US accordingly.

Affected Files: 06_GOVERNMENTS.md; 35_CANON_DATABASE.md; DATABASE/COUNTRIES.md; 00_INDEX.md; 01_CORE_PREMISE.md; 29_PROTAGONIST_ANOMALY.md.

Secondary Consequences: DATABASE/COUNTRIES.md is regenerated from 35 at the final rebuild; the swap is recorded here so the rebuild preserves it. No other ID namespaces affected.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: SOC-001 (HIGH) — the threshold-adjacent service class named and owned

[WORLD AUDIT PATCH]

Issue: SOC-001 — 19's class taxonomy vs 18's daily-life texture: the threshold-adjacent service class (drivers, fixers, cleaners) was gestured at by both files but owned by neither.

Previous Canon: 19's Ordinary civilians "staff its camouflage (every mundane job inside a supernatural company)"; 18's dorm class touched the supernatural as "employees (the night shift)" — no named stratum.

New Canon: 19.1 now names **the threshold-adjacent** as a class: drivers, cleaners, fixers, dispatchers, Kestrel ground crews, the Night Clerks' day-job selves — *proximity without clearance*, the hidden world's best-informed and worst-paid witnesses; the masquerade's labor shortage lives here. Arthur starts here. 18.5's dorm class now cross-references it (the employed layer of the dorm class is the threshold-adjacent stratum). 19 remains the structural taxonomy; 18.5 remains the daily-life texture — the bridge is now explicit both ways.

Reason: Proposed solution — align the taxonomies and add the missing middle both files gestured at.

Affected Files: 19_SOCIAL_CLASSES.md (new 19.1 subsection); 18_CIVILIAN_LIFE.md (18.5 cross-reference).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: NAR-001 (HIGH) — Arthur has never *knowingly* met another Loud adult

[WORLD AUDIT PATCH]

Issue: NAR-001 — Arthur's Loud isolation vs the Night Clerks (disproportionately Loud), NQA's deliberate Loud hiring, and Yusuf (Loud, known to Arthur).

Previous Canon: 29 established Arthur as Loud without addressing how he could work inside Loud-dense institutions and know a Loud man without the fact registering.

New Canon: 29's identity section now carries the CANON qualifier: Arthur has never *knowingly* met another Loud adult — the *category*, not the people. He grew up around rememberers (Yusuf's logbook, his mother's silences, half the Night Clerks' cell) without ever having the word; Loudness was a private weather, not a population. The Night Clerks are the first people with a name for what he is — and he still doesn't know how many of them qualify.

Reason: Proposed solution — qualify as "never *knowingly* met": he works alongside Loud people constantly without knowing they're Loud, and neither do they.

Affected Files: 29_PROTAGONIST_ANOMALY.md (identity section).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: NAR-002 (HIGH) — the original/copy chain: KNF holds the original, SMD holds a copy

[WORLD AUDIT PATCH]

Issue: NAR-002 — 06's KNF file on Arthur vs the SMD's file: which agency holds the original?

Previous Canon: 06 GOV-014 held "the thin file" (EVENT-092 Sweeper report); 06 GOV-006 held Arthur's employer-filed Census record — with no stated original/copy relationship.

New Canon: The KNF's thin file is the **original** government record on Reed Arthur (opened in Liwanag, 2024 — the EVENT-092 Sweeper lead's report). The SMD's Ravenscroft Census record is a *copy* — employer-filed, thinner than the original — and the Division has never seen the Sweeper report itself, because underfunded bureaus share files *upward*, not sideways. The asymmetry is plot-load-bearing: the agency with jurisdiction doesn't know what the agency of origin wrote.

Reason: Proposed solution — KNF holds the original (Liwanag origin), SMD holds a copy (Ravenscroft jurisdiction).

Affected Files: 06_GOVERNMENTS.md (GOV-014 secrets; GOV-006 Census passage).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: SER-001 (HIGH) — the Uses 13+ physical generative principle

[WORLD AUDIT PATCH]

Issue: SER-001 — The observe → hypothesize → test → pay sequence as Arthur's method vs 04's discovery grammar (premise stale: neither the sequence nor a 04 discovery grammar exists in current canon).

Previous Canon: 29 B.11's header already stated each use is "discovered through observation, never granted by revelation" and "paid for" — but stated nothing about uses beyond the twelve.

New Canon: 29 B.11 now carries the CANON **generative principle (Uses 13+)**: the twelve are the *documented* ladder, not the *complete* ladder; any use beyond them must be generated the same way — **observe, hypothesize, test at the smallest falsifying scale, pay** — never granted by revelation, never whispered by the entity, never free. Serialization rule: a Use 13+ that skips a step is a continuity error, not a power-up.

Reason: Decision (l) — discovery grammar becomes the Uses 13+ physical generative principle.

Affected Files: 29_PROTAGONIST_ANOMALY.md (B.11).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: REL-001 (HIGH) — two-stage founding dates made explicit (Veil Office → Ordo Veli)

[WORLD AUDIT PATCH]

Issue: REL-001 — 10's founding dates vs 24's timeline.

Previous Canon: 10 already carried the two-stage form ("founded in its modern form in 1951, inheriting four centuries of predecessor archives"); 24 named the predecessor ("the Veil Office — the direct institutional ancestor") — but neither file named the other stage.

New Canon: 10's REL-001 profile now names the predecessor stage explicitly: "inheriting the four-century archive of its predecessor, the Veil Office (24_HISTORY.md)." The two stages are now cross-cited both ways: Veil Office (slow accretion from the 1348 papal clerks) → *Ordo Veli* (1951 modern charter).

Reason: Proposed solution — two-stage founding dates.

Affected Files: 10_RELIGIONS.md (REL-001).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: REL-002 (HIGH) — Attuned clergy reconciled: no ordination, lay profession only

[WORLD AUDIT PATCH]

Issue: REL-002 — Attuned clergy vs restrictions: 10's REL-001 profile said "a dozen Attuned in holy orders" while 24's timeline said "no Attuned may hold holy orders in the Order of the Veil — a rule still enforced" (35's REL-001 row sided with the prohibition: "no Attuned in holy orders").

Previous Canon: Direct contradiction — 10 vs 24 (+35).

New Canon: The 1378 prohibition is on Attuned **ordination** (priesthood), still enforced — and enforced on the dozen first. The dozen Attuned in the modern Order are professed in its *lay* religious orders (brothers and sisters, never priests): "holy orders" in 10's broad sense, never sacramental office. 24's line now reads "no Attuned may be *ordained*"; 10's profile now reads "a dozen Attuned professed in the Order's lay religious orders (brothers and sisters, never ordained)." Both statements are now true simultaneously.

Reason: Proposed solution — reconcile by narrowing the prohibition to ordination and the exception to lay profession.

Affected Files: 10_RELIGIONS.md (REL-001); 24_HISTORY.md (1378 Schism passage).

Secondary Consequences: 35's REL-001 row ("no Attuned in holy orders") to be refined at the final rebuild ("no Attuned ordained; dozen Attuned in lay profession").

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: REL-003 (HIGH) — Majelis founding date: no patch needed (premise stale)

[WORLD AUDIT PATCH]

Issue: REL-003 — the issue alleged a founding-date conflict for the Majelis Fenomena.

Finding: No competing date exists in canon. 10's REL-003 profile ("convened in Jakarta in 1987") stands alone — 24, 25, 34, and 35 carry no other founding date for the Majelis.

New Canon: None.

Reason: No contradiction exists.

Affected Files: None.

Status: Closed — no contradiction found. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: POWER-006 (MEDIUM) — disposition: already patched under HIGH

[WORLD AUDIT PATCH]

Issue: POWER-006 — ANOMALY-004 INTEL `None` vs `Reactive`.

Disposition: Resolved in the HIGH tier as part of the combined entry "POWER-001/002/003/004/006 (HIGH)" — `Reactive` (the stair counts back) won; 05 corrected. No further action.

Status: Closed — see HIGH-tier entry. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: POWER-007 (MEDIUM) — person-bound filing policy: the Laggard's C-A is policy, not corruption

[WORLD AUDIT PATCH]

Issue: POWER-007 — The Laggard is filed `C-A` but reads as `C-D` (motivated under-classification to dodge the Compact's 72-hour reporting trigger?).

Previous Canon: 05 filed ANOMALY-001 as `MV-T1/C-A/—/Local/Unknown` with no stated reason for the A-class effort mismatch.

New Canon: New CANON policy in 05 Axis 2 — **person-bound filings**: where the anomaly is bound to a living person, containment class describes the *relationship*, not the object (a person cannot be "uncontained"); person-bound anomalies file **C-A by default** with D-equivalent surveillance. The Laggard's C-A is this policy, not a cover-up: BPF Jakarta files it A, staffs it D, and the standing 5-year re-audit trigger exists precisely because classification and effort disagree. Plus **old-notation guidance**: pre-Compact/pre-1962 single-letter grades in old files are approximate and must be re-filed before citing.

Reason: Decision (e) — keep the Laggard C-A; add the Classification Office person-bound filing policy and old-notation guidance.

Affected Files: 05_ANOMALY_CLASSIFICATION.md (Axis 2 CANON note).

Secondary Consequences: The same policy covers any future person-bound anomaly (e.g., Arthur-adjacent filings).

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: POWER-008 (MEDIUM) — the Lullaby gets a citable Tribunal ruling: suggestion seeding at memetic scale

[WORLD AUDIT PATCH]

Issue: POWER-008 — The Ward Six Lullaby's behavioral compulsion strains "no direct mind control" (02 CANON-LOCKED).

Previous Canon: 28 described the Lullaby's compulsion and memory degradation with no stated legal/physical boundary.

New Canon: 28's ANOMALY-007 profile now carries the CANON Tribunal ruling (*Quiet Desk v. Ward Six Propagation*, 2021): the Lullaby is the CANON's boundary case and falls on the lawful side — **suggestion seeding at memetic scale**, not direct mind control. Evidence: resistance is documented (refusers exist — the V flag exists because propagation is *resisted*, not automatic); the singer-side memory degradation is the **backlash mechanism** of 02's rule, exactly as seeding doctrine predicts. The ruling is citable by examiners.

Reason: Proposed solution 2 — a Tribunal ruling on which side the boundary case falls (a ruling is citable; a handwave isn't).

Affected Files: 28_ANOMALIES.md (ANOMALY-007).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: POWER-009 (MEDIUM) — the Static Saint inflicts *resonance damage*, not Erosion

[WORLD AUDIT PATCH]

Issue: POWER-009 — The Static Saint "accrues Erosion at ~1 Fathom per month without channeling" contradicts 04's Erosion doctrine (Erosion is the wear-cost of *channeling*).

Previous Canon: 28 used "Erosion" for the Saint's effect.

New Canon: Classification Office correction (2022) in 28's ANOMALY-012 profile: the Saint inflicts **resonance damage** — externally imposed Veil-wear, measured on the Fathom scale but ontologically distinct from channeling Erosion. Legal consequence: Erosion is self-incurred and non-compensable; resonance damage is *inflicted*, which is why the file is I-flagged and victims' estates are eligible for Meridian Re coverage that true Erosion never qualifies for. The field shorthand "Fathom-debt" is an accounting metaphor (cross-ref the Gilded Cradle, ANOMALY-015).

Reason: Proposed solution 1 — keep the effect, name it correctly; reserve "Erosion" for channeling wear.

Affected Files: 28_ANOMALIES.md (ANOMALY-012).

Secondary Consequences: Any other file using "Erosion" for externally inflicted wear should be rechecked at final rebuild (the Meridian Re paragraph in 08 refers to "supernatural losses" generally — no conflict).

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: POWER-010 (MEDIUM) — Gilded Cradle ontology: Erosion transfers, "Fathom-debts" is the accounting metaphor

[WORLD AUDIT PATCH]

Issue: POWER-010 — The Gilded Cradle reifies Fathoms as transferable objects ("eleven Fathom-debts the world is carrying") vs 04's Fathoms-as-measurement-scale.

Previous Canon: 28's ANOMALY-015 Rule described infants waking "carrying the rocker's Fathoms."

New Canon: Classification Office correction (2022) in 28's ANOMALY-015 profile: the cradle transfers *Erosion* (physical Veil-wear), not Fathoms; "Fathom-debts" is the Compact's accounting metaphor. No Fathom-debt ledger exists anywhere — only damaged Veil, moved from bearer to bearer.

Reason: Proposed solution 1 — clarify the ontology; the debt language is bureaucratic, not physical.

Affected Files: 28_ANOMALIES.md (ANOMALY-015).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: POWER-011 (MEDIUM) — T6 (pre-Drowning) doctrine written

[WORLD AUDIT PATCH]

Issue: POWER-011 — The T6 band (81–100 Fathoms, pre-Drowning) had no stated containment or doctrine.

Previous Canon: 04 defined T6 as a measurement band only.

New Canon: New §4.8 in 04 — **pre-Drowning doctrine**: mandatory relief rotation ("garden leave"); the **Drowning watch** (two-person Lantern detail, continuous Seismograph flagging, standing Sweeper standby — the watch is for everyone *near* the subject, not the subject); at 95+ Fathoms, warded-facility transfer (SITE-009's Liwanag wing handles the Pacific caseload). No doctrine for 100 — the Drowning *is* the doctrine. Three confirmed Worldtides live past 70 Fathoms under permanent observation; none has come back down.

Reason: Proposed solution 1 — write the T6 doctrine.

Affected Files: 04_POWER_SYSTEM.md (new §4.8).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: PROTAG-001 (MEDIUM) — the ratchet ruler, published and non-binding

[WORLD AUDIT PATCH]

Issue: PROTAG-001 — The ratchet math is unbounded and self-referential (no stated cap-per-season; the 10s ceiling doing structural work it can't do forever).

Previous Canon: 29 B.6 stated only "extreme use adds permanent fractions of a second" (Ilsa: 3.0 → 3.4s over seven years); the quoted logged/unlogged increments and the serialization-guide file did not exist in current canon.

New Canon: New CANON-adjacent **drafter's ruler (non-binding)** in 29 B.6: a *logged* extreme use deepens the lag ~0.25s; an *unlogged* one ~1s; the per-season ratchet budget is ~1–1.5s, so the 10s ceiling stays a series-level mystery. The story may spend the budget differently but may not spend *more* without an explicit author decision. Arthur never sees these numbers — diegetically he knows only that the lag is lengthening and the journal is missing its last page.

Reason: Decision (k) — publish the nonbinding ratchet ruler.

Affected Files: 29_PROTAGONIST_ANOMALY.md (B.6).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: PROTAG-003 (MEDIUM) — the flare's burn is permanent and CANON-locked

[WORLD AUDIT PATCH]

Issue: PROTAG-003 — The flare's point-of-no-return needs a permanent consequence (the issue's reinstatement mechanics were stale — no such mechanics exist in current canon).

Previous Canon: 29 Use 12: "A flare he can't unfire" / "everyone comes. Everyone." — implied permanence, never locked.

New Canon: New CANON under Use 12: the flare is a point of no return and the burn is permanent — the T1-curiosity cover identity is gone forever, the filing is ash, every Lantern-sensitive for kilometers knows what he is; no reinstatement, no re-filing, no quiet return to the records desk. The cover story must be rebuilt from scratch, and the rebuild *is* the next season's engine.

Reason: Proposed solution 1 — make the burn permanent; the fake-climax risk is closed.

Affected Files: 29_PROTAGONIST_ANOMALY.md (Use 12).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: PROTAG-004 (MEDIUM) — no patch needed (premise stale)

[WORLD AUDIT PATCH]

Issue: PROTAG-004 — The sterile-kill denial creates an unsatisfying immunity (citing a §C sterile-kill doctrine).

Finding: No sterile-kill doctrine and no sterile-kill denial exist anywhere in canon. Current 29 states the opposite: "A bullet still works." Arthur survives by observation and cunning, "without plot armor" — the physics grants no immunity.

New Canon: None.

Reason: No contradiction exists.

Affected Files: None.

Status: Closed — no such doctrine found. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: PROTAG-005 (MEDIUM) — the stealth-calculus ruler published (non-binding)

[WORLD AUDIT PATCH]

Issue: PROTAG-005 — Detection radius per use-tier unstated; the Seismograph's "large" never quantified against Arthur's use-tiers.

Previous Canon: 29 stated only that deep use is "visible to Lantern-sensitives across kilometers and to instruments"; 07's Seismograph floor (channeling above ~T3) did not map to the Laggard's non-channeling uses.

New Canon: New CANON-adjacent **drafter's ruler (non-binding)** in 29 (under Use 12): the Laggard is not channeling, so the Seismograph's T3-floor applies to *pressure displacement*, not tier output. Planning guideline: Uses 1–5 — below instrument threshold (Lantern-visible within meters); Uses 6–9 — Lantern-visible across kilometers, metro-level instrument flags; Use 10 — instruments see nothing, the *artifact* is the signature; Use 11 — invisible by definition; Use 12 — every Lantern-sensitive for kilometers, Seismograph pressure spike. Arthur knows none of these numbers — his doctrine is *assume the worst and stay shallow*.

Reason: Proposed solution 1 — publish the radius table as a drafter's ruler.

Affected Files: 29_PROTAGONIST_ANOMALY.md.

Secondary Consequences: 26.4's new Snowden paragraph cross-references this ruler.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: PROTAG-006 (MEDIUM) — the mirror beat's missing trace is canonical secrecy

[WORLD AUDIT PATCH]

Issue: PROTAG-006 — The smiling mirror reflection is documented but appears in no registry — unregistered anomaly or continuity error?

Previous Canon: 29 documented the mirror beat (Ilsa's journals; Arthur's two sightings) with no stated reason for the missing institutional trace.

New Canon: New CANON in 29 §A: the mirror beat has no institutional trace *deliberately* — Ilsa documented it only in her private, unfiled journals; Arthur has told no one. He treats the smiling reflection as the one thing he will not put in writing, because filed things get examined. The absence of a registry entry is the beat's secrecy made canonical — and the day someone else mentions the mirror is the day he knows he's been read.

Reason: Proposed solution 2 — explain the gap; the absence of the trace *is* the trace.

Affected Files: 29_PROTAGONIST_ANOMALY.md (§A).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: PROTAG-007 (MEDIUM) — the rot-immunity boundary stated

[WORLD AUDIT PATCH]

Issue: PROTAG-007 — Use-10's rot-immunity boundary unstated (deep-lag/high-pressure replay is the highest-intensity event class; is Use 10 a tool or a WMD?).

Previous Canon: 29 Use 10: "recordings of the shadow do not rot" — no boundary.

New Canon: New CANON under Use 10: immunity is a property of the *medium* (Membrane-darkness), with a capacity — it holds up to ~3 hours lag-depth (Ilsa's documented maximum) and T4-equivalent event pressure; beyond that depth-pressure product, rot applies normally. Inside the boundary, a clean record of anything he can survive witnessing; past it, a rotting bomb. He has never tested the boundary — Ilsa's journals mark it PROVISIONAL, margin note *"don't."*

Reason: Proposed solution 1 — state the boundary the author can plan around.

Affected Files: 29_PROTAGONIST_ANOMALY.md (Use 10).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: PROTAG-008 (MEDIUM) — the anti-Snowden regime is already working on him

[WORLD AUDIT PATCH]

Issue: PROTAG-008 — Use 10 is the walking Snowden the whole information-control doctrine exists to prevent; why does the regime tolerate him?

Previous Canon: 26.4's Snowden stress-test listed three failed leakers with no Arthur reconciliation.

New Canon: New CANON in 26.4: the doctrine has not failed to notice Use 10 — it has *responded* per doctrine: no strike (martyrs leak louder than the living), but the Quiet Desk's human-intelligence interest — recruitment, surveillance, the escrow's cold arithmetic. The instruments never saw the recordings (Use 10 is below the Seismograph's threshold); the *people* saw the clerk. And the escrow inverts the doctrine's math: seizing him triggers the dead-man's switch, so the system that digests leakers by outliving them cannot outlive him by seizing him. The regime's answer to the walking Snowden is the oldest one — *hire him before he publishes.*

Reason: Proposed solution 2 — the Quiet Desk's interest *is* the doctrinal response; the doctrine is working as designed, on him.

Affected Files: 26_INFORMATION_CONTROL.md (26.4).

Secondary Consequences: Cross-references the PROTAG-005 stealth ruler.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: POL-001 (MEDIUM) — Aisha is dual-hatted by design

[WORLD AUDIT PATCH]

Issue: POL-001 — Aisha's contracting authority split across two agencies (35/32: GOV-006-contracted; 14: KNF-contracted).

Previous Canon: 32's profile said "GOV-006-contracted (SMD) Sweeper team leader in Ravenscroft... formerly KNF Liwanag Sweeper lead, recruited to the SMD in 2023"; 14's Liwanag note called her team "KNF-contracted."

New Canon: The split is deliberate — she is **dual-hatted by design**: her Ravenscroft warrant is SMD (GOV-006); when staging from Kalsada's van yard in Liwanag she operates under KNF contract authority (a liaison seam between the two bureaus). The dual warrant is the point — and the reason her unfiled follow-ups read as treason to *both* sides.

Reason: Proposed solution 2 — make the split deliberate and say so.

Affected Files: 32_ROMANCE_FRAMEWORK.md (Configuration C).

Secondary Consequences: 35's CHAR-034 row to be refined at the final rebuild ("dual-hatted: SMD Ravenscroft / KNF Liwanag liaison").

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: POL-004 (MEDIUM) — the rotation/turf-war relationship made explicit

[WORLD AUDIT PATCH]

Issue: POL-004 — The 3-year director rotation vs. the National Police Agency turf war (the 1995 charter's original sin).

Previous Canon: 06 stated the rotation (Leadership) and the turf war (Internal conflicts) without relating them.

New Canon: New parenthetical in 06's SMD Leadership bullet: the rotation was designed to prevent fiefdoms; its side effect is that the NPA turf war is never *resolved*, only inherited — every director arrives to a litigated line and leaves it litigated. The war is bureaucratic, not personal, and it outlives every director — which is the point.

Reason: Proposed solution 1 — keep the rotation and make the turf war bureaucratic, not personal.

Affected Files: 06_GOVERNMENTS.md (GOV-006 Leadership).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: POL-007 (MEDIUM) — GOV-015/016 stubs: deferred, not expanded

[WORLD AUDIT PATCH]

Issue: POL-007 — GOV-015 and GOV-016 are stubs ("Content to be developed").

Disposition: **Deferred per decision (m)** — coverage check recorded, stubs not expanded. Per the audit mandate, deferrals are recorded in the changelog rather than canon-patched: the intended content (SMD charter details; Albion accession terms) is substantially covered by 06's main SMD profile, and expanding two government registry stubs mid-audit would grow the world beyond the patch mandate. A future registry amendment may delist or write them; the stubs stand as marked.

New Canon: None.

Affected Files: None.

Status: Deferred — decision (m). Awaiting v1.3 verification (stubs remain marked "Content to be developed").

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: MIL-001 (MEDIUM) — the anomaly-war doctrine written (as the thing the Accords forbid)

[WORLD AUDIT PATCH]

Issue: MIL-001 — No anomaly-war doctrine (forces, Drowndust, the 90-second rule, but no doctrine for *fighting* an anomaly as opposed to containing one).

Previous Canon: 13 carried force structure, arsenals, the BLACK TIDE ladder, and five national doctrines — but no stated fighting doctrine.

New Canon: New §13.7 — **the anomaly-war doctrine**: the 1949 Accords forbid anomaly-war doctrine as a category (anomalies are *contained*, never fought as enemies), and 13.7 is the standing doctrine for the moment containment has already failed — (1) containment-first (JCC notified before the first shot), (2) the 90-second rule governs (Fathoms budgeted like ammunition), (3) Drowndust is the last resort (head-of-state release, Compact-reviewable), (4) the escalation ladder *is* the doctrine (WATCH → SURGE → BLACK TIDE; at BLACK TIDE evacuation is the operation). The Saratov precedent is taught as what happens when step 1 is skipped.

Reason: Proposed solution 1 — write the doctrine; the honest form is the doctrine the Accords forbid.

Affected Files: 13_MILITARY.md (new §13.7).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: MIL-002 (MEDIUM) — Drowndust's target set stated

[WORLD AUDIT PATCH]

Issue: MIL-002 — Drowndust deterrence has no stated target set or supply.

Previous Canon: 13.3 already stated the supply (processed Drowning-site residue, capped by Drownings, four finite stockpiles, the Compact's SITE-006 counter-stockpile, the Smelters' casus-belli line) and the Quiet-immunity — but not what the dust is *for*.

New Canon: 13.3's CANON now states the **target set** (JCC sealed annex): not states, factions, or populations — *events*: E-class contingencies, pre-Drowned T5+ subjects past recovery, Drowning-site denial. Useless against the Quiet, counterproductive against the contained — a weapon with exactly one legitimate target class, *the thing nothing else can stop*, which is why every stockpile's existence is also an admission.

Reason: Proposed solution 1 — state both target set and supply (supply was already stated; the target set is the fix).

Affected Files: 13_MILITARY.md (13.3 CANON).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: MIL-003 (MEDIUM) — the concealment line drawn: tactical vs strategic, Batavia Static as precedent

[WORLD AUDIT PATCH]

Issue: MIL-003 — Tide-noise vs. witnessed combat (the military's signature vs. the Veil's promise).

Previous Canon: 13's Tide-noise generators "jam both channeling and Seismograph detection" with no stated limit; 26's Veil doctrine assumed large-scale concealment.

New Canon: The Tide-noise bullet now draws the line: *tactical* engagements are concealable (noise-farming + the Seismograph's T3-floor); *strategic* Threshold events are not — the Seismograph sees them, and the cover story is "earthquake/explosion." The standing precedent is the **Batavia Static (1948, EVENT-033)** — Dutch and Indonesian Lanterns clashing over Kota Tua, laundered as independence-war artillery — and every noise-farming plan since is graded against it. A recent engagement seen past its cover story is a plot in progress, not a doctrine failure.

Reason: Proposed solution 1 — draw the line.

Affected Files: 13_MILITARY.md (13.3 Tide-noise generators).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: LAW-002 (MEDIUM) — the Reed doctrine canonized

[WORLD AUDIT PATCH]

Issue: LAW-002 — Arthur's situation is the sharp edge of the legal framework (a load-bearing design note, not a contradiction).

Previous Canon: 14.3(2) carried the LAW-001 acknowledgment clause ("future drafters must not 'fix' this gap by legislating it") but no named principle.

New Canon: New CANON **Reed doctrine** at the head of 14.3: the threshold legal framework is complete and self-consistent *except where the tether touches it*. The doctrine is **jurisprudence, not statute** — courts recognize the gap; legislatures are forbidden from "fixing" it. A future Tribunal that legislates the tether would end the theme; the law's completeness *breaking* at the protagonist is load-bearing by design.

Reason: Proposed solution 1 — canonize the principle as named doctrine.

Affected Files: 14_LAW_ENFORCEMENT.md (14.3).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: INFO-001 (MEDIUM) — the SSW watchlist tiered; EVENT-087's redacted approver

[WORLD AUDIT PATCH]

Issue: INFO-001 — The SSW watchlist problem (the doctrine promises surveillance the institutions can't deliver).

Previous Canon: 06's SMD profile held "an unacknowledged SSW-worker watchlist compiled from dispatch-company filings" with no tiering; 25's EVENT-087 said the flagged hire was "approved anyway. Someone wanted him inside. (Who? PROVISIONAL...)".

New Canon: (1) The watchlist is **tiered by Threshold-adjacency** — only migrants in Threshold-adjacent jobs (claims processing, containment logistics, records) are actively watched; the rest are filed and forgotten. The tiering is the doctrine's honest answer to the capacity gap. (2) EVENT-087's hidden truth now names the deliberate seam: the approval carries a signature block **redacted in every copy the SMD has ever obtained** — someone with clearance ordered a Lantern-screened HR desk to hire a flagged Loud migrant into a Threshold-adjacent records job. The SSW mismatch is deliberate, not a continuity error.

Reason: Proposed solution 1 + decision (d) — the SSW mismatch is deliberate through EVENT-087's redacted approver.

Affected Files: 06_GOVERNMENTS.md (GOV-006 Secrets); 25_TIMEmessaging app.md (EVENT-087).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: TECH-001 (MEDIUM) — the imagery stack: the Veil's most expensive program

[WORLD AUDIT PATCH]

Issue: TECH-001 — Commercial satellites and drones vs. persistent sites (the Veil's doctrine predates the satellite constellation era).

Previous Canon: 27.1's four mechanisms (static rot, Tide-noise, classified Seismograph data, the Veil Reflex) covered *events* but not persistent *geographic* sites.

New Canon: New fifth mechanism in 27.1 — **the imagery stack**: satellite-tasking influence (priority-tasking buys and quiet re-tasking through cutout brokers), imagery-laundering (the archived frame is the *replacement* frame), and drone no-fly enforcement (warded perimeters file as aviation hazards; the rest is polite confiscation). It is the Veil's most expensive program, with the thinnest margin: a single unlaundered commercial pass over a Wound-class site is a containment incident by definition.

Reason: Proposed solution 1 — update the doctrine and state the cost.

Affected Files: 27_TECHNOLOGY.md (27.1).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: TECH-002 (MEDIUM) — open-weight LLMs brought inside the doctrine

[WORLD AUDIT PATCH]

Issue: TECH-002 — Open LLMs vs. the Quiet (the chokepoint model doesn't cover local, offline, open-weight models).

Previous Canon: 27.3 covered ML detection and Information-Seep dataset infection, but not open weights.

New Canon: New bullet in 27.3 — the Compact's information doctrine now covers model weights: (1) **poisoned datasets** (Seep-adjacent corpora salted with confidently wrong physics); (2) **the deepfake dividend as countermeasure** (any genuine leak reads as synthetic; the noise farmers keep it that way); (3) the Quiet's samizdat runs on local models anyway — the Gray Market's press is a mesh of fine-tuned open weights, and model-poisoning is the arms race's current front. The doctrine covers weights now; the weights keep moving.

Reason: Proposed solution 1 — extend the regime to weights.

Affected Files: 27_TECHNOLOGY.md (27.3).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: TECH-003 (MEDIUM) — the Obsidian 2019 recording contained as a registered exception

[WORLD AUDIT PATCH]

Issue: TECH-003 — The Obsidian 2019 clean recording (a rot-free T4 recording vs. the static-rot doctrine).

Previous Canon: 27 noted the recording ("the only known rot-free recording of a high-pressure event... completely classified") with no containment rationale.

New Canon: 27's bullet now registers the **exception**: the capture was a fluke of specific, stated conditions (an Obsidian-pattern Tide-noise filter stack running *inverted* during a pressure null — the filter canceled the rot instead of the signal, for eleven seconds). The recording is in Compact custody (sealed vault, Tribunal warrant required); the conditions are unrepeatable by design (inversion parameters never logged; five years of failed reproduction). The rot doctrine holds; the exception is registered, sealed, and cited by every examiner who asks why the doctrine has exactly one footnote.

Reason: Proposed solution 1 — contain it: fluke conditions stated, Compact custody, unrepeatable.

Affected Files: 27_TECHNOLOGY.md (Communications).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: FAC-011 (MEDIUM) — the 28-year inaction was the protocol: a tripwire left armed

[WORLD AUDIT PATCH]

Issue: FAC-011 — The Cartographers' 28-year inaction on Ilsa's journals (a cold case needs a "why now?").

Previous Canon: 29 and 32/EVENT-100 established the journals' custody and Pram's 2024 find, but 12 gave no reason for the 28-year dormancy.

New Canon: New Secrets entry in 12's SUP-002 profile: Ilsa's journals sat dormant-monitor for 28 years **by protocol, not neglect** — the Exchange's standing rule is that the Laggard file activates only when a new holder surfaces. The inaction *was* the action: a tripwire left armed. Reed Arthur is the condition; Pram's 2024 find of the 1996 field map (EVENT-100) is the trigger; the reclassification of ANOMALY-001 from curiosity to priority is the tripwire firing.

Reason: Proposed solution 2 — the inaction was the action (the Cartographers were waiting for the torn page's subject to reappear).

Affected Files: 12_FACTIONS.md (SUP-002 Secrets).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: GEO-002 (MEDIUM) — Ravenscroft straddles Cape Omaezaki: two bays, canonical

[WORLD AUDIT PATCH]

Issue: GEO-002 — Ravenscroft sits on two bays (21: Enshū-nada; 22's LOC-007/LOC-020: Suruga Bay).

Previous Canon: Both bay attributions with no stated geography reconciling them.

New Canon: New CANON in 21's Ravenscroft profile: the metro straddles **Cape Omaezaki** — Enshū-nada to the south, Suruga Bay to the east. The cape geography is a feature: two waterfronts, two port districts, two smuggling routes — the Blackwater Syndicate truce polices the Suruga side, the Ferrymen relay works the Enshū side, and the SMD's port protocol has to be negotiated twice.

Reason: Proposed solution 1 — make it canonical.

Affected Files: 21_CITIES.md (CITY-033).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: GEO-003 (MEDIUM) — ZONE-006 renamed: the Shimizu Wound

[WORLD AUDIT PATCH]

Issue: GEO-003 — ZONE-006 "Odaiba Wound" is a Tokyo place-name in Ravenshire.

Previous Canon: 23 filed ZONE-006 as "The Odaiba Wound (Ravenscroft waterfront)."

New Canon: Renamed to **the Shimizu Wound** — for the Shimizu waterfront district it actually sits under — with a CANON rename note: old cross-references reading "Odaiba Wound" refer to this zone.

Reason: Decision (g) — rename to a Ravenshire-local name.

Affected Files: 23_SECRET_FACILITIES.md (ZONE-006).

Secondary Consequences: 35's ZONE-006 row and DATABASE/LOCATIONS.md to be updated at the final rebuild.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: GEO-004 (MEDIUM) — the 8.9M metro's merger history stated

[WORLD AUDIT PATCH]

Issue: GEO-004 — The 8.9M Ravenscroft metro vs. real Ravenshire geography (~3.6M prefecture).

Previous Canon: 21 stated the 8.9M figure with no merger history.

New Canon: New CANON in 21's Ravenscroft profile: the metro is a fictional conurbation — the post-war Shōwa mergers consolidated half a dozen fishing and port towns into a single bay city, and the 1972 and 1996 amalgamations *absorbed* Hamamatsu and Ravenshire City outright (their names survive as ward names, their city halls as ward offices). The real prefecture's ~3.6M is the world outside the merger line; inside it, Ravenscroft is Albion's third metro by construction — the Tokaido corridor's industry needed a port, and the port needed a city.

Reason: Proposed solution 1 — reconcile explicitly; the 8.9M is honest worldbuilding.

Affected Files: 21_CITIES.md (CITY-033).

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: SOC-002 (MEDIUM) — the three-minute rule renamed

[WORLD AUDIT PATCH]

Issue: SOC-002 — The "three-second rule" is defined as 180 seconds (name contradicts its own definition by a factor of 60).

Previous Canon: 24, 25, and 31 used "three-second rule" for the 180-second livestream-takedown doctrine (EVENT-080).

New Canon: Renamed to the **"three-minute rule"** everywhere (24_HISTORY.md, 25_TIMEmessaging app.md, 31_CONFLICT_ENGINE.md — 5 occurrences). 31:16's "180-second livestream rule" already matched the definition and stands.

Reason: Proposed solution 1 — the name now matches the 180-second definition.

Affected Files: 24_HISTORY.md; 25_TIMEmessaging app.md; 31_CONFLICT_ENGINE.md.

Secondary Consequences: 35's EVENT-080 row and DATABASE/EVENTS.md to be updated at the final rebuild.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: NAR-003 (MEDIUM) — Pram's destination fixed: Ravenscroft

[WORLD AUDIT PATCH]

Issue: NAR-003 — Pram's destination: 29 said Jakarta; 12/25/32 said Ravenscroft.

Previous Canon: 29:114 ("Pramudya Nugroho (CHAR-032) has been sent to Jakarta (EVENT-100)") vs EVENT-100 ("Pram is sent to Ravenscroft"), 12's hidden truth ("reassigned to Ravenscroft"), and 32's Configuration D ("reassigned to Ravenscroft, arriving September 2024").

New Canon: 29 now reads Ravenscroft. The "Jakarta" was a stale pre-relocation remnant; all four sources agree — Pram is sent to Ravenscroft (EVENT-100), arriving September 2024, carrying Ilsa's journals.

Reason: Proposed solution 2 — pick one destination (Ravenscroft, per the relocation) and fix the outlier.

Affected Files: 29_PROTAGONIST_ANOMALY.md.

Secondary Consequences: None.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: NAR-004 (MEDIUM) — CG-044: BPF-originated, KNF-absorbed

[WORLD AUDIT PATCH]

Issue: NAR-004 — CG-044's filing agency: 31 stages "The BPF Mole Hunt" (BPF-internal) while 35's row files it under KNF (and 32 calls it "the KNF mole hunt").

Previous Canon: Three-way tension — BPF setup, KNF database row, KNF label in 32.

New Canon: New Filing line in 31's CG-044: **BPF-originated, KNF-absorbed** — the Quiet Desk took jurisdiction upward. The transfer is the beat: the absorption is why the Quiet Desk has it (35's KNF row stands), why 32 calls it the KNF mole hunt, and why Aisha's unfiled BPF follow-ups read as treason to the agency that now owns the case.

Reason: Proposed solution 2 — make it a transferred file; the transfer is the beat.

Affected Files: 31_CONFLICT_ENGINE.md (CG-044).

Secondary Consequences: 35's CG-044 row ("KNF") is confirmed correct as the *current* filing agency at the final rebuild.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: SER-002 (MEDIUM) — romance configuration: deferred to serialization planning

[WORLD AUDIT PATCH]

Issue: SER-002 — The five romance configurations need a pre-serialization choice (serialization can't start while all five are live).

Disposition: **Deferred per decision (i)** — the romance configuration choice is deferred to serialization planning, but must be chosen before chapter 1. Per the audit mandate, the deferral is recorded here rather than canon-patched: all five configurations remain live as *framework* (canon-neutral), and the choice is a serialization-planning decision, not a patch-phase decision.

New Canon: None.

Affected Files: None.

Status: Deferred — decision (i). Awaiting v1.3 verification (configs remain live as framework).

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: REL-004 (MEDIUM) — disposition: already patched under FAC-007

[WORLD AUDIT PATCH]

Issue: REL-004 — REL-008 (Church of the Open Eye) has no profile but is staged by the conflict engine (31:513).

Disposition: Resolved in the HIGH tier as part of the FAC-007 registry reconciliation — 10_RELIGIONS.md now carries the full REL-008 profile (doctrine, origin, modern face, institutional ties, relationship beats), and REL-008 rows were added to the religion/registry tables. No further action.

Status: Closed — see FAC-007 entry. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: POWER-012 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: POWER-012 — Routine Erosion accumulation rates (~5 Fathoms/year) vs career viability; the issue's "sustainable career 15–25 years" quote is stale (absent from current 04), but the arithmetic is real: 5 Fathoms/year × 20 years hits the Drowning line.

Disposition: Patched. Added the **career budget** (CANON) to 04_POWER_SYSTEM.md §4.4: the relief-rotation system caps career accumulation at ~60 Fathoms — operators approaching the cap are rotated to non-channeling postings, mandatory stand-down years are priced into staffing models, depth pay hedges the residual risk, and the pension system (08 8.4) is the actuarial expression of the same budget.

New Canon: The ~60-Fathom career cap; mandatory relief rotation; "garden leave" track; pension/insurance as actuarial expression of the career budget.

Affected Files: 04_POWER_SYSTEM.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: POWER-013 (LOW) — disposition: patched (mechanical)

[WORLD AUDIT PATCH]

Issue: POWER-013 — EVENT-047's 35_CANON_DATABASE.md one-liner ("T6 Choir event") invents a Choir actor that 25_TIMEmessaging app.md's hidden truth doesn't support.

Disposition: Patched. Corrected the 35 row to match the timeline: "Global near-breach; pressure spike, no Choir actor; ~300 Loud interned; Agus Hidayat (CHAR-035) dies." The generated row will also be regenerated at the final database rebuild.

New Canon: None (mechanical correction to match existing canon).

Affected Files: 35_CANON_DATABASE.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: POWER-014 (LOW) — disposition: closed — stale premise

[WORLD AUDIT PATCH]

Issue: POWER-014 — Vector notation mismatches between 05.5's examples and 28's case entries (old vs current notation).

Disposition: **Closed — stale premise.** The HIGH-tier normalization pass already reconciled 28's vectors to current notation; no old-notation vectors remain in 28_ANOMALIES.md, and 05_ANOMALY_CLASSIFICATION.md (POWER-007) already carries the in-world guidance that older examiner notes use pre-revision grammar. Nothing left to fix.

New Canon: None.

Affected Files: None.

Status: Closed — stale premise. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: PROTAG-009 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: PROTAG-009 — The escrow deters only rational actors; the irrational-actor case (fanatics) needs pricing.

Disposition: Patched. Added **residual risk** (stated) to 29_PROTAGONIST_ANOMALY.md's escrow CANON: the escrow buys safety from *institutions*, not fanatics — Arthur's Choir-facing precautions are a separate system (Use 3, the Night Clerks' street-level early warning, staying beneath the Choir's notice; the Choir courts the shadow-blessed, it does not seize them — yet). Also removed a duplicated sentence introduced by the edit.

New Canon: The escrow's stated residual risk; the three-part Choir-facing precaution system.

Affected Files: 29_PROTAGONIST_ANOMALY.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: PROTAG-010 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: PROTAG-010 — The "engineered transfer" intent boundary: does positioning Arthur (employment, housing) void a future transfer?

Disposition: Patched. Added the **boundary** (CANON) to 29_PROTAGONIST_ANOMALY.md B.8: *proximate* positioning (arranging the death scene, seating the witness) voids; *life* positioning (employment, housing, the redacted approver's hiring file) does not — the tether distinguishes the *death* from the *biography*. Arthur's NQA employment does not void a future transfer.

New Canon: The proximate-vs-life positioning boundary; the Quiet Desk wants the line sharper than this.

Affected Files: 29_PROTAGONIST_ANOMALY.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: PROTAG-011 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: PROTAG-011 — Use 10's anchor stability across deepening lag: the anchor is a single point of failure with no acknowledgment.

Disposition: Patched. Added to 29_PROTAGONIST_ANOMALY.md's Use-10 boundary CANON: the anchor degrades with depth — deeper lag stretches the anchor thinner, edge-corruption creeps inward, the clean recording gets riskier as the ratchet climbs. The endgame's physics prices itself.

New Canon: Anchor degradation with lag-depth; edge-corruption inward creep.

Affected Files: 29_PROTAGONIST_ANOMALY.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: PROTAG-012 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: PROTAG-012 — Misconceptions #2 (T1 Lantern Resonance — the "aware" reading) and #5 (pre-Drowning symptom — the "mechanical" reading) in 29's §B.10 are mutually inconsistent.

Disposition: Patched. Added an authorial note to §B.10: #2 and #5 are the two rival schools of tether theory — the "aware" school vs the "mechanical" school — who have been arguing in the Compact's journals for a decade. The inconsistency is in-world disagreement; the list is authorial.

New Canon: The two rival tether-theory schools (in-world).

Affected Files: 29_PROTAGONIST_ANOMALY.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: PROTAG-013 (LOW) — disposition: deferred per decision (j)

[WORLD AUDIT PATCH]

Issue: PROTAG-013 — The 2023 biennial monitor: does it happen, what does it show, what happens next.

Disposition: **Deferred per decision (j)** — the 2023 monitor outcome is deferred via the austerity backlog. Per the audit mandate, the deferral is recorded here; 29's "thin, biennial monitor, a file nobody has read twice" remains the standing state until the backlog clears. This is a plot beat reserved for drafting, not a canon gap.

New Canon: None.

Affected Files: None.

Status: Deferred — decision (j). Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: PROTAG-014 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: PROTAG-014 — "Membrane" vs "Membranous" terminology drift in 29.

Disposition: Patched. Added a TERMINOLOGY (CANON) note to 29_PROTAGONIST_ANOMALY.md: **Membrane** is the phenomenon (the substrate-rendering); **Membranous** is the phase-state adjective (the condition of being within the Membrane's rendering, e.g., "the Membranous phase"). Noun for the substrate, adjective for the state.

New Canon: The Membrane/Membranous terminology canon.

Affected Files: 29_PROTAGONIST_ANOMALY.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: POL-002 (LOW) — disposition: closed — consistent as written

[WORLD AUDIT PATCH]

Issue: POL-002 — Lantern-examiner loan direction: 06 says the prefectural desk borrows from the SMD; GEO-005's patch says the SMD borrows from the prefecture.

Disposition: **Closed — consistent as written.** The current 06_GOVERNMENTS.md text (SMD "Internal conflicts": "the Ravenscroft field office borrows the prefectural quiet desk's Lantern examiners and never returns them on time") already states the decided direction — the SMD borrows from the prefecture — and GEO-005's patch uses the same direction. The issue's quoted 06 statement is stale; no contradiction exists in current canon.

New Canon: None.

Affected Files: None.

Status: Closed — consistent as written. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: POL-003 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: POL-003 — Albion's 1949 signatory status: 06's origin text ("Built under US occupation supervision to satisfy the 1949 Accords") could be read as claiming 1949 signatory status.

Disposition: Patched per decision (n). Added to 06_GOVERNMENTS.md's Albion origin: Albion was **not** a 1949 signatory — the occupation desk was compliance machinery, not accession; Albion acceded in **1952** via a US-backed quiet arrangement.

New Canon: Albion's 1952 accession via the US-backed quiet arrangement.

Affected Files: 06_GOVERNMENTS.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: POL-005 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: POL-005 — The SMD's study of the KNF's Liwanag-office dynamic lacks a paper trail.

Disposition: Patched. Named the paper trail in 06_GOVERNMENTS.md: **SMD Internal Memorandum 19-04** ("Field-office autonomy in archipelagic jurisdictions," 2017, Liaison Arm archive), citing the KNF's Daungan deconfliction memos and the Division's own 2014 Ravenshire prefectural-loan audit.

New Canon: SMD Internal Memorandum 19-04.

Affected Files: 06_GOVERNMENTS.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: POL-006 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: POL-006 — Great-power Compact payoffs unstated (why the US/China/Russia stay).

Disposition: Patched. Added the **great-power payoff** (CANON) to 07_INTERNATIONAL_RELATIONS.md: the US gets Seismograph placement and overflight coverage; China gets process control (committee chairs, classification-standard drafting, veto-by-arrears); Russia gets grandfathering (legacy arrays, closed cities, pre-1989 filings exempt from re-audit). Each payoff is unstated in the treaty text and unmistakable in practice; the price of exit is losing the payoff while everyone else keeps theirs.

New Canon: The three great-power payoffs.

Affected Files: 07_INTERNATIONAL_RELATIONS.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: MIL-004 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: MIL-004 — The Ninth Bell's tactical vs strategic role (13_MILITARY.md doesn't mention the Bell at all; the issue's 09_MILITARY.md reference is stale).

Disposition: Patched. Added the **threat level** (both) to 12_FACTIONS.md's SUP-007 profile: the Bell's *cells* (3–8 operatives) are a **tactical** threat (sabotage, thinning, murder); the **Peal** (the nine-site eschaton) is a **strategic** threat — the JCC spends more on the Bell than on any other non-state actor. Doctrine files both: cells get noise-farmed containment, the Peal gets the full anomaly-war ladder (13.7).

New Canon: The Bell's dual threat-level filing.

Affected Files: 12_FACTIONS.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: MIL-005 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: MIL-005 — The ninety-second rule doesn't cover passive detection (listening posts, Seismograph watch, Lantern overwatch).

Disposition: Patched. Added the negative space to 13_MILITARY.md's ninety-second rule: the rule governs sustained *engagements* and raids' execution budgets; it does **not** govern *passive detection* — observation is not expenditure. Staff-college mnemonic: "ninety seconds is how long you can fight; forever is how long you can be watched."

New Canon: The rule's stated non-coverage of passive detection.

Affected Files: 13_MILITARY.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: MIL-006 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: MIL-006 — The Saratov sleeper's Fathom status is unstated.

Disposition: Patched. Added to 13_MILITARY.md's bound-seep arsenals: the sleeper carries *suppressed* Fathoms — unmeasurable while comatose, fully accrued the moment it wakes (that is the sleeper's definition; waking one is a launch decision, not a medical one).

New Canon: Suppressed-Fathom sleeper status.

Affected Files: 13_MILITARY.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: LAW-003 (LOW) — disposition: closed — already stated

[WORLD AUDIT PATCH]

Issue: LAW-003 — CASE-006's damages-cap basis unstated.

Disposition: **Closed — already stated.** The current 14_LAW_ENFORCEMENT.md CASE-006 text states the basis: "capped damages at the BPF's annual field budget, noting that bankrupting the agency would kill more people than the misclassification did" — the public-utility-insolvency rationale. No patch needed.

New Canon: None.

Affected Files: None.

Status: Closed — already stated. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: LAW-004 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: LAW-004 — Finders-law non-reporting penalty unstated (14 says "failure to report is the offense, not the finding" but gives no penalty).

Disposition: Patched. Added the **penalty** to 14_LAW_ENFORCEMENT.md: forfeit of the find plus an administrative fine scaled to class (C-B+: forfeit and fine; C-A+: referral — an unreported C-A is treated as an unlicensed containment operation); escalates to criminal prosecution if the unreported find causes harm — which is why the Gray Market's "found, not bought" defense fails everywhere it's been tested.

New Canon: The finders-law penalty schedule.

Affected Files: 14_LAW_ENFORCEMENT.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: INFO-002 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: INFO-002 — Static-rot transitivity to second-order records: does the catalog rot?

Disposition: Patched. Added the **transitivity** (CANON) to 26_INFORMATION_CONTROL.md: rot applies to *records of events*, not *records of records* — a photograph of a Seep rots; a written report *about* the photograph does not. The catalog is safe — but its fidelity to rotted primaries is bounded: where the primary died, the catalog preserves the report, not the event, and every serious archive carries the gap as stated provenance.

New Canon: The static-rot transitivity rule.

Affected Files: 26_INFORMATION_CONTROL.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: INFO-003 (LOW) — disposition: closed — stale premise

[WORLD AUDIT PATCH]

Issue: INFO-003 — The Gray Book's Loud editors: the Loud pipeline treats Loud as recruits, not publishing staff.

Disposition: **Closed — stale premise.** Current canon has no "Gray Book with Loud editors" in the information regime: the Gray Book is the Rememberers' (IND-002) anonymized, volunteer-compiled civilian incident log (12_FACTIONS.md); the "Three editors read them; two wrote memos; all six forgot the details" passage (26:107) is the 1992 Geneva clerk beat about *newspaper* editors, not the Gray Book. The Gray Book's editorship is described (Rememberers, volunteer-compiled). No contradiction exists.

New Canon: None.

Affected Files: None.

Status: Closed — stale premise. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: TECH-004 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: TECH-004 — Phone-sensor Seismograph: the Compact's position on the phone grid is unstated.

Disposition: Patched. Added the **phone-grid question** (stated) to 27_TECHNOLOGY.md: the Compact *can't* use phone telemetry for Threshold discrimination — the noise floor is ~2 orders of magnitude above the T3 detection threshold, and no crowdsourcing buys coherent integration without synchronized, calibrated hardware. The Gray Market got there first: civilian "pressure-tracking" apps are the Veil's newest hole — crude, uncalibrated, good enough to sell as "Tide weather."

New Canon: The phone-grid noise floor; Gray Market pressure-tracking apps.

Affected Files: 27_TECHNOLOGY.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: TECH-005 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: TECH-005 — The tech-should-have-solved sweep: 2024-ordinary tech (cameras, payments, biometrics, satellites, LLMs) should have collapsed concealment beats, and the file never runs the per-beat check.

Disposition: Patched. Added the **2024 principle** (CANON) to 27_TECHNOLOGY.md: the Veil's modern posture is *posture*, not invisibility — the Compact manages *interpretation*, not *observation*. The deepfake dividend means every genuine capture reads as synthetic, noise farming keeps the fakes ahead of the truth, and the Veil Reflex edits the witnesses the cameras can't. The technology that should have collapsed concealment instead industrialized the cover story.

New Canon: The 2024 interpretation-management principle.

Affected Files: 27_TECHNOLOGY.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: ECON-012 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: ECON-012 — Depth-pay incentive effects are unpriced: the pay structure incentivizes the deep work the Erosion doctrine warns against.

Disposition: Patched. Added the **incentive hedge** (CANON) to 08_ECONOMY.md's depth-pay line: every depth-pay contract carries a **mandatory relief-rotation offset** — paid stand-down years the employer funds and the employee cannot waive (the waiver is the abuse vector the 1977 revision closed). The premium buys the risk; the rotation caps it; the career budget (04 §4.4) is the ceiling both obey.

New Canon: The mandatory relief-rotation offset; the unwaivable stand-down.

Affected Files: 08_ECONOMY.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: ECON-013 (LOW) — disposition: closed — stale premise

[WORLD AUDIT PATCH]

Issue: ECON-013 — Quiet-leave uptake rates and graywater market volumes imply different workforce sizes; "an internal audit in 2021 found 11% of volume leaking."

Disposition: **Closed — stale premise.** The quoted numbers (uptake rates, market volumes, the 2021 11%-leak audit) do not exist in the current 08_ECONOMY.md — quiet leave is described only as a service-denominated benefit (8.2.1), and graywater only as a street-market drug (line 85). There are no conflicting workforce figures in current canon to reconcile.

New Canon: None.

Affected Files: None.

Status: Closed — stale premise. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: ECON-014 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: ECON-014 — RC-029's bank run vs the Compact backstop: both can't be true unless the backstop's credibility is the variable.

Disposition: Patched. Added the **backstop question** (CANON) to 31_CONFLICT_ENGINE.md's RC-029 setup: the Compact Catastrophe Backstop exists and would cover the bank — but it isn't *believed* by Gray Market clients, who can't claim a backstop they'd have to admit using. The run is a confidence crisis, not a solvency crisis — the classic Diamond-Dybvig beat, played in sounding.

New Canon: The RC-029 confidence-crisis reading.

Affected Files: 31_CONFLICT_ENGINE.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: ECON-015 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: ECON-015 — Argent's fractional reserve: a fractional-reserve Quiet bank with no stated reserve ratio and no lender of last resort.

Disposition: Patched. Added the **reserve question** (stated) to 11_CORPORATIONS.md's CORP-008 Secrets: Argent runs a stated **~1:3 sounding reserve ratio** against its credit book, and its unspoken backstop is the Compact's Catastrophe facility — never tested, universally priced in. Argent is too-big-to-fail: if it falls, the settlement system falls with it.

New Canon: The ~1:3 sounding reserve ratio; the Compact backstop as Argent's implicit lender of last resort.

Affected Files: 11_CORPORATIONS.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: ECON-016 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: ECON-016 — The sector table sums (~$95–141B) below the $140–200B CANON total; the missing share is never named as a line item.

Disposition: Patched. Added a **Subtotal (measurable sectors)** row and the **unaccounted lines** (named, still estimated) to 08_ECONOMY.md's sector table: Gray Market commerce ($12–20B), in-kind/barter Quiet services ($8–12B), unlicensed disposal and Tide-brokerage ($5–9B), unreported private retainers ($3–6B). The four lines bridge the table to the CANON total — the gap is *accounted* even where it can't be *measured*.

New Canon: The four named unaccounted lines.

Affected Files: 08_ECONOMY.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: FAC-012 (LOW) — disposition: closed — stale premise

[WORLD AUDIT PATCH]

Issue: FAC-012 — The Alon/Koi flip: CRIM-006 rendered "Not a threat yet. Hasn't read the Ravenscroft survey" in one passage and under a flipped name/leadership attribution in another.

Disposition: **Closed — stale premise.** The quoted renderings do not exist in current canon: CRIM-006 is consistently "The Alon Combine" led by Kapitan Rudy Salonga (12_FACTIONS.md), and the 35_CANON_DATABASE.md / DATABASE/FACTIONS.md rows match. The flip lived only in the worker artifact FACTION_AUDIT.md, not in the bible.

New Canon: None.

Affected Files: None.

Status: Closed — stale premise. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: FAC-013 (LOW) — disposition: patched (mechanical)

[WORLD AUDIT PATCH]

Issue: FAC-013 — The 34 header count: §34.1 reads "the 21 profiled factions" while the matrix covers 22.

Disposition: Patched. Corrected the section header to "the 22 profiled factions" (matching the FAC-007 registry decision). Note: the issue's "header claims 36 factions" is stale — the current file header carries the controlled-vocabulary legend, not a 36-faction claim.

New Canon: None (mechanical correction).

Affected Files: 34_FACTION_RELATIONSHIPS.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: FAC-014 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: FAC-014 — The Ferrymen's perfect record ("zero lost cargoes in seventy years" reported as fact).

Disposition: Patched. Qualified the SUP-010 record in 12_FACTIONS.md: zero *reported* lost cargoes in seventy years — the record is *reported* perfect; the Compact's loss-database disagrees in three cases the Ferrymen classify as "delivered to an alternate consignee," and everyone understands what that euphemism costs.

New Canon: The three disputed loss cases; the "alternate consignee" euphemism.

Affected Files: 12_FACTIONS.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: FAC-015 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: FAC-015 — The Salt Road pilgrimages: no file states who *protects* the Ninth Bell's pilgrimages to ANOMALY-029.

Disposition: Patched. Added the **pilgrimage protection** (stated) to 12_FACTIONS.md's CRIM-005 profile: the Road *escorts* the Bell pilgrimages itself — guides, water-right, silence — because hospitality is the creed and an unescorted Bell column in Road territory would be everyone's catastrophe. The cost: each pilgrimage burns a season's worth of Compact goodwill (the Seismograph Authority's working truce is priced in pilgrimages).

New Canon: The Road's escort obligation; the goodwill cost.

Affected Files: 12_FACTIONS.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: FAC-016 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: FAC-016 — The Care Axis absolution: the 34 essay's "the Peal quietly regretted" is an unsourced absolution for the two bombed gardens.

Disposition: Patched. Rewrote the 34_FACTION_RELATIONSHIPS.md Care Axis essay note: the absolution is the *Care Axis's claim* (in-world advocacy, not established fact — the Bell's record neither confirms nor denies, and the Quiet Garden's registry still lists both bombings as Bell-attributed). The Bell's guilt stays open; the Axis's forgiveness is stated as the Axis's.

New Canon: The attribution stays open; the essay's claim is marked as the Axis's advocacy.

Affected Files: 34_FACTION_RELATIONSHIPS.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: FAC-017 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: FAC-017 — The conflict matrix's cells don't share a legend (RIVALS cells describing kill contracts and murdered crews).

Disposition: Patched. Recoded four matrix cells in 34_FACTION_RELATIONSHIPS.md to match the controlled vocabulary: SUP-004 vs Bell → AT-WAR (standing kill/capture contract on Rectors); SUP-009 vs Bell → AT-WAR (Seasons bombings); SUP-010 vs Bell → AT-WAR (murdered crews, defensive); CRIM-003 vs Compact → AT-WAR (bounty, simultaneously used via cutouts).

New Canon: None (mechanical recoding to the existing legend).

Affected Files: 34_FACTION_RELATIONSHIPS.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: FAC-018 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: FAC-018 — The SMD/Blackwater Syndicate ally+enemy coding: the matrix can't represent the truce's duality.

Disposition: Patched. Added **TRUCE** to 34_FACTION_RELATIONSHIPS.md's controlled vocabulary (cooperation *and* antagonism simultaneously — cooperation on the named protocol, antagonism everywhere else) and recoded the two "CLIENT-ish" cells (CRIM-007 vs GOV bloc; CRIM-006 vs GOV-014) to TRUCE.

New Canon: The TRUCE stance code.

Affected Files: 34_FACTION_RELATIONSHIPS.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: FAC-019 (LOW) — disposition: patched (mechanical)

[WORLD AUDIT PATCH]

Issue: FAC-019 — The Liwanag Bay Seep leftover: 11's CORP-011 Enemies entry references "the Liwanag Bay Seep's taxonomy (RC-026)" — the pre-relocation name leaking through.

Disposition: Patched. Corrected to "the Ravenscroft Bay Seep's taxonomy (RC-026, the RC-016 seep)" — RC-026 disputes the Ravenscroft Bay Seep, not a Liwanag seep.

New Canon: None (mechanical relocation-residue fix).

Affected Files: 11_CORPORATIONS.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: FAC-020 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: FAC-020 — Argent's Liwanag branch: a branch described as important in a theater that's now secondary.

Disposition: Patched. Added the **branch's role** (stated) to 31_CONFLICT_ENGINE.md's RC-029 setup: the Liwanag branch is Argent's *Gray Market* hub — secondary theater, primary function; Geneva wouldn't touch these accounts, and the branch exists precisely so Geneva doesn't have to.

New Canon: The Liwanag branch as Argent's Gray Market hub.

Affected Files: 31_CONFLICT_ENGINE.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: FAC-021 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: FAC-021 — CORP-013 (Ferrymen Mutual) is referenced in 35 but has no profile in 11.

Disposition: Patched. Wrote the full **CORP-013 — Ferrymen Mutual** profile in 11_CORPORATIONS.md: maritime Quiet insurance, Rotterdam HQ, ~90 staff, ~$220M revenue, Pieter Van Doole; the insurance paradox (the voyage is completed before the risk attaches — losses classified as "delivered to an alternate consignee," the code is the claims department). Updated the corporate-landscape table (13 corps, twelve of thirteen know).

New Canon: The CORP-013 profile; the insurance paradox.

Affected Files: 11_CORPORATIONS.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: FAC-022 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: FAC-022 — The triple go-legitimate beat: factions described as "going legitimate" with no Compact amnesty/rehabilitation mechanism.

Disposition: Patched. Added **Criminal rehabilitation (the missing mechanism)** to 14_LAW_ENFORCEMENT.md: the Compact has **no** amnesty or rehabilitation protocol — no *pentiti* regime, no truth-and-reconciliation track. The claims are claims: the Blackwater Syndicate's young presidents *want* legitimacy, the Koi Precepts *order* a humanitarian pivot if the masquerade collapses, the Lantern Bearers *bid* for it — and no one believes any of them, which is the story. The absence is deliberate: a real mechanism would require admitting the criminal economy is load-bearing.

New Canon: The stated absence of a Compact rehabilitation mechanism.

Affected Files: 14_LAW_ENFORCEMENT.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: FAC-023 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: FAC-023 — Four characters named Okafor across four factions with no stated relation.

Disposition: Patched. Added a **name-collisions** (CANON) note to 12_FACTIONS.md's registry: Partner Ayo Okafor (Red Ledger), Margaret Okafor (Halcyon CEO), "Doc" Okafor (researcher), and the Okafor of CASE-002 (Drowned Choir seeder, 2009) are **unrelated** — Okafor is a common name, and the hidden world is small enough for coincidence to look like conspiracy, which is a standing joke among the four's colleagues.

New Canon: The four Okafors' stated non-relation.

Affected Files: 12_FACTIONS.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: FAC-024 (LOW) — disposition: closed — stale premise

[WORLD AUDIT PATCH]

Issue: FAC-024 — Halcyon/Bell recruitment direction: 12 says Halcyon hires Bell-adjacent talent; 09_MILITARY's table says the Bell recruits from Halcyon.

Disposition: **Closed — stale premise.** The quoted 12 statement does not exist in current canon: 12_FACTIONS.md's registry table reads "CORP-001 Halcyon Dynamics — Simulation-hypothesis engineers; Bell recruitment target (talent)" — the direction is consistent (the Bell recruits *from* Halcyon). No contradiction.

New Canon: None.

Affected Files: None.

Status: Closed — stale premise. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: GEO-005 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: GEO-005 — The four-agents problem: 22's SMD regional field office watches the landings "with four agents, one boat" — personnel the org chart doesn't stage.

Disposition: Patched. Specified in 22_SUPERNATURAL_LOCATIONS.md: the four agents include two prefectural-quiet-desk Lantern examiners on the standing loan (06, GOV-006 — "never returned on time"), which is the mechanism.

New Canon: The field office's four-agent composition (two on prefectural loan).

Affected Files: 22_SUPERNATURAL_LOCATIONS.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: GEO-006 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: GEO-006 — The Pale Court buyers: CG-043's buyer is "a Pale Court cadet branch" with no Ravenscroft address (the issue mislabels it RC-043; it's CG-043).

Disposition: Patched. Gave the cadet branch its Ravenscroft address in 31_CONFLICT_ENGINE.md's CG-043 setup: **the Nagisa Collection** — a waterfront private gallery, nominally a contemporary-art foundation, actually the cadets' local front.

New Canon: The Nagisa Collection (Pale Court cadet-branch front, Ravenscroft).

Affected Files: 31_CONFLICT_ENGINE.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: GEO-007 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: GEO-007 — The two hills: the "hill station" (21) and the "low-pressure hill reserve" (23, ZONE-005) with inconsistent relative positioning.

Disposition: Patched. Added the **identity** (CANON) to 23_SECRET_FACILITIES.md's ZONE-005: it is the *same hill* — the Takakusa Hill facility; the hill station is the *operational* building, the Calibration Reserve is the *low-pressure ground* it sits on. One hill, two functions; the "cleanest readings" claims are the operations staff's and the calibration staff's versions of the same claim.

New Canon: The Takakusa hill identity reconciliation.

Affected Files: 23_SECRET_FACILITIES.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: GEO-008 (LOW) — disposition: closed — stale premise

[WORLD AUDIT PATCH]

Issue: GEO-008 — The 05:58 train: 25's "Arthur's train is the first one, 05:58" vs 20's station timetable.

Disposition: **Closed — stale premise.** No station timetable exists in the current 20_GEOGRAPHY.md to contradict the beat (the beat lives in 18_CIVILIAN_LIFE.md:13 and stands uncontradicted). Nothing to reconcile.

New Canon: None.

Affected Files: None.

Status: Closed — stale premise. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: GEO-009 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: GEO-009 — The Karuizawa hour: "an hour from the listening post by the old rail line" fails real-world geography (Ravenscroft-area → Karuizawa exceeds an hour).

Disposition: Patched. Added **travel time** (CANON) to 22_SUPERNATURAL_LOCATIONS.md's LOC-014: ~3.5 hours from the Ravenscroft metro by the old rail line (two changes) — the archive's remoteness is the point; the caretaker prefers visitors who've earned the trip.

New Canon: The 3.5-hour Karuizawa travel time.

Affected Files: 22_SUPERNATURAL_LOCATIONS.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: HIST-004 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: HIST-004 — The 1977 revision pointer: the Drowndust ban's mandatory revision is cited without a citable source (and a phantom "emergency 1978 revision session").

Disposition: Patched. Added the **revision's text pointer** (CANON) to 24_HISTORY.md: the full text is held in the Meridian Compact's archive (Meridian House, Geneva), reading-privilege restricted, Archivist-certified. There was no "emergency 1978 revision session" — the 1978 date in secondary citations is the unpublished protocol's *ratification* year. Drafters cite **1977** for the revision, **1979** for the Second Protocols.

New Canon: The 1977 revision archive pointer; the 1978-session correction.

Affected Files: 24_HISTORY.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: HIST-005 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: HIST-005 — The Fukushima Rule's content drift: one name, two meanings (treaty principle vs containment doctrine).

Disposition: Patched per decision (o). Added the **two-clause reading** (CANON) to 24_HISTORY.md: (1) a **treaty principle** — some Tide-marks too sacred to exploit (the 2009 read-only principle); (2) an **exported manage-around doctrine** — some places can't be contained, only managed around (the SMD's operational export, cf. RC-008). One name, two meanings, both canonical — the drift is the doctrine's history, not a copy error.

New Canon: The Fukushima Rule's two-clause reading.

Affected Files: 24_HISTORY.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: REL-005 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: REL-005 — The Bell's chronology: 10's nine-bell chronology vs 24's dated entries.

Disposition: Patched. Added **sacred vs. secular dating** (CANON) to 10_RELIGIONS.md: the nine-bell chronology is the Bell's *sacred calendar*; where it diverges from 24's timeline, the divergence is the *faith's*, not the bible's — the Bell dates by phase-significance, the Compact by Seismograph. Both stated, neither reconciled; sacred and secular dating disagree in the real world too.

New Canon: The sacred-calendar dating canon.

Affected Files: 10_RELIGIONS.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: REL-006 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: REL-006 — The Parisada's venting mechanism is THEORY-tagged, but 10's operational detail ("It works often enough...") risks being read as CANON.

Disposition: Patched. Tagged the operational passages explicitly as THEORY in 10_RELIGIONS.md's REL-004: the *effectiveness* claim is the working group's own (corroborated only by the BPF Bali liaison's existence); whether it works *because of* the ritual or *alongside* it is the THEORY the Compact won't touch.

New Canon: None (tagging correction).

Affected Files: 10_RELIGIONS.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: SOC-003 (LOW) — disposition: closed — stale premise

[WORLD AUDIT PATCH]

Issue: SOC-003 — Ward offices' Quiet functions: 17 says ward offices have Quiet functions, but Arthur's paperwork shows only civil administration.

Disposition: **Closed — stale premise.** The current canon does not attribute Quiet functions to ward offices: 18_CIVILIAN_LIFE.md:21 shows only *civil* administration (residence cards, SSW status, My Number). There is no contradiction to resolve.

New Canon: None.

Affected Files: None.

Status: Closed — stale premise. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: SOC-004 (LOW) — disposition: patched

[WORLD AUDIT PATCH]

Issue: SOC-004 — Chonaikai as Veil infrastructure: the mechanism (how a neighborhood association maintains secrecy) is unstated.

Disposition: Patched. Added the **mechanism** (stated) to 14_LAW_ENFORCEMENT.md's capillary network: the neighbourhood association's *kairanban* (circular notice board) doubles as a low-grade information-control channel — the disaster-drill schedule is also a sweep schedule; the garbage-sorting rules encode what gets reported and to whom. Nobody is recruited, nobody is briefed — the Division reads the board as terrain. (The neighbourhood association notice board is the first thing a Sweeper team photographs on arrival.)

New Canon: The kairanban information-control mechanism.

Affected Files: 14_LAW_ENFORCEMENT.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: MEDIUM-tier follow-up refinements (POWER-008/009/010)

[WORLD AUDIT PATCH]

Issue: Verification risks flagged during the MEDIUM tier: (1) ANOMALY-012's Rule sentence said victims "accrue Erosion" while the new correction names resonance damage; (2) ANOMALY-015's Rule said "the infant wakes carrying the rocker's Fathoms" while the new note claimed the Rule text was corrected to Erosion; (3) POWER-008's "CASE-006-adjacent Quiet Desk v. Ward Six Propagation" risked reading as a pseudo-ID.

Disposition: Patched. (1) ANOMALY-012's Rule now reads "accrues **resonance damage** at ~1 Fathom per month without channeling" (and quote punctuation normalized to the file's curly-quote style). (2) ANOMALY-015's Rule now reads "The infant wakes carrying the rocker's *Erosion*, measured in Fathoms." (3) The Ward Six Propagation ruling is now described as "a separate ruling, jurisprudentially adjacent to CASE-006's liability doctrine, not part of it."

New Canon: None (wording reconciliations).

Affected Files: 28_ANOMALIES.md.

Status: Patched. Awaiting v1.3 verification.

## v1.3 — 2026-09-19 — WORLD AUDIT PATCH: overall forensic-audit summary (v1.3 sign-off)

[WORLD AUDIT PATCH]

Issue: The v1.3 forensic audit (Albion-primary relocation bible) is complete. This entry records the overall totals and the final rebuild state.

Disposition: Complete. Issue totals: **3 CRITICAL / 36 HIGH / 33 MEDIUM / 51 LOW = 123 issues** — 110 patched, 8 closed as stale premise, 5 explicitly deferred (romance configuration → serialization planning before chapter 1; 2023 monitor → austerity backlog; GOV-015/016 stubs → recorded, not expanded; 1 HIGH + 3 MEDIUM per their tier batches), 0 unresolved. Red-team totals: **570 asked / 543 answered from canon / 21 patch-required / 6 intentional mysteries preserved** (543 + 21 + 6 = 570). The six intentional mysteries (tide-cycle driver; what is behind the Laggard / whether intelligent; whether the Undertow wants anything; 2018 dip causation; Ilsa Brandt's torn final page; Level-7 Worldtide silence) were preserved — no patch resolved any of them.

New Canon: None in this entry (summary only).

Affected Files: 35_CANON_DATABASE.md (rebuilt — stale EVENT-047, ZONE-006 "Odaiba Wound" → "The Shimizu Wound", EVENT-080 three-minute rule fixed); DATABASE/ (all six views regenerated); 37_FINAL_WORLD_BIBLE.md (regenerated from the 37 numbered source files, v1.3 — post-forensic-audit); AUDIT/FINAL_WORLD_AUDIT.md (new — mandated sections + 10 explicit system stress tests, all HOLD).

Status: Verified 2026-09-19 — 30 countries, 33 cities, 20 LOC, 10 ZONE, 10 SITE, 30 anomalies, 35 characters, 100 events, 50 RCs, 52 CGs, 412 unique IDs, every referenced ID resolves, no duplicate IDs, no broken Markdown file links.

## v1.4 — 2026-09-20 — [CHARACTER PATCH]: British protagonist canon patch (sign-off)

[CHARACTER PATCH]

Issue: CHAR-001 was an Indonesian SSW migrant worker (Raka Wijaya); per user directive the protagonist is now an ordinary native British man. All biographical anchors (family, coworker, birthplace, visa machinery, remittance/dorm/kos texture) contradicted the retarget.

Previous Canon: Raka Wijaya, 24, Indonesian migrant worker, night-shift records clerk at NQA Ravenscroft on SSW visa; family in Tebet, Jakarta (Darma/Sari Wijaya, sister Anindya "Dita" Rahayu); coworker Bayu Santoso (fellow migrant, Loud).

New Canon: **Reed Arthur** (森 大地), 24, Ravenscroft native; regular-employee night-shift records clerk at NQA Ravenscroft's records archive (CORP-011, high-attention hiring); Loud, not Attuned; holder of ANOMALY-001 since March 2017; lives in a ¥48,000/month 1K in Willowmere, ten minutes on foot from his parents. Anomaly mechanics unchanged.

Reason: User-mandated protagonist retarget (ordinary native British male, starts weak, anomaly seems weak/inconvenient/unreliable).

Affected Files: 01, 06, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36; 02, 03, 04, 05, 08 (name tokens); DATABASE/CHARACTERS.md, DATABASE/JAPANESE_CHARACTER_NAMES.md, DATABASE/EVENTS.md, DATABASE/FACTIONS.md, DATABASE/ANOMALIES.md, DATABASE/LOCATIONS.md (name tokens); AUDIT/* (name tokens only); 00_INDEX.md; 38_MANIFEST.md; 37_FINAL_WORLD_BIBLE.md (rebuilt).

Status: Applied 2026-09-20 — 925 mechanical name-token replacements + targeted content rewrites; zero residual old-name hits tree-wide (verified by grep).

## v1.4 — 2026-09-20 — [CHARACTER PATCH]: Yusuf bridge + EVENT-079 relocation

[CHARACTER PATCH]

Issue: ANOMALY-001's transfer chain (Ilsa Brandt → Yusuf Hidayat → protagonist) was anchored in Tebet, Jakarta; the new protagonist is Ravenscroft-born and never left Albion.

Previous Canon: Yusuf Hidayat dies March 2017 in Tebet; tether passes to teenage Raka (EVENT-079).

New Canon: In 2016, aging and ill, Yusuf accepted lodging with Ravenscroft's informal circle of Loud rememberers (the loose network later absorbed as the Night Clerks' Ravenscroft cell, IND-004); lived in a spare room on the Reed family's Willowmere street; seventeen-year-old Arthur ran his errands. Yusuf died of a stroke March 2017 with Arthur beside him (EVENT-079, Ravenscroft); the tether passed to the nearest Loud witness. Transfer mechanics unchanged (proximity + Loudness; cannot be engineered). Yusuf's Indonesian identity, *bau payau*, and logbook preserved.

Reason: Minimal bridge preserving the 21-year control-group holder and the transfer mechanics while grounding the protagonist's acquisition in Ravenscroft.

Affected Files: 24_HISTORY.md, 25_TIMEmessaging app.md, 29_PROTAGONIST_ANOMALY.md (Part B), 35_CANON_DATABASE.md, DATABASE/EVENTS.md.

Status: Applied 2026-09-20.

## v1.4 — 2026-09-20 — [CHARACTER PATCH]: CHAR-008 given-name collision fix

[CHARACTER PATCH]

Issue: CHAR-008 (Compact Secretary-General) and CHAR-031 (Dr. Amara Nwosu) shared the given name "Amara" — genuine confusion risk between two female speaking principals.

Previous Canon: Amara Diallo (CHAR-008).

New Canon: **Fatoumata Diallo** (CHAR-008); surname kept. CHAR-031 keeps "Amara" (pairs naturally with Igbo surname Nwosu). Prose-only Dr. Amara Eze (12_FACTIONS.md SUP-011) left unchanged (no ID; three-way collision resolved by this fix).

Reason: Collision fix per the character-naming canon (Phase 3).

Affected Files: 07_INTERNATIONAL_RELATIONS.md, 11_CORPORATIONS.md, 35_CANON_DATABASE.md, DATABASE/CHARACTERS.md.

Status: Applied 2026-09-20 — all "Amara Diallo" hits replaced; every remaining bare "Amara" verified as CHAR-031 or Dr. Amara Eze (kept).

## v1.4 — 2026-09-20 — [CHARACTER PATCH]: CHAR-016 surname collision fix

[CHARACTER PATCH]

Issue: CHAR-016 and CHAR-005 (Director-General Ratna Kusuma) shared the surname "Kusuma" though unrelated — shared surname in prose implies a relation that doesn't exist.

Previous Canon: Nadia Kusuma (CHAR-016).

New Canon: **Nadia Puspita** (CHAR-016); given name kept. CHAR-005 keeps "Kusuma" (more established). She remains an Indonesian migrant (SSW), NQA Ravenscroft claims adjuster, 25 — romance Configuration A, rewritten as the cross-cultural configuration.

Reason: Collision fix per the character-naming canon (Phase 3).

Affected Files: 18_CIVILIAN_LIFE.md, 29_PROTAGONIST_ANOMALY.md, 32_ROMANCE_FRAMEWORK.md, 35_CANON_DATABASE.md, DATABASE/CHARACTERS.md.

Status: Applied 2026-09-20.

## v1.4 — 2026-09-20 — [CHARACTER PATCH]: CHAR-012–015 repurposing

[CHARACTER PATCH]

Issue: CHAR-012–015 described an Indonesian family/coworker circle for a protagonist who is now a native British Reed Arthur — relationship-to-protagonist lines could not stand.

Previous Canon: CHAR-012 Anindya "Dita" Rahayu (sister, 29, ER nurse, Jakarta); CHAR-013 Darma Wijaya (father, 58, retired civil servant); CHAR-014 Sari Wijaya (mother, 55, Tebet warung owner); CHAR-015 Bayu Santoso (fellow migrant coworker, 26, Loud).

New Canon (IDs unchanged; dramatic functions kept, biographies replaced — see `_charpatch_protagonist.md` §7): CHAR-012 **Hannah Reed** (森 七海), 22, Arthur's younger sister, ordinary office worker, lives at home; CHAR-013 **Thomas Reed** (森 隆), 58, father, current *department manager* (section chief), parts procurement, local auto-parts manufacturer (Hama-kogyo); CHAR-014 **Eleanor Reed** (森 裕子), 55, mother, part-time supermarket staff, family folk-heuristic keeper; CHAR-015 **Saitō Yūto** (斎藤 悠斗), 26, Arthur's coworker and closest friend, night-shift records clerk, also Loud (unacknowledged). The Static Hour contact beat (CG-017) was Bayu-specific and was **not** transferred — removed from `31_CONFLICT_ENGINE.md` (no dangling reference).

Reason: Keep the dramatic functions (sibling / father / mother / coworker-friend beats), replace the biographies with culturally native ones.

Affected Files: 31_CONFLICT_ENGINE.md (CG-017, CG-025, CG-037, CG-050), 32_ROMANCE_FRAMEWORK.md, 35_CANON_DATABASE.md, DATABASE/CHARACTERS.md, DATABASE/JAPANESE_CHARACTER_NAMES.md, `_charpatch_protagonist.md`, `_rename_registry.md` (§6).

Status: Applied 2026-09-20.

## v1.4 — 2026-09-20 — [CHARACTER PATCH]: CHAR-036/037 creation

[CHARACTER PATCH]

Issue: The retargeted protagonist's NQA night-shift workplace needed its human furniture (boss, senior) — new canon, ≤3 new characters allowed.

Previous Canon: None (new IDs).

New Canon: CHAR-036 **Okada Kumiko** (岡田 久美子), 47, Quiet — night-shift section chief, NQA Ravenscroft records archive; kind, tired; runs the break rotation. CHAR-037 **Hasegawa Kenji** (長谷川 健司), 34, Quiet — senior night-shift records clerk, ten years on nights; teaches Arthur filing tricks and survival tricks in the same dry tone.

Reason: Workplace texture for the citizen-clerk protagonist (boss → employee / senior → junior / peer registers differentiated without exposition).

Affected Files: 35_CANON_DATABASE.md, DATABASE/CHARACTERS.md, DATABASE/JAPANESE_CHARACTER_NAMES.md.

Status: Applied 2026-09-20.

## v1.4 — 2026-09-20 — [CHARACTER PATCH]: British cultural-consistency audit fixes

[CHARACTER PATCH]

Issue: The British Character Consistency Audit (2026-09-20) found 6 genuine cultural/internal-logic issues in Arthur's scenes.

Previous Canon: (1) shift ends 06:00 but first train 05:58; (2) landlord asking about the electricity bill; (3) "homesick tax" migrant residue; (4) rent ¥58,000 vs canonical ¥48,000; (5) 1K-class band ¥50–65k excluding Arthur's ¥48k; (6) "precarious residency" applied to a citizen.

New Canon: (1) first train 06:04; (2) landlord stopped asking why his meter barely moves; (3) clause removed; (4) ¥48,000/month; (5) band ¥45–65k/month; (6) "thin-file precarity".

Reason: Cultural/internal consistency for the native-citizen protagonist.

Affected Files: 18_CIVILIAN_LIFE.md, 34_FACTION_RELATIONSHIPS.md.

Status: Applied 2026-09-20 by the audit agent; recorded here.

## v1.4 — 2026-09-20 — [CHARACTER PATCH]: OLD→NEW name mapping record (§20 requirement)

[CHARACTER PATCH]

Issue: §20 requires a durable OLD→NEW name mapping record for the rename.

Previous Canon: N/A.

New Canon: Complete mapping in `_rename_registry.md` §§1–2 (Phase 3: Raka Wijaya→Reed Arthur; Amara Diallo→Fatoumata Diallo; Nadia Kusuma→Nadia Puspita) and §6c (Phase 3b: CHAR-012–015 repurposing aliases + CHAR-036/037 creation). Kanji/readings in `DATABASE/JAPANESE_CHARACTER_NAMES.md`.

Affected Files: `_rename_registry.md`, `DATABASE/JAPANESE_CHARACTER_NAMES.md`.

Status: Recorded 2026-09-20.

## v1.4 — 2026-09-20 — Sweep methodology note (historical-notes rule)

[CHARACTER PATCH]

Issue: The final sweep had to update names tree-wide without rewriting dated audit/decision prose.

Disposition: In `AUDIT/_RELOC-*.md`, `AUDIT/_DECISIONS.md`, and `AUDIT/CHANGELOG.md` entries dated before 2026-09-20, **only** name-token replacements (rules 1–4: Raka/Darma/Sari/Bayu/Amara/Nadia families) were applied; dated reasoning prose (relocation rationales, Tebet/SSW/migrant-era analysis) was left verbatim as a record of superseded canon. The same rule was extended to all other `AUDIT/*` files and dated coordinator notes (e.g. `35_CANON_DATABASE.md:534`). Tebet/SSW/migrant/kos tokens surviving in those files are therefore **deliberate historical residue**, not misses — every such hit was reviewed and confirmed as either a dated record or a legitimate world-context (Jakarta geography, regional labor migration, Liwanag City texture, OFW/diaspora beats). Name tokens (Raka/Wijaya/Bayu Santoso/Anindya/Darma Wijaya/Sari Wijaya/Nadia Kusuma/Amara Diallo) are zero tree-wide; the only intentional exceptions are the OLD→NEW record tables in `_rename_registry.md` and `_charpatch_protagonist.md` §§6–7.

Affected Files: AUDIT/*, 35_CANON_DATABASE.md (note preserved), 21_CITIES.md:331 (historical aside reworded to avoid a false claim).

Status: Documented 2026-09-20.

## v1.5 — 2026-09-20 — [MYSTERY PATCH] Mystery architecture & foreshadowing audit: filing jurisdiction seam

[MYSTERY PATCH]

Issue: "Filed by BPF Jakarta" (29 B.1) vs the SMD's Ravenscroft file — apparent jurisdictional contradiction (A-14).

Previous Canon: Both statements, unconnected.

New Canon: The vector was opened in Jakarta (1996, Yusuf); the 2017 Ravenscroft transfer was never reported by anyone, so jurisdiction never formally moved. The SMD's Ravenscroft file is the thin local copy. Both statements true; the seam is now a clue about institutional attention (29 B.1, "Filing status" paragraph).

Affected Files: 29_PROTAGONIST_ANOMALY.md.

Status: CANON 2026-09-20.

## v1.5 — 2026-09-20 — [MYSTERY PATCH] Mystery architecture: new DATABASE files + audit

[MYSTERY PATCH]

Issue: The bible had no mystery database, knowledge map, foreshadowing chains, red-herring registry, dependency graph, reveal order, or mystery-architecture audit.

Previous Canon: N/A (new files).

New Canon: DATABASE/MYSTERIES.md (102 mysteries: 38 major, 64 minor; closed L5 set of 5 preserved); DATABASE/INFORMATION_KNOWLEDGE_MAP.md (24 secrets × 5 actors × 4 phases); DATABASE/FORESHADOWING.md (38 clue chains, 142 typed entries, 5 gaps found — 3 repaired, 2 closed by verification — 6 weak clues strengthened); DATABASE/RED_HERRINGS.md (36 registered, 6 misdirections, 7 unregistered candidates); DATABASE/MYSTERY_DEPENDENCIES.md (15 hard / 9 soft dependencies, 6 collision risks); DATABASE/REVEAL_ORDER.md (4-phase reveal schedule, L5 protection); AUDIT/MYSTERY_ARCHITECTURE_AUDIT.md (four tests: dead-end, over-mystification, emotional-impact, archive-omniscience — all pass). MYSTERY-005 upgraded from provisional thread to scheduled mystery per 33 §8's audit clause.

Affected Files: DATABASE/* (new), AUDIT/MYSTERY_ARCHITECTURE_AUDIT.md (new).

Status: CANON 2026-09-20.

[POWER PATCH]

Issue: 04_POWER_SYSTEM.md §4.8 conflated Arthur's ratchet (lag-seconds, a tether property) with the Fathom/Drowning band (Attuned Erosion), implying Arthur is on a Drowning trajectory — contradicting his CANON zero-Fathom, non-Attuned status.

Previous Canon: "(Arthur's ratchet climbs *toward* this band — the endgame's physics is the Drowning watch with his name on it.)"

New Canon: The parallel is now stated as institutional, not physical — Arthur accrues no Fathoms; the ratchet is measured in lag-seconds; what climbs toward the Drowning watch is his *file*, because a man holding a lengthening window onto the Undertow presents the same attention economics as a man dissolving into it.

Affected Files: 04_POWER_SYSTEM.md (§4.8).

Status: CANON 2026-09-20.

[POWER PATCH]

Issue: 29_PROTAGONIST_ANOMALY.md's escrow "auto-sync" described the Laggard's shadow holding prints out-of-phase *between weekly check-ins*, contradicting Use 7's stated rule that shadow-storage retrieval must occur within the lag window (hours, not weeks) — the drafter's parenthetical equated the weekly check-in interval with the lag window.

Previous Canon: "he photographs each new entry and drops the print into the shadow at deep lag; the shadow holds it out-of-phase until the next check-in handoff (this is why the check-in is weekly: the storage window is the lag window)."

New Canon: The shadow leg is a covert courier, not a vault — during the weekly check-in deep-lag session the shadow carries prints out-of-phase past surveillance to that session's handoff; nothing survives in the shadow between check-ins; a missed session's entries travel by the lawyer/journalist legs alone (the redundancy's purpose). Use 7's window rule now governs the escrow consistently.

Affected Files: 29_PROTAGONIST_ANOMALY.md (B.11, Use 10 escrow).

Status: CANON 2026-09-20.

[CORRECTION]

Issue: Phase-4 CHANGELOG prose recorded the mystery database as "102 mysteries: 38 major, 64 minor," but the Phase-4 C-domain integration added MYSTERY-103, MYSTERY-104, and MYSTERY-105 (see DATABASE/MYSTERIES.md counts header and 35_CANON_DATABASE.md rows). The canon was correct; only the changelog/manifest prose was stale.

Previous Text: "DATABASE/MYSTERIES.md (102 mysteries: 38 major, 64 minor...)".

Corrected Record: DATABASE/MYSTERIES.md holds 105 mysteries (41 major, 64 minor; 5 closed L5 intentional mysteries among the majors; 1 answered-in-canon). No canon content changed by this correction.

Affected Files: AUDIT/CHANGELOG.md (this entry); 38_MANIFEST.md (MYSTERIES row corrected).

Status: CANON 2026-09-20.

[POWER PATCH]

Issue: Dr. Amara Nwosu (CHAR-031) held three mutually exclusive affiliations across canon files — 29_PROTAGONIST_ANOMALY.md (Part A and B.9) placed her in the Compact science directorate; DATABASE/CHARACTERS.md and 35_CANON_DATABASE.md listed her as Director, Vesper Tide-Medicine Division; 11_CORPORATIONS.md said Dr. Emil Hartmann "runs the Tide-medicine division." Flagged by the Phase-5 faction-capability inventory.

Previous Canon: Nwosu simultaneously Compact science directorate (29) and Vesper Tide-Medicine Division director (04_PROJECT_STATE/CHARACTERS/35), with Hartmann running the same division (11).

New Canon: Nwosu was Compact science directorate; her longitudinal Erosion paper was suppressed (EVENT-091, 2024-03); Vesper recruited her to direct the Tide-Medicine Division (within Specialty Synthesis, headed by Hartmann — reporting line clarified). The Compact science directorate retains its institutional appetite for unregistered longitudinal subjects but no longer has Nwosu; Vesper's B.9 interest entry now names her as its face ("clinical, consensual, well-funded — and impossible to leave").

Affected Files: 29_PROTAGONIST_ANOMALY.md (Part A line 45; B.9 Compact + Vesper entries); 11_CORPORATIONS.md (CORP-002 leadership); DATABASE/CHARACTERS.md (CHAR-031 row); 35_CANON_DATABASE.md (CHAR-031 row).

Status: CANON 2026-09-20.

[POWER PATCH]

Issue: 06_GOVERNMENTS.md's GOV-002 (China / Jade Office) secrets list omitted the Drowndust stockpile, while 13_MILITARY.md §13.3's Compact assessment (high confidence) names four stockpiling states (US, Russia, China, North Korea) and the US (GOV-001), Russia (GOV-003), and North Korea (GOV-012) profiles all list the stockpile as a secret. Flagged by the Phase-5 faction-capability inventory.

Previous Canon: GOV-002 secrets were (1) Project Vermilion and (2) the Stillwater-dosing proposal only.

New Canon: GOV-002 secrets add (3) a Drowndust stockpile — one of the four the Compact assesses (13_MILITARY.md §13.3); unacknowledged by Beijing and held outside the Office's own ledgers.

Affected Files: 06_GOVERNMENTS.md (GOV-002 secrets list).

Status: CANON 2026-09-20.

## v1.6 — Power progression audit (2026-09-20)

New Canon: DATABASE/POWER_PROGRESSION.md (power-system map A–Q: 5 disciplines, 12 Laggard uses, 6 hard-capped core abilities, Erosion/Fathom economics, ratchet budget, 7-stage protagonist curve, canon-status ledger); AUDIT/POWER_PROGRESSION_AUDIT.md (18 sections: 74 power mechanics analyzed, 28 combination/exploit simulations with classifications, 10-question cost/limitation matrix per major ability, counterplay matrix, multidimensional hierarchy, 28-record faction capability audit, 1000-chapter stress test at ch. 50/100/200/300/500/700/1000, ceiling audit, protagonist-vs-world test, deus-ex-machina audit, 4 patches, 16 intentional exceptions, 7 unresolved UNKNOWNs; verdict: 1000-chapter viable, GO for Faction & Conflict Engine audit).

Affected Files: DATABASE/POWER_PROGRESSION.md (new); AUDIT/POWER_PROGRESSION_AUDIT.md (new); 04_POWER_SYSTEM.md (§4.8 ratchet wording); 29_PROTAGONIST_ANOMALY.md (B.11 escrow; Nwosu entries); 11_CORPORATIONS.md (CORP-002 leadership); 06_GOVERNMENTS.md (GOV-002 secrets); DATABASE/CHARACTERS.md + 35_CANON_DATABASE.md (CHAR-031 rows); 00_INDEX.md + 38_MANIFEST.md (v1.6).

Invariants Verified Unchanged: ANOMALY-001 mechanism (tether, not shadow); inheritance chain (proximity + Loudness, unengineered); March 2017 Ravenscroft transfer (Yusuf → Arthur); Reed Arthur identity (24, Ravenscroft native, vocational college graduate, night-shift records clerk, 1K ¥48,000/month); all character/faction/anomaly IDs.

Status: CANON 2026-09-20.

## v1.7 — Faction & conflict engine audit (2026-09-20)

New Canon: DATABASE/FACTIONS_AND_CONFLICTS.md (faction & conflict database A–K: 88 organization-like IDs — 81 registered GOV/INTL/CORP/REL/SUP/CRIM/IND/RES + 7 auxiliary ACAD/NET/MED; 22-faction relationship matrix condensed; 5 alliance structures + 5 volatile rivalries; full conflict records for 50 RC + 52 CG with parties/objectives/stakes/status/Arthur-dependence/second-order consequences; conflict dependency graph; dead-conflict classification; information hierarchy; government response patterns; corporate/economic conflict map; 4 response simulations; antagonist audit); AUDIT/FACTION_CONFLICT_ENGINE_AUDIT.md (17 sections: autonomy tests — 28/28 factions AUTONOMOUS, 0 DEPENDENT; 102/102 conflicts ACTIVE without Arthur — 87 fully independent, 15 Arthur-instanced, 0 Arthur-required; relationship matrix audit — 132 cells verified, Bell AT-WAR/RIVALS count corrected to 13 of 21; alliance/rivalry audit; second/third-order consequences; government, corporate, and information-hierarchy audits; response simulations; antagonist audit; dependency graph; dead-conflict classification — 0 dead, 6 overlap candidates ruled interlocks/parallels/finale; 2 contradiction candidates investigated → 0 genuine → 0 [FACTION PATCH]es; 8 intentional exceptions; 7 unresolved UNKNOWNs; verdict: enough independent conflict engines — YES, GO for Romance Architecture audit).

Affected Files: DATABASE/FACTIONS_AND_CONFLICTS.md (new); AUDIT/FACTION_CONFLICT_ENGINE_AUDIT.md (new); 00_INDEX.md (v1.7; mystery counts corrected to 105/41/64; added POWER_PROGRESSION rows omitted in v1.6); 38_MANIFEST.md (v1.7; 93 files). No canon file required patching — zero [FACTION PATCH]es; two investigated tensions (SUP-003 hidden Silence faction; CG-044 cross-sovereign absorption) ruled intentional design with written rulings in the audit.

Invariants Verified Unchanged: ANOMALY-001 mechanism (tether, not shadow); inheritance chain (proximity + Loudness, unengineered); March 2017 Ravenscroft transfer (Yusuf → Arthur); Reed Arthur identity (24, Ravenscroft native, vocational college graduate, night-shift records clerk, 1K ¥48,000/month); all character/faction/anomaly IDs; no chapters, scenes, prose, dialogue, or story outlines created.

Status: CANON 2026-09-20.

## v1.8 — 2026-09-20 — Romance Architecture audit (Phase 7)

### [ROMANCE PATCH] 1 — CG-041 "Saitō is the under-redacted source" contradicts the Phase-3 charpatch ruling
- **Problem:** DATABASE/FACTIONS_AND_CONFLICTS.md CG-041's Arthur-dependence cell named "Saitō is the under-redacted source."
- **Discovery:** Phase 7 information-asymmetry extraction; verified against 25_TIMEmessaging app.md EVENT-097's authoritative row ("anonymous NQA claim-files cache") and the Phase-3 charpatch ruling (CANON): the Static Hour contact beat was Bayu-specific and deliberately NOT transferred to Saitō.
- **Change:** Cell now reads: "NO — Arthur can kill, feed, or *shape* the story via one clerk-chosen document; the cache's source is unidentified (EVENT-097's anonymous-cache ruling stands — the Phase-3 charpatch deliberately did not transfer the Static Hour contact beat to CHAR-015)."
- **Reason:** Stale residue contradicted a CANON-LOCKED charpatch ruling.
- **Affected files:** DATABASE/FACTIONS_AND_CONFLICTS.md (CG-041 row).
- **New risk:** None — MYSTERY-011's sender remains a genuine open thread (four in-world candidates).
- **Status:** CANON 2026-09-20.

### [ROMANCE PATCH] 2 — DATABASE/EVENTS.md EVENT-097's stale Saitō beat
- **Problem:** DATABASE/EVENTS.md EVENT-097 convenience row read "Anonymous NQA claim-files cache; Saitō's (CHAR-015) Static Hour contact."
- **Discovery:** Same Phase 7 extraction; contradicts 25_TIMEmessaging app.md's authoritative row.
- **Change:** Row now reads: "Anonymous NQA claim-files cache (sender unidentified — MYSTERY-011; per the Phase-3 charpatch ruling, no CHAR-015 contact beat)."
- **Reason:** Consistency with the charpatch ruling and 25_TIMEmessaging app.md.
- **Affected files:** DATABASE/EVENTS.md (EVENT-097 row).
- **New risk:** None — convenience view only.
- **Status:** CANON 2026-09-20.

### [ROMANCE PATCH] 3 — Kira's base: "Liwanag-based" vs "Ravenscroft-based"
- **Problem:** 21_CITIES.md:397 listed "RES-001 Meridian Institute (stringers like CHAR-033 Kirana "Kira" Maheswari, Liwanag-based)."
- **Discovery:** Phase 7 extraction; contradicts 32_ROMANCE_FRAMEWORK.md §32.2B ("freelance Quiet-care counselor based in Ravenscroft") and DATABASE/CHARACTERS.md.
- **Change:** Changed to "Ravenscroft-based."
- **Reason:** Philippines-primary-era leftover; Tanaw's RES-001 presence is kept, no Liwanag work circuit invented.
- **Affected files:** 21_CITIES.md; 37_FINAL_WORLD_BIBLE.md (rebuilt).
- **New risk:** None.
- **Status:** CANON 2026-09-20.

### Phase 7 audit summary
- **Problem:** Romance architecture needed architectural audit before story design.
- **Discovery:** Ecosystem sound; five structural configurations; zero forced romance; 37/37 characters independently motivated; three genuine contradictions (patched above); two candidates ruled out (Nadia Kusuma residual — zero hits tree-wide, stale coordinator note; D-03 direction — comprehension vs exploration-flow distinction, intentional).
- **Change:** New files: DATABASE/ROMANCE_ARCHITECTURE.md; AUDIT/ROMANCE_ARCHITECTURE_AUDIT.md. 00_INDEX.md → v1.8. 38_MANIFEST.md rebuilt.
- **Reason:** Per spec §24.
- **Affected files:** DATABASE/ROMANCE_ARCHITECTURE.md (new); AUDIT/ROMANCE_ARCHITECTURE_AUDIT.md (new); AUDIT/CHANGELOG.md; DATABASE/FACTIONS_AND_CONFLICTS.md; DATABASE/EVENTS.md; 21_CITIES.md; 00_INDEX.md; 37_FINAL_WORLD_BIBLE.md; 38_MANIFEST.md.
- **New risk:** 7 independence watches (1 elevated: CHAR-031 Nwosu); 2 trope watches; 1 requirement (CG-044 vs Nadia's routine — disproof on-page first); 12 unresolved UNKNOWNs. All recorded in the audit.
- **Status:** CANON 2026-09-20.

Invariants Verified Unchanged: ANOMALY-001 mechanism (tether, not shadow); inheritance chain (proximity + Loudness, unengineered); March 2017 Ravenscroft transfer (Yusuf → Arthur); Reed Arthur identity (24, Ravenscroft native, vocational college graduate, night-shift records clerk, 1K ¥48,000/month); all character/faction/anomaly IDs; established relationships, history, personality traits, supernatural rules; no chapters, scenes, prose, dialogue, or story outlines created.

---

## Phase 8 — Story & Arc Architecture (2026-09-20)

### [STORY PATCH] 1 — MYSTERY-019's wrong EVENT-061 citation
- **Previous Canon:** DATABASE/MYSTERIES.md MYSTERY-019's core question cited "(EVENT-061)" for the 1975–76 Choir preacher who "sang the pressure"; EVENT-061 also appeared in RELATED.
- **New Canon:** (EVENT-061) removed from the core question and RELATED. EVENT-061 is "The Dolly Static (1996)" (biotech/cloning), unrelated to the 1975–76 incident. The preacher incident is canon-supported in-world fact (see MYSTERY-019's OBJECTIVE TRUTH) with no EVENT ledger entry assigned. [STORY PATCH] annotations left in the file for audit traceability.
- **Reason:** Wrong-number citation (the mystery worker flagged it; coordinator verified against DATABASE/EVENTS.md and 25_TIMEmessaging app.md).
- **Affected files:** DATABASE/MYSTERIES.md; AUDIT/CHANGELOG.md; AUDIT/STORY_ARCHITECTURE_AUDIT.md.
- **New risk:** None — no content changed, only the wrong pointer removed.
- **Status:** CANON 2026-09-20.

### Non-patch sequencing correction — CG-048 auction re-windowed to ~400–450
- **Previous state:** The faction extraction worker inferred the Second Silence Auction (CG-048) at ~ch. 750.
- **Correction:** Sequencing only (no canon content changed): the canon edge CG-043→CG-048→ARC VIII (the page surfaces in ARC VIII's climax; Arthur authenticates it "on his terms" as CG-048's key lot) requires the auction to precede ARC VIII. CG-043 staged at ARC V (~280–380); the auction opens ARC VIII (~400–450). Recorded in STORY_ENGINE.md §11.6.
- **Status:** CANON 2026-09-20.

### Open canon tension (NOT patched) — CG-029's site
- **Tension:** 31_CONFLICT_ENGINE.md CG-029 sites the warded skyscraper in Jakarta (GOV-004 permits); CG-050 ties the same development to Yūko's house in Ravenscroft.
- **Disposition:** Recorded open per the no-silent-fix rule. The story architecture requires one site or parallel Helios developments before the ward-anchor crisis (~ch. 650–700). Recorded in STORY_ENGINE.md §11.7 and AUDIT/STORY_ARCHITECTURE_AUDIT.md §18.
- **Status:** OPEN 2026-09-20.

### Phase 8 audit summary
- **Problem:** Story & arc architecture needed macro-architectural design before chapter planning.
- **Discovery:** 12 earned arcs (8–15 band); 105 mysteries integrated with 0 premature reveals; 7-stage power curve with 0 jumps; 28/28 factions autonomous; 5 romance configurations gated and unforced; 60-kind palette with 0 within-phase repeats (2 endgame-kind intentional exceptions); 7/7 stress-test checkpoints PASS; 1 genuine contradiction (patched); 1 genuine tension (recorded open); 1 worker-draft error dispositioned as not-canon (the validation draft's EVENT-100/transfer claim — canon holds EVENT-079; no canon file affected).
- **Change:** New files: DATABASE/STORY_ENGINE.md; DATABASE/ARC_ARCHITECTURE.md; DATABASE/ARC_DEPENDENCY_GRAPH.md; DATABASE/LONG_SERIAL_STRUCTURE.md; AUDIT/STORY_ARCHITECTURE_AUDIT.md. 00_INDEX.md → v1.9. 37_FINAL_WORLD_BIBLE.md rebuilt. 38_MANIFEST.md rebuilt.
- **Reason:** Per spec §24 (Phase 8: story engine, 8–15 major arcs, dependency graph, long-serial structure, endgame direction; macro architecture only).
- **Affected files:** All five new files; 00_INDEX.md; AUDIT/CHANGELOG.md; DATABASE/MYSTERIES.md ([STORY PATCH] 1); DATABASE/ARC_ARCHITECTURE.md (kind-label corrections §10, §13 reconciliation, §14 endgame-kind exception); DATABASE/STORY_ENGINE.md (§11 adjudications 5–8); 37_FINAL_WORLD_BIBLE.md (rebuilt); 38_MANIFEST.md (rebuilt).
- **New risk:** 4 Chapter Engine preconditions (CG-029 site decision before ~ch. 650; Peal-vs-Front decision before ~ch. 850; romance-configuration selection; Approach-band pile-up staging); 1 adjacency watch (ARC I→II share the 60 family across the P1/P2 boundary); 12 story-layer UNKNOWNs. All recorded in the audit.
- **Status:** CANON 2026-09-20.

Invariants Verified Unchanged: ANOMALY-001 mechanism (tether, not shadow); inheritance chain (proximity + Loudness, unengineered); March 2017 Ravenscroft transfer (Yusuf → Arthur, EVENT-079); Reed Arthur identity (24, Ravenscroft native, vocational college graduate, night-shift records clerk, 1K ¥48,000/month); all character/faction/anomaly IDs; established relationships, history, personality traits, supernatural rules; no chapters, scenes, prose, dialogue, or story outlines created.

## Phase 9 — Chapter Engine Architecture (2026-09-20)

### Phase 9 summary — machine built, zero patches
- **Problem:** The macro story architecture needed a formal chapter-generation system before any chapter planning could begin.
- **Discovery:** Four parallel drafting workers produced 8 framework/tracking files (~35,700 words); the coordinator verified every deliverable against canon (all referenced IDs resolve; all 105 mystery IDs covered; all CHAR-001–037 covered; all prose references resolve), ran 5 hypothetical-range coherence tests (ch. 1–10, 11–20, 21–30, 31–50, 51–100 — all PASS), and ran a full §33 consistency scan (0 broken IDs, 0 broken references, 0 contradictions, 0 retcons — working tree differs from v1.9 by exactly 8 file additions, 0 modifications). 0 genuine issues found; 0 patches required.
- **Change:** New files: DATABASE/CHAPTER_ENGINE.md; DATABASE/INFORMATION_FLOW.md; DATABASE/CHAPTER_MYSTERY_TRACKER.md; DATABASE/CHAPTER_FORESHADOWING_TRACKER.md; DATABASE/CHARACTER_STATE_TRACKER.md; DATABASE/DAICHI_PROGRESS_TRACKER.md; DATABASE/CHAPTER_HOOK_SYSTEM.md; DATABASE/LONG_TERM_CONTINUITY.md; AUDIT/CHAPTER_ENGINE_AUDIT.md. 00_INDEX.md → v2.0. 38_MANIFEST.md rebuilt.
- **Reason:** Per spec §§3–30 (Phase 9: chapter-generation framework, information/mystery/foreshadowing tracking, character/Arthur state tracking, hook system, 1000-chapter memory, 16 failure modes; the machine, not chapters).
- **Affected files:** All nine new files; 00_INDEX.md; AUDIT/CHANGELOG.md; 38_MANIFEST.md.
- **New risk:** 4 Chapter Engine preconditions remain open parameters (CG-029 site before ~ch. 650; Peal-vs-Front before ~ch. 850; romance-configuration selection — the engine is config-agnostic; Approach-band pile-up staging); planning-worker / consistency-worker role assignment for the 12-step batch protocol is a blueprint-stage operational decision.
- **Status:** CANON 2026-09-20.

### Discrepancy investigated, ruled out — task-brief "12 intentional UNKNOWNs" vs canon's closed L5 set of five
- **Previous state:** The Phase 9 task brief's project-status line described "12 intentional UNKNOWN mystery elements."
- **Disposition:** Canon is explicit and triple-sourced (DATABASE/MYSTERIES.md counts + status key + L5 note; AUDIT/MYSTERY_ARCHITECTURE_AUDIT.md §2 TEST 2 and §6) that the closed L5 set is five and must not be expanded. The "12" conflates the 12 story-layer and 12 romance-layer UNKNOWN items from Phases 7–8. The mystery tracker implements the canon five and documents the discrepancy in DATABASE/CHAPTER_MYSTERY_TRACKER.md §3. No canon file changed.
- **Status:** RULED OUT 2026-09-20.

### Discrepancy investigated, ruled out — "81 org IDs" vs "88 org IDs"
- **Previous state:** A drafting worker noted DATABASE/FACTIONS_AND_CONFLICTS.md profiles 81 core org IDs while DATABASE/STORY_ENGINE.md mentions 88.
- **Disposition:** Direct count confirms 81 core org IDs (SUP/CRIM/GOV/INTL/CORP/REL/IND/RES) plus satellite IDs (ACAD, MED, NET) ≈ 88 depending on counting scope. Counting-scope difference, not a contradiction. The 28/28 autonomy verdict and 102-conflict count are unaffected.
- **Status:** RULED OUT 2026-09-20.

Invariants Verified Unchanged: ANOMALY-001 mechanism (tether, not shadow); inheritance chain (proximity + Loudness, unengineered); March 2017 Ravenscroft transfer (Yusuf → Arthur, EVENT-079); Reed Arthur identity (24, Ravenscroft native, vocational college graduate, night-shift records clerk, 1K ¥48,000/month); all character/faction/anomaly IDs; established relationships, history, personality traits, supernatural rules; no chapters, scenes, prose, dialogue, titles, or new lore created.

### Phase 11 summary — prose batch 001–005, all PASS
- **Problem:** Convert the Phase-10 blueprints for Chapters 001–005 into polished commercial English prose under strict fidelity constraints (no canon/blueprint alteration; no invented lore; close POV; restrained supernatural; Stage-1 power state; no meta-language in prose).
- **Discovery:** Five drafting workers produced ~11,800 words of prose; two independent audits (structural/fidelity, craft) found zero canon violations, zero leaks, zero overpowering. Coordinator's personal full read + automated re-validation (hidden-vocab, meta-language, leak, power, continuity, repetition scans) identified 6 hard continuity issues and 21 craft issues.
- **Change:** New files: CHAPTERS/001_The_Three-Second_Shadow.md (2,587 words); CHAPTERS/002_Willowmere.md (2,635 words); CHAPTERS/003_Sunday_Dinner.md (2,393 words); CHAPTERS/004_The_Measurement.md (2,021 words); CHAPTERS/005_Saitos_Test.md (2,287 words); AUDIT/PROSE_001_005_AUDIT.md (5/5 chapters PASS across all 14 dimensions; 27 prose-only patches recorded; 4 WATCH carry-forwards). 27 prose-only patches applied: corridor clock/location unified across 001/004/005; zipper pull key ring (001/004); rent dates aligned (001/002); ch. 003 meal contradiction closed against ch. 002; ch. 004 alarm anchored to the canon 15:00 wake; shift-label fix; opener and repetition trims; ch. 005 introspection trim. 00_INDEX.md → v2.1. 38_MANIFEST.md updated.
- **Reason:** Per Phase-11 task: write chapters 001–005 only, audit, and stop.
- **Affected files:** 6 new files; 00_INDEX.md; AUDIT/CHANGELOG.md; 38_MANIFEST.md.
- **New risk:** 4 prose carry-forwards for batch 006–010 (filing-metaphor density; Saitō's false belief must be maintained; Arthur's private log must not surface early; commute mode stays incidental). Chapters 006–020 remain unwritten and untouched.
- **Status:** PROSE PASS 2026-09-20.

Invariants Verified Unchanged (Phase 11): no canon file modified; no blueprint file modified; eight architecture systems remain CANON-LOCKED; DATABASE/CHAPTER_BLUEPRINT_001_020.md untouched; no supernatural mechanics, factions, characters, history, or mystery answers invented; no chapters beyond 005 created.

### Phase 14 summary — prose batch 016–020, all PASS (READY)
- **Problem:** Convert the Phase-10 blueprints for Chapters 016–020 into polished commercial English prose under strict fidelity constraints (no canon/blueprint alteration; no invented lore; close POV; restrained supernatural; Stage-1 power state; no meta-language in prose), closing the P1/ARC I opening movement.
- **Discovery:** Five drafting workers produced 9,889 words of prose (016: 1,949; 017: 1,843; 018: 2,011; 019: 2,009; 020: 2,077). The coordinator audited each chapter sequentially against its binding blueprint, the finalized prior chapters, and the full 001–015 canon before acceptance. Automated scans (leak vocabulary, timeline, ledger tracking, mirror/sighting discipline) found zero canon violations, zero leaks, zero overpowering.
- **Change:** New files: CHAPTERS/016_Sunday_Dinner_Again.md; CHAPTERS/017_The_Badge_Log.md; CHAPTERS/018_The_Unwritten_Rule.md; CHAPTERS/019_The_Photograph.md; CHAPTERS/020_Method.md; DATABASE/CHAPTER_016_020_STATE_SNAPSHOT.md (end-of-ch.20 baseline for ch 21+); DATABASE/CHAPTER_016_020_CAUSALITY.md (15→21 seams); AUDIT/PROSE_016_020_AUDIT.md (24-dimension verdicts: 23 PASS, 1 non-blocking WATCH, 0 FAIL). 6 prose-only patches applied: ch.16 shelf position + B3 route (2); ch.18 ledger priced-presence line (1); ch.19 Saitō-debt duration fix (1); ch.20 ledger shelf orientation + method-carry duration (2). 00_INDEX.md → v2.4. 38_MANIFEST.md updated (143 files).
- **Reason:** Per Phase-14 task: write chapters 016–020 only, audit, and stop.
- **Affected files:** 8 new files; 00_INDEX.md; AUDIT/CHANGELOG.md; 38_MANIFEST.md.
- **New risk:** 3 prose carry-forwards for batch 021+ (the ambiguous 9/18 Nadia overlap stays undetermined — place her deliberately; Saitō's two-second glance (ch.11) and air-pressure look (ch.12) remain unresolved — do not resolve by accident; series-refrain density (21:58 punch-in, "Same time tomorrow") is ritual idiom, not filler — keep varying shift openings). Chapters 021+ remain unwritten and untouched.
- **Status:** PROSE PASS 2026-09-20. Verdict: READY.

Invariants Verified Unchanged (Phase 14): no canon file modified; no blueprint file modified; eight architecture systems remain CANON-LOCKED; DATABASE/CHAPTER_BLUEPRINT_001_020.md untouched; no supernatural mechanics, factions, characters, history, or mystery answers invented; no chapters beyond 020 created; Chapters 001–015 byte-identical (diff-verified against the canonical tree).

### Phase 15 summary — P1 FULL NARRATIVE AUDIT of Chapters 001–020, verdict READY
- **Problem:** Determine whether the completed P1 / ARC I prose (Chapters 001–020, 45,378 words) functions as one continuous opening narrative structurally ready to continue into Chapter 021 — an audit-only task: no new chapters, no canon/blueprint redesign, no new mysteries, the two explicit WATCH items (9/18 overlap UNDETERMINED; Saitō's two-second glance UNRESOLVED) to be preserved, never resolved by implication.
- **Discovery:** Six independent worker audits (prose readers 001–007 / 008–014 / 015–020; mechanics auditor; mystery auditor; world auditor), each a full read of its assigned prose, plus coordinator verification of every flagged item against the actual text, blueprint, and canon docs. All six workers returned READY on their axes. Findings: 0 Severity-1 issues; 1 Severity-2 (ch.11's closing line misdated the cordon — "three nights ago, Sunday, 21:40" vs the verified Monday 9/14 21:40); 5 Severity-3 (tenure wobble "two/three years"; rent-day conflict ch.2 "fifth" vs ch.15 "first"; one Western-order "Arthur Reed"). Several candidate flags were investigated and cleared as false positives or intentional motifs (ch.7 day-labels vs blueprint DATE-TIME; game-streak progression; blueprint-authorized 2020 discharge paper; explained rice ball-day change; deliberate grace-inflation characterization). Both explicit WATCH items verified preserved across all twenty chapters.
- **Change:** 9 prose-only patches applied and diff-verified: 011_Aftershock.md ("two nights ago, Monday, 21:40"); tenure standardized to "two years" across 014 (×1), 017 (×2), 018 (×1), 020 (×1) against the ch.1/2/6/7 majority (the ch.10 "keeper's log" instance is fictional radio drama, untouched); 015_Rent_Day_Arithmetic.md (rent "on the fifth" / "paid September 5th"); 007_No_Category.md ("Reed Arthur"). New file: AUDIT/P1_FULL_NARRATIVE_AUDIT.md (28 sections: executive verdict, macro progression, all 19 transition audits, pacing map, repetition audit, Arthur arc, anomaly progression, mystery progression 001/002/013, information-control audit, character ecosystem, romance, British setting, archive realism, ordinary/supernatural balance, factions, foreshadowing, openings, endings, emotional arc, themes, word counts, WATCH items, issues, patches, remaining WATCHes, P1 end-state, 021+ recommendation). 00_INDEX.md → v2.5. 38_MANIFEST.md updated (144 files).
- **Reason:** Per the P1 audit task: audit only, then stop. Do not generate Chapters 021+.
- **Affected files:** 5 chapter files (6 one-line patches); AUDIT/P1_FULL_NARRATIVE_AUDIT.md (new); 00_INDEX.md; AUDIT/CHANGELOG.md; 38_MANIFEST.md.
- **New risk:** 6 documented carry-forward WATCH items for batch 021+ (9/18 overlap undetermined; Saitō's glance unresolved; ledger as live tracked state; sleep-pattern discipline; refrain density as ritual idiom; Saitō's compounding debt). Chapters 021+ remain unwritten and untouched.
- **Status:** P1 FULL NARRATIVE AUDIT 2026-09-20. Verdict: READY.

Invariants Verified Unchanged (Phase 15): no canon file modified; no blueprint file modified; eight architecture systems remain CANON-LOCKED; DATABASE/CHAPTER_BLUEPRINT_001_020.md untouched; no supernatural mechanics, factions, characters, history, or mystery answers invented; no chapters beyond 020 created; all patches prose-only and minimal (9 lines across 7 files); the two explicit WATCH items preserved unresolved.

### Phase 16 summary — SOP INTEGRATION + prose revision of Chapters 001–020 against the FAST-PACE DEEP-MYSTERY RETENTION SOP, verdict READY
- **Problem:** Integrate the user's new standing editorial document (FAST-PACE DEEP-MYSTERY RETENTION SOP, 36 sections, CANON-ADJACENT / EDITORIAL LOCK, Priority High) into the project verbatim, then revise Chapters 001–020 against it — prose-only, never canon — covering: §17 ASCII romanization of character names; §2 story-state movement; §3 retention triad + §4 micro-hooks; §13/§14/§34 anti-formulaic/vocabulary/craft; §16 decorative-British removal; §8 information density + §18 dialogue; §15 ordinary-life function; §11 human friction + §12 rhythm + §20 ending variety + §22/§23/§24 retention windows; §19 chapter length (1,800–2,500, structural exceptions allowed).
- **Discovery:** Four independent revision workers (001–005 / 006–010 / 011–015 / 016–020), each having read all assigned chapters in full plus all 36 SOP sections, returned per-chapter reports with before/after word counts, §35 gates, and deliberate-unchanged lists. Coordinator re-verified: zero macrons remain in prose (Saito ×187 incl. possessives, Yuko ×8, converted centrally); diff scope = exactly the 20 chapter files + 1 new SOP file; every flagged judgment call (003 dialogue line, 010→011 seam repair, 007/008 day-label tension) investigated — the seam repair uses ch.11's exact wording and adds no fact; the day-label tension is temporally coherent, not a contradiction. British retained only per §16 criteria (完食/彼女は？/kanji search terms/protective charm/Nadia's register/stairwell exchange). Total prose: 45,378 → 44,321 words (−1,057, −2.3%); only genuine filler compressed; ch.14 (2,711) and ch.1 (2,516) retain length under §19's structural clause.
- **Change:** New files: DATABASE/FAST_PACE_DEEP_MYSTERY_RETENTION_SOP.md (verbatim SOP + provenance header); AUDIT/SOP_REVISION_AUDIT.md (per-chapter logs, coordinator verifications, integrity confirmations). Revised: all 20 CHAPTERS files (craft-level tightening; one continuity-repair line added to 010 to match 011's established wording; prose-bug fix in 004). 00_INDEX.md → v2.6. 38_MANIFEST.md updated (146 files).
- **Reason:** Per the user's SOP integration directive: the SOP is now the standing editorial standard for blueprint, prose generation, revision, and narrative audit.
- **Affected files:** 20 chapter files (prose-only revisions); DATABASE/FAST_PACE_DEEP_MYSTERY_RETENTION_SOP.md (new); AUDIT/SOP_REVISION_AUDIT.md (new); 00_INDEX.md; AUDIT/CHANGELOG.md; 38_MANIFEST.md.
- **New risk:** None new. The two explicit WATCH items (9/18 overlap UNDETERMINED; Saito's two-second glance UNRESOLVED) remain preserved; mystery architecture 001/002/013 untouched; Arthur Stage 1 / zero Fathom; romance unlocked; factions untouched. Note: §17 ASCII romanization applies to prose chapters only — canonical database and historical audit documents retain formal romanization; this distinction is documented in the provenance header and the revision audit.
- **Status:** SOP INTEGRATION + CHAPTER REVISION 2026-09-21. Verdict: READY.

Invariants Verified Unchanged (Phase 16): no canon file modified; no blueprint file modified; eight architecture systems remain CANON-LOCKED; DATABASE/CHAPTER_BLUEPRINT_001_020.md untouched; no supernatural mechanics, factions, characters, history, or mystery answers invented; no new mysteries, events, clues, or resolutions introduced; no chapters beyond 020 created; intentional UNKNOWNs preserved; the two explicit WATCH items preserved unresolved; three truth layers intact for every edited passage; all revisions prose-only and minimal (net −1,057 words across 20 chapters, −2.3%).

### Phase 17 summary — NON-NATIVE READABILITY & ACCESSIBILITY STANDARD integrated into the editorial SOP architecture, verdict READY
- **Problem:** Integrate the user's new canonical editorial standard (NON-NATIVE READABILITY & ACCESSIBILITY STANDARD — easy-to-read/hard-to-forget, vocabulary levels 1–4, sentence complexity, mystery complexity rule, figurative control, accessibility test, target reader standard, prose beauty standard, chapter generation requirement, existing chapter revision requirement, revision priority, SOP relationship, final editorial principle) into the existing SOP architecture. Explicit boundaries: no story-architecture redesign, no canon change, no chapter prose rewritten, SOP integration and enforcement wiring only.
- **Discovery:** Full repository search (filenames, headings, content) found NO existing accessibility/readability prose rule — the only "readability" hits elsewhere are incidental word usage (ward readability in audits, "readable" files in the blueprint), not prose standards. The authoritative prose/retention SOP is DATABASE/FAST_PACE_DEEP_MYSTERY_RETENTION_SOP.md (Part I, §§1–36, verbatim user body + provenance header). Per the task's Phase 2, the new standard was integrated INTO that existing MD as PART II (§§37–50, aligned numbering, cross-referenced to §§8/12/13/14/33/34/35) — no duplicate SOP created. The Chapter Engine (DATABASE/CHAPTER_ENGINE.md) is the generation pipeline; AUDIT/NARRATIVE_AUDIT.md is a historical audit report (v1.2), not a standing SOP, and was deliberately left untouched. ARC_ARCHITECTURE.md / STORY_ENGINE.md carry no prose-style hooks and were left untouched per the no-unnecessary-modification rule.
- **Change:** DATABASE/FAST_PACE_DEEP_MYSTERY_RETENTION_SOP.md — provenance header updated to record the addition; §§1–36 byte-identical; PART II appended (§37 primary principle / §38 vocabulary levels 1–4 / §39 sentence complexity / §40 mystery complexity rule / §41 figurative language control cross-referencing §§13/34 / §42 accessibility test / §43 target reader / §44 prose beauty / §45 chapter generation requirement with §35+§50 gate pairing and CHAPTER_ENGINE wiring note / §46 existing-chapter revision requirement / §47 revision priority / §48 SOP relationship + four tension resolutions — §14 rotation vs Level-3 specialized vocabulary (complementary: rotation ≠ removal), §34 vs §41 (same target, two angles), §33.C operationalized by Part II, §13 × §41 one rule one rationale / §49 final editorial principle / §50 READABILITY AUDIT checklist of 15 items, run together with §35). DATABASE/CHAPTER_ENGINE.md — §22 step 12 now names the readability standard as a prose-stage editorial constraint; §24 quality diagnostic checklist gains the READABILITY dimension (ten→eleven dimensions; PASS/WATCH/FAIL criteria defined, WATCH repaired at prose stage, FAIL returns to step 11, plan unchanged). 00_INDEX.md → v2.7 (+ manifest row for the retention/readability SOP; CHAPTER_ENGINE row notes the READABILITY dimension). 38_MANIFEST.md — SOP row updated; build stamp → v2.7 (2026-09-21). File count unchanged: 146.
- **Reason:** Per the user's SOP integration directive: readability is now an editorial constraint for all future chapters (021+), enforced at Chapter Blueprint → Prose Generation → Prose Revision → Narrative Audit → Full Narrative Audit. Workflow chain now reads: CANON → STORY/ARC → CHAPTER ENGINE → RETENTION SOP (Part I) → NON-NATIVE READABILITY (Part II) → CHAPTER BLUEPRINT → PROSE → NARRATIVE AUDIT.
- **Affected files:** DATABASE/FAST_PACE_DEEP_MYSTERY_RETENTION_SOP.md; DATABASE/CHAPTER_ENGINE.md; 00_INDEX.md; AUDIT/CHANGELOG.md; 38_MANIFEST.md.
- **New risk:** None new. The standard is explicitly subordinate to CANON/WORLD BIBLE and STORY & ARC ARCHITECTURE; it cannot override canon, mystery architecture, character architecture, or plot. No chapter prose touched; no existing chapter revision performed in this phase (that is separate follow-up work — see follow-up below).
- **Status:** SOP INTEGRATION 2026-09-21. Verdict: READY.
- **Follow-up (not in this phase):** when the user orders a revision pass of Chapters 001–020 against the new readability standard, apply §46–§47: simplify delivery only where §42/§50 flag genuine friction; preserve Arthur's specialized vocabulary, voice, atmosphere, and mystery depth. Do not run that pass unprompted.

Invariants Verified Unchanged (Phase 17): no canon file modified; no blueprint file modified; no mystery/character/faction/power/history file modified; eight architecture systems remain CANON-LOCKED; DATABASE/CHAPTER_BLUEPRINT_001_020.md untouched; no chapters created, deleted, or revised — all 20 CHAPTERS files byte-identical (checksum-verified against the pre-integration tree); §§1–36 of the retention SOP byte-identical (verbatim integrity preserved); no new canon, mysteries, events, clues, or resolutions introduced; the two explicit WATCH items (9/18 overlap UNDETERMINED; Saito's two-second glance UNRESOLVED) untouched; this phase was SOP-document integration only.

### Phase 18 summary — NON-NATIVE READABILITY REVISION PASS, Chapters 001–020, verdict READY
- **Problem:** Execute the controlled readability revision pass per the user's 30-section directive, using the integrated NON-NATIVE READABILITY STANDARD (Retention SOP Part II, §§37–50). Boundaries: simplify the delivery, never the idea; no plot/canon/mystery/character/atmosphere changes; no blueprint or architecture edits; no 021+.
- **Discovery:** Four revision workers (001–005 / 006–010 / 011–015 / 016–020) read every chapter in full plus the SOP and blueprints, applied the §8 sentence test to every candidate change, and kept only edits passing the final gate ("easier for a non-native reader WITHOUT making the story easier to understand?"). Coordinator independently verified every diff hunk-by-hunk against the pre-pass originals. The prose was already close to standard after two prior revision phases, so the pass is deliberately light: 3,154 sentences reviewed, 29 changed (0.9%), 31 classified edits (CLEARER_WORDING ×20, SENTENCE_SIMPLIFICATION ×7, AMBIGUITY_REDUCTION ×2, IDIOM_CLARIFICATION ×1, CONTEXTUAL_ANCHOR ×1). Honest zeros on 5 chapters (003, 008, 012, 013, 015) and zero edits on 020 "Method" (thesis lines kept byte-identical). §50 audit: 297/300 PASS, 3 WATCH (deliberate voice/doctrine retentions), 0 FAIL. Specialized vocabulary preserved throughout (manifest, discrepancy, requisition, cordon, falsification, etc.; rotation ≠ removal); cultural vocabulary preserved (convenience store, rice ball, protective charm, messaging app, Indonesian register); no macron regressions; ASCII names intact.
- **Change:** 15 of 20 CHAPTERS files revised (phrase-level only); 5 unchanged. New: AUDIT/READABILITY_REVISION_REPORT_001_020.md (§28 full report), AUDIT/READABILITY_WORKLOG_BLOCK_A.md–_D.md (per-chapter records with checksums and §50 tables), AUDIT/READABILITY_DIFFS/*.diff (20 unified diffs vs pre-pass originals), AUDIT/_BASEmessaging app_READABILITY.txt (pre-pass checksums + word counts). 00_INDEX.md → v2.8. 38_MANIFEST.md updated (151 files).
- **Reason:** Per the user's directive: prose must remain accessible to non-native English readers (easy words + deep ideas) without simplifying the story, mystery, characterization, or atmosphere.
- **Affected files:** 15 chapter files (readability-only prose revisions); 26 new audit files (1 §28 report, 4 block worklogs, 20 unified diffs, 1 baseline record); 00_INDEX.md; AUDIT/CHANGELOG.md; 38_MANIFEST.md.
- **New risk:** None. All 31 edits readability-only; no plot/event/decision/timeline/ending/foreshadowing changes.
- **Status:** READABILITY REVISION PASS 001–020 2026-09-21. Verdict: READY.

Invariants Verified Unchanged (Phase 18): no canon file modified; no blueprint file modified; no mystery/character/faction/power/history file modified; eight architecture systems remain CANON-LOCKED; DATABASE/CHAPTER_BLUEPRINT_001_020.md untouched; no chapters created, deleted, or revised beyond the 15 readability-only prose passes; chapter order, timeline, endings unchanged; the two explicit WATCH items (9/18 overlap UNDETERMINED; Saito's two-second glance UNRESOLVED) untouched; Mystery 001 unresolved / 002 slow-seed / 013 doctrine-only; three truth layers intact for every edited passage; Arthur Stage 1, zero Fathom, "accessible Arthur, not simplified Arthur"; retention functions (curiosity / movement / residue) preserved; word counts stable (44,321 → 44,309, −12 words, −0.03%).

### Phase 19 summary — NARRATIVE QUALITY EXPANSION + CHAPTER 001–020 REVISION, verdict READY
- **Problem:** Integrate the permanent NARRATIVE MOVEMENT VARIETY rules into the existing editorial SOP architecture (no duplicate SOP, no competing pacing system) and perform a surgical revision of Chapters 001–020 against the P1 narrative evaluation's identified weaknesses (conflict variety, supporting-character agency, social friction, emotional depth, external consequence, pacing variety, repeated investigation/procedure patterns, formulaic chapter movement). Boundaries: no story/mystery/power/faction/romance redesign; no timeline, reveal-order, or Ch-020-ending changes; no new subplots, major characters, or supernatural mechanics; protagonist concept unchanged.
- **Discovery:** Phase B — four Reader-Analysts each read five chapters + blueprint sections in full and produced movement/method/agency/ending/repetition matrices. Honest result: 19 of 20 chapters have no genuine weakness (solitary chapters are blueprint-legal by design; the night-shift ritual is the load-bearing ordinary baseline; dependencies like 005's repeat of 004's filming are intentional). The one genuine weakness: CH-018 verbatim-echoes CH-017's opening exchange and closing farewell and repeats its own first stair-trip description in the second trip.
- **Change:** DATABASE/FAST_PACE_DEEP_MYSTERY_RETENTION_SOP.md — PART III added (§§51–60: narrative movement variety with the 12-category taxonomy and ≤3-consecutive rule; investigation repetition control; supporting-character agency; social friction; emotional consequence; external consequence; anti-formula chapter rule; character life outside the mystery; serial pacing rule; Part III tension resolutions), provenance header updated, §45 extended. DATABASE/CHAPTER_ENGINE.md — §22 step 12 names Part III constraints; §24 PACING dimension fails a fourth consecutive same-dominant-movement chapter; §26 cross-references §§51/52/57. CHAPTERS/018_The_Unwritten_Rule.md — MINOR PATCH: greeting line and locker farewell no longer verbatim-repeat 017 (nonverbal beats preserve warmth/intent; two-finger gesture is Takashi's established register), redundant second stair-trip description compressed per XIII.G (2,006 → 1,908 words, −98, −4.9% — excess over the 0.5–3% band is entirely duplicated-description removal, no rewriting). 19 chapters byte-identical. New: AUDIT/NARRATIVE_QUALITY_REVISION_REPORT_001_020.md (Part XVIII full report), AUDIT/NARRATIVE_DIFFS/CH018_The_Unwritten_Rule.diff. 00_INDEX.md → v2.9. 38_MANIFEST.md updated (152 files).
- **Reason:** Per the user's directive: the revision must strengthen variety and human consequence without changing what makes THE QUIET TIDE THE QUIET TIDE — and the rules must be permanent, enforced at Blueprint → Prose → Revision → Audit for all future chapters (021+).
- **Affected files:** DATABASE/FAST_PACE_DEEP_MYSTERY_RETENTION_SOP.md; DATABASE/CHAPTER_ENGINE.md; CHAPTERS/018_The_Unwritten_Rule.md; AUDIT/NARRATIVE_QUALITY_REVISION_REPORT_001_020.md (new); AUDIT/NARRATIVE_DIFFS/CH018_The_Unwritten_Rule.diff (new); 00_INDEX.md; AUDIT/CHANGELOG.md; 38_MANIFEST.md.
- **New risk:** None. Triple approval gate (§35 + §50 + Part III movement check) is defined for future chapters; no gate exists for already-released 001–020 (retro-gate not required by the directive).
- **Status:** NARRATIVE QUALITY EXPANSION + REVISION 001–020 2026-09-21. Verdict: READY.

Invariants Verified Unchanged (Phase 19): no canon file modified; no blueprint file modified; no mystery/character/faction/power/history file modified; eight architecture systems remain CANON-LOCKED; DATABASE/CHAPTER_BLUEPRINT_001_020.md untouched; no chapters created, deleted, or revised beyond the single CH-018 surgical patch; §§1–36 and §§37–50 of the retention SOP byte-identical; chapter order, timeline, endings unchanged; the two explicit WATCH items (9/18 overlap UNDETERMINED; Saito's two-second glance UNRESOLVED) untouched; Mystery 001 unresolved / 002 slow-seed / 013 doctrine-only; three truth layers intact for every edited passage; Arthur Stage 1, zero Fathom; romance unlocked; no information leaks, subplots, major characters, or premature revelations; chapter word counts stable (44,309 → 44,211, −98 words, −0.22% — all from the CH-018 patch).


---

## SECTION: `AUDIT/_DECISIONS.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/_DECISIONS.md` · sha256 `170ab4f2a30f0322abc92bb4b004e9f2e995c2a76529d97f9cc16e5ad886c275` · 2,199 words. No content changed.

# COORDINATOR DECISIONS — THE QUIET TIDE v1.2 (Albion-primary) forensic audit

**Date:** 2026-09-19 · **Status:** recommendations. The patch agent treats a recommendation as **decided**
unless it finds a contradiction — in which case it escalates back here rather than improvising.
Decisions (a), (b), and (f) are **patch-blocking**: FAC-001, FAC-007, and POWER-005 cannot be patched until picked.

---

## Required decisions

### (a) SUP-004 identity — FAC-001 (CRITICAL, patch-blocking)
**The clash:** six files describe the Red Ledger as a gray-market auction house whose Factor brokers
person-attached anomalies (14, 24, 25/EVENT-084/093, 29, 31/RC-017/RC-043/CG-048, 35); one file (12) describes
a Code-bound anti-trafficking PMC that refuses trafficking contracts and returns fees with interest.
**Options:**
1. Keep the 12 PMC; move the Factor and the auctions to the Ash Exchange or a new gray-market actor.
2. Keep the gray-market auctioneer (six files vs. one); rewrite the 12 profile as the Ledger's *public-facing
   Code* — real for the PMC division, while the Factor runs a black-book brokerage the Partners don't
   acknowledge (12 already gives the Ledger a "black book" of Code-violating clients — the infrastructure exists).
3. Split SUP-004 into two registry entries.
**Recommendation: option 2.** The gray-market identity is load-bearing for the novel's central market thread
(EVENT-093 → RC-043 → CG-048); rewriting one profile is cheaper than rewriting six files of staged beats.
The Code survives as the PMC division's genuine operating ethic — which makes the Factor's black book a
*hypocrisy*, and hypocrisy is plot fuel. **Constraint:** whichever way this goes, ECON-009's turnover/force
arithmetic and FAC-002's handful rule must be resolved consistently with the chosen identity.

### (b) Faction registry: aspirational 36 vs profiled 22 — FAC-007 (HIGH, patch-blocking)
**The clash:** the registry is numbered for 36; 22 have profiles. Stubs: SUP-011, IND-006/007/010, REL-008, IND-008/009.
34's header claims 36 but covers 22.
**Options:**
1. Write the missing profiles (five full + stubs).
2. Reduce the registry to the 22 profiled factions; re-tag the rest as reserved namespaces.
3. Minimum: fix 34's header to 22 and delist the stubs from the count.
**Recommendation: option 2, with one exception.** Writing five new profiles pre-patch risks introducing fresh
contradictions. Reduce to 22 and reserve the namespaces. **Exception:** REL-008 already has staged beats
(31:513) — write a short REL-008 profile from the beats' implied doctrine, or cut the beats (see decision (m)).

### (c) Tether-succession legal vacuum — LAW-001 (CRITICAL)
**The clash:** the real transfer mechanism (death-proximity to the nearest Loud witness, 29 §B.8) sits outside
every statute: no title, no probate (CASE-004 excludes non-property), no license category, no recipient duty.
**Options:**
1. One acknowledgment clause in 14 §14.3(2): non-severable tether succession is *legally invisible*; the
   Division's C-A filing is an administrative convenience, not a legal regime.
2. Invent a tether-succession statute.
3. Defer to the Tribunal's CASE-007.
**Recommendation: option 1.** The vacuum is load-bearing — the law's completeness *breaking* at the
protagonist is the theme (LAW-002). Do not legislate the tether; name the gap in one clause so future
patches don't "fix" it by over-legislating.

### (d) SSW visa field mismatch — SOC-001 (HIGH)
**The clash:** Arthur's SSW visa does not legally cover insurance records-clerk work.
**Options:**
1. Make the mismatch deliberate: NQA's Quiet hiring apparatus bent the rules — *someone wanted him inside*
   (EVENT-087's PROVISIONAL hire) — and the irregular paperwork is his precarity engine.
2. Change the visa category to one that covers the work.
3. Change the job to one the visa covers.
**Recommendation: option 1.** It converts the bug into the load-bearing precarity mechanism the Tuesday
problem needs: he can't afford scrutiny because the paperwork doesn't quite hold. **Constraint:** the patch
must tie the irregularity to EVENT-087's redacted approver (decision (n)) — the two threads are one thread.

### (e) Laggard C-A vs C-D filing — POWER-007 (MEDIUM)
**The clash:** the Laggard reads as `C-D` (mobile tracked containment) but is filed `C-A` (05.5:95), which
avoids the Compact's 72-hour reporting trigger.
**Options:**
1. Re-file as `C-D` and explain the buried 72-hour report (requires a cover-up beat).
2. Keep `C-A` with an explicit Classification Office policy line: person-bound anomalies are filed `C-A`
   as policy ("a person cannot be 'uncontained'"), with D-equivalent surveillance.
3. Add a Classification Office guidance note on notation/grammar (pairs with POWER-014).
**Recommendation: option 2 (+3).** The non-reporting stays *institutional*, not corrupt — which is why
nobody in Geneva noticed, why the file "yawned three times," and why the Compact's completeness breaks
exactly at Arthur (the theme again). One policy sentence in 05; the older "MV-T1/C-A/—/Local/Reactive" notes
(POWER-014) become the pre-revision grammar the guidance note explains.

### (f) Which Gilded Cradle Rule survives — POWER-005 (HIGH, patch-blocking)
**The clash:** 28's Erosion-transfer cradle (eleven children, Tribunal prohibition, `C-C/R+P`) vs 30/35's
"keeps what is placed in it" object (`C-B/R/Urban`).
**Options:**
1. Keep 28's Rule; rewrite 30's Scenario 3 around it (Sweepers responding to an unauthorized twelfth use).
2. Keep 30/35's Rule; rewrite 28's entry (loses the eleven children, the trolley problem, four factions' positions).
3. Split into a new ANOMALY-031 (requires amending 28's 002–030 completeness claim).
**Recommendation: option 1.** 28's Rule is the richer, more load-bearing design — the trolley problem, the
Tribunal order, and four factions' positions all hang on it. 30's "exception clause" beat dies, but the
unauthorized-twelfth-use scenario is a better story. **Constraint:** POWER-010's Fathom-reification issue
must be resolved consistently with the surviving Rule (recommend the accounting-metaphor reading: the Cradle
transfers Erosion; "Fathom-debts" is the Compact's bookkeeping language).

### (g) ZONE-006 "Odaiba Wound" rename — GEO-003 (MEDIUM)
**The clash:** a Tokyo place-name on a Ravenshire zone.
**Options:**
1. Rename to a Ravenshire-local name.
2. Keep as an in-world nickname with a stated who-and-why.
3. Move the zone to Tokyo Bay.
**Recommendation: option 1.** Any Albion-literate reader trips on contact; a nickname justification is lore
debt for a copy error. (Suggested direction: a Shiohama/wound-field name — the patch agent picks the exact
name; it must not collide with existing zone names.)

### (h) Meridian Vector vs anomaly-catalog prose authority — POWER-001..004 (HIGH)
**The clash:** 05.5's ratified vectors vs 28's field-truth prose (four anomalies: 006, 012, 013, 030).
**Options:**
1. 05.5 always wins (Compact ratification outranks field catalogs); rewrite 28's status prose.
2. 28's field truth always wins; re-file the vectors in 05.5.
3. Per-case: 05.5 wins *except* where 28's field truth is load-bearing — with an explicit Classification
   Office dispute note per 05.3 (which already says bureaucratic disagreement is the norm).
**Recommendation: option 3, with the per-case calls made now:**
- ANOMALY-006 → 05.5 wins (`C-C`); rewrite 28's "downgraded" line as a posture adjustment, not a reclassification.
- ANOMALY-012 → keep `C-D`; annotate the Seismograph Authority's `E` proposal as an unfiled dispute.
- ANOMALY-013 → keep `C-B` (the threat/containment-orthogonality teaching example is load-bearing); rewrite 28's
  "cannot be sealed" as "cannot be vaulted."
- ANOMALY-030 → keep `C-C`; the Archivists' Charter is a custodian's filing argument, and the `D` filing would
  remove the Compact funding the containment needs.
- ANOMALY-004 → 28 wins (`Reactive`); correct 05.5 (one word, no doctrinal fallout).
**Decision rule for the patch agent:** the ratified vector is the *legal* filing (budgets, triggers, JCC
posture); 28's prose is *field truth* the Classification Office hasn't reconciled. Mark each disputed filing
with a dispute note; do not silently conform either side.

### (i) Romance configuration — SER-002 (MEDIUM)
**The clash:** five romance configurations are staged; serialization can't start with all five live.
**Options:**
1. Choose the primary configuration now, in this audit.
2. Keep all five as canon-neutral framework; defer the choice to the serialization plan (not the patch phase).
3. Merge: make the choice the season-1 arc.
**Recommendation: option 2.** The audit should not choose the novel's romance — but the choice is *required*
before chapter 1, and the serialization plan must record it. Note for that plan: Config E doubles as a
Loud-politics thread, which may weigh the choice.

---

## Further decisions found during consolidation

### (j) The 2023 biennial monitor — PROTAG-013 (LOW)
**Options:** (1) deferred — austerity backlog (RC-040's cost-cutting); (2) completed and passed (the tether read
as T1-curiosity at low lag); (3) completed and suppressed (someone wanted him inside).
**Recommendation: option 1.** The deferral feeds the "protection expiring" plot and explains the paper-trail
gap with the cheapest available cause. (The red team held this for the parent — this is the ruling.)

### (k) The ratchet ruler — PROTAG-001 (MEDIUM)
**Options:** (1) publish the drafter's ruler (~0.25s logged / ~1s unlogged, per-season lag budget) marked
**non-binding**; (2) keep the math diegetic-only with a hidden ledger in 35; (3) pace seasons by Fathoms, not lag-seconds.
**Recommendation: option 1.** The clock needs a legible face for the reader to feel it tighten; marking it
non-binding keeps it a guideline, not hard canon. The 10s ceiling stays untouched (L5-5 governs it).

### (l) Uses 13+ generative principle — SER-001 (HIGH)
**Options:** (1) promote the discovery grammar (observe → hypothesize → test → pay) to a physical principle:
the twelve are the *documented* ladder; force/knowledge-without-interpretation never generates;
(2) tie generation to the ratchet (new lag-depths unlock new observables); (3) cap the ladder at twelve —
post-ladder growth is *combinations*, not inventions.
**Recommendation: option 1** (with 2 as a compatible complement: deeper lag widens the observable set the
grammar works on). This is the conservative choice — no new mechanics, and it directly enforces the
protagonist spec's "never secretly omnipotent" constraint: every new use must be *earned* through the grammar.

### (m) GOV-015/016 stubs — POL-007 (MEDIUM)
**Options:** (1) delist (if 06's profile already covers the SMD charter / Albion accession content);
(2) write minimal entries; (3) merge into adjacent entries.
**Recommendation: option 1, after a coverage check.** The patch agent verifies whether 06's main profile
covers the charter and accession material; whatever is uncovered gets a minimal entry (option 2 for the gap
only). Do not leave stubs.

### (n) The NQA flagged-applicant thread — FAC-008 (HIGH)
**Options:** (1) register as an owned plot thread (the approver is redacted *in-world*, not from the author);
(2) reclassify as a bug (flagged *after* hiring — routine post-hire review); (3) pay it off now (name the approver).
**Recommendation: option 1.** This is the hinge of decision (d) — the SSW irregularity and the flagged hire
are one thread. The patch only needs to ensure EVENT-087's PROVISIONAL entry is registered as a plot thread
with an owner in 31, not silently dropped.

### (o) The Fukushima Rule's two meanings — HIST-005 (LOW)
**Options:** (1) two-clause reading: the Rule *is* both a treaty read-only principle (24/25) and an exported
manage-around doctrine (31/RC-008) — state both in 24; (2) rename RC-008's doctrine; (3) mark practitioners'
misuse as in-world drift.
**Recommendation: option 1.** The treaty weight matters for the history and the doctrine weight matters for
RC-008's staging; the two-clause reading preserves both without renaming anything.

### (p) The ninth site — HIST-002/NAR-005 (HIGH)
**The clash:** the ninth site exists in the plot (31) but the 35 L5 registry doesn't distinguish plot threads
from mysteries; the worker's NAR-005 finding: "the ninth site is a plot thread, not an L5."
**Options:** (1) register the ninth site as a plot thread (owned, in 31), explicitly not an L5;
(2) promote it to an L5-adjacent mystery in 33; (3) correct the 35 row to remove the L5 tag.
**Recommendation: option 1 (+3).** The ninth site is a *location the plot will visit*, not a cosmological
unknown — registering it as a thread keeps the L5 set closed (the closed set is load-bearing; see
`01_CANON_MODEL.md` §3). Fix the 35 row when the database is rebuilt last in the patch order.

---

## Decision log (for the patch agent)
| # | Decision | Pick | Gates |
|---|---|---|---|
| (a) | SUP-004 identity | gray-market auctioneer; 12's Code = PMC division's public ethic, Factor runs black book | FAC-001, LAW-001, ECON-009 |
| (b) | Registry 36 vs 22 | reduce to 22; reserve namespaces; write REL-008 short profile | FAC-007, FAC-013, FAC-017 |
| (c) | Tether-succession vacuum | one acknowledgment clause; do not legislate | LAW-001, LAW-002 |
| (d) | SSW visa mismatch | deliberate via EVENT-087 | SOC-001, POL-007(excl), INFO-001 |
| (e) | Laggard C-A filing | keep C-A; Classification Office policy line | POWER-007, POWER-014 |
| (f) | Gilded Cradle Rule | keep 28's Erosion-transfer Rule; rewrite 30 Scenario 3 | POWER-005, POWER-010 |
| (g) | ZONE-006 rename | rename to Ravenshire-local name | GEO-003 |
| (h) | Vector vs prose authority | per-case rule (calls listed above) | POWER-001..004, POWER-006 |
| (i) | Romance config | defer to serialization plan; choose before chapter 1 | SER-002 |
| (j) | 2023 monitor | deferred (austerity backlog) | PROTAG-013 |
| (k) | Ratchet ruler | publish non-binding drafter's ruler | PROTAG-001 |
| (l) | Uses 13+ principle | discovery grammar as physical principle | SER-001 |
| (m) | GOV-015/016 | delist after coverage check; fill gaps minimally | POL-007 |
| (n) | NQA flagged hire | register as owned plot thread | FAC-008, decision (d) |
| (o) | Fukushima Rule | two-clause reading in 24 | HIST-005 |
| (p) | Ninth site | plot thread, not L5; fix 35 row at rebuild | HIST-002 |


---

## SECTION: `AUDIT/_rename_registry.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/_rename_registry.md` · sha256 `37ad919a2480d7fca2c36810318f6d0db6a3c975bf3405b08792a4c3d5d03e52` · 1,376 words. No content changed.

# RENAME REGISTRY — Character Naming Canon, Phase 3 (2026-09-20)

> Complete OLD NAME → NEW NAME table for the prose-sweep agent, plus collision fixes and family-structure notes. IDs never change. This registry is authoritative for name replacement in all prose; `DATABASE/JAPANESE_CHARACTER_NAMES.md` carries the kanji/readings for British characters.

## 1. Renames (OLD → NEW)

| ID | Old name | New name | Reason |
|---|---|---|---|
| CHAR-001 | Raka Wijaya | **Reed Arthur** (森 大地) | Mandated protagonist rewrite: ordinary native British male, 24, Ravenscroft. |
| CHAR-008 | Amara Diallo | **Fatoumata Diallo** | Given-name collision with CHAR-031 Dr. Amara Nwosu (both female principals). Kept the established surname Diallo; Fatoumata is a natural Senegalese/Mande female given name, era-plausible for a Compact SG. |
| CHAR-016 | Nadia Kusuma | **Nadia Puspita** | Duplicated surname with CHAR-005 Director-General Ratna Kusuma (unrelated characters; prose sharing the surname implies a relation that doesn't exist). Kept established given name Nadia; Puspita is a natural Indonesian surname with no canon collisions. |

## 2. Prose-sweep alias table

Apply in prose, case-sensitively where applicable. Longest match first.

| Old prose form | New prose form | Notes |
|---|---|---|
| Raka Wijaya | Reed Arthur | Full-name mentions (events, reports, files). |
| Raka | Arthur | Standalone given-name mentions. |
| Raka's | Arthur's | Possessives. |
| the Wijaya boy | the Reed boy | `25_TIMEmessaging app.md` EVENT-098 ("Ashworth asks after 'the Wijaya boy'"). |
| Raka's novel | Arthur's novel | `14_LAW_ENFORCEMENT.md` §79 ("For Raka's novel: …"). |
| Raka's story | Arthur's story | `14_LAW_ENFORCEMENT.md` §79 ("When Raka's story collides…"). |
| Amara Diallo | Fatoumata Diallo | Full-name mentions of the Compact SG. |
| Secretary-General Amara Diallo | Secretary-General Fatoumata Diallo | Titled mentions. |
| Amara (SG context) | Fatoumata | ⚠️ Disambiguate: standalone "Amara" may also mean Dr. Amara Nwosu (CHAR-031) or the prose-only Dr. Amara Eze (`12_FACTIONS.md` SUP-011). Replace only when the referent is the Compact Secretary-General. |
| Nadia Kusuma | Nadia Puspita | All mentions of CHAR-016. |
| Nadia (CHAR-016 context) | Nadia | Standalone "Nadia" is unambiguous in canon — no change needed. |

## 3. Collision fixes applied

| Collision | Finding | Fix |
|---|---|---|
| CHAR-008 vs CHAR-031: identical given name "Amara" (both female speaking principals) | Genuine confusion risk. | CHAR-008 renamed → Fatoumata Diallo. CHAR-031 kept (Amara pairs naturally with Igbo surname Nwosu). |
| CHAR-005 vs CHAR-016: identical surname "Kusuma" (unrelated) | Genuine — shared surname in prose implies a relation that doesn't exist. | CHAR-016 renamed → Nadia Puspita. CHAR-005 kept (more established). |
| Hidayat ×2: CHAR-018 Yusuf Hidayat / CHAR-035 Agus Hidayat | Not a collision — they are brothers; shared surname is correct. | None. |
| Wijaya ×3: CHAR-001 (old) / CHAR-013 Darma Wijaya / CHAR-014 Sari Wijaya | Phase 3b: CHAR-013/014 repurposed to Thomas Reed / Eleanor Reed (see §6). No Wijaya names remain in canon. | Resolved — registry §6. |

**Flagged, NOT changed (for sweep-agent awareness, no action):**
- Prose-only "Lena" (malalim faction leader, `12_FACTIONS.md` CRIM-006) vs CHAR-024 Lena Hoffmann (German investigator, b. 1961). Context disambiguates (1970s–90s European history vs current Ravenscroft Filipino crime politics); renaming a prose-only minor figure would be churn.
- Prose-only "Dr. Amara Eze" (`12_FACTIONS.md` SUP-011 founder figure) vs CHAR-031 Dr. Amara Nwosu. Both are Nigerian-affiliated therapists/researchers, which is a mild echo — but Eze is prose-only with no ID, and the CHAR-008→Fatoumata fix already removes the three-way "Amara" collision. Left for the prose sweep to keep an eye on, not to rename.
- CHAR-021 "Dr. Leonid Kulik (1883–1942)" mirrors a real historical Soviet mineralogist. It is not a placeholder or a nationality mismatch, so per the brief's "fix only clear placeholders or mismatches" rule it was kept. Flagged here for the coordinator's awareness.

## 4. Family-structure audit

**British families:** No married British women appear in the roster; no British parent/sibling/household inconsistencies found. CHAR-001's family (Reed family) is being authored by the parallel protagonist-background agent — this registry does not invent family members.

**RESOLVED — Phase 3b (2026-09-20), per `_charpatch_protagonist.md` §7:**
- CHAR-012 → **Hannah Reed** (森 七海): Arthur's younger sister, 22, ordinary office worker, lives at home; Quiet.
- CHAR-013 → **Thomas Reed** (森 隆): Arthur's father, 58; current mid-level office worker — *department manager* (section chief), parts procurement, local auto-parts manufacturer (Hama-kogyo); Quiet.
- CHAR-014 → **Eleanor Reed** (森 裕子): Arthur's mother, 55; part-time supermarket staff; family folk-heuristic keeper; Quiet.
- CHAR-015 → **Saitō Yūto** (斎藤 悠斗): Arthur's coworker and closest friend, 26; night-shift records clerk, NQA Ravenscroft; also Loud (unacknowledged); Quiet-adjacent civilian. (The Static Hour contact beat, CG-017, was Bayu-specific and was **not** transferred.)
- CHAR-016 **Nadia Puspita** kept as Indonesian migrant (SSW), NQA Ravenscroft claims adjuster, 25; romance A — cross-cultural configuration in the rewritten `32_ROMANCE_FRAMEWORK.md`.
- CHAR-001's `DATABASE/CHARACTERS.md` row reconciled with the patch's employer line: regular-employee night-shift records clerk, NQA Ravenscroft records archive (CORP-011).

**Foreign/Filipino name verification:** all non-British roster names audited against stated nationality — no placeholders or mismatches found, none changed. Specifically: CHAR-010 Tomás Aquino Reyes and CHAR-034 Aisha Rahman are natural Filipino names (Aisha Rahman is plausible for a Filipina-Muslim from the Bangsamoro context) and were **never Albionified**; Indonesian roster names (CHAR-005, 012–018, 026, 032, 033, 035) all natural, kept.

## 5. Files written by this agent

- `DATABASE/JAPANESE_CHARACTER_NAMES.md` (new) — British-name canon table with kanji/readings.
- `DATABASE/CHARACTERS.md` — rows updated for CHAR-001, CHAR-008, CHAR-016 only.
- `_rename_registry.md` (this file) — complete rename/collision/family record.

**Not touched (per brief):** `29_PROTAGONIST_ANOMALY.md`, `AUDIT/*`, `CHANGELOG.md`, `00_INDEX.md`, `38_MANIFEST.md`, `37_FINAL_WORLD_BIBLE.md`, `35_CANON_DATABASE.md`, and all other numbered content files — prose name changes are the sweep agent's job, using §2 above.

---

## 6. Phase 3b — Character repurposing & creation (2026-09-20)

Authoritative definitions: `_charpatch_protagonist.md` §§6–7. IDs never change; only names, biographies, and dramatic functions are (re)assigned.

### 6a. Repurposed (existing IDs, new British identities)

| ID | Old identity | New identity | Kanji / reading | Dramatic function kept |
|---|---|---|---|---|
| CHAR-012 | Anindya "Dita" Rahayu — Arthur's sister (old canon) | **Hannah Reed** | Hannah Reed | Younger-sister beat (interrogation: sleep, food, dark circles, dating); age 29→22, ER-nurse career dropped as migrant-era texture |
| CHAR-013 | Darma Wijaya — Arthur's father (old canon) | **Thomas Reed** | Thomas Reed | Bewildered-proud father beat; current mid-level office worker (*department manager*, parts procurement, local auto-parts manufacturer), not retired |
| CHAR-014 | Sari Wijaya — Arthur's mother (old canon) | **Eleanor Reed** | Eleanor Reed | Folk-heuristic keeper; 2018 *tsuite iru* counselor/*cleansing ritual* guilt beat transplanted from Tebet warung-owner to Willowmere supermarket worker |
| CHAR-015 | Bayu Santoso — Arthur's fellow migrant coworker (old canon) | **Saitō Yūto** | 斎藤 悠斗, さいとう・ゆうと | Deskmate/friend beat; "two Loud people, shared glances at wrong files"; Static Hour contact beat (CG-017) deliberately **not** transferred |

### 6b. Created (new IDs)

| ID | Name | Kanji / reading | Role |
|---|---|---|---|
| CHAR-036 | Okada Kumiko | 岡田 久美子, おかだ・くみこ | 47, Quiet. Night-shift section chief, NQA Ravenscroft records archive; kind, tired; runs the break rotation |
| CHAR-037 | Hasegawa Kenji | 長谷川 健司, はせがわ・けんじ | 34, Quiet. Senior night-shift records clerk, NQA Ravenscroft; ten years on nights; Arthur's dry mentor |

### 6c. Prose-sweep aliases (append to §2)

Apply longest-match-first, alongside §2:

| Old prose form | New prose form | Notes |
|---|---|---|
| Anindya "Dita" Rahayu | Hannah Reed | Full-name mentions of CHAR-012 (old canon) |
| Darma Wijaya | Thomas Reed | Full-name mentions of CHAR-013 (old canon) |
| Sari Wijaya | Eleanor Reed | Full-name mentions of CHAR-014 (old canon) |
| Bayu Santoso | Saitō Yūto | Full-name mentions of CHAR-015 (old canon) |
| Anindya | Hannah Reed | Standalone |
| Dita | Nanami | Standalone (incl. quoted 'Dita') |
| Rahayu | Nanami | Standalone surname |
| Darma | Takashi | Standalone |
| Sari | Yūko | Standalone ("Ibu Sari" constructions reworded, not mechanically replaced) |
| Bayu | Saitō | Standalone |

**Sweep status:** all §2 + §6c aliases applied tree-wide (2026-09-20, final-sweep agent); zero residual hits for every old form except in this registry's own OLD→NEW record and the struck-through historical notes.


---

## SECTION: `AUDIT/REMAINING_RISKS.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/REMAINING_RISKS.md` · sha256 `f52fb8e9f26df56c063492823d0d73df712df0266b1d5582401464affe3ea6fd` · 709 words. No content changed.

# REMAINING RISKS — THE QUIET TIDE World Bible

> Build: FINAL_WORLD_BIBLE · Date: 2026-09-19
> Policy: CRITICAL/HIGH issues must be eliminated or explicitly explained. None remain unexplained.

## CRITICAL — 0
No world-breaking issue was found in 124 adversarial attacks and 10 world simulations, and severity was deliberately not inflated to manufacture any.

## HIGH — 0 unpatched
All 9 HIGH findings were patched in CHANGELOG v1.0 and verified by the coordinator (the treaty chronology, origin dates, Tunguska, the Sweeper arithmetic, Loudness scope, the infohazard doctrine, the Laggard transfer/phasing, and the vector reconciliation were each re-verified on disk). The vector reconciliation (F-M4) touched the protagonist's own filing — the canonical vector is `MV-T1/C-A/—/Local/Unknown` per 05 §5.5; residual risk is limited to future drafters re-introducing the examiners' in-world "Reactive" dodge as a filing, which 29 now explicitly flags as behavior, not filing.

## MEDIUM — residual notes (all patched; these are watch-items, not holes)
1. **Newly invented numbers.** The Sweeper corps table (05/26), clerk sampling math (27), routine Erosion costs (04), and Drowndust production economics (04/13) are new canon invented during patching. They are internally consistent but have not been independently stress-tested against every downstream use. If a future draft leans hard on one of these figures, re-check the arithmetic first.
2. **The infohazard race doctrine (17).** The doctrine shows the Compact *usually* wins the race against a Loudness-inducing infohazard and defines the lost-race protocol. A lost race is a civilization-scale event by design — the bible now owns that consequence rather than hiding it.
3. **Drowndust-vs-Quiet (04/13).** Canon: Quiet lack patterns, so Drowndust's Fathom-forcing mechanism does not affect them — it is an anti-Attuned weapon. This was chosen because it sharpens the arms-control doctrine (states stockpile it precisely because it spares Quiet populations). The alternative reading (Quiet suffer Fathom-analogous Erosion) was considered and rejected; drafts must not quietly reintroduce it.
4. **SITE-009's funding (06/23).** The Compact-co-funding arrangement is a sovereignty fiction the KNF maintains. It is a feature (it deepens the sovereignty-hawk vs. realist conflict), but any draft that has the Compact *openly* run the site contradicts GOV-014.
5. **Three-faction convergence on Arthur (Sim G).** The simulation judged his survival "narrow but real" — against three factions at once, their competition is his cover. Against a *single* competent faction with a sealed warrant, the bible is honest that he would likely be taken. Do not write him escaping a focused, competent capture on cleverness alone without earning it.

## LOW — accepted
The 21 LOW findings were patched (one-line or one-paragraph fixes). No LOW was judged worth elevating. The two unclaimed independent-group slots (IND-008/009) are intentional headroom, not gaps.

## INTENTIONAL MYSTERIES (do not "resolve" these in drafts without a canon-lock change)
- **L5-1:** What drives the High Tide (the Tide's driver is UNKNOWN).
- **L5-2:** What the thing behind the Laggard is / whether it is intelligent. Simulations F and G leaned on this; it must stay unresolved.
- **L5-3:** The Ninth Bell's ninth site.
- **L5-4:** The attention-pressure mechanism Nwosu's suppressed paper touched.
- **L5-5:** The Laggard's ratchet threshold (the torn page).
Each has a resolution condition in [33_MYSTERIES.md](../33_MYSTERIES.md). Per 02.V, relabeling a gap as a mystery is forbidden — these five passed the mystery-integrity audit (genuine unknowns, no contradictions masked).

## Known coverage blind spots
- Audit 3 did not re-read 15_EDUCATION.md or 22_SUPERNATURAL_LOCATIONS.md in depth. The post-assembly validation (links, IDs, orphaned references) covers structural integrity, but a future deep audit of those two files is recommended before they carry plot weight.
- The 50 regional conflict generators (RC-001..050) and 52 general generators (CG-001..052) were individually verified for presence and ID integrity, and their faction interlocks were mapped in 34 §34.6 — but they were not each red-teamed as scenarios. The ten A–J simulations plus the 124 attacks are the scenario coverage.

## Structural bets the bible makes (for the novelist's awareness)
1. **"Outpaced, not exposed"** is the endgame the bible commits to (26.4 minority report). The masquerade fails by arithmetic, not by revelation.
2. **Information, not power, is the scarce resource** (02.II). Every economy-breaking scheme the auditors designed died on this principle.
3. **Competence is distributed** (02.IV). No faction — and no protagonist — gets to be the only competent actor in a scene.
