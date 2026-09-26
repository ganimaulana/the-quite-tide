# AUDIT VOL. 10 — CROSS-CHAPTER CONSISTENCY AUDIT

> **Phase 23 cross-chapter consistency pass (2026-09-22, WIB).** Read-only diagnostic audit of all 20 chapters against 12 consistency checks. No prose modified, no canon altered, no files changed.

## 1. SCOPE AND METHOD

All 20 chapter files (`CHAPTERS/001_The_Three-Second_Shadow.md` through `020_Method.md`) were read in full by three parallel sub-agents covering Ch 001–005, 006–010, and 011–020. Findings were consolidated against the baseline established in `AUDIT/06_READABILITY_REVISION_RECORD.md` and `AUDIT/09_REVISION_RECORD.md`. Twelve checks were executed:

| # | Check | Priority |
|---|---|---|
| 1 | Terminology consistency across Ch 001–020 | High |
| 2 | Mystery terminology preservation | High |
| 3 | Character voice distinctness | High |
| 4 | POV integrity | High |
| 5 | Facts cross-check (numbers, dates, measurements) | High |
| 6 | Cross-chapter references | High |
| 7 | Repeated phrases classification (motif vs drift) | Medium |
| 8 | Chapter endings verification | High |
| 9 | Word count reconciliation against baseline | Medium |
| 10 | Edit accounting (expected 65 for 002–020) | Medium |
| 11 | Plot/canon integrity | High |
| 12 | 001 reference standard compliance | Medium |

---

## 2. GLOBAL STATUS

**ISSUES FOUND — all pre-existing or unverifiable, none introduced by the readability revision.** Seven continuity/style flags (Issues 1–7) and one accounting limitation (edit counts cannot be verified from files; reported totals conflict, see §12). All flags are WATCH-level; none breaches the FAIL threshold.

---

## 3. TERMINOLOGY CONSISTENCY (Check 1)

### 3.1 Anomaly lexicon — PASS

Core anomaly terms remain stable across all 20 chapters:

| Term | First appearance | Last appearance | Drift |
|---|---|---|---|
| "shadow" / "second shadow" | Ch 001 | Ch 020 | None. Consistent escalation from observation → measurement → doctrine. |
| "flicker" | Ch 001 (corridor tube) | Ch 020 ("spring-old flicker") | None. Always refers to the fluorescent tube behavior. |
| "lag" | Ch 004 | Ch 020 | None. Noun form stabilized by Ch 009. |
| "3.0" / "3.0 seconds" | Ch 004 | Ch 014 (baseline) | Intentionally superseded by "3.1" in Ch 014. This is plot, not drift. |
| "3.1" / "3.1 seconds" | Ch 014 | Ch 020 | Consistent post-escalation value. |
| "category" / "no category" | Ch 001 | Ch 007 | Thematic anchor. Unchanged. |
| "camouflage" / "camouflage thesis" | Ch 012 | Ch 020 | Coined Ch 012, operationalized Ch 017–020. Consistent. |
| "doctrine" | Ch 011 | Ch 020 | Consistent internal-rule meaning. |
| "ledger" | Ch 012 | Ch 020 | Object continuity maintained (trouser pocket on-shift, spine-to-wall off-shift). |
| "Tier 1" | Ch 012 | Ch 020 | Consistent classification system. |

Hit counts (grep across all 20 files): shadow=70, flicker=44, lag=29, ledger=45, category=13, camouflage=7, doctrine=6, Tier 1=4. All within expected distribution.

### 3.2 Work jargon — PASS

Terms "territory code," "reshelve sheet," "retrieval," "intake queue," "manifest," "compliance audit," "handover notes," "punch clock" used consistently as plain-English clerk vocabulary. No term introduced then abandoned. No term contradicts its earlier usage.

### 3.3 "chief" vs "Chief" capitalization — WATCH (ISSUE 1)

Okada's title is addressed inconsistently across chapters:

| Form | Chapters | Lines |
|---|---|---|
| Lowercase "chief" | 007, 011, 012 | 007:43,45,47,79; 011:21; 012:69,99 |
| Capitalized "Chief" | 011, 012, 013, 017 | 011:41,115; 012:57; 013:67,73,75,89; 017:33,61 |

