# DATABASE VOL. 03 â€” Continuity & Knowledge Trackers â€” THE QUIET TIDE

> **Phase 20 repository consolidation (2026-09-21, v3.0).** This numbered volume merges 9 source files **verbatim** into one file. No content was changed, rewritten, or summarized â€” only this header, the source register below, and per-section attribution separators were added. To find a document's new location, see `AUDIT/00_CONSOLIDATION_MAP.md`.

## Source register

| # | Original file | Words | sha256 (pre-merge) |
|---|---|---|---|
| 1 | `DATABASE/CHARACTER_STATE_TRACKER.md` | 7,146 | `ef715ab6b2c7e2f0â€¦` |
| 2 | `DATABASE/ARTHUR_PROGRESS_TRACKER.md` | 3,777 | `0c2a970fe8a006bdâ€¦` |
| 3 | `DATABASE/CHAPTER_FORESHADOWING_TRACKER.md` | 3,388 | `52e9ebeb4b7adc1câ€¦` |
| 4 | `DATABASE/CHAPTER_HOOK_SYSTEM.md` | 3,566 | `fcff972ff34208ddâ€¦` |
| 5 | `DATABASE/CHAPTER_MYSTERY_TRACKER.md` | 3,911 | `635860e403b69c6fâ€¦` |
| 6 | `DATABASE/INFORMATION_FLOW.md` | 2,485 | `ed19e85feccf3f03â€¦` |
| 7 | `DATABASE/INFORMATION_KNOWLEDGE_MAP.md` | 2,570 | `8ef02d6962e48495â€¦` |
| 8 | `DATABASE/ROMANCE_ARCHITECTURE.md` | 5,698 | `2f60c6053b2540a0â€¦` |
| 9 | `DATABASE/POWER_PROGRESSION.md` | 7,224 | `950826063cab061eâ€¦` |

---


---

## SECTION: `DATABASE/CHARACTER_STATE_TRACKER.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `DATABASE/CHARACTER_STATE_TRACKER.md` Â· sha256 `ef715ab6b2c7e2f0a0c4974d216ec89963d778e5dde3f3d1a1135add431aa25e` Â· 7,146 words. No content changed.

# DATABASE â€” Character State Tracker (THE QUIET TIDE)

> Phase 9 â€” Chapter Engine Architecture: Tracking Systems. Operational machinery only â€” no chapters, scenes, prose, dialogue, or chapter titles.
> Sources of truth: `DATABASE/CHARACTERS.md` (CHAR-001â€“037) Â· `DATABASE/POWER_PROGRESSION.md` (7 stages, ratchet, 16-item no-shortcut list, 8 power-jump brakes) Â· `DATABASE/FACTIONS_AND_CONFLICTS.md` (81+ org IDs, 102 ACTIVE conflicts, 28/28 autonomy verdict) Â· `DATABASE/ROMANCE_ARCHITECTURE.md` (configs Aâ€“E, 6 rules, dinner rule, 7 independence watches) Â· `DATABASE/STORY_ENGINE.md` (Â§3 internal arc; Â§4 ordinary-life engine) Â· `DATABASE/ARC_ARCHITECTURE.md` Â· `DATABASE/LONG_SERIAL_STRUCTURE.md`.
> This file defines the schema the Chapter Engine must maintain per major character, the series-start ledger, and the audit rules that prevent continuity drift across ~1,000 chapters.

---

## Â§1. Purpose

The Character State Tracker is the continuity ledger for every character the reader meets more than once. Its job is to make **forgetting impossible by procedure rather than by memory**: after every chapter batch, the planner updates the schema, and the batch audit (Â§10, Â§12â€“Â§14) detects drift the drafter cannot be trusted to notice. It is the machine answer to the long-serial question *"but why didn't she remember the wound from chapter 41?"*

---

## Â§2. State schema â€” the eleven fields

Every tracked character carries these eleven fields at all times. A field may be `UNKNOWN (recorded)` â€” never silently empty.

| # | Field | Definition |
|---|---|---|
| 1 | **Current location** | Where the character physically is (city, district, building) at the ledger's current chapter. Includes custody/displacement status (detained, traveling, off-grid). |
| 2 | **Current objective** | What the character is actively trying to accomplish â€” one primary, up to two secondary. Objective changes are ledgered with the event that changed them. |
| 3 | **Current emotional state** | The character's working emotional register (grief, wariness, exhaustion, devotion, suspicion), stated in observable terms. May not contradict the previous entry without an intervening cause. |
| 4 | **Current knowledge** | What this character *knows* â€” facts, secrets learned, methods discovered. Cross-linked to `DATABASE/INFORMATION_KNOWLEDGE_MAP.md`: knowledge is the ledger's most drift-prone field, and the audit's first target. |
| 5 | **Current relationships** | Trust and hostility states toward every other character the character has meaningfully interacted with, with the last event that moved each one. Relationships change only through events, never off-page (see Â§10, Rule 4 and Â§14, NO-RESET). |
| 6 | **Current faction status** | Standing, rank, and trust level with each faction the character touches (employer, handler, informant, target). Faction-side bookkeeping per Â§13. |
| 7 | **Current injuries** | Physical and Erosion-state damage, with recovery stage. Injuries heal at canon rates (see Â§10, Rule 2) â€” never faster, and the healer's paradox applies (POWER_PROGRESSION Â§F: aggressive Bone healing transfers Erosion-risk to the healer). |
| 8 | **Current resources** | Money, equipment, favors owed, institutional access, safe houses. For Arthur see the dedicated tracker (`DATABASE/ARTHUR_PROGRESS_TRACKER.md`); this field covers everyone else. |
| 9 | **Current secrets** | What the character hides, from whom. Each secret carries: the holder, the excluded party, the exposure vector, the cost of exposure. See Â§14 for romantic secrets. |
| 10 | **Current beliefs** | What the character *believes is true* about the world and themselves â€” including wrong beliefs. Beliefs are canon facts for behavior purposes; a character acts on a wrong belief until an event changes it. |
| 11 | **Current misunderstandings** | Each character's specific misreads of *other characters' motives* (the misunderstandings are load-bearing per POWER_PROGRESSION Â§L). Misunderstandings resolve only through evidence, never by assertion. |

---

## Â§3. Update rules per chapter batch

1. **Every tracked character whose situation changed in the batch gets all affected fields re-written.** Touching one field requires re-reading all eleven for contradictions.
2. **No field may be deleted.** Old states are archived with chapter ranges (e.g., `injuries: sprained wrist â€” healed ch. 212â€“240`). History is a scroll, not a snapshot.
3. **Any field change must cite the chapter where the change occurred.** A change without a chapter citation is rejected by the audit.
4. **Fields 4 (knowledge) and 5 (relationships) are checked against the three-state separation doctrine** (`DATABASE/ARTHUR_PROGRESS_TRACKER.md` Â§11): a character's knowledge may not contain facts their ledger cannot justify them having witnessed or been told.
5. **Field 10 (beliefs) may contradict field 4 (knowledge) of another character, but never contradict its own character's field 4** â€” a character cannot hold a belief they have learned is false without a recorded rationalization (denial, compartmentalization â€” ledgered as such).
6. **Field 11 (misunderstandings) must be re-checked whenever field 5 (relationships) moves.** Misunderstandings resolving without new evidence is a Rule-5 violation (Â§10).

---

## Â§4. What "major/recurring" means

A character is **major** if canon gives them independent objectives (faction heads, romance candidates, family, Night Clerks principals). A character is **recurring** if they appear across arcs even without objectives (Okada, Hasegawa). **Minor one-scene characters** (the HR screener, the dredger foreman, a one-night clerk) are **grouped as "track on appearance"** â€” a single floating ledger entry created at first appearance with fields 1, 2, 4, 5 only, and archived when they exit. The ledger below covers all major/recurring living characters.

---

## Â§5. The initial ledger â€” series start

Values are grounded in `DATABASE/CHARACTERS.md` and `DATABASE/ROMANCE_ARCHITECTURE.md`. No invented backstory. Series start = the week before ARC I's opening (ch. ~1), UNLESS the canon start-state explicitly places a character later (arrival dates are noted).

| ID | Name | Location | Objective | Emotional state | Knowledge | Relationships | Faction status | Injuries | Resources | Secrets | Beliefs | Misunderstandings |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CHAR-001 | Arthur Reed | 1K apartment, Willowmere, Ravenhurst; nights at NQA Ravenhurst records archive (B2â€“B3) | Stay uninteresting; keep the archive job; measure the shadow without filing it | Wary, meticulous, dryly stable â€” masking fatigue present but managed | Shadow lags ~3s (unmeasured as rule); 2017 transfer memory (unexamined); the 2021 examination's sealed record exists (he does not know its content) | Mother/father/sister (dutiful, withheld); SaitÅ (closest friend, shared noticing); Night Clerks cell (loyalty by presence); Okada/Hasegawa (professional respect) | NQA employee (flagged hire, unknowing); Loud, unregistered (legal â€” the Census registers the Attuned, not Loudness); SMD thin file subject (unknowing); holds ANOMALY-001 (unknowing of the mechanism) | None (pre-series) | ~Â£230,000/month salary; rent Â£48,000; records-room access; Night Clerks' Discord; SaitÅ's shared memory | The mirror (SECRET-005 â€” told no one); the no-mirrors-after-midnight rule (unwritten) | Understanding a thing = surviving it (archivist's deformation); safety = absence; the shadow is a personal curse, not an anomaly | Misreads institutional silence as indifference (the silence is camouflage/doctrine); believes his memory is "good memory," not Loudness |
| CHAR-002 | Elena Voss | BTA headquarters (US) | Continental containment on a budget; Drowndust counter-proliferation | Institutional, steady | No Arthur knowledge (UNAWARE stance) | Professional vs other agency heads | BTA Director (GOV-001); Meridian Compact T1 member | None known | Full BTA apparatus | Classified | The franchise model can hold the High Tide | Structural â€” no personal misreads recorded |
| CHAR-003 | Zhao Mingde | Jade Office (China) | Total legibility â€” every Attuned filed, posted, pensioned | Controlled, patient | No Arthur knowledge | Professional vs other agency heads | Head, Jade Office (GOV-002) | None known | State apparatus | Classified | Legibility is achievable | Structural |
| CHAR-004 | Arkady Volkov | Department 12 (Russia) | Strategic depth â€” anomalies as arsenal | Calculating | No Arthur knowledge (doctrinal seizure posture toward unregistered assets generally) | Vs Compact: RIVALS | Head, Dept 12 (GOV-003) | None known | Dept 12 assets | Classified | Assets are seized, not recruited | Structural |
| CHAR-005 | Ratna Kusuma | BPF HQ (Indonesia) | Pragmatic triage on 1/40th the budget | Pragmatic, dry | No Arthur knowledge (his Jakarta file exists, unread) | Vs Compact CLIENT | Head, BPF (GOV-004) | None known | BPF apparatus | Classified | Triage beats aspiration | Structural |
| CHAR-006 | Ri Kang-dae | Simjo-guk (North Korea) | The palace's Awakening lineage | Opaque | No Arthur knowledge | Minimal | Bureau Chief (GOV-012) | None known | Simjo-guk | Classified | UNKNOWN (recorded) | Structural |
| CHAR-007 | Aldo Ferretti | Vatican OEP | The Asylum Protocol; anomaly-adjacent pastoral care | Pastoral, watchful | No Arthur knowledge | Professional | Prefect, OEP (GOV-010) | None known | OEP apparatus | Classified | Pastoral containment holds | Structural |
| CHAR-008 | Fatoumata Diallo | Geneva (Compact) | Maintain the Accords; keep the masquerade's economics solvent | Steady, diplomatic | No Arthur knowledge | Primary convener | SG, Meridian Compact (INTL-001) | None known | Compact machinery | Classified | The Accords hold | Structural |
| CHAR-009 | Adaeze Okonkwo | Geneva (Compact observation) | UNKNOWN (recorded) â€” observed, not commanded | Observed | Cosmological â€” T6 Tide; Worldtide | Compact observation subject | Compact observation subject | None known (Erosion arithmetic applies at her tier) | N/A | UNKNOWN | UNKNOWN | N/A |
| CHAR-010 | TomÃ¡s Aquino Reyes | Manila (Compact observation) | UNKNOWN (recorded) | Observed | Cosmological â€” T6 Choir; Worldtide | Compact observation subject | Compact observation subject | None known | N/A | UNKNOWN | UNKNOWN | N/A |
| CHAR-011 | Hana Shirakawa | Hokkaido (Compact observation) | UNKNOWN (recorded) | Observed | Cosmological â€” T6 Hollow; Worldtide | Compact observation subject | Compact observation subject | None known | N/A | UNKNOWN | UNKNOWN | N/A |
| CHAR-012 | Hannah Reed | Reed family home, Willowmere | Ordinary office life; two-year plan unspecified (canon: UNKNOWN beyond present) | Warm, mildly teasing; unaware | None of the hidden world; Quiet | Brother (affectionate, teasing); mother/father (dutiful) | None | None | Office job salary | None | Normal life is the default | Believes Arthur's odd hours are just the job |
| CHAR-013 | Thomas Reed | Reed family home, Willowmere | Provide; keep the household steady | Steady, understated | None of the hidden world (his silences are management, per ARC V); Quiet | Family (provider's reserve) | None (employer: Ravenhurst Industrial District auto-parts) | None | KachÅ salary | The careful silences (management, not knowledge â€” do not promote to canon) | Normalcy is maintained by steady work | Misreads Arthur's distance as young-adult reserve |
| CHAR-014 | Eleanor Reed | Reed family home, Willowmere | Keep the family's peace; the folk-heuristic keeper (salt by the door, *protective charm*) | Warm, quietly vigilant; asks *Are you seeing anyone?* every other Sunday | Folk heuristics (practical, wrong-theoried); what she manages around 2018 (held â€” ARC V) | Family (the peace is the load-bearing asset) | None | None | Part-time supermarket wages | Her careful silences (UNKNOWN content â€” recorded, not invented) | The peace is protectable | Misreads nothing â€” but says nothing (the distinction is load-bearing) |
| CHAR-015 | Samuel Brooks | Two desks over from Arthur, NQA Ravenhurst nights; 1K nearby | Test what two Loud clerks can get away with; keep the night shift's private history | Curious, dry, loyal; restless inside the routine | Loud (unacknowledged â€” neither has the word); the shadow's *behaviors* observed, not told; does NOT know the mirror (SECRET-005's tripwire is sharpest here) | Arthur (closest friend; the only fully-shared memory); Night Clerks cell | None (adjacent to every leak; ambient, not sourced) | None | Night-clerk wages; the shared unedited memory | The extent of his testing (UNKNOWN to Arthur); what he has observed about the shadow | Knowledge is for using; two Louds staying quiet is safe (false â€” the demographers' flag, MYSTERY-010) | Misreads Arthur's weather-stance as caution rather than doctrine |
| CHAR-016 | Nadia Rahma | NQA Ravenhurst, day shift (overlaps Arthur's nights by 2 hours) | Complete the five-year plan; renew/upgrade SSW status | Kind, funny, homesick; professionally unflappable | None of the hidden world; Quiet; the "weird dreams" (unexplained to her); her filings' authorship UNKNOWN to her | Arthur (dawn-convenience store acquaintance; one-sided); claims-desk colleagues | NQA employee; her claims tier is on the SMD's SSW-adjacency watchlist (structural â€” she does not know) | None | Adjuster salary; the routine manual + revision history (access) | None deliberate â€” she is Quiet; forgetting is not hiding. The *world* hides from her: the pipeline's editing behavior, analytics flags, the second leak (MYSTERY-055) | Plans are how you stay a person; her adjustments are neutral routine (false â€” MYSTERY-012) | Believes ordinary paperwork is safe; will later learn her hands softened filings (MYSTERY-012) |
| CHAR-017 | Larasati "Laras" Prameswari | BPF field (Indonesia; Ravenhurst-adjacent per canon) | Hunt the mole; decide tell-KNF vs run-double (RC-032) | Sharp, professional; under pressure | Mole-hunt facts (partial); Arthur's visitor logs (he is the investigation's favorite witness â€” she does not yet treat him as more) | BPF command chain; professional | BPF field investigator (GOV-004) | None known | BPF field resources | The tell-vs-double decision (her ledger, in progress) | The mole is findable | Misreads the BPF-internal mole hunt as separate from CG-044's atmosphere (relocation note: unaffected) |
| CHAR-025 | Vivienne Ashworth | Pale Court circuits | Custodianship; authenticated pieces; dynastic continuity; the Season | Regal, deliberate | No Arthur knowledge at series start; holds the Court's wrong bloodline theory (formulated later per ARC V) | Vs Compact: WARY; vs KNF/GOV: WARY | Pale Court dynast (SUP-009); T4 Choir | None known (Fathom arithmetic applies) | Court collections, capital | The four unregistered T4+ pieces (ARC XIIIâ€“approach exposure) | The Reed line holds a hidden aristocracy (WRONG â€” SECRET-015 irony; canon: no hidden aristocracy) | Misreads ordinariness as concealment |
| CHAR-026 | Hendra "Bos Naga" Gunawan | Naga Hitam operations | Survive the succession dispute; keep the Drowndust cache unspent; buy paper leverage | Tense, operational | No Arthur knowledge (UNAWARE); operational succession facts | Vs BPF: CLIENT (Priok veto); vs CRIM-004: rivals | Operational head, Naga Hitam (CRIM-002) â€” titular head Dewi "Naga" Mahmud remains | None known | Syndicate operations, Drowndust cache | The cache's true state | The succession is winnable | Misreads paper as control (paper on sightings is leverage, not custody) |
| CHAR-027 | "The Factor" | Red Ledger brokerage | Contracts and the pension plan; the Code | Professional, precise; name unrecorded by design | No Arthur knowledge yet (will initiate the black-book inquiry â€” EVENT-093) | Professional vs buyers | Senior broker, Red Ledger (SUP-004) | None known | The market itself | Identity (canon: unrecorded) | The Code protects the market | Misreads nothing about the market; misreads people as prices |
| CHAR-028 | June Park | Lantern Bearers network | Leak the hidden world carefully; build the Akari cell | Principled, careful, urgent | Knows the leak's mechanics (CG-041); Arthur as *demographic*, not yet as source (RECRUITING stance) | Vs Compact: WARY; vs governments: COLD | Founder, Lantern Bearers (SUP-005); Loud | None | Journalist's network, the cache | The leak's sourcing (her operational security) | The world can be leaked carefully | Misreads Arthur's willingness (his weather-stance is not consent) |
| CHAR-029 | Silas Crane | Hollow Men circuits | The last dive; his warning to deliver | Tired, terminal (82 Fathoms) | Hollow T3; knows the 82-Fathoms arithmetic; holds Crane's warning (MYSTERY-007) | Vs everyone: wary | Diver, Hollow Men (SUP-006) | Terminal Erosion (82 Fathoms â€” irreversible) | The dive's receipts | Whatever he wouldn't say on the record (the warning's second half) | Deep water has a voice | Structural |
| CHAR-030 | Amos Kade | Ninth Bell circuits | The Peal â€” nine simultaneous thinnings; win the Peal-vs-Parish war | Certain, recruiting | Bell doctrine; preaches against the Court's eschaton | Vs Compact: AT-WAR; vs Choir: AT-WAR | Prophet, Ninth Bell (SUP-007/REL-006); Loud | None known | 400,000-adjacent adherent network | The ninth site (UNKNOWN by design) | The Bell's eschaton is imminent | Structural |
| CHAR-031 | Amara Nwosu | Vesper Tide-Medicine Division (recruited 2024; ex-Compact science directorate) | Erosion research; the zero-Erosion longitudinal subject question | Clinical, driven | Nwosu's data (MYSTERY-015: the Tide remembers Drownings); what her suppressed paper showed (UNKNOWN to others) | Vs Compact science: severed (defection) | Director, Vesper Tide-Medicine Division (CORP-002); ex-Meridian Institute (RES-001) | None known | Vesper's funding ("impossible to leave") | The suppressed paper's content | Erosion is researchable | Misreads consent as the end of the ethics question (Vesper's structure is itself the compromise) |
| CHAR-032 | Pramudya "Pram" Nugroho | Cartographers' SE Asia circuit â€” **arrives Ravenhurst September 2024 (EVENT-100)**; series start: *not yet in Ravenhurst* | Continue Ilsa's work; map the tether; serve the Exchange â€” and tell Arthur the truth about the choosing | Charming, precise, conflicted | Ilsa's journals' *content* (knows more about Arthur's condition than Arthur knows himself); does NOT know the mirror; believes the journals are complete (false â€” one page missing); believes continuing Ilsa's work is neutral scholarship (false) | Exchange command; Exchange valuation of the Laggard (the buyer inquiry, EVENT-093) | Cartographers' Exchange field mapper (SUP-002); T2 Hollow | None known (Fathom arithmetic applies at T2) | Field kit; the journals (disputed property); Exchange posting | What he reports; what the Exchange ordered about Arthur; whether the reassignment was his finding or his posting; the second price (MYSTERY-051) | Curiosity's price is the work; disclosure is the canon question (will he *tell* Arthur he's choosing) | Misreads the Exchange's interest as scholarship; misreads the journals as complete |
| CHAR-033 | Kirana "Kira" Maheswari | Ravenhurst (freelance; Quiet-care counseling) | Do the counseling work well; manage her Fathoms honestly; keep the stringer income from becoming experimentation | Precise, dry, exhausted | 31 Fathoms and counting (her precise trajectory is her secret); the triangle's upstream (what she's reported, what she's held back); Tide-mark reading of Arthur's rooms (what she has/hasn't read) | Meridian Institute (RES-001) stringer employer; professional | Meridian Institute stringer; T2 Lantern; 31 Fathoms | 31 Fathoms (irreversible; side effects per tier-depth table) | Counselor's income; stringer stipend | The triangle's upstream; her trajectory; her unreported readings | The clock is a fact, not a tragedy; accurate reading is the kindest thing | Misreads her readings as giving her the truth of *him* (marks, not interior) |
| CHAR-034 | Aisha Rahman | Ravenhurst (SMD contract; KNF liaison seam) | Keep her team alive; manage the seam; decide what to do with the witness she can't Veil-edit | Tired, decisive, dry-humored | The standing case file (him); the unfiled follow-ups (her ledger); the seam's pressures; the Desk's plan (MYSTERY-008 â€” UNKNOWN to her) | SMD contract officers; KNF liaison side; her team | SMD (GOV-006) Sweeper team lead; KNF liaison seam (GOV-014); fraternization rules apply | None known | Sweeper team; dual-hat warrant authority | The full count/content of unfiled follow-ups; KNF-side pressures; that fraternization is itself the breach | Protection is never free; loyalty to the living over the org chart | Misreads the thin file as thin attention (M-03: thinness is camouflage) |
| CHAR-036 | Clara Whitmore | NQA Ravenhurst records archive, nights; section chief | Keep the night shift running; manage the break rotation | Kind, tired, observant | Scheduling knowledge (who is absent when); nothing of the hidden world; Quiet | Night staff (maternal-professional) | NQA section chief (CORP-011) | None | The rota; her authority | None | People work better when they're treated like people | Misreads Arthur's oddity as night-shift fatigue |
| CHAR-037 | Henry Lawson | NQA Ravenhurst records archive, nights; senior clerk | Keep the room's seams intact; dry-mentor the new clerk | Dry, steady, ten-years-on-nights | Ten years of night-shift knowledge; the cover story's seams; nothing of the hidden world; Quiet | Arthur (mentor's distance); Okada (professional) | NQA senior clerk (CORP-011) | None | Institutional memory; seniority | None | Nights reveal who people are | Misreads Arthur's filing obsession as diligence |
| â€” | **TRACK ON APPEARANCE** (deceased/historical one-scene figures) | â€” | â€” | â€” | â€” | â€” | â€” | â€” | â€” | â€” | â€” | â€” |
| CHAR-018 | Yusuf Hidayat (1951â€“2017, deceased) | *Ravenhurst, 2017 â€” the transfer* | Track on appearance (inheritance-chain beats only) | â€” | ANOMALY-001 holder 1996â€“2017; Quiet Night survivor; Loud | Brother Agus (CHAR-035); successor Arthur (proximity transfer) | None (survivor) | Deceased (2017) | N/A | The 1996 survival story | UNKNOWN (recorded) | N/A |
| CHAR-019 | Ilsa Brandt (1962â€“1996, missing) | *1989â€“1996 journals; missing since 1996* | Track on appearance (journal-reading beats; the handwriting tripwire) | â€” | ANOMALY-001 holder â‰¤1989â€“1996; journal author; Ilsa's torn page (the page's content UNKNOWN to all living) | Previous/next holders | Cartographers-adjacent (contested) | Missing, presumed dead | The journals | The torn page; the 1996 counterparty | Ratchet has an end (the journals' claim) | N/A |
| CHAR-020 | Eleanor Vance (1903â€“1971) | Historical | Track on appearance (1949 Accords beats) | â€” | Architect of the 1949 Meridian Accords; first Compact SG | â€” | INTL-001 (foundational) | Deceased | N/A | N/A | N/A | N/A |
| CHAR-021 | Leonid Kulik (1883â€“1942) | Historical | Track on appearance (Tunguska Seep report beats) | â€” | First suppressed Tunguska Seep report | â€” | â€” | Deceased | N/A | N/A | N/A | N/A |
| CHAR-022 | Miriam "Mother Mercy" Adler (1928â€“1971) | Historical | Track on appearance (Choir-founding beats) | â€” | Founder, Drowned Choir (SUP-001/REL-005); Drowned 1971 | â€” | SUP-001 (foundational) | Deceased | N/A | N/A | N/A | N/A |
| CHAR-023 | Emil Sorensen (1922â€“1988) | Historical | Track on appearance (Quiet Night beats) | â€” | Compact SG during 1977 Quiet Night; ordered the "Long Quiet" | â€” | INTL-001 (historical) | Deceased | N/A | N/A | N/A | N/A |
| CHAR-024 | Lena Hoffmann (b. 1961) | Historical-adjacent | Track on appearance (Rhine Drowning inquiry beats) | â€” | German investigator; Rhine Drowning inquiry | â€” | Independent | â€” | â€” | N/A | N/A | N/A |
| CHAR-035 | Agus Hidayat (1955â€“1977) | Deceased | Track on appearance (Quiet Night casualty beats) | â€” | Yusuf's brother; died in the Quiet Night | Brother Yusuf (CHAR-018) | â€” | Deceased (1977) | N/A | N/A | N/A | N/A |

---

## Â§6. Ledger lifecycle â€” creation, promotion, demotion

1. **Creation:** a "track on appearance" entry is created the first time a character appears in two or more scenes in a batch. Promotion to full eleven-field tracking is automatic at that point.
2. **Promotion to major:** when a character acquires a Arthur-independent objective (they enter a conflict record RC-/CG- as a party, not scenery), they move to the full ledger with all eleven fields. The planner must backfill fields 1â€“11 from canon at promotion â€” no field may default to "assumed."
3. **Demotion:** a character demoted to "track on appearance" keeps their archived history (fields retain their scroll) but the batch audit only re-checks fields 1, 4, 5. Demotion is recorded with the chapter and the in-story reason (death, departure, storyline closure).
4. **Death:** death entries are permanent and final â€” no resurrection, per POWER_PROGRESSION Â§C (resurrection is CANON-LOCKED impossible). A dead character's ledger is sealed with the cause and chapter. Echoes are not people (canon) â€” if an echo appears, it gets a *new* track-on-appearance entry, never the dead character's row back.

---

## Â§7. Canon-safety rules for the ledger

1. **No field may invent backstory.** Every value must trace to `DATABASE/CHARACTERS.md`, `DATABASE/ROMANCE_ARCHITECTURE.md`, `DATABASE/ARC_ARCHITECTURE.md`, or a cited chapter. UNKNOWN is always preferable to invention.
2. **Arrival dates are hard.** Pramudya Nugroho is not in Ravenhurst before September 2024 (EVENT-100). A ledger entry showing him in Ravenhurst at ch. 20 is a continuity error â€” the audit checks location against arrival canon.
3. **The romance candidates' UNKNOWN histories stay UNKNOWN.** Romance ARCHITECTURE Â§2â€“6 explicitly record several relationship histories as UNKNOWN, not as "none." The ledger must never fill these with invented pasts.
4. **Deceased/historical characters stay deceased/historical.** CHAR-018/019/020â€“024/035 are track-on-appearance only. No flashback may change their ledgered facts.
5. **The 1K is the 1K; the rent is Â£48,000; the shift is 22:00â€“06:00.** Arthur's ordinary-life anchors are drift-sensitive â€” see `DATABASE/ARTHUR_PROGRESS_TRACKER.md`. The ledger rejects any ordinary-life change (moved apartment, new job) without the corresponding arc beat and its cost.

---

## Â§8. The ordinary-life four functions check

Per `DATABASE/STORY_ENGINE.md` Â§4, the night shift / family dinner / convenience store geography / Okadaâ€“Hasegawa / Night Clerks cell each fire four functions per arc: **rest, contrast, stakes-grounding, information bottleneck**. The Character State Tracker's batch audit (Â§10) includes this check: **any batch whose arc-adjacent chapters spend stakes without rest, or spend information without bottleneck, is flagged.** Specifically:

- Arthur's ledger fields 7â€“8 (injuries, resources) moving *down* (harmed, poorer) without field 3 (emotional state) registering rest-beats in the same batch â†’ **misery drift** flag.
- Field 4 (knowledge) expanding for Arthur without the records room, Loud recall, or the wrong-file-next-to-the-right-file being the cited source â†’ **omniscience drift** flag (he files what he sees, and what he sees is partial).
- Any chapter where Okada or Hasegawa notice nothing, do nothing, and exist only as furniture for three consecutive batches â†’ **furniture drift** flag (kindness-as-cover is a register, not set dressing).

---

## Â§9. Interaction with the Arthur Progress Tracker

CHAR-001's fields are maintained here in summary form only. The authoritative record for Arthur is `DATABASE/ARTHUR_PROGRESS_TRACKER.md` (the sixteen-field schema, the three-state separation doctrine, growth accounting). The batch audit reconciles the two: if this tracker's Arthur row contradicts the Progress Tracker, the Progress Tracker wins and this row is re-written.

---

## Â§10. THE SIX ANTI-AMNESIA RULES

Characters must not forget major events, injuries, betrayals, or discoveries between chapters; must not change personality suddenly; must not lose knowledge.

### Rule 1 â€” Major events are permanent ledger entries
**Rule:** any event the arc ledger marks as major (a reveal, a death, an exposure, a betrayal, a promise, a debt) may never be absent from the affected character's fields 4/5/6 in a later batch.
**Detection:** the batch audit runs the **major-events replay**: it lists every major event in the character's history-scroll and checks that fields 4/5/6 still reflect it. A field that reads as if the event never happened (e.g., a character who was betrayed treating the betrayer with neutral warmth) is flagged.
**Correction:** the field is re-written to reflect the event, and the planner must add a reconciling beat in the *next* batch (an explanation of the apparent lapse â€” suppressed, compartmentalized, or the ledger error is corrected in-story only if an in-story mechanism exists; otherwise the ledger is fixed silently and the audit notes the fix).

### Rule 2 â€” Injuries heal at canon rates, never faster
**Rule:** field 7 (injuries) follows real recovery times: sprains in weeks, fractures in months, Erosion never (irreversible, POWER_PROGRESSION Â§F). The healer's paradox binds: aggressive Bone healing transfers Erosion-risk to the healer â€” a healed injury without a ledgered cost is a violation.
**Detection:** the audit checks each injury's chapter-range against its recovery window. An injury recorded at ch. X and gone by ch. X+10 with a 90-day canon window is flagged. Erosion decreases are *impossible* â€” any Fathom decrease in any character is a hard error.
**Correction:** the injury is restored to the ledger with its remaining recovery window; the planner must write the still-healing state in the next batch.

### Rule 3 â€” Betrayals change relationships, never vanish
**Rule:** a betrayal recorded in field 5 (relationships) must still move the relationship ledger in every subsequent batch until the arc's own beat ledger resolves it. A betrayed character may forgive, understand, or compartmentalize â€” each is a *recorded transition* with a chapter citation, never a silent reset.
**Detection:** the audit's **trust-trajectory check**: it plots field-5 values across batches. Any unexplained positive inflection after a betrayal (warmth returning without a reconciling event) is flagged.
**Correction:** the relationship is re-written to the betrayal-consistent state; the planner may stage a forgiveness/closure beat in the next batch if and only if the evidence window supports it.

### Rule 4 â€” No sudden personality change
**Rule:** field 3 (emotional state) and the personality baseline in CHARACTERS.md may not change without a ledgered cause. The allowed causes: (a) a major event in the batch (cited); (b) Erosion's personality erosion at 40â€“60 Fathoms (POWER_PROGRESSION Â§F â€” the thinning, canon); (c) a Choir seeding whose backlash is itself ledgered (canon mechanics); (d) the internal arc's documented transitions per STORY_ENGINE Â§3 (for Arthur only). Anything else is drift.
**Detection:** the audit compares field 3 across batches for step-changes with no cited cause in fields 2, 4, or 5. A step-change without a cause is flagged.
**Correction:** the field is rolled back; the planner may introduce the change *gradually* over a cited multi-batch transition if the story requires it.

### Rule 5 â€” No knowledge loss between chapters
**Rule:** field 4 (knowledge) is monotonic except by two mechanisms only: (a) Quiet memory editing by the Veil â€” which is *itself* a ledgered event with a cause (the pipeline, an encounter), applied only to Quiet characters (Nadia, Okada, Hasegawa, the family); (b) infohazard contamination handled per canon. An Attuned or Loud character may not "forget" what they learned.
**Detection:** the audit's **knowledge monotonicity check**: any field-4 entry present in batch N and absent or weakened in batch N+1 without a cited Veil-edit or infohazard event is flagged. Arthur's Loud memory makes him the audit's reference standard â€” his field 4 may only shrink by in-world infohazard mechanics (canon-derived risk: his Loudness is an infohazard liability â€” POWER_PROGRESSION Â§I, THEORY).
**Correction:** the knowledge is restored. If the drafter intended a memory edit, it must be re-written as an explicit Veil event with an authoring mechanism, or as infohazard exposure with canon consequences.

### Rule 6 â€” Secrets stay secret until their exposure window
**Rule:** field 9 (secrets) may not leak to other characters' field 4 except through the ledgered exposure vector and at the mystery-schedule window (REVEAL_ORDER). Accidental on-page leakage â€” a character referencing knowledge they cannot have â€” is the most common failure and the audit's primary target.
**Detection:** the audit cross-checks every character's field 4 against every other character's field 9: if character B's knowledge contains a fact that is character A's secret, the exposure vector and chapter citation must exist. A match without a vector is flagged as **premature knowledge**.
**Correction:** either the exposure is re-written as having a valid vector (if the story supports one) or B's knowledge is rolled back and the scene that exposed it is flagged for rewrite.

---

## Â§11. Three-state separation â€” pointer

The three-state separation doctrine (WHAT ARTHUR KNOWS vs WHAT THE READER KNOWS vs WHAT IS ACTUALLY TRUE) is defined authoritatively in `DATABASE/ARTHUR_PROGRESS_TRACKER.md` Â§11. It binds the Character State Tracker at the following points: field 4 (knowledge) is Arthur's column only â€” the planner must not let the reader's column (SECRET-007, SECRET-015) or the truth column leak into any non-Arthur field 4 without a cited information path. The romance candidates' field 4 entries are especially sensitive: Nadia's, Kira's, Aisha's, Pram's, and SaitÅ's knowledge must each be defensible against the question *"how did they learn this?"*

---

## Â§12. POWER CONTINUITY

**The seven verification items** â€” checked per character, per batch, for any character who channels, holds an anomaly, or operates Seep-adjacent equipment:

1. **Ability state:** what the character can currently do â€” including Arthur's current Use ladder position (Uses discovered, per POWER_PROGRESSION Â§C). No ability may appear that the Use ladder or the stage curve does not support.
2. **Limitations:** the active limits (Laggard hard limits for Arthur: fixed to holder's position; cannot affect matter directly; base lag ~3s; Lantern-visible deep use; the entity's attention; "a bullet still works"). Limitations may not be waived for convenience â€” a waived limit requires the documented cost that buys the waiver.
3. **Costs:** the price paid for every use in the batch (ratchet fractions for Arthur â€” logged ~0.25s, unlogged ~1s; Fathoms for the Attuned, irreversibly upward). A use without a ledgered cost is a power-jump-brake violation.
4. **Previous usage:** cumulative accounting â€” Arthur's ratchet position (3.0 â†’ 3.1 by ARC I; the per-season budget ~1â€“1.5s), each Attuned character's Fathom depth (monotonic, per Rule 2 of Â§10). The ledger carries running totals.
5. **Recovery requirements:** physiological (Arthur: nosebleeds, chill, exhaustion proportional to depth â€” a 3-minute deepening = a day in bed); Attuned: rest, Stillwater, stand-down years per the Fathom tables. A character who used hard in batch N and is fresh in batch N+1 without the recovery beat is flagged.
6. **Environmental requirements:** wards dampen the Laggard's Membrane-side effects (cannot sever the tether; deep use inside wards is louder at the entity's end); Tide pressure; light conditions (the Laggard drinks ambient light); the ninety-second rule for Attuned formations. If a batch's scene contradicts the scene's environment, it is flagged.
7. **Known counters:** the counters documented against each ability must be *available to the opposition* where canon says they are (Lantern-sensitives within kilometers of deep use; wards; bullets; information advantage). An ability that lands where its documented counter should have fired â€” and the counter is never mentioned â€” is flagged (the counter's absence must itself be explained: Tide-noise, unfamiliarity, or the opponent's error, ledgered).

**The no-new-ability-without-reason rule:** no character gains an ability, a Use, or a new application of an existing ability without one of the canon ladders: Arthur â€” the generative principle (observe â†’ hypothesize â†’ test at the smallest falsifiable scale â†’ pay the cost, POWER_PROGRESSION Â§C); the Attuned â€” the discipline's fixed domain and the 7-stage Erosion economy. "He tried harder" is never a reason.

**Tie to the 8 power-jump brakes and the 16-item no-shortcut list:** both are bound on every arc transition per ARC_DEPENDENCY_GRAPH (no stage skipped, no Use spent without its price, the escrow's reliability model changing only via documented triggers). The power-continuity audit operationalizes them: any batch that advances Arthur's Use ladder or any Attuned's effective tier must cite the brake it passed through (the generative principle's four steps; the Erosion ledger; the ratchet budget). A batch that cannot name its brake is rejected.

---

## Â§13. FACTION CONTINUITY

**The eight tracking axes** â€” maintained per faction that acts or is acted upon in the batch (the full roster lives in `DATABASE/FACTIONS_AND_CONFLICTS.md`):

1. **Objective:** the faction's Arthur-independent objective (per the roster â€” e.g., the Quiet Desk's "file everything," the Court's "custodianship"). Objectives change only through the faction's own conflict records; a faction may not quietly acquire a new objective off-page.
2. **Resources:** money, personnel, assets, stockpiles (the Drowndust cache; the Ledger's liquidity; the Compact's ~2,000 Seismograph stations). Spent resources stay spent â€” a faction that lost a cache in ARC IV may not act as if it holds one in ARC VII.
3. **Knowledge:** what the faction knows about Arthur specifically â€” cross-referenced to the "five actors hold canon facts" rule (STORY_ENGINE Â§6: CORP-011, GOV-006, GOV-014, IND-004, SUP-009). **Any sixth faction's knowledge of Arthur must cite its acquisition path.** This is the faction-continuity audit's primary target.
4. **Strategy:** the faction's current plan (the Desk's recruitment pitch; the Bell's ninth-site hunt; the Court's collecting doctrine). Strategies evolve through the 102 conflict records' 2nd/3rd-order consequences â€” never by authorial fiat.
5. **Recent losses:** what the faction has lost in the last two batches (personnel, assets, legitimacy). Losses constrain what the faction can attempt next.
6. **Recent gains:** what the faction has gained. Gains constrain what the faction *must defend* next.
7. **Relationships:** the relationship matrix stance (ALLIES Â· CLIENT Â· COLD Â· WARY Â· RIVALS Â· AT-WAR Â· UNAWARE Â· TOLERATED Â· TRUCE) toward every faction it interacted with in the batch. Stance changes cite the event (e.g., the TRUCE stances break only per J.4 conditions).
8. **Active operations:** every operation the faction is running, with its status. **Operations do not pause between arcs.** An operation started in ARC III and never resolved is still running in ARC V unless its conflict record shows resolution â€” this is the factions-remember rule.

**The factions-remember rule:** factions have institutional memory. A faction that was humiliated, outbid, or exposed in a batch *acts like it* in the next â€” the stance matrix moves, the strategy adjusts, the losses constrain. The audit's **institutional-memory check** flags any faction whose behavior in a batch is inconsistent with its last two batches of losses and gains.

**Tie to the 28/28 autonomy verdict:** all 28 profiled factions are autonomous with Arthur-independent objectives; 0 of the 102 conflicts are Arthur-required (`DATABASE/FACTIONS_AND_CONFLICTS.md` Â§D: Arthur-dep. count 0). The Chapter Engine must therefore **schedule faction action between Arthur's chapters**: every batch planning cycle includes a faction-tick pass â€” each faction on the interleave map (ARC_ARCHITECTURE Â§13.1/13.3) advances its operations by one tick according to its own logic. Arthur chapters *intersect* these ticks; they do not *cause* them. The audit verifies: any batch in which a faction's only action is reacting to Arthur, with no independent tick, is flagged as **protagonist-centrism drift**.

---

## Â§14. ROMANCE CONTINUITY

**The nine tracking axes** â€” maintained per configuration *that is active*, plus the relationship-state of the unselected four (per STORY_ENGINE Â§7, unchosen configurations persist as relationships, never dangling threads):

1. **Trust:** the current trust level and its ledger of events (the file-sharing beat; the disclosure; the breach). Trust moves only through events.
2. **Emotional state:** each partner's working emotional register toward the other (per ROMANCE_ARCHITECTURE's per-config trust patterns).
3. **Recent interaction:** the last meaningful scene between the two, its chapter, and what it changed.
4. **Unresolved conflict:** the active structural tension (the Tuesday problem for A; the triangle for B; the seam for C; the fieldwork-vs-kindness for D; tool-vs-weather for E). Unresolved conflicts do not resolve by time passing.
5. **Secrets:** the romance-relevant secrets (her unfiled follow-ups; his mirror; the triangle's upstream; the journals' custody) with exposure vectors and windows.
6. **Shared experiences:** the accumulated history â€” dawn convenience store mornings, archive sessions, the doctrine argument. This is the anti-amnesia field for romance: shared experiences may never be treated as if they didn't happen.
7. **Progression:** the measurable movement along the configuration's trust engine (courtship by repeated low-stakes proximity for A; the arithmetic stated for B; respect-first for C; courtship by archive for D; the friendship's doctrinal negotiation for E).
8. **Regression-if-justified:** setbacks are allowed *only* with cited cause (the leak for A; the Institute's pressure for B; the seam's treason reading for C; the scheduled betrayal for D; the demographers' flag for E). Regression without cause is a Rule-4 violation.
9. **Expectations:** what each partner currently expects of the other and of the relationship â€” including the *family gauntlet* expectation (Rule 5: the dinner outranks any declaration; *New Year* is the annual audit).

**The NO-RESET rule:** romance never resets between arcs. No timeskip, no arc boundary, no "fresh start" may return a relationship to an earlier state. Trust earned in ARC III is still earned in ARC VII; a wound inflicted in ARC VI is still a wound in ARC IX unless the ledger shows its resolution. The audit's **romance-trajectory check** plots all nine axes across batches; any axis that returns to a prior value without a cited resolving event is flagged.

**The intimacy-only-through-events rule:** intimacy (emotional or physical) advances only through staged events with evidence â€” per ROMANCE_ARCHITECTURE Â§9, romance beats cannot land before their evidence exists (reveal-order gating). A configuration's intimacy may not outrun its information economy. The audit checks: the current intimacy level must be supportable by the cited shared experiences in axis 6.

**Parameterization across configurations Aâ€“E:** this schema is configuration-agnostic. The same nine axes track Arthur Ã— Nadia (A), Ã— Kira (B), Ã— Aisha (C), Ã— Pram (D), or Ã— SaitÅ (E). The configuration-specific content lives in ROMANCE_ARCHITECTURE Â§1â€“6 (trust patterns, attraction triggers/blockers, structural tensions, information asymmetries) â€” the tracker references those, and does NOT select among them. At selection time, the Chapter Engine activates one configuration's nine axes in full and maintains the other four as STORY_ENGINE Â§7 relationships (Aâ†’colleague, Bâ†’professional contact, Câ†’institutional protector, Dâ†’professional betrayal/friendship, Eâ†’the great friendship) with axes 1â€“4 maintained at minimum.

**The six romance rules as audit constraints:**
- Rule 1 (no deceived civilian partner): if the active configuration involves a Quiet partner, the asymmetry's management must appear in axes 4/5 â€” the asymmetry is *the story*, never background.
- Rule 2 (consent includes memory): any axis-6 (shared experience) involving a Quiet partner's forgotten days must be ledgered as an intimate violation, never as an advantage â€” the audit flags any beat that treats Loud recall of a Quiet partner's forgotten experience as "cute."
- Rule 3 (Erosion is not romantic): axes 2/7 for Configuration B may never aestheticize the Fathom clock â€” the audit flags tragedy-porn framing.
- Rule 4 (factions don't pause for love): axis 8 of FACTION continuity (Â§13) and romance axis 4 are cross-checked â€” a partner's handler/faction pressure must be *present* in the romance ledger wherever the surveillance gradient says it is (B: Census-monitored; C: government-contract; A: SSW-adjacency watchlist; D: Hollow-discipline monitoring; E: structurally invisible, NQA employer files only).
- Rule 5 (the dinner rule): axis 9 must record the dinner gauntlet's status per configuration (A: post-final-revelation; B: post-triangle-resolution; C: post-seam-priced; D: post-telling; E: post-mirror). Commitment without the dinner is a hard error.
- Rule 6 (Arthur's weakness applies): his romantic assets in any axis are attention, memory, honesty, and showing up â€” the audit flags any beat where he is suave, rich, or powerful.

**The 7 independence watches** (ROMANCE_ARCHITECTURE audit Â§10): the unselected candidates' ledgered independence (their own objectives, their own scenes, their own lives) is checked by the batch audit â€” no candidate may exist only as a romance option. If an unselected configuration's relationship-state hasn't moved in three batches, the audit flags **dangling-thread risk** and the planner must schedule the STORY_ENGINE Â§7 maintenance beat.

---

## Â§15. Batch audit procedure (summary)

Per chapter batch, the planner runs, in order:
1. **Field update pass** (Â§3) â€” all touched characters, all touched factions, active romance axes.
2. **Anti-amnesia sweep** (Â§10) â€” major-events replay, injury-rate check, trust-trajectory check, personality step-change check, knowledge monotonicity check, secret-exposure vector check.
3. **Power continuity pass** (Â§12) â€” the seven verification items for every ability use; brake citation for every ladder advance.
4. **Faction continuity pass** (Â§13) â€” the eight axes; institutional-memory check; the faction-tick pass (protagonist-centrism drift check).
5. **Romance continuity pass** (Â§14) â€” the nine axes; NO-RESET trajectory check; intimacy-evidence check; the six-rule cross-check; independence-watch check.
6. **Ordinary-life four-functions check** (Â§8) â€” rest/contrast/stakes-grounding/bottleneck coverage.
7. **Ledger commit** â€” every change cites its chapter; the history-scroll is appended, never overwritten.

---

*End of CHARACTER_STATE_TRACKER.md â€” Phase 9, THE QUIET TIDE.*


---

## SECTION: `DATABASE/ARTHUR_PROGRESS_TRACKER.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `DATABASE/ARTHUR_PROGRESS_TRACKER.md` Â· sha256 `0c2a970fe8a006bd31cdd5d019799e3c95e5665daedd20fa0534b67c37d4abf6` Â· 3,777 words. No content changed.

# DATABASE â€” Arthur Progress Tracker (THE QUIET TIDE)

> Phase 9 â€” Chapter Engine Architecture: Tracking Systems. Operational machinery only â€” no chapters, scenes, prose, dialogue, or chapter titles.
> Sources of truth: `DATABASE/CHARACTERS.md` (CHAR-001) Â· `DATABASE/ROMANCE_ARCHITECTURE.md` (Â§1 â€” Arthur's profile) Â· `DATABASE/POWER_PROGRESSION.md` (the 7 stages, the 12 documented Uses, the ratchet, the generative principle, the 16-item no-shortcut list, the 8 power-jump brakes) Â· `DATABASE/STORY_ENGINE.md` (Â§3 internal arc UNFILEDâ†’ANSWERABLE; Â§4 ordinary-life engine) Â· `DATABASE/ARC_ARCHITECTURE.md` Â· `DATABASE/LONG_SERIAL_STRUCTURE.md`.
> Canon lock: Arthur's growth is **understanding-shaped, never power-shaped** (STORY_ENGINE Â§3 invariants; POWER_PROGRESSION curve verdict: *"the Laggard's output stays ~zero throughout; what grows is Arthur's read of it and the world's read of him. The bullet still works at Stage 7."*) The tracker below is the instrument that enforces this.

---

## Â§1. Purpose

The Character State Tracker (`DATABASE/CHARACTER_STATE_TRACKER.md`) covers every character. This tracker is Arthur-only, deeper, and differently shaped: it tracks **what he knows, what he can read, what he owes, and what he has spent** â€” not what he can do. It is the machine that keeps the protagonist ordinary for ~1,000 chapters while the world around him prices him as a market-maker.

---

## Â§2. Tracker schema â€” the sixteen fields

Every field is defined once, then carries its **series-start value** (ARC I opening, ch. ~1) grounded in canon. No invented backstory.

| # | Field | Definition | Series-start value (canon-grounded) |
|---|---|---|---|
| 1 | **Physical condition** | Body state: health, injuries, fatigue, conditioning, reaction speed, and the anomaly's physiological toll. | Healthy; 24; lean and athletic; good cardiovascular conditioning; fast natural reaction time; no Esper-powered physical enhancement. He maintains fitness through regular running and ordinary conditioning. The anomaly's social cost is already active (dim rooms, dead plants); no injuries. |
| 2 | **Mental/emotional condition** | Working register: masking fatigue, guilt economy, loneliness, fear ledger. Tracked in the four-asset terms of Â§3. | Meticulous, dry, conflict-avoidant; masking fatigue present; the guilt economy running (carries cost pre-emptively); inverted loneliness load-bearing. Believes safety = absence. |
| 3 | **Anomaly understanding** | What he understands about ANOMALY-001 â€” the mechanism model he currently holds, including the parts he knows he doesn't know. | Near-zero. Observes the lag (~3s, unmeasured as rule); no tether concept; does not know Yusuf's name is connected (proximity + Loudness, unengineered â€” he was 17). Incorrectly believes: the shadow is a personal curse/inconvenience; his memory is just "good memory." |
| 4 | **Anomaly control** | What he can do with the anomaly deliberately â€” the discovered-Use ladder position (Uses 0â€“12, per POWER_PROGRESSION Â§C), each with its discovery chapter and cost paid. | Uses 0â€“1 only (notice + Use 1: Veil-immune witness, discovered by observation). Cannot do anything supernatural on purpose. |
| 5 | **Known limitations** | The hard limits he currently understands (subset of the full canon limits â€” he may not know them all). | Knows: none, yet. (Full canon limits â€” fixed to holder's position; cannot affect matter directly; base lag ~3s; out-of-phase cannot act; "a bullet still works" â€” live in the engine's copy, not his head.) |
| 6 | **Known counters** | The counters he knows exist against *his* anomaly (subset of canon). | Knows: none. (Canon: wards dampen; Lantern-sensitives detect deep use across kilometers; Stillwater/Anchor/Drowndust don't affect him â€” which is why institutions use recruitment.) |
| 7 | **Resources** | Money, equipment, access, favors. | ~Â£230,000/month salary; Â£48,000/month 1K rent in Willowmere; records-room access (B2â€“B3); the Night Clerks' Discord; SaitÅ's shared memory. No equipment beyond civilian. |
| 8 | **Money** | Separate from resources: the cash-flow ledger â€” salary, rent, the costs the anomaly imposes (dead plants, shortened dates), any faction money (none at start; any arrival is a ledgered event with strings). | Ordinary: salary in, rent/food/convenience store out. No hidden-world income. Any future money from a faction is tracked with its price (Vesper's funding is "impossible to leave"; the Ledger's money is a leash). |
| 9 | **Equipment** | Tools of the clerk's method: notebooks, reflective surfaces, cameras, the escrow's legs (once built). | Civilian only: phone, notebooks, the archive's equipment. No supernatural tools. |
| 10 | **Relationships** | Trust states toward every recurring character â€” pointer to the Character State Tracker's field 5; this field tracks the *Arthur-side* ledger only. | Mother/father/sister (dutiful, withheld); SaitÅ (closest friend, shared noticing); Night Clerks cell; Okada/Hasegawa (professional respect). Romance seeds: A's melon pan/dawn convenience store (one-sided, unparseable); E's friendship (pre-built). |
| 11 | **Faction awareness** | What he knows about each faction's existence, objectives, and interest in him â€” the engine's copy holds the truth; his copy holds what he's seen. | Knows: his employer NQA; nothing of the hidden world's factions (the SMD, the Desk, the Exchange, the Court are all unknown or rumors). The world's read of *him*: five actors hold canon facts (CORP-011, GOV-006, GOV-014, IND-004, SUP-009 â€” STORY_ENGINE Â§6). |
| 12 | **Known mysteries** | Mysteries he is actively aware of and working (MYSTERY-001's surface question; the 2017 transfer's story). | The shadow (001 surface); the sealed 2021 examination record (knows it exists, not its content); the flagged hiring file (EVENT-087 â€” unexamined). |
| 13 | **Unknown mysteries** | Mysteries the *engine* knows exist but he does not â€” the largest field, and the one that must never leak into his behavior. | The full L5 set (002's hinge, 003's finale, 013's nature, 015's driver); the ratchet; the entity's attention; the transfer rule; the journals; the torn page; the Desk's doctrine; the Tuesday problem's mechanism (012's authorship). |
| 14 | **Current objectives** | One primary, up to two secondary â€” per arc, per STORY_ENGINE's per-arc table. | Measure the shadow (is it real? lengthening?) while proving the camouflage thesis â€” stay a T1 curiosity beneath every instrument. |
| 15 | **Current fears** | The fear ledger â€” each fear with its chapter of origin. | Being filed; being read (the mirror beat); curiosity that spends him; costing the people who love him (the inherited guilt economy). |
| 16 | **Unresolved decisions** | Choices he has deferred â€” each with the chapter it was deferred in and the cost of deferral. | Whether to tell anyone about the shadow (deferred, ch. ~1); whether to write down the mirror (deferred â€” SECRET-005's tripwire); what the 2021 examination found (unasked). |

---

## Â§3. Series-start anchor block (immutable reference)

These values are canon anchors. They may only change through the ledgered events of the arcs â€” and Â§8 of the Character State Tracker rejects un-cited ordinary-life changes.

- **Age:** 24 (b. 14 March 2000). **Status:** Ravenhurst native; regular-employee night-shift records clerk, NQA Ravenhurst records archive (B2â€“B3), CORP-011.
- **Shift:** 22:00â€“06:00. **Housing:** 1K apartment, Willowmere, ~Â£48,000/month.
- **Anomaly:** ANOMALY-001 "The Laggard" â€” seven-year-old shadow tether to the Undertow via Yusuf Hidayat's death in Ravenhurst, March 2017 (proximity + Loudness, unengineered). Holder since age 17. Ratchet position: 3.0s (â†’ ~3.1 by ARC I's end).
- **Loudness:** Loud, not Attuned. Zero Fathoms (the anomaly does the work; he pays in attention-risk and ratchet, never Fathoms â€” POWER_PROGRESSION Â§F).
- **Census:** unregistered â€” completely legal (the Census registers the Attuned, not Loudness; Albion's employer-mediated Census never flagged him â€” no Hollow Pattern).
- **Power position:** Stage 1 (ARC I; Uses 1â€“2 discovered). Certified-weak anomaly; the camouflage thesis.
- **Internal arc position:** UNFILED â€” believes safety = absence; never be interesting.
- **Ordinary-life anchors:** the night shift; the every-other-Sunday Willowmere dinner; the 03:00 convenience store; Clara Whitmore; Henry Lawson; the Night Clerks' Ravenhurst cell.
- **Romance position:** single; all five configurations UNSELECTED; the dinner rule gates every commitment.

---

## Â§4. Update rules per chapter batch

1. **Every batch updates fields 1â€“4 and 12â€“16 at minimum.** Fields 5â€“11 update when touched; a field untouched for three consecutive batches is flagged for staleness review.
2. **Anomaly understanding (3) and anomaly control (4) move only through the generative principle** (POWER_PROGRESSION Â§C): observe â†’ hypothesize â†’ test at the smallest falsifiable scale â†’ pay the cost. Each Use discovery cites all four steps and the chapter of each. A Use that skips a step is a continuity error, not a power-up (canon).
3. **Field 4 (control) may only hold Uses â‰¤ the current stage curve** (POWER_PROGRESSION Â§D: Stage 1 = Uses 0â€“1; Stage 2 = Uses 2â€“4; Stage 3 = Uses 5â€“7 + Use 8; Stage 4 = Uses 8â€“10 + escrow live; Stage 5 = Uses 10â€“11 understood; Stage 6 = Use 12 spent/threatened + Uses 13+ via generative principle only; Stage 7 = structural ceiling). A Use above the stage is a brake violation.
4. **Field 13 (unknown mysteries) shrinks only by reveals at REVEAL_ORDER windows.** Field 12 (known mysteries) grows only by what he has witnessed or been told â€” cross-checked against the three-state doctrine (Â§11).
5. **Money (8) and resources (7) are conserved.** Every yen in and out is ledgered. A faction payment without a tracked price is flagged.
6. **Unresolved decisions (16) may not accumulate beyond five.** If the field holds five deferred decisions, the planner must resolve or escalate one in the next batch â€” deferred decisions are narrative debt.

---

## Â§5. Growth accounting â€” understanding-shaped, never power-shaped

Growth is measured in **four assets reallocated, never output gained** (STORY_ENGINE Â§3: attentionâ†’devotion, memoryâ†’testimony, honestyâ†’the telling, showing-upâ†’commitment). The tracker records each as a ledger line:

- **Attentionâ†’devotion:** his noticing reallocated from camouflage (noticing to stay unfiled) to care (noticing the people adjacent to him). Ledgered per arc with the chapter where the reallocation was priced.
- **Memoryâ†’testimony:** Loud recall reallocated from private survival to evidence â€” the clean recording (Use 10), the archive as inheritance (ARC IX), the mirror finally written down (ARC XII: *to whom*).
- **Honestyâ†’the telling:** his anti-deception discipline reallocated into disclosure â€” the telling beats per configuration (the mirror to SaitÅ at the tripwire; the page authentication on his terms).
- **Showing-upâ†’commitment:** the night shift's recurrence reallocated from tactic to vow â€” the dinner rule, the 03:00 convenience store as kept promise, the four assets.

**Per-stage growth entries (what the tracker records at each stage):**

| Stage | What the tracker records as "growth" |
|---|---|
| 1 (ARC I) | The method established: observation, not activation. The camouflage thesis proved. Three advantages named: perfect recall, clerk's eye, certified-weak anomaly. |
| 2 (ARCs IIâ€“III) | The tether as method. Stillness learned. First active options (Uses 2â€“4), every option priced. The difference between documenting and surviving. |
| 3 (ARC III) | Competence priced. Uses 5â€“8 in play. The escrow *concept*. Attention flows both ways (the lean). |
| 4 (ARCs IVâ€“VI) | Documentation becomes weapon. The escrow goes live (Use 10). Mutually assured disclosure priced. The guilt economy becomes untenable. |
| 5 (ARCs Vâ€“VII) | Erosion-free operation as *understood* advantage. He becomes a market-maker in information. The flare held in reserve. The world's read of him is the progression axis. |
| 6 (ARC VIII) | Uses 12 spent/threatened. Uses 13+ only via observeâ†’hypothesizeâ†’testâ†’pay. The ratchet's budget is now the series budget. The page names the deadline. |
| 7 (ARCs Xâ€“XII) | Structural ceiling. Information-asymmetry maturity. The clerk's method IS the finale. No new Uses needed. The test designed: his idea, his design, dangerous. |

**Growth the tracker FORBIDS recording:** any entry of the form "he can now defeat X" where X is a tier or a faction; any entry where output increases without a priced Use; any entry where understanding increases without the generative principle's four steps; any entry where the world's read of him improves without the corresponding exposure cost.

---

## Â§6. The ratchet's one-way accounting

Erosion events are permanent ledger entries. The ratchet (POWER_PROGRESSION Â§F) runs one way:

- **Base lag:** 3.0s (2017) â†’ ~3.1s (2024, ARC I). Ilsa's data: 3.0 â†’ 3.4s over seven years.
- **Pricing:** logged extreme use ~+0.25s; unlogged ~+1s; per-season budget ~1â€“1.5s (drafter's ruler â€” non-binding planning instrument, but the ledger treats it as the budget).
- **Ledger rule:** every deep-lag use, shadow-storage use, and flare (Uses 6â€“12) is entered with: the chapter, the logged/unlogged status, the fraction added, the running total. The total is **monotonic increasing, forever**. A batch that uses deep lag without a ratchet entry is a continuity error.
- **What happens at 10s, at a minute: UNKNOWN** (Ilsa's last journal page torn out â€” the tracker records the unknown, it does not fill it).
- **The anchor's degradation:** the rot-immunity boundary holds to ~3h lag-depth and T4-equivalent pressure; edge-corruption creeps inward as the ratchet climbs (POWER_PROGRESSION Â§C, Use 10). The tracker records the boundary's current state per batch where Use 10 is in play.
- **The ratchet is never a power-up.** Lengthening the lag is never recorded as increased capability â€” it is recorded as increased *cost and risk* (the entity's attention compounds; the deadline approaches). Any ledger entry framing ratchet growth as empowerment is flagged.

---

## Â§7. The four ordinary-life functions as growth witnesses

Per STORY_ENGINE Â§4, the ordinary-life engine's four functions (rest, contrast, stakes-grounding, information bottleneck) are the *witnesses* to Arthur's internal arc. The tracker cross-references:

- **Rest beats** are where the four assets recharge (the 03:00 convenience store as the one free choice; futsal by the bay). A batch with no rest beat while fields 1â€“2 degrade is flagged for misery drift.
- **Contrast beats** are where the internal arc's cost is visible (three streets over, a Sweeper team processes someone's worst night). The tracker requires contrast beats to *cost* him noticing â€” never free pathos.
- **Stakes-grounding beats** are where the arc's price lands on the ordinary (the archive access revocable; the 1K under golden-handcuffs pressure). Every stakes-grounding beat cites field 7/8.
- **Bottleneck beats** are where his information position stays partial (he files what he sees; what he sees is the records room, Loud recall, the wrong file next to the right file). The tracker rejects any field-12 growth whose source is not bottleneck-compatible â€” this is the omniscience check.

---

## Â§8. Romance-agnostic progression

The tracker records Arthur's *romantic capacity* (his assets: attention, memory, honesty, showing up â€” ROMANCE_ARCHITECTURE Rule 6) without reference to any configuration. The configuration-specific trust engines live in the Character State Tracker's Â§14. This tracker's fields 10 and 15â€“16 hold the configuration-independent material: his fear of costing people (the inherited guilt economy), his *Are you seeing anyone?* answer at the every-other-Sunday dinner (treated as possibly-changed), the mirror as the one room he keeps even from the closest friend. Whichever configuration the story engine selects, these fields are the soil it grows in.

---

## Â§9. Faction-awareness growth (the world's read of him)

Field 11's growth is the series' second progression axis (the first is understanding). The tracker records it as a **visibility ladder**, each rung with its chapter and its cost:

1. T1-curiosity camouflage (ARC I) â€” the filing that protects him.
2. The thin file stays thin â€” watch-not-act (ARC III).
3. The buyer's inquiry (EVENT-093) â€” first bid, not the last.
4. The recruitment pitch (MYSTERY-008, ARC VI) â€” the golden handcuffs refused or priced.
5. Threat, not asset (ARC V's aftermath) â€” every faction prices him differently.
6. The flare threatened (ARC VI) / spent (ARC VIII) â€” the T1 cover burned, point of no return.
7. The indispensable witness (ARCs IXâ€“XII) â€” the clerk's method as the finale.

Each rung must cite the exposure event that earned it. Visibility is never free â€” the ledger records what each rung *cost* (the camouflage of smallness, spent; the 1K apartment, the night shift â€” ARC VIII).

---

## Â§10. Relationship-debt ledger

Field 10's companion: every relationship carries a **debt line** â€” what he owes, what is owed him, and the inherited guilt economy's running balance. The guilt economy (ROMANCE_ARCHITECTURE Â§1: *"the guilt changed everything"* â€” his mother's *cleansing ritual*) resolves into *responsibility*, not absolution (STORY_ENGINE Â§3 invariants). The tracker records: each pre-emptive cost-absorption (he ends things early, arrives late, leaves early), each absorbed cost that belonged to someone else (the arc's forced lesson, ARC IV onward), and the balance's movement toward responsibility. The balance may never reach zero by absolution â€” only by answerability.

---

## Â§11. THE THREE-STATE SEPARATION DOCTRINE

### Â§11.1. The three states

For **every information beat** in every chapter batch, the planner maintains three columns:

| Column | Definition | Who holds it |
|---|---|---|
| **WHAT ARTHUR KNOWS** | Facts Arthur can defend from his own ledger â€” witnessed, read, told, or deduced from his bottleneck-compatible sources. Subdivided: *certain* (observed/reported with chain) vs *suspected* (inferred, flagged as such in his head). | Arthur's field 12 (certain) + his flagged suspicions (field 3's model, marked provisional) |
| **WHAT THE READER KNOWS** | Facts the narrative has shown the reader â€” including the two deliberate ironies where the reader leads Arthur by one phase (SECRET-007: the page for sale while he hunts it; SECRET-015: the Court's error about the Reed line), and any dramatic-irony staging the arc ledger authorizes. | The arc's reveal ledger; never Arthur's behavior |
| **WHAT IS ACTUALLY TRUE** | Canon truth per the databases â€” including the L5 set, the torn page's content, the entity's nature, the ratchet's end. Most of this column is permanently inaccessible to both Arthur and the reader. | The engine's copy only |

### Â§11.2. The merge prohibition

**No column may be merged into another without a cited information path.** Specifically:

1. The reader's column may never leak into Arthur's behavior. If the reader has seen SECRET-007 (the page for sale) but Arthur has not, Arthur may not act as if he suspects the auction. The planner must write his scenes from his column only.
2. The truth column may never leak into the reader's column except through REVEAL_ORDER's staged windows. The L5 set stays in the truth column until its protection window opens (ARC XI/XII per LONG_SERIAL_STRUCTURE Â§5).
3. Arthur's column may never contain facts whose only source is the truth column. Every entry in his column cites: the chapter witnessed, the source (records room / Loud recall / wrong-file-next-to-right-file / told-by-X / deduced-from-Y), and the certainty level.
4. **Suspicions are not knowledge.** Arthur may suspect (the arrow may have reversed; the lean points at pressure, not safety) â€” suspicions live in field 3's model, marked provisional, and may not drive action the way knowledge does. A suspicion acted on as certainty is flagged.

### Â§11.3. Worked examples of the three states diverging (generic, not chapters)

**Example A â€” the auction irony.** *Arthur knows:* a page of Ilsa's journal is missing; the ratchet lengthens with deep use. *The reader knows:* the page is for sale at the Second Silence Auction, with three factions bidding (SECRET-007's deliberate irony â€” the reader watches the bidding before Arthur does). *Actually true:* the page names the ratchet's end, and its content is worse than the bidding assumes (L5-5, held to ARC VIII). The merge prohibition: Arthur's search for the page must be written without any knowledge of the auction; the reader's tension comes from the gap, not from his acting on it.

**Example B â€” the Court's error.** *Arthur knows:* the Pale Court is interested in him (the gala question; the cadets' bid). *The reader knows:* the Court's diligence is built on a wrong theory â€” there is no hidden Reed aristocracy (SECRET-015; canon: the wrongness is the point). *Actually true:* he is a 24-year-old clerk whose ordinariness is the whole story. The merge prohibition: Arthur may not act as if he knows the theory is wrong *about him specifically* until the appraisal beat (ARC V) gives him the evidence; the reader's dramatic irony is the gap between the Court's certainty and his ordinariness.

**Example C â€” the tether's end.** *Arthur knows:* deep use is noticed (cold drift, dreams of dark water); the shadow leaned first in the deep-lag session. *The reader knows:* the same, plus the journals' last un-torn warning (the arrow may have reversed). *Actually true:* whether the entity's attention is intelligence, and whether it has intentions (L5-2 â€” the hinge is *whether it answers*, held to ARC XII). The merge prohibition: neither Arthur nor the reader may treat the entity as a character with motives until the test is earned; the planner must keep both columns at "felt looked-at; no word for it."

**Example D â€” the pipeline.** *Arthur knows:* Nadia's filings soften; the manual's revision history exists. *The reader knows:* (post-leak) what her hands did, in the revision history, with him present. *Actually true:* the routine's authorship (MYSTERY-012 â€” UNKNOWN; possibly NQA training, possibly Quiet Desk procedure, possibly emergent pipeline incentives). The merge prohibition: after the leak, Arthur knows *what* happened but not *who authored* the routine â€” the planner must not let him act as if the authorship question is settled; the truth column's UNKNOWN must survive the reveal.

### Â§11.4. Per-batch reconciliation procedure

For every information beat in the batch, the planner produces **all three columns** in the beat's ledger entry:

1. **Beat identification:** the chapter, the scene, the fact at stake.
2. **Column A (Arthur):** what he knew before, what changed, the source, the certainty level. If the beat *should not* change his knowledge (he wasn't there; the source is bottleneck-incompatible), the entry says so explicitly.
3. **Column B (Reader):** what the reader knew before, what the beat shows them, whether the beat widens or narrows the Arthurâ€“reader gap (the two ironies are the only authorized lead; any other reader-lead is flagged).
4. **Column C (Truth):** the canon truth, cited to the database. If UNKNOWN, the entry says UNKNOWN â€” the planner does not speculate.
5. **Merge check:** the auditor verifies no column's new content could only have come from another column without a cited path. A failure is a hard error â€” the beat is rewritten.

### Â§11.5. The doctrine's load-bearing function

The three-state separation is what makes the long serial's dramatic irony *sustainable*: the reader can lead Arthur by one phase for 700 chapters without the story collapsing into either omniscience (Arthur acting on reader knowledge) or frustration (the reader never learning anything). It is also what protects the L5 schedule â€” the truth column's protection windows are enforced by the merge prohibition, not by anyone's memory.

---

## Â§12. Interaction with the other two tracking files

- **Character State Tracker** (`DATABASE/CHARACTER_STATE_TRACKER.md`): Arthur's summary row there reconciles to this file; this file wins on conflict. The anti-amnesia rules (Â§10 there) apply to Arthur's fields here with the three-state doctrine as the knowledge-field's special case.
- **Long-Term Continuity** (`DATABASE/LONG_TERM_CONTINUITY.md`): this file's fields 3, 4, 6, 12, 13, and 16 are the primary inputs to the continuity ledger's fifteen categories (character development, power progression, resolved/active mysteries, injuries, promises, debts, secrets, unresolved decisions). The band-handoff audit re-certifies them at every band boundary.

---

*End of ARTHUR_PROGRESS_TRACKER.md â€” Phase 9, THE QUIET TIDE.*


---

## SECTION: `DATABASE/CHAPTER_FORESHADOWING_TRACKER.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `DATABASE/CHAPTER_FORESHADOWING_TRACKER.md` Â· sha256 `52e9ebeb4b7adc1cdfb992f2b3b15510c5b6185d60dc4eb8fa11c029a4ed8aee` Â· 3,388 words. No content changed.

# DATABASE â€” CHAPTER FORESHADOWING TRACKER (Chapter Engine)

**THE QUIET TIDE v1.9** Â· Phase 9: Chapter Engine Architecture â€” TRACKING SYSTEMS
**Purpose:** the pipeline that carries every clue from planting to payoff. This file stages *how* clues are laid; CHAPTER_MYSTERY_TRACKER.md tracks *what stage each mystery has reached*; INFORMATION_FLOW.md governs *who learns what*.
**Canon anchors:** DATABASE/FORESHADOWING.md (38 clue chains: core cluster 001â€“015 with 142 typed entries; A/B majors 016â€“038 condensed; 5 repaired gaps; 6 strengthened weak clues) Â· DATABASE/MYSTERIES.md (herring lists per record) Â· DATABASE/RED_HERRINGS.md (RH-001â€“036 registered; M-01â€“06 structural misdirections; 7 unregistered candidates â€” texture only) Â· DATABASE/REVEAL_ORDER.md (reveal stages, phases, the L5 protection schedule) Â· DATABASE/ARC_ARCHITECTURE.md (arc windows) Â· DATABASE/INFORMATION_KNOWLEDGE_MAP.md (asymmetry rules).
**Not this file:** no chapters, no scenes, no prose. A staging plan, not a chapter plan. Every entry below is a series-start plan (Stageâ‚€ = UNPLANTED); the pipeline advances through the batch protocol (CHAPTER_MYSTERY_TRACKER.md Â§4).

---

## Â§1 â€” THE FIVE-STAGE PIPEmessaging app

| Stage | Job | Minimum separation guidance |
|---|---|---|
| **1. SETUP** | Plant the clue with no explanation. The reader *sees* it before knowing its meaning. A good setup is legible on reread and invisible on first read â€” texture that turns out to have been evidence. | Must land at least one full arc before its reveal arc. For MAJOR reveals, setup â‰¥2 arcs before the reveal is the norm. Setup that shares an arc with its reveal is not foreshadowing â€” it is exposition wearing a costume. |
| **2. REINFORCEMENT** | Repeat or vary the clue so it becomes pattern, not noise. Reinforcement is what makes the reader *carry* the clue across hundreds of chapters â€” the carrying time is the payoff's principal. (Cf. SECRET-005: the mirror tripwire pays in proportion to 300 chapters of carrying.) | At least one arc after setup; for majors, reinforcement beats should span â‰¥2 arcs. A clue reinforced only once, in the same arc as setup, is a hint, not a chain. |
| **3. MISDIRECTION** | Pair the true clue with a false frame â€” a registered herring (RH-###) or a structural misdirection (M-##) â€” so the reveal is protected without being unfair. The herring must be *disprovable in-world*: a misdirection that cannot be disproved is a lie, and lies are texture (the 7 unregistered candidates), never staged misdirection. | Planted before or with reinforcement, never after the reveal. A herring that outlives its sell-by (its disproof available in-world but never delivered) becomes dead weight â€” the tracker retires it per the batch protocol. |
| **4. RECONTEXTUALIZATION** | A beat â€” often after the reveal, sometimes just before â€” that reframes the earlier clues so reread pays. The reveal answers the question; recontextualization changes what the *earlier* chapters meant. | **Must be planned before the reveal it serves** (Â§3, rule 3). A recontextualization improvised after the reveal is commentary; a planned one is architecture. It may itself be the setup for a deeper mystery (pipelining: 001's tether reveal recontextualizes the Laggard clues *and* sets up 002). |
| **5. REVEAL** | The answer lands â€” and pays at least the setup's accumulated weight. Per MYSTERY-003's canon rule: mysteries kept this long must pay off *upward*. A reveal that pays less than its carrying time cost the reader is a broken promise. | Gated by REVEAL_ORDER.md's phases and the L5 schedule. The reveal's arc is fixed by canon; the pipeline's job is to make the fixed date feel inevitable, not scheduled. |

### The nowhere test

A MAJOR reveal passes only if, on reread, the reader can find **at least two prior traces â€” a setup and a reinforcement â€” in distinct arcs before the reveal arc**. If the reveal's only prior trace sits in its own arc, it appeared from nowhere: **FLAG** the plan and push the setup back. The test is run by the consistency worker at batch step 4 (CHAPTER_MYSTERY_TRACKER.md Â§4). PARTIAL reveals are held to a lighter version (one trace); FINAL reveals to the full version â€” the deeper the answer, the longer the chain must be.

---

## Â§2 â€” THE TRACKER TABLE (all 38 canon chains)

`Target` = reveal stage/phase per REVEAL_ORDER.md. `Setup â†’ reinforcement` = arc windows (Arcs: I ~1â€“80 Â· II ~80â€“180 Â· III ~150â€“250 Â· IV ~250â€“350 Â· V ~280â€“380 Â· VI ~300â€“400 Â· VII ~330â€“450 Â· VIII ~400â€“500 Â· IX ~400â€“500 Â· X ~450â€“550 Â· XI ~500â€“600 Â· XII ~550â€“700). `Misdirection` = registered herrings/misdirections or record-listed herrings. `Recontext` = the planned reframing beat. Stageâ‚€ = UNPLANTED for all (series-start plan).

### Core cluster (001â€“015)

| M | Target reveal | Setup â†’ reinforcement (arcs) | Misdirection pairing | Recontextualization plan |
|---|---|---|---|---|
| 001 | P2 MAJOR (tether, ch. 150â€“250) | SETUP I (the 3s lag, ch. 1; observables ch. 1â€“20) â†’ REINF Iâ€“II (ratchet ch. 30â€“60; filed vector + examiner's dodge ch. 40â€“80; journals via Pram II) | RH-001â€“009 (the 12 misunderstandings); M-01 (Vector measures output); M-02 (the two rival schools) | The tether reveal reframes every prior clue as tether-physics; the filing system's blindness becomes the point |
| 002 | P4 FINAL (the hinge, ch. 400+) | SETUP I (dark-water dreams, ch. 10â€“20) â†’ REINF II (Crane's warning ch. 80â€“120), IIIâ€“IV (orientation shifts), IVâ€“VI (Shirakawa's impressions ch. 200â€“300) | "god"/"machine" are UNREGISTERED â€” texture only; L5-2 must never be staged as either | The hinge reframes the dreams as direction-with-possible-intent; puts L5-3 under pressure |
| 003 | P3 MAJOR (auction announced ch. 250â€“350); P4 FINAL (page surfaces ch. 350â€“450) | SETUP II (torn binding, margin notes, date paradox ch. 60â€“100) â†’ REINF III (handwriting/dating check ch. 200â€“300), IV (three-faction bidding, CG-048 ch. 250â€“350) | RH-010â€“014 (faked death; Choir; destroyed page; protect-Arthur; prophecy) | The page's content reframes the ratchet as a *deadline*; the bidding reframes as tragedy |
| 004 | P2 PARTIAL (Surabaya 1993, ch. 150â€“200); P3 PARTIAL (counterparty ch. 300â€“400); P4 FINAL | SETUP II (journals end Oct 1996 / logbook begins Nov 1996) â†’ REINF III (Surabaya 1993 entry, the transfer rule), VI (Ledger's 1996 paper) | RH-010/011; the missing Seep and 1996 bell staged as the Kota Tua cluster, not separate reveals | The deal's nature reframes Ilsa victimâ†’actor; her unfinished business becomes a present claim on Arthur |
| 005 | P3 MAJOR (redaction breaks ch. 250â€“350) | SETUP Iâ€“II (flagged file, redacted signature, CORP-011 doctrine ch. 40â€“80) â†’ REINF III (HR screener remembers the call ch. 120â€“180) | RH-015â€“017 (grades; Night Clerks; mother) | The approver's reason reframes Arthur's "luck" as *management* â€” every ally reprices |
| 006 | P2 surface (inquiry ch. 100â€“150); P3 MAJOR (Nagisa Collection ch. 280â€“380); P3 FINAL (merges w/ 010) | SETUP IIâ€“III (inquiry string, filed-vector language) â†’ REINF III (three cutouts, Nagisa ledger, gala question, Desk's watch-not-act ch. 120â€“250) | RH-018/019 (Choir; Vesper); "Factor invented it" is UNREGISTERED â€” texture only | Arthur attends his own auction: reframes him from person to *lot*; the appraisal as proof |
| 007 | P2 MAJOR (note reaches Arthur; grammar flip ch. 150â€“200) | SETUP II (counseling note, filed and ignored ch. 80â€“120) â†’ REINF VI+ (second diver corroborates, independent, ch. 300+) | RH-020/021 (his own Drowning; Erosion metaphor) | The grammar flip â€” *he* is someone's shadow â€” reframes the note from poetry to geometry |
| 008 | P2 seed (thin file ch. 60â€“100); P3 MAJOR (recruitment pitch ch. 300â€“400) | SETUP II (thin file, Aisha's unfiled follow-ups) â†’ REINF III (compromise visible ch. 150â€“220), VI (escrow failure models ch. 300â€“400) | RH-022â€“024 (ignorance; raid; handler); M-03 (thinness as camouflage) | The pitch reframes every prior "luck" as management; the escrow test as the arc hinge |
| 009 | P2 PARTIAL (second request ch. 150â€“220); P3 PARTIAL (margin-sketch file); P4 MAJOR (confirm/deny ch. 350+) | SETUP II (two requests; the B2â€“B3 basement) â†’ REINF III (the Archivists audit, don't browse), IIIâ€“IV (Javanese figure, Passchendaele nurse ch. 150â€“220) | RH-025 (they want *his* files); M-04 (pre-1980/Quiet Night cover) | Confirmation reframes the Laggard from anomaly to *institution* â€” centuries-circled, never caught |
| 010 | P2 seed (gala question ch. 120â€“180); P3 MAJOR (Court's offer ch. 300â€“400, merges w/ 006) | SETUP III (gala question, Loud-line doctrine) â†’ REINF IV (demographers' flag: two Louds, one desk ch. 200â€“280), VI (Eleanor's silences) | RH-026/027 (secret bloodline â€” CANON-FORBIDDEN; the Court wants the line) | The Court confronting its wrong theory reframes the bloodline cosmology as institutional critique |
| 011 | P2â€“III surface (leak breaks ch. 150â€“220); P3 PARTIAL (serials reconstructed ch. 220â€“300); P3 FINAL (sender ch. 350â€“450) | SETUP III (the cache; filed-off serials; June's verification) â†’ REINF IVâ€“V (serials point at Ravenhurst) | RH-028/029 (the Factor; fake cache) | The sender's motive reframes the leak from journalism to factional play; Nadia's catastrophe |
| 012 | P2 PARTIAL (manual's revision history ch. 150â€“220); P3 MAJOR (leak breaks; she learns ch. 220â€“300) | SETUP II (softened filings; the Tuesday problem ch. 60â€“110) â†’ REINF III (the manual), IV (analytics flags) | RH-030/031 (plant; Loud) â€” both load-bearing for the romance; never staged cheaply | The routine's authorship reframes the pipeline's editing as *policy*; Arthur's archive becomes the only unedited record |
| 013 | P2 PARTIAL (Ilsa's journal entry ch. 150â€“220); P3 MAJOR (tripwire: someone mentions the mirror ch. 300â€“400); P4 FINAL (merges w/ 002) | SETUP I (no-mirrors-after-midnight rule; two sightings ch. 20â€“40) â†’ REINF III (Ilsa's documentation, thirty years apart) | RH-032 (tired eyes); "entity mocking him" is UNREGISTERED â€” texture only, the most dangerous reading | The tripwire reframes the secrecy rule as compromised: the one thing he wouldn't write down, read back to him |
| 014 | P2 seed (blank plaque ch. 100â€“150); P3 PARTIAL (Rememberers' elders ch. 200â€“280); P4 MAJOR/FINAL (paper trail; survivors ch. 350â€“450) | SETUP IIâ€“III (plaque â€” monumental negative; the number; 1979 Protocols) â†’ REINF IV (elders: "the taken") | RH-033 (Sorensen's personal crime); "all executed" is UNREGISTERED â€” the truth must be *worse* | The survivors reframe the masquerade's original sin as a present-tense debt |
| 015 | P2 seed (Nwosu's data reaches Arthur ch. 200â€“300); P4 FINAL (driver shown or shown-unshowable ch. 450+) | SETUP I (tripling since 2000; Jan 2024 peak; 14th-c. High Tide) â†’ REINF IIâ€“III (2020 dip-and-rebound), IVâ€“V (Nwosu's paper; Shirakawa's impressions ch. 200â€“300) | L3 cosmologies â€” respected for praxis, doubted for cosmology; NEVER staged as herrings (RED_HERRINGS.md: "Being wrong has never stopped anyone from being effective") | The driver's showing (or shown-unshowable) reframes the entire setting; L5-3 stands or falls here |

### A/B majors (016â€“038)

| M | Target reveal | Setup â†’ reinforcement (arcs) | Misdirection pairing | Recontextualization plan |
|---|---|---|---|---|
| 016 | P4 MAJOR (ch. 300â€“400) | SETUP III (the heartbeat ch. 120â€“180) â†’ REINF: missing examiner's report (negative), Choir's unofficial pilgrimage | "T5's lair"; "the heartbeat is mechanical" | The patient's identity reframes the Choir's quiet infrastructure; a 26-year sealed room may open |
| 017 | P4 MAJOR (ch. 400+) | SETUP IIIâ€“IV (redrawing maps ch. 200â€“300) â†’ REINF: Exchange's silent recruitment; Choir's avoidance (behavioral negative) | "T5+"; "it's the Tide's source" â€” L5-1 GUARD: keep the well *adjacent* to the driver, never identical | The well's nature reframes cartography itself; staged *after* 015's partial |
| 018 | P4 MAJOR (ch. 350+) | SETUP III (unasked answers ch. 150â€“220) â†’ REINF: liturgical curation language; Veil-immunity (unique) | "The Archivists are feeding it" (mundane reading stays live until disproven) | An unasked answer addressing Arthur *by name* reframes the information infrastructure as inhabited |
| 019 | P4 MAJOR (ch. 350+) | SETUP III (1976 task force's "no fraud" ch. 150â€“220) â†’ REINF: hymn-tide method; three named Drownings | "Latent Attunement"; "coincidence" (task force ruled it out) | A modern preacher singing again reframes the Compact's instrument-epistemology; loads 027 |
| 020 | P2 MAJOR (examiner identified ch. 200â€“300) | SETUP Iâ€“II (the examination exists ch. 40â€“80) â†’ REINF: the seam â€” Arthur told nobody | "Arthur slipped and told someone" (contradicted by canon â€” the seam is real) | The method reframes the archive-omniscience question: specific and limited, never "the system sees everything" |
| 021 | P4 MAJOR (ch. 300+) | SETUP III (no Seep at Kota Tua â€” negative ch. 150â€“200) â†’ REINF: 03.1's usual pattern; a comparison case | "She didn't Drown" (the tether's survival already addresses this separately) | If the tether eats Drownings, the entity gains feeding behavior â€” L5-3 under pressure from a new direction |
| 022 | P4 MAJOR (response pattern ch. 300â€“400) | SETUP IIâ€“III (2017 single-site ringing ch. 100â€“150) â†’ REINF: 1996 ringing; the other ringings | "The Bell rang *for* Arthur" (anthropomorphizing an instrument) | The mapped pattern reframes the Bell as a tether-detector; every future transfer becomes visible |
| 023 | P4 MAJOR (ch. 450+) | SETUP IIIâ€“IV (dormancy's uniqueness ch. 200â€“300) â†’ REINF: no institutional response (pre-Compact); 118-year duration | RH-034/035 (burned out; the Compact stopped it) | Dormancy's mechanism â€” or its end â€” reframes the T5 threat model; may vindicate the Garden |
| 024 | P4 MAJOR (criteria ch. 400+) | SETUP III (the designation exists ch. 150â€“220) â†’ REINF: no documentation; what's at the top of T5 | "Clerical error" (UNREGISTERED â€” the mundane reading stays live); "T7 = the Tide" â€” L5-1 GUARD | The criteria's wording names the endgame scale; whoever wrote it had a *specific* fear |
| 025 | P4 MAJOR (ch. 400+) | SETUP IIIâ€“IV (survey data ch. 200â€“300) â†’ REINF: the naming (whose idiom?); the depth | "Natural formation" (trust the surveyors until given reason not to) | A second survey or dive reframes deep-sea Tide cosmology; stage carefully vs 017/015 |
| 026 | P3 PARTIAL (data reaches Arthur ch. 200â€“300); P4 MAJOR (suppressor ch. 350â€“450) | SETUP III (the thesis ch. 150â€“220) â†’ REINF IIIâ€“IV (raw data's survival) | RH-036 (the paper was wrong â€” suppression is for *dangerous* papers) | The suppression's *motive* reframes the paper as the smaller mystery; loads L5-4 |
| 027 | P4 MAJOR (ch. 450+) | SETUP IV (Arthur connects 2018 data to 1977 scale ch. 250â€“350) â†’ REINF: the Compact's modeling refusal (behavioral negative) | "The Compact knows and is hiding it" (UNREGISTERED â€” refusal may be epistemic caution, not conspiracy) | A "yes" reframes the masquerade as *causally implicated* in the High Tide â€” the series' sharpest turn |
| 028 | P4 MAJOR (collation ch. 350+) | SETUP I (the 70% figure ch. 1+) â†’ REINF IIIâ€“VII (margin phenomena: preacher, unasked answers, impossible impressions) | "The 30% is noise" / "the 30% is the adversary" (UNREGISTERED â€” never resolve by assertion) | The collation â€” by Arthur, the clerk â€” reframes the series' epistemic frame; resolves only with L5-3 |
| 029 | P4 MAJOR (oldest ledger read ch. 300â€“400) | SETUP I (ledgers' age ch. 100â€“150) â†’ REINF: the burial-society theory | "Always been an insurer" (the ledgers predate the industry) | The original purpose reframes the pipeline's editing (012) as historical motive |
| 030 | P4 MAJOR (ch. 350â€“450) | SETUP IIâ€“III (protocol's ninth-shaped hole ch. 100â€“150) â†’ REINF: the eight sites' geography | "There is no ninth site" (the protocol disagrees) | The ninth site's location â€” or its explained absence â€” completes the Bell's function (022) |
| 031 | P4 MAJOR (ch. 400+) | SETUP III (the Ledger's name ch. 150â€“220) â†’ REINF: the succession's invisibility | "No succession â€” it's immortal" (institutions aren't; the Ledger exists because someone dies) | The succession reframes every deal the Exchange ever brokered |
| 032 | P4 MAJOR (terminus ch. 350â€“450) | SETUP III (ban text + mandatory revision ch. 120â€“180) â†’ REINF: the pipeline's route; the 1977 coincidence | "Just a drug trade" (the revision suggests institutional stakes) | The terminus gives the 1977 cluster (Long Quiet, internment, ban) its material link |
| 033 | P4 MAJOR (ch. 400+) | SETUP III (doctrine + efficacy ch. 120â€“180) â†’ REINF: the Root's secrecy; the Ravenhurst notice (EVENT-095) | "The Root is a T5"; "the Garden is passive" (the notice proves attention) | The Root reframes stillness as the series' best answer to the Tide â€” horticultural eschatology |
| 034 | P4 MAJOR (ch. 400+) | SETUP IIIâ€“IV (charter's gaps ch. 200â€“300) â†’ REINF: three-government custody pattern | "The pages are ceremonial" (governments don't split custody of ceremony three ways) | A surfaced page renegotiates the Compact's legitimacy; 014 may be *in* the missing pages |
| 035 | P4 MAJOR (ch. 350â€“450) | SETUP III (three-desk contest ch. 150â€“220) â†’ REINF: 77 years un-declassified | "About war crimes" (the desks involved will tell) | The file's contents reframe pre-Compact history; may intersect 034 |
| 036 | P4 MAJOR (ch. 400+) | SETUP IIIâ€“IV (protocol's text ch. 200â€“300) â†’ REINF: non-use in living memory (or unrecorded use) | "Dead letter" (dead letters don't stay current â€” check revision dates) | Invocation reframes the Compact as escapable; Arthur's endgame gains a formal path |
| 037 | P4 MAJOR (ch. 350â€“450) | SETUP III (Sarr's actions ch. 150â€“220) â†’ REINF: the succession mechanism | "Sarr lost faith" (doubt isn't loss â€” a doubting head who *stays* is more dangerous) | The succession or schism reframes the Choir's folk-vs-theology tension |
| 038 | P4 MAJOR (ch. 400+) | SETUP III (suppressed hymns ch. 150â€“220) â†’ REINF: the cantors' denial (what exactly is denied?) | "Just a metaphor" (heresies aren't suppressed for metaphors) | The tenth bell reframes the Bell's mechanics (022/030) and the Choir's counting |

**MYSTERY-103â€“105 (C-draft additions).** FORESHADOWING.md predates these three; no canon clue chains are staged for them. Their foreshadowing is `TBD-per-plan`: when the Chapter Engine schedules them, it builds chains from their records' KNOWN CLUES (103: the capacity table, the unasked question; 104: the hygiene doctrine, the salted corpora; 105: EVENT-084's auctioned Rule, the premium mechanism) and runs the nowhere test before their reveals. No chain is invented here.

---

## Â§3 â€” PIPEmessaging app RULES

1. **Not every mystery needs all five stages.** Minors may run SETUP â†’ REVEAL, or even a single planted question with a quiet answer. The full pipeline is for staged majors. Skipping stages is a planning decision, logged in the tracker â€” never drift.
2. **Major reveals REQUIRE at least setup + reinforcement.** This is the nowhere test's floor (Â§1). A major reveal with only one prior trace is re-staged or re-arced.
3. **Recontextualization beats must be planned before the reveal they serve.** The tracker records the planned recontext beat at the same time the reveal is scheduled â€” if the reveal moves arcs, the recontext beat moves with it.
4. **Misdirection uses only registered material.** Staged misdirection draws from RED_HERRINGS.md's registered herrings (RH-001â€“036) and structural misdirections (M-01â€“06), or from a mystery record's own listed herrings. The 7 unregistered candidates are texture â€” the novel may *mention* them, never *stage* them. A plan that stages an unregistered candidate as misdirection is FLAGged at batch step 9.
5. **Pipelining is encouraged.** A reveal may double as the next mystery's setup (001's tether reveal â†’ 002's entity question; 013's tripwire â†’ 002's hinge). The tracker marks pipelined beats in both chains so the batch protocol never retires a clue that is still load-bearing downstream.
6. **Herring retirement is scheduled.** Every staged herring carries its disproof's in-world availability date. When the disproof becomes available, the batch protocol weakens the herring; when delivered, it retires it from the FALSE BELIEFS ledger. A herring with no scheduled disproof is not staged â€” it is parked as texture.
7. **The L5 cap binds the pipeline.** No chain may carry a protected truth (L5-1â€“L5-5) to REVEAL except through its canon resolution condition at its canon window (REVEAL_ORDER.md's L5 protection schedule). Chains may deepen L5-adjacent SUSPECTS indefinitely; the truth column does not move by pipeline pressure. The tripwire (CHAPTER_MYSTERY_TRACKER.md Â§3) fires on any plan that would.
8. **Weak-clue repairs are preserved.** FORESHADOWING.md's six strengthened clues (W-01â€“W-06: the examiner's dodge mechanism; the redaction's consistency; the dormancy as thesis; the Choir's avoidance; the buyer's documentary source; the 2018 sweep's negative) are load-bearing as staged. Plans must not revert them to their weak forms.

---

*End of CHAPTER_FORESHADOWING_TRACKER.md â€” Chapter Engine, tracking systems.*


---

## SECTION: `DATABASE/CHAPTER_HOOK_SYSTEM.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `DATABASE/CHAPTER_HOOK_SYSTEM.md` Â· sha256 `fcff972ff34208dd0d58fef603d82657370a569a1e0edb4272ad4a5dba6ea0d2` Â· 3,566 words. No content changed.

# CHAPTER HOOK SYSTEM â€” THE QUIET TIDE

> Phase 9 â€” Chapter Engine Architecture. Canon build: FINAL_WORLD_BIBLE v1.9 (2026-09-20).
> Scope: the SUBSYSTEM governing how chapters end and what pulls the reader into the next chapter. This file defines ending classes, hook types, and control rules. It contains NO chapters, NO prose, NO dialogue, NO chapter titles, and invents NO new lore. All canon references are by ID and file name.

---

## Â§1. Doctrine: the ending's job

The ending of a chapter has exactly one job: **to create a reason to continue reading.** Shock is one way to do that; it is not the only way, and in this series it is often the wrong way.

THE QUIET TIDE is a mystery-driven serial about an ordinary clerk whose power is subtle and informational (29_PROTAGONIST_ANOMALY.md; POWER_PROGRESSION.md), whose questions are architectural (105 mysteries, MYSTERIES.md; staged through REVEAL_ORDER.md), and whose central questions are *what does it cost to know things*, *who is the archive for*, and *what does presence obligate* (STORY_ENGINE.md Â§2). The serial's fuel is question-debt and priced knowledge, not adrenaline. An ending system built for this novel must therefore treat the *unanswered question*, the *repriced relationship*, and the *documented cost* as first-class engines of continuation â€” equal in status to danger.

**The anti-mandate:** no chapter is required to end on a cliffhanger. A chapter may end CLOSED (Â§17) â€” a small, complete satisfaction â€” or TRANSITION â€” a quiet relocation â€” and these endings are not weaker versions of cliffhangers; they are load-bearing. The 10-checkpoint pacing model (LONG_SERIAL_STRUCTURE.md Â§1â€“Â§2) already runs the serial on ~30 budgeted major reveals across ~1,000 chapters; cliffhangers are the *exception* structure, and the serial's sustainability depends on the rule, not the exceptions.

**Three principles govern the whole subsystem:**

1. **Tension must be earned by the chapter's systems, never manufactured by its ending.** If the tension exists only because the ending withholds information the POV character already has, or stages a danger no system in the chapter supports, the ending is artificial (Â§4, detection test).
2. **Every ending is priced against the canon pacing budget.** Major revelations have protection windows (REVEAL_ORDER.md: L5 schedule; the ~1-per-25/40 rule, STORY_ENGINE.md Â§5); faction peaks never double-crest at adjacent checkpoints (ARC_ARCHITECTURE.md Â§13.3); open-thread debt is capped at â‰¤2 new threads per arc (STORY_ENGINE.md Â§5). An ending that promises beyond what these budgets allow is a lie the arc architecture cannot pay.
3. **Hooks serve the reader-lead rule, never collapse it.** The reader may lead Arthur by at most one phase (STORY_ENGINE.md Â§10), except the two deliberate ironies (SECRET-007, SECRET-015). A hook may *use* the gap between what the reader knows and what Arthur knows â€” it must never accidentally close it (Â§6).

---

## Â§2. The ten hook types

A hook type is a *mechanism*: what reader-state it produces, and where in this series it is appropriate or inappropriate. Appropriateness is judged against locked canon â€” Arthur's subtle informational ability, the 28/28 faction autonomy verdicts (FACTIONS_AND_CONFLICTS.md; STORY_ENGINE.md Â§10), the cost-of-knowing theme, and the reveal budget.

1. **QUESTION hook.** *Produces:* an open interrogative in the reader's mind ("what was on the torn page?"). *Appropriate:* at any time â€” this is the native hook of a mystery serial; every arc runs on â‰¤2 new open threads (STORY_ENGINE.md Â§5), and QUESTION hooks are the micro-form of that debt. *Inappropriate:* when the question asked is a protected UNKNOWN (REVEAL_ORDER.md: L5 protection schedule) or an ENDGAME UNKNOWN that must stay unresolvable-by-design (STORY_ENGINE.md Â§9) â€” a QUESTION hook pointed at L5-3 ("does the Undertow want anything?") *promises an answer the canon forbids*, violating Â§6's hook-to-arc-checkpoint consistency.
2. **DANGER hook.** *Produces:* immediate physical or institutional threat-state ("the Sweeper team has his address"). *Appropriate:* sparingly, in arcs whose kind is adversarial (ARC II's provenance contest, ARC VI's golden handcuffs) and at canon checkpoint PEAKs (ARC_ARCHITECTURE.md Â§13.3). *Inappropriate:* as a substitute for a question the chapter failed to earn; and *never* as Arthur's own combat action â€” his synergy is informational, never combat (STORY_ENGINE.md Â§4), and a DANGER hook centered on him fighting contradicts the canon's genuine-powerlessness conditions. Danger may arrive *at* him; it must never be solved *by* him through means he does not possess.
3. **DISCOVERY hook.** *Produces:* the reader learns a concrete fact and must recalculate ("the journal has a second hand"). *Appropriate:* at reveal-order windows; discovery is the clerk's method made narrative â€” appraisal, collation, authentication, testing (STORY_ENGINE.md Â§5). *Inappropriate:* when the discovery is a major reveal outside its budgeted window (REVEAL_ORDER.md arc-level pacing rules) or when it resolves a mystery a protected schedule reserves â€” a discovery hook must check the dependency graph (MYSTERY_DEPENDENCIES.md) before firing.
4. **EMOTIONAL hook.** *Produces:* relational pressure â€” a dinner silence, an unanswered telling, a debt of presence ("Eleanor kept the seat anyway"). *Appropriate:* as the primary hook engine of the ordinary-life system (STORY_ENGINE.md Â§4) and the romance configurations (ROMANCE_ARCHITECTURE.md); the dinner rule is explicitly "commitment technology," and its hooks carry more long-term force than most DANGER hooks. *Inappropriate:* when used to manufacture melodrama over a relationship whose evidence is not yet gated â€” romance beats land only after their evidence exists (STORY_ENGINE.md Â§7), so an EMOTIONAL hook cannot leapfrog reveal-order gating.
5. **INFORMATION hook.** *Produces:* knowledge-as-cost â€” the reader understands that someone now knows something expensive ("SaitÅ wrote down the wrong file's number"). *Appropriate:* constantly; this is the series' thematic engine ("what does it cost to know things?" â€” STORY_ENGINE.md Â§2). INFORMATION hooks pair naturally with CONSEQUENCE endings (Â§17). *Inappropriate:* when the knowledge implies Arthur is becoming omniscient â€” the ordinary-life engine's information-bottleneck function (STORY_ENGINE.md Â§4: he knows only what the records room, Loud recall, and the wrong file provide) must hold at every ending. A hook that suggests he now "knows everything" is canon-violating.
6. **ANOMALY hook.** *Produces:* phenomenological wrongness â€” the shadow leaned, the bell rang with no wind. *Appropriate:* as texture and early-warning; Arthur's ability is subtle and informational, so ANOMALY hooks must read as *observations of rules*, never as spectacle ("the lag ran seven seconds long" â€” a measurement, not a lightning bolt). *Inappropriate:* when the anomaly implies a new power stage â€” power stages are budgeted at 7 across ~700 chapters with brakes on every rung (POWER_PROGRESSION.md; STORY_ENGINE.md Â§10: the 16-item no-shortcut list). An anomaly hook must never read as "he leveled up."
7. **FACTION hook.** *Produces:* institutional motion â€” someone filed something, someone's invoice moved ("the Cartographers bought the pier's debt"). *Appropriate:* at faction-checkpoint crests (ARC_ARCHITECTURE.md Â§13.3), where interleave systems are ACTIVE or PEAK; this is how the 102 generators surface at chapter scale. *Inappropriate:* when it violates 28/28 faction autonomy â€” a faction hook must show the faction acting on *its own* logic, with Arthur entering the conflict, never generating it (STORY_ENGINE.md Â§6). A hook that centers "what will Arthur do about the Faction's plan" collapses the autonomy the canon requires; the hook must center "what the faction's plan costs the people it touches," with Arthur as one of those people.
8. **CHARACTER hook.** *Produces:* a person changed in the reader's estimation â€” a new alignment revealed, a mask dropped ("Okada's scheduling note had a second meaning"). *Appropriate:* after that character's evidence exists; the canon carries 414 IDs with staged trajectories (CHARACTERS.md; ARC_ARCHITECTURE.md Â§13.1). *Inappropriate:* as a shortcut for a reveal that belongs to collation â€” character hooks that "reveal" a person without the clerk's method doing the work read as authorial fiat. Only a holder can authenticate (STORY_ENGINE.md Â§5).
9. **REVERSAL hook.** *Produces:* the frame breaks â€” what the chapter established was read from the wrong side ("the lean points at pressure, not safety"). *Appropriate:* rarely, at midpoints and arc climaxes, where ARC_ARCHITECTURE.md's per-arc structure already stages a midpoint reversal or climax; reversals are how arcs turn, so they belong to arc-turning chapters. *Inappropriate:* stacked â€” two REVERSAL hooks in sequence destroy both, and a reversal outside the arc's turn structure is a trick, not architecture. Reversal hooks are rationed under the same logic as Â§4's THREAT/REVERSAL rationing.
10. **CONSEQUENCE hook.** *Produces:* the invoice arrives â€” a choice made chapters ago is priced ("the escrow's ~30% failure rate just failed on *him*"). *Appropriate:* as the long-serial's memory â€” CONSEQUENCE hooks are how a ~1,000-chapter serial stays coherent; they reward the reader who remembers. They are the natural pairing for arcs about guilt economies and responsibility (ARCs IVâ€“VI; STORY_ENGINE.md Â§3). *Inappropriate:* when the consequence arrives without its cause having been established in text â€” a consequence without a visible prior choice is a punishment without a crime, and the reader reads it as the author's cruelty rather than the world's logic.

---

## Â§3. The nine ending classes

An ending class is the chapter's terminal *shape*. The batch protocol (Â§5) reads classes, not hooks; a chapter may combine hook types, but it ends in one class.

1. **OPEN.** The chapter ends mid-motion â€” a door opening, a file requested, a walk begun. The work continues; the reader's reason to continue is *momentum*. Natural hook pairings: QUESTION, DISCOVERY (the file arrives next chapter). OPEN is the series' default workhorse and must never be mistaken for a cliffhanger: OPEN manufactures motion, not peril.
2. **CLOSED.** The chapter completes a small unit of work â€” a form filed, a meal finished, a fact verified. The reader's reason to continue is *satisfaction and trust*: the serial keeps its promises, so the next chapter's promise is worth reading. Natural hook pairings: EMOTIONAL (quiet), INFORMATION (a cost tallied). CLOSED endings are legitimate and necessary (see Â§4): they are the breathing room that lets major revelations land.
3. **QUESTION.** The chapter ends on a stated or implied interrogative it does not answer. The reason to continue is *the debt*. Natural hook pairings: QUESTION (native), ANOMALY (the phenomenon asks). QUESTION endings spend question-debt: they are only legal where the debt cap (â‰¤2 new open threads/arc) has headroom and the L5 protection schedule (REVEAL_ORDER.md) is respected.
4. **DISCOVERY.** The chapter ends with a new fact the reader must recalculate around. The reason to continue is *reappraisal*. Natural hook pairings: DISCOVERY (native), CHARACTER (the fact is a person). DISCOVERY endings are the reveal mechanism's terminal shape (STORY_ENGINE.md Â§5: appraisal/collation/authentication/testing); each one must be checked against the reveal budget and the faction-repricing rule (every major reveal reprices â‰¥2 factions â€” REVEAL_ORDER.md arc-level rules).
5. **THREAT.** The chapter ends with danger imminent or newly priced. The reason to continue is *survival concern*. Natural hook pairings: DANGER (native), FACTION (the threat is institutional), CONSEQUENCE (the invoice is a threat). THREAT endings are RATIONED (Â§4): they are the currency of cliffhangers, and overprinting devalues every other class.
6. **EMOTIONAL.** The chapter ends on relational weight â€” a silence kept, a seat taken, a telling withheld or given. The reason to continue is *attachment*. Natural hook pairings: EMOTIONAL (native), CONSEQUENCE (the emotional invoice). The ordinary-life engine (STORY_ENGINE.md Â§4) is this class's natural home; the dinner rule's every-other-Sunday beat is designed to produce EMOTIONAL endings that carry more force than a threat.
7. **REVERSAL.** The chapter ends by breaking its own frame. The reason to continue is *disorientation that demands re-reading*. Natural hook pairings: REVERSAL (native), INFORMATION (the fact that breaks the frame). RATIONED alongside THREAT (Â§4): a reversal that does not correspond to an arc-level turn is a gimmick, and stacked reversals cancel each other.
8. **CONSEQUENCE.** The chapter ends with an invoice presented â€” a past choice priced, a debt called, a ratchet fraction taken. The reason to continue is *reckoning*. Natural hook pairings: CONSEQUENCE (native), FACTION (the invoicing institution), INFORMATION (the cost made legible). This class is the cost-of-knowing theme's terminal form; it is how the serial demonstrates that knowledge is never free (STORY_ENGINE.md Â§2).
9. **TRANSITION.** The chapter ends by relocating â€” scene, system, register, or time ("three streets over," "two weeks later"). The reason to continue is *orientation curiosity*. Natural hook pairings: OPEN, FACTION (the interleave map moves â€” ARC_ARCHITECTURE.md Â§13.3's PEAK/ACTIVE cells are chapter-scale transitions). TRANSITION endings are legitimate and necessary: they move the serial between Arthur's story and the 12 faction systems without requiring his presence, preserving the 28/28 autonomy verdicts.

---

## Â§4. Cliffhanger control

**The rule:** *a cliffhanger every chapter destroys impact.* This is not taste; it is arithmetic. The serial budgets ~30 major reveals across ~1,000 chapters (LONG_SERIAL_STRUCTURE.md Â§1). If THREAT and REVERSAL endings â€” the classes that carry shock â€” are not rationed, three things fail: (1) the reveal budget collapses, because every chapter promises what the arc cannot deliver; (2) the ordinary-life engine's rest function (STORY_ENGINE.md Â§4) cannot fire, because rest requires chapters that do not threaten; (3) the reader learns the cliffhanger is a reflex, and stops flinching. A reflex is not tension; it is punctuation the reader learns to skip.

**Operationalized distribution guidance (binding on the batch protocol):** THREAT and REVERSAL endings are *rationed classes*. Across any arc, THREAT endings cluster at the arc's own turn structure (opening disruption, midpoint reversal, climax â€” ARC_ARCHITECTURE.md's per-arc shape) and at faction-checkpoint PEAKs (ARC_ARCHITECTURE.md Â§13.3); outside those zones they are exceptional and must be justified in the batch audit. REVERSAL endings are rarer still: at most one per arc outside the endgame arcs (XIâ€“XII â€” ARC_ARCHITECTURE.md Â§14), because each arc has one true turn and every extra reversal is a lie about where the turn is. CLOSED and TRANSITION endings are *legitimate and necessary*, not failures: without CLOSED the serial has no trustworthy rhythm, and without TRANSITION the 12 Arthur-independent faction systems (STORY_ENGINE.md Â§6) cannot move without dragging him to every scene â€” the batch protocol must not flag them as weak. OPEN, QUESTION, DISCOVERY, EMOTIONAL, and CONSEQUENCE are the *load-bearing middle* â€” in a healthy arc these five classes constitute the majority of endings, carrying the mystery engine, the ordinary-life engine, and the cost-of-knowing theme chapter to chapter.

**The breathing-room rule (binding):** a major reveal (REVEAL_ORDER.md's staged majors; STORY_ENGINE.md Â§5's ~1/25 and ~1/40 cadence) must be followed by *processing space* â€” never stacked under another reveal, and never stacked under a THREAT or REVERSAL ending in the same batch neighborhood. The chapter after a major reveal should be CLOSED, EMOTIONAL, TRANSITION, or CONSEQUENCE â€” an ending that lets the reader *sit with* the fact â€” not another escalation. "Finales are earned by Arthur's action, never exposition" (STORY_ENGINE.md Â§5), and earning requires air. Stacking reveals is how serials train readers to skim: if everything is the biggest thing, nothing is.

**The artificial-cliffhanger detection test (binding, applied per chapter in batch audit):**

> Ask: *would this ending's tension survive if the POV character said out loud what he already knows?* If the tension exists only because the chapter withholds information Arthur already possesses â€” the classic "he knows the answer but doesn't think it" maneuver â€” the cliffhanger is artificial. Rewrite: either have him know it openly and derive the tension from what knowing *costs* (INFORMATION/CONSEQUENCE pairing), or derive the tension from what he genuinely does not know (QUESTION pairing). Withholding his own knowledge is never an ending; it is a postponement wearing a cliffhanger's clothes.

The test's second prong: *does any system in this chapter support the threat?* A THREAT ending is artificial if the danger is introduced only in the final beat with no faction, mystery, power, or ordinary-life system behind it. Arthur's visibility detonates pre-laid tripwires (STORY_ENGINE.md Â§6) â€” "pre-laid" is the operative word. A tripwire that was laid in the same paragraph it detonates is not pre-laid.

---

## Â§5. Variation enforcement

The batch protocol (the Chapter Engine's per-batch audit, 10-chapter batches) checks ending-class distribution. The rules:

1. **No more than 2 consecutive same-class endings (N = 2).** Reasoning: 1 consecutive is rhythm (two QUESTION endings in a row can be a deliberate interrogative run); 2 is a pattern the reader starts to anticipate, which is the maximum tolerable; 3 is a rut â€” the reader has learned the serial's move, and learning the serial's move is how surprise dies. The count resets at arc boundaries (a new arc may legitimately re-open with OPEN). *Exception:* TRANSITION endings may reach 3 consecutive in the Approach band (~700â€“1000+), where the 102 generators' convergence (LONG_SERIAL_STRUCTURE.md Â§3) legitimately requires multi-system relocation; this is the only exception and it must be flagged in the audit as Approach-band interleave.
2. **Rationed-class caps per 10-chapter batch:** THREAT â‰¤ 3, REVERSAL â‰¤ 1. A batch exceeding either is returned for rewrite â€” not because the chapters are bad, but because the batch's currency is debased. A batch with THREAT = 0 is *fine* (ordinary-life arcs legitimately run on EMOTIONAL/CLOSED), and the protocol must not treat a THREAT-free batch as a defect.
3. **Breathing-room audit:** for every major reveal in the batch (checked against REVEAL_ORDER.md's staged windows), the protocol verifies that the *following* chapter's ending class is one of CLOSED, EMOTIONAL, TRANSITION, or CONSEQUENCE. A reveal followed by THREAT/REVERSAL/QUESTION is flagged: QUESTION compounds the debt instead of letting it settle; THREAT/REVERSAL escalates past the reveal instead of honoring it.
4. **Pairing with the chapter-type palette.** The 11 chapter types defined in CHAPTER_ENGINE.md (the Chapter Engine's core document, Phase 9) carry their own narrative work; the ending class must be *compatible* with the chapter type, not redundant with it. A chapter whose type is already informational (e.g., a records-room collation chapter) should not end DISCOVERY unless the discovery exceeds the type's own work â€” otherwise the ending repeats the chapter. Conversely, a chapter whose type is ordinary-life (night-shift rest, convenience store break) ending THREAT is a register violation unless a canon checkpoint PEAK justifies it (ARC_ARCHITECTURE.md Â§13.3): the ordinary must be allowed to be ordinary, or the contrast function (STORY_ENGINE.md Â§4) dies. The general principle: **the ending class should complete the chapter type's arc of work, not echo it.**

---

## Â§6. Series-specific hook discipline

Three constraints, each binding on every chapter ending in every batch.

**1. Hooks must never promise what the arc architecture cannot deliver (hook-to-arc-checkpoint consistency).** Before a chapter ends on a hook, the hook's promise is checked against the arc's checkpoints: does the arc's remaining window contain the payoff? A QUESTION hook in ARC V pointing at the Compact's internment (ARC IX's truth commission) is legal â€” the spine has room. A DANGER hook promising a Bell eschaton beat in ARC II is not â€” the Theological War PEAKs at ~ch. 500 (ARC_ARCHITECTURE.md Â§13.3), and promising it 400 chapters early is a lie. Specific red lines: no hook may promise CG-052's redline being spent before the Approach band (ARC_ARCHITECTURE.md Â§13.1â€“13.2: activated in ARC XI, never spent there); no hook may promise the driver shown before ARC XI's window (REVEAL_ORDER.md: L5-1 earliest ch. 450+); no hook may touch the never-resolved list (STORY_ENGINE.md Â§9). The arc's kind also constrains the hook: an ARC I (authentication â€” private self-appraisal) chapter cannot end on a FACTION PEAK hook; the kind's register is private, and the hook must be too. When in doubt, the hook points at the arc's *own* checkpoint or the next one â€” never three checkpoints ahead.

**2. Hooks must not leak protected UNKNOWN mysteries (the protection protocol).** The L5 protection schedule (REVEAL_ORDER.md) and the ENDGAME UNKNOWN ledger (STORY_ENGINE.md Â§9) define what no ending may touch: 015's driver (L5-1, and 017/024 may not answer it by accident), 002's entity (L5-2, and 007/013 feed but never resolve), the margin (L5-3), 026/027's mechanism (L5-4, open even as the effect is used), 003's page (L5-5). "Leak" includes partial answers: a DISCOVERY ending that gives away half of L5-2's answer in ARC III is a leak, not a tease â€” REVEAL_ORDER.md's windows are *earliest* resolutions, and feeding is only legal through the designated feeders (007, 013 for L5-2; the scheduled majors for the rest). The batch protocol's protection check: for each DISCOVERY, QUESTION, and INFORMATION hook, name the mystery ID it touches; if the ID is on the protection schedule and the chapter is before its window, or on the ENDGAME UNKNOWN ledger at all, the hook is cut. MYSTERY-087/089 (SaitÅ's adjacency; the Tuesday mechanism) are staged-but-open (LONG_SERIAL_STRUCTURE.md Â§5): hooks may circle them â€” never land.

**3. The reader-lead rule applied to hooks (exploit the gap, never collapse it).** The reader may lead Arthur by at most one phase (STORY_ENGINE.md Â§10), except the two deliberate ironies (SECRET-007: the page is for sale while he hunts it; SECRET-015: the Court's error about the Reed line). Hooks *may* exploit this gap â€” the most powerful hook type in this series is the one the canon deliberately stages: the reader knows the inquiry's publication prices Arthur's head (CG-041's chain, ARC_ARCHITECTURE.md Â§13.2) while Arthur does not yet; a CONSEQUENCE or FACTION ending that lets the reader watch the invoice travel toward an unaware clerk is the reader-lead rule working as designed. What hooks must *never* do is collapse the gap accidentally: an ending that lets Arthur "figure out" what the reader knows â€” or an ending staged from the reader's knowledge that Arthur then acts on without the clerk's method earning it â€” violates both the reader-lead rule and the no-shortcut list (STORY_ENGINE.md Â§10: the 16 no-shortcut items). The audit question per chapter: *whose knowledge is this ending standing in?* If it stands in the reader's knowledge and hands it to Arthur, cut it. If it leaves Arthur unaware â€” staged dramatic irony, with the two ironies as the only standing exceptions â€” it is the series' sharpest tool: use it rarely, and on purpose.

---

*End of CHAPTER_HOOK_SYSTEM.md â€” Phase 9 subsystem, THE QUIET TIDE.*


---

## SECTION: `DATABASE/CHAPTER_MYSTERY_TRACKER.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `DATABASE/CHAPTER_MYSTERY_TRACKER.md` Â· sha256 `635860e403b69c6f6c7e42126c58446149c2971b39677c599417bc2ead9b972b` Â· 3,911 words. No content changed.

# DATABASE â€” CHAPTER MYSTERY TRACKER (Chapter Engine)

**THE QUIET TIDE v1.9** Â· Phase 9: Chapter Engine Architecture â€” TRACKING SYSTEMS
**Purpose:** the running ledger of all 105 mysteries. This file tracks *what is known, by whom, and what stage each mystery has reached*; INFORMATION_FLOW.md defines the states and the movement rules; CHAPTER_FORESHADOWING_TRACKER.md tracks the clue chains that move them.
**Canon anchors:** DATABASE/MYSTERIES.md (all records, the closed L5 set) Â· DATABASE/REVEAL_ORDER.md (staging vocabulary, phases, pacing rules) Â· DATABASE/MYSTERY_DEPENDENCIES.md (D-edges, C-collisions) Â· DATABASE/RED_HERRINGS.md (RH-001â€“036, M-01â€“06) Â· DATABASE/INFORMATION_KNOWLEDGE_MAP.md (SECRET-001â€“024, â—/â—/â—‹ values) Â· DATABASE/ARC_ARCHITECTURE.md (arc windows) Â· DATABASE/STORY_ENGINE.md (Â§8 phases/arcs, Â§10 inherited constraints).
**Not this file:** no chapters, no scenes, no prose. A starting ledger, not a chapter plan.

---

## Â§1 â€” TRACKER SCHEMA

One record per mystery. Fields:

| Field | Format |
|---|---|
| **MYSTERY ID** | MYSTERY-001â€¦105 (canon-final; draft temp IDs retired â€” concordance in MYSTERIES.md) |
| **LAYER** | The mystery's canon CATEGORY (what stratum of the world it lives in: anomaly / cosmological / historical / organizational / character / government / information / personal / technology / classification / economy / faction). For minors, the anchor-derived cluster, flagged `(a)` â€” assigned from the canon anchor's draft prefix (A = anomaly/history, B = faction/character, C = information-systems, H = history, P = personal, EVENT = event-led), provisional until the minor is promoted. |
| **MAJOR / MINOR** | MAJOR (full record, staged) or MINOR (one-line question with canon anchor; promotable only if the novel needs it) |
| **FIRST APPEARANCE** | Arc window from ARC_ARCHITECTURE.md (Arcs Iâ€“XII), mapped from the record's chapter staging; `TBD-per-plan` where canon stages none (all minors) |
| **CLUES** | The ledger of planted clues: each entry cites type (direct/indirect/behavioral/environmental/documentary/negative), planting beat, and current state (planted / reinforced / spent / disproved) |
| **ADDITIONAL CLUES** | Clues added by chapter plans after series start â€” never invented off-ledger; each addition is a deliberate information operation (INFORMATION_FLOW.md Â§2) |
| **RED HERRINGS** | Registered herrings (RH-### / M-## from RED_HERRINGS.md) attached to this mystery, with live/dead status per holder |
| **PARTIAL ANSWERS** | Truths established short of resolution, each cited to the beat that established them |
| **FALSE THEORIES** | In-world wrong theories currently held, with holder and confidence (feeds INFORMATION_FLOW.md's FALSE BELIEFS state) |
| **REVEAL STAGE** | Staging vocabulary from REVEAL_ORDER.md: `UNFILED` (not yet on the page) Â· `SURFACED` (the question is posed) Â· `SEEDED` (early partial/seed beat landed) Â· `PARTIAL` (some truth established) Â· `MAJOR` (the big reveal landed) Â· `FINAL` (resolved per its resolution condition) Â· `PROTECTED-L5` (cap â€” the closed set; see Â§3) Â· `ANSWERED-IN-CANON` |
| **CURRENT READER KNOWLEDGE** | â— knows Â· â— suspects/partial Â· â—‹ does not know (INFORMATION_KNOWLEDGE_MAP.md values) |
| **CURRENT ARTHUR KNOWLEDGE** | â— knows Â· â— suspects/partial Â· â—‹ does not know |
| **RESOLUTION STATUS** | OPEN Â· PARTIAL Â· INTENTIONAL MYSTERY (L5) Â· ANSWERED-IN-CANON â€” plus the provisional register where canon flags it (005's payoff-mandatory thread; 009's confirm-or-deny search; 008's live thread; 013's tripwire payoff) |

---

## Â§2 â€” THE FULL 105-MYSTERY LEDGER (series-start values)

Series start = chapter 1. Per REVEAL_ORDER.md P1, no L3+ truth exists yet; per INFORMATION_KNOWLEDGE_MAP.md, the reader leads Arthur by at most one phase. Initial values below are the ledger's opening position â€” the machine's zero state. `Stageâ‚€` = REVEAL STAGE at series start; `Râ‚€`/`Dâ‚€` = reader/Arthur knowledge at series start; `Statusâ‚€` = resolution status at series start. Arc windows: I ~1â€“80 Â· II ~80â€“180 Â· III ~150â€“250 Â· IV ~250â€“350 Â· V ~280â€“380 Â· VI ~300â€“400 Â· VII ~330â€“450 Â· VIII ~400â€“500 Â· IX ~400â€“500 Â· X ~450â€“550 Â· XI ~500â€“600 Â· XII ~550â€“700.

### MAJOR MYSTERIES (001â€“038, 103â€“105)

| ID | Layer | M | First appearance | Stageâ‚€ | Râ‚€ | Dâ‚€ | Statusâ‚€ |
|----|-------|---|------------------|--------|----|----|---------|
| 001 | anomaly | MAJOR | ARC I (ch. 1) | SURFACED | â— (sees the lag, no name) | â—‹ | PARTIAL |
| 002 | anomaly/cosmological | MAJOR | ARC I (dreams, ch. ~10â€“20) | SEEDED | â— (dreams) | â— (felt looked-at) | INTENTIONAL MYSTERY (L5-2) |
| 003 | historical/personal | MAJOR | ARC II (Pram, ch. ~60â€“100) | UNFILED | â—‹ | â—‹ | INTENTIONAL MYSTERY (L5-5) |
| 004 | historical | MAJOR | ARC II (ch. ~60â€“100) | UNFILED | â—‹ | â—‹ | OPEN |
| 005 | organizational/personal | MAJOR | ARC Iâ€“II (ch. ~40â€“80) | UNFILED | â— (flagged file seen) | â—‹ | OPEN (payoff mandatory per 33 Â§8) |
| 006 | organizational | MAJOR | ARC IIâ€“III (rumor, ch. ~100â€“150) | UNFILED | â—‹ | â—‹ | OPEN |
| 007 | anomaly | MAJOR | ARC II (ch. ~80â€“120) | UNFILED | â—‹ | â—‹ | OPEN |
| 008 | government | MAJOR | ARC II (thin file, ch. ~60â€“100) | UNFILED | â—‹ | â—‹ | OPEN (live thread) |
| 009 | organizational/historical | MAJOR | ARC II (ch. ~50â€“90) | UNFILED | â—‹ | â—‹ | OPEN (PROVISIONAL â€” confirm or deny) |
| 010 | character/faction | MAJOR | ARC III (ch. ~120â€“180) | UNFILED | â—‹ | â—‹ | OPEN |
| 011 | organizational | MAJOR | ARC III (ch. ~150â€“220) | UNFILED | â—‹ | â—‹ | OPEN |
| 012 | character/organizational | MAJOR | ARC II (ch. ~60â€“110) | UNFILED | â— (the softening) | â— | OPEN |
| 013 | personal/anomaly | MAJOR | ARC I (the rule, ch. ~20â€“40) | SEEDED | â— (the no-mirrors rule) | â— (his only secret) | OPEN (tripwire payoff) |
| 014 | historical/government | MAJOR | ARC IIâ€“III (ch. ~100â€“150) | UNFILED | â—‹ | â—‹ | OPEN |
| 015 | cosmological | MAJOR | ARC I (texture, ch. 1+) | SURFACED-as-texture | â— (the tripling as news) | â—‹ | INTENTIONAL MYSTERY (L5-1) |
| 016 | historical/anomaly | MAJOR | ARC III (ch. ~120â€“180) | UNFILED | â—‹ | â—‹ | OPEN |
| 017 | historical/cosmological | MAJOR | ARC IIIâ€“IV (ch. ~200â€“300) | UNFILED | â—‹ | â—‹ | OPEN |
| 018 | organizational/information | MAJOR | ARC III (ch. ~150â€“220) | UNFILED | â—‹ | â—‹ | OPEN |
| 019 | information/anomaly | MAJOR | ARC III (ch. ~150â€“220) | UNFILED | â—‹ | â—‹ | OPEN |
| 020 | anomaly/information | MAJOR | ARC Iâ€“II (ch. ~40â€“80) | UNFILED | â— (the examination exists) | â— | OPEN |
| 021 | anomaly/historical | MAJOR | ARC III (ch. ~150â€“200) | UNFILED | â—‹ | â—‹ | OPEN |
| 022 | anomaly/historical | MAJOR | ARC IIâ€“III (ch. ~100â€“150) | UNFILED | â—‹ | â—‹ | OPEN |
| 023 | historical/cosmological | MAJOR | ARC IIIâ€“IV (ch. ~200â€“300) | UNFILED | â—‹ | â—‹ | OPEN |
| 024 | classification/cosmological | MAJOR | ARC III (ch. ~150â€“220) | UNFILED | â—‹ | â—‹ | OPEN |
| 025 | anomaly/information | MAJOR | ARC IIIâ€“IV (ch. ~200â€“300) | UNFILED | â—‹ | â—‹ | OPEN |
| 026 | information/character | MAJOR | ARC III (ch. ~150â€“220) | UNFILED | â— (background texture) | â—‹ | PARTIAL (carries L5-4) |
| 027 | cosmological/information | MAJOR | ARC IV (ch. ~250â€“350) | UNFILED | â—‹ | â—‹ | OPEN (carries L5-4) |
| 028 | information/cosmological | MAJOR | ARC I (texture, ch. 1+) | SURFACED-as-texture | â— (the 70% figure) | â—‹ | OPEN (carries L5-3 hinge) |
| 029 | organizational/historical | MAJOR | ARC I (texture, ch. 1+) | SURFACED-as-texture | â— (ledgers' age, throwaway) | â— (phenomenon-level) | OPEN |
| 030 | anomaly/organizational | MAJOR | ARC IIâ€“III (ch. ~100â€“150) | UNFILED | â—‹ | â—‹ | OPEN |
| 031 | organizational/historical | MAJOR | ARC III (ch. ~150â€“220) | UNFILED | â—‹ | â—‹ | OPEN |
| 032 | organizational/government | MAJOR | ARC III (ch. ~120â€“180) | UNFILED | â—‹ | â—‹ | OPEN |
| 033 | organizational/anomaly | MAJOR | ARC III (ch. ~120â€“180) | UNFILED | â—‹ | â—‹ | OPEN |
| 034 | government/information | MAJOR | ARC IIIâ€“IV (ch. ~200â€“300) | UNFILED | â—‹ | â—‹ | OPEN |
| 035 | government/historical | MAJOR | ARC III (ch. ~150â€“220) | UNFILED | â—‹ | â—‹ | OPEN |
| 036 | government/information | MAJOR | ARC IIIâ€“IV (ch. ~200â€“300) | UNFILED | â—‹ | â—‹ | OPEN |
| 037 | organizational/character | MAJOR | ARC III (ch. ~150â€“220) | UNFILED | â—‹ | â—‹ | OPEN |
| 038 | organizational/anomaly | MAJOR | ARC III (ch. ~150â€“220) | UNFILED | â—‹ | â—‹ | OPEN |
| 103 | technology/information | MAJOR | ARC III (ch. ~150â€“220) | UNFILED | â—‹ | â—‹ | OPEN |
| 104 | technology/information | MAJOR | ARC IIIâ€“IV (ch. ~200â€“300) | UNFILED | â—‹ | â—‹ | OPEN |
| 105 | economy/information | MAJOR | ARC IIIâ€“IV (ch. ~200â€“300) | UNFILED | â—‹ | â—‹ | OPEN |

**Ledger notes (majors).** (a) 001's Dâ‚€ = â—‹ follows INFORMATION_KNOWLEDGE_MAP.md SECRET-001 P1 (he has the phenomenon, not the secret). (b) 002's Stageâ‚€ = SEEDED because the dark-water dreams are on the page from ch. ~10â€“20 as stress dreams â€” the question exists before it has a name. (c) 013's Dâ‚€ = â—: the mirror sightings are Arthur's only P1 secret (SECRET-005). (d) "SURFACED-as-texture" (015/028/029) means the phenomenon is background texture; the *question* is not yet posed â€” the stage advances to SURFACED only when a character or the narration frames it as a question. (e) 026's Râ‚€ = â— is background texture (SECRET-021 P1); its PARTIAL status is the suppression being established, not the paper's contents.

### MINOR MYSTERIES (039â€“102)

All minors: first appearance `TBD-per-plan`; Stageâ‚€ `UNFILED`; Râ‚€ `â—‹`; Dâ‚€ `â—‹`; Statusâ‚€ `OPEN` â€” except MYSTERY-090 (`ANSWERED-IN-CANON`; Râ‚€ â—, Dâ‚€ â—). Layer = anchor-derived cluster `(a)`, provisional until promotion. A minor promoted to major gets a full record: first-appearance staging, clue ledger, herring attachment, and reveal-stage placement per REVEAL_ORDER.md's phase rules.

| IDs | Layer (a) | Question (one line) |
|-----|-----------|---------------------|
| 039 | event-led | The 1996 Obsidian recording â€” what was on the unplayed cylinder? |
| 040 | faction/character | The Argent Vault's succession mechanism |
| 041 | faction/character | What Meridian Re actually reinsures â€” and against what |
| 042 | faction/character | Did the Pale Court steer the 1977 T5s, and which ones? |
| 043 | faction/character | Vesper's clinical endgame â€” treatment, containment, or harvest? |
| 044 | faction/character | What the Cradle screen was actually screening for |
| 045 | faction/character | What the Blackwater Syndicate harbor charter actually charters |
| 046 | faction/character | What the Ferrymen carried â€” and for whom (the child) |
| 047 | faction/character | The Quiet Ledger â€” what it is, and who keeps it |
| 048 | faction/character | What Halcyon's "thin-place compute" is actually computing |
| 049 | faction/character | The 2014 Quiet Desk memo's actual recommendation |
| 050 | faction/character | Why the Red Ledger keeps a Rule it will not enforce |
| 051 | faction/character | The Exchange's "second price" â€” the one not in the contract |
| 052 | faction/character | What the 2002 file loss actually lost |
| 053 | faction/character | The Cartographers' "deep map" â€” and who it is for |
| 054 | faction/character | What the Hollow Men's dive log redacts |
| 055 | faction/character | The Lantern Bearers' "second leak" â€” the one June Park is holding back |
| 056 | faction/character | What the Night Clerks' Ravenhurst cell actually trades |
| 057 | faction/character | The Rememberers' oldest memory |
| 058 | faction/character | The 1977 Drowndust ban's first version â€” before the mandatory revision |
| 059 | faction/character | The Tribunal's sealed award in the Kota Tua matter |
| 060 | faction/character | What the Memorandum Group's standing file on Ravenhurst says |
| 061 | history | The "other" 1996 bell ringing â€” the one not at the Bell's site |
| 062 | history | What stopped the 2007 examination from upgrading the vector |
| 063 | history | What the 1992 examination was actually examining (pre-transfer) |
| 064 | history | The "Jakarta boxes" provenance â€” who packed them, what was left out |
| 065 | history | What the 2018 sweep found at the morgue â€” and what it did not find |
| 066 | history | The "harbor light" the Blackwater Syndicate keeps lit |
| 067 | history | What the January 2024 peak actually peaked *in* |
| 068 | anomaly/history | The "second shadow" in Yusuf's logbook margins |
| 069 | anomaly/history | What Ilsa's 1991/1993/1995 divestment attempts actually did |
| 070 | anomaly/history | The "ferry" in Ilsa's journals â€” the one the tether waited at |
| 071 | anomaly/history | What Yusuf's brother Agus saw before the crane collapse |
| 072 | anomaly/history | The "bau payau" â€” the brackish smell's source |
| 073 | anomaly/history | What the 2020 Vesper clinician actually scanned (the Fathom-0 scare) |
| 074 | anomaly/history | The "cold halo" â€” the 1â€“2Â°C drop's mechanism |
| 075 | anomaly/history | What the Lantern-headache sufferers heard (~10m) |
| 076 | anomaly/history | The "voice-memo echo" â€” the 3s delayed voice's content |
| 077 | anomaly/history | What the children pointed at |
| 078 | anomaly/history | What the dogs left â€” and the cats stayed for |
| 079 | anomaly/history | The "darker-dark" â€” the less-than-zero light's physics |
| 080 | anomaly/history | Why Ilsa's ratchet measurements stop at 3.4s â€” what happens at 3.5 |
| 081 | anomaly/history | The "shallow places" geography â€” where exactly Crane dove |
| 082 | anomaly/history | What the Holloway counselor redacted from Crane's note |
| 083 | personal | The "second" September 2024 convergence â€” why five events in one month |
| 084 | personal | What the 2023 biennial monitor concluded (deferred) |
| 085 | personal | What Arthur's mother's "careful silence" is actually protecting |
| 086 | personal | What the *cleansing ritual* actually cleansed (the 2018 ritual) |
| 087 | personal | What Samuel Brooks's Loudness is adjacent to â€” why two Louds at one desk |
| 088 | personal | What the neighborhood counselor actually counseled |
| 089 | information-systems | The "Tuesday problem" â€” why Nadia forgets Tuesdays specifically |
| **090** | personal | **Are all humans born Loud? â€” ANSWERED-IN-CANON (Râ‚€ â—, Dâ‚€ â—)** |
| 091 | history | The "first" bell ringing â€” the one before 1996 |
| 092 | faction/character | What the SMD's Ravenhurst file actually contained â€” before it went thin |
| 093 | faction/character | The "third" cutout â€” the one the Quiet Desk hasn't identified |
| 094 | faction/character | What Vivienne Ashworth's gala question actually cost her |
| 095 | faction/character | The "wedding" the Pale Court cadets were buying for |
| 096 | faction/character | What the Factor's escrow paper actually escrowed |
| 097 | faction/character | The "second" price of the Nagisa Collection's art |
| 098 | faction/character | What the 1977 internment's budget line actually funded |
| 099 | anomaly/history | The "other" pre-1989 holder â€” the one Ilsa only inferred |
| 100 | anomaly/history | Are there other tethers â€” and if so, where |
| 101 | anomaly/history | What the Surabaya 1993 attempt actually targeted |
| 102 | anomaly/history | What the dark-water dreams are actually showing â€” direction, or invitation |

**Ledger totals (series start):** 105 mysteries Â· 41 MAJOR / 64 MINOR Â· UNFILED 99 Â· SURFACED 1 (001) Â· SEEDED 1 (002) Â· SURFACED-as-texture 3 (015/028/029) Â· PARTIAL 2 (001/026) Â· PROTECTED-L5 3 records + 2 hinge-carriers (see Â§3) Â· ANSWERED-IN-CANON 1 (090).

---

## Â§3 â€” PROTECTION PROTOCOL FOR THE CLOSED L5 SET

**The protected set (canon).** MYSTERIES.md and the mystery-architecture audit are explicit: the closed L5 set is **five**, staged across six records â€” *"The closed set is five; the audit does not expand it."*

| L5 | Mystery record(s) | The protected truth | Earliest resolution | Statusâ‚€ |
|----|-------------------|---------------------|---------------------|----------|
| L5-1 | MYSTERY-015 | What drives the Tide cycle | ch. 450+ | PROTECTED â€” INTENTIONAL MYSTERY |
| L5-2 | MYSTERY-002 | What stands at the other end; is it intelligent | ch. 400+ (Arthur earns the test) | PROTECTED â€” INTENTIONAL MYSTERY |
| L5-3 | MYSTERY-028 (hinge) | Does the Undertow want anything (the no-adversary axiom's margin) | ch. 450+ (may never fully resolve â€” recontextualize, never invalidate) | PROTECTED â€” hinge inside an OPEN record |
| L5-4 | MYSTERY-026 + MYSTERY-027 | What caused the 2018 attention-pressure effect (mechanism) | ch. 350+ (mechanism stays open past 350 even as the effect is used) | PROTECTED â€” hinge inside PARTIAL (026) and OPEN (027) records |
| L5-5 | MYSTERY-003 | What was on Ilsa Brandt's torn final page | ch. 350â€“450 (surfaces; worse than the bidding) | PROTECTED â€” INTENTIONAL MYSTERY |

**Canon note on a task-brief discrepancy.** The Phase 9 task brief described "12 intentional UNKNOWNs." Canon (MYSTERIES.md Part 3â€“4; AUDIT/MYSTERY_ARCHITECTURE_AUDIT.md Â§2 TEST 2 and Â§6) fixes the closed set at five and forbids expansion. This protocol implements the canon five. The other 28 major mysteries with `OBJECTIVE TRUTH: UNKNOWN` are ordinary OPEN mysteries with staged payoffs â€” unknown *for now*, not protected. The discrepancy is flagged for the parent orchestrator; the engine does not invent seven additional protected items to match the brief.

**The tripwire.** Any chapter plan â€” at any stage, in any arc â€” that would move a protected L5 truth toward resolution (from UNKNOWN into any KNOWS state, or that would *answer* the protected question by assertion, implication, or a character speculating correctly on-page) triggers an automatic **FLAG**:

1. The plan is halted at the information layer; the FLAG names the L5, the offending beat, and the state movement it would cause.
2. Clearing the FLAG requires an explicit **user-level decision** (not a worker judgment call): the user confirms the resolution condition is met (ch. window reached, Arthur's action earned it, dependencies cleared) or the beat is rewritten.
3. **Deepening is permitted; answering is not.** The engine may move L5-adjacent items freely: SUSPECTS may grow, FALSE BELIEFS may multiply, phenomena may accumulate (the ratchet lengthens, the margin's phenomena collate, the bidding intensifies). What may never happen by accident is the truth column moving. Per MYSTERY-015's canon rule: until the resolution condition, *no character speculates correctly on-page*.
4. **Adjacent-mystery guard.** REVEAL_ORDER.md's L5 protection schedule names the specific adjacent mysteries that must not answer an L5 by accident: 017 and 024 must not answer L5-1; 007 and 013 must feed L5-2 without resolving it; 019 and 026 must not answer L5-3; 015's mechanism stays open while its effects are used (L5-4); 006's person-auction and 003's paper-auction stay in different arcs (L5-5). The batch protocol (Â§4, step 8) checks these edges every batch.
5. **The Level-7 Worldtide silence** is registered in the audit and is NOT promoted to L5. It is a documented silence, not a protected mystery â€” the engine must not treat it as either.

---

## Â§4 â€” UPDATE DISCIPmessaging app: THE 12-STEP BATCH PROTOCOL

The ledger advances **chapter-batch by chapter-batch** (a batch = the set of chapters planned together, typically one arc's drafting unit). Two roles:

- **The planning worker** proposes the batch's information deltas (INFORMATION_FLOW.md Â§2) and the resulting ledger updates.
- **The consistency worker** verifies every update against the canon files and either accepts it into the ledger or returns it with FLAGs.

Neither role invents lore, mysteries, characters, or IDs. The ledger only ever records what canon already contains or what an accepted chapter plan has deliberately added.

**The 12 steps** (run in order; a FLAG at any step returns the batch to the planning worker):

1. **Collect deltas.** Gather every chapter's information delta (BEFORE â†’ OPERATIONS â†’ AFTER) from the batch.
2. **Verify acquisition.** For each new KNOWS claim, demand the Â§7 acquisition chain (INFORMATION_FLOW.md). Unknown source â†’ FLAG.
3. **Check knowledge consistency.** No character knows what they have not reasonably acquired; no beat acts on READER-only knowledge (leakage detection, INFORMATION_FLOW.md Â§4).
4. **Advance reveal stages per REVEAL_ORDER.** A stage may advance only in its canon phase window and only when the gating table (INFORMATION_FLOW.md Â§5) is satisfied: SURFACE/SEED needs a planted question; PARTIAL needs a cited clue in a KNOWS state; MAJOR needs setup + reinforcement already planted (the nowhere test), the reader-lead rule satisfied, and â‰¥2 factions repriced; FINAL needs HARD dependencies cleared, collisions checked, and Arthur's action as the mechanism.
5. **Check dependencies.** Against MYSTERY_DEPENDENCIES.md's D-table: no mystery advances past a HARD edge whose prerequisite has not reached the required stage. (E.g., 002's PARTIAL requires 001's MAJOR; 008's MAJOR requires 005's resolution.)
6. **Check collisions.** Against the C-table: no two colliding reveals in the same arc (C-01: 002's hinge vs 015's partial â‰¥100 chapters apart; C-02: the two auctions in different arcs; C-03: 005 before 008's pitch; C-04: 013's tripwire before 002's hinge; C-05: 014 vs 034 â‰¥80 chapters or deliberately merged; C-06: 011 before 012's manual reveal).
7. **Check the reader-lead rule.** The reader never leads Arthur by more than one phase â€” except SECRET-007 and SECRET-015, the two deliberate ironies. Any other lead â†’ FLAG.
8. **Scan the L5 tripwire.** No protected truth moved toward resolution (Â§3); adjacent-mystery guards respected; no character speculated correctly on-page about an L5.
9. **Maintain red herrings.** Herrings attached to advanced mysteries are re-scored: live (holder still believes, disproof not yet available in-world), weakened (disproof available but not yet delivered), or dead (disproof delivered â€” the herring is spent and removed from the FALSE BELIEFS ledger). No registered herring may be confirmed as true; no unregistered candidate may be staged as misdirection (RED_HERRINGS.md rule).
10. **Update the clue ledger.** Mark planted clues spent or reinforced; log additional clues with their beats; retire clues whose payoff has landed.
11. **Update knowledge cells.** Advance CURRENT READER KNOWLEDGE and CURRENT ARTHUR KNOWLEDGE (and OTHER CHARACTERS / FACTIONS where the batch moves them) per the accepted deltas. FALSE BELIEFS entries are updated with holder, confidence, and disproof status.
12. **Flag open questions for the next batch.** Unresolved dependencies, unspent setups approaching their payoff windows, herrings nearing their sell-by, and any mystery whose stage has not moved in two consecutive batches (stagnation watch â€” the question-debt cap of â‰¤2 new OPEN threads per arc means stalled threads must be deliberately parked, not forgotten).

**Ledger hygiene.** The ledger is append-only history plus current-state: every update records the batch, the chapter(s), and the canon or plan citation that caused it. A state is never overwritten without its prior value being preserved in the history. The ledger is the Chapter Engine's memory of what the series has told â€” it is never edited to make a plan convenient.

---

*End of CHAPTER_MYSTERY_TRACKER.md â€” Chapter Engine, tracking systems.*


---

## SECTION: `DATABASE/INFORMATION_FLOW.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `DATABASE/INFORMATION_FLOW.md` Â· sha256 `ed19e85feccf3f03fddf93ea950c99e70e8c4fecb6fc917d030f1dcdb89082f4` Â· 2,485 words. No content changed.

# DATABASE â€” INFORMATION FLOW (Chapter Engine)

**THE QUIET TIDE v1.9** Â· Phase 9: Chapter Engine Architecture â€” TRACKING SYSTEMS
**Purpose:** the information-state machine the Chapter Engine runs on. This file defines *how knowledge moves*; CHAPTER_MYSTERY_TRACKER.md defines *what* is tracked; CHAPTER_FORESHADOWING_TRACKER.md defines *how clues are staged*.
**Canon anchors:** DATABASE/MYSTERIES.md (105 mysteries, the closed L5 set) Â· DATABASE/REVEAL_ORDER.md (reveal stages and pacing) Â· DATABASE/MYSTERY_DEPENDENCIES.md (dependency edges, collision risks) Â· DATABASE/RED_HERRINGS.md (registered herrings RH-001â€“036, misdirections M-01â€“06) Â· DATABASE/INFORMATION_KNOWLEDGE_MAP.md (SECRET-001â€“024, structural rules) Â· DATABASE/STORY_ENGINE.md (Â§2 the three questions; Â§5 the information engine; Â§7 romance interface; Â§10 inherited constraints).
**Not this file:** no chapters, no scenes, no prose, no dialogue. Only the machine.

---

## Â§1 â€” THE INFORMATION-STATE SCHEMA

Every fact the series cares about exists, at any moment, in up to eight states simultaneously â€” one per knower. The states are the ledger's vocabulary. Each definition names the *subject* of knowledge first.

| # | State | Subject of knowledge | Definition |
|---|-------|----------------------|------------|
| 1 | **READER KNOWS** | The reader | The fact has been presented as reliable narrative truth â€” not as a character's claim, not as texture, but as something the narration vouches for. Test: could the reader cite it in an argument about the plot and be right? |
| 2 | **ARTHUR KNOWS** | Arthur Reed (CHAR-001) | Arthur holds the fact as established in his own mind. He can act on it, file on it, and be wrong about its implications â€” but he will not un-know it without a canon mechanism (Veil-editing, Quiet forgetting). Test: would he bet his job on it? |
| 3 | **OTHER CHARACTERS KNOW** | A named character (Nadia, Aisha, SaitÅ, June Park, Pram, â€¦) | The named individual holds the fact as established. Always named â€” "someone knows" is not a state, it is a missing citation. Each holder is a separate ledger entry. |
| 4 | **FACTIONS KNOW** | An institution (the Quiet Desk, the Red Ledger, the Exchange, the Choir, â€¦) | The fact is in the faction's *working model*: briefed, tasked around, priced, or acted on. **Possession is not knowledge.** Per INFORMATION_KNOWLEDGE_MAP.md structural rule 2, institutions hold without knowing (SECRET-006: the Exchange holds Ilsa's journals 28 years without reading them; SECRET-011: the Hollow Men file Crane's warning and never see it). The ledger therefore tracks two sub-states: **HOLDS** (possesses the record) and **KNOWS** (has institutional attention on it). A faction that HOLDS but does not KNOW is a loaded gun, not a player. |
| 5 | **READER SUSPECTS** | The reader | The reader has seen clues pointing at the fact but has received no confirmation. This is fair-play territory: the suspicion must be *earnable* from planted clues, never from authorial winks. Test: on reread, the reader can point at the clue. |
| 6 | **ARTHUR SUSPECTS** | Arthur | Arthur has formed a hypothesis he has not verified. He *cannot* act on it as fact without the plan showing his working â€” suspicion that drives action must be cited as inference (see Â§7, sources 8 and 11). Test: would he say "I think" rather than "I know"? |
| 7 | **FALSE BELIEFS** | A named holder (character or faction) | Someone believes something *false* about the fact, with a recorded confidence level. False beliefs are **first-class tracked items**, not annotations. Every ledger entry records: the holder, the false belief, its confidence (firm / working / fragile), its canon disproof (from RED_HERRINGS.md where registered), and whether the disproof is *available in-world* yet. A herring the characters cannot yet disprove is live misdirection; a herring the reader has seen disproved is dead weight â€” the ledger distinguishes them. |
| 8 | **UNKNOWN** | No one | No actor holds or suspects the fact. It exists only in the author's canon record (the ACTUALLY TRUE column of Â§4). This is the default state of every mystery at series start. UNKNOWN is not ignorance â€” it is the engine's inventory of unspent truth. |

**KNOWS vs SUSPECTS (the load-bearing line).** KNOWS means the holder treats the fact as settled enough to act on; SUSPECTS means the holder treats it as a live hypothesis. The difference is behavioral, not verbal: a character who says "I know" but acts on contingency is in SUSPECTS. The ledger records behavior, not dialogue claims.

---

## Â§2 â€” THE PER-CHAPTER RULE

**Every chapter must intentionally modify AT LEAST ONE information state.**

Movement is the chapter's information delta. Increasing uncertainty counts as movement: a chapter that moves an item from KNOWS into SUSPECTS (destabilizing a certainty), or that plants a new FALSE BELIEF, or that moves an item from FALSE BELIEFS into UNKNOWN-adjacent doubt (a herring collapsing), has moved the machine. So does a chapter that moves nothing toward answers but deepens a SUSPECTS state â€” provided the deepening is deliberate and logged, not drift.

**The delta record.** Every chapter plan carries an information delta in three parts:

1. **BEFORE:** the ledger snapshot of every item the chapter touches (state, holder, confidence).
2. **OPERATIONS:** the list of moves, each naming the scene or beat that causes it. Format: `[item] : [state A] â†’ [state B] â€” via [beat]`. Example shape: `SECRET-019's examiner method : READER SUSPECTS â†’ READER KNOWS â€” via the 2021 examiner's identity surfacing in Arthur's file`.
3. **AFTER:** the new states, with any new ledger entries (new SUSPECTS, new FALSE BELIEFS) created and any spent clues marked.

**What does not count.** Texture without movement (a clue repeated with no new state), a reveal the reader already had (KNOWS â†’ KNOWS), and off-page drift ("meanwhile the Desk learnsâ€¦" without a beat) do not satisfy the rule. If a chapter's delta is empty, the chapter is not yet planned.

**Pacing guardrail.** Per REVEAL_ORDER.md, P1 holds the reader's questions above answers at roughly 5:1. The per-chapter rule does not override this: most deltas in P1 move items from UNKNOWN into SUSPECTS (planting), not into KNOWS. The engine plants far more than it pays.

---

## Â§7 â€” THE KNOWLEDGE CONSISTENCY RULE (Chapter Engine Â§7)

**NO CHARACTER MAY KNOW INFORMATION THEY HAVE NOT REASONABLY ACQUIRED.**

"Reasonably acquired" is not a vibe. It is a chain. Every knowledge claim in a chapter plan must name its acquisition source; a claim with no source is not a gap â€” it is a **FLAG**, and the plan does not proceed until the FLAG is cleared or the claim is cut.

### The eleven sanctioned acquisition sources

Each source carries a one-line test. The planner applies the test; if the claim fails it, the source is invalid for that claim.

1. **Direct observation.** *Test:* was the character present, perceiving, and capable (Loud/Quiet/Veil constraints respected) at the time and place?
2. **Conversation.** *Test:* who told them, when â€” and did the teller know it themselves (produce the teller's own chain)?
3. **Document.** *Test:* which record, who filed it, is it authentic and unredacted â€” and did the character actually read it (holding â‰  reading, per Â§1)?
4. **Investigation.** *Test:* what method did they use, and what did it actually reveal â€” not what they hoped it would?
5. **Previous event.** *Test:* were they present at the event? If not, this is not the source â€” the source is the conversation or document that reported it.
6. **Faction report.** *Test:* was the fact briefed to them in their role, and does the faction institutionally KNOW it (not merely HOLD it)?
7. **Rumor.** *Test:* who repeated it, through how many mouths, and what has the repetition added or stripped? (Rumor never upgrades SUSPECTS to KNOWS.)
8. **Inference.** *Test:* from which cited premises â€” and is the inference valid, or merely plausible (mark confidence: firm / working / fragile)?
9. **Supernatural ability.** *Test:* which ability, what are its canon limits â€” and does this use exceed them?
10. **Historical record.** *Test:* primary or secondary â€” and what has time done to it (rot, Veil-editing, redaction, the 28-year dormancy)?
11. **Deduction.** *Test:* what is the full premise chain â€” and would *this character* actually assemble it (their skill and habits, not the author's)?

### The citation requirement

Every knowledge claim in a chapter plan is written as: **[fact] â† [source type] â† [specific origin]**. The origin must be specific: a named person, a named document, a ledgered event. "He figured it out" is not a citation â€” it is sources 8 or 11 with the premises listed, or it is a FLAG.

### Worked generic procedure (not a chapter)

How a planner traces "Character X knows fact Y" back to a canon-grounded origin:

1. **State the claim** in one sentence: "X knows Y."
2. **Name the acquisition source** from the eleven above. If none fits, FLAG â€” do not proceed.
3. **Step one link back.** If the source is a document: who filed it, and how did X come to read it? If a conversation: who told X, and what is *their* chain (repeat from step 1 for the teller)? If observation: establish presence and capability.
4. **Repeat** until the chain terminates in a canon-grounded origin: a bible entry (e.g., 26_INFORMATION_CONTROL Â§26.4), an EVENT ledger entry, a filed record named in MYSTERIES.md's KNOWN CLUES, or a scene already in the information ledger.
5. **If the chain ends in "they just know,"** or in a source that itself has no chain, the claim is a **leak** (see Â§4): FLAG it, cut it, or build the missing link as a deliberate beat â€” which itself becomes an information operation in the chapter's delta (Â§2).

---

## Â§4 â€” THE THREE-STATE SEPARATION DOCTRINE

Three columns, never merged: **WHAT ARTHUR KNOWS** Â· **WHAT THE READER KNOWS** Â· **WHAT IS ACTUALLY TRUE**. The reader-lead rule (STORY_ENGINE.md Â§10; INFORMATION_KNOWLEDGE_MAP.md structural rule 1): the reader may know more than Arthur, but never leads him by more than one phase â€” except the two deliberate ironies, SECRET-007 (the torn page for sale) and SECRET-015 (the Court's wrong theory). ACTUALLY TRUE is the author's column; no character's KNOWS state may contain it except through the acquisition chains of Â§7.

**Formal rules for plans:**

1. **Three columns, always.** Every chapter plan's information section lists the touched items under all three headings, even when two are empty. An empty ARTHUR KNOWS column is information â€” it means the chapter runs on dramatic irony or on Arthur's ignorance as a load-bearing condition.
2. **No cross-column contamination.** A beat that is only in READER KNOWS (e.g., the reader sees the auction announced in CG-048 before Arthur learns of it â€” SECRET-007) must never cause Arthur to act as if he knows it. If Arthur's behavior in the plan is only explicable by reader-level knowledge, the plan has a leak.
3. **"Realizes" is a claim.** Any beat written as "Arthur realizes X" must cite the trigger: the premises he assembled (deduction/inference) or the new evidence he received. Untriggered realization is a FLAG.
4. **"Everyone knows" is forbidden.** Plans never write "it's common knowledge," "word gets around," or "the hidden world knows." Knowledge has holders; name them or FLAG.
5. **The FALSE BELIEFS column is separate from the TRUE column.** A faction acting on a wrong theory (the Pale Court's bloodline cosmology â€” SECRET-015) is tracked under FALSE BELIEFS with its holder and confidence, never filed as what the faction "knows." When the plan needs the Court's behavior, it reads the FALSE BELIEFS column.

**Leakage detection procedure** (run against every chapter plan before it is accepted):

1. List every ARTHUR KNOWS and OTHER CHARACTERS KNOW claim the plan makes.
2. For each, demand the Â§7 acquisition chain. Produce the chain or mark the claim.
3. Cross-check each chain against the information-flow ledger (the running record of what has been planted, shown, told, and filed). A chain that references a beat not in the ledger is broken â€” FLAG.
4. Any claim with no chain, or a broken chain, is a **leak**: information has entered a character's head from the author's column without traveling through the world. FLAG it.
5. Any beat where a character acts on information that exists only in the READER KNOWS column is **cross-contamination**: FLAG it.
6. FLAGS are cleared only by: cutting the claim, building the missing link as a deliberate beat (logged in the delta), or â€” for intentional ironies â€” explicit sign-off that the irony is one of the two canon-sanctioned ones (SECRET-007, SECRET-015).

---

## Â§5 â€” INTERACTION WITH THE MYSTERY ENGINE

Information states are the gates on REVEAL_ORDER.md's reveal stages. A mystery's stage (CHAPTER_MYSTERY_TRACKER.md) may advance only when the information states behind it have moved.

**The gating table** (staging vocabulary from REVEAL_ORDER.md):

| Reveal stage | Required information-state movement | Gate |
|---|---|---|
| **SURFACE / SEED** | The question enters READER SUSPECTS (the reader sees something unexplained) or ARTHUR SUSPECTS. | No gate beyond the per-chapter rule (Â§2). Planting is cheap; the 5:1 question-debt ratio is the governor. |
| **PARTIAL** | At least one clue is in READER KNOWS or ARTHUR KNOWS (as established fact, not hypothesis); the partial answer is cited. | The dependency table (MYSTERY_DEPENDENCIES.md): a HARD edge (A â†’ B) means B's PARTIAL requires A's PARTIAL or better. |
| **MAJOR** | The reveal's core fact enters READER KNOWS and ARTHUR KNOWS (or deliberately one without the other, per the knowledge map's asymmetry notes). | (a) Reader-lead rule satisfied (â‰¤1 phase, except SECRET-007/015). (b) Every MAJOR reprices â‰¥2 factions (REVEAL_ORDER.md pacing rule 2) â€” the plan names the repriced factions. (c) The foreshadowing pipeline (CHAPTER_FORESHADOWING_TRACKER.md) shows setup + reinforcement already planted â€” the nowhere test is passed. |
| **FINAL** | ACTUALLY TRUE merges into the KNOWS columns per the resolution. | (a) All HARD dependencies cleared. (b) Collision risks checked (MYSTERY_DEPENDENCIES.md C-table: no colliding reveal in the same arc). (c) Finales are earned by Arthur's action, never exposition (REVEAL_ORDER.md pacing rule 5). |

**L5 gating (the closed set).** The five intentional mysteries (MYSTERY-002/L5-2, MYSTERY-003/L5-5, MYSTERY-015/L5-1, MYSTERY-028/L5-3 hinge, MYSTERY-026+027/L5-4) carry a hard cap: **no information operation may move their core truth from UNKNOWN into any KNOWS state** except through their canon-defined resolution conditions at their canon-defined windows (REVEAL_ORDER.md's L5 protection schedule). Deepening is permitted â€” SUSPECTS may grow, FALSE BELIEFS may multiply, phenomena may accumulate â€” but the truth column stays shut. Any plan that would move an L5 core truth toward KNOWS is an automatic FLAG requiring explicit user-level decision (see CHAPTER_MYSTERY_TRACKER.md Â§3, the protection protocol).

**Negative movement counts.** Information states can move backward, and the gates respect it: Veil-editing, Quiet forgetting (the Tuesday problem â€” MYSTERY-089/SECRET-017), and destroyed records move items from KNOWS to SUSPECTS or back to UNKNOWN. A mystery's reveal stage does not automatically regress when a character forgets â€” the *stage* is a property of the series (what has been revealed), while the *states* are properties of knowers. The ledger tracks both.

---

*End of INFORMATION_FLOW.md â€” Chapter Engine, tracking systems.*


---

## SECTION: `DATABASE/INFORMATION_KNOWLEDGE_MAP.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `DATABASE/INFORMATION_KNOWLEDGE_MAP.md` Â· sha256 `8ef02d6962e48495a0db326101f0891d572fa876ea6dbff9e183c857bfb049f8` Â· 2,570 words. No content changed.

# DATABASE â€” INFORMATION & KNOWLEDGE MAP

**THE QUIET TIDE v1.5â€“v1.6** Â· created in the Mystery architecture & foreshadowing audit (2026-09-20); carried forward unchanged in the Power progression audit
**Purpose:** track who knows what, when. Knowledge in this series is asymmetric by design â€” the map exists so reveals land on characters who *don't* know yet, and so the reader's advantage over Arthur is managed, never accidental.
**Phases:** P1 (ch. 1â€“100: the curiosity) Â· P2 (ch. 100â€“250: the tether) Â· P3 (ch. 250â€“400: the market) Â· P4 (ch. 400+: the hinge).
**Actors:** R = reader Â· D = Arthur Â· AL = allies (Night Clerks, Nadia, Aisha, Pram) Â· AN = antagonists (Pale Court cadets, the Factor/Red Ledger, the Quiet Desk as institutional antagonist) Â· GF = governments/factions (SMD, Compact, Choir, Exchange, Archivists, Vesper, Halcyon).
**Cell values:** â— knows Â· â— suspects/partial Â· â—‹ does not know Â· â€” not applicable/dead.

---

## SECRET-001 â€” The Laggard is a tether, not a shadow

| Phase | R | D | AL | AN | GF |
|-------|---|---|----|----|----|
| P1 | â— (sees the lag, no name) | â—‹ | â—‹ | â—‹ | â—‹ |
| P2 | â— (Ilsa's journals via Pram) | â— | â— (Night Clerks hear) | â— (Ledger prices it) | â— (Exchange owns the journals) |
| P3 | â— | â— | â— | â— | â— |
| P4 | â— | â— | â— | â— | â— |

**Asymmetry notes:** The reader learns with Arthur (no dramatic irony â€” the horror is shared). The Exchange *holds* the truth for 28 years without *reading* it (dormant archive â€” institutional knowledge without institutional attention).

## SECRET-002 â€” The transfer rule (unforced death/Drowning â†’ nearest Loud witness; engineered transfer fails)

| Phase | R | D | AL | AN | GF |
|-------|---|---|----|----|----|
| P1 | â—‹ | â—‹ | â—‹ | â—‹ | â—‹ |
| P2 | â— (Surabaya 1993 entry) | â— | â—‹ | â— (Ledger's 1996 paper hints) | â—‹ |
| P3 | â— | â— | â— | â— (Ledger understands â€” hence the buyer) | â— |
| P4 | â— | â— | â— | â— | â— |

**Asymmetry notes:** The Factor's buyer (MYSTERY-006) is buying something that *cannot be transferred by purchase* â€” the buyer's ignorance of SECRET-002 is the dramatic engine of the auction arc. The reader must learn SECRET-002 *before* the auction (P2) so the auction reads as tragedy/farce, not confusion.

## SECRET-003 â€” The ratchet (deep use permanently lengthens the lag; Ilsa 3.0â†’3.4s)

| Phase | R | D | AL | AN | GF |
|-------|---|---|----|----|----|
| P1 | â— (Arthur notices 3.0â†’3.1) | â— | â—‹ | â—‹ | â—‹ |
| P2 | â— (Yusuf's logbook confirms) | â— | â—‹ | â—‹ | â—‹ |
| P3 | â— | â— | â— | â— | â— |
| P4 | â— | â— | â— | â— | â— |

**Asymmetry notes:** Arthur's private measurement is the series' clock. No institution tracks it (the examiners measure *output*, not lag â€” the filing system's blindness is structural).

## SECRET-004 â€” Something stands at the other end; attention flows both ways (L5-2)

| Phase | R | D | AL | AN | GF |
|-------|---|---|----|----|----|
| P1 | â— (dreams) | â— (felt looked-at) | â—‹ | â—‹ | â—‹ |
| P2 | â— (Crane's warning) | â— | â—‹ | â—‹ | â—‹ |
| P3 | â— | â— | â— | â—‹ | â—‹ |
| P4 | â— (the hinge â€” Arthur's test) | â— | â— | â— | â— |

**Asymmetry notes:** L5-2 â€” nobody reaches â—, including the reader, until the resolution condition (Arthur earns the test). The map enforces this: no phase shows â— for anyone.

## SECRET-005 â€” The smiling reflection

| Phase | R | D | AL | AN | GF |
|-------|---|---|----|----|----|
| P1 | â— (the no-mirrors rule) | â— | â—‹ | â—‹ | â—‹ |
| P2 | â— (Ilsa's journal entry) | â— | â—‹ | â—‹ | â—‹ |
| P3 | â— | â— | â—‹ | â— (someone mentions the mirror â€” the tripwire) | â—‹ |
| P4 | â— | â— | â— | â— | â— |

**Asymmetry notes:** Arthur's *only* secret the reader shares from P1. The tripwire (someone else mentions the mirror) must land on a reader who has carried the secret for 300 chapters â€” the payoff is proportional to the carrying time.

## SECRET-006 â€” Ilsa's journals exist (Exchange archive, dormant 28 years)

| Phase | R | D | AL | AN | GF |
|-------|---|---|----|----|----|
| P1 | â—‹ | â—‹ | â—‹ | â—‹ | â— (Exchange holds, doesn't read) |
| P2 | â— (Pram's arrival) | â— | â— | â— | â— |
| P3 | â— | â— | â— | â— | â— |

**Asymmetry notes:** The Exchange's dormancy is the series' thesis on archives: *holding is not knowing.*

## SECRET-007 â€” The torn last page exists and is for sale (L5-5)

| Phase | R | D | AL | AN | GF |
|-------|---|---|----|----|----|
| P1 | â—‹ | â—‹ | â—‹ | â—‹ | â—‹ |
| P2 | â— (the torn binding) | â— | â—‹ | â— (Ledger knows) | â— |
| P3 | â— (the auction announced) | â— | â— | â— | â— |
| P4 | â— | â— | â— | â— | â— |

**Asymmetry notes:** The reader learns the page is *for sale* before Arthur does (CG-048) â€” one of the series' few deliberate dramatic ironies: the reader watches three factions bid on the deadline of Arthur's life.

## SECRET-008 â€” The 1996 Kota Tua deal (Ledger paper; counterparty unknown)

| Phase | R | D | AL | AN | GF |
|-------|---|---|----|----|----|
| P1 | â—‹ | â—‹ | â—‹ | â— (Ledger's institutional memory) | â—‹ |
| P2 | â— | â— | â—‹ | â— | â—‹ |
| P3 | â— | â— | â—‹ | â— | â— |
| P4 | â— | â— | â— | â— | â— |

## SECRET-009 â€” The hiring approver's identity (redacted signature)

| Phase | R | D | AL | AN | GF |
|-------|---|---|----|----|----|
| P1 | â— (the flagged file) | â—‹ | â—‹ | â—‹ | â— (Quiet Desk holds redactions) |
| P2 | â— | â— | â—‹ | â—‹ | â— |
| P3 | â— | â— | â— | â— | â— |
| P4 | â— | â— | â— | â— | â— |

## SECRET-010 â€” The Factor's buyer (Pale Court cadets, Nagisa Collection)

| Phase | R | D | AL | AN | GF |
|-------|---|---|----|----|----|
| P1 | â—‹ | â—‹ | â—‹ | â— (Ledger knows) | â— (Quiet Desk watches) |
| P2 | â— (the inquiry rumor) | â—‹ | â— | â— | â— |
| P3 | â— | â— | â— | â— | â— |

**Asymmetry notes:** The antagonists know first; the reader second; Arthur last. The reveal order is a *class* reveal: Arthur learns he is a lot, not a person.

## SECRET-011 â€” Crane's warning (the entity seen from the Undertow)

| Phase | R | D | AL | AN | GF |
|-------|---|---|----|----|----|
| P1 | â—‹ | â—‹ | â—‹ | â—‹ | â— (Holloway filed it) |
| P2 | â— | â— | â— | â— (Hollow Men never saw their own flag) | â— |
| P3 | â— | â— | â— | â— | â— |

**Asymmetry notes:** The Hollow Men's bureaucracy ate their own diver's warning â€” the series' purest case of *institutional knowledge without institutional attention* (cf. SECRET-006).

## SECRET-012 â€” The Quiet Desk's doctrine (anti-Snowden; hire-before-publish; the hard case)

| Phase | R | D | AL | AN | GF |
|-------|---|---|----|----|----|
| P1 | â—‹ | â—‹ | â—‹ | â— (the Desk) | â— (SMD) |
| P2 | â— | â— | â— (Aisha's compromise visible) | â— | â— |
| P3 | â— | â— | â— | â— | â— |

## SECRET-013 â€” The escrow / dead-man's switch (~70% exposure on seizure)

| Phase | R | D | AL | AN | GF |
|-------|---|---|----|----|----|
| P1 | â—‹ | â—‹ | â—‹ | â—‹ | â—‹ |
| P2 | â— | â— | â— | â— (the Desk models it) | â— |
| P3 | â— | â— | â— | â— | â— |

**Asymmetry notes:** The reader and Arthur build it together (P2) â€” the series' only symmetric construction project. Everyone else *discovers* it.

## SECRET-014 â€” The Archivists' pre-1989 search (Javanese figure, Passchendaele nurse)

| Phase | R | D | AL | AN | GF |
|-------|---|---|----|----|----|
| P1 | â—‹ | â—‹ | â—‹ | â—‹ | â— (Archivists) |
| P2 | â— (the second request) | â— | â—‹ | â—‹ | â— |
| P3 | â— | â— | â— | â— | â— |

## SECRET-015 â€” The Pale Court's bloodline interest (wrong theory; the Court believes anyway)

| Phase | R | D | AL | AN | GF |
|-------|---|---|----|----|----|
| P1 | â—‹ | â—‹ | â—‹ | â— (cadets) | â—‹ |
| P2 | â— (the gala question) | â—‹ | â—‹ | â— (the Court) | â—‹ |
| P3 | â— | â— | â— | â— | â— |

**Asymmetry notes:** The antagonists' *error* is the secret â€” the reader learns the Court is wrong (P3) while the Court continues acting on its theory. Dramatic irony as institutional critique.

## SECRET-016 â€” June Park's cache (sender unknown; serials filed off)

| Phase | R | D | AL | AN | GF |
|-------|---|---|----|----|----|
| P1 | â—‹ | â—‹ | â—‹ | â—‹ | â—‹ |
| P2 | â— (the leak breaks) | â—‹ | â— (Lantern Bearers hold it) | â— | â— |
| P3 | â— | â— | â— | â— | â— |
| P4 | â— (sender identified) | â— | â— | â— | â— |

## SECRET-017 â€” Nadia's routine (the pipeline's authorship)

| Phase | R | D | AL | AN | GF |
|-------|---|---|----|----|----|
| P1 | â— (the softening) | â— | â—‹ | â—‹ | â— (NQA's pipeline) |
| P2 | â— | â— | â— (Nadia shows the manual) | â—‹ | â— |
| P3 | â— | â— | â— | â— | â— |

## SECRET-018 â€” The Quiet Night internment (~300 Loud interned, 1977)

| Phase | R | D | AL | AN | GF |
|-------|---|---|----|----|----|
| P1 | â—‹ | â—‹ | â—‹ | â—‹ | â— (Memorandum Group) |
| P2 | â— (the blank plaque) | â—‹ | â— (Rememberers' elders) | â—‹ | â— |
| P3 | â— | â— | â— | â— | â— |

## SECRET-019 â€” The 2021 examination's method (how the examiner found him)

| Phase | R | D | AL | AN | GF |
|-------|---|---|----|----|----|
| P1 | â— (the examination exists) | â— | â—‹ | â—‹ | â— (the examiner's desk) |
| P2 | â— | â— | â—‹ | â—‹ | â— |

**Asymmetry notes:** Resolves early (P2) â€” the answer constrains the archive-omniscience test: the method must be *specific and limited* (a sweep, an informant, a routine), never "the system sees everything."

## SECRET-020 â€” The jurisdiction seam (BPF Jakarta filed; SMD holds the thin copy; the 2017 transfer unreported)

| Phase | R | D | AL | AN | GF |
|-------|---|---|----|----|----|
| P1 | â— | â—‹ | â—‹ | â—‹ | â— (both desks, neither connecting) |
| P2 | â— | â— | â—‹ | â—‹ | â— |

**Asymmetry notes:** The reader's clerk-eye beats the institutions' â€” the seam is visible to anyone who reads *both* files. Arthur is the first to hold both.

## SECRET-021 â€” The 2018 attention-pressure effect (L5-4)

| Phase | R | D | AL | AN | GF |
|-------|---|---|----|----|----|
| P1 | â— (background texture) | â—‹ | â—‹ | â—‹ | â— |
| P2 | â— | â— | â—‹ | â—‹ | â— |
| P3 | â— (Nwosu's data) | â— | â— | â— | â— |
| P4 | â— (L5-4 â€” the mechanism stays open) | â— | â— | â— | â— |

## SECRET-022 â€” The T7 designation (empty; undocumented; the ceiling that isn't)

| Phase | R | D | AL | AN | GF |
|-------|---|---|----|----|----|
| P1 | â—‹ | â—‹ | â—‹ | â—‹ | â— (whoever wrote it) |
| P2 | â— (the footnote) | â— | â—‹ | â—‹ | â— |
| P3 | â— | â— | â—‹ | â—‹ | â— |
| P4 | â— | â— | â— | â— | â— |

## SECRET-023 â€” The Bell's response pattern (rings at tether events?)

| Phase | R | D | AL | AN | GF |
|-------|---|---|----|----|----|
| P1 | â—‹ | â—‹ | â—‹ | â—‹ | â—‹ |
| P2 | â— (the 2017 ringing) | â— | â—‹ | â—‹ | â— |
| P3 | â— | â— | â— | â— | â— |

## SECRET-024 â€” The margin note's impossibility ("Do not let them auction the boy")

| Phase | R | D | AL | AN | GF |
|-------|---|---|----|----|----|
| P1 | â—‹ | â—‹ | â—‹ | â—‹ | â—‹ |
| P2 | â— (EVENT-100 â€” the reader sees the date problem) | â— | â—‹ | â—‹ | â—‹ |
| P3 | â— (the handwriting check) | â— | â— | â— | â— |

**Asymmetry notes:** The reader is invited to notice the date paradox *before* Arthur runs the handwriting check â€” a fair-play clue. The check's result (contemporary hand vs 1996 hand) determines whether a new player is annotating Ilsa's journals *now*.

---

## KNOWLEDGE MAP: STRUCTURAL RULES

1. **The reader never leads Arthur by more than one phase** â€” except SECRET-007 (the auction) and SECRET-015 (the Court's error), the two deliberate dramatic ironies. Everywhere else, reader and Arthur discover together.
2. **Institutions hold without knowing** (SECRET-006, SECRET-011, SECRET-020) â€” the series' thesis: archives are not attention.
3. **Antagonists know first only when their knowledge is *wrong*** (SECRET-015) or *useless* (SECRET-010's buyer can't complete the purchase â€” SECRET-002). Correct, useful antagonist knowledge arrives no earlier than P3.
4. **L5 secrets never reach â—** for anyone â€” including the reader â€” until their resolution conditions. The map enforces the closed set.
5. **Arthur's archive advantage** is visible in the map: he is the only actor who reaches â— on SECRET-020 (both files) and SECRET-003 (the ratchet) â€” not because he has clearance, but because he *reads*.


---

## SECTION: `DATABASE/ROMANCE_ARCHITECTURE.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `DATABASE/ROMANCE_ARCHITECTURE.md` Â· sha256 `2f60c6053b2540a0bcfba196f47e066ae59f79e2cf0ded7f7c0c5ab743773a19` Â· 5,698 words. No content changed.

# DATABASE â€” Romance Architecture (THE QUIET TIDE)

> Version: v1.8 (Romance architecture audit, 2026-09-20). Canon build: FINAL_WORLD_BIBLE v1.8.
> Source of truth for romantic configuration: `32_ROMANCE_FRAMEWORK.md` (five candidate configurations, six inviolable rules). This database records per-character romantic architecture â€” needs, boundaries, trust, secrets, asymmetry â€” for audit and story-engine use. It does not create scenes, dialogue, or plot. All prose in English.
> Canon locks preserved: Arthur's identity and anomaly mechanism; inheritance chain; Ravenhurst March 2017 transfer; all character/faction/anomaly IDs; no chapters, scenes, prose, dialogue, or story outlines created in this phase.

## 0. Governing rules (from 32_ROMANCE_FRAMEWORK.md Â§32.3 â€” CANON)

1. **No "civilian partner who never finds out."** Loving someone systematically deceived, whose memory the Veil edits nightly, is horror with better lighting. If a Quiet partner is chosen, the asymmetry itself must be the story.
2. **Consent includes memory.** A Loud partner knows things about a Quiet partner's forgotten experiences. The novel must treat this as an intimate violation â€” never a cute advantage.
3. **Erosion is not romantic.** The Attuned clock must never be aestheticized into tragedy-porn. Fathoms are a medical fact; the story's job is what the characters *do* with the fact.
4. **Factions don't pause for love.** The org chart is the chaperone. A partner's handler is always in the room.
5. **Family is the commitment ceremony.** Bringing someone to the every-other-Sunday dinner in Willowmere outranks any declaration. Eleanor's *Are you eating properly?* directed at a partner is the novel's "I love you."
6. **Arthur's weakness applies here too.** He doesn't get to be suave, rich, or powerful in romance. His romantic assets are the same as his survival assets: attention, memory, honesty, and showing up for the night shift. Anyone who loves him loves *that* â€” or it's not love, it's plot.

Additional structural facts (from Â§32.1): the schedule problem (22:00â€“06:00; inverted calendar); the Tuesday problem (Loud/Quiet cognitive asymmetry); the Attuned clock (Erosion arithmetic, Census-monitored registered relationships); faction loyalty as the third party in every relationship; Reed family texture (Willowmere dinners, *New Year* audit, 1K economics).

---

## 1. Arthur Reed  â€” CHAR-001

**Age:** 24 (b. 14 March 2000). **Gender:** male. **Pronouns:** he/him.
**Personality:** Meticulous, dry-humored, conflict-avoidant but stubborn about facts. A clerk's epistemology: *if it's not in the file it didn't happen, and he keeps files.* Kind in the specific way of people who work nights â€” he remembers the cleaning staff's names. Brave the way clerks are brave: he will not run, he will *document*. Professional deformation: he believes understanding a thing is the same as surviving it.
**Worldview:** The hidden world is weather â€” survive it, file around it, never be interesting. Institutions read files; therefore stay unfiled. He cannot afford a police file, a hospital file, or a Census file, because every file is read by someone.
**Social position:** Economically modest, socially unremarkable British citizen. No famous family, no bloodline, no connections that matter. "Unremarkable by design and by nature."
**Occupation:** Night-shift records/archive clerk (22:00â€“06:00), NQA Ravenhurst branch records archive (B2â€“B3), CORP-011. Regular employee. ~Â£230,000/month; 1K apartment in Willowmere, Â£48,000/month.
**Faction:** None formally. Adjacent: NQA (employer), Night Clerks Ravenhurst cell (IND-004, futsal + Discord â€” "the first people who have a name for what he is"), the Ravenhurst Loud circle via Yusuf's bridge. Loud, not Attuned. Holder of ANOMALY-001 (the Laggard) since March 2017 (Yusuf Hidayat died beside seventeen-year-old Arthur; proximity + Loudness, not choice). Zero Fathoms.
**Goals:** Stay uninteresting; keep the archive job; understand the anomaly well enough to survive it; protect the people adjacent to him by keeping them out of files. Long-term: undefined â€” he has no five-year plan, which every candidate partner notices.
**Fears:** Being filed; being read (the mirror beat â€” "the day someone else mentions the mirror is the day he knows he's been read"); curiosity that spends him (institutional interest = experiments = the ratchet); costing the people who love him (the inherited guilt economy: his mother's *cleansing ritual*, "the guilt changed everything").
**Values:** Honesty, attention, memory, showing up. Never exploits asymmetric knowledge. Deploys his dangerous asset (the escrow) defensively, for disclosure, never as coercion.
**Relationship history:** Single. Has dated; "the Laggard ends dates early" â€” dim rooms, flickering lights, cold drift, dying plants. Mother asks *Are you seeing anyone?* every other Sunday; the answer is treated as possibly-changed.
**Emotional needs:** To be known without being filed. Parallel presence â€” someone simply *there* at 03:00. A shared memory no one edits.
**Emotional boundaries:** Will not perform suaveness; will not bend what he remembers to comfort someone; will not create a file on a partner; will not ask anyone to pay the anomaly's cost. The mirror is the one room he keeps even from the closest friend.
**Trust patterns:** Trusts showing-up without agenda (SaitÅ, Okada, the Night Clerks); treats ordinariness as a credential; mirrors trust for trust (protects by *not* filing â€” the mirror beat is his template). Distrusts filing, institutional curiosity, being read.
**Attraction triggers:** Sustained low-stakes attention; someone who treats his margins as a life's work; shared unedited memory; honesty under pressure; ordinariness chosen deliberately.
**Attraction blockers:** Performative charm (he can't parse it â€” "professionally unequipped to parse" romantic interest); anyone who would create a file on him (handler, Census registration); curiosity that spends him; being surveilled as a condition of intimacy.
**Compatibility factors:** Inverted schedule overlap; comfort with cheap, public dating geography (convenience store/family restaurant); willingness to meet the family gauntlet; respect for the archive ethics (anti-deception; the Veil-immune witness stance).
**Incompatibility factors:** Need for conventional dates/privacy (the 1K forbids it); need to be the interesting one (he performs normalcy); institutional loyalty that requires filing him; inability to tolerate the Tuesday asymmetry (for Quiet partners) or the Erosion arithmetic (for Attuned partners).
**Relationship risks:** He absorbs cost pre-emptively (ends things early, arrives late, leaves early); studies the relationship instead of risking it (archivist's deformation); carries the Tuesday asymmetry alone rather than burdening a Quiet partner; withholds the mirror even inside full trust.
**Relationship leverage:** His memory (retention of small detail as devotion); his honesty (never exploits what he knows); his showing-up (recurrence as care); the escrow (mutually assured disclosure â€” seizing him costs more than bargaining).
**Secrets:** The mirror/smilÂ­ing reflection (SECRET-005 â€” told no one, not even SaitÅ); the ratchet's private measurements (SECRET-003 â€” "the series' clock"); the escrow's construction (SECRET-013, P2 build); the entity at the tether's end (L5-2, unknown to him too â€” "felt looked-at; no word for it").
**Information asymmetry (general):** He knows every strange thing he has ever seen in complete detail; no institution knows he knows this much. Every partner knows less about the hidden world than he does â€” except Pram (knows the journals' content) and Kira (reads Tide-marks). The Census, the Desk, the Compact all model him; all models are incomplete.
**Potential relationship dynamics:** Courtship by repeated low-stakes proximity â†’ accumulated attention â†’ trust shown by shared files â†’ the family dinner as commitment â†’ post-commitment negotiation of the specific structural tension (Tuesday/Erosion/seam/fieldwork/shared-memory).

---

## 2. Configuration A â€” Nadia Rahma â€” CHAR-016

**Age:** 25. **Gender:** female.
**Personality:** Kind, funny, relentlessly normal â€” "the most radical thing in Arthur's life." Recites her five-year plan like a prayer. Professional, unflappable at the claims desk; privately homesick in the specific way of people building a life in a country that files them by visa category.
**Worldview:** Plans are how you stay a person inside a system that files you. Ordinary life is not default â€” it is *chosen*, daily, against the machine.
**Social position:** Indonesian migrant on SSW visa, two years into a five-year plan. NQA Ravenhurst claims adjuster, day shift overlapping Arthur's nights by two hours. Quiet. Economically adjacent to Arthur (similar class), culturally an outsider-insider.
**Occupation:** Claims adjuster, NQA Ravenhurst (CORP-011). Processes Arthur's incident reports.
**Faction:** NQA (employer). No hidden-world faction. Her "routine" adjustments' authorship is UNKNOWN (MYSTERY-012) â€” possibly NQA training, possibly Quiet Desk procedure, possibly emergent pipeline incentives.
**Goals:** Complete the five-year plan; renew/upgrade status; build a chosen life in Ravenhurst; send money home; be *someone* rather than a visa category.
**Fears:** Visa non-renewal; being a burden; the "weird dreams" she can't explain; learning what her hands have actually done at work.
**Values:** Normalcy, diligence, chosen belonging, honesty in small things.
**Relationship history:** Canon-unspecified beyond the present. No established prior relationships â€” the audit records this as UNKNOWN, not as "none."
**Emotional needs:** To be seen as a person making a choice, not a symbol of normalcy; to have her five-year plan treated as real; laughter that isn't about the strange days.
**Emotional boundaries:** Will not be pitied for the visa; will not be a project; will not tolerate being handled â€” by Arthur, by NQA, by anyone.
**Trust patterns:** Trusts routine and paperwork (her world runs on filed forms); trusts people who show up in the overlap window; slow to trust institutions after learning what the pipeline does.
**Attraction triggers:** Attention that remembers small things; someone who treats her plan as serious; dawn-convenience store consistency; dry humor that doesn't punch down.
**Attraction blockers:** Pity; being treated as "the normal one" (a role, not a person); secrecy that feels like the pipeline's secrecy; anyone who knows her forgotten days and uses it.
**Compatibility factors (with Arthur):** Same employer, overlapping shifts (two hours â€” the only window); same class; shared convenience store geography; his memory-honesty matches her paperwork-honesty; both chose Ravenhurst (his by birth-default, hers by decision â€” the city as decision, not default).
**Incompatibility factors:** The Tuesday problem â€” structural and permanent; his inverted absence vs her day-shift life; her forgetting makes every shared strange day his alone; the ethics of the asymmetry are unanswered.
**Relationship risks:** He carries the asymmetry alone (guilt); she is unknowingly part of the machine that edits him (her softened filings); the leak (CG-041) turns her handled files into a catastrophe; mole-hunt atmosphere (CG-044) makes her routine look deliberate.
**Relationship leverage:** She processes the pipeline â€” she can show him the routine manual and its revision history; her ordinariness is the one thing the hidden world can't price; "briefly, partially, through *his* files" â€” her remembering is the final revelation.
**Secrets:** None she keeps deliberately â€” she is Quiet; forgetting is not hiding. The *world* hides from her: the pipeline's editing behavior, the analytics flags, what her adjustments removed, the second leak (MYSTERY-055).
**Information asymmetry:** He knows her forgotten days; she knows nothing of the hidden world until the leak; both falsely believe her adjustments are neutral routine and that ordinary paperwork is safe; neither knows the routine's authorship or who sent the cache.
**Potential relationship dynamics:** Melon pan â†’ dawn convenience store â†’ file-sharing trust beat (he shows his files; she shows the manual + revision history) â†’ the Wednesday catastrophe (leak: she learns what she handled) â†’ trust â†’ conflict â†’ deeper understanding â†’ her choice with remembering â†’ the family dinner (post-revelation only â€” committing before she knows what she handled would violate Rule 1).

---

## 3. Configuration B â€” Kirana "Kira" Maheswari â€” CHAR-033

**Age:** 28 (b. 1996). **Gender:** female.
**Personality:** Professional empathy, personal exhaustion. Precise â€” Lanterns feel their Fathoms "the way others feel weather." Dry about her own arithmetic; refuses sentimentality about the clock. Curious in the way of someone whose profession is reading rooms.
**Worldview:** Everything leaves marks; the kindest thing is to read them accurately. The clock is a fact, not a tragedy â€” what matters is what you do with the remaining time.
**Social position:** Freelance Quiet-care counselor based in Ravenhurst (see [ROMANCE PATCH] â€” corrected from a stale "Liwanag-based" line in 21_CITIES.md). Meridian Institute (RES-001) stringer. T2 Lantern. 31 Fathoms and counting. Economically precarious-freelance; professionally respected in Quiet-care circles.
**Occupation:** Quiet-care counselor (freelance); Institute stringer (longitudinal observation).
**Faction:** Meridian Institute (RES-001) â€” employer with a data interest in Arthur's anomaly (zero-Erosion longitudinal subject; "Nwosu's dream subject"). The ethics triangle: her ethics vs. her employer's interest vs. her feelings.
**Goals:** Do the counseling work well; manage her Fathoms honestly; keep the stringer income without letting it become experimentation; understand what the Tide-marks of a tether actually show.
**Fears:** Becoming a case file to herself; the Institute crossing from observation to experimentation; wanting a patient/client to stop channeling and not knowing whether that's love or control.
**Values:** Accurate reading; consent; professional boundaries; the medical-fact stance toward Erosion.
**Relationship history:** Canon-unspecified. Professional intimacy is her native register; personal history is UNKNOWN (recorded, not invented).
**Emotional needs:** To be known as a person, not read as a room; restraint from someone who *could* know everything (Arthur's memory is total â€” he could be the watcher, and chooses not to be); someone for whom her Fathoms are a fact, not a countdown to grieve.
**Emotional boundaries:** Will not be aestheticized (Rule 3); will not have her readings treated as surveillance; will not let the Institute's interest become the relationship's terms; will not be "saved" from channeling â€” the stop-channeling question stays hers.
**Trust patterns:** Trusts precise people; trusts restraint (what someone chooses *not* to read); distrusts institutional appetite; distrusts being managed as a tragedy.
**Attraction triggers:** Someone who doesn't flinch at the arithmetic; who treats her readings as a sense, not a superpower; who has his own memory-discipline (a fellow professional of memory); honesty about costs.
**Attraction blockers:** Tragedy framing; being read without consent; the Institute's data hunger wearing a lover's face; anyone who wants her to stop channeling *for them*.
**Compatibility factors (with Arthur):** Two professionals of memory â€” his perfect, hers borrowed from rooms; both understand costs as arithmetic; both work the same city; his honesty-discipline matches her consent-discipline; "learning what it means to be known *completely* and loved anyway."
**Incompatibility factors:** No privacy â€” she reads Tide-marks; his rooms, routines, shadow's history are legible; his secrecy-as-safety collides with her legibility; the Erosion arithmetic (every year together is measurably less of them); Census-monitored registered relationship; her employer's interest in him as data.
**Relationship risks:** Observation spending him (the ratchet â€” no neutral instrument pointed at the Laggard); the consent line on Tide-mark reading; the triangle resolving toward the Institute; his fear of being read meeting her inability not to read.
**Relationship leverage:** She may be the first living person to *see* what Ilsa saw (the Laggard's Tide-marks); her restraint is the trust currency (what she *doesn't* report); her precision about her own Fathoms models honest cost-accounting for him.
**Secrets:** The triangle's upstream â€” what she has already reported, what she held back; her precise Fathom trajectory; whether she has read marks he asked her not to read.
**Information asymmetry:** She knows far more than he volunteers (Tide-marks); he knows the mirror (she doesn't â€” or her sense might catch it; canon keeps the overlap unestablished); both falsely believe the Institute's interest is neutral observation and that her readings give her the truth of him (marks, not interior); neither knows the entity, the ratchet's end, or what Nwosu's suppressed paper showed.
**Potential relationship dynamics:** Professional contact (counseling adjacent) â†’ the arithmetic stated plainly upfront (the premise, not the reveal) â†’ "known completely" beat after the tether reveal (P2) â†’ the triangle's pressure (Institute's shadow, ch. ~200â€“300) â†’ her choice: the person over the data (refusing a collection, redacting a report, resigning the stringer role) â†’ post-choice negotiation of the clock as fact.

---

## 4. Configuration C â€” Aisha Rahman â€” CHAR-034

**Age:** 36 (b. 1988). **Gender:** female.
**Personality:** Divorced, dry, competent. Has buried two teams and one marriage, in that order. Professional warmth kept behind procedure; humor as armor; decisive under fire; tired in the way of people who clean up after the world.
**Worldview:** The system prices everything; the only honest move is to know the price and choose anyway. Protection is never free â€” "her protection is itself the compromise."
**Social position:** GOV-006-contracted (SMD) Sweeper team leader in Ravenhurst. Filipina-Muslim, Mindanaoan â€” formerly KNF Liwanag Sweeper lead, recruited to the SMD in 2023. Dual-hatted by design: Ravenhurst warrant is SMD; staging from Kalsada's van yard in Liwanag she operates under KNF contract authority â€” a liaison seam between the two bureaus. Senior to Arthur by 12 years and by institutional weight.
**Occupation:** Sweeper team leader (supernatural cleanup/containment).
**Faction:** SMD (GOV-006) contract; KNF liaison seam. Fraternization rules apply. Her unfiled follow-ups are protocol breaches; under CG-044's absorption they "read as treason to *both* sides."
**Goals:** Keep her team alive; manage the seam without being eaten by it; decide what to do with the witness she can't Veil-edit; survive the mole hunt with her people intact.
**Fears:** Burying a third team; the treason reading becoming real; the Desk using her as the recruitment lever; becoming the handler she refuses to be.
**Values:** Professional competence; the breach as proof (she *doesn't* file â€” that is the evidence of her); loyalty to the living over the org chart; respect first.
**Relationship history:** Divorced â€” one marriage buried (canon). The marriage's details are UNKNOWN (recorded, not invented). The divorce is load-bearing: she knows what it costs to choose wrong, and what it costs to stay.
**Emotional needs:** Respect without flattery; someone who understands the compromise without needing it explained; a relationship that isn't another operation.
**Emotional boundaries:** Will not be the handler (RH-024 disproved: "a handler would file; Aisha *breaches*"); will not let competence read maternal; will not let interest read as flattery; will not file the follow-up â€” the line she has drawn.
**Trust patterns:** Trusts professional respect first ("two professionals on opposite sides of the same incident tape â€” respect first, everything else negotiated under fire"); trusts people who understand price; distrusts the org chart's reading of her; distrusts being managed.
**Attraction triggers:** Competence under pressure; honesty about costs; someone who recognizes the breach for what it is (Arthur's mirror-beat ethics mirrored); dry humor that survives the job.
**Attraction blockers:** Being handled; being idealized as the protector; anyone who needs her to file â€” or not file â€” *for them*; the 36/24 register tipping into maternal or into flattery.
**Compatibility factors (with Arthur):** Mutual professional respect; shared incident-tape literacy; his archive ethics (protection by not filing) mirrors hers; both understand price; cross-cultural directness (Mindanao/Willowmere â€” both families ask unanswerable questions).
**Incompatibility factors:** 12-year age and institutional seniority gap â€” the power imbalance is real and must be negotiated, never erased; every date is a conflict of interest; every shared file is a protocol breach; her job includes deciding what to do with witnesses like him; the dual-hat seam; the treason reading.
**Relationship risks:** Institutional â€” the break is the org chart's, not the heart's (she files the follow-up under pressure; the Desk uses the relationship as the recruitment lever; the seam forces a choice and she chooses the bureau). The mole hunt's atmosphere. The recruitment pitch (MYSTERY-008, ch. ~300â€“400): "handler, leash, Census file â€” the golden handcuffs, personalized."
**Relationship leverage:** She is the Desk's instrument and its breach simultaneously â€” she can choose; the compromise's origin (what she filed before she started protecting him â€” MYSTERY-020's candidate) is the trust deep-beat; her resignation of the seam is the priced third burial.
**Secrets:** The full count and content of her unfiled follow-ups; the KNF-side pressures on the seam; that fraternization itself is the breach â€” she cannot disclose the relationship without incriminating them both.
**Information asymmetry:** She knows the standing case file (him); he learns the compromise mid-arc (ch. ~150â€“220); both falsely believe the thin file means thin attention (M-03: thinness is camouflage) and that her protection makes him safer; neither knows the Desk's actual plan (MYSTERY-008), the hiring approver (MYSTERY-005), or the 2023 monitor's outcome (MYSTERY-084).
**Potential relationship dynamics:** Professional contact (EVENT-092: she learns his name from the replay report) â†’ respect-first working proximity â†’ the compromise realized (he learns she keeps not filing) â†’ the seam's pressure (CG-044 absorption) â†’ the hiring answer reframes the Desk (MYSTERY-005, ch. ~250â€“350) â†’ the recruitment pitch (MYSTERY-008, ch. ~300â€“400) â†’ her choice: the file, the pitch, or the seam â€” at professional cost â†’ post-choice: what a relationship looks like after the org chart has priced it.

---

## 5. Configuration D â€” Pramudya "Pram" Nugroho â€” CHAR-032

**Age:** 31 (b. 1993). **Gender:** male.
**Personality:** Charm as camouflage; curiosity as appetite. Genuinely warm; genuinely reporting to people who see Arthur as a survey instrument. Professional, precise, devastating when the betrayal comes â€” "professional, precise, and devastating" is the canon promise.
**Worldview:** The unmappable wants mapping; the price of the map is the work. Institutions price everything â€” the question is whether you say the price out loud.
**Social position:** Cartographers' Exchange (SUP-002) field mapper, SE Asia circuit â€” reassigned to Ravenhurst (EVENT-100), arriving September 2024. T2 Hollow. The Exchange is "the oldest continuously operating hidden-world institution."
**Occupation:** Field mapper (supernatural cartography).
**Faction:** Cartographers' Exchange (SUP-002). His institution wants to *map* the Laggard â€” experiments, the ratchet, *spending Arthur*. The journals are disputed property (Exchange claims ownership; Archivists and Red Ledger contest the page â€” CG-048).
**Goals:** Continue Ilsa's work; map the tether; serve the Exchange â€” and, in tension, tell Arthur the truth about the choosing ("the question isn't whether Pram would choose Arthur over the Exchange â€” it's whether he'd *tell* Arthur he's choosing").
**Fears:** Repeating Ilsa's cost without her clarity; the Exchange's second price ("the one not in the contract" â€” MYSTERY-051); becoming the instrument that spends someone he likes.
**Values:** Curiosity; honesty about price; the archive as shared ground; choosing out loud.
**Relationship history:** Canon-unspecified. Professional charm is his native register; personal history UNKNOWN (recorded, not invented).
**Emotional needs:** To be chosen back by someone who knows the price; a shared obsession that isn't only fieldwork; to be told â€” and to tell â€” plainly.
**Emotional boundaries:** Will not lie about the choosing (the canon question is disclosure, not defection); will not let the archive do the relationship's emotional work (the Ilsa-journal intimacy shortcut is a flagged watch); will not pretend the Exchange's interest is neutral.
**Trust patterns:** Trusts fellow mappers of the unmappable; trusts people who read the margins honestly; distrusts institutional sentimentality; distrusts his own charm as a credential.
**Attraction triggers:** Shared obsession (two people who map the unmappable); marginal honesty (field notes, not just Ilsa's); someone who sets terms (Arthur authenticating the torn page â€” "only a holder can confirm it... He sets the terms").
**Attraction blockers:** Being mapped as a subject; the Exchange's ownership claim on the journals; fieldwork disguised as kindness; the second price.
**Compatibility factors (with Arthur):** The slow burn of shared obsession; courtship by archive (reading Ilsa's journals together); both live in margins and field notes; Arthur's clerk's-eye on the mapper's fieldwork is a genuine meeting of methods.
**Incompatibility factors:** Every kindness is also fieldwork; the institution wants experiments (the ratchet); the journals are disputed property; the betrayal is *scheduled* ("when it comes"); the missing page sits under every reading-together session.
**Relationship risks:** The professional betrayal â€” precise, devastating; the Exchange asserting journal ownership mid-relationship; the handwriting check (SECRET-024) landing wrong (a contemporary hand); delivery to the Second Silence Auction (CG-048) as the Exchange's lot.
**Relationship leverage:** The journals â€” "the most intimate gift possible: the previous holders' interior lives"; his disclosure (the telling); defection from the mapping assignment at cost; resolving the custody contest in Arthur's favor.
**Secrets:** What he reports to the Exchange; what the Exchange ordered about Arthur; whether his reassignment was his finding or his posting (who sent him, with what brief); the Exchange's valuation of the Laggard (the buyer inquiry, EVENT-093).
**Information asymmetry:** He arrives knowing more about Arthur's *condition* than Arthur knows himself (the journals); Arthur knows the mirror (Pram doesn't â€” though the journals document Ilsa's sightings; whether Pram has read that entry is unestablished); both falsely believe the journals are the complete record (one page missing) and that continuing Ilsa's work is neutral scholarship; neither knows the torn page's contents, who tore it, or the ratchet's end.
**Potential relationship dynamics:** Arrival with the journals (ch. ~60â€“100 â€” the relationship starts on a missing page) â†’ courtship by archive â†’ the tether reveal via the journals (ch. ~150â€“250; the reader learns with Arthur) â†’ the handwriting tripwire (ch. ~200â€“300) â†’ the auction arc (ch. ~250â€“350; C-02: not shared with the buyer's auction) â†’ the scheduled betrayal (professional, precise, devastating) â†’ the telling â†’ Arthur's authentication of the page (ch. ~350â€“450) â†’ post-betrayal: what remains when the archive is priced.

---

## 6. Configuration E â€” Samuel Brooks (æ–Žè—¤ æ‚ æ–—) â€” CHAR-015

**Age:** 26. **Gender:** male.
**Personality:** Ordinary, dry, loyal. The only person at work who *remembers*. Treats what they know as a *tool* â€” wants to test what two Loud clerks can get away with â€” while Arthur treats it as weather. Curiosity that looks like recklessness to Arthur.
**Worldview:** Knowledge is for using. Two Loud people in one records room is an opportunity, not just a condition. (Arthur's counter-doctrine: survive it, file around it, never be interesting.)
**Social position:** Night-shift records clerk, NQA Ravenhurst, two desks over from Arthur. Also Loud (unacknowledged â€” "though neither of them has a word for it"). Quiet-adjacent civilian. Arthur's closest friend.
**Occupation:** Records clerk (night shift), NQA Ravenhurst (CORP-011).
**Faction:** None. Adjacent to every leak Arthur touches. (Per the Phase-3 charpatch ruling and [ROMANCE PATCH] in this audit: the Static Hour contact beat was Bayu-specific and NOT transferred â€” the Lantern Bearers' cache is anonymous per EVENT-097; SaitÅ's leak adjacency is ambient, not sourced.)
**Goals:** Test what two Loud clerks can get away with; be the person who doesn't need the performance; keep the night shift's private history intact.
**Fears:** Being filed ("being seen is what gets you filed"); the demographers' flag; losing the one person who remembers; his curiosity getting Arthur noticed.
**Values:** Loyalty; the shared unedited memory; honesty without performance; curiosity.
**Relationship history:** Canon-unspecified beyond the friendship. The friendship *is* the history â€” years of shared glances at wrong files.
**Emotional needs:** To be met without the normalcy performance; a shared memory no one edits; someone who takes the curiosity seriously instead of filing it under recklessness.
**Emotional boundaries:** Will not be managed into Arthur's weather-doctrine; will not have the friendship filed; will not accept the demographers' theory of them (the Court is wrong â€” RH-026).
**Trust patterns:** Trusts the shared memory absolutely ("a private history, complete and unedited"); trusts noticing; distrusts the weather-stance as a life; distrusts institutions' reading of the two-desk anomaly.
**Attraction triggers:** Being fully seen (Arthur doesn't perform around him â€” "the rarest thing Arthur owns"); shared noticing (the shadow's behaviors); choosing a doctrine *together*.
**Attraction blockers:** The curiosity/recklessness fault line; the blast radius (loving him means sharing it); the mirror â€” the one performance Arthur maintains even here.
**Compatibility factors (with Arthur):** Inverted schedule (both live it); the only fully-shared memory in Arthur's life; no performance needed; both clerks â€” same methods, same margins; the friendship is pre-built trust.
**Incompatibility factors:** Tool vs weather â€” the fundamental doctrinal split; his testing impulses are the relationship's risk vector; the Court's demographers *will* flag two Louds one desk apart (MYSTERY-010, ch. ~200â€“280); the mirror sits inside the only honest relationship as the one lie.
**Relationship risks:** His testing gets them noticed (the demographers' flag landing by his hand); his leak adjacency puts a price on Arthur's head (CG-041's blast radius); the mirror's discovery reading as the one lie inside the only honest relationship.
**Relationship leverage:** The shared memory itself; mutual disclosure (the mirror told â€” Arthur's hardest disclosure); a jointly chosen doctrine (testing-stance vs weather-stance, resolved not shelved).
**Secrets:** The extent of his testing (what he has tried); what he has told the Lantern Bearers, if anything (ambient adjacency, not sourced contact); his reading of Arthur's hiding.
**Information asymmetry:** He knows the shadow's behaviors Arthur hides (observed, not told); Arthur knows the mirror (told no one â€” SECRET-005's tripwire is sharpest here); both falsely believe two Louds staying quiet is safe and that the night shift is cover; neither knows the tether's nature (until P2), the hiring approver, or what SaitÅ's Loudness is adjacent to (MYSTERY-087 â€” OPEN).
**Potential relationship dynamics:** Pre-built friendship (P1) â†’ the risk reveal scheduled (demographers' flag ch. ~200â€“280; leak ch. ~150â€“220) â†’ the doctrinal argument (tool vs weather) â†’ the mirror tripwire (ch. ~300â€“400: "the day someone else mentions the mirror") â†’ disclosure as defusal (telling SaitÅ *at* the tripwire) â†’ post-disclosure: the only fully-shared memory, finally complete â€” and what two Louds do with it.

---

## 7. NO ROMANTIC FUNCTION â€” the remaining 31 characters

Explicitly marked per audit Â§2. None of these is a love interest; each has independent reasons to exist (see AUDIT/ROMANCE_ARCHITECTURE_AUDIT.md Â§9â€“10).

| ID | Name | One-line reason |
|---|---|---|
| CHAR-002 | Director Elena Voss | World-level official (BTA, GOV-001); no Ravenhurst presence |
| CHAR-003 | Commissioner Zhao Mingde | World-level official (Jade Office, GOV-002); no Ravenhurst presence |
| CHAR-004 | General Arkady Volkov | World-level official (Dept 12, GOV-003); no Ravenhurst presence |
| CHAR-005 | Director-General Ratna Kusuma | World-level official (BPF, GOV-004); institutional, not personal |
| CHAR-006 | Bureau Chief Ri Kang-dae | World-level official (Simjo-guk, GOV-012); no Ravenhurst presence |
| CHAR-007 | Monsignor Aldo Ferretti | World-level official (OEP, GOV-010); no Ravenhurst presence |
| CHAR-008 | Secretary-General Fatoumata Diallo | World-level official (Compact, INTL-001); no Ravenhurst presence |
| CHAR-009 | Adaeze Okonkwo | Confirmed Worldtide (T6); Compact observation subject, Geneva â€” cosmological figure |
| CHAR-010 | TomÃ¡s Aquino Reyes | Confirmed Worldtide (T6); Compact observation subject, Manila â€” cosmological figure |
| CHAR-011 | Hana Shirakawa | Confirmed Worldtide (T6); Compact observation subject, Hokkaido â€” cosmological figure |
| CHAR-012 | Hannah Reed | Arthur's younger sister, 22 â€” familial register only; romantic framing would be inappropriate |
| CHAR-013 | Thomas Reed | Arthur's father, 58 â€” familial register only |
| CHAR-014 | Eleanor Reed | Arthur's mother, 55 â€” familial register only |
| CHAR-017 | AKP Larasati "Laras" Prameswari | BPF field investigator; professional register â€” mole-hunt engine, not romantic |
| CHAR-018 | Yusuf Hidayat (1951â€“2017) | Deceased; previous ANOMALY-001 holder â€” inheritance chain, not romance |
| CHAR-019 | Ilsa Brandt (1962â€“1996, missing) | Missing; previous holder â€” journals' author, not a living romantic subject |
| CHAR-020 | Eleanor Vance (1903â€“1971) | Historical figure; Accords architect |
| CHAR-021 | Dr. Leonid Kulik (1883â€“1942) | Historical figure; Tunguska report |
| CHAR-022 | Miriam "Mother Mercy" Adler (1928â€“1971) | Historical figure; Choir founder |
| CHAR-023 | Emil Sorensen (1922â€“1988) | Historical figure; Quiet Night SG |
| CHAR-024 | Lena Hoffmann (b. 1961) | Investigator with own legacy (Rhine Drowning inquiry); no Ravenhurst presence |
| CHAR-025 | Vivienne Ashworth (b. 1948) | Pale Court dynast; antagonist register â€” the buyer's fury, not romance |
| CHAR-026 | Hendra "Bos Naga" Gunawan (b. 1975) | Criminal operational head; succession-war engine â€” antagonist register |
| CHAR-027 | "The Factor" | Senior Red Ledger broker; antagonist register â€” name unrecorded by design |
| CHAR-028 | June Park (b. 1985) | Leak journalist; Loud â€” professional register (the leak's vector, not a partner) |
| CHAR-029 | Silas Crane (b. 1970) | Hollow diver, terminal (82 Fathoms); objectively stronger than Arthur â€” warning figure |
| CHAR-030 | Reverend Amos Kade (b. 1968) | Prophet-antagonist (Ninth Bell); Loud â€” ideological register |
| CHAR-031 | Dr. Amara Nwosu (b. 1978) | Erosion researcher; clinical register â€” 48/24 age-power dynamic makes romance inappropriate; needs non-Arthur subjects (independence watch) |
| CHAR-035 | Agus Hidayat (1955â€“1977) | Deceased; Yusuf's brother â€” Quiet Night casualty |
| CHAR-036 | Clara Whitmore (47) | Night-shift section chief; maternal-professional register â€” "kind boss" drift guarded |
| CHAR-037 | Henry Lawson (34) | Senior clerk, dry mentor; professional register |

---

## 8. Compatibility classifications (summary â€” full reasoning in AUDIT Â§4)

No rankings. No "best girl" lists. The five configurations are *alternatives*, not concurrent rivals â€” the novel chooses among structural tensions, not among people.

| Pair | Classification | One-line reason |
|---|---|---|
| Arthur Ã— Nadia (A) | HIGH POTENTIAL | Structural tension is the setting's central romantic question (the Tuesday problem); both choose ordinariness; trust engine is fully staged by canon mysteries |
| Arthur Ã— Kira (B) | DIFFICULT BUT INTERESTING | "Known completely and loved anyway" vs. no-privacy collision with his secrecy-as-safety; the clock is priced in; the triangle must resolve by her agency |
| Arthur Ã— Aisha (C) | DIFFICULT BUT INTERESTING | Respect-first professionals; the 36/24 register and every-date-is-a-breach must be negotiated, never erased; the break is institutional |
| Arthur Ã— Pram (D) | POSSIBLE | Courtship by archive is genuine; but "every kindness is also fieldwork" and the betrayal is scheduled â€” the relationship's meaning must be earned past it |
| Arthur Ã— SaitÅ (E) | POSSIBLE | The only fully-shared memory; but tool-vs-weather is a real doctrinal split and the blast radius is shared â€” friendship-to-romance must cross the mirror |

---

## 9. Structural constraints on all configurations

- **Surveillance gradient:** the five configs are five different surveillance postures â€” B fully Census-monitored; C via government-contract status; A via the SMD's SSW Threshold-adjacency watchlist (claims processing is a watched tier); D via Hollow-discipline monitoring; E structurally invisible to the Census ("the Loud aren't Census subjects at all") and visible only through NQA's employer files. Rule 4 fires at different strengths per config â€” recorded, not a contradiction.
- **Age registers:** A 25/24 (peer); B 28/24 (near-peer); D 31/24 (senior-by-experience, peer-by-vulnerability); E 26/24 (peer); C 36/24 (senior â€” the imbalance is real; the audit requires it negotiated, never erased, never maternal, never flattery).
- **The dinner rule:** no configuration reaches commitment without the Willowmere gauntlet (Rule 5). For A, the dinner belongs after the final revelation; for B, after the triangle resolves; for C, after the seam is priced; for D, after the telling; for E, after the mirror.
- **Information-economy coupling:** every configuration's trust engine is gated by mystery reveal order (see AUDIT Â§6, Â§16). Romance beats cannot land before their evidence exists.
- **Failure is allowed:** any configuration may fail naturally, remain friendship, or go unrequited â€” the audit's failure test (Â§18 of the audit report) keeps all five honest.


---

## SECTION: `DATABASE/POWER_PROGRESSION.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `DATABASE/POWER_PROGRESSION.md` Â· sha256 `950826063cab061eade6b6389b7695e055eb7ce6cf3ce29ad52ba529592ce1f0` Â· 7,224 words. No content changed.

# DATABASE â€” Power Progression (THE QUIET TIDE)

> Power-progression audit database, v1.6 (2026-09-20). Companion to the mystery architecture
> (`DATABASE/MYSTERIES.md`, `DATABASE/INFORMATION_KNOWLEDGE_MAP.md`). This file documents the
> power ecosystem **as canon establishes it** â€” what exists, what it costs, what limits it, what
> counters it. It does not invent mechanics. Anything canon does not establish is marked UNKNOWN.
>
> Canon-status key: **CANON-LOCKED** (foundational; change requires CHANGELOG entry) Â· **CANON**
> (established fact) Â· **PROVISIONAL** (re-audited each cycle) Â· **THEORY** (in-world belief or
> doctrine position; load-bearing for policy, not truth) Â· **IN-WORLD MISCONCEPTION** (believed by
> characters, false) Â· **UNKNOWN** (not established; author-level intentional mystery where noted).

---

## A. Power categories

| Category | Definition | Canon status |
|---|---|---|
| **Resonance (channeling)** | Deliberate channeling of Undertow pressure through the Hollow Pattern by an Awakened Attuned. Willed intrusion; priced in Fathoms. | CANON (03, 04) |
| **Anomaly (Seep) Rules** | Fixed, alien-but-discoverable Rules executed by Seeps (object / place / organism / event / information). Not willed; not priced in Fathoms â€” priced in Tide pressure, visibility, and containment cost. Anomaly Rules may exceed Attuned channeling caps; the excess is priced into the anomaly (02.I). | CANON (02, 03) |
| **The Laggard (ANOMALY-001)** | Neither Resonance nor ordinary Seep: a tether â€” the shadow cast in the Membrane by something standing in the Undertow at the holder's coordinates. Passive, always-on; "use" means reading, deepening, or entering it. The holder (Arthur) is not Attuned and accrues no Fathoms. | CANON (29 B.3, B.4) |
| **Technology** | Seismograph network, Tide-noise generators, Stillwater (drugs/aerosol), Anchor restraints/systems, warded architecture, Drowndust munitions, Lantern-sensitives/instruments, claims-ML, imagery stack. Mundane-engineered counters to channeling. | CANON (04.5, 13.3, 26, 27) |
| **Information** | Not a power, but the setting's scarcest resource (02.II: "Information is the scarce resource, not power"). Records, vectors, Tide-mark readings, Loud memory, clean recordings. Treated as a power category because it decides fights. | CANON (02.II) |
| **Institutions** | Law, bureaucracy, the Tribunal, licensing regimes, insurance, the Census. "Institutions are the apex predator of individuals" (30, Scenario 6). A power category because paperwork defeats T4s. | CANON (30) |
| **Folk heuristics** | Trial-and-error containment practices, often practically effective with wrong theories. The Compact archives them as phenomenological field reports. | CANON (03.2) |

---

## B. Anomaly categories

**By substrate** (03.3, CANON): Object Seeps (most common, most containable) Â· Place Seeps Â· Organism Seeps Â· Event Seeps Â· Information Seeps (rarest, most feared, hardest to contain â€” "you cannot put a fact in a vault").

**By Meridian Vector** (05, CANON): `MV-[THREAT T0â€“T7]/[CONTAINMENT Aâ€“E]-[FLAGS]/[RANGE]/[INTEL]`. Threat measures maximum demonstrated output equivalent (same T-scale as Attuned tiers, deliberately). Containment is orthogonal to Threat. Flags: I (infohazard), B (biohazard), P (psychohazard), R (reality distortion), M (memetic), V (vector/propagating). Range: Local â†’ Urban â†’ Regional â†’ Continental â†’ Global â†’ Memetic. Intel: None / Reactive / Sapient / Unknown (Unknown treated as Sapient for rules of engagement until disproven â€” the Sapient-presumption protocol, post-Oslo).

**Person-bound filing policy** (05.1, CANON): person-bound anomalies are filed C-A by default (the class describes the relationship, not the object); auditors read person-bound C-A as "contained for now, watched like it's loose."

---

## C. Ability types

### The Five Disciplines (04.2, CANON â€” discipline fixed at Awakening, never changes)

| Discipline | Domain | Weak â†’ strong | Regulation |
|---|---|---|---|
| **LANTERN** | Perception, information, memory | Sense Tide pressure â†’ read Tide-marks â†’ track a person by their "wake" | Lightest; staffs detection, forensics, journalism |
| **TIDE** | Matter and energy | Warm a cup â†’ shatter concrete â†’ (T5+) weather-scale events | Heavy; Tide combat licenses most restricted |
| **BONE** | Body and self | Accelerated healing â†’ physical augmentation â†’ (T5+) regeneration | Medical licensing; sports bans |
| **CHOIR** | Social influence, suggestion | Calm a room â†’ seed a suggestion â†’ (T4+) crowd-scale emotional steering | **Most regulated discipline on earth.** Unlicensed Choir use = prison in 140+ countries; Choir use in elections/referenda is an Accords/Tribunal offense |
| **HOLLOW** | Direct Undertow interfacing | Sense thin places â†’ briefly "wade" (partial phase) â†’ Slipping | Rarest (~3% of Attuned); monitored by every intelligence agency; most Hollow work state-monopolized |

### Named hard-capped abilities (02.I CANON-LOCKED; 04.6 CANON restatements)

- **Slipping (teleportation):** Hollow only; arrival requires recognition by another living person (not self/echo/recording); recognition decays; cost scales with distance/unfamiliarity; warded zones shred unrecognized arrivals; hardened wards shred all non-whitelisted arrivals. No combat-blinking across continents. Slip-courier chains economically dead (each link pays full Erosion cost; price compounds past cargo value within three hops).
- **Causal bubbles (time):** Attuned channeling only; line-of-sight scale, minutes at most, ruinous Erosion. No past alteration, ever. Anomaly Rules may sustain larger/longer bubbles, priced into the anomaly (visibility, pressure, containment).
- **Suggestion seeding (Choir):** no direct mind control (CANON-LOCKED); seeding plants impulses experienced as one's own thoughts; resisted by awareness, strong identity, training, stubbornness; always produces backlash (seeder experiences distorted echo of the implanted impulse); mass reliable mind control logistically impossible (per-link unreliability compounds geometrically).
- **Power copying/theft:** requires consuming the source's pattern during collapse (Drowning-adjacent window) â€” a stable living pattern cannot be taken; requires T3+ Lantern examiner; Seismograph-visible (reads as T4+ event); lawful only with consent or Tribunal warrant. The thief inherits the victim's accumulated Fathoms and the thief's own future accumulation rate doubles. Net loss, always. (Three corpses in Compact vaults prove why.)
- **Healing (Bone):** accelerates the body's own repair; cannot regrow what the pattern no longer "remembers" (old amputations fail); cannot cure Erosion; aggressive healing transfers Erosion-risk to the healer.
- **Matter creation:** borrowed matter reverts â‰¤72h (usually much sooner for complex structures). Conjured weapons work for a fight, not a war. Licensed conjuration contracting (temporary tooling) is a real regulated trade.
- **Resurrection:** impossible (CANON-LOCKED). Echoes are not people; they degrade.

### ANOMALY-001 â€” the twelve documented uses (29 B.11, CANON â€” discovery order = the novel's progression spine)

Each use discovered through observation, never granted by revelation; each paid per 29 B.6; each with a stated counter.

1. **Veil-immune witness** â€” the shadow records what the Membrane showed it; cross-checkable against Loud memory. Counter: proof without chain of custody is a story; the Tribunal doesn't accept shadow-testimony (yet).
2. **Reading the lag as a recording** â€” 3-second window replays his recent position. Counter: 3 seconds, his position only, requires stillness and a reflective surface.
3. **Anchor against memory alteration** â€” the shadow shows what his body actually did; defeats gaslighting/suggestion. Counter: anchors actions, not motives; a clever Choir operator works with that.
4. **Revealing Tide-marks** â€” the shadow darkens over old Tide-marks; a dowsing rod for history. Counter: Tide-marks are impressions, not video; interpretation must be learned.
5. **Stepping into the lag (3s out-of-phase)** â€” unseen, intangible, unable to act; moves normally through space but solid matter still blocks him ("intangible means no touch, not phasing"). Counter: 3 seconds; no interaction; Lantern-sensitives feel the wrongness; the entity notices.
6. **Deepening the lag (3s â†’ 3min â†’ 3h)** â€” Stillness-adjacent technique; 3 minutes reads a room's recent past; 3 hours was Ilsa's maximum ("it almost didn't give me back"). Counter: physiological cost, the ratchet, attention â€” at 3 hours, he was the one being observed.
7. **Shadow-storage** â€” at deep lag, small objects held out-of-phase. Rules: only what the shadow covers; nothing living; retrieve within the lag window or it's gone (partial corrupted return); each use lengthens the lag; capacity is roughly one night of record per session; covering more deepens the lag faster (capacity *is* the ratchet).
8. **Thin-place dowsing** â€” the shadow leans toward Tide pressure on its own. Counter: points at pressure, not safety.
9. **Unobserved observation (deep lag)** â€” at 3-minute lag, watch a room unseen. Counter: "at deep lag you are not the only observer" â€” the entity's attention, which is personal.
10. **The clean recording** â€” the shadow is Membrane-darkness, not Undertow-structured information, so recordings of the shadow do not rot. A provable, permanent, un-rottable record of a Seep. **Rot-immunity boundary (CANON):** immunity holds for replay at lag-depths up to ~3 hours and events up to T4-equivalent pressure; beyond that depth-pressure product, rot applies normally. The anchor degrades with depth (edge-corruption creeps inward as the ratchet climbs). Counter: possessing it makes him a target of every faction simultaneously; using it spends the masquerade itself.
11. **Erosion-free operation** â€” he is not Attuned; the anomaly does the work; he pays in attention-risk and ratchet, never Fathoms. Counter: his currencies are finite too â€” the ratchet only runs one way, and attention compounds.
12. **The long-shadow flare** â€” deliberately lengthening the lag to minutes; visible to every Lantern-sensitive for kilometers. A distress signal that can't be unfired. **Point of no return (CANON):** a flared holder's T1-curiosity cover identity is gone forever â€” no reinstatement, no re-filing, no quiet return to the records desk.

**Generative principle â€” Uses 13+ (29 B.11, CANON):** the twelve are the *documented* ladder, not the *complete* ladder. Any further use must be generated the same way: observe â†’ hypothesize â†’ test at the smallest falsifiable scale â†’ pay the cost. Never granted by revelation, never whispered by the entity, never free. A Use 13+ that skips a step is a continuity error, not a power-up.

---

## D. Existing strength classifications

**Tiers T0â€“T7 (04.3, 30.1, CANON):** Tier measures *maximum sustainable output* â€” not skill, not danger, not Erosion rate, not intelligence, not preparation.

| Tier | Name | Practical ceiling | Approx. global population |
|---|---|---|---|
| T0 | Quiet | Ordinary human capability â€” including killing an Attuned with a rifle | ~8 billion |
| T1 | Spark | Party tricks; inconvenient or minor utility | ~800,000 |
| T2 | Lantern | Professional-grade; the working class of the hidden world | ~90,000 |
| T3 | Surge | Decides a firefight or a boardroom; registered, watched | ~8,000 |
| T4 | Tempest | National asset/threat; Seismograph-visible | ~700 |
| T5 | Cataclysm | City-scale consequences; every use a geopolitical event | ~40 |
| T6 | Worldtide | Continental consequences; three confirmed alive (CHAR-009/010/011: Okonkwo, Reyes, Shirakawa) | 3 confirmed |
| T7 | Unknown | Reserved for "we don't know what that was" | 0 confirmed |

**Tier is not destiny in a fight (04.3, 30, CANON):** raw tier wins *unprepared* encounters; preparation is the great equalizer. A prepared T2 with knowledge, terrain, and the right countermeasure routinely survives â€” sometimes defeats â€” a T4. The seven mechanisms (30.3): Rule interference Â· preparation Â· terrain Â· Tide-noise Â· information advantage Â· Erosion attrition Â· social and legal constraints.

**What tier can't buy (30.1, hard limits, all tiers):** time (no past alteration) Â· minds (no direct mind control at any tier) Â· permanence (borrowed matter reverts at every tier) Â· self (no tier reverses Erosion, not even on oneself).

---

## E. Limitations

**Universal (CANON-LOCKED, 02.I):** no true resurrection Â· no permanent created matter (â‰¤72h reversion) Â· the past cannot be changed Â· no direct mind control Â· no power copying (except the Drowning-adjacent ritual, net loss) Â· patterns capturable only during collapse Â· Slipping has anchors (recognition by another living person; wards shred) Â· Erosion irreversible Â· causal bubbles small/brief/expensive.

**Discipline-fixed:** discipline fixed at Awakening; no one changes discipline; apparent versatility is clever application within one discipline (04.2).

**Laggard hard limits (29 B.5, CANON):** fixed to the holder's position (cannot be sent/lent/aimed) Â· cannot affect matter directly (a shadow; everything works by being read or entered) Â· base lag ~3s window; deeper costs (B.6) Â· grants records, not knowledge (misreading always possible) Â· out-of-phase: cannot act on the world (no touch/speech/contact), moves normally through space, solid matter blocks him Â· Lantern-sensitives and instruments see deep use (the flare cannot be unfired) Â· wards dampen Membrane-side effects but cannot sever the tether; deep use inside wards is louder at the entity's end Â· no protection except being unseen for seconds; a bullet still works.

**Anomaly-specific:** each catalogued anomaly's Rule is its own limitation (28_ANOMALIES.md); the Meridian Vector's Threat axis measures demonstrated output, not potential.

---

## F. Costs

**Erosion â€” Fathoms 0â€“100 (04.4, CANON):** output scales linearly; Erosion scales exponentially past ~40. Routine low-output work: ~0.005â€“0.02 Fathoms/day; career budget ~5 Fathoms/year; relief-rotation caps careers at ~60 Fathoms (rotation to non-channeling postings; mandatory stand-down years). Side effects by depth: <20 nosebleeds/migraines; 20â€“40 memory gaps, emotional flattening, sleep disorders; 40â€“60 personality erosion ("the thinning"), Veil weakening (Tide-mark bleed); 60â€“80 identity instability, involuntary channeling, physical wrongness; 80â€“100 pre-Drowning. Irreversible (02.I). Stillness practices, Stillwater-class drugs, rest slow further accumulation; nothing reverses it. The cruel arithmetic: the most powerful are on the shortest clocks (T5s rarely past 50).

**Per-tier serious-use costs (30.2, CANON):** T1 negligible (<0.1) Â· T2 0.5â€“2 Â· T3 3â€“8 Â· T4 10â€“25 Â· T5 25â€“60 Â· T6 40+. One fight's cost: T2 a bad week of migraines; T3 months of recovery; T4 a year of self minimum; T5 possibly everything.

**The Laggard's currencies (29 B.6, CANON)** â€” Arthur accrues no Fathoms; his prices are different:
1. **Social cost** (ambient, permanent): dim rooms, dead plants, dates ending early, landlord questions â€” exhausting, forever.
2. **The ratchet:** ordinary life adds nothing; *extreme* use (deep lag, storage, the flare) adds permanent fractions of a second to the base lag. Ilsa: 3.0 â†’ 3.4s over seven years. Arthur: 3.0 (2017) â†’ ~3.1s (2024). What happens at 10s, at a minute: UNKNOWN (Ilsa's last journal page torn out). Drafter's ruler (non-binding planning instrument): logged extreme use ~+0.25s; unlogged ~+1s; per-season budget ~1â€“1.5s.
3. **The entity's attention:** deliberate deep use is *noticed* by whatever stands at the other end â€” orientation shifts, cold drift, dreams of dark water (all three holders). Whether attention is dangerous: UNKNOWN (Layer 5).
4. **Physiological:** nosebleeds, hypothermia-like chill, exhaustion proportional to depth/duration (3-minute deepening = a day in bed; Ilsa's 3-hour maximum = a week, "it almost didn't give me back").
5. **Exposure:** deep use visible to Lantern-sensitives across kilometers and to instruments; every serious use spends secrecy â€” the one resource he cannot replenish.

**Backlash (Choir):** the seeder experiences a distorted echo of the implanted impulse; per-link unreliability compounds geometrically (02.I).

**Theft arithmetic:** thief inherits victim's Fathoms; thief's future accumulation rate doubles (04.6).

**Healer's paradox:** aggressive Bone healing transfers Erosion-risk to the healer (04.6).

---

## G. Activation conditions

- **Resonance:** willed channeling by an Awakened Attuned (Hollow Pattern + First Tide trigger: trauma, near-death, or Seep exposure). ~60% of carriers never Awaken. No reliable artificial Awakening (three state programs + one corporate, all ended in Drownings â€” CANON, load-bearing).
- **Laggard:** none â€” passive, always-on (29 B.4). "Use" = reading (observation), deepening (deliberate lag extension via Stillness-adjacent technique), or stepping into (out-of-phase). All three learned, not granted.
- **Seep Rules:** each anomaly's own trigger conditions (28_ANOMALIES.md); Rules execute without anyone's will.
- **Slipping:** recognition anchor + Erosion payment per distance/unfamiliarity.
- **Technology:** mundane operation (Stillwater dosing, noise generation, ward maintenance) â€” no supernatural activation.

---

## H. Failure conditions

- **Channeling:** overdraw â†’ Fathom spike â†’ thinning â†’ involuntary channeling â†’ Drowning at 100 (new Seep where they stood). Failed wards shred Slipping arrivals. Tide-noise collapses channeling conditions.
- **Laggard uses:** Use 5 â€” the 3-second window ends (re-synchronization mid-step is disorienting; mistimed entry leaves him visible). Use 6 â€” deepening too far: Ilsa's 3-hour maximum "almost didn't give her back." Use 7 â€” window closes before retrieval: partial corrupted return ("unwrapped"); nothing living survives. Use 10 â€” beyond the depth-pressure boundary: rot applies normally; the anchor degrades with depth (edge-corruption creeps inward). Use 12 â€” the flare cannot be unfired; cover identity burned permanently.
- **Escrow (29 B.11, CANON â€” patched 2026-09-20 for Use-7 timescale consistency):** three redundant legs â€” (1) lawyer-held sealed affidavit, mailed on missed weekly check-in; (2) dead-man's publication split across two Loud journalists who don't know each other (halves useless alone); (3) Night Clerks dead drop + Cartographers' waystation backup. The shadow leg is a covert courier *within* the check-in deep-lag session (Use-7 window = hours), not a vault between check-ins. Stated limits: court order opens the lawyer's box (journalists' halves survive); seizure kills the check-in which *triggers* the switch (seizure indistinguishable from death by design); deters rational actors only (the Choir is not rational). Quiet Desk assessment: ~30% failure rate (seizure-before-handoff, corrupted halves, missed check-in during the Membranous phase). Deterrence works through uncertainty (~70% exposure odds), not certainty.
- **Theft ritual:** fails profitably â€” always net loss (inherited Fathoms + 2Ã— burn).
- **Containment:** C-class anomalies fail expensively (continuous active intervention); E-class has no containment â€” mitigation and evacuation only.

---

## I. Counters

**The seven weak-survive-strong mechanisms (30.3, CANON):** (1) Rule interference â€” attack the condition, not the channeler (break line-of-sight, flood Tide-noise, trigger the exception clause); (2) preparation â€” wards, Stillwater gas, Anchor restraints, blueprints, schedules ("A T4 with a plan beats a T5 with a mood"); (3) terrain â€” thin places, warded zones, mundane geography favor the defender; (4) Tide-noise â€” military-grade jammers make a T0 squad fight a T3 on near-even terms for ninety seconds; (5) information advantage â€” knowing the enemy's Rule, Fathom depth, handler, schedule is worth more than two tiers; (6) Erosion attrition â€” don't win, last; make them spend; (7) social and legal constraints â€” Census files, handlers, licenses; Choir use without license is prison in 140+ countries.

**Technology counters (04.5, 13.3, CANON):** Stillwater (dampens channeling; side effect emotional blunting) Â· Stillwater aerosol (area denial; controversial at scale) Â· Anchor restraints/systems (Hollow-pattern disruptors) Â· warded containment cells (architectural Seep-suppression; expensive) Â· Tide-noise generators (jam channeling + detection; double-edged) Â· Drowndust munitions (force Fathom accumulation; banned; Quiet unaffected â€” no Hollow Pattern to accumulate in; supply capped by Drownings; industrial Drowning = Compact casus belli).

**Laggard-specific counters (29 B.5, B.11, CANON):** wards dampen Membrane-side effects (cannot sever the tether; deep use inside wards is louder at the entity's end) Â· Lantern-sensitives detect deep use across kilometers Â· the T1 filing is camouflage that exposure destroys Â· out-of-phase: 3-second limit, no interaction, solid matter still blocks Â· the entity's attention (cost, not counter, but bounds routine deep use) Â· bullets (B.5: "A bullet still works") Â· conventional Attuned-suppression (Stillwater, Anchor, Drowndust) does NOT affect Arthur â€” he doesn't channel â€” which is why institutions use human intelligence (recruitment) instead of suppression against him.

**Arthur-specific vulnerability (audit note, derived from canon):** his Loudness â€” perfect, uneditable recall â€” is a liability against Information Seeps: Quiet minds shed infohazard contamination via the Veil; his cannot. (Status: THEORY â€” operational consequence of 03.1 + 03.4, not yet stated in canon.)

---

## J. Environmental dependencies

- **Seep-adjacent:** thin places amplify Hollow work and attract the Laggard's lean (29 B.11, Use 8); warded zones suppress Membrane-side phenomena and shred unrecognized Slipping arrivals (02.I).
- **Tide pressure:** high ambient pressure degrades Hollow-Pattern MRI screening (screening centers built in low-pressure zones, 27.4); static rot rate proportional to Tide pressure (02.III); Seep frequency tripled since 2000 on the High Tide (03.1).
- **Light/darkness:** the Laggard drinks ambient light (rooms dim 5â€“10%); total darkness makes the darker-dark *more* visible, not less (29 B.2).
- **Line-of-sight:** causal bubbles capped at line-of-sight scale (02.I); many Rules have line-of-sight conditions attackable via Rule interference (30.3).
- **The ninety-second rule (13, CANON):** no Attuned formation sustains peak output past ninety seconds â€” endurance beats peak in every longer engagement; conventional forces, wards, and prepared T2s win by lasting.

---

## K. Information dependencies

- **Power is legible (02.IV, CANON):** every ability and anomaly follows a Rule discoverable through observation. "If Arthur cannot eventually figure out *why* something happened, it should not have happened."
- **Information is the scarce resource (02.II, CANON-LOCKED):** raw power is common enough to be cheap; reliable, specific, actionable knowledge about Rules, Tide-marks, and faction intentions is what money buys. "Information is cheaper than Fathoms" (30.2): a Lantern T2 who knows a T4's Rule spends zero Fathoms to spoil a channeling worth 20.
- **Arthur's information position (29, CANON):** Loud (perfect Seep recall) + records clerk (ten thousand vectors read; knows what a wrong filing looks like) + the Laggard as window (Veil-immune records; Tide-mark dowsing; clean recordings). His advantage is *connecting separately-held records*, not unrestricted access â€” redactions, classification, static rot, bureaucracy, and misinformation all still bind him (see DATABASE/INFORMATION_KNOWLEDGE_MAP.md).
- **Static rot (02.III, 03.4, CANON-LOCKED):** recordings of active Seeps corrupt proportional to Tide pressure; written notes survive better than video; Loud memory survives best â€” which is why witnesses are worth more than footage, and why Arthur is valuable.
- **The deepfake dividend (02.III):** synthetic media destroyed public trust in video â€” protects the masquerade, but factions can't prove things to each other either; the Compact's closed verification protocols (witnessed, multi-sensor, in-person) are the only currency of proof.

---

## L. Psychological / behavioral constraints

- **Discipline hygiene (04.5, CANON):** academies teach never to channel angry, tired, or grieving â€” emotional state degrades control.
- **Choir backlash (02.I):** seeding always echoes back on the seeder; mass seeding compounds unreliability geometrically.
- **The thinning (04.4):** at 40â€“60 Fathoms, personality erosion â€” the Attuned's own identity becomes a constraint on continued operation.
- **Arthur's professional deformation (29 Part A, CANON):** he believes understanding a thing is the same as surviving it â€” "the Laggard is going to teach him otherwise." His flaw is epistemological, not moral.
- **Stubbornness as countermeasure (30, Scenario 2):** awareness resists seeding; the file is armor.
- **Social constraints on the strong (30.3, mechanism 7):** T5s have mothers, bank accounts, Census files, handlers â€” the law is a leash the weak can pull.
- **The Choir's irrationality (29 B.11):** the escrow deters rational actors; the Choir is not rational â€” fanaticism as a constraint on deterrence-based planning.
- **Folk-heuristic keepers, counselors, optometrists (29 B.10):** the misunderstandings are load-bearing â€” how the world files what it can't price.

---

## M. Equipment interaction

- **Seismograph network (04.5, 02.II, CANON):** ~2,000 Compact stations; detects Tide-pressure events â‰¥T3 globally within minutes. Unregistered large-scale use is *visible*; the question is who responds first. Blind band: sub-T3 (MYSTERY-103).
- **Drafter's ruler â€” Laggard stealth calculus (29 B.11, CANON-adjacent, non-binding planning):** Uses 1â€“5 below instrument threshold (Lantern-visible within meters); Uses 6â€“9 Lantern-visible across kilometers, Seismograph-adjacent instruments flag within the metro; Use 10's recording emits nothing but the artifact is the most incriminating object in the hidden world; Use 11 invisible by definition; Use 12 every Lantern-sensitive for kilometers + Seismograph pressure spike. (The Laggard is not channeling, so the T3 floor does not apply cleanly â€” instruments see pressure displacement, not tier output.)
- **Tide-noise generators (13.3, CANON):** jam channeling and Seismograph detection simultaneously â€” standard cover for covert Attuned operations; tactical engagements concealable, strategic Threshold events not.
- **Wards:** architectural Seep-suppression; dampen the Laggard's Membrane-side effects; cannot sever the tether; hardened wards shred all non-whitelisted Slipping arrivals (02.I).
- **Anchor systems:** vehicle-mounted/emplaced Hollow-pattern disruptors; standard at high-threat checkpoints.
- **Lantern-sensitives:** detect deep Laggard use across kilometers; headaches within ~10m of Arthur (29 B.2).
- **Claims-ML / training-hygiene bound (27.3):** no model trains on unreviewed Seep-adjacent text; Arthur's labels *are* the review layer â€” his indexing feeds both sides' models ("garbage in, gospel out").

---

## N. Team synergy

- **Sweeper doctrine (30, Scenario 3):** the exterminator model â€” professionals don't duel anomalies; they process them. T0 teams + one T1 + Tribunal prohibition orders + perimeter + documentation defeat a T4 object-seep theft with zero casualties.
- **Drowning watch (04.8):** two-person Lantern detail + continuous Seismograph flagging + standing Sweeper standby â€” synergy as containment of a person.
- **Relief-rotation staffing (04.4):** the Compact's agencies price mandatory stand-down years into every staffing model â€” synergy as Erosion management.
- **Arthur's team position (29 Part A):** his network is night-shift clerks, family, and a Discord server (Night Clerks' Ravenhurst cell, IND-004) â€” no combat synergy; his synergy is informational (shared glances at wrong files; street-level early warning).
- **Combined arms (13):** Attuned as JTAC-equivalents designating for conventional strike (US); mass Stillwater logistics + embedded Attuned at company level (China); ward-construction engineers + disaster-relief companies (Albion/SMD).

---

## O. Faction-level capabilities (summary)

Full per-faction capability records: Phase 6 (`DATABASE/FACTIONS_AND_CONFLICTS.md`). Audit-relevant power facts:

- **Meridian Compact:** Seismograph Authority (~2,000 stations), Joint Containment Command (INTL-006), the Tribunal (INTL-002), Classification Office (Geneva), science directorate (Membrane Theory, ~70% accurate). Can assert concurrent jurisdiction above T3/C-C; JCC takes command at T4+/Regional+.
- **GOV-006 Albion / SMD:** civilian Albion Cabinet Office organ; commands Albion Defence Force assets only via disaster-relief framing (the constitutional prohibition on offensive war); Ravenhurst field office holds Arthur's thin file (biennial monitor, unread twice).
- **The Quiet Desk:** human-intelligence doctrine â€” recruitment and surveillance over seizure; its answer to Arthur is "hire him before he publishes" (26.4).
- **Militaries:** all maintain the 90-second rule, BLACK TIDE ladder (WATCH â†’ SURGE â†’ BLACK TIDE), and anomaly-war doctrine for post-containment failure (13.7). Drowndust stockpiled by â‰¥4 states despite the ban; the Compact holds a deniable counter-stockpile (SITE-006).
- **The Red Ledger (SUP-004):** auctions Rules and information; attempted trafficking of the Laggard via black-book inquiry (EVENT-093) â€” the market prices what it can't contain.
- **Vesper Pharmaceuticals (CORP-002):** Tide-medicine; wants Arthur as a zero-Erosion longitudinal subject â€” clinical, consensual, well-funded, impossible to leave.
- **The Cartographers (SUP-002):** would treat the tether as a survey instrument beyond price â€” scientific interest as the most dangerous kind (they will experiment).
- **The Hollow Men (SUP-006):** divers; Silas Crane (Hollow T3, 82 Fathoms) â€” deep water with a voice.

---

## P. Containment implications

- **Containment class is orthogonal to Threat (05.1, CANON):** a T5 can be class A (city-killer asleep in a vault); a T1 can be class E (a harmless rumor that cannot be un-known).
- **C-class is the budget war:** ~40Ã— the cost of B-class; "expensive enough to hurt, common enough to multiply."
- **E-class:** no containment â€” mitigation and evacuation only (ANOMALY-029, the Well: permanent JCC watch).
- **Person-bound:** filed C-A; staffed like D ("contained for now, watched like it's loose").
- **Information Seeps:** cannot be vaulted; containment = compartmentalization, audio-fingerprint programs, memetic-range assessment, noise-farming countermeasures.
- **Arthur as containment problem:** cannot be vaulted (the tether travels with the holder); cannot be suppressed (no channeling to dampen; Stillwater/Anchor/Drowndust don't apply); cannot be seized cheaply (escrow's mutually assured disclosure). The only containment that works on him is *social* â€” employment, relationships, the ordinary life he wants to protect. (This is why the Quiet Desk recruits instead of raiding.)

---

## Q. Legal and political implications

- **Choir law (04.2, 14.3):** most regulated discipline on earth; unlicensed use = prison in 140+ countries; election/referendum use is an Accords/Tribunal offense; contracts influenced by unlicensed Choir use are voidable; licensed commercial use subject to pattern-of-outcome audits.
- **Seizure doctrine (26.4):** unregistered Seep materials seized on sight (no warrant where vector T3+); the quiet-visit ladder â€” visit â†’ audit â†’ seizure â†’ Tribunal referral â€” deliberately boring at every rung (raids make martyrs; filing cabinets make compliance).
- **Classification law (05.3):** T3+/C-D+ â†’ report to Geneva within 72h; T4+/Regional+ â†’ JCC standby; I flag â†’ possession criminalized; V flag â†’ cross-border notification; Sapient/Unknown â†’ Sapient rules of engagement, Tribunal remit, asylum law engaged (one jurisdiction).
- **Theft law (02.I):** pattern-theft lawful only with consent or Tribunal warrant; without one, murder + pattern-theft â€” "the two charges the Tribunal has never once declined to prosecute."
- **Census:** registers the *Attuned*, not Loudness â€” being Loud and unregistered is completely legal (29 Part A). Albion's employer-mediated Census never flagged Arthur (no Hollow Pattern).
- **Drowndust ban:** 1949 Meridian Accords (mandatory 1977 Quiet Night revision); no verification regime, only deterrence; industrial Drowning (manufacturing Drownings for dust) = Compact casus belli.
- **Newborn Hollow-Pattern screening:** several countries screen; several ban as human-rights violation â€” live political fault line (04.5).

---

## Arthur's power curve (Â§4 of the audit brief)

Seven stages. Each stage: CAN do / CANNOT do / does not yet understand / incorrectly believes / risks / required resources / costs / counters / enemies that still win / genuinely powerless situations / realistically achievable victories.

### STAGE 1 â€” START (story opening; Uses 0â€“1)

- **CAN:** notice wrongness (Loud recall); file and cross-reference vectors; realize the shadow "remembers" a door that was open when he blinked (Use 1); survive by being beneath notice.
- **CANNOT:** anything supernatural on purpose; defend himself physically; interpret what the shadow shows beyond the obvious.
- **Does not yet understand:** that the lag is a window; that the T1 filing is camouflage; that anyone is watching him.
- **Incorrectly believes:** the shadow is a personal curse/inconvenience; his memory is just "good memory"; the hiring flag was routine HR.
- **Risks:** the SMD's thin file; the Factor's black-book inquiry (EVENT-093); Pram's arrival (EVENT-100); the street preacher (Choir attention).
- **Resources required:** his job (access to vectors); the Night Clerks' Discord; SaitÅ's shared glances.
- **Costs:** ambient social cost (dim rooms, dead plants, dates ending early).
- **Counters:** any â€” he has no active defense; a bullet; a quiet visit; a Choir seed he can't detect yet.
- **Enemies that still win:** everyone. A single Sweeper, a corporate interrogator, the Factor's buyer, a curious Lantern T1.
- **Genuinely powerless:** any physical confrontation; any situation requiring him to act unseen (he can't yet step into the lag); any infohazard (he can't forget).
- **Achievable victories:** noticing the wrong file; documenting the old-quarter replay (EVENT-092); surviving by being uninteresting.

### STAGE 2 â€” EARLY DEVELOPMENT (Uses 2â€“4)

- **CAN:** read the lag as a 3-second recording (Use 2, via mirrors); anchor against memory alteration â€” cross-reference his actions against the shadow (Use 3); dowse Tide-marks â€” read rooms' history (Use 4, via Ilsa's journals through Pram).
- **CANNOT:** act while unseen; store anything; deepen deliberately; prove anything to anyone (no chain of custody).
- **Does not yet understand:** the ratchet (he notices the lag lengthening but not the price schedule); the entity's attention; that the journals are a curriculum.
- **Incorrectly believes:** that understanding the shadow's behavior equals controlling it; that the journals contain all the answers (the last page is torn out).
- **Risks:** first deliberate experiments are Lantern-visible within meters; Pram's field reports home spend him a little each time; the mirror beat (if anyone else mentions it, he's been read).
- **Resources:** Ilsa's journals (via Pram); reflective surfaces; stillness and time.
- **Costs:** social cost deepening (he starts arriving after people, leaving before them, as doctrine); first ratchet fractions (logged, ~0.25s each).
- **Counters:** interpretation errors (Tide-marks are impressions); anyone who moves faster than 3 seconds; wards dampen readability.
- **Enemies that still win:** any prepared T1+; Aisha's Sweeper team (if ordered); the Factor (money doesn't care about his readings).
- **Genuinely powerless:** against anyone who knows what he is (the readings don't stop a seizure); against the Choir's irrationality; against physical force.
- **Achievable victories:** proving to *himself* what happened in a room; defeating gaslighting (including an NQA "routine" interview); mapping a thin place before entering it.

### STAGE 3 â€” COMPETENCE (Uses 5â€“7)

- **CAN:** step into the lag â€” 3 seconds out-of-phase, unseen, intangible (Use 5); deepen deliberately to minutes (Use 6); store small objects out-of-phase within the window (Use 7); dowse thin places as a compass (Use 8).
- **CANNOT:** pass through solid matter (intangible â‰  phasing); act on the world while out-of-phase; hold deep lag without physiological cost; store anything living; retrieve after the window closes (partial corrupted return).
- **Does not yet understand:** the entity's end of the attention (he feels looked-at without a model for it); the rot-immunity boundary's far edge; what the ratchet is *for* (he treats it as a price; it may be a countdown â€” UNKNOWN).
- **Incorrectly believes:** that 3 seconds of ghosthood is an escape tool rather than a dodge (it doesn't get him *through* anything, only *past* notice); that the shadow's lean is guidance rather than appetite.
- **Risks:** deep use is Lantern-visible across kilometers; each extreme use is a permanent ratchet fraction; the dreams (dark water, something standing with him) intensify; the Quiet Desk's interest sharpens from curiosity to arithmetic.
- **Resources:** the journals' deepening technique; a secure place to recover (a day in bed per deepening); the Night Clerks' early warning.
- **Costs:** ratchet (unlogged deep uses ~1s each â€” the expensive ones); physiological (nosebleeds, chill, exhaustion); exposure (secrecy spent per serious use).
- **Counters:** Lantern-sensitives feel the wrongness; wards dampen; anyone who simply waits 3 seconds; recognition-based tracking of his *wake* fails (the Laggard eats it â€” accidental camouflage), but *visual* pursuit doesn't.
- **Enemies that still win:** a T2 Hollow tracker who switches to mundane methods (cameras, schedules); a Choir operator who works with motives rather than actions (Use 3 anchors actions, not motives); anyone with a rifle and patience.
- **Genuinely powerless:** inside a warded cell (deep use possible but louder at the entity's end â€” and he's still physically *there*); against Drowndust-area denial (doesn't affect him, but it affects everyone he'd call for help); against being *fired* (losing the archive access that makes him dangerous).
- **Achievable victories:** eavesdropping unseen (Use 5/9 shallow); smuggling small objects past surveillance (Use 7 within-window); dowsing a safe route through thin places; surviving the Kota Tua-class event by flinching *into* the shadow.

### STAGE 4 â€” DANGER (Uses 8â€“10; the escrow goes live)

- **CAN:** unobserved deep-lag observation (Use 9); the clean recording â€” un-rottable photographic proof of sub-T4 events at â‰¤3h lag (Use 10); mutually assured disclosure via the three-leg escrow (lawyer affidavit + split-key journalists + Night Clerks dead drop, shadow as in-session courier).
- **CANNOT:** record T5+ events cleanly (rot applies past the depth-pressure boundary); compel anyone to *believe* the recording (chain of custody still a story); survive the *consequences* of publishing (the escrow deters seizure, not assassination by fanatics).
- **Does not yet understand:** what the anchor's degradation will cost him as the ratchet climbs (edge-corruption creeps inward); whether the entity's attention has a threshold after which observation becomes *visitation*.
- **Incorrectly believes:** that the escrow makes him safe (it makes him *expensive to seize* â€” ~70% exposure odds â€” which is not safety, and he knows the Desk knows the ~30% failure rate); that a clean recording ends arguments (it starts them â€” every faction at once).
- **Risks:** possession makes him a target of every faction simultaneously; using the recording spends the masquerade itself; the Quiet Desk's recruitment pitch arrives (the hiring redaction breaks); the Pale Court's wrong bloodline theory attaches to him.
- **Resources:** the escrow's three legs (lawyer, journalists, dead drop); the Night Clerks' street-level early warning; his Choir-facing precautions (Use 3 + staying beneath notice).
- **Costs:** the ratchet's per-season budget starts binding (~1â€“1.5s); exposure cost goes exponential (every serious use now spends *faction-level* secrecy); the social cost becomes operational (he must manage who knows he can prove things).
- **Counters:** the recording's chain-of-custody problem; the escrow's stated failure modes (court order, seizure-before-handoff, corrupted halves, Membranous-phase missed check-in); the Choir's irrationality; the Tribunal doesn't accept shadow-testimony (yet).
- **Enemies that still win:** the Drowned Choir (fanatics don't do arithmetic); a state actor willing to eat the ~30% exposure odds; anyone who kills him *without* trying to steal (the tether passes to the nearest Loud witness â€” or dissipates if engineered â€” either way *he* is dead); old age, illness, a car accident (the world is indifferent).
- **Genuinely powerless:** against the entity itself (whatever stands at the other end is not something he can fight); against the masquerade's collapse (if his recording leaks, the world that results has no place for a clerk); against his own ratchet (one-way).
- **Achievable victories:** deterring the Quiet Desk's seizure wing (mutually assured disclosure); proving a faction's lie *to a specific audience* (not the world â€” a Tribunal desk, a journalist's editor); surviving recruitment by becoming more useful hired than seized.

### STAGE 5 â€” STRATEGIC POWER (Uses 10â€“11 understood; the information weapon)

- **CAN:** operate Erosion-free where every rival is on a Fathom clock (Use 11 as *understood* advantage); price his cooperation (Nwosu's paper, the Cartographers' survey, the Ledger's auction â€” he becomes a market-maker in information); run the flare as a strategic signal (Use 12 held in reserve â€” the threat of the flare is worth more than the flare).
- **CANNOT:** convert information into physical safety (the bullet still works); compel belief at scale (the deepfake dividend means even his clean photos face a world that trusts no image); outrun the ratchet.
- **Does not yet understand:** the full shape of what the factions will pay â€” and what paying *costs him* (every deal is a file, and files are read by someone).
- **Incorrectly believes:** that being valuable is the same as being safe (Vesper's interest is "impossible to leave"; the Cartographers will *experiment*).
- **Risks:** the auction dynamic (EVENT-093's buyer was the first bid, not the last); the Pale Court's bloodline fiction becoming *operationally true* (courts don't need truth, they need a story); the entity's attention compounding with each deep use.
- **Resources:** faction competition itself (bidders restrain each other); the Tribunal's procedures (paperwork as armor); his ordinary life (the thing he protects is also his camouflage).
- **Costs:** attention (the entity's end is now *accustomed* to his use â€” the dreams change); the ratchet approaches the single-digit seconds where Ilsa's data ends; every alliance is a leak surface.
- **Counters:** mutually assured disclosure cuts both ways (he can't use what he can't afford to leak); the Ledger prices his information â€” and sells the *price* to his enemies; the Quiet Desk's long game (outlive him â€” he's mortal, the Desk isn't).
- **Enemies that still win:** time (the Desk can wait; his body can't); the entity (attention is not a negotiation); a coalition (if the factions ever agree on him, the bidding war ends and the carving starts).
- **Genuinely powerless:** against the High Tide itself (900+ Seep events a day â€” the world is getting stranger faster than he can file it); against the L5 questions (he cannot *use* what he doesn't understand, and the understanding is the danger).
- **Achievable victories:** manipulating *situations* â€” setting factions against each other with timed disclosures; surviving as the indispensable witness; choosing who gets to know what, when (information as terrain).

### STAGE 6 â€” HIGH-END (Use 12 spent or credibly threatened; Uses 13+ via the generative principle)

- **CAN:** the flare â€” summon every Lantern-sensitive for kilometers, burn the T1 cover forever, and *choose the audience* (a flare fired over a Tribunal hearing is a different weapon than one fired over a black site); generate Uses 13+ by the observeâ€“hypothesizeâ€“testâ€“pay rule (each new use a season-level achievement, each paid in ratchet).
- **CANNOT:** unfire the flare; return to the records desk; stop the ratchet; know whether the next fraction of a second is the one Ilsa's torn page warned about.
- **Does not yet understand:** what lives under the lengthening lag (the 10s question is now *his* question, not Ilsa's); whether the entity's attention has become something with *intentions* (L5 #2 approaches as lived experience, not theory).
- **Incorrectly believes:** possibly, that he is now the one using the tether â€” the journals' last un-torn warning suggests the arrow may have reversed some time ago, and he hasn't found the test that falsifies it yet.
- **Risks:** the post-flare world (everyone knows; the bidding war becomes a custody war); the ratchet's unknown far end; the Crane warning's second half (whatever Silas Crane wouldn't say on the record).
- **Resources:** whatever he built in Stages 4â€“5 (alliances, the escrow's tested legs, the Night Clerks grown into something larger); the torn page's absence (not knowing is now a *tactical* asset â€” his enemies can't plan around what isn't in any file).
- **Costs:** the ratchet budget is now the series budget (each Use 13+ spends fractions he can't afford to waste); the entity's attention is a standing condition, not an event; the ordinary life is gone (the 1K apartment, the night shift â€” the camouflage of smallness, spent).
- **Counters:** everything that countered him at Stage 4, plus: his fame (the best ward he owned was being uninteresting); the Compact's full attention (the Drowning watch with his name on it â€” institutional, not physical, per the 04.8 clarification); the possibility that deep use now *invites* rather than merely *notifies*.
- **Enemies that still win:** the entity; a united Compact (if the hostage-exchange logic ever prices him as acceptable loss); his own accumulated attention-debt.
- **Genuinely powerless:** against the answer to L5 #2 if the answer is "yes, and it has been waiting"; against the ratchet's far end (unknown by design).
- **Achievable victories:** confronting major supernatural threats *through preparation and understanding* â€” the intended endgame shape: not the strongest person in the room, but the one who read the room's file.

### STAGE 7 â€” LATE-STAGE (structural, not plotted)

- **CAN (structural):** whatever the generative principle has earned him by then, priced in a ratchet approaching the unknown; the story's information position fully matured (he understands events differently from everyone else â€” the Â§14 asymmetry realized).
- **CANNOT (structural):** become the strongest person in the world (the system forbids it â€” Erosion caps the Attuned, the ratchet caps him, and the bullet still works); resolve the L5 mysteries by power (they are questions, not enemies); return to smallness.
- **Does not yet understand:** the L5 set â€” by design, these outlast his power curve (mystery as the permanent tension source when power plateaus).
- **Risks:** the series' central irony made personal â€” the better he understands the tether, the more he resembles its previous holders, and the journals show where that road ends (Ilsa's torn page).
- **Achievable victories (structural):** the clerk's victory â€” documentation, testimony, the file that outlives the fight. The story's thesis: the most dangerous survivor is the best-informed weak man in Ravenhurst.

> Curve verdict (audit): the progression is **knowledge-shaped, not power-shaped** â€” each stage adds *understanding and options*, never raw output. The Laggard's output stays ~zero throughout; what grows is Arthur's *read* of it and the *world's read* of him. No stage grants physical invulnerability, uncounterable surveillance, or cost-free operation. The bullet still works at Stage 7. This is the structural guarantee against hidden-OP drift.

---

## Status ledger â€” canon-status of this database's claims

- **CANON-LOCKED:** the 02.I hard rules; tier measures maximum sustainable output; Erosion irreversibility; the Laggard's mechanism (tether, not shadow), inheritance chain (proximity + Loudness, unengineered), and 2017 Ravenhurst transfer.
- **CANON:** everything else stated as fact above unless marked otherwise.
- **PROVISIONAL:** Ilsa's pre-1989 holder inferences; the drafter's ruler (ratchet budget); the rot-immunity boundary's exact depth-pressure numbers (Ilsa's journals mark them PROVISIONAL, margin note "don't").
- **THEORY:** Membrane Theory (~70% accurate); Arthur's Loudness as infohazard vulnerability (audit-derived).
- **UNKNOWN:** what drives the Tide cycle Â· what is behind the Laggard / whether it is intelligent Â· whether the Undertow wants anything Â· what caused the 2018 dip Â· what was on Ilsa's torn page Â· what happens at 10s+ ratchet Â· whether the entity's attention is dangerous.
- **DEPRECATED:** the filed `MV-T1/D/Local/Reactive` reading (in-world dodge, superseded by `MV-T1/C-A/â€”/Local/Unknown`); the escrow's pre-patch "shadow as week-long vault" description (contradicted Use 7; corrected 2026-09-20).