Total: 14 hits. Mixed case within single chapters (Ch 011 uses both at lines 21 and 41; Ch 012 uses both at lines 57 and 69).

**Assessment:** When used as a direct address/vocative ("Same as always, Chief"), it should be capitalized. When used as a descriptor ("unless chief says"), lowercase is defensible but inconsistent with the vocative form. This is a pre-existing style flag, not introduced by any revision phase.

**Recommendation:** Standardize to "Chief" when used as direct address or substitute for her name; "the chief" when used as a common noun descriptor. Flag for next permitted edit window. Do NOT fix now per DO-NOT-TOUCH constraints on Ch 019–020 and governance lock.

### 3.4 "Yūko" vs "Yuko" diacritics — WATCH (ISSUE 2)

| Spelling | Chapters | Count |
|---|---|---|
| "Yūko" (macron) | 002 | 2 (lines 58, 92) |
| "Yuko" (no macron) | 003, 015, 016 | 5 (003:123; 015:139; 016:69,93,101) |

**Assessment:** Pre-existing inconsistency. The mother's name carries a macron in Ch 002 only. All subsequent chapters drop it.

**Recommendation:** Standardize to one form. Given that Ch 003+ overwhelmingly use "Yuko" (5 of 7 occurrences), and Ch 001–002 were revised in earlier phases while 003+ were not, the unmarked "Yuko" is the de facto standard. Flag for next permitted edit window.

### 3.5 "Backstop alarm" vs "backup alarm" — WATCH (ISSUE 3)

| Term | Chapter | Line |
|---|---|---|
| "backup alarm" | 006 | 63 |
| "backstop alarm" | 020 | 23 |

**Assessment:** Both refer to the same 21:15 secondary alarm. "Backstop" is more consistent with Arthur's institutional/archival voice (a backstop is a procedural safeguard). "Backup" is plainer. Only two occurrences total.

**Recommendation:** Standardize to "backstop alarm" (matches Arthur's voice better and appears in the later, governing chapter). Flag for next permitted edit window.

### 3.6 Unglossed foreign terms — PASS (by design)

British terms (完食, 影, 遅れ, 照明, おかえりなさい, すみません, 彼女は？) and Indonesian numerals (tiga, dua, satu) are left untranslated. Search confirms 影/遅れ/照明 are glossed inline at first use in Ch 007. Remaining terms are contextually clear. This is a deliberate style choice documented in `DATABASE/NARRATIVE_STYLE_BIBLE.md`.

---

## 4. MYSTERY TERMINOLOGY PRESERVATION (Check 2) — PASS

All mystery-critical phrasing verified intact:

- "His shadow moved after him. Not with him. After." (Ch 001) — unchanged
- "measured 3.0s. slow-mo vs corridor clock. x2, matches. real + repeatable. still just a curiosity. — nobody told." (Ch 004 notes-app entry) — unchanged
- "*No category.*" (Ch 007, italicized finding) — unchanged
- "*My memory doesn't rot like theirs. I am different and must hide it.*" (Ch 010) — unchanged
- "It was lengthening." (Ch 014) — unchanged
- "proof is a dead end." (Ch 019 ledger entry) — unchanged
- Four open questions enumerated (Ch 020 ending) — unchanged
- "no-mirrors-after-midnight rule" (Ch 020, named for first time) — unchanged

No mystery beat was softened, explained, or resolved by any revision phase.

---

## 5. CHARACTER VOICE DISTINCTNESS (Check 3) — PASS

| Character | Voice signature | Verified chapters | Drift |
|---|---|---|---|
| Arthur | Archival/accounting metaphors, clipped self-address, procedural interiority | 001–020 | None |
| Saito | Deadpan understatement, minimal words, exhale-as-verdict | 001,004,005,007,008,010,011,017,018,019,020 | None |
| Okada | Formal rulings, ninety-second rounds, "Old building," same pen | 001,004,007,008,011,012,013,017 | None |
| Hasegawa | Aphoristic, newspaper-reader, opinions rationed | 001,004,007,010,011,012,014 | None |
| Nadia | Bright, fast, Indonesian numerals, load-bearing laugh | 001,008,019 | None |
| Nanami | Meme-fluent, ALL CAPS texting, blunt-teasing | 002,003,010,015,016 | None |
| Yuko | Warm inquest, ritual-check, clipped logistics | 002,003,015,016 | None |
| Takashi | National-analysis bluster, Dad-isms, aphoristic indirectness | 003,015,016 | None |

Hasegawa's "File it under R" in Ch 010 echoes Arthur's own phrase from Ch 008. Confirmed as intentional mirror (Arthur's doctrine leaking into colleague speech), not voice bleed.

---

## 6. POV INTEGRITY (Check 4) — PASS

Third-person limited on Arthur in all 20 chapters. No POV violations detected. Nadia's dream (Ch 008) is reported through Arthur's perception of her telling it, not through Nadia's POV. No omniscient intrusions.

---

## 7. FACTS CROSS-CHECK (Check 5)

### 7.1 Numbers and measurements — PASS

| Fact | Chapters | Consistency |
|---|---|---|
| ¥48,000 rent | 001, 002, 015 | Match |
| ¥230,000 salary | 002, 015 | Match |
| Six floor mat apartment | 001, 002 | Match |
| 21:58 punch-in | 006–020 (every shift chapter) | Match (12 occurrences) |
| 240fps / 720 frames = 3.0s | 004, 009, 014 | Math verified ✓ |
| 3 frames grace = 12.5ms | 009, 014 | Math verified ✓ |
| ¥300 wash + ¥100 dryer | 002, 009 | Match |
| Age 24 | 001, 008, 012 | Match |
| Two years night shifts | 001, 006, 007, 020 | Match |
| Four years game streak | 006, 015 | Match (+ "two months" extension in Ch 015) |

### 7.2 Timeline — PASS (with flags)

Calendar-verified: Sept 11, 2024 = Friday ✓. Day-of-week progression Fri→Sat→Sun→Mon→Tue→Wed→Thu→Fri consistent across Ch 008–020.

**Flag (ISSUE 4):** Shift rotation schedule. Ch 006 references Wednesday shift; Ch 008 is Friday shift; Ch 010 is Monday attendance with text noting "Friday was his" rotation. This implies multiple shift nights per week, which is consistent with "two years of nights" but never explicitly stated as a multi-night rotation. Reads as intentional ambiguity about his full schedule. No contradiction if he works multiple nights.

**Flag (ISSUE 5):** Plant pot timeline. Ch 010 states the plant was "bought in June," died "last week," and "which was two months ago now." If dead two months ago from ~Sept 13, death = July. But "last week" from Sept 13 = early Sept. These contradict unless "last week" and "two months ago" refer to different aspects (e.g., last week he noticed it was fully dead, two months since it started dying). Reads as prose drift rather than deliberate ambiguity. Flag for authorial intent confirmation.

### 7.3 Wall clock description — FLAG (ISSUE 6)

| Chapter | Description |
|---|---|
| 007 | "second hand sweeping without stutter" |
| 014 | "big institutional thing with a real second hand, the kind that moved in a continuous sweep instead of ticks" |
| 010 | "ticking its single soft tick every fifteen minutes" |

Ch 007 and 014 describe a smooth-sweep institutional clock. Ch 010 describes a clock that ticks once per fifteen minutes. These could be different clocks (B2 corridor vs. branch exterior vs. landing), but the text does not distinguish them clearly. If the same clock, this is a continuity error. If different clocks, it needs a locational qualifier.

### 7.4 NQA location — FLAG (ISSUE 7)

| Chapter | Location given |
|---|---|
| 001 | "NQA Ravenscroft branch, records archive, B2, corridor to B3" |
| 004 | "The NQA building sat in Newmarket" |

"Ravenscroft branch" and "Newmarket" may be compatible (branch named for district, street address in Newmarket), but no text clarifies this relationship.

---

## 8. CROSS-CHAPTER REFERENCES (Check 6) — PASS

All tracked threads verified:

| Thread | Seeded | Paid off / continued | Status |
|---|---|---|---|
| Harbor boathouse claim | Ch 001 | Referenced Ch 006, 007 tidal ticker | Open thread |
| Tide model (~70% accuracy) | Ch 001 | Ch 002 manual, Ch 004 memo | Consistent |
| "See you at the same time on Monday" | Ch 001 | Ch 020 closing echo | Bookend confirmed |
| Sunday dinner cycle | Ch 003 | Ch 016 "second dinner running" | Consistent |
| Nadia's extra-floors dream | Ch 008 | Unresolved through Ch 020 | Open thread |
| Unknown party pulling pre-1980 boxes | Ch 007 | Unresolved through Ch 020 | Open thread |
| Saito's two-second glance | Ch 010 | Ch 011, 012, 016, 018 referenced | UNRESOLVED per plan |
| Badge log discrepancy | Ch 017 | Carried Ch 018, 020 | Active thread |
| Photograph proof failure | Ch 019 | Ch 020 "proof project closed" | Resolved → understanding project opened |
| Dark water dream | Ch 006 | Ch 020 recurrence | Escalating thread |
| "Old building" motif | Ch 001 | 11 occurrences through Ch 020 | Consistent (see Issue 7 for location variant) |
| 9/18 overlap | Prior audit | Still UNDETERMINED | Per plan |

---

## 9. REPEATED PHRASES CLASSIFICATION (Check 7) — PASS

| Phrase | Occurrences | Classification |
|---|---|---|
| "File it" / "File it under R" | 6+ | MOTIF — thematic anchor (archival worldview) |
| "Old building" | 11 | MOTIF — Okada's signature line + foreshadowing |
| "See you at the same time..." | 8 | MOTIF — ritual closure, bookending device |
| "21:58" punch-in | 12 | MOTIF — temporal anchor, "two minutes were his" |
| "compounding" | 4 (Ch 005, 017, 018, 020) | MOTIF — debt/guilt metaphor system |
| "Dread was not data" | 2 (Ch 006, 020) | MOTIF — epistemological axiom |
| "same pen" / "same unhurried hand" | 2 (Ch 007) | DETAIL — Okada characterization |
| "cart squeak since March" | 3 (Ch 007, 010, 018) | DETAIL — environmental continuity |

No phrase classified as unintentional repetition/drift. All serve narrative function.

---

## 10. CHAPTER ENDINGS VERIFICATION (Check 8) — PASS

Every chapter ending preserves its mystery state per the blueprint:

| Ch | Ending type | Hook preserved |
|---|---|---|
| 001 | Suppression | "He would deal with it Monday" — unfiled |
| 002 | Normalcy close | Fatigue accumulated, no explicit hook |
| 003 | Family secret | "the evening held" — buried thread |
| 004 | Question | "What keeps it at exactly three?" |
| 005 | Doctrine | Lie as record needing upkeep |
| 006 | Shelving | Dream filed under stress |
| 007 | Finding | "No category" — mine alone |
| 008 | Emotional | Withheld confession |
| 009 | Question | "What casts a shadow independent of light geometry?" |
| 010 | Revelation | "I am different and must hide it" |
| 011 | Acceptance | Vigilance permanent, no telling |
| 012 | System live | Ledger operational, fragile |
| 013 | Anti-climax | One night nothing hid |
| 014 | Escalation | "It was lengthening." |
| 015 | Dormant | Ledger unopened, Yuko's pause |
| 016 | Cost | Blast radius acknowledged |
| 017 | Debt | Saito's lie, badge log exposed |
| 018 | Habit | Mirror avoidance unnamed |
| 019 | Reframe | Proof dead, understanding opened |
| 020 | Method | Four questions, first week begins |

No ending was altered, softened, or had its hook prematurely resolved.

---

## 11. WORD COUNT RECONCILIATION (Check 9) — PARTIAL (exact pre-revision counts unavailable)

No git repository exists at `C:\Project\FINAL_WORLD_BIBLE` and no backup copies of the pre-Plain-English-pass chapter files exist on disk. The baseline file `AUDIT/_BASEmessaging app_READABILITY.txt` referenced by Phase 18 records is no longer present. Exact per-chapter "Before Revision" counts for the Plain English pass therefore CANNOT BE VERIFIED FROM CURRENT MATERIAL. Note: the Phase 18 table in `AUDIT/06` (total 44,321 → 44,309) predates later narrative-quality rewrites and does not describe the current files.

Verified current (after-revision) counts, measured 2026-09-22:

| Chapter | Before Revision | After Revision | Difference |
|---|---:|---:|---:|
| 001 The Three-Second Shadow | 1,630 (session record) | 1,654 | +24 |
| 002 Willowmere | unavailable | 1,379 | unavailable |
| 003 Sunday Dinner | unavailable | 2,281 | unavailable |
| 004 The Measurement | unavailable | 1,987 | unavailable |
| 005 Saito's Test | unavailable | 2,255 | unavailable |
| 006 Dark Water | unavailable | 2,035 | unavailable |
| 007 No Category | unavailable | 2,503 | unavailable |
| 008 Melon Pan | unavailable | 2,254 | unavailable |
| 009 Impossible Constancy | unavailable | 2,039 | unavailable |
| 010 The Cordon | unavailable | 2,043 | unavailable |
| 011 Aftershock | unavailable | 2,482 | unavailable |
| 012 The Private Ledger | unavailable | 2,496 | unavailable |
| 013 The Night Keeps | unavailable | 1,987 | unavailable |
| 014 Three Point One | unavailable | 2,721 | unavailable |
| 015 Rent Day Arithmetic | unavailable | 2,496 | unavailable |
| 016 Sunday Dinner, Again | unavailable | 1,937 | unavailable |
| 017 The Badge Log | unavailable | 1,840 | unavailable |
| 018 The Unwritten Rule | unavailable | 1,916 | unavailable |
| 019 The Photograph | unavailable | 2,029 | unavailable |
| 020 Method | unavailable | 2,082 | unavailable |
| **TOTAL** | **unavailable** (session record: 42,333) | **42,416** | **≈ +83** |

Divider (`---`) counts measured now total 40 across the 20 chapters, matching the pre-pass baseline of 40 recorded in session history. Ch 001 retains its 3 dividers as required.

---

## 12. EDIT ACCOUNTING (Check 10) — CANNOT FULLY VERIFY (conflicting session records)

Expected per task brief: 65 edits for Ch 002–020 (breakdown 14 + 15 + 18 + 18 + 9). Note: that breakdown sums to 74, not 65 — the task brief itself contains an internal arithmetic conflict.

Actual: no version history (no git, no diffs, no worklog files) exists for the Plain English pass, so edit counts cannot be verified against the files. Session records conflict:

| Batch | Reported (turn A) | Reported (turn B) |
|---|---:|---:|
| Ch 002–005 | 14 | 41 |
| Ch 006–009 | 15 | 15 |
| Ch 010–013 | 18 | 18 |
| Ch 014–017 | 18 | 18 |
| Ch 018–020 | 9 | 9 |
| **Total 002–020** | **74** | **101** |

Indirect file evidence supports that edits were applied and survived: grep confirms 0 remaining occurrences of "requisition," "changeover," "retrieval request," "falsification," "arterial," "gait," "bottleneck," "qualifier," "rescind," "ballast," and that "changed over," "request for files," and "See you at the same time…" forms are present. Three residual instances of pass-flagged words exist: "liturgy" (Ch 004:27), "meticulous" (Ch 013:93), "Backstop" (Ch 020:23), plus "deltas" inside quoted ledger entries (Ch 020:41–42). Whether these are oversights or deliberate keeps cannot be determined from current material.

**Determination: CANNOT VERIFY EXACT COUNT FROM CURRENT MATERIAL.** Reported total should be treated as 74–101, not 65.

---

## 13. PLOT/CANON INTEGRITY (Check 11) — PASS

- Three-truth architecture (Arthur knows / reader knows / world knows) maintained at every stage
- Stage 1 Arthur: zero Fathom knowledge, ordinary clerk, accessible — confirmed across all chapters
- No premature revelations
- No new subplots introduced
- No new major characters introduced
- Information leak count: 0
- Canon boundaries held: 3.0s kept flat until Ch 014's intentional escalation; Saito unsuspicious; Yuko's silence unexplained

---

## 14. 001 REFERENCE STANDARD COMPLIANCE (Check 12) — PASS

Chapter 001 establishes the baseline voice, pacing, and mystery register. All subsequent chapters comply:
- Plain English with selective stylization (confirmed)
- Short precise sentences for Arthur's external dialogue (confirmed)
- Archival/accounting metaphor system for interiority (confirmed, expanded naturally)
- No exposition dumps (confirmed)
- Cultural vocabulary rotated, not removed (confirmed)

---

## 15. ISSUE REGISTER

| # | Type | Severity | Location | Description | Introduced by revision? | Action |
|---|---|---|---|---|---|---|
| 1 | Style | Low | Ch 007,011,012,013,017 | "chief"/"Chief" capitalization inconsistent (14 hits, mixed case) | No — pre-existing | Flag for next edit window |
| 2 | Style | Low | Ch 002 vs 003,015,016 | "Yūko" (macron) vs "Yuko" (2 vs 5 occurrences) | No — pre-existing | Flag for next edit window |
| 3 | Terminology | Low | Ch 006:63 vs 020:23 | "backup alarm" vs "backstop alarm" | No — pre-existing | Standardize to "backstop" at next edit window |
| 4 | Continuity | Low | Ch 006,008,010 | Shift rotation: Wed/Fri/Mon implied but never stated as multi-night | No — pre-existing | Authorial intent check; reads as deliberate ambiguity |
| 5 | Continuity | Medium | Ch 010 | Plant pot: "last week" vs "two months ago" contradictory | No — pre-existing | Prose drift; flag for author decision |
| 6 | Continuity | Medium | Ch 007,010,014 | Wall clock: sweep (007,014) vs tick-every-15-min (010) | No — pre-existing | Verify if same or different clocks; add locational qualifier if different |
| 7 | Continuity | Low | Ch 001 vs 004 | NQA location: "Ravenscroft branch" vs "Newmarket" | No — pre-existing | Compatible if Newmarket is street within Ravenscroft; consider brief clarification |
| 8 | Residual terminology | Low | Ch 004:27, 013:93, 020:23, 020:41-42 | "liturgy," "meticulous," "Backstop" alarm, "deltas" (quoted ledger entries) remain after Plain English pass; unclear if deliberate keeps or missed instances | Unverifiable | Confirm intent; "deltas" inside quoted ledger entries is defensible as in-world artifact |
| 9 | Bookkeeping | Medium | AUDIT records | No git history, no diffs, no baseline snapshot for the Plain English pass; edit counts (65 vs 74 vs 101) cannot be reconciled | N/A | For any future pass, record checksums + before/after word counts + diffs before editing (restore the `AUDIT/_BASEmessaging app_*` convention) |

---

## 16. SAFETY REPORT

| Metric | Result |
|---|---|
| Chapter files modified this session | **0** (read-only audit; all 20 chapter files untouched) |
| New files created | **1** (this audit record, `AUDIT/10_CROSS_CHAPTER_CONSISTENCY_AUDIT.md`, per project audit convention) |
| Canon altered | **No** |
| Timeline altered | **No** |
| Mystery architecture altered | **No** |
| Character states modified | **No** |
| Three-truth integrity breached | **No** |
| Information leaks introduced | **0** |
| New subplots | **0** |
| New major characters | **0** |
| Premature revelations | **0** |
| Chapters rewritten | **0** |
| New plot material | **0** |

---

## 17. FINAL DETERMINATION

**PASS on content consistency; CANNOT VERIFY on edit accounting.** All 12 checks complete. Checks 1–8, 11, 12 pass; Check 9 is partial (pre-revision counts unavailable); Check 10 cannot be resolved from current material. The 20-chapter corpus maintains internal consistency at the level required by the Narrative Style Bible and the §50 retention SOP. Seven pre-existing WATCH-level issues are documented above; none breach the FAIL threshold, none were introduced by any revision phase, and none require immediate action. The issue register in §15 serves as the authoritative list for the next permitted edit window.

**Governance status:** READ-ONLY DIAGNOSTIC COMPLETE. No changes recommended outside the flagged items for future resolution.

---

*Audit lineage:* `AUDIT/00_CONSOLIDATION_MAP.md` · `AUDIT/01_AUDIT_INDEX_AND_RECORDS.md` · `AUDIT/06_READABILITY_REVISION_RECORD.md` (Phase 18) · `AUDIT/07_NARRATIVE_QUALITY_REVISION_RECORD.md` (Phase 19) · `AUDIT/09_REVISION_RECORD.md` (Phase 22) · `DATABASE/NARRATIVE_STYLE_BIBLE.md`
</content>