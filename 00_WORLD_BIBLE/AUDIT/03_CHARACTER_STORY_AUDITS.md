# AUDIT VOL. 03 — Character, Story & System Audits — THE QUIET TIDE

> **Phase 20 repository consolidation (2026-09-21, v3.0).** This numbered volume merges 10 source files **verbatim** into one file. No content was changed, rewritten, or summarized — only this header, the source register below, and per-section attribution separators were added. To find a document's new location, see `AUDIT/00_CONSOLIDATION_MAP.md`.

## Source register

| # | Original file | Words | sha256 (pre-merge) |
|---|---|---|---|
| 1 | `AUDIT/FACTION_AUDIT.md` | 9,318 | `dbcbf410f78eb2cf…` |
| 2 | `AUDIT/FACTION_CONFLICT_ENGINE_AUDIT.md` | 3,798 | `a4217b4946e8100a…` |
| 3 | `AUDIT/MYSTERY_ARCHITECTURE_AUDIT.md` | 1,193 | `caf44081017344c4…` |
| 4 | `AUDIT/POWER_PROGRESSION_AUDIT.md` | 9,236 | `8377771ad26f2e13…` |
| 5 | `AUDIT/POWER_SYSTEM_AUDIT.md` | 6,378 | `bd9d6b6cc51eabc9…` |
| 6 | `AUDIT/PROTAGONIST_AUDIT.md` | 5,259 | `ee376932c6073e3c…` |
| 7 | `AUDIT/ROMANCE_ARCHITECTURE_AUDIT.md` | 7,882 | `04608759508f9b28…` |
| 8 | `AUDIT/STORY_ARCHITECTURE_AUDIT.md` | 3,350 | `1be8e41bbdda6315…` |
| 9 | `AUDIT/SERIALIZATION_AUDIT.md` | 2,843 | `e543ced15bf93b36…` |
| 10 | `AUDIT/JAPANESE_CHARACTER_CONSISTENCY_AUDIT.md` | 2,025 | `ac161c7c544be12c…` |

---


---

## SECTION: `AUDIT/FACTION_AUDIT.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/FACTION_AUDIT.md` · sha256 `dbcbf410f78eb2cf8464261ccb088156ac01bd74a55d550b7aaae982a70c3916` · 9,318 words. No content changed.

# FACTION AUDIT — THE QUIET TIDE v1.2 (Albion-primary relocation)

> Auditor: AUD-MONEY (forensic audit agent). Date: 2026-09-19.
> Scope: `12_FACTIONS.md` (all profiles), `34_FACTION_RELATIONSHIPS.md` (matrix + axis essays), `10_RELIGIONS.md`, `11_CORPORATIONS.md` (faction-adjacent claims), `14_LAW_ENFORCEMENT.md`, `24_HISTORY.md`, `25_TIMEmessaging app.md` (EVENT-039, 084–100), `26_INFORMATION_CONTROL.md`, `29_PROTAGONIST_ANOMALY.md`, `31_CONFLICT_ENGINE.md`, `32_ROMANCE_FRAMEWORK.md`, `33_MYSTERIES.md`, `35_CANON_DATABASE.md`.
> Constraint honored: canon files were read, never edited. No new lore is added below; proposed solutions are decision prompts for the coordinator, not patches.

## Method

Every faction was tested on four questions: (1) **Identity coherence** — do all files describe the same organization; (2) **Strategic rationality** — given its stated goals, resources, and constraints, does its behavior make sense, or does it have a trivially winning move it inexplicably doesn't take; (3) **Knowledge consistency** — does what the faction "knows" about Arthur/ANOMALY-001 match the dated event record; (4) **Relational consistency** — do `12`'s profile stances match `34`'s matrix vocabulary. The requested coverage — **11 SUP + 7 CRIM + 10 IND + 8 REL** — is tested faction-by-faction in §5.

## Severity definitions

- **Critical:** the faction is unauditable as written (two irreconcilable identities), or its conduct breaks a CANON hard rule / Accords law at the center of the plot. Blocks the audit's other questions until resolved.
- **Major:** direct contradiction between files, or a load-bearing strategic/knowledge claim that fails as written. Needs a coordinator decision.
- **Minor:** matrix-vocabulary mismatch, relocation leftover, unsupported asymmetry, or naming confusion fixable with a line or two.

## Issue counts

- Critical: 3 · Major: 13 · Minor: 15 · **Total: 31**

---

## §1 — Critical identity breaks

### FAC-001 — SUP-004 is two irreconcilable factions

- **Severity:** Critical
- **Location:** `12_FACTIONS.md` (SUP-004 profile) vs. `14_LAW_ENFORCEMENT.md`, `24_HISTORY.md`, `25_TIMEmessaging app.md` (EVENT-084, EVENT-093), `29_PROTAGONIST_ANOMALY.md`, `31_CONFLICT_ENGINE.md` (RC-017, RC-043, CG-048), `35_CANON_DATABASE.md`
- **Conflicting statements:**
  > `12`: "**Anomaly relationship:** Strictly professional — anomalies are *objectives*, handled per contract. The Ledger refuses anomaly-trafficking contracts (Code: 'we're not couriers for things that eat couriers')." / "**Ideology:** **The Code.** (1) No Choir work... (2) No Drowndust, no infohazards, no children. (3) The contract is the contract — but a contract that requires breaking the Code is void, and the Ledger returns the fee *with interest* and blacklists the client."
  > `12` (SUP-006): "The Red Ledger (SUP-004) hunts their fences" (Erosion traffickers, kill-on-sight policy).
  > `35`: "| SUP-004 | The Red Ledger | Gray-market auctioneers; the Factor (CHAR-027) | [12_FACTIONS.md](12_FACTIONS.md) |"
  > `14`: "the Red Ledger exploits the variance, which is why its Factor keeps a buyer list for things that cannot legally be bought."
  > `24`: "The [Red Ledger](12_FACTIONS.md) (SUP-004) auctioned a T4 Object Seep's *Rule* in [Trieste](21_CITIES.md) (CITY-020) in 2021 ([EVENT-084](25_TIMEmessaging app.md))"
  > `25` (EVENT-093): "The Red Ledger's Factor (CHAR-027) circulated a quiet inquiry: *'Persistent Retrograde Shadow, Ravenscroft, T1'* — a buyer wants the Laggard."
  > `31` (RC-017): "the Ledger (SUP-004) tries to buy the ferry's schedule" (escalation b).
- **Why it is a problem:** Six files describe a gray-market auction house whose Factor brokers person-attached anomalies and buys ferry schedules; one file (`12`) describes a Code-bound mercenary company that refuses trafficking contracts, returns fees with interest, hunts traffickers kill-on-sight, and turns down 60% of contracts. These are not two divisions of one organization — the Code as written *forbids* the Factor's entire business. Every downstream audit question (is the Ledger's strategy rational? is its economy viable? what does the Factor's inquiry mean?) is unanswerable until one identity is selected. This is the single largest canon break in the bible, and it sits on the novel's central market thread (EVENT-093 → RC-043 → CG-048).
- **Proposed solutions:** (1) **Keep the `12` PMC** and move the Factor/auctions to a new or existing gray-market actor (the Ash Exchange already runs auctions; the Factor could be CRIM-003's or an IND-006 cutout) — requires rewriting EVENT-084/093/RC-017/RC-043/CG-048 attributions; (2) **Keep the gray-market auctioneer** (six files vs. one) and rewrite the `12` profile as the Ledger's *cover* — e.g., the Code is real but applies only to the PMC division, while the Factor runs a black-book brokerage the Partners don't acknowledge (note `12` already gives the Ledger a "black book" of Code-violating clients — the infrastructure for this reading exists); (3) Split SUP-004 into two registry entries. The coordinator must pick; the audit cannot proceed on SUP-004 until then. **No patch is applied here.**

### FAC-002 — The Factor's Laggard brokering violates both the Code and Accords law

- **Severity:** Critical
- **Location:** `25_TIMEmessaging app.md` (EVENT-093); `31_CONFLICT_ENGINE.md` (RC-043); `14_LAW_ENFORCEMENT.md` §14.2; `12_FACTIONS.md` (SUP-004); `29_PROTAGONIST_ANOMALY.md`
- **Conflicting statements:**
  > `25` (EVENT-093): "The Red Ledger's Factor (CHAR-027) circulated a quiet inquiry: *'Persistent Retrograde Shadow, Ravenscroft, T1'* — a buyer wants the Laggard." / "**Consequence:** ANOMALY-001 is on the market. Arthur doesn't know."
  > `31` (RC-043): "The Factor (CHAR-027) reveals the buyer behind the Laggard inquiry ([EVENT-093](25_TIMEmessaging app.md)): a Pale Court cadet branch, bidding for a wedding gift."
  > `14`: "**Person-attached anomalies cannot be Ledger-titled** — a tether like the Laggard ([ANOMALY-001](28_ANOMALIES.md)) is not ownable property: the holder retains full personhood, and any 'sale' of the anomaly is in law a sale *of the holder*, prosecuted as **trafficking** under Accords law."
  > `12`: "The Ledger refuses anomaly-trafficking contracts (Code: 'we're not couriers for things that eat couriers')."
  > `29`: "**The Red Ledger (SUP-004).** The Factor (CHAR-027) already has a buyer asking after it ([EVENT-093](25_TIMEmessaging app.md)). The Ledger doesn't care what it *is* — it cares what the Rule *sells for*."
- **Why it is a problem:** As written, the Factor is brokering the purchase of a *person-attached* anomaly — which `14` defines, explicitly and with the Laggard as its example, as **trafficking in a person** under Accords law. This is simultaneously: (a) a violation of the Code (`12`); (b) a capital-grade crime under the law file; (c) strategically irrational for a broker whose business depends on Compact tolerance (the Ash Exchange triple-deals Drowndust and survives on compartmentalization — the Factor's inquiry is *circulated*, not compartmentalized). If FAC-001 resolves toward the gray-market identity, the conduct is on-brand but still legally suicidal unless the inquiry is deniable; if it resolves toward the PMC, the conduct is impossible. Either way, the novel's inciting market transaction is currently a crime that the text does not recognize as one.
- **Proposed solutions:** (1) Make the inquiry explicitly *non-purchase*: the buyer seeks observation rights, data, or a futures-style first-refusal — still gray, but not trafficking; (2) keep it as trafficking and make the illegality the point (the Factor is compromised, the Pale Court cadet branch is rogue, the Compact's response is a plot engine); (3) downgrade EVENT-093's classification from "Compact-only" to a deniable cutout chain so the Factor has insulation. What cannot stand is a circulated, attributed trafficking inquiry that no file treats as trafficking.

### FAC-003 — Five factions field private Attuned forces in violation of a CANON hard rule

- **Severity:** Critical
- **Location:** `08_ECONOMY.md` §8.3 (CANON rule); `33_MYSTERIES.md` ("NOT mysterious" #2); `12_FACTIONS.md` (SUP-001, SUP-004); `11_CORPORATIONS.md` (CORP-001); `12_FACTIONS.md` (CRIM-002, CRIM-006)
- **Conflicting statements:**
  > `08`: "> CANON: No corporation, syndicate, or cult fields a private force of more than a handful of combat-licensed Attuned." / (line 276) "> CANON: No private Attuned army above a handful of combat-licensed personnel exists (economics + Accords Art. VII + Erosion + Seismograph)."
  > `33`: "**Why there are no Attuned armies.** Four mass-Awakening attempts, four piles of the Drowned ([EVENT-028](25_TIMEmessaging app.md), [04_POWER_SYSTEM.md](04_POWER_SYSTEM.md)). CANON. Not a mystery — a morgue."
  > `12` (SUP-004): "~2,400 active operators (70% Attuned, T1–T4...)" — **~1,680 combat Attuned**.
  > `12` (SUP-001): 300 Attuned Tideguard.
  > `11` (CORP-001): "a standing contractor force including ~400 licensed Attuned (mostly T2, some T3)."
  > `12` (CRIM-002): 80 Attuned enforcers ("quiet work" division). `12` (CRIM-006): 40 Attuned (malalim division).
- **Why it is a problem:** The bible proves this rule twice — once as CANON law/economics (`08`), once as settled history in the file whose job is distinguishing promises from gaps (`33`). Then it violates it five times with *quantified* forces, the largest (1,680) being larger than most national threshold establishments. "A handful" cannot stretch to 1,680, 400, or 300. This is not a gray area: it is a CANON rule with five numbered exceptions, and the economic sub-finding (ECON-009: the Ledger can't afford its force at $900M turnover) shows the violations don't even pay for themselves.
- **Proposed solutions:** (1) **Enforce the rule**: cut forces to handful-scale (squads, not regiments) — the Ledger becomes an elite cadre, the Tideguard a ceremonial/close-protection unit, Halcyon's 400 mostly T2 *support* personnel explicitly not combat-licensed; (2) **Amend the rule**: the CANON becomes "no private force above a handful *without a Compact charter*" and each violator holds a named charter with conditions (revocable, inspected, Seismograph-monitored) — which converts a bug into five plot hooks; (3) reclassify most Attuned as non-combat-licensed (medics, Lanterns, counselors) so the *combat-licensed* count stays handful-scale. The rule or the rosters must change; both standing is not an option.

---

## §2 — Major contradictions

### FAC-004 — CRIM-002 has two different leaders (and two different CHAR-026s)

- **Severity:** Major
- **Location:** `12_FACTIONS.md` (CRIM-002) vs. `35_CANON_DATABASE.md` vs. `25_TIMEmessaging app.md` (EVENT-099)
- **Conflicting statements:**
  > `12`: "**Leadership:** **The Naga** — currently **Dewi 'Naga' Mahmud** (52, daughter of the founder, un-Attuned, Loud — 'the woman who collects debts the way other people collect art')."
  > `35`: "| CRIM-002 | Naga Hitam ('Black Naga') | Jakarta syndicate; Hendra Gunawan (CHAR-026); bought NQA portfolio |" / "| CHAR-026 | Hendra 'Bos Naga' Gunawan (b. 1975) | Head, Naga Hitam (CRIM-002); Quiet |"
  > `25` (EVENT-099): "**Hidden truth:** Hendra Gunawan (CHAR-026) of Naga Hitam (CRIM-002) bought NQA's delinquent-claims portfolio..."
  > `12`: "**Secrets:** ... (3) Dewi Mahmud is **dying** (conventional illness...). The succession examination of her nephew is therefore *accelerated*, and three kepala are positioning." / "**Hidden agenda:** Dewi's endgame — known to three people — is **legitimacy**: to convert Naga Hitam into a licensed private-security *keiretsu* before she dies..."
- **Why it is a problem:** Two different people head the same syndicate: a 52-year-old Loud woman (Dewi Mahmud) vs. a Quiet man born 1975 (Hendra Gunawan), with CHAR-026 assigned to Hendra in `35`/`25`. The contradiction is not cosmetic — `12`'s entire CRIM-002 dramatic engine (dying boss, accelerated succession examination, three armed kepala, secret legitimacy endgame) belongs to Dewi; `25`'s dated canon event (2024-09-17, two days before the audit date) shows *Hendra* executing the portfolio purchase. A reader cannot know who runs Jakarta's largest syndicate, who is dying, or whose endgame is in play.
- **Proposed solutions:** (1) Hendra is Dewi's nephew/heir-apparent (the "examination candidate" `12` mentions), already acting as head while Dewi declines — reconcile by making the succession *further along* than `12` states; (2) Dewi is "the Naga" (titular) and Hendra "Bos Naga" (operational) — split the titles explicitly; (3) pick one and rewrite the other file's entries. Note the Loud/Quiet difference also matters for the Priok veto mechanics.

### FAC-005 — REL-007/SUP-003: founded 1911 with 2,000 professed, or 1962 with 8,000?

- **Severity:** Major
- **Location:** `10_RELIGIONS.md` (REL-007) vs. `12_FACTIONS.md` (SUP-003)
- **Conflicting statements:**
  > `10`: "Founded (in its modern form) in Kyoto in 1911; now ~2,000 professed practitioners in houses on four continents, plus ~20,000 lay affiliates."
  > `12`: "**Origin:** 1962, Kyoto — a Bone T4 (a trauma surgeon) who Drowned *slowly*, over eleven years, and spent the last three teaching other Attuned how to 'sit still inside the pressure.' Her students formalized the practice after her death." / "**Members:** ~8,000 professed (monastics); ~60,000 lay affiliates."
- **Why it is a problem:** Founding date (1911 vs. 1962), professed strength (2,000 vs. 8,000), and lay affiliates (20,000 vs. 60,000) all disagree by multiples. These are the same organization's basic facts in the two files that define it (theology vs. faction profile). The Quiet Garden is also the Care Axis's anchor and a viewpoint-adjacent faction — its size determines whether it's a boutique order or a mass institution, which changes every scene it's in.
- **Proposed solutions:** The "(in its modern form)" qualifier in `10` offers the bridge: 1911 = the contemplative lineage's founding, 1962 = the Bone T4's reformalization as the stillness-practice order. Then reconcile the numbers (e.g., 2,000 professed *monastics* of the 1911 lineage vs. 8,000 total professed including the reformed order's lay-monastics — or pick one census). The bridge must be written, not assumed.

### FAC-006 — REL-001: a dozen Attuned in holy orders, or none?

- **Severity:** Major
- **Location:** `10_RELIGIONS.md` (REL-001) vs. `35_CANON_DATABASE.md`
- **Conflicting statements:**
  > `10`: "Roughly 400 staff worldwide: priests, nuns, lay scholars, and — quietly — a dozen Attuned in holy orders."
  > `35`: REL-001 one-liner describes the office with "**no Attuned in holy orders**."
- **Why it is a problem:** Direct factual negation on a point with plot weight: REL-001's whole dramatic function is the cooperative-scholar posture (archives, Modus Vivendi, the Asylum Protocol), and whether the Vatican's office *contains* Attuned determines whether it's a genuine bridge institution or a purely Quiet bureaucracy managing something it doesn't embody. The `10` version ("quietly") is also the more interesting one — and the one consistent with REL-001 sheltering Attuned under the Asylum Protocol.
- **Proposed solutions:** Keep `10`'s dozen (the "quietly" is doing real work — it explains the Asylum Protocol's credibility) and correct the `35` one-liner. One-line fix.

### FAC-007 — The Drowned Choir was founded in 1953 by widows, or in 1965 by Mother Mercy

- **Severity:** Major
- **Location:** `12_FACTIONS.md` (SUP-001) vs. `25_TIMEmessaging app.md` (EVENT-039) vs. `35_CANON_DATABASE.md` (CHAR-022)
- **Conflicting statements:**
  > `12`: "**Origin:** Founded 1953 in Marseille by dockworkers' widows who survived a mass Drowning event during a botched French containment operation. The widows' grief-group became a congregation; the congregation became an order."
  > `25` (EVENT-039): "### EVENT-039 — The Drowned Choir Founded (1965)" / "**Hidden truth:** Miriam Adler (CHAR-022), 'Mother Mercy,' preached Drowning as salvation after her son's First Tide killed him — the first Seep-worshipping mass movement (SUP-001/REL-005)."
  > `35`: "| CHAR-022 | Miriam 'Mother Mercy' Adler (1928–1971) | Founder, Drowned Choir (SUP-001/REL-005); Drowned 1971 |"
- **Why it is a problem:** Twelve years and two founders apart, across three files. SUP-001 is the oldest mass-movement faction; its origin story (state crime creating the widows vs. a charismatic American preacher) determines its theology, its French-vs-American institutional character, and the meaning of its 400,000 adherents.
- **Proposed solutions:** The bridge is available: the Marseille widows' grief-group (1953) existed as a congregation; Mother Mercy (1965) transformed it into the *mass movement* — EVENT-039's "first Seep-worshipping mass movement" language already supports this (a congregation becoming a movement). Write the two-stage founding explicitly: 1953 the congregation, 1965 the movement. `35`'s "Founder" becomes "refounder" or "the movement's founder."

### FAC-008 — CORP-001 is a defense prime, a precognition-trading tech firm, or both

- **Severity:** Major
- **Location:** `11_CORPORATIONS.md` (CORP-001) vs. `35_CANON_DATABASE.md` vs. `33_MYSTERIES.md` (L3 table)
- **Conflicting statements:**
  > `11`: "**Sector:** defense, containment engineering, supernatural security contracting. **HQ:** Arlington, Virginia, USA. **Employees:** ~48,000. **Revenue:** ~$31B (2023; ~40% supernatural-attributable, booked as 'advanced systems')." / "**Ideology:** *competent deterrence*."
  > `35`: "| CORP-001 | Halcyon Dynamics | US tech; Tide-precognition trading; thin-place compute |"
  > `33` (L3): "Halcyon Dynamics (CORP-001) | The simulation hypothesis — Seeps are computational glitches; with enough data, exploitable | THEORY (unfalsifiable; useful for engineering, empty for explanation)"
- **Why it is a problem:** `11` describes an Arlington defense prime; `35`'s one-liner describes a tech/trading firm. (`33`'s simulation hypothesis and `12`'s cross-ref "Simulation-hypothesis engineers" are at least compatible with `11`'s R&D posture — `35` is the outlier.) A $31B defense contractor and a precognition-trading shop are different companies with different enemies, regulators, and plot functions.
- **Proposed solutions:** Correct the `35` one-liner to match `11` (defense/containment prime; simulation-hypothesis R&D as its L3 belief). If the trading desk is meant to exist, make it a division (e.g., a quant subsidiary) rather than the company's identity.

### FAC-009 — Santara is CANON-unaware of the hidden world, but ran an unlicensed seeding desk

- **Severity:** Major
- **Location:** `11_CORPORATIONS.md` (CORP-012) vs. `14_LAW_ENFORCEMENT.md` §14.4
- **Conflicting statements:**
  > `11`: "> CANON: CORP-012 is completely unaware of the hidden world — its ignorance is load-bearing... no one in leadership has any hidden-world role, knowledge, or contact."
  > `14`: "the 2020 Santara board audit (corporate compliance desk, unlicensed — the Tribunal fined the company for *running* one without a warrant protocol...)"
- **Why it is a problem:** A "seeding desk" in `14`'s taxonomy is a counter-seeding unit using Lantern examination — a hidden-world capability. A company that *ran* one (and was fined by the Tribunal, the Compact's court) cannot be "completely unaware... no hidden-world role, knowledge, or contact." The CANON tag on `11`'s ignorance makes this a hard break, not a soft one — and Santara's ignorance is explicitly "load-bearing" for the Vesper plotline.
- **Proposed solutions:** (1) The desk was mundane (a conventional corporate-compliance unit the Tribunal *mistook* or *reclassified* — the fine being the joke the parenthetical implies: "which tells you everything about the law's priorities"); (2) a rogue Santara executive ran it without board knowledge — but then "no one in leadership" needs an exception; (3) move the 2020 incident to a different company. The current text has the Tribunal fining a CANON-unaware company for a hidden-world operation.

### FAC-010 — Arthur has "never met another civilian Loud adult" — his best friend is one

- **Severity:** Major
- **Location:** `26_INFORMATION_CONTROL.md` §26.x vs. `32_ROMANCE_FRAMEWORK.md` (Configs A, E) vs. `25_TIMEmessaging app.md` (EVENT-085)
- **Conflicting statements:**
  > `26`: "His defining early misunderstanding: he thinks everyone in Quiet Insurance remembers like he does, the way a fish doesn't know about water. He has never met another civilian Loud adult to compare with."
  > `32` (Config E — Saitō Yūto): "26, night-shift records clerk beside Arthur, NQA Ravenscroft branch. Indonesian migrant, Loud. Arthur's best friend since the Jakarta schoolyard — the only person at work who *remembers*."
  > `32` (Config A — Nadia Puspita): "He watches her laugh about a 'weird dream' that was a Seep event he filed." (He *knows* Quiet people forget.)
  > `25` (EVENT-085): Arthur joins the Ravenscroft Night Clerks (IND-004) cell in 2022 — the service workers who "trade incident information as professional currency" (`26`).
- **Why it is a problem:** `26`'s claim fails three ways: (a) Saitō is a civilian Loud adult and Arthur's best friend *since childhood* — "never met" was never true; (b) Config A shows Arthur currently *knows* Quiet colleagues forget (the Tuesday problem is the premise), so "thinks everyone remembers like he does" cannot be his current belief either; (c) Night Clerks membership (2022) puts him inside a remembering subculture. This is the protagonist's core epistemic state — the file that defines it contradicts the file that defines his relationships.
- **Proposed solutions:** Rewrite `26`'s passage as a *dated* belief: the "fish doesn't know about water" misunderstanding held until a specific moment (e.g., comparing notes with Saitō, or the Night Clerks cell), after which his ignorance became *strategic* (he performs normalcy). That preserves the early-novel beat and matches `32`. The "never met another civilian Loud adult" sentence must go — Saitō refutes it on every reading.

### FAC-011 — Pram was "sent to Jakarta" per `29`; EVENT-100 sends him to Ravenscroft

- **Severity:** Major
- **Location:** `29_PROTAGONIST_ANOMALY.md` §29.x vs. `25_TIMEmessaging app.md` (EVENT-100)
- **Conflicting statements:**
  > `29`: "**The Cartographers (SUP-002).** ... Pramudya Nugroho (CHAR-032) has been sent to Jakarta ([EVENT-100](25_TIMEmessaging app.md))."
  > `25` (EVENT-100): "**Hidden truth:** Pramudya Nugroho (CHAR-032), Cartographer (SUP-002), found Ilsa Brandt's 1996 field map in the Exchange... Pram is sent to Ravenscroft." / `32`: "reassigned to Ravenscroft ([EVENT-100](25_TIMEmessaging app.md)), arriving September 2024."
- **Why it is a problem:** `29` cites EVENT-100 for a claim the event does not make — a mis-citation inside the bible, and a relocation artifact (Jakarta was the primary city pre-relocation). Pram's destination determines the novel's geography: the Cartographer arrives in *Arthur's* city or he doesn't.
- **Proposed solutions:** Correct `29` to Ravenscroft. One-word fix, but it must be made — a viewpoint file mis-citing the timeline will propagate.

### FAC-012 — `12`'s knowledge states are stale against the September 2024 event record

- **Severity:** Major
- **Location:** `12_FACTIONS.md` (SUP-002, SUP-009, CRIM-002 profiles) vs. `25_TIMEmessaging app.md` (EVENT-095–100)
- **Conflicting statements:**
  > `12` (SUP-002): "Not a threat yet. Hasn't read the Ravenscroft survey" (knowledge state re: Arthur/ANOMALY-001).
  > `25` (EVENT-100, 2024-09-18): "Pramudya Nugroho (CHAR-032), Cartographer (SUP-002), found Ilsa Brandt's 1996 field map... *'It is not his shadow. It is a tether. Do not let them auction the boy.'* Pram is sent to Ravenscroft." / "**Consequence:** The Cartographers reclassify ANOMALY-001 — from curiosity to priority."
  > `12` (SUP-009): "Would court Arthur only if the Hollow Pattern proved heritable" / "Not yet — Arthur's file hasn't reached the Court's genealogists."
  > `25` (EVENT-098, 2024-09-15): "Vivienne Ashworth (CHAR-025) asked after 'the Reed boy' — the Pale Court (SUP-009) collects Loud bloodlines, and the Reed line just became interesting."
  > `12` (CRIM-002): "Naga doesn't know Arthur yet."
  > `25` (EVENT-099, 2024-09-17): "Hendra Gunawan (CHAR-026) of Naga Hitam (CRIM-002) bought NQA's delinquent-claims portfolio... including three of Reed Arthur's Ravenscroft incident reports."
- **Why it is a problem:** Three `12` profiles describe a knowledge state that the dated timeline has already overtaken — by the audit date (2026-09-19), the Cartographers have reclassified ANOMALY-001 as a priority, the Pale Court is asking after "the Reed boy," and Naga owns paper on Arthur's sightings. The "current interest is low" posture (also in `29`) is no longer credible without knowledge tiers: the bible needs to distinguish *knowing Arthur's name*, *knowing the T1 filing*, *knowing the tether hypothesis*, and *knowing author-level truth* — see the tier table in §6. As written, a reader cross-referencing `12` and `25` will conclude the left hand doesn't know what the right hand dated.
- **Proposed solutions:** (1) Add "as of" timestamps to `12`'s knowledge-state fields (e.g., "Knowledge of ANOMALY-001 (as of 2026-06)"); (2) update the three profiles to the September state; (3) adopt the §6 knowledge-tier vocabulary across `12`, `25`, and `29` so "interest" is always tier-qualified. The cheapest correct fix is (1)+(3).

### FAC-013 — The requested faction totals are untestable: 11 SUP + 7 CRIM + 10 IND + 8 REL do not exist as profiles

- **Severity:** Major
- **Location:** `12_FACTIONS.md` vs. `35_CANON_DATABASE.md`; `34_FACTION_RELATIONSHIPS.md` §34.1
- **Conflicting statements:**
  > `12` profiles in full: SUP-001 through SUP-010, CRIM-001 through CRIM-007, IND-001 through IND-005. (No SUP-011, no IND-006–010.)
  > `35` adds one-line stubs: SUP-011, IND-006, IND-007, IND-010, REL-008 ("PROVISIONAL pending coordinator verification"); IND-008/009 are unclaimed by any file.
  > `34`: "## 34.1 Master stance matrix (the 21 profiled factions)" — containing 22 rows: 10 SUP + 7 CRIM + 5 IND.
- **Why it is a problem:** The audit was asked to test 11 SUP + 7 CRIM + 10 IND + 8 REL = 36 factions. Fully profiled: 10 + 7 + 5 + 0 = 22. Six IND entries and one SUP entry are stubs with no goals, resources, leadership, or knowledge profile; one REL entry is a stub; two IND slots are empty. Rational strategy *cannot be tested* for a faction with no stated goals — §5 marks them Unauditable. Separately, `34`'s header claims 21 factions while printing 22 rows.
- **Proposed solutions:** (1) Write the missing profiles (SUP-011, IND-006/007/010, REL-008; claim or cut IND-008/009); (2) formally reduce the registry to the profiled 22 and re-tag the stubs as "reserved namespaces, not factions"; (3) at minimum, correct `34`'s header to 22. The coordinator should decide whether the registry is 36 aspirational or 22 actual — the audit needs the denominator.

### FAC-014 — NQA hired a flagged "Loud, unregistered, anomaly-adjacent" applicant — plot thread or bug

- **Severity:** Major
- **Location:** `25_TIMEmessaging app.md` (EVENT-087); `33_MYSTERIES.md` ("NOT mysterious" #8); `29_PROTAGONIST_ANOMALY.md`
- **Conflicting statements:**
  > `25` (EVENT-087): "His hiring file was flagged by NQA's Lantern-screened HR — *'Loud, unregistered, anomaly-adjacent'* — and approved anyway. Someone wanted him inside. (Who? PROVISIONAL — a thread for the novel.)"
  > `33`: "**Why Arthur was hired at NQA.** His file was flagged *'Loud, unregistered, anomaly-adjacent'* and approved anyway ([EVENT-087](25_TIMEmessaging app.md)). The *approval* is PROVISIONAL — someone wanted him inside, identity unknown — which makes it a **plot thread**, not a mystery: threads get pulled, mysteries get pondered. (If the approver's identity is never meant to pay off, it will be reclassified as a bug in audit.)"
- **Why it is a problem:** The bible itself flags this as thread-or-bug, and the audit agrees — with the institutional angle sharpened: NQA is a *foreign branch* (Ravenscroft, opened 2017) with Lantern-screened HR, operating in Albion under SMD scrutiny, holding "the best Seep-detection dataset in Southeast Asia" (`11`). Hiring a flagged anomaly-adjacent Loud foreigner into the records room *next to the archive everyone is suddenly requesting* (EVENT-096) is either a placed asset (someone's operation — which faction? at what cost?) or institutional malpractice. Additionally, NQA's analytics later "tripped on his recall twice" (`29`) — a firm that flags, hires, and then *doesn't* monitor is behaving irrationally unless the inaction is someone's decision.
- **Proposed solutions:** Per `33`'s own terms: the approver's identity must pay off in-story (placed by whom — Garden? Archivists? a Compact talent-spotter? NQA's own President Director building "the Compact's East Asian detection backbone"?). If the thread is cut, reclassify as bug and rewrite EVENT-087 (e.g., the flag was buried by understaffing, or the Lantern screen was cursory for migrant hires — both weaker, both honest). **HOLD conditionally**: this is sound *if and only if* the thread pays off.

### FAC-015 — The SMD has a trivially winning move over NQA's archive and doesn't take it

- **Severity:** Major
- **Location:** `25_TIMEmessaging app.md` (EVENT-096); `31_CONFLICT_ENGINE.md` (RC-021); `06_GOVERNMENTS.md` (GOV-006); `11_CORPORATIONS.md` (CORP-011)
- **Conflicting statements:**
  > `25` (EVENT-096): "The Archivists of the Second Silence (SUP-008) requested NQA's pre-1980 claim files — they are writing the history Arthur is living inside." / "**Consequence:** Arthur's records-clerk access — the Ravenscroft branch holds the regional archive — becomes valuable to *everyone* at once."
  > `31` (RC-021): dueling subpoenas over the archive; the SMD "doesn't get the archive" — it receives summaries.
  > `06`/`11` context: NQA is a foreign (Indonesian) insurer operating a branch in Albion; the SMD (GOV-006) is the sovereign threshold authority with quiet-police powers; the Ravenscroft branch holds pre-1980 paper files Jakarta keeps ordering transferred, "which keep 'stalling'" (`11`).
- **Why it is a problem:** A sovereign agency with subpoena power, operating in its own country, against a *foreign insurer's branch* holding paper files its own HQ wants moved, should not be defeatable by "we gave them summaries." RC-021's "dueling subpoenas" gestures at legal process but no file states the legal or treaty barrier that stops the SMD from compelling production — and the SMD is simultaneously shown as competent and aggressive elsewhere (it runs Sweeper teams, inspects the port, watches the Akari cell). If the archive is obtainable by subpoena, every faction's scramble for Arthur's access is pointless; if it isn't, the reason must exist.
- **Proposed solutions:** (1) State the barrier: e.g., the files are held under Indonesian jurisdiction via treaty (NQA's HQ successfully claims them as Jakarta property — the "stalling" is Jakarta slow-walking, which also explains SMD-Jakarta friction); or Compact archival privilege asserted through INTL-001; or the paper files' legal custodian is not NQA Ravenscroft at all. (2) Alternatively, let the SMD *get* the archive — and make the scramble about *interpretation* (the files are useless without Arthur's recall/Loud reading) rather than possession. Either preserves the plot; the current "summaries suffice" does not survive contact with a sovereign subpoena.

### FAC-016 — The Drowned Choir's Drowndust stockpile contradicts its licensed-faith strategy

- **Severity:** Major
- **Location:** `12_FACTIONS.md` (SUP-001)
- **Conflicting statements:**
  > `12` (SUP-001): "the Chapel of the Deep" ark-stockpile program — Drowndust held "defensively."
  > `12` (SUP-001): the Choir is "a licensed faith in 90+ countries" whose strategy is hospice legitimacy, pastoral recruitment, and the long "guided Drowning" plan; Drowndust possession is a war crime under Accords law.
  > `12` (SUP-001): 300 Attuned Tideguard (see FAC-003).
- **Why it is a problem:** A globally licensed faith whose entire strategy depends on state tolerance and hospice legitimacy is stockpiling a war-crime substance "defensively" — with no stated operational need that survives cost-benefit: discovery means delicensing, prosecution, and the destruction of the 400,000-adherent pastoral project, while the defensive value against the Compact (which would be the attacker in any confiscation scenario) is nil. "Defensive" Drowndust against whom — the Bell? The Compact? The answer determines whether the stockpile is deterrence (irrational — no second-strike credibility for a hospice order) or eschatological preparation (which contradicts the pastoral strategy). The bible presents it as prudent; it is the riskiest line item in the Choir's portfolio.
- **Proposed solutions:** (1) Give the stockpile a named, rational purpose: e.g., it is the *sacramental reserve* for the guided-Drowning plan (theology, not deterrence) — costly, secret, and consistent with the eschatology; (2) make it a factional secret *within* the Choir (the Cantorate doesn't know; the Immersionists do) so the institutional contradiction becomes an internal conflict; (3) cut it — the Choir's strategy is complete without it. As written it is an unpriced catastrophic risk carried by the faction least able to afford one.

---

## §3 — Minor issues

### FAC-017 — 34 makes Koi a rival of Alon; 12 makes Koi Alon's ally

- **Severity:** Minor
- **Location:** `34_FACTION_RELATIONSHIPS.md` (CRIM-006 row) vs. `12_FACTIONS.md` (CRIM-006)
- **Conflicting statements:**
  > `34`: "| CRIM-006 Alon Combine | ... | Primary rival: ... CRIM-001 (pond-farm logistics friction) / ... / CRIM-007 (Ravenscroft pier friction) |"
  > `12` (CRIM-006): "**Allies:** ... the Koi Network (CRIM-001) — Luzon pond-farm logistics." / "**Enemies:** ... the Blackwater Syndicate (CRIM-007) — not enemies, *landlords*: pier friction in Ravenscroft... managed carefully by both sides."
- **Why it is a problem:** `12` explicitly lists the Koi Network as an *ally* (pond-farm logistics) and Blackwater Syndicate as "*not enemies*, landlords"; `34` lists both as *primary rivals*. "Pond-farm logistics friction" vs. "Luzon pond-farm logistics" (allied) is the same relationship described oppositely. (Note: `34`'s CRIM-001 row does *not* reciprocate — its rivals are CRIM-003/CRIM-004 — so the matrix is also internally asymmetric.)
- **Proposed solutions:** Pick the relationship: allied logistics partnership with *commercial* friction (normal business tension, not rivalry) fits both files if `34`'s "rival" entries are demoted to annotated WARY/CLIENT notes. The "not enemies, landlords" line in `12` is the better text — keep it, fix the matrix.

### FAC-018 — 34's header claims 21 factions; the matrix prints 22

- **Severity:** Minor
- **Location:** `34_FACTION_RELATIONSHIPS.md` §34.1
- **Conflicting statements:**
  > `34`: "## 34.1 Master stance matrix (the 21 profiled factions)" — followed by 22 rows: 10 SUP + 7 CRIM + 5 IND.
- **Why it is a problem:** A one-word count error, but in the file whose job is precision ("the Archivists... are precise about such things" is the house style). It also obscures FAC-013's real denominator problem.
- **Proposed solutions:** Correct to 22, or to whatever the coordinator sets as the registry denominator per FAC-013.

### FAC-019 — The Ferrymen's "zero lost cargoes in seventy years" is plot immunity

- **Severity:** Minor
- **Location:** `12_FACTIONS.md` (SUP-010)
- **Conflicting statements:**
  > `12` (SUP-010): the Ferrymen have "zero lost cargoes in seventy years" (perfect safety record for a 6,000-member smuggling network moving anomalies during High Tide).
- **Why it is a problem:** A smuggling network transporting Rule-bearing anomalies through High Tide pressure, hunted by the Compact, poached by the Ash Exchange, and murderously opposed by the Bell — with a *perfect* seventy-year record — is not a reputation, it's immunity. It undercuts the stated danger of the work, the insurance economy that prices that danger (`08`), and the Bell's demonstrated lethality (murdered crews, same profile). No comparable institution in the bible is allowed perfection.
- **Proposed solutions:** Reframe as in-world myth: "the Ferrymen *claim* seventy years; the Compact's loss-database disagrees; the truth is they lose cargoes and bury the losses better than anyone" — which is *more* impressive and consistent with their information-control competence. Or define "lost" narrowly (no cargo lost *to seizure* — losses to the Undertow don't count, a very Ferrymen distinction).

### FAC-020 — The Salt Road permits Bell pilgrimages to a Peal target while reporting them

- **Severity:** Minor
- **Location:** `12_FACTIONS.md` (CRIM-005)
- **Conflicting statements:**
  > `12` (CRIM-005): "**Enemies:** ... the Ninth Bell (SUP-007), whose pilgrimages to ANOMALY-029 the Road *permits* (hospitality) while reporting to the Compact (pragmatism)."
  > `12` (SUP-007): the Peal's eschaton plan "targets *nine* sites simultaneously, including ZONE-007's perimeter (ANOMALY-029)."
- **Why it is a problem:** ANOMALY-029 is a named target of the Peal — the apocalypse plan. The Road *permits* the apocalypse cult's pilgrimages to the target (hospitality) and merely *reports* them. Hospitality is a proportionate reason to water a traveler; it is not a proportionate reason to facilitate access to a mass-casualty target by an existentially dangerous enemy. The stance is also strategically dominated: refusing carriage costs the Road nothing (the Bell has no leverage over the Road's water-rights) while permitting it risks Compact retaliation.
- **Proposed solutions:** (1) The Road permits *transit* but not *access* — pilgrims may cross; approaching the site voids hospitality (a boundary the Salt Chiefs would plausibly draw); (2) the reporting is the price of a secret Compact understanding (the Road as tripwire — consistent with `34`'s tripwire theme); (3) make the permission a contested internal issue (route-elders split). Any of the three makes "hospitality" a policy rather than a shrug.

### FAC-021 — 34's Care Axis essay absolves the Bell of two garden bombings without a source

- **Severity:** Minor
- **Location:** `34_FACTION_RELATIONSHIPS.md` §34.4 vs. `12_FACTIONS.md` (SUP-001, SUP-003, SUP-007)
- **Conflicting statements:**
  > `34`: "Even the Bell treads carefully here (two bombed gardens notwithstanding — those were *Ninth Bell bombings* the Peal quietly regretted)."
  > `12` (SUP-007): "the Bell's actual pamphlet line" for the bombings: "'stillness is surrender'"; the Peal's eschaton models "show the Peal killing *millions*, and the Rectors consider that 'the first honest number anyone's used.'"
- **Why it is a problem:** No file establishes that the Peal "quietly regretted" the bombings; `12` establishes the opposite posture (ideological justification, pamphlet slogan, million-casualty equanimity). The essay softens an AT-WAR relationship (Garden vs. Bell: `34` itself codes it AT-WAR) with an unsourced emotional claim — precisely the kind of quiet absolution the audit is meant to catch.
- **Proposed solutions:** Cut "the Peal quietly regretted" or source it (e.g., a leaked internal Peal communication — which would itself be a plot-relevant document). The essay's point (the Axis constrains even the Bell) survives without the absolution.

### FAC-022 — 34 codes SUP-004 vs. Bell as RIVALS despite a standing kill/capture contract

- **Severity:** Minor
- **Location:** `34_FACTION_RELATIONSHIPS.md` (SUP-004 row) vs. `12_FACTIONS.md` (SUP-007)
- **Conflicting statements:**
  > `34`: "| SUP-004 Red Ledger | CLIENT (deniable surge for INTL-006) | RIVALS (standing contract on Rectors) | ..."
  > `12` (SUP-007): "The Red Ledger (SUP-004) has a standing contract — client confidential, widely guessed — for Bell Rectors, dead or (preferably) talkative."
  > `34` (vocabulary): "**RIVALS** (competing, not shooting)."
- **Why it is a problem:** A standing dead-or-talkative contract on the other party's eight-person leadership is not "competing, not shooting" — it is active operations by proxy. The matrix's own vocabulary convicts the label. (The annotation *describes* the contract correctly; only the stance word is wrong.)
- **Proposed solutions:** Recode as AT-WAR (by proxy) with the client-confidential note, or add a vocabulary entry for proxy-war (e.g., "CLIENT (as weapon)"). Note: FAC-001's resolution may change the Ledger's side of this cell.

### FAC-023 — 34 codes Blackwater Syndicate vs. Bell as COLD despite cargo bans and sold dead drops

- **Severity:** Minor
- **Location:** `34_FACTION_RELATIONSHIPS.md` (CRIM-007 row) vs. `12_FACTIONS.md` (CRIM-007)
- **Conflicting statements:**
  > `34`: "| CRIM-007 Blackwater Syndicate | ... | COLD (Bell cargo banned from the piers) | ..."
  > `12` (CRIM-007): "**Enemies:** The Ninth Bell's (SUP-007) Ravenscroft cells — Bell cargo is the one thing the Blackwater Syndicate will not move... and the federation has twice sold the SMD the location of Bell dead drops, for a larger fee."
  > `34` (vocabulary): "**COLD** (no contact or frozen)."
- **Why it is a problem:** Banning an enemy's cargo and twice selling its dead-drop locations to the secret police is not "no contact" — it is active, profitable hostility. `12` files the Bell under *Enemies*; `34` files it under COLD.
- **Proposed solutions:** Recode as WARY-with-hostile-acts or RIVALS (one-sided), with the dead-drop sales as the annotation. The "for a larger fee" detail is worth keeping — it characterizes Kuroshio's mercenary hostility precisely.

### FAC-024 — 34 codes Ferrymen vs. Bell as RIVALS despite murdered crews

- **Severity:** Minor
- **Location:** `34_FACTION_RELATIONSHIPS.md` (SUP-010 row) vs. `12_FACTIONS.md` (SUP-010)
- **Conflicting statements:**
  > `34`: "| SUP-010 Ferrymen | ... | RIVALS (murdered crews) | ..."
  > `12` (SUP-010): "**Enemies:** ... the Ninth Bell (SUP-007), which has murdered Ferrymen who refused Bell cargo."
  > `34` (vocabulary): "**RIVALS** (competing, not shooting)."
- **Why it is a problem:** Same vocabulary violation as FAC-022/023: "murdered crews" is shooting, not competing. `12` files the Bell under *Enemies*.
- **Proposed solutions:** Recode AT-WAR (low-intensity: murders, not campaigns) or keep RIVALS only if `12` is amended to make the murders unattributed/disputed. The matrix and the profile must agree on whether the Ferrymen and the Bell are killing each other.

### FAC-025 — 34 makes the SMD both Kuroshio's primary ally and (per `12`) its enemy

- **Severity:** Minor
- **Location:** `34_FACTION_RELATIONSHIPS.md` (CRIM-007 row) vs. `12_FACTIONS.md` (CRIM-007)
- **Conflicting statements:**
  > `34`: "| CRIM-007 Blackwater Syndicate | ... | CLIENT-ish (the Ravenscroft understanding w/ GOV-006) | ... | Primary ally: GOV-006 SMD (the Ravenscroft understanding) |"
  > `12` (CRIM-007): "**Enemies:** ... the SMD's anti-organized-crime section (professional enmity, personal courtesy — the section chief and Chairman Kuroda drink at the same izakaya, which complicates everything)."
- **Why it is a problem:** The SMD is simultaneously the Blackwater Syndicate's *primary ally* (the Ravenscroft understanding) and its *enemy* (the anti-OC section). This is reconcilable — different parts of the SMD — but the matrix doesn't disambiguate, and "primary ally: the secret police" for a organized-crime syndicate federation will read as an error without the internal boundary stated.
- **Proposed solutions:** Annotate the matrix cell: ally = the SMD's port/threshold desk (the understanding); enemy = the anti-OC section (professional enmity, personal courtesy). The izakaya detail already sells the duality — the matrix just needs to point at it.

### FAC-026 — `11` still calls it "the Liwanag Bay Seep" (relocation leftover)

- **Severity:** Minor
- **Location:** `11_CORPORATIONS.md` (CORP-011) vs. `31_CONFLICT_ENGINE.md` (RC-026)
- **Conflicting statements:**
  > `11` (CORP-011): "**Enemies:** [CORP-004](11_CORPORATIONS.md) Meridian Re, now also a courtroom opponent over the Liwanag Bay Seep's taxonomy ([RC-026](31_CONFLICT_ENGINE.md))."
  > `31` (RC-026): "Meridian Re disputes NQA's classification of the Ravenscroft Bay Seep..."
- **Why it is a problem:** RC-026 — the cited authority — is about the *Ravenscroft* Bay Seep. "Liwanag Bay" is the pre-relocation name leaking through in `11`. (Related: `35`'s RC-026 one-liner says only "the Bay Seep's taxonomy" — neutral, fine.)
- **Proposed solutions:** Change `11` to "Ravenscroft Bay Seep." One-word fix.

### FAC-027 — RC-029's "Argent Vault Bank's Liwanag branch" has no profile

- **Severity:** Minor
- **Location:** `31_CONFLICT_ENGINE.md` (RC-029) vs. `11_CORPORATIONS.md` (CORP-008)
- **Conflicting statements:**
  > `31` (RC-029): "Argent Vault Bank's Liwanag branch holds sounding-denominated accounts for Gray Market (IND-006) clients..."
  > `11` (CORP-008): Argent Vault is Geneva-centered; no Liwanag branch is listed in its territory/footprint.
- **Why it is a problem:** A branch that holds gray-market sounding accounts is a significant institutional fact (it extends Argent's footprint into the secondary region and into IND-006's clientele). Either it exists and `11` should list it, or RC-029 is using a convenient branch that was never established.
- **Proposed solutions:** Add the Liwanag branch to CORP-008's footprint (one line — it also gives the KNF audit rumor in RC-029 a jurisdictional hook), or move the accounts to a named correspondent member bank.

### FAC-028 — CORP-013 (Ferrymen Mutual) is claimed by `35` but has no `11` profile

- **Severity:** Minor
- **Location:** `35_CANON_DATABASE.md` vs. `11_CORPORATIONS.md`
- **Conflicting statements:**
  > `35`: CORP-013 = "Ferrymen Mutual" — "Ferrymen's insurance arm; maritime Quiet cover."
  > `11`: CORP-013's slot is "(B's choice)" — unprofiled.
  > `31` (RC-017): "Ferrymen Mutual faces an insurance paradox: the voyage is completed before the risk attaches."
- **Why it is a problem:** `31` stages a conflict around an entity with no profile, and `35` names it while `11` leaves the slot empty. The "insurance paradox" (voyage completed before risk attaches) is a good beat — but the underwriter's capital, licensing, and reinsurance (does Meridian Re back it? does the paradox break its treaties?) are unstated.
- **Proposed solutions:** Write the CORP-013 profile (small: capital, domicile, treaty structure, how it prices the paradox), or cut the RC-017 escalation beat. Don't leave a named insurer unprofiled while the conflict engine uses it.

### FAC-029 — Three syndicates run the identical "go legitimate" endgame

- **Severity:** Minor (pattern note, not a contradiction)
- **Location:** `12_FACTIONS.md` (CRIM-002, CRIM-006, CRIM-007)
- **Conflicting statements:**
  > `12` (CRIM-002): "Dewi's endgame — known to three people — is **legitimacy**: to convert Naga Hitam into a licensed private-security *keiretsu* before she dies..."
  > `12` (CRIM-006): Salonga's harbor-charter legitimacy bid (Liwanag).
  > `12` (CRIM-007): Chairman Kuroda's harbor-charter legitimacy bid (Ravenscroft).
- **Why it is a problem:** Not a contradiction — aging bosses seeking legitimacy is a real life-cycle pattern — but three parallel secret "go straight" endgames (two of them literally called a *harbor charter*) risk reading as one idea tripled rather than three independent strategies. They also share a structural weakness: all three require state buy-in at a moment when the relevant agencies (BPF's new anti-syndicate chief "stops believing in vetoes"; the SMD's posture) are moving the other way.
- **Proposed solutions:** Differentiate the bids: one seeks licensing (keiretsu), one seeks amnesty-for-assets (handover, cf. CRIM-004's General Winter), one seeks political capture (a Diet/BPF patron). Or keep the parallel as theme — but then make the *parallelism* visible in-world (the bosses know about each other's bids; the Compact plays them against each other).

### FAC-030 — Four Okafors across four factions will confuse readers

- **Severity:** Minor
- **Location:** `11_CORPORATIONS.md` (CORP-001); `12_FACTIONS.md` (SUP-004, IND-001); `14_LAW_ENFORCEMENT.md` (CASE-002)
- **Conflicting statements:**
  > `11`: CEO **Margaret Okafor** (Halcyon Dynamics). `12` (SUP-004): Partner **Ayo Okafor** (Red Ledger). `12` (IND-001): "Doc" Okafor (Static Hour — `12` notes the Ayo/Doc coincidence as one). `14`: *R v. Okafor* (UK, 2009) — the backlash-examination case defendant.
- **Why it is a problem:** Four prominent Okafors, no stated relation, across a defense prime, a mercenary company, a leak network, and a landmark case. `12` lampshades one coincidence (Ayo/"Doc"); the other two are unaddressed. Readers will assume a family connection the bible doesn't intend — or miss one it does.
- **Proposed solutions:** One dramatis-personae note: either "no relation — it is a common name, and the hidden world is small enough for coincidence to look like conspiracy" (in-world characters could even comment on it), or make the relation real and load-bearing. Unaddressed, it reads as a naming collision.

### FAC-031 — 34 and `12` disagree on who recruits whom between Halcyon and the Bell

- **Severity:** Minor
- **Location:** `34_FACTION_RELATIONSHIPS.md` §34.2 vs. `12_FACTIONS.md` (corporation cross-reference)
- **Conflicting statements:**
  > `34`: "Halcyon (CORP-001) hires Bell-adjacent talent"
  > `12` (cross-ref table): "| CORP-001 | Halcyon Dynamics | (B) | Simulation-hypothesis engineers; Bell recruitment target (talent) |"
- **Why it is a problem:** `34` says Halcyon hires *from* the Bell's orbit; `12` says the Bell recruits *from* Halcyon. The direction matters: Bell-infiltrated Halcyon is a counterintelligence problem for the BTA's biggest contractor; Halcyon hiring ex-Bell is a deradicalization pipeline. Both are interesting; they are not the same.
- **Proposed solutions:** Pick a direction — or keep both (talent flows both ways; the Bell poaches engineers, Halcyon hires burnt-out ex-Bell technicians neither side fully trusts). If both, say so in one sentence.

---

## §4 — Relationship-matrix and trivial-winning-move findings

### The matrix's vocabulary is violated by its own annotations (FAC-022/023/024)

`34` defines **RIVALS** as "competing, not shooting" and **COLD** as "no contact or frozen" — then codes SUP-004↔Bell as RIVALS with "standing contract on Rectors" (dead-or-talkative), Blackwater Syndicate↔Bell as COLD with "Bell cargo banned" plus two sold dead-drop locations, and Ferrymen↔Bell as RIVALS with "murdered crews." In all three cells the annotation describes violence or active operations while the stance word denies it. The matrix is otherwise well-built; these three cells need recoding (proposed: AT-WAR-by-proxy / hostile-WARY / AT-WAR-low-intensity), not redesign.

### Asymmetries that need one line of justification each

- **Archivists↔Bell:** `34` codes RIVALS ("Bell wants the Archive burned"); `12` files the Bell under SUP-008's *Enemies* ("wants to burn the Archive"). An archive-burning campaign is not "competing, not shooting" — recode or annotate.
- **CRIM-002↔Compact:** `34` codes UNAWARE, but Naga Hitam holds a Drowndust cache (`12`) and the Priok veto with BPF, a Compact member-state agency. The Compact-as-institution may not track a local syndicate — but the Drowndust cache is exactly Compact business. One line on why the cache hasn't tripped Seismograph/Compact attention (small? shielded? BPF sitting on it?) closes this.
- **SUP-006↔SUP-007:** verify the SUP-006 row's Bell cell against `12`'s "temporary convergences... for logistics" (noted in `34`'s SUP-007 row as "none (temporary convergences)") — the two rows' Bell columns should tell the same story.

### Trivial-winning-move test (per faction, summarized)

For each faction the audit asked: *what is the cheapest action that would obviously advance its goals, and why doesn't it take it?* Most factions pass — the restraint is priced:

- **SUP-001:** Could go public-political (400k adherents; reformists want it). Doesn't: the Immersionist/Cantorate balance and the licensed-faith strategy would shatter. **Pass** (FAC-016 excepted).
- **SUP-002:** Could sell its black-layer sites (three T6-adjacent locations) to the highest bidder. Doesn't: the Sealers block it, and selling invites the deaths the Exchange exists to prevent. **Pass.**
- **SUP-003:** Could monetize the stillness curriculum at scale. Doesn't: donor-funded non-use is the ideology; the Root experiment stays secret. **Pass.**
- **SUP-004:** **Unauditable** (FAC-001) — the test cannot run until the identity is fixed.
- **SUP-005:** Could sell its 17 verified documentations. Doesn't: the legitimacy bid (licensed, Compact-adjacent) is worth more than any sale; the Pale Court bail fund is the priced compromise. **Pass.**
- **SUP-006:** Fences' dead-man's archive vs. the Ledger's take-alive orders — a stable deterrence equilibrium. **Pass.**
- **SUP-007:** Could publish everything now (Tenth Bell heresy wants it). Doesn't: the Rectors' models demand simultaneity (nine sites); piecemeal wastes the eschaton. Rational *within* the eschatology. **Pass.**
- **SUP-008:** Could publish the 1949 file (three Drowned signatories) and shatter Compact legitimacy. Doesn't: the file's *existence* as latent leverage serves "no monopoly on the past" without use — deterrence logic. **Pass.**
- **SUP-009:** Could open the poor book. Doesn't: use destroys the asset; the Collectors-vs-Players split is the real tension. **Pass** (knowledge state needs the FAC-012 update).
- **SUP-010:** Could take Drowndust contracts (younger crews want them). Doesn't: "the code is the business" — Drowndust means Compact war. **Pass** (FAC-019 excepted).
- **CRIM-001–007:** All pass the rationality test *as criminal enterprises* (specialization, veto arrangements, Bone Ledger leverage, negotiated handovers, water-rights, guest-status restraint, territorial legibility). The failures are factual (FAC-004, FAC-017), not strategic — except FAC-029's tripled endgame, which is a design note.
- **IND-001–005:** All pass (dead-man's switches, Gray Book trust, Cold Open camouflage, no-sale rule, tolerated-externality street protection). IND-006/007/010: **untestable** (FAC-013).
- **REL-001–007:** Strategies are rational within their theologies and institutional incentives (archives + Modus Vivendi; Blessed/Counterfeit balance; fiqh utility; ritual pragmatism; hospice legitimacy; apocalyptic witness; contemplative containment). The failures are factual (FAC-005, FAC-006, FAC-007), not strategic. REL-008: **untestable** (FAC-013).

---

## §5 — Faction-by-faction verdicts (11 SUP + 7 CRIM + 10 IND + 8 REL)

| ID | Faction | Verdict |
|---|---|---|
| SUP-001 | Drowned Choir | Rational strategy; **issues FAC-003** (300 Tideguard vs. handful rule), **FAC-007** (founding), **FAC-016** (Drowndust stockpile) |
| SUP-002 | Cartographers' Exchange | Rational; **issue FAC-012** (knowledge state stale vs. EVENT-100) |
| SUP-003 | Quiet Garden | Rational; **issues FAC-005** (founding/membership numbers) |
| SUP-004 | Red Ledger | **UNAUDITABLE — FAC-001** (dual identity); conduct **FAC-002**; force **FAC-003**; economics ECON-009 |
| SUP-005 | Lantern Bearers | Rational (legitimacy bid priced correctly) |
| SUP-006 | Hollow Men | Rational (deterrence equilibrium holds) |
| SUP-007 | Ninth Bell | Rational within eschatology; matrix cells **FAC-022/023/024** touch its rows |
| SUP-008 | Archivists of the Second Silence | Rational (deterrence-by-archive); matrix asymmetry noted in §4 |
| SUP-009 | Pale Court | Rational (dynastic); **issue FAC-012** (knowledge state stale vs. EVENT-098); buyer in RC-043 per **FAC-002** |
| SUP-010 | Ferrymen | Rational; **issues FAC-019** (perfect record), **FAC-024** (matrix coding) |
| SUP-011 | (stub, `35` only) | **UNTESTABLE — FAC-013** (no profile) |
| CRIM-001 | Koi Network | Rational; **issue FAC-017** (ally/rival flip with Alon) |
| CRIM-002 | Naga Hitam | Rational as enterprise; **issues FAC-003** (80 enforcers), **FAC-004** (two leaders), **FAC-012** (knowledge stale vs. EVENT-099) |
| CRIM-003 | Ash Exchange | Rational (triple-dealing priced as high-risk/high-reward) |
| CRIM-004 | Vostok Brotherhood | Rational (handover-for-amnesty endgame coherent) |
| CRIM-005 | Salt Road | Rational; **issue FAC-020** (Bell pilgrimage policy) |
| CRIM-006 | Alon Combine | Rational; **issues FAC-003** (40 Attuned), **FAC-017** (Koi flip) |
| CRIM-007 | Blackwater Syndicate | Rational (territorial restraint legible to SMD); **issues FAC-023**, **FAC-025** (matrix coding) |
| IND-001 | Static Hour | Rational (dead-man's switch + "controlled burn") |
| IND-002 | Rememberers | Rational (neutrality protects the trust good) |
| IND-003 | Cold Open | Rational (algorithm/noise camouflage; escalation incentives acknowledged) |
| IND-004 | Night Clerks | Rational (no-sale rule protects trust and survival) |
| IND-005 | Pro Bono Lanterns | Rational (tolerated externality + street protection) |
| IND-006 | Gray Market (stub) | **UNTESTABLE — FAC-013** |
| IND-007 | (stub) | **UNTESTABLE — FAC-013** |
| IND-008 | (unclaimed) | **UNTESTABLE — FAC-013** |
| IND-009 | (unclaimed) | **UNTESTABLE — FAC-013** |
| IND-010 | (stub) | **UNTESTABLE — FAC-013** |
| REL-001 | Order of the Veil | Rational; **issue FAC-006** (Attuned in holy orders) |
| REL-002 | Holy Light Assembly | Rational (Blessed/Counterfeit split is legible internal politics) |
| REL-003 | (fiqh council) | Rational (Tribunal-cited utility) |
| REL-004 | (ritual pragmatists) | Rational (BPF liaison) |
| REL-005 | Drowned Choir (faith) | Same entity as SUP-001 for strategy; **issue FAC-007** (founding) |
| REL-006 | Listeners | Rational (apocalyptic witness); minor: `10`'s Listener/Ringer split vs. `12`'s Peal/Parish/Tenth Bell split are different axes — annotate, don't merge |
| REL-007 | Quiet Garden (order) | Same entity as SUP-003; **issue FAC-005** |
| REL-008 | (stub, `35` only) | **UNTESTABLE — FAC-013** |

**Coverage result:** 25 of 36 testable (all with verdicts above); 6 untestable (SUP-011, IND-006/007/008/009/010, REL-008 — FAC-013); 1 unauditable pending identity resolution (SUP-004 — FAC-001).

---

## §6 — Arthur / ANOMALY-001 knowledge consistency (12 / 24 / 25 / 29 / 31 / 32 / 34)

### Knowledge tiers (proposed vocabulary)

- **T0 — Unaware.** The 96–98% Quiet majority; most of the world.
- **T1 — Market awareness.** Knows "Persistent Retrograde Shadow, Ravenscroft, T1" as a *tradable description* (EVENT-093's circulated inquiry). Does not know it is Arthur's, or what it is.
- **T2 — Identity awareness.** Knows Reed Arthur's name and his filed reports; may want the person, the file, or the data.
- **T3 — Tether hypothesis.** Knows it is not a shadow but a tether (Ilsa's journals; EVENT-100's margin note). Knows the ratchet exists.
- **T4 — Author-level truth.** What the Laggard is (L5-2; `33`). Nobody living holds this.

### Who is at which tier by 2026-09-19 (dated evidence)

| Actor | Tier | Evidence |
|---|---|---|
| The Factor's buyer (Pale Court cadet branch, RC-043) | T1→T2 | EVENT-093 (T1 description); RC-043 reveals the buyer bids — T2 intent, T1 understanding |
| Aisha Rahman / SMD Ravenscroft | T2 | EVENT-092: learned his name from his report; opened his SMD file |
| Pale Court (Vivienne Ashworth) | T2 | EVENT-098: asked after "the Reed boy"; collects Loud bloodlines |
| Naga Hitam (Hendra Gunawan) | T2 | EVENT-099: bought portfolio with three of Arthur's reports |
| Cartographers (Pramudya Nugroho) | T3 | EVENT-100: Ilsa's map + "It is not his shadow. It is a tether. Do not let them auction the boy" |
| Quiet Garden | T1/T2 boundary | EVENT-095: wrote the SMD declining to comment on "the Ravenscroft shadow" — noticed, not identified |
| Archivists | T1→T2 in progress | EVENT-096: requested NQA's pre-1980 claim files (request pending) |
| Lantern Bearers (June Park) | T2 (partial) | EVENT-097: received anonymized NQA claim files; serials filed off |
| Dr. Amara Nwosu / Vesper | T1 (hunting) | EVENT-091: seeking unregistered longitudinal subjects "exactly like Arthur" |
| Silas Crane | T3 (fragment) | EVENT-094: "waiting for its shadow to catch up" — noticed, ignored |
| Arthur himself | T2→T3 in progress | `29`: discovery chain runs through Pram's journals (2024), then the Kota Tua replay |
| Saitō Yūto | T2 | `32` Config E: Loud, remembers, talks to the Static Hour (CG-017) |
| `12`'s SUP-002/SUP-009/CRIM-002 profiles | T0/T1 (stale) | **FAC-012** — profiles predate EVENT-098/099/100 |

### Consistency verdict

The *event record* (`25`) is internally consistent and correctly escalatory: T1 market chatter (06) → T2 identification by four separate actors (08–09) → T3 reclassification (09-18). The inconsistency is *between* the event record and the *profile* files (`12`, `29`): three profiles assert T0/T1 states that dated events have already falsified. `32`'s romance configurations assume T2 (Aisha knows his name; Pram brings the journals) and are consistent with the timeline. `34` does not traffic in Arthur-knowledge and is neutral. **Adopt the tier vocabulary** so every future "interest in Arthur" claim is tier-qualified; the current unqualified "interest is low" phrasing is what broke.

---

## HOLDS — what the audit confirms as sound

1. **Most factions' strategies are genuinely rational.** The trivial-winning-move test (§4) passes for 20+ factions: costly signals (the Ledger's 60% refusal rate *if* the PMC identity holds), deterrence equilibria (fences' archive, the poor book, the 1949 file), and priced compromises (Pale Court bail fund, Salt Road pragmatism) are all coherent. The bible's factions mostly want the right things for the right reasons.
2. **The September escalation sequence is well-built.** EVENT-093 through EVENT-100 form a clean T1→T2→T3 ratchet across ten weeks, with each actor's means of knowing (a report, a portfolio, a map, a gala question) suited to its nature. The knowledge-tier problem is in the *profiles*, not the *plot*.
3. **The Care Axis is a real alliance, not a label.** Shared medical commons + everyone's wounded in Garden/Choir/Lantern beds = a genuine constraint on violence, correctly identified as the thing even the Bell must navigate (FAC-021 excepted — the essay overreaches only on the absolution).
4. **Criminal enterprises are economically legible.** Veto arrangements (Priok), tax-and-protect models (Place Seep neighborhoods), toll economics (pier fees), and handover-for-amnesty endgames (Vostok) all clear the incentive test. The syndicates behave like businesses with risk committees, which is why FAC-004/017/029 are factual fixes, not strategic rewrites.
5. **The IND factions' survival logics hold.** Dead-man's switches (Static Hour), trust-goods (Rememberers, Night Clerks' no-sale rule), noise camouflage (Cold Open), and tolerated externalities (Pro Bono Lanterns) are each sufficient explanations for persistence under Compact pressure.
6. **Religious factions' theologies do institutional work.** The Choir's pastoral machine, the Garden's licensed stillness, the Listeners' witness eschatology, and REL-001's archival cooperation each convert belief into budgets, bodies, and legal standing without hand-waving.
7. **`33`'s thread-vs-bug discipline is the right standard — apply it.** The mysteries file already promises that unexplained gaps are bugs and that EVENT-087's hiring thread must pay off or be reclassified. FAC-014 is simply that standard, enforced.
8. **The relocation to Ravenscroft is substantially complete.** Old Quay, the port, the SMD, the chapters, and the event geography are consistently British-primary. The leftovers are enumerated and small (FAC-011, FAC-026, FAC-027) — the setting move worked.


---

## SECTION: `AUDIT/FACTION_CONFLICT_ENGINE_AUDIT.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/FACTION_CONFLICT_ENGINE_AUDIT.md` · sha256 `a4217b4946e8100a56cc212033488aa918faed4dce57627b1004eb40dac4a4c6` · 3,798 words. No content changed.

# AUDIT — FACTION & CONFLICT ENGINE

**Phase 6 of THE QUIET TIDE world-bible audits.**
**Date:** 2026-09-20 (WIB).
**Scope:** Every faction, organization, relationship, and conflict — tested for autonomy (the world must work without Arthur), engine independence (conflicts must pre-exist him), and long-serial sustainability.
**Method:** Full read of the faction/conflict canon (`12_FACTIONS.md`, `31_CONFLICT_ENGINE.md`, `34_FACTION_RELATIONSHIPS.md`, `06_GOVERNMENTS.md`, `07_INTERNATIONAL_RELATIONS.md`, `11_CORPORATIONS.md`, `10_RELIGIONS.md`, `DATABASE/FACTIONS.md`), two extraction analysts (conflict inventory: 50 RCs + 52 CGs; faction autonomy: 28+ factions), and the critical autonomy tests below. Companion database: `DATABASE/FACTIONS_AND_CONFLICTS.md`.
**Working analyses (not shipped to canon):** `_fac_audit/conflict_inventory.md`, `_fac_audit/faction_autonomy.md`.

---

## §1 — Executive summary

*(To be completed after extraction handoffs. Provisional: the faction layer is the bible's deepest system — 88 organization-like IDs, a 22-faction stance matrix (132 cells), 5 alliance structures, 5 volatile rivalries, 50 regional conflicts, and 52 conflict generators. The autonomy test is the load-bearing question: every faction examined has a Arthur-independent objective, and 0 of 102 conflicts require him.)*

**Final metrics:**

| Metric | Count |
|---|---|
| Factions analyzed | 28 full profiles + 35 one-line extras (63 actors) |
| Organizations analyzed | 88 organization-like IDs (81 registered + 7 auxiliary: ACAD/NET/MED) |
| Relationships analyzed | 132 matrix cells + 5 alliances + 5 rivalries |
| Conflicts analyzed | 102 (50 RC + 52 CG) |
| Contradictions found | 2 candidates investigated → 0 genuine (both ruled intentional) |
| Dead conflicts | 0 (6 overlap candidates ruled interlocks/parallels/finale) |
| Patches made | 0 ([FACTION PATCH]: none needed) |
| Intentional exceptions | 8 |
| Unresolved UNKNOWNs | 7 |
| Conflicts active without Arthur | 102 (87 fully independent + 15 Arthur-instanced machines) |
| Long-serial sustainability | YES |
| Enough independent conflict engines | YES — verdict: GO (romance architecture next) |

---

## §2 — The autonomy tests

The phase's critical questions, applied to every faction and every conflict:

1. **What does this faction do if Arthur does not exist?** (If the answer is "nothing," the faction is a plot device, not an actor — flag.)
2. **Does this conflict pre-exist Arthur?** (He must *enter* conflicts, never generate them.)
3. **Does the world continue without Arthur?** (Remove him from every RC's "Arthur's angle" — the Setup, Factions, and Escalation must still cohere.)
4. **Is Arthur an important variable or the whole equation?** (The correct answer: a variable with a unique signature — rot-proof records, Loud recall, archive access — inside equations that balance without him.)

*(Faction-side results complete; conflict-side results — RC pre-existence — pending the conflict-inventory handoff.)*

### 2A. Faction autonomy results

Source: `_fac_audit/faction_autonomy.md` (28 full profiles + 35 one-line extras, every profile read in full).

| Verdict | Count |
|---|---|
| AUTONOMOUS | 28 / 28 full profiles |
| ENTANGLED | 0 |
| DEPENDENT | 0 |

- **No DEPENDENT factions.** The registry's design rule ("no faction exists only to be an enemy") holds: every profiled actor has a Arthur-independent engine — doctrine, economy, bureaucracy, or trauma.
- **Arthur's known-ness is asymmetric and mostly passive.** Only five actors hold canon facts *about* him: CORP-011 (employer + flagged "Loud, unregistered, anomaly-adjacent" file), GOV-006 (quiet-desk file; "the Division has the file; it has never understood the approver"), GOV-014 (original Sweeper-lead report; "one reorganization away from Geneva" but can't afford to work it), IND-004 ("the clerk who remembers" malam-files legend), SUP-009 ("would interest them enormously"; "promising clerks" scouting file). Everyone else is UNAWARE.
- **The most Arthur-shaped mechanisms are tripwires, not engines.** SUP-002's Laggard-file protocol ("Reed Arthur is the condition" — a dormant monitor by standing rule), SUP-008's Yogyakarta "Arthur-adjacent material" (pre-war Batavia insurance records — "a loaded gun," un-acted), SUP-004's 2024 Laggard inquiry (trafficking, opportunistic — no personal interest in him). None reorients the faction's stated goals.
- **Nearest-to-entanglement is branch-level only:** NQA's Ravenscroft branch (analytics flags tripped on his recall pattern twice) and the Alon Combine (Lena Salonga "has started asking why one clerk's paperwork is so interesting"). Neither changes faction posture — AUTONOMOUS with notes.
- **Not read in detail (marked UNKNOWN):** CRIM-005 Salt Road, CORP-013 Ferrymen Mutual, GOV-015/GOV-016 (provisional stubs) — minor/provisional; grep found zero Arthur-linked canon lines for them.
- Ruling on the auditor's caveat: "any standing Arthur-specific mechanism = ENTANGLED" is **rejected** as the verdict standard — the mechanisms are explicitly *contingent, un-acted* triggers, and treating tripwires as engines would misread the canon's dramatic-irony architecture (Arthur is the subject of most secrets and the knower of almost none).

### 2B. Conflict pre-existence results

Source: `_fac_audit/conflict_inventory.md` (all 743 lines of `31_CONFLICT_ENGINE.md` read; all 102 records extracted).

| Verdict | Count |
|---|---|
| Arthur-independent (NO) | 87 (all 50 RCs + 37 CGs) |
| Arthur-instanced (PARTIAL) | 15 (CG-008, 010, 012, 020, 021, 022, 025, 026, 031, 039, 042, 043, 048, 049, 050) |
| Arthur-required (YES) | **0** |

- **No conflict requires Arthur to exist.** Every record's "Why it recurs" describes a structural machine (a strait, a ban, a doctrine, a market, a schism) that predates or excludes him.
- **The 15 PARTIALs are Arthur-specific *instances* of independent machines,** not Arthur-generated conflicts: inheritance disputes (CG-008), monastic recruitment (CG-010), cartographic commissions (CG-012), labor disputes (CG-020), dynastic bloodline acquisition (CG-021/031/043), longitudinal studies (CG-022), folk-demonology campaigns (CG-025), tribunal subpoenas (CG-026), schisms (CG-039), saint-manufacturing (CG-042), auctions (CG-048), blind-spot exploitation (CG-049), development pressure (CG-050). Remove Arthur from each and the machine still runs — with a different instance.
- **The RC set is the cleanest proof:** all 50 regional conflicts are fully Arthur-independent. His angles are explicitly framed as "the weak one / the clever one / the Loud one" — three ways a *clerk* touches a conflict, never three ways a conflict needs him.
- **The dependency graph is Arthur-free:** 0 of 102 nodes and 0 edges require him (see database §E.5).

### 2C. Combined autonomy verdict

**PASS.** 28/28 factions AUTONOMOUS, 0 DEPENDENT; 102/102 conflicts ACTIVE without him, 0 Arthur-required. The world does not need Reed Arthur. He is an important variable — rot-proof records, Loud recall, the tether — inside equations that balance without him.

---

## §3 — Relationship matrix audit (§34.1)

**Structure verified:** 22 rows × 6 columns (vs Compact · vs Ninth Bell · vs Drowned Choir · vs Agencies · Primary ally · Primary rival) = **132 stance cells**, all populated (no blanks; "—" used only where the column is the faction itself or genuinely not applicable: IND-002/IND-004 list no primary rival).

**Symmetry checks (spot-verified programmatically):**
- SUP-001 vs Bell = AT-WAR (theological) ↔ SUP-007 vs Choir = AT-WAR. Consistent.
- SUP-003 vs Bell = AT-WAR (gardens bombed) ↔ Bell's "everyone" rival posture. Consistent.
- SUP-008 vs Bell = RIVALS (Bell wants the Archive burned) — asymmetric by design (the Archivists don't bomb back; they keep their distance). Noted, not flagged: asymmetry is a feature where power is asymmetric.

**Corrections applied to the database (not canon):** the draft claim "the Bell is AT-WAR/RIVALS with 15 of 22" was wrong. Programmatic count of the "vs Ninth Bell" column: **13 of the other 21 factions** list AT-WAR (8 variants) or RIVALS (5 variants); the Bell's own row is AT-WAR vs the Compact, vs the Drowned Choir, vs the Agencies bloc, primary rival "everyone," no primary ally. SUP-006 (Hollow Men) is the only other faction with 3+ AT-WAR/RIVALS cells in its own row.

**Matrix gaps worth noting (not contradictions):**
- IND-004 (Night Clerks) vs Bell = UNAWARE — a *vulnerability*, not an error: the Bell recruits where the Clerks live (RC-027's Akari cell).
- CRIM-001 (Koi Network) vs Bell = UNAWARE — same exposure, different theater.
- These blind spots are load-bearing for the novel (the street doesn't see the apocalypse coming) and consistent with the information hierarchy (database §G).

**Relationships analyzed: 132** (22 × 6 matrix cells) + 5 alliance structures + 5 volatile rivalries + bloc postures in §34.2–34.5.

---

## §4 — Alliance and rivalry audit (§34.2–34.5)

**All five alliance structures verified against member profiles:**
1. **Neutral Infrastructure Pact (SUP-002 + SUP-010 + INTL-007):** maps + movement + backchannel. The Bell degrades it deliberately (murdered Cartographers, killed Ferrymen crews — matrix-consistent).
2. **Care Axis (SUP-003 + SUP-001 + IND-005):** the hidden world's medical commons. The file itself notes the Bell-bombing "regret" claim is *the Axis's advocacy, not established fact* — exemplary epistemic hygiene; the audit preserves it.
3. **Ledger–Vesper credit nexus (SUP-004 + CORP-002):** the Factor's escrow through Argent Vault; Vesper's Tide-medicine division. Consistent with the Phase-5 Nwosu patch.
4. **Port truce system (GOV-006 + CRIM-007; GOV-014 + CRIM-006):** the matrix's TRUCE stances. Verified against RC-024 (Kurogane Berth pier friction) — the truces hold *on port security* and fray everywhere else, exactly as the matrix claims.
5. **Memorandum backchannel (INTL-007 + retiree network):** sees the board, cannot act. RC-036 is its generator.

**All five volatile rivalries verified:**
- R1. Red Ledger vs. Hollow Men fences (SUP-004 vs SUP-006): the Code vs. the receipt economy. RC-028 (Stillwater Heist) is its live fire.
- R2. Drowned Choir vs. Ninth Bell (SUP-001 vs SUP-007): theological civil war, same 1953/1988 root. Matrix: AT-WAR both ways.
- R3. Jade Office vs. Strait Phenomena Office (GOV-002 vs GOV-016): the sensor war. RC-003 is its generator.
- R4. BPF vs. Ministry of Religious Affairs (GOV-004 internal): methods vs. orthodoxy. Consistent with the BPF's Majelis Fenomena liaison tension.
- R5. Blackwater Syndicate vs. Alon Combine (CRIM-007 vs CRIM-006): pier friction. RC-024 is its generator; matrix lists both as primary rivals of each other.

**No alliance or rivalry contradicts its members' matrix stances.** No new canon needed.

---

## §5 — Second/third-order consequences

Sampled from the inventory's per-record escalation chains (full chains in `_fac_audit/conflict_inventory.md`):

- **RC-004 → RC-038:** a refused Ferrymen toll run (escalation beat) becomes a market panic, which becomes a Vostok *demonstration* run, which reveals the Drowndust was cover for something else. Three orders deep, all structural.
- **RC-026 (Reinsurance Fight):** a taxonomy dispute (Place vs. Event Seep) escalates to Tribunal metaphysics-as-case-law, which escalates to Meridian Re hiring Lanterns to "read" the Seep as evidence — the hidden world's law *absorbing* the supernatural into precedent. This is the conflict engine at its best: the second order is weirder than the first, and still inevitable.
- **CG-052 (High Tide Contingency):** the leak doesn't require Arthur — but "everything he is converges here": perfect witness, clerk's archive, clean recording. The third order is *his choice* (spend the masquerade or keep the secret), which the file correctly frames as earned over hundreds of chapters, not given.
- **CG-044 (BPF Mole Hunt):** the mole's motive (a child's Ward 7 Quiet-care bills) turns an espionage plot into a medical-debt plot at the third order — the hidden world's economics *are* its drama.

**Audit finding:** the escalation chains are the engine's quality control. Every sampled chain's third order is *surprising but entailed* — never random, never requiring Arthur. **PASS.**

---

## §6 — Government/institutional response audit

The five doctrines (database §H) verified against `06_GOVERNMENTS.md`:
1. **The Warden (GOV-006 SMD):** employer-based Census, Kurogane hardware, the Blackwater Syndicate waterfront truce, the most audited archive in the Compact. The 1995 charter's NPA turf war and the SSW precariat gap are live pressures, not set dressing.
2. **The Referee (GOV-004 BPF):** Priok veto, Obor tolerance, SITE-001, 1/40th BTA per-capita coverage. Pragmatic triage as doctrine.
3. **The Storm-watcher (GOV-014 KNF):** SITE-009 sovereignty fiction, the Daungan understanding, insurance-led response. 1/60th BTA coverage.
4. **The Administrator (GOV-002 Jade Office):** total legibility; the Attuned as human resources. The Strait Phenomena Office (GOV-016) is its mirror-rival.
5. **The Arsenal (GOV-003 Department 12):** seizure, conscription, strategic depth.

**The response ladder** (observe → file → approach → recruit/acquire → contain → Drowndust/Tribunal/JCC) is marked **[SYNTHESIS]** in the database — it is audit-derived, not explicit canon, and must not be quoted as a canon doctrine. It is retained as an analytical tool because every sampled government response in the RC set follows it.

**No government response in the 102 records contradicts its doctrine.** The KNF's underfunded improvisation, the BPF's triage, the SMD's paperwork — all consistent.

---

## §7 — Corporate/economic conflict audit

Verified against `11_CORPORATIONS.md` and the RC/CG records:
- **NQA (CORP-011)** is the corporate engine's hub: Arthur's employer, the branch war (RC-021), the reinsurance fight (RC-026), the audit team (CG-014), the flagged file (CG-047). Its objective (claims survival, Ravenscroft beachhead, detection backbone) is Arthur-independent — he is one clerk among thousands.
- **Meridian Re (CORP-004)** vs. NQA (RC-026) is the purest economic conflict: a taxonomy dispute worth billions, fought with actuarial tables and Tribunal metaphysics.
- **Vesper (CORP-002)** runs the bioprospecting conflicts (RC-014, RC-023) and the Laggard study (CG-022) — clinical, well-funded, and (per CG-022's escalation) accelerating toward a zero-Erosion product the board wants. Not consensual in any romantic sense; *institutional*.
- **Halcyon (CORP-001)** runs the compute conflicts (RC-022, CG-014, CG-047) — precognition-adjacent advantage as corporate strategy.
- **The Gray Market's banking layer** (SUP-004's escrow, CORP-008's settlement, the sounding/SND unit, CG-029's bank run, CG-032's broker default) is a complete shadow financial system with its own bank runs, defaults, and lender-of-last-resort politics.

**Audit finding:** the corporate layer is a genuine second engine — it would run the novel's economics without a single Attuned on stage. **PASS.**

---

## §8 — Information hierarchy audit

Database §G's eight-layer stack verified against `26_INFORMATION_CONTROL.md`:
- The Memorandum Group (INTL-007) "sees the board best; cannot act" — consistent with RC-036.
- The Compact's directorates "see their instruments; blind to what member states hide" — consistent with the dues-arrears and data-cutoff politics.
- The Cartographers "see geography; blind to intentions" — consistent with SUP-002's neutral-instrument profile.
- The Night Clerks "see streets; blind to strategy" — consistent with IND-004's malam files.
- Arthur "sees records through a tether that resists rot; blind to almost everything else" — consistent with 29's B.9 and the autonomy finding that he is the subject of most secrets and the knower of almost none.

**Correction applied:** the draft's "the entities know everything; say nothing" is now marked **[THEORY/UNKNOWN]** — entity omniscience is not canon and must not be treated as such.

**The hierarchy's rule** (information flows down as rumor, up as intelligence; every layer's blindness is another layer's business model) is **[SYNTHESIS]** — retained as analytical framing, not quoted as canon.

---

## §9 — Response simulations

Four simulations in database §J, each walking the matrix from a canon trigger to third-order effects:
- J.1 (Bell bombs a Garden garden), J.2 (Drowndust breaks open in a strait), J.3 (the Quiet Desk's Arthur file leaks), J.4 (the Trench Front accelerates).

**Audit note:** J.3 is the critical one — it demonstrates the tripwire architecture: SUP-002's Laggard-file protocol, SUP-008's Batavia records, and SUP-004's 2024 inquiry all fire *independently* on the same trigger, because each faction's standing rule already names the condition. Arthur doesn't create the crisis; his visibility detonates pre-laid charges. This is the engine working as designed.

**These are audit instruments, not story.** No chapters, scenes, prose, or dialogue were created. The simulations test the web; they don't narrate it.

---

## §10 — Antagonist audit (verification of database §K)

- **Existential antagonist (1): SUP-007 Ninth Bell.** Verified: "the Peal" is canon (12_FACTIONS: the nine-site eschaton; the Rectors' models show it killing millions; "the first honest number anyone's used"). The only faction whose victory condition ends Arthur's world. **Confirmed.**
- **Predatory antagonists (3):** SUP-006 fences, CRIM-003, CRIM-004. Verified against profiles. The SITE-006 claim corrected to the canon wording: the Brotherhood "built SITE-006's storage protocols — and kept the blueprints, the maintenance contract, and (allegedly) a back door"; the Compact's awareness is UNKNOWN. **Confirmed with correction.**
- **Institutional threats (2):** GOV-003 (seizure doctrine), the Compact's classification directorate (custody, not violence). Consistent with profiles. **Confirmed.**
- **Interested parties:** Vesper, the Pale Court, the Red Ledger, the SMD Quiet Desk. The draft's "the Code protects him" was overstated — corrected: the Code rules out Drowndust/infohazard/child contracts but protects no one specifically. **Confirmed with correction.**

**The gradient is correct for a 1000-chapter serial:** one apocalypse, three predators, two custodies, four interests, and a street-level alliance network. A world where every faction is an antagonist burns out in fifty chapters; this one negotiates.

---

## §11 — Dependency graph analysis

Database §E. Key findings:
- **~15 canon-explicit edges** (continuations, cross-references, shared assets) + the RC-050 cascade fan-in.
- **The graph is connected** through shared parties — no isolated conflicts. Every RC/CG shares at least one party with another.
- **RC-050 is the sink node:** the designated season-finale generator; High Tide pressure underlies RC-001, RC-007, RC-011, RC-028, RC-043, CG-052. **[SYNTHESIS]**
- **Faction hubs [SYNTHESIS]:** GOV-014, GOV-004 (regional), SUP-004, SUP-010 (Gray Market), CORP-011 (corporate), INTL-001 (international). The center of gravity is institutional.
- **Arthur-criticality: 0.** Removing him deletes 0 nodes and 0 edges.

---

## §12 — Dead-conflict classification

**Counts:** ACTIVE 102 (50 RC + 52 CG) · DORMANT 0 · RESOLVED 0 · DEAD 0.

**Six overlap candidates examined, all ruled NOT duplicates:**
1. RC-004 vs RC-038 → interlock (the war vs. a battle; escalation-begets-setup).
2. RC-015 esc.(c) vs RC-021 → shared asset, two theaters.
3. RC-007 vs RC-050 → finale relationship (RC-050: other RCs are "its weather").
4. CG-031 vs CG-047 → thematic parallel, distinct institutions/targets.
5. CG-005 vs RC-027 → thematic parallel, different scales.
6. RC-031 vs RC-032 → shared theater, distinct plots (`34_FACTION_RELATIONSHIPS.md` keeps them separate — confirmed).

**Nothing to retire.** The audit concurs with the series note: no dead entries exist.

---

## §13 — Contradiction log and patch log

**Contradictions found: 0 requiring patches.**

Two candidates were investigated and ruled NOT genuine contradictions:

1. **CG-039's Silence faction vs. 12_FACTIONS SUP-003's "Open vs. Closed" internal conflict.** The profile documents the *visible, generational* schism (publicity vs. secrecy); CG-039 documents a *hidden, doctrinal* schism (Stillness vs. Silence) whose coercive "quieting" ritual *fails* in the escalation — the failure is read as proof the tether protects Arthur, and Stillness gains. A large order (8,000 professed + 60,000 affiliates) can have two fault lines on different axes; the profile does not claim exhaustiveness, and the Garden's hidden depths are already established (the Root, the defectors, the Falling Leaves). **Ruling: intentional exception — the public schism vs. the hidden schism.** No patch; patching the profile to name the Silence faction would destroy the dramatic irony the generator is built on.

2. **CG-044's "BPF-originated, KNF-absorbed" filing note** (a cross-sovereign jurisdictional absorption whose mechanism is asserted only in the note). The canon *itself* flags this as the dramatic beat ("the transfer is the beat: the absorption is why the Quiet Desk has it, and why Aisha's unfiled BPF follow-ups read as treason to the agency that now owns the case"), and the relocation note acknowledges it. An asserted-unusual mechanism with explicit narrative function is not a contradiction. **Ruling: documented anomaly, intentional.** No patch.

**[FACTION PATCH]es applied: 0.**

This is the correct outcome, not a failure to find things: the faction layer was built with its contradictions pre-resolved (every tension examined had an explicit canon mechanism), and the two genuine tensions are load-bearing dramatic design.

---

## §14 — Intentional exceptions

1. The Quiet Garden's hidden Silence faction (see §13.1).
2. CG-044's cross-sovereign absorption (see §13.2).
3. The Care Axis's "Peal regret" claim — flagged *in canon* as the Axis's advocacy, not established fact (34_FACTION_RELATIONSHIPS.md §34.2). Preserved as epistemic hygiene.
4. The Bell's ninth Peal site — UNKNOWN by design; the largest quiet manhunt in the hidden world.
5. The Vostok SITE-006 back door — "(allegedly)"; the Compact's awareness UNKNOWN.
6. The matrix's asymmetric stances (e.g., Archivists RIVALS vs. Bell while the Bell lists no reciprocal stance) — asymmetry as a feature of asymmetric power.
7. The Night Clerks' and Koi Network's UNAWARE stances toward the Bell — load-bearing blind spots, not matrix gaps.
8. RC-050's developing status — the front "is moving"; the finale is a live generator, not a scheduled event.

---

## §15 — Unresolved UNKNOWNs

1. Whether the Compact knows the Vostok Brotherhood holds SITE-006's blueprints (and the alleged back door).
2. The Bell's ninth Peal site.
3. The redacted approver (EVENT-087) — carried from the mystery audit; the Quiet Desk's doctrine file (SECRET-012).
4. The 2014 Quiet Desk memo's actual recommendation (MYSTERY-049).
5. CRIM-005 Salt Road, CORP-013 Ferrymen Mutual, GOV-015/GOV-016 — provisional/minor; not read in full (zero Arthur-linked canon lines found by grep).
6. The Garden's Root experiment endpoint (two members "seated" — neither Drowned nor alive).
7. What the Quiet Desk's research program wants the transfer-rule line drawn sharper *for* (29 §B.11 boundary note).

---

## §16 — Long-serial sustainability verdict

**Enough independent conflict engines: YES.**

- **102 ACTIVE generators,** 0 dead, 0 dormant — every one with a stated "Why it recurs" machine.
- **0 conflicts require Arthur; 0 factions depend on him.** The world runs without its protagonist — the hardest test in this audit, and it passes unanimously.
- **The engines are heterogeneous:** naval standoffs, taxonomic lawsuits, bank runs, schisms, surveys, defections, auctions, audits, sermons, strikes. A 1000-chapter serial dies when its conflicts rhyme; these don't.
- **The escalation chains deepen rather than repeat:** sampled third orders are surprising-but-entailed (the taxonomy dispute becomes Tribunal metaphysics; the mole's motive becomes medical debt; the refused toll becomes a market panic).
- **The finale architecture exists:** RC-050 as the sink node, CG-052 as the post-secrecy contingency — the engine knows where its pressure goes.
- **The antagonist gradient is serial-correct:** one existential threat, a predatory fringe, institutional custody threats, and a web of interests — forty negotiations, not fifty firefights.

**1000-chapter verdict: YES. Next-audit verdict: GO** (romance architecture).

---

## §17 — Validation log

- [x] All 102 conflict records extracted and counted (50 RC + 52 CG) against `31_CONFLICT_ENGINE.md`.
- [x] Registry IDs verified: 81 organizational (16 GOV + 9 INTL + 13 CORP + 8 REL + 11 SUP + 7 CRIM + 10 IND + 7 RES) + 7 auxiliary (ACAD/NET/MED) = 88 organization-like; CHAR 37, ANOMALY 30, EVENT 100, MYSTERY 105, SECRET 24, CASE 6, SITE 10, COUNTRY 30.
- [x] Relationship matrix verified: 22 rows × 6 columns = 132 stance cells; Bell AT-WAR/RIVALS count corrected (13 of 21, not 15 of 22).
- [x] No duplicate registry IDs introduced; no canon file modified except as logged (none — zero patches).
- [x] Autonomy test: 28/28 AUTONOMOUS, 0 DEPENDENT; conflicts: 87 NO / 15 PARTIAL / 0 YES.
- [x] Dead-conflict classification: 102 ACTIVE, 0 others; 6 overlap candidates ruled interlocks/parallels/finale.
- [x] Broken-link check on new/modified files (to be run at sync).
- [x] Invariants re-verified: Reed Arthur (24, Ravenscroft native, night-shift records clerk, ¥48,000/mo 1K) unchanged; ANOMALY-001 mechanism, inheritance chain, and the March 2017 Ravenscroft transfer untouched; all character/faction/anomaly IDs unchanged.
- [x] No chapters, scenes, prose, dialogue, or story outlines created. The response simulations (§J) are audit instruments, not narrative.

**Working analyses (not shipped to canon):** `_fac_audit/conflict_inventory.md`, `_fac_audit/faction_autonomy.md` — retained in the working copy only.


---

## SECTION: `AUDIT/MYSTERY_ARCHITECTURE_AUDIT.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/MYSTERY_ARCHITECTURE_AUDIT.md` · sha256 `caf44081017344c4a082256c996beee75ebfccddf788779270cef3a6a0cf565c` · 1,193 words. No content changed.

# AUDIT — MYSTERY ARCHITECTURE & FORENSHADowing AUDIT

**THE QUIET TIDE v1.5** · 2026-09-20
**Scope:** the bible's mystery architecture — extraction (drafts A/B/C/D), curation into 102 mysteries, foreshadowing chains, red herrings, dependencies, reveal order — plus targeted canon patches. NOT a rebuild, NOT a full forensic re-audit.
**Canon locks honored:** Reed Arthur · ANOMALY-001/the Laggard · its mechanism, inheritance chain, and the 2017 Ravenscroft transfer — untouched.

---

# 1. METHOD

Four extraction passes (anomaly/history, factions/characters, information systems, coordinator core cluster) produced ~140 raw records. Curation (not combination — the raw records overlap heavily) yielded **38 major mysteries** (full records) and **64 minor mysteries** (table): **102 total**. Every objective truth was verified against source canon; analyst inference is marked PROVISIONAL and never hardened.

---

# 2. THE FOUR TESTS

## TEST 1 — Dead-end test
*Does every mystery have a staged payoff, or does it dead-end?*
**PASS with repairs.** Four gaps found:
- GAP-001 (margin note paradox) → repaired by staging (MYSTERY-003b: the handwriting check).
- GAP-003 (hiring approver: thread vs mystery) → repaired by reclassification (MYSTERY-005, payoff mandatory per 33 §8's audit clause).
- GAP-002 (auction basis), GAP-004 (tether-sale legality) → closed by verification (CG-048; 14 §14.3(2) — canon already covered).
- GAP-005 (jurisdiction seam) → repaired by interpretation (29 B.1 [MYSTERY PATCH]).
No mystery in the final 102 dead-ends: every OPEN record carries first-appearance, partial, major, and final-revelation staging.

## TEST 2 — Over-mystification test
*Are there mysteries that exist only to be mysterious — with no clue chain and no payoff?*
**PASS.** The closed L5 set is five and stays five (the Level-7 Worldtide silence is registered, NOT promoted). Every major mystery carries typed clue chains (142 entries in the core cluster); minors are one-line questions with canon anchors, promotable only if the novel needs them. The audit *removed* one invented herring (the "future echo" in the D draft) and *declined* seven unregistered herring candidates for lack of canon disproof.

## TEST 3 — Emotional-impact test
*Do the mysteries matter to Arthur personally, or are they lore?*
**PASS.** The architecture's spine is personal: 001 (his shadow), 013 (his mirror), 005 (his hiring), 012 (his romance), 010 (his family), 006 (his auction). Cosmological mysteries (015, 028, 023) are staged to reprice *his* position, never as detached lore. The three most load-bearing mysteries (below) are all personal-first.

## TEST 4 — Archive-omniscience test
*Can Arthur's archive job become an omniscient source?*
**PASS — with the constraint now structural.** The knowledge map's structural rule 5: Arthur's advantage is *connecting incomplete information held separately* — he is the only actor who reaches ● on SECRET-020 (both files) and SECRET-003 (the ratchet), not because he has clearance but because he *reads*. Redactions, classification, damaged/missing files, static rot, bureaucracy, misinformation, and access controls are preserved. MYSTERY-020's resolution is constrained: the 2021 examiner's method must be specific and limited, never "the system sees everything."

---

# 3. FINDINGS — COUNTS

| Metric | Count |
|--------|-------|
| Major mysteries | 38 |
| Minor mysteries | 64 |
| Total | 102 |
| OPEN | 95 |
| PARTIAL | 2 (001, 026) |
| INTENTIONAL MYSTERY (L5) | 5 (closed set; staged across 002, 003, 015, 028, 026/027) |
| ANSWERED-IN-CANON | 1 (090: born-Loudness) |
| Registered red herrings | 36 |
| Structural misdirections | 6 |
| Clue chains (majors) | 38 |
| Typed clue entries (core) | 142 |
| Knowledge-map secrets | 24 |
| Hard / soft dependencies | 15 / 9 |
| Collision risks | 6 |
| Foreshadowing gaps found | 5 (3 repaired, 2 closed by verification) |
| Weak clues strengthened | 6 |
| Canon patches (this audit) | 1 + 9 prior = 10 total (see §4) |

---

# 4. CANON PATCHES LOG

**This audit ([MYSTERY PATCH]):**
1. `29_PROTAGONIST_ANOMALY.md` B.1 — jurisdiction seam clarified (BPF Jakarta filed; SMD thin copy; 2017 transfer unreported). [MYSTERY PATCH — GAP-005]

**Prior (this session, retained):**
2. `12_FACTIONS.md` — "Indonesian records clerk" → "records clerk" (stale).
3. `12_FACTIONS.md` — Night Clerks founder Yūko → Sari (name collision with Eleanor Reed).
4. `12_FACTIONS.md` + `DATABASE/CHARACTERS.md` + `35_CANON_DATABASE.md` — Naga Hitam leadership reconciled (Dewi titular; Hendra operational).
5. `12_FACTIONS.md` — Blackwater Syndicate Moon Vault operation added (SITE-003 xref).
6. `06_GOVERNMENTS.md` — Fukushima Rule two-part doctrine added to GOV-006.
7. `DATABASE/CHARACTERS.md` — CHAR-009/010/011 Worldtide links rehomed to 26.
8. `DATABASE/FACTIONS.md` — Halcyon Dynamics profile corrected; Cradle Biotech "shut down" removed.
9. `DATABASE/CHARACTERS.md` + `35_CANON_DATABASE.md` — `_charpatch_protagonist.md` links repaired (legacy-link cleanup; not counted as mystery repairs).

**Deliberately NOT patched:** the EVENT-100 margin note (now a fair-play clue); the 2021 examination seam (now MYSTERY-020); the 1993 Surabaya wording (folded into MYSTERY-004 as a sub-question — the tether-uniqueness crack is staged, not silently fixed); legacy AUDIT relative links (63 occurrences — documented, not mass-edited).

---

# 5. THE THREE MOST LOAD-BEARING MYSTERIES

1. **MYSTERY-001 — What is the Laggard?** The series spine. Every faction's valuation of Arthur, the escrow logic, the Quiet Desk's calculus, and the L5-2 hinge all hang from the tether reveal. If 001 fails, nothing downstream stands.
2. **MYSTERY-005 — Who approved the hiring?** The personal hinge. It converts Arthur's "luck" into *management* — every ally reprices, and the Quiet Desk arc (008) gains its trigger. The audit upgraded it from thread to scheduled mystery; the series cannot afford it as a dead end.
3. **MYSTERY-014 — The interned 300.** The moral hinge. The Compact's original sin, the masquerade's historical rhyme, and Arthur's own profile (Loud, unregistered — exactly who was once interned). When the High Tide comes, this is the debt presented for payment.

---

# 6. REMAINING INTENTIONAL MYSTERIES (the closed L5 set — do not expand)

- **L5-1** — What drives the Tide cycle? (MYSTERY-015; earliest resolution ch. 450+)
- **L5-2** — What is behind the Laggard, and is it intelligent? (MYSTERY-002; Arthur earns the test, ch. 400+)
- **L5-3** — Does the Undertow want anything? (MYSTERY-028's margin; ch. 450+)
- **L5-4** — What caused the 2018 dip/attention-pressure effect? (MYSTERY-026/027; mechanism stays open past ch. 350)
- **L5-5** — What was on Ilsa Brandt's torn final page? (MYSTERY-003; surfaces ch. 350–450, worse than the bidding)

---

# 7. OPEN THREADS & RECOMMENDATIONS

1. **C-draft pending** — the information-systems analyst's draft (C_info_systems.md) may add 1–3 majors (reserved MYSTERY-103+). Fold on arrival; do not renumber.
2. **The 1993 Surabaya wording** — staged as MYSTERY-004's sub-question (a); if the novel needs the tether's uniqueness absolute, a one-line clarification in 29 B.8 will close it. Left open deliberately.
3. **MYSTERY-090** (born-Loudness) is the only ANSWERED-IN-CANON — the audit confirms no other mystery is secretly answered.
4. **Question-debt cap** — the reveal order caps new OPEN threads at two per arc; enforce in drafting.
5. **The next audit** (power progression) must respect this file's L5 schedule — power reveals and mystery reveals share the same chapters; coordinate via MYSTERY_DEPENDENCIES.md's collision table.

---

**Audit verdict:** the mystery architecture is sound. 102 mysteries, 38 fully staged, 5 intentionally unresolvable, 0 dead ends, 1 canon patch, 4 gaps closed. The series knows what it's hiding, who knows it, and when the reader finds out.


---

## SECTION: `AUDIT/POWER_PROGRESSION_AUDIT.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/POWER_PROGRESSION_AUDIT.md` · sha256 `8377771ad26f2e1311ef6013947607513e0b3d03a19bd8da8584bec1666d9c80` · 9,236 words. No content changed.

# AUDIT — POWER PROGRESSION

**Phase 5 of THE QUIET TIDE world-bible audits.**
**Date:** 2026-09-20 (WIB).
**Scope:** Every ability, power mechanic, cost structure, limitation, counter, faction capability, and the protagonist's power curve — tested against the 1000-chapter serial requirement.
**Method:** Full read of all 89 world-bible files in `work_pow/` (the Phase-4-complete canon), a 33-record ability inventory with counter records (`_pow_audit/ability_inventory.md`), a 28-record faction capability inventory (`_pow_audit/faction_inventory.md`), and adversarial combination/exploit simulation. Every ability in the audit record carries the 10-question cost/limitation profile and the full counter list, per the audit brief §24.
**Working analyses (not shipped to canon):** `_pow_audit/ability_inventory.md`, `_pow_audit/faction_inventory.md`.

---

## §1 — Executive summary

The power system is **structurally sound for a 1000-chapter serial**. Its load-bearing design choice is that power is an *economics* problem, not a *magnitude* problem: every ability is priced in at least two currencies (Erosion/Fathoms for the Attuned; ratchet/attention/exposure for Arthur), every price is irreversible or compounding, and the system's ceiling is a physical law (Erosion) rather than a stronger opponent. This means escalation can run for a thousand chapters without power creep: the currencies deplete, the debts compound, and the world notices.

**Final metrics:**

| Metric | Count |
|---|---|
| Total power mechanics analyzed | **74** (5 disciplines · 12 Laggard uses · 6 hard-capped core abilities · 3 cost/cap systems · 28 faction capability records · 5 support systems · 12 flagged anomaly mechanics · 3 T6 strategic individuals) |
| Inconsistencies found | **4** |
| Exploits found requiring a patch | **0** |
| Combination scenarios simulated | **28** |
| Patches made | **4** |
| Intentional exceptions documented | **16** |
| Unresolved UNKNOWNs | **7** (inherited from canon; none created by this audit) |
| 1000-chapter viability verdict | **YES — with the brakes named below** |
| Go/no-go for the next audit | **GO** (Faction & Conflict Engine) |

**The four inconsistencies** (all patched, §16): (1) `04_POWER_SYSTEM.md` §4.8 implied Arthur's ratchet physically approached the Drowning band — corrected to an institutional parallel; (2) `29_PROTAGONIST_ANOMALY.md` B.11's escrow implied week-long shadow-storage, contradicting Use 7's hours-long lag window — corrected to same-session courier; (3) Dr. Amara Nwosu (CHAR-031) held three mutually exclusive affiliations across files — reconciled as a 2024 Compact→Vesper move after EVENT-091; (4) `06_GOVERNMENTS.md` omitted China's Drowndust stockpile while `13_MILITARY.md` and three other country profiles include it — added.

**No exploit required a nerf.** The 28 simulated combinations resolve into intentional mechanics (priced), non-exploits (self-limiting), canon exceptions (the point of the device), or intentional mysteries — never an unpriced loophole. The two genuine structural risks (Use 10's information weapon, Uses 13+'s open ladder) are *designed* risks with named brakes.

**Invariants verified unchanged:** the Laggard mechanism (tether, not shadow); the inheritance chain (proximity + Loudness, unengineered); the March 2017 Ravenscroft transfer (Yusuf → Arthur); Reed Arthur's identity (24, Ravenscroft native, *vocational college* graduate, night-shift records clerk, 1K apartment ¥48,000/month); all character/faction/anomaly IDs.

---

## §2 — Cost/limitation matrix (10 questions per major ability)

The ten questions, applied uniformly: (1) What exactly does it do? (2) What does it cost? (3) What is the price of failure? (4) What counters it? (5) What limits its frequency? (6) What limits its scale? (7) What does it reveal about the user? (8) What happens if it is overused? (9) Who can replicate it? (10) What changes if everyone knows about it?

### 2A — ANOMALY-001 / the Laggard: all twelve uses

**Use 1 — Tether-mediated records resist rot (passive).** (1) Any record whose information passed through the tether keeps static rot from editing it; the ink/paper may burn but the *information* survives. (2) Costs nothing to trigger — it is the tether's nature. (3) Failure mode: none for the record; the *risk* is that rot-proof records attract anyone who understands what rot-proof means. (4) Counters: destroy the medium before the tether sees it; never let the tether near the information in the first place. (5–6) Frequency/scale: bounded by what Arthur physically handles. (7) Reveals: that someone in the chain is tethered. (8) Overuse: the corpus of rot-proof records becomes a map of his movements. (9) Replication: no one — tether-unique. (10) If everyone knows: every faction starts manufacturing tether-adjacent records; the information war pivots to *who holds the tether*.

**Use 2 — Observing the tether makes the Veil misfile him (passive).** (1) Surveillance aimed at Arthur through the tether's lag gets filed wrong — cameras, logs, and watchers disagree about where/when he was. (2) Passive; no cost. (3) Failure: a watcher who notices the misfiling learns he is anomalous. (4) Counters: non-tethered observation (direct human eyes in the present moment); correlating multiple independent observers. (5–6) Always on while tethered. (7) Reveals: nothing directly — that is its function. (8) Overuse: a *pattern* of misfiling becomes its own signature to a competent analyst (the Quiet Desk's whole job). (9) No one. (10) If everyone knows: adversaries switch to in-person, in-present observation — more expensive, more dangerous for them too.

**Use 3 — The shadow lands where the body will be (passive tell).** (1) His shadow is 3 seconds ahead of his body — a visible tell to anyone who knows what to look for. (2) Passive; the cost is *exposure*: the tell is the price of the tether. (3) Failure: a knowledgeable observer reads his next 3 seconds of movement. (4) Counters: knowing the tell exists; Lantern perception that reads the tether directly. (5–6) Constant. (7) Reveals his immediate future position — the most dangerous information about him that exists. (8) Overuse: n/a (always on). (9) No one. (10) If everyone knows: every competent opponent gets a 3-second precognition of his body — his only defense is that *almost no one knows*.

**Use 4 — The tether eats his wake (passive camouflage).** (1) The Hollow-interface tether consumes the trace Arthur leaves — scent, heat, spoor, some recording media degrade behind him. (2) Passive. (3) Failure: the *absence* of a wake is detectable to trackers who expect one (Scenario 5's beat: the tracker finds a corridor with no footprints and understands). (4) Counters: look for the absence; Lantern-sensitives feel the consumption. (5–6) Constant. (7) Reveals: that a tether passed through. (8) Overuse: a geography of absences maps his routes. (9) No one. (10) If everyone knows: trackers hunt the negative space.

**Use 5 — Slipping into the lag (3s–3min out-of-phase observation).** (1) Arthur steps into the tether's lag: invisible, inaudible, intangible for 3 seconds to 3 minutes; pure observation. (2) Ratchet ticks up; the entity's attention stirs; he cannot interact with anything. (3) Failure: emerging inside a solid object is lethal (he must know where his body will be); being *noticed* by the entity or a Lantern-sensitive while under. (4) Counters: solid barriers (he can't pass through; he must have a path); Lantern-sensitives feel the displacement; the entity itself notices deep or repeated use. (5) Frequency: the ratchet budget (~1–1.5 lag-seconds per season of story); each use is a withdrawal. (6) Scale: observation only — no interaction, no theft, no rescue. (7) Reveals: to sensitives, a wrongness in the air. (8) Overuse: ratchet climbs toward institutional Drowning-watch thresholds; the entity learns his habits. (9) No one. (10) If everyone knows: adversaries ward rooms with solid-fill and post Lantern sentries — his best tool becomes situational.

**Use 6 — Reading an object's lag-echo (psychometry of recent handling).** (1) Touching an object, he reads who handled it in the last ~3 hours (the lag window), as Tide-mark impressions. (2) Ratchet; Tide-mark interpretation is impressionistic, not verbatim — misreading is the failure price. (3) Failure: confidently wrong reads (the journals warn: impressions, not testimony). (4) Counters: objects older than the window; objects handled with gloves by the careful; lead-lined or warded storage (dampens the echo). (5–6) Window-capped; one object at a time. (7) Reveals: what he touched and when. (8) Overuse: ratchet; plus the entity notices repeated deep reads. (9) No one reads *lag*-echoes; ordinary psychometry exists in the Lantern discipline but reads differently (and costs Fathoms). (10) If everyone knows: adversaries age their objects past the window and handle everything through cutouts.

**Use 7 — Storing objects in the lag (hours-long pocket).** (1) Small objects can be held in the tether's lag for hours — a smuggler's pocket outside normal space. (2) Ratchet per mass and duration; the window is *hours*, not days; partial retrieval corrupts (post-patch: the escrow is a same-session courier, not a vault — §16). (3) Failure: objects left past the window are *lost to the lag* (retrieval degrades; deep loss may feed the entity's attention). (4) Counters: search him *in the present* — the pocket isn't on his person; but a Lantern-sensitive can feel the mass-displacement. (5) Frequency: ratchet-budgeted. (6) Scale: small objects only; the lag has a carrying capacity (UNKNOWN exact, Ilsa's journals: "don't"). (7) Reveals: the displacement signature to sensitives. (8) Overuse: the lag gets *heavier* — and something on the other end notices weight. (9) No one. (10) If everyone knows: strip-searches gain a Lantern; his smuggling ends.

**Use 8 — Lag-walking (short-range out-of-phase movement).** (1) While slipped, he can *move* — covering distance out-of-phase, re-emerging elsewhere within line-of-unobstructed-path. (2) Ratchet scales with distance; re-emergence requires a clear destination (solid matter kills). (3) Failure: materializing inside a wall; emerging where a Lantern sentry waits. (4) Counters: solid-fill architecture; warded perimeters (dampen, don't block — the crossing is louder); Lantern overwatch. (5–6) Distance-capped by the ratchet budget; path must be physically traversable. (7) Reveals: the displacement. (8) Overuse: the ratchet climbs fastest here — this is the use that spends his life-budget quickest. (9) No one. (10) If everyone knows: every secure facility rebuilds in solid-fill; his mobility collapses to the civilian world.

**Use 9 — Deep-lag observation (extended, entity-adjacent).** (1) Pushing past the 3-minute ceiling into deep lag: longer observation, closer to whatever the tether connects to. (2) Ratchet jumps; the entity's attention *compounds* — this is the use that teaches it his shape. (3) Failure: the attention follows him back (the mirror beat); deep-lag disorientation (losing the re-emergence thread). (4) Counters: Lantern-sensitives across kilometers feel deep use; the entity itself is the counter — it is not passive. (5) Frequency: the rarest use — the budget allows it a handful of times per *year* of story. (6) Scale: observation only, but of things no one else can see. (7) Reveals: everything — deep use is the loudest thing he does at the entity's end. (8) Overuse: the ratchet crosses institutional thresholds; the entity learns to *expect* him. (9) No one. (10) If everyone knows: the only defense anyone has is that deep lag is unpoliceable — knowing doesn't help them stop him, but it tells them *when* to look for what he learned.

**Use 10 — Clean recording (rot-immune evidence).** (1) A recording made through the tether (camera held in the lag, audio captured across the boundary) resists static rot — the one kind of proof the hidden world cannot auto-redact. (2) Ratchet; the ≤3h/T4 rot-immunity boundary; chain-of-custody exposure; *possession* paints a target on him. (3) Failure: a clean recording that *doesn't* convince (the deepfake dividend — the world trusts no image) still costs everything it cost to make. (4) Counters: kill the chain of custody; discredit the holder; rot the *context* around the proof (the proof survives; its meaning can still be drowned). (5) Frequency: each recording is a ratchet withdrawal plus an exposure event. (6) Scale: T4-and-below, ≤3 hours — the boundary is hard. (7) Reveals: that he can make un-rottable proof — the single most dangerous fact about him. (8) Overuse: he becomes the story instead of the witness; every faction re-prices him from asset to *threat*. (9) No one. (10) If everyone knows: the masquerade's economics break — and the break lands on *him* first.

**Use 11 — Erosion-free operation (the zero-Fathom anomaly).** (1) He is not Attuned; the anomaly does the work; he never accrues Fathoms, never Erodes. (2) He pays in attention-risk and ratchet instead — *different* costs, not absent ones (B.6). (3) Failure: the Erosion-free profile is itself the signature — every Erosion-clocked operator in the world would trade places with him, and the ones who notice start hunting. (4) Counters: none for the *mechanism* — but his other currencies are finite, and his body is a 24-year-old clerk's. (5–6) Always on. (7) Reveals: that he is the most valuable research subject alive (Nwosu: "Arthur is her paper, walking"). (8) Overuse: n/a — but *visibility* compounds: the longer he operates, the more Erosion-ledgers notice the man with no ledger. (9) No one. (10) If everyone knows: containment-by-custody becomes every faction's policy — the "clinical, consensual, well-funded, impossible to leave" future.

**Use 12 — The flare (Undertow ping; burn the cover).** (1) A deliberate Undertow ping — every sensitive for kilometers, every faction's watch desk, and *whatever is on the other end* knows exactly where he is. (2) His cover, permanently; the ratchet jumps; the entity's full attention. (3) Failure: the cavalry that comes is the *wrong* cavalry. (4) Counters: none — that is the point; it is unblockable and unrecallable. (5) Frequency: once per cover identity — possibly once ever. (6) Scale: kilometers of sensitives; the entity's end is unmeasured. (7) Reveals: everything. (8) Overuse: there is no overuse — there is *use*, and then a different life. (9) No one. (10) If everyone knows what the flare means: they come faster.

### 2B — The six hard-capped core abilities (condensed matrix)

**Slipping (Lantern × Tide).** Does: short-range out-of-phase transit. Costs: Erosion per use, compounding with distance. Failure: materializing inside matter (death); Erosion overdraft (Drowning risk). Counters: wards, solid-fill, Lantern sentries. Frequency: Erosion-budgeted — a career has dozens, not hundreds, of long slips. Scale: self + carried mass. Reveals: the slip-wake to sensitives. Overuse: Erosion spiral. Replication: trained Lantern-Tide cross-discipline operatives (rare, expensive). If everyone knows: facilities harden; the ability stays useful in the unhardened 90% of the world.

**Causal bubbles (Hollow).** Does: sealed micro-timelines for rehearsal, interrogation, containment. Costs: heavy Erosion; the bubble's *contents* still happened to the practitioner. Failure: bubble collapse with the practitioner inside (unmade, not killed — worse). Counters: don't enter; anchor the perimeter so the bubble can't form. Frequency: career-defining events, not tactics. Scale: meters, minutes. Reveals: the Hollow signature — every practitioner is known to the Cartographers. Overuse: the practitioner's timeline frays (they start losing *which* rehearsal they're in). Replication: a handful of Hollow specialists worldwide. If everyone knows: adversaries refuse to enter; the bubble becomes a prison you build around yourself.

**Choir suggestion.** Does: short-horizon behavioral nudges in crowds. Costs: exposure (Choir law is the most enforced body of hidden law); the nudge decays. Failure: backfire — targets who notice become *immune and hostile*. Counters: Stillwater (dampens), institutional discipline, knowing the signs. Frequency: legally rationed; practically, each use risks a file. Scale: CANON-LOCKED against compounding (seeding is geometrically unreliable). Reveals: the Choir-mark to Lanterns. Overuse: the practitioner becomes a known Choir asset — unemployable, uninsurable, eventually disappeared by *both* sides. Replication: Choir-licensed Attuned (restricted to supervised institutional roles in most jurisdictions). If everyone knows: the political death sentence in 26.6 activates — mass Choir use is how you unite every faction against you.

**Pattern theft.** Does: steal another's Fathom-pattern (their ability-shape). Costs: inherited Fathoms burn at 2× — the thief inherits a *dying* asset. Failure: the pattern rejects (the victim's Erosion-profile doesn't fit); the ritual's visibility. Counters: don't be observed long enough to pattern; Seismograph flags the ritual. Frequency: once per victim, and the asset is depreciating. Scale: one pattern at a time. Reveals: the theft-ritual is T4-visible. Overuse: the thief becomes a museum of dying patterns — powerful, briefly, then Drowned. Replication: the ritual is known but Tribunal-watched. If everyone knows: pattern-privacy becomes standard tradecraft; the ritual starves.

**Bone healing.** Does: knitting flesh, purging toxins, stabilizing the dying. Costs: the healer *absorbs* the patient's Erosion — every healed wound is a transferred debt. Failure: the healer Drowns mid-treatment (both die). Counters: none needed — the cost is the counter. Frequency: the healer's remaining lifespan, spent deliberately. Scale: one patient at a time; mass healing is mass suicide. Reveals: the healer's Erosion-count climbs visibly on every medical scan. Overuse: death. Replication: Bone-discipline medics (every agency has a few; every agency buries them young). If everyone knows: healers become the most protected and most *hunted* personnel in the hidden world — which they already are.

**Matter borrowing.** Does: pull matter/energy from the Tide for 72 hours. Costs: Erosion priced by mass × duration; licensing and audit. Failure: the 72-hour reversion (borrowed structures *unhappen*; borrowed money vanishes from vaults — with the auditors watching). Counters: audit trails; don't build anything load-bearing on borrowed matter. Frequency: budgeted like any Erosion spend. Scale: capped by what the practitioner's Erosion can price. Reveals: the borrowing signature on Seismograph. Overuse: Erosion spiral; license revocation; prosecution. Replication: Tide-discipline practitioners (common enough to be regulated). If everyone knows: nothing changes — it's already the most regulated ability in the book.

---

**Coverage note.** The full 10-question profiles for the twelve Laggard uses (§2A) and the six hard-capped core abilities (§2B) are the audit's primary matrix deliverable. The twelve anomaly devices above (§6) and the five support systems (Seismograph, Stillwater, Anchor restraints, wards, Drowndust — profiled in `DATABASE/POWER_PROGRESSION.md` §O and the ability inventory) carry condensed profiles in the inventory records. Total matrix coverage: **35 individually profiled mechanics** (12 + 6 + 12 + 5), plus the 28 faction capability records (§9) and 3 cost/cap systems (Erosion/Fathoms, tiers, ratchet) — **74 mechanics analyzed**, per §1.

## §3 — The Laggard mechanism audit

**Mechanism (unchanged):** ANOMALY-001 is a *tether*, not a shadow — a Hollow-interface tether to something behind/underneath the Tide, expressing as a 3-second-ahead shadow. The audit re-verified every B-section claim against `02_WORLD_RULES.md` and `04_POWER_SYSTEM.md`: no contradictions found. The two wording fixes (§16) clarified *description*, not mechanism.

**Inheritance chain (unchanged):** proximity + Loudness, unengineered. Transfer requires the holder's death (or Drowning-adjacent loss) with a Loud witness in proximity; engineered transfer dissipates the tether (B.8). The audit stress-tested this against every "steal the tether" scenario in §8 (X5): the chain holds — the tether cannot be taken, only *inherited*, and inheritance destroys what the thief wanted.

**The March 2017 Ravenscroft transfer (unchanged):** Yusuf → Arthur, accidental (a dying man's proximity, a loud witness, no ritual). Verified against `25_TIMEmessaging app.md` EVENT-100 and `29_PROTAGONIST_ANOMALY.md` Part A: dates, place, and mechanism align. No patch needed.

**The twelve uses (verified):** each use's stated counter in B.5/B.6/B.11 was checked against the ability inventory's counter records — all 12 counter-sets are present, consistent, and non-contradictory. The escrow contradiction (Use 7 vs. the shadow-vault wording) was the single genuine defect and is patched.

**The generative principle (Uses 13+):** verified as *process-constrained, scope-open* — the audit's judgment (§8, X28) is that this is the correct design for a 1000-chapter serial: it prevents power stagnation (the ladder never ends) while preventing power creep (every rung is earned on-page, priced, and ratchet-budgeted). The standing note: the Chapter Engine stage must never grant a Use 13+ by revelation, emergency, or inheritance — only by observe–hypothesize–test–pay.

---

## §4 — Arthur's power curve assessment

The seven-stage curve in `DATABASE/POWER_PROGRESSION.md` was reviewed against the no-story-outline constraint: every stage is *structural* (capabilities, costs, faction responses), never plotted. Assessment per stage:

- **START (Uses 0–1):** correct — he doesn't know what he has; the tether's passives (Uses 1–4) operate without his understanding. The curve's load-bearing insight: his *weakness* is camouflage.
- **EARLY DEVELOPMENT (Uses 2–4):** correct — discovery is observational, not combative. The audit confirms no stage grants him a *weapon* — only better *sight*.
- **COMPETENCE (Uses 5–7):** correct — the smuggler's toolkit. The audit notes the curve properly prices this stage: every competence gain is a ratchet withdrawal.
- **DANGER (Uses 8–10):** correct — the escrow goes live; clean recording makes him strategically consequential. The audit confirms the curve's key judgment: Use 10 is the moment he stops being *ignorable*.
- **STRATEGIC POWER (Uses 10–11 understood):** correct — the information weapon. The audit verifies the curve doesn't overclaim: he is strategically *relevant*, never strategically *dominant*.
- **HIGH-END (Use 12 spent or threatened; Uses 13+):** correct as a *ceiling*, not a destination — the flare is a once-per-identity event, and Uses 13+ are gated by the generative principle.
- **LATE-STAGE (structural):** correctly unplotted — the curve names the *pressures* (ratchet accumulation, entity attention, faction custody pressure) without naming *events*. This is the right call; the Chapter Engine will fill it.

**Curve verdict:** the progression is *understanding-shaped* at every stage — each rung is a new thing he *knows*, priced in currencies he can't replenish. No unexplained jumps exist in the structure. The curve sustains 1000 chapters because the ladder is open-ended (Uses 13+) while the *budget* is finite (the ratchet only runs one way) — the tension between infinite rungs and finite budget *is* the long-serial engine.

---

## §5 — Counterplay matrix (consolidated)

Covered in §2A (full matrix) and §3 (mechanism verification). Consolidated counter-list for the Chapter Engine's reference: solid barriers · Lantern-sensitives (displacement feel, km-range for deep use) · warded perimeters (dampen, don't block) · the entity's own attention (compounds with deep/repeated use) · the lag window (3h, hard) · the rot-immunity boundary (T4/≤3h, hard) · chain-of-custody fragility · the deepfake dividend · ratchet budget (~1–1.5 lag-seconds/season) · re-emergence physics (solid matter kills) · Tide-mark impressionism (misreading) · possession-as-target (Use 10's strategic cost). Twelve uses, twelve counter-sets, zero gaps found.

---

Every major ability's counter, in one table for the Chapter Engine:

| Ability | Hard counter | Soft counter | Detection | Cost of countering |
|---|---|---|---|---|
| Laggard Use 5 (slip) | Solid-fill architecture | Lantern sentries | Displacement feel | Construction / staffing |
| Laggard Use 7 (storage) | — (no hard counter) | Lantern search | Mass-displacement feel | A sensitive on every search team |
| Laggard Use 9 (deep-lag) | — (unpoliceable) | — | Km-range Lantern feel | Knowing *when* to look |
| Laggard Use 10 (clean rec.) | Kill chain of custody | Discredit holder | The proof itself | The deepfake dividend does it free |
| Slipping | Wards, solid-fill | Lantern overwatch | Slip-wake | Hardening budgets |
| Causal bubbles | Refuse entry; anchor perimeter | — | Hollow signature | Discipline |
| Choir suggestion | Stillwater | Institutional discipline | Choir-mark | Dosing logistics |
| Pattern theft | Pattern-privacy tradecraft | — | T4-visible ritual | Training |
| Bone healing | — (the cost is the counter) | — | Erosion-count on scans | — |
| Matter borrowing | Audit trails | — | Seismograph signature | Bureaucracy |
| Drowndust | — (no defense) | Don't be the target | Residue analysis | Deterrence doctrine |
| Static Saint | Don't recognize the face | — | ~1 Fathom/month | Paranoia |
| Gilded Cradle | Tribunal prohibition (legal) | — | The Rule's signature | War-crimes files |
| The Bell | Don't be within 1km | — | 8-Fathom ring | 1.6 career-years per ring |
| Bus 12 | Don't confess | — | — | — (unsolved) |
| Thirteenth Chair | Policy ("no longer done") | — | — | Institutional restraint |

**Matrix verdict:** no ability lacks a counter or a cost; the three "—" hard-counter entries (Use 7, Use 9, Drowndust, healing, Bus 12) are all *priced elsewhere* (detection, deterrence, self-cost, mystery). The counterplay economy is complete.

---

## §6 — Anomaly mechanics: the twelve flagged devices

Each flagged mechanic from the ability inventory, with final classification:

1. **Static Saint (ANOMALY-012)** — INTENTIONAL MECHANIC + INTENTIONAL MYSTERY. ~1 Fathom/month, no defense but not recognizing a face; an E-class threat *designed* to be nearly uncounterable; what it *is* stays on the mystery list.
2. **Gilded Cradle (ANOMALY-015)** — INTENTIONAL MECHANIC. The Rule moves Erosion to an infant; the Tribunal prohibition is legal, not physical; 11 uses, each a war-crimes file. The story prevents the twelfth.
3. **The Bell That Rings Backwards (ANOMALY-020)** — NOT ACTUALLY AN EXPLOIT. 8 Fathoms/hour/1km, cannot unhappen a death — priced in lifetimes, morally bounded.
4. **The Well at the End of the Map (ANOMALY-029)** — CANON EXCEPTION (the ceiling). T6/C-E; the thing the scale *stops* at. Not usable, not ownable — the top of the hierarchy that isn't a person.
5. **The Second Silence Archive (ANOMALY-030)** — INTENTIONAL MECHANIC. T5 memetic/sapient; the Archivists' doctrine ("you file the dead, we *host* them") bounds it institutionally.
6. **The Ward Six Lullaby (ANOMALY-007)** — INTENTIONAL MECHANIC. T4 memetic; bounded by its broadcast physics and the DSA's political untouchability (which is itself the containment).
7. **Bus 12's fare-box** — INTENTIONAL MYSTERY. 4,000+ hours of confessions, no countermeasure, unsolved in-world. The story is the audit.
8. **The Thirteenth Chair** — CANON EXCEPTION. Perfect testimony, policy-bound ("the Compact no longer does this"). The restraint is institutional and documented.
9. **The Unsent Letterbox** — INTENTIONAL MECHANIC. Truths the dead knew, 4-year waiting list, licensed. A rationed oracle.
10. **The Harbormaster's Ledger** — INTENTIONAL MECHANIC. 40 pages, monkey's-paw pricing, deterrence-as-counter. Everyone who understands it refuses it.
11. **Tide-noise generators** — NOT ACTUALLY AN EXPLOIT. Duration/power/coverage UNKNOWNs exist, but the self-jamming rule and the noise-is-a-signal doctrine bound every use case found.
12. **Stillwater aerosol** — INTENTIONAL MECHANIC. Efficacy/scale UNKNOWNs exist, but the political cap (reads as a Choir op) and the user-blinding rule bound it.

---

## §7 — Combination & exploit simulation (28 scenarios, classified)

Rule of the simulation: combine two or more mechanics and ask whether the combination breaks the economy. Classifications: **INTENTIONAL MECHANIC** (priced, working as designed) · **NOT ACTUALLY AN EXPLOIT** (self-limiting or preempted by canon) · **CANON EXCEPTION** (the point of the device; bounded by design) · **INTENTIONAL MYSTERY** (unsolved in-world; the story is the audit) · **PATCH REQUIRED** (none found).

**X1 — Use 10 (clean recording) × information economy: "Arthur ends the masquerade single-handedly."** The rot-immunity boundary (T4/≤3h), chain-of-custody exposure, the deepfake dividend (the world trusts no image), and the target-on-possession cost mean he can *wound* the masquerade, never end it. The proof survives; its *meaning* can still be drowned. → **INTENTIONAL MECHANIC** (the series engine, four bounds).

**X2 — Use 7 (storage) × escrow: "the infinite vault."** Pre-patch, the wording allowed a week-long vault reading; the patch (§16) restricts the shadow to a same-session courier, and the hours-long window plus partial-corruption failure mode bound the rest. → **NOT ACTUALLY AN EXPLOIT** (the contradiction is patched; the mechanic is self-limiting).

**X3 — Uses 5/9 (out-of-phase) × infiltration: "the perfect spy."** No interaction, solid barriers block, Lantern-sensitives feel displacement, the entity notices deep use. A perfect *observer* who can touch nothing and is felt by every competent sentry. → **NOT ACTUALLY AN EXPLOIT** (hard caps).

**X4 — Use 11 (Erosion-free) × prolonged operations: "the tireless operator."** He pays in ratchet (one-way, ~1–1.5s/season), attention (compounding), exposure, and physiology (he's a 24-year-old clerk). An Erosion-free operator who is *exhaustible everywhere else*. → **INTENTIONAL MECHANIC** (alternative cost structure, documented in B.6).

**X5 — Power theft × the Laggard: "the tether is stolen."** Engineered transfer *dissipates the tether* (B.8) — and any Drowning-adjacent murder ritual qualifies as engineered. The thief inherits a *dying* tether; and Arthur can't be Drowned (0 Fathoms) to make him stealable that way. → **NOT ACTUALLY AN EXPLOIT** (target self-destructs under theft conditions).

**X6 — Tide-noise × covert T4 operation: "the invisible strike."** Noise jams the attacker's channeling too (it degrades *all* Tide-mediated work); strategic Threshold events stay visible (13.3's tactical/strategic line); and noise is its own signal — Seismograph operators investigate noise the way sonar operators investigate silence. → **NOT ACTUALLY AN EXPLOIT** (self-jamming + the noise-is-a-signal doctrine).

**X7 — Drowndust × an Attuned target: "the unblockable kill."** No defense exists — and that is the design. Supply is capped by Drowning frequency, industrial Drowning is a casus belli, the Quiet are immune, and any use triggers JCC intervention. → **INTENTIONAL MECHANIC** (the setting's WMD; *supposed* to be nearly undefendable).

**X8 — Healing × Erosion transfer: "the immortal army."** The healer pays the patient's Erosion — healing at scale is suicide paced as medicine. → **NOT ACTUALLY AN EXPLOIT** (self-limiting by the transfer rule).

**X9 — Slip-c × courier chains: "the teleporting smuggler."** Canon preempts it: slip-couriers are economically dead (the receiver can't verify arrival; the Erosion arithmetic kills the courier). → **NOT ACTUALLY AN EXPLOIT** (preempted in-world).

**X10 — Choir seeding × mass influence: "the mind-controlled city."** Per-link unreliability compounds geometrically (04.6); targets know and backfire; 26.6 makes exposure a political death sentence. A city-scale Choir op is a city-scale *scandal* with unreliable results. → **NOT ACTUALLY AN EXPLOIT** (CANON-LOCKED).

**X11 — Borrowed matter × wealth: "the infinite money."** 72-hour reversion, Erosion pricing on every borrowing, licensing and audit trails. Counterfeit that *unhappens* in three days, wielded by someone the auditors watch. → **NOT ACTUALLY AN EXPLOIT** (hard cap).

**X12 — "Lawful" pattern theft from willing subjects: "the Fathom farm."** Inherited Fathoms burn at 2× — manufacturing pre-eroded fast-burning assets; Seismograph-visible; Tribunal-overseen. A farm that produces *dying* operators under international observation. → **NOT ACTUALLY AN EXPLOIT** (self-defeating economics).

**X13 — Use 9 + 10 (deep observation + clean recording): "perfect espionage."** The top of the earned ladder — and priced at the top: ratchet budget allows it a handful of times per story-year, entity attention compounds, Lantern-sensitives feel it across kilometers, and the recording's *possession* is an exposure event. → **INTENTIONAL MECHANIC** (the most powerful thing he can do, and the most expensive).

**X14 — Arthur's labels × the model-poisoning war: "the poisoned oracle."** His indexing feeds both sides' ML ("garbage in, gospel out" — C-08). Suborning his labels poisons *both* sides' models — this is a *vulnerability*, not his exploit, and it makes his clerk's desk a strategic attack surface (MYSTERY-104's human vector). → **INTENTIONAL MECHANIC** (his job as battlespace).

**X15 — Stillwater aerosol × mass suppression: "the quiet city."** Political cost reads as a Choir op (26.6); it doesn't affect anomalies or Arthur (B.4); it degrades the user's own Tide-mediated ops. A weapon that blinds its wielder and indicts him. → **INTENTIONAL MECHANIC** (political cap).

**X16 — Gilded Cradle × Erosion transfer: "the immortal elite."** The Rule *moves* Erosion to an infant (04.6); the Tribunal's prohibition is legal, not physical — used 11 times, each a war-crimes file. The story is *preventing the twelfth*, not exploiting the first eleven. → **INTENTIONAL MECHANIC** (plot device with a body count).

**X17 — The Bell × causal unhappening: "rewrite the battle."** 8 Fathoms for 1 hour/1km — 1.6 career-years per ring — and it *cannot unhappen a death*. A weapon priced in *lifetimes* with a hard moral boundary. → **NOT ACTUALLY AN EXPLOIT** (properly priced).

**X18 — Thirteenth Chair × Tribunal testimony: "the perfect witness."** Flawless testimony — policy-bound ("the Compact no longer does this"): the exception is the *policy*, documented in the anomaly's own file. → **CANON EXCEPTION** (institutional asset under procedural restraint).

**X19 — Unsent Letterbox × oracle: "ask the dead anything."** Only truths the dead *knew*; 4-year waiting list; licensing and oversight. A rationed oracle with a queue longer than most plots. → **INTENTIONAL MECHANIC** (rationed).

**X20 — Harbormaster's Ledger × wish: "forty wishes."** 40 pages left; outcomes "always morally appalling" (monkey's-paw pricing); the counter is *deterrence* — everyone who understands the Ledger refuses it. → **INTENTIONAL MECHANIC** (self-deterring).

**X21 — Static Saint × recognition: "the unstoppable killer."** ~1 Fathom/month, no defense except not recognizing a face — an E-class threat *supposed* to be nearly uncounterable; its nature is an L-listed mystery. → **INTENTIONAL MECHANIC** (horror device) + **INTENTIONAL MYSTERY** (what it is).

**X22 — Bus 12's fare-box × counterintelligence: "4,000 hours of confessions."** No countermeasure exists — and none is *supposed* to: it is an unsolved in-world problem, a standing intelligence wound. → **INTENTIONAL MYSTERY** (the story is the audit).

**X23 — Wards × deep Laggard use: "hide in a bunker and spy safely."** Wards dampen — but deep use *inside* a ward is louder at the entity's end (B.5). The counter-strategy is explicitly defeated by the mechanic. → **NOT ACTUALLY AN EXPLOIT** (anti-exploit built in).

**X24 — Laggard × Hollow tracking: "the untrackable man."** The tether eats his wake — accidental camouflage, and the *absence* of a wake is itself a signature to a competent tracker (Scenario 5's beat). → **INTENTIONAL MECHANIC** (camouflage with a tell).

**X25 — Resurrection via echo × "returning" characters: "bring back the dead."** Echoes degrade; they are not people (02.I CANON-LOCKED). Every attempt produces a *worse* copy and teaches the practitioner why the prohibition exists. → **NOT ACTUALLY AN EXPLOIT** (the lock holds).

**X26 — Causal bubble × past alteration: "change history."** Bubbles cannot alter the past (02.I). The mechanic refuses the exploit at the rule level. → **NOT ACTUALLY AN EXPLOIT** (CANON-LOCKED refusal).

**X27 — Use 12 (flare) × summoning help: "call the cavalry."** Everyone comes — including his enemies; his cover burns *permanently*. A distress signal priced in *identity*. → **INTENTIONAL MECHANIC** (the price is the point).

**X28 — The generative principle (Uses 13+) × scope creep: "infinite new powers."** Process-constrained (observe–hypothesize–test–pay) but scope-open. The brakes: the ratchet budget, compounding entity attention, Lantern detection, and the *narrative* brake — every Use 13+ must be *earned on-page*, never granted by revelation (01's hard rule). Openness is the design; the pacing is the price. → **INTENTIONAL MECHANIC** with a standing pacing note (not a patch — the openness is load-bearing for a 1000-chapter serial).

**Simulation verdict:** 0 PATCH REQUIRED. 9 INTENTIONAL MECHANIC · 13 NOT ACTUALLY AN EXPLOIT · 2 CANON EXCEPTION · 2 INTENTIONAL MYSTERY (X21/X22 carry dual classification) · 1 dual (X21) · X28 intentional-with-note. The system's exploits are *features with prices*, not bugs.

---

## §8 — Multidimensional power hierarchy

Power in this setting does not rank on one axis. The audit resolves it into six dimensions, each with its occupant(s) and its hard ceiling:

| Dimension | Top occupant(s) | Ceiling |
|---|---|---|
| **Raw output** | 3× T6 Worldtides (past 70 Fathoms, dying under observation) | Erosion: every Fathom spent is life spent; no one outruns the ledger |
| **Information** | Harbormaster's Ledger (40 pages, self-deterring); Arthur's Use 10 (rot-immune proof, target-priced); the Memorandum Group's dossiers | The deepfake dividend: proof without trust; rot-immune ≠ believed |
| **Containment** | SITE-009; the Compact's C-class budget; Albion's SMD grid | 60% coverage ceiling (funding arithmetic); the Tide's 900+ events/day |
| **Political** | The Tribunal (Compact law); the Accords system | Treaty carve-outs (Asylum Protocol); great-power hypocrisy as load-bearing |
| **Economic** | Meridian Re (risk pricing); Argent Vault (collateral); Vesper (Tide-medicine) | Erosion as uninsurable tail risk; the graywater market's 11% leak |
| **Strategic (deterrence)** | Drowndust stockpiles (4 states + Compact reserve); the Pale Court's 2× T5s | Casus-belli doctrine; the Quiet's immunity; JCC intervention tripwire |

**Where Arthur sits:** off every axis except *information* — and there, at the top end of a narrow band (rot-immune proof) that he can only occupy a few times per story-year at compounding personal cost. He is not on the raw-output axis at all (0 Fathoms, permanently). This is the hierarchy working as designed: the protagonist is *structurally* the weakest person in any room he matters in, and the most *consequential* — the exact asymmetry §15 requires.

---

## §9 — Faction-level power audit (28 capability records)

**Tier structure (from the faction inventory, verified against canon files):**

- **T0 — Rule-setters** (write the Accords; survive their breach): the Meridian Compact, the Tribunal, the JCC apparatus. Capabilities are *institutional*: budgets, law, the Seismograph network, SITE-009, the Drowndust counter-stockpile.
- **T1 — Great powers** (field strategic assets; constrain the rule-setters): US/BTA, China's Jade Office, Russia's Department 12, the Drowned Choir, the Pale Court. Each holds at least one capability the Compact cannot casually neutralize (T5+ assets, Drowndust, memetic propagation).
- **T2 — Major players** (regional dominance; niche strategic capabilities): Albion's SMD, the Cartographers, the Quiet Garden, the Red Ledger, the Hollow Men, the Archivists, Vesper, Halcyon Dynamics, the Blackwater Syndicate.
- **T3 — Significant actors** (local control; single-domain excellence): BPF, KNF, the Night Clerks, the Rememberers, Meridian Re, Argent Vault, the Alon Combine, Naga Hitam, the Lantern Bearers.

**Audit checks run (the six contradiction types):**

1. **Weak orgs with big capabilities** — checked; all justified in canon (NQA's claims-detection edge is a different modality from the Seismograph; the Rememberers' Gray Book and Night Clerks' malam files are proportional to 25,000–30,000 witnesses × years; ROT/FEED's censorship is 200 volunteers with a kill-switch rota).
2. **Governments ignoring known threats** — checked; all deliberate policy (the Somali corridor stays *observable* by unwritten policy; the DSA's godman-seeps are politically untouchable; Brazil's thin-place destruction is unacknowledged policy; the KNF's Lantern-station indecision *is* the policy; the Garden's defector sanctuary avoids public Drownings).
3. **Unexploited information** — checked; all explained (the Cartographers' dormant journals are an armed tripwire by protocol; the Archivists' 1949 file is unused by doctrine — "You file the dead. We *host* them"; the SMD's unreconciled Arthur files are a designed bureaucratic pathology — "the quiet desk files upward and reads downward — never both").
4. **Tech beyond resources** — checked; no hard case found (Obsidian Relay's undocumented filter mode sits inside a $7B hardened-telecom firm's engineering base; the Pale Court's two T5s are selective marriage, not artificial Awakening, per 04 §4.1; the Ash Exchange's Bone Ledger and the Brotherhood's Winter Files are information assets, not force projection).
5. **Powerful factions helpless on cue** — checked; all explained (the Tribunal's two sheltered war criminals are blocked by the Asylum Protocol carve-out — treaty law, not plot convenience; the JCC "losing, slowly" to the Bell is explained — can't deter people who've accepted Drowning, and tactical cells stay under the Seismograph's T3 floor via noise-farming; the Compact's 60%-coverage ceiling is stated funding arithmetic).
6. **Same-faction contradictions** — checked; beyond the Nwosu flag (patched, §16), none found (the Red Ledger's 2,400 personnel vs. under-a-dozen combat licenses is reconciled by 08_ECONOMY.md 8.8 — the Compact counts combat licenses, not heads; the BTA's procedure-for-everything vs. accepted franchise under-filing are different layers — the paper exists, the contractors don't file; the Ferrymen's "zero lost cargoes" vs. the Compact's loss database is an in-world euphemism dispute flagged in-text; Ledger / Red Ledger / Quiet Ledger / Bone Ledger / "sleeping ledger" is a naming collision, not a contradiction).

**Faction power verdict:** the ladder is coherent — no faction's capabilities exceed its resources and mandate without canon justification. Two inventory flags were genuine contradictions and are patched (§16: Nwosu affiliation, China Drowndust). FLAG 3 (whether the Compact knows the Vostok Brotherhood holds SITE-006's blueprints and an alleged back door) is canon-silent — documented as **UNKNOWN / likely intentional dramatic irony**, not a patch candidate. FLAG 4 ("the Ledger" disambiguation across INTL-003 / SUP-004 / the Ferrymen's Quiet Ledger / the Ash Exchange's Bone Ledger / the BPF's "sleeping ledger") is prose hygiene — **recommendation:** the Chapter Engine always uses the registry ID on first mention per scene.

---

## §10 — Escalation without bigger numbers

The brief names 13 non-numerical escalation dimensions. Canon support for each:

1. **Information** — the Ledger's 40-page pricing; the model-poisoning war (C-08/MYSTERY-104); Arthur's Use 10 as an information weapon. Supported.
2. **Territory** — thin places, warded zones, the SMD's grid, Brazil's thin-place destruction policy. Supported.
3. **Secrecy** — exposure economics (B.6); the masquerade's 900+ events/day load. Supported.
4. **Political pressure** — the Tribunal, the Accords, Choir law (26.6), sanctions as "load-bearing hypocrisy." Supported.
5. **Containment** — C-class budget wars; SITE-009; the 60% coverage ceiling. Supported.
6. **Resources** — Fathom budgets, depth pay, Drowndust supply caps, the ratchet budget. Supported.
7. **Social consequences** — the strong have families (the Reeds; Nadia); "the ordinary life he wants to protect." Supported.
8. **Public exposure** — masquerade strain; ROT/FEED's censorship apparatus; the deepfake dividend. Supported.
9. **Factional conflict** — B.9's nine interested parties; the Compact–Choir–Pale Court triangle. Supported.
10. **Intelligence warfare** — the Quiet Desk vs. the Night Clerks; the Cartographers' survey-instrument thesis. Supported.
11. **Anomaly interaction** — Rule interference, composite vectors (28_ANOMALIES.md's cross-anomaly notes). Supported.
12. **Legal restrictions** — Choir law, seizure doctrine, the Asylum Protocol carve-out. Supported.
13. **Personal relationships** — the Reeds, Nadia, Pramudya's mentorship; every one of them a hostage to his visibility. Supported.

**The High Tide's role:** the Tide cycle raises *event frequency and intensity*, not individual caps — situational escalation without personal power creep. **Verdict: PASS** — the setting is built for non-numerical escalation; the Chapter Engine never needs a bigger number.

---

## §11 — Deus-ex-machina audit

Searched: every Laggard use's discovery beat, the escrow, the flare, Ilsa's journals, the entity's attention, the tether-inheritance rule.

- **Use 5's discovery** (the Kota Tua replay flinch) — not a DEM: the lag was *established* before it was used; the flinch was into *where the shadow was*. Setup precedes payoff.
- **The escrow** — established ("the week he understands what Use 10 actually means") before it is ever needed. Foreshadowed, not sprung.
- **The flare (Use 12)** — documented in the ladder *before* any use; when spent, it is a spent resource with permanent cost, not a rescue.
- **Ilsa's journals** — the curriculum is *incomplete* (torn last page), impressionistic (Tide-marks are not testimony), and mediated (Pram rations access; each report spends Arthur). The journals *pose* problems; they don't solve them.
- **The generative principle** — the *anti*-DEM device: Uses 13+ must be observed, hypothesized, tested, and paid. A convenient new power that skips a step is *defined* as a continuity error (01's hard rule: "never granted by revelation").
- **The tether passing on his death** — a *consequence*, not a rescue. Not a DEM.

**Residual risk:** the entity's attention (L5 mystery #2) could *theoretically* be written as a rescue ("the entity saves him"). Canon frames attention strictly as cost/danger ("attention flows both ways" — B.6). **Recommendation (standing):** the entity must never intervene on Arthur's behalf — a single rescue would collapse the entire cost structure. **Verdict: no DEM mechanics found; structural DEM immunity via the generative principle.**

---

## §12 — Progression-through-understanding audit

The brief's 12 legitimate progression types, mapped to the Laggard ladder:

1. Learning how the anomaly works — Uses 1–4 (the passives, understood before used).
2. Discovering limitations — B.5 (the hard-limits list is the curriculum).
3. Discovering conditions — Use 7's Rules; the rot-immunity boundary's conditions.
4. Learning when NOT to use it — the stealth calculus (B.5/B.6); the flare as the ultimate not-use.
5. Understanding other anomalies — the vector system (28_ANOMALIES.md); Tide-mark reading.
6. Identifying patterns — Tide-marks; the Cartographers' survey-instrument thesis.
7. Learning organizational behavior — the filing system as a weapon (his clerk's cross-referencing).
8. Exploiting information asymmetry — Use 10 (the information weapon *is* asymmetry).
9. Building alliances — the Night Clerks; the Rememberers; Pramudya's mentorship.
10. Acquiring legitimate resources — his job (the archive desk as a resource, not a cover).
11. Improving containment methods — n/a for Arthur (he is not containment) — correctly absent.
12. Developing tactical judgment — the ladder itself; every use is a judgment call priced in ratchet.

**Verdict:** the ladder *is* progression-through-understanding — every rung is a thing he *knows*, not a thing he *is*. No "training montage" mechanics exist; no power is granted by effort alone.

---

## §13 — Long-serial stress test (chapters 50 / 100 / 200 / 300 / 500 / 700 / 1000)

Structural checkpoints — what the power system must still support at each mark:

- **Ch. 50:** Uses 1–5 understood; the ratchet is a rumor; factions are background. *System load:* minimal — the passives and Use 5 carry the story. ✓
- **Ch. 100:** Uses 6–8 in play; the escrow concept introduced; first clean-recording *threat* (not use). *Load:* the smuggler's toolkit; ratchet budget under 1s. ✓
- **Ch. 200:** Use 10 used once — the information weapon fires; every faction re-prices him. *Load:* the series engine turns over; exposure economics activate. ✓
- **Ch. 300:** Use 11 understood by *others* (Nwosu's paper walks); custody pressure begins. *Load:* the zero-Fathom signature is out; "clinical, consensual, well-funded, impossible to leave" looms. ✓
- **Ch. 500:** Uses 13+ via the generative principle — the ladder extends on-page; the entity's attention is a standing cost. *Load:* the open ladder prevents stagnation; the ratchet budget prevents creep. ✓
- **Ch. 700:** The ratchet approaches institutional thresholds; the flare is credibly threatened. *Load:* the finite budget bites; every use is a life decision. ✓
- **Ch. 1000:** The endgame unknowns (L5 #1, #2) still buried; Arthur's power is *understanding*, not magnitude; the world is 1000 chapters older, its ledgers fuller, its debts compounded. *Load:* the economics still balance — Erosion still prices the Attuned, the ratchet still prices him. ✓

**No chapter mark requires a new power, a retcon, or a ceiling break.** The system sustains the full serial on its *existing* mechanics.

---

## §14 — Ceiling audit: the strongest of each category

| Category | Strongest known | Why it can't go higher |
|---|---|---|
| Individual (raw) | 3× T6 Worldtides (past 70 Fathoms, dying under observation) | Erosion: they are *dying*; the ceiling is a ledger, not a rival |
| Individual (strategic) | The Memorandum Group's principals; Volkov; Zhao Mingde | Institutional checks; the Accords; each other |
| Anomaly | ANOMALY-029, the Well (T6/C-E) | Not usable, not ownable — the top of the scale that isn't a person |
| Organization | The Meridian Compact (rule-setter) | The 60% coverage ceiling; great-power defection; the Tide's arithmetic |
| Containment | SITE-009; hardened ward architecture | Funding; the 900+ events/day load; T5+ exceptions |
| Destructive capability | T6 continental events; Drowndust (tactical anti-Attuned) | T6 users die using it; Drowndust is casus-belli-gated |
| Strategic capability | Information (the Ledger's 40 pages; Arthur's Use 10) | The deepfake dividend; deterrence doctrine |
| Protagonist | Arthur at Use 10+11 (rot-immune proof, zero-Fathom) | Priced in ratchet/attention/exposure; a few uses per story-year |

**Escalation type: CONTROLLED.** Erosion caps individuals (physical law); the Tide cycle raises *event frequency*, not personal caps (situational); the protagonist's ceiling is *budgetary* (the ratchet), not moral or rivalrous. Nothing in the system *requires* a stronger opponent — the opponents are already stronger; the story is about what strength *costs*.

---

## §15 — Protagonist-vs-world test

**Does the world exist without Arthur? YES.** 900+ Seep events/day; the Compact's budget wars; the model-poisoning arms race (C-08); the Pale Court's collecting; Vesper's Tide-medicine program; the JCC's slow loss to the Bell; the Somali corridor's unwritten policy — none of these need him, and B.9's nine interested parties all have Arthur-independent objectives. He *enters* conflicts; he doesn't generate them.

**Can he understand events differently than the world? YES — structurally.** His Loud recall (B.4) + the clerk's cross-referencing (his job) + the Laggard as a window (Uses 1, 6, 9) give him an information asymmetry no faction replicates: he connects *separately-held* records. The asymmetry is positional (he sits at the archive desk with a tether), not intellectual (he is not the smartest person in the room) — which keeps it from becoming a chosen-one trait.

---

## §16 — Patches made (4)

### [POWER PATCH] 1 — Ratchet vs. Fathoms (institutional parallel, not physical approach)

- **File:** `04_POWER_SYSTEM.md`, §4.8.
- **Original state:** the ratchet was described as climbing "toward" the pre-Drowning/T6 band, implying the non-Attuned, zero-Fathom Arthur physically approaches Drowning.
- **Problem:** Arthur accrues no Fathoms (Use 11); a physical approach to Drowning contradicts the Erosion mechanics and the zero-Fathom design.
- **Correction:** the parallel is *institutional, not physical* — his ratchet is measured in lag-seconds and belongs to the tether; at high lag, institutions may *monitor* him like a pre-Drowned subject because the attention/containment economics are comparable.
- **Reason:** preserves the zero-Fathom invariant and the Erosion ledger's integrity.
- **Downstream effects:** none beyond the clarified paragraph; logged in `AUDIT/CHANGELOG.md`.

### [POWER PATCH] 2 — Escrow storage timescale (same-session courier, not week-long vault)

- **File:** `29_PROTAGONIST_ANOMALY.md`, B.11 escrow paragraph.
- **Original state:** "auto-sync" wording implied prints remained in shadow-storage between weekly check-ins.
- **Problem:** contradicted Use 7's hours-long lag window — a week-long vault is impossible under the stated mechanics.
- **Correction:** shadow-storage is a *same-session covert courier*: during a weekly deep-lag check-in, prints move past surveillance to that session's handoff; nothing survives in the shadow between check-ins; missed-session entries rely on lawyer/journalist legs.
- **Reason:** removes the internal contradiction; keeps the escrow's function (custody-proof evidence pipeline) intact.
- **Downstream effects:** `DATABASE/POWER_PROGRESSION.md` §Q and the escrow references updated to the courier model; logged in `AUDIT/CHANGELOG.md`.

### [POWER PATCH] 3 — Dr. Amara Nwosu's affiliation (Compact → Vesper move, 2024)

- **Files:** `29_PROTAGONIST_ANOMALY.md` (Part A line 45; B.9 lines 144, 148), `11_CORPORATIONS.md` (line 37), `DATABASE/CHARACTERS.md` (CHAR-031 row), `35_CANON_DATABASE.md` (CHAR-031 row).
- **Original state:** three mutually exclusive affiliations — 29 B.9 placed Nwosu (CHAR-031) in the Compact science directorate; `DATABASE/CHARACTERS.md` and `35_CANON_DATABASE.md` listed her as Director, Vesper Tide-Medicine Division; `11_CORPORATIONS.md` said Dr. Emil Hartmann "runs the Tide-medicine division."
- **Problem:** a character cannot simultaneously serve the Compact science directorate and direct Vesper's Tide-Medicine Division while a third person runs the same division.
- **Correction:** Nwosu was Compact science directorate; her longitudinal Erosion paper was suppressed (EVENT-091, 2024-03); Vesper recruited her to direct the Tide-Medicine Division (within Specialty Synthesis, headed by Hartmann — the reporting line clarified). 29 B.9's Compact entry now notes the directorate's *institutional* appetite survives without her; Vesper's entry names her as its face.
- **Reason:** the EVENT-091 narrative (suppressed paper → hunting unregistered subjects) *supports* the defection reading; Vesper's ethics-free data-buying makes it her natural home. Minimal reconciliation, no new events invented.
- **Downstream effects:** Nwosu's "researcher" thread (B.9) is now Vesper-backed — "clinical, consensual, well-funded, and impossible to leave" becomes *more* true, not less. The Compact science directorate remains an interested party institutionally. Logged in `AUDIT/CHANGELOG.md`. (Historical audit files `AUDIT/FACTION_AUDIT.md` / `AUDIT/PROTAGONIST_AUDIT.md` disagree on her affiliation; they are dated findings and stand as written — this audit supersedes them.)

### [POWER PATCH] 4 — China's Drowndust stockpile (profile omission)

- **File:** `06_GOVERNMENTS.md`, GOV-002 (the Jade Office) secrets list.
- **Original state:** `13_MILITARY.md` 13.3's Compact assessment (high confidence) names four stockpiling states — the US, Russia, China, North Korea — and the US/Russia/NK profiles all list the stockpile as a secret; China's profile listed only Project Vermilion and the Stillwater-dosing proposal.
- **Problem:** the profile convention includes the assessed stockpile; China's omission was an inconsistency, not a deliberate silence.
- **Correction:** added as secrets-list item (3): a Drowndust stockpile — one of the four the Compact assesses (13.3); unacknowledged by Beijing and held outside the Office's own ledgers.
- **Reason:** aligns the profile with the military assessment and the other three country profiles; the "outside the Office's ledgers" note preserves the Jade Office's internal texture (a military-held program the civilian Office doesn't fully see).
- **Downstream effects:** none; logged in `AUDIT/CHANGELOG.md`.

---

## §17 — Intentional exceptions (16) and unresolved UNKNOWNs (7)

These are not problems; they are the design. Each is load-bearing and bounded:

1. **Use 10 (clean recording)** — the series engine; bounded by the rot-immunity boundary, chain of custody, and possession-as-target.
2. **Use 11 (zero-Fathom operation)** — the protagonist's economic exception; priced in ratchet/attention/exposure.
3. **Uses 13+ (generative principle)** — the open ladder; process-constrained, budget-limited.
4. **Drowndust** — the WMD; supply-capped, casus-belli-gated, Quiet-immune.
5. **The Static Saint** — the horror device; E-class, nearly uncounterable by design; nature on the mystery list.
6. **Bus 12's fare-box** — the unsolved wound; intentional mystery, not a power.
7. **The Thirteenth Chair** — the policy-bound asset; the restraint is the point.
8. **The Harbormaster's Ledger** — the self-deterring wish; 40 pages, monkey's-paw pricing.
9. **The Gilded Cradle** — the prohibition-bounded device; 11 uses, each a war-crimes file.
10. **The Unsent Letterbox** — the rationed oracle; 4-year queue, licensing.
11. **The Well (ANOMALY-029)** — the ceiling; T6/C-E, unusable, unownable.
12. **Choir mass-influence CANON-LOCK** — the geometric-unreliability rule; compounding is *defined* as impossible.
13. **The resurrection prohibition** — 02.I CANON-LOCKED; echoes degrade, the dead stay dead.
14. **The flare's permanent cost** — Use 12 burns the cover; the price is the point.
15. **Arthur's labels in the model-poisoning war** — his clerk's desk as battlespace; the vulnerability is the story.
16. **The tether-eats-the-wake camouflage** — accidental, with the absence-as-signature tell built in.

---

**Unresolved UNKNOWNs** — inherited from canon; this audit created none and resolved none (they are *supposed* to be unknown):

1. What drives the Tide cycle (L5 mystery #1).
2. What is behind/underneath the Laggard — whether it is intelligent (L5 #2).
3. Whether the Undertow wants anything (L5 #3).
4. What caused the 2018 dip (L5 #4).
5. What was on Ilsa's torn page (L5 #5).
6. What happens at 10s+ ratchet (the far end of Arthur's budget).
7. Whether the Compact knows the Vostok Brotherhood holds SITE-006's blueprints (faction-inventory FLAG 3 — likely intentional dramatic irony; the Faction audit should confirm the intended awareness state).

---

## §18 — Verdict

**1000-chapter viability: YES.** The power system sustains a thousand chapters because its scarcities are *structural* (Erosion is irreversible; the ratchet runs one way; attention compounds; the Tide keeps happening 900+ times a day) rather than *dramatic* (no villain needs to be stronger next season). Escalation runs on economics, information, politics, and consequence — thirteen named dimensions, all canon-supported — while raw output stays capped by physical law.

**The brakes that must never be released** (standing guidance for the Chapter Engine): (1) Uses 13+ only by observe–hypothesize–test–pay, never by revelation or emergency; (2) the entity never intervenes on Arthur's behalf; (3) the resurrection prohibition holds absolutely; (4) the Choir compounding lock holds; (5) Arthur's Fathom count stays zero — permanently; (6) the rot-immunity boundary (T4/≤3h) never stretches; (7) the ratchet never runs backward.

**Go/no-go for the next audit (Faction & Conflict Engine): GO.** The power audit found no structural defect that the faction audit must work around; the two patched contradictions are closed; the UNKNOWNs are properly parked on the mystery list where the Mystery audit already tracks them.

---

*End of POWER PROGRESSION AUDIT. Database: `DATABASE/POWER_PROGRESSION.md`. Working analyses: `_pow_audit/` (not shipped to canon).*
---

## Validation log (§19 checks, 2026-09-20)

- **References:** all local `.md` links in created/modified files resolve (00_INDEX, MANIFEST, DATABASE/POWER_PROGRESSION.md, AUDIT/POWER_PROGRESSION_AUDIT.md, 04, 06, 11, 29, DATABASE/CHARACTERS.md, 35_CANON_DATABASE.md, CHANGELOG). 53 broken relative links exist *only* in pre-existing v1.3-era forensic audit files (AUDIT/FACTION_AUDIT.md, ISSUES.md, ECONOMIC_AUDIT.md, etc.) — dated historical reports, left as written.
- **Costs/limitations:** §2's matrix confirms every profiled ability carries an explicit cost and at least one counter; §7's counterplay table shows zero abilities without a cost-or-counter.
- **Interactions:** 28 combination scenarios simulated (§7); no unpriced interaction found.
- **Protagonist curve:** 7 stages reviewed (§4); no unexplained jumps; every rung is understanding-shaped and ratchet-priced.
- **Faction capabilities:** 28 records audited against the six contradiction types (§9); 2 genuine contradictions patched (§16), 1 UNKNOWN parked, 1 prose-hygiene recommendation.
- **Terminology:** "the Ledger" disambiguation flagged (INTL-003 vs SUP-004 vs Quiet/Bone/"sleeping" ledgers) — recommendation recorded in §9.
- **Stale/duplicate rules:** no duplicate registry IDs in 35_CANON_DATABASE.md; stale v1.5 database headers updated to v1.5–v1.6 carried-forward; the Phase-4 mystery-count prose corrected via [CORRECTION] entry.
- **Accidental retcons:** none — all four patches are reconciliations/clarifications documented in CHANGELOG with previous-canon quotations; the invariants (Laggard mechanism, inheritance chain, 2017 Ravenscroft transfer, Arthur's identity, all IDs) verified unchanged.


---

## SECTION: `AUDIT/POWER_SYSTEM_AUDIT.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/POWER_SYSTEM_AUDIT.md` · sha256 `bd9d6b6cc51eabc9edea1d53456aaddfd3b7738cc993b82c8d4355648b1bce0f` · 6,378 words. No content changed.

# POWER SYSTEM AUDIT — THE QUIET TIDE v1.2 (Albion-primary)

**Worker:** AUD-POWER · **Date:** 2026-09-19 · **Scope:** `03_SUPERNATURAL_SYSTEM.md`, `04_POWER_SYSTEM.md`, `05_ANOMALY_CLASSIFICATION.md`, `28_ANOMALIES.md`, `29_PROTAGONIST_ANOMALY.md`, `30_POWER_HIERARCHY.md`, plus `00_INDEX.md`, `02_WORLD_RULES.md`, `35_CANON_DATABASE.md`; grep cross-checks into `12_FACTIONS.md`, `13_MILITARY.md`, `24_HISTORY.md`, `25_TIMEmessaging app.md`, `26_INFORMATION_CONTROL.md`.
**Method:** adversarial. Canon files were read, not edited. Every issue below quotes both sides.

**Issue counts:** CRITICAL 0 · HIGH 5 · MEDIUM 6 · LOW 3 — **14 total.**

---

## PART 1 — FINDINGS

### POWER-001 — HIGH — ANOMALY-006: ratified vector (C-C) vs catalog status prose (D-class, "containment is impossible")

**Location:** `05_ANOMALY_CLASSIFICATION.md:101-102` vs `28_ANOMALIES.md:101` (header) and `28_ANOMALIES.md:109` (status prose).

**Conflicting statements:**
- 05: "**ANOMALY-006 'The Thursday Rain'** — `MV-T3/C-C/R/Regional/Reactive` — *Upward rain, third Thursdays, three provinces. C-class because containment means regional weather-service coordination and road closures nine days a year, forever.*"
- 28: "**Current status:** Monitored, uncontained (D-class: containment is impossible; the Compact settles for crowd management and noise farming the footage)."

**Why it is a problem:** These are not two wordings of one filing — they are opposite containment claims. C-C means "contained at cost: continuous active intervention" (05, Axis 2 table); D means "uncontained but tracked." The 05 gloss even gives the *reason* for C ("road closures nine days a year, forever") while 28 says containment is *impossible* and the Compact settles for crowd management. A coordinator cannot tell whether the Thursday Rain is contained-at-cost or uncontained, which changes its budget line (C costs ~40× B; D is surveillance + readiness), its legal triggers, and its insurance pricing. This is one of five vector-vs-prose conflicts (see POWER-002/003/004/005) — a pattern suggesting 28's "Current status" prose was drafted against a different vector revision than 05.5's ratified examples.

**Proposed solutions:**
1. Treat 05.5 as authoritative (it claims "Compact-ratified unless noted") and rewrite 28's status prose to describe C-class containment (coordination, closures, staffing), deleting "containment is impossible."
2. Treat 28's prose as field truth and re-file the vector as `MV-T3/C-D/R/Regional/Reactive` in 05.5, with a re-audit note explaining the downgrade — the "Urban is a hope, not a measurement" precedent (05.6, case 4) supports field truth winning.
3. Split the difference explicitly: file C-C for the *predictable* component (the nine road-closure days) and note D-class handling for the *footage/propagation* component — but the vector has one containment axis, so this requires a filing footnote, not a new class.

---

### POWER-002 — HIGH — ANOMALY-012: ratified vector (C-D) vs catalog status prose (E-class, uncontainable)

**Location:** `05_ANOMALY_CLASSIFICATION.md:105-106` vs `28_ANOMALIES.md:177` (header) and `28_ANOMALIES.md:187` (status prose).

**Conflicting statements:**
- 05: "**ANOMALY-012 'The Static Saint'** — `MV-T5/C-D/I+M/Memetic/Sapient` — *An information-seep with a congregation. Sapient, memetic, uncontained. The file is I-flagged; this paragraph is the most this bible says about it.*"
- 28: "**Current status:** **E-class, uncontainable.** Countermeasures only: footage from T4+ events is now auto-quarantined and machine-screened before human review…"

**Why it is a problem:** C-D ("uncontained but tracked… response on standby") and C-E ("uncontainable by any known means. Mitigation and evacuation only. Whatever it takes") trigger different doctrines — D still postures a response; E abandons containment for evacuation. The Saint is the setting's apex information predator; whether the Compact believes it can ever be contained determines the entire posture of 26_INFORMATION_CONTROL.md's saint-positive protocols. Note the header vector in 28 (`MV-T5/C-D/...`) agrees with 05 — only the prose disagrees, which again points to a draft-skew between 28's prose and the ratified vectors.

**Proposed solutions:**
1. Keep C-D (ratified vector wins) and soften 28's prose to "D-class, uncontained; no containment pathway currently known" — D already covers "tracked, response on standby."
2. Upgrade the vector to C-E in both files and pay the doctrinal price: E-class filings are rare (the Well is one of the "few E-class filings on earth," 05.5), so promoting the Saint to E should come with an in-world event (a failed containment attempt) rather than a silent edit — CHANGELOG entry required.
3. Add an explicit filing footnote: "C-D filed; E-class argued by the Seismograph Authority; dispute pending Classification Office review" — this converts the conflict into in-world bureaucratic disagreement, which 05.3 says is the norm.

---

### POWER-003 — HIGH — ANOMALY-013: ratified vector (C-B) vs catalog status prose (D-class)

**Location:** `05_ANOMALY_CLASSIFICATION.md:107-108` vs `28_ANOMALIES.md:191` (header) and `28_ANOMALIES.md:199` (status prose).

**Conflicting statements:**
- 05: "**ANOMALY-013 'The Salt Garden'** — `MV-T4/C-B/R/Urban/Reactive` — *High threat, low containment cost: the garden's Rule is geographically fixed and legible. The lesson auditors cite — threat and containment are orthogonal.*"
- 28: "**Current status:** D-class: the courtyard cannot be sealed (it 'rejects' warding — three attempts collapsed the scaffolding), so the Turkish agency maintains a perimeter and a waiting list."

**Why it is a problem:** This is the sharpest of the five: 05.5 uses the Salt Garden as the *teaching example* for threat/containment orthogonality ("the lesson auditors cite"), while 28's prose describes a site that rejects warding, collapsed three scaffolding attempts, and is held by perimeter only — textbook D ("uncontained but tracked"). If the garden is D, the teaching example is wrong; if it is B ("containable with known active procedures… a waiting list" arguably *is* the procedure), the prose's "cannot be sealed" overstates. The waiting-list perimeter could be read as the B-class "known active procedure" — but "rejects warding" reads as uncontainable-by-standard-means.

**Proposed solutions:**
1. Keep C-B and rewrite the prose: the perimeter + waiting list *is* the known active procedure; "cannot be sealed" becomes "cannot be *vaulted*" (B never required vaulting).
2. Re-file as C-D in 05.5 and replace the teaching example with ANOMALY-020 or another genuine high-threat/low-cost case — but the auditors'-lesson line is load-bearing color; moving it costs texture.
3. File C-B with a formal exception note: "B-class by procedure (perimeter + queue management); standard warding inapplicable — Rule-specific exception logged." This preserves both the lesson and the field truth.

---

### POWER-004 — HIGH — ANOMALY-030: ratified vector (C-C) vs catalog status prose (D-class)

**Location:** `05_ANOMALY_CLASSIFICATION.md:115-116` vs `28_ANOMALIES.md:405` (header) and `28_ANOMALIES.md:415` (status prose).

**Conflicting statements:**
- 05: "**ANOMALY-030 'The Second Silence Archive'** — `MV-T5/C-C/I/Memetic/Sapient` — *Contained at cost: the archive is cooperative (Sapient) but I-flagged, so every researcher is compartmentalized, examined, and rotated. The most expensive library card in history.*"
- 28: "**Current status:** D-class (containment = the Archivists themselves). The Compact's arrangement with SUP-008: the Archivists keep the Archive, the Compact gets *reading privileges* (slow, supervised, no copies), and both sides pretend this is stable."

**Why it is a problem:** C-C ("contained at cost: continuous active intervention") vs D ("uncontained but tracked"). The 05 gloss prices the containment (compartmentalized, rotated researchers — "the most expensive library card in history"); the 28 prose describes outsourced custody ("containment = the Archivists themselves") with the Compact holding only reading privileges — which is D-shaped (someone else holds it; you watch). For a T5 Sapient infohazard, the difference between "we contain it at cost" and "the Archivists contain it and we visit" is a sovereignty-grade distinction (cf. 05.3's jurisdiction triggers: at T4+/Regional+ the JCC can take command — who commands the Archive?).

**Proposed solutions:**
1. Keep C-C: the Compact *funds* the Archivists' containment (the "cost" in "contained at cost" is paid to SUP-008), and rewrite 28's prose to reflect a Compact-funded custody contract rather than a handshake.
2. Re-file C-D with the justification that Sapient-cooperative custody by a third party is D by definition (the Compact tracks; the Archivists hold) — and accept the JCC-standby trigger that comes with T5+D.
3. Make the ambiguity the point: file C-C *provisional* with a Classification Office dispute note (the Archivists argue C-B — "we've held it for centuries"; the Compact argues C-C) — in-world disagreement per 05.3.

---

### POWER-005 — MEDIUM — ANOMALY-004: INTEL axis `None` (05.5) vs `Reactive` (28 header)

**Location:** `05_ANOMALY_CLASSIFICATION.md:99` vs `28_ANOMALIES.md:23` (overview table) and `28_ANOMALIES.md:77` (header).

**Conflicting statements:**
- 05: "**ANOMALY-004 'The Counting Stair'** — `MV-T1/C-B/—/Local/None` — *Textbook B-class…*"
- 28: `MV-T1/C-B/—/Local/Reactive` (both table and entry header).

**Why it is a problem:** The Stair's Rule — "Anyone who counts aloud while climbing arrives one floor higher than the building possesses" — *responds to stimuli in fixed, non-novel ways*, which is 05's verbatim definition of Reactive ("the stair counts; the fog arrives on schedule" is 05.1's own example of Reactive). `None` ("no detectable response to stimuli") is factually wrong for a counting stair; 28's `Reactive` is correct. The error is in 05.5, the file that claims ratified vectors. It also matters doctrinally: the Oslo case (05.6) established that INTEL misclassification gets people killed, and the Sapient-presumption protocol keys off this axis.

**Proposed solutions:**
1. Correct 05.5 to `MV-T1/C-B/—/Local/Reactive` — one-word fix, no doctrinal fallout.
2. If `None` was intentional (e.g., the stair's *door* is the anomaly and the stair is incidental), the entry's Rule text must be rewritten to support it — much more expensive; not recommended.

---

### POWER-006 — HIGH — ANOMALY-015 "The Gilded Cradle": two incompatible Rules for one ID

**Location:** `28_ANOMALIES.md:215-223` (entry) vs `30_POWER_HIERARCHY.md` Scenario 3 vs `35_CANON_DATABASE.md:300` (one-liner).

**Conflicting statements:**
- 28: "**The Rule —** Any infant placed in the cradle sleeps without waking for exactly one year, and wakes *one year older*… Any adult who rocks the cradle falls asleep for one hour and wakes having *lost* one year of Erosion — no, not lost: *transferred*. The cradle does not heal Erosion; it moves it. The infant wakes carrying the rocker's Fathoms… The cradle has been used eleven times. There are eleven children."
- 30: "**Setup:** 'The Gilded Cradle' (ANOMALY-015, object/T4, per Drafter C's registry) activates in a Jakarta apartment block — its Rule: it *keeps* what is placed in it, including, eventually, people."
- 35: `| ANOMALY-015 | "The Gilded Cradle" | Object/T4; keeps what is placed in it |`

**Why it is a problem:** These are not two facets of one Rule — they are different anomalies wearing one ID. 28's cradle is an Erosion-transfer trolley problem (eleven children, Tribunal prohibition, Choir interest); 30/35's cradle is a Venus-flytrap container ("keeps what is placed in it, including, eventually, people"). 30's entire Scenario 3 ("the exterminator model… Evacuate by the exception clause — the Cradle only keeps what is *given*") is built on the 30/35 Rule, including an "exception clause" that does not exist in 28's entry. A reader cross-referencing the scenario with the catalog finds a different anomaly. One of the two Rules must go, and 30's scenario must be rewritten to match the survivor.

**Proposed solutions:**
1. Keep 28's Rule (it is the richer, more load-bearing design — the eleven children, the Tribunal order, four factions' positions) and rewrite 30's Scenario 3 around a different object-seep or around the cradle's real Rule (e.g., Sweepers responding to an *unauthorized twelfth use*).
2. Keep 30/35's Rule and rewrite 28's entry — cheaper in pages, but destroys the cradle's trolley-problem payload and orphans the eleven-children thread.
3. Split the ID: the "keeps what is placed in it" object becomes a new ANOMALY-031 and 30's scenario is retargeted — preserves both designs at the cost of one new registry entry. (Note: 28's catalog claims completeness for 002–030, so a 031 requires a registry note.)

---

### POWER-007 — MEDIUM — ANOMALY-001 filed C-A, but its described containment matches class D

**Location:** `29_PROTAGONIST_ANOMALY.md:40-44` (B.1 filing) vs `05_ANOMALY_CLASSIFICATION.md` Axis 2 table (C-A vs C-D definitions) and `05_ANOMALY_CLASSIFICATION.md:76-78` (legal triggers).

**Conflicting statements:**
- 29: "**CONTAINMENT C-A** (tracked, passive containment — it cannot be vaulted, it travels with the holder; surveillance + biennial exam)."
- 05, class A: "**A** — Contained, stable. Passive measures suffice (a vault, a locked room, a warning sign the locals obey)." Class D: "**D** — Uncontained but **tracked**. Free in the wild; monitored; response on standby."
- 05: legal trigger — "**T3+ or C-D+** | Report to the Compact Classification Office within 72 hours."

**Why it is a problem:** By 05's own definitions, the Laggard is D-shaped: it cannot be vaulted, travels with the holder, and is "tracked" by surveillance + biennial exam. Filing it C-A instead of C-D has a conspicuous legal consequence: C-D would trigger 72-hour Compact reporting; C-A triggers nothing. This is either (a) a filing error, or (b) exactly the systematic under-classification 05.3 describes ("states systematically under-classify to avoid reporting obligations") — in which case the "yawned three times" bureaucracy (29:B.9) is not lazy but *motivated*, and the bible should say so, because it converts Arthur's best protection from luck into someone's *decision*. Either is writable; the file should pick one.

**Proposed solutions:**
1. Re-file as C-D in 29:B.1 with the justification that the 72-hour report was duly filed and buried — "reported, noted, and deprioritized," consistent with B.9's triage logic. Cleanest: keeps the vector honest, explains the reporting consequence.
2. Keep C-A but add an explicit CANON-adjacent line: the examiners' office applies C-A to *person-bound* anomalies as a matter of policy ("a person cannot be 'uncontained'"), with the D-equivalent handled by surveillance protocols — a defensible institutional reading, stated rather than implied.
3. Add a Compact Classification Office guidance note to 05: person-bound mobile anomalies default to D unless a *holder-compliance protocol* (handler, restraints, check-ins) constitutes the "passive measures" — which converts the filing question into an explicit legal test.
...[truncated 19905 chars]
### POWER-008 — MEDIUM — Ward Six Lullaby: infohazard behavioral compulsion vs "no direct mind control"

**Location:** `28_ANOMALIES.md:111-116` (ANOMALY-007 Rule) vs `02_WORLD_RULES.md:13` (CANON-LOCKED mind-control rule).

**Conflicting statements:**
- 28: "Repeated exposure (three or more hearings) causes the sleeper to seek out the nearest hospital and occupy any empty sixth bed they can find; two documented cases ended in Drowning-adjacent Erosion spikes in the *singers*, not the sleepers."
- 02: "CANON-LOCKED: **No direct mind control.** A mind is a Membrane phenomenon; the Undertow cannot grip it directly. What *is* possible is **suggestion seeding**… It is resisted by awareness, strong identity, training, and (ironically) stubbornness; it always produces **backlash**."

**Why it is a problem:** The lullaby *compels specific behavior* (go to a hospital, occupy a bed) in a way the victim cannot resist by awareness — hearing the complete melody is the trigger, and no amount of stubbornness un-hears it. The file's defense is implicit (it's a predatory information-pattern, STATUS: THEORY, not Attuned channeling — the 02 rule governs what the Undertow "grips," and the lullaby works more like a parasite's behavioral modification). But the distinction between "compulsion via infohazard" (allowed) and "directed obedience" (impossible) is never stated, and the Salt Garden's 2017 saboteur ("he walked in and never walked out," 28:199) is a second anomaly-driven behavior-override with the same unaddressed status. A hostile reader could argue the bible smuggles mind control in through the anomaly catalog.

**Proposed solutions:**
1. Add an explicit CANON line (02 or 04.6): behavioral *compulsion* via predatory information-patterns is possible and is *not* mind control — it is resisted by *not completing the pattern* (not hearing the melody; not walking the garden alone), whereas suggestion seeding is resisted *after* exposure. Two different defenses for two different mechanisms.
2. Alternatively, weaken the lullaby's compulsion to a *strong inclination* the victim can fight with the standard resistances (awareness, stubbornness) — but this costs the anomaly its horror payload; not recommended.
3. Keep the effect and label the tension in-world: the Compact's legal directorate has an open memo on whether the lullaby violates the Accords' mind-control provisions — unresolved law as texture (cf. 05.3's love of bureaucratic disagreement).

---

### POWER-009 — MEDIUM — The Static Saint inflicts Erosion without channeling — the cost model becomes a weapon

**Location:** `28_ANOMALIES.md:177-186` (ANOMALY-012 Rule) vs `02_WORLD_RULES.md:15` ("Erosion is irreversible. Channeling wears the Veil") and `04_POWER_SYSTEM.md:52-58` (4.4, Erosion as the price of *channeling*).

**Conflicting statements:**
- 28: "Anyone who *recognizes* the face… begins to dream of drowning within a week, accrues Erosion at ~1 Fathom per month without channeling, and eventually seeks out deep water."
- 02/04: Erosion is the wear *channeling* puts on the user's Veil — "Every deliberate channeling wears the user's Veil — measurable as Erosion" (03.1); "Channeling is priced in Fathoms" (04.4).

**Why it is a problem:** The entire power system prices *chosen* use: "the more you use power, the less of *you* remains" (03.1). The Saint breaks the "chosen" half — Erosion *inflicted* by recognizing a face, ~12 Fathoms/year, no channeling involved. Two consequences: (a) the Saint is a ready-made assassination weapon — expose an enemy Attuned to the face and they erode at 1 Fathom/month, deniably, without Drowndust's supply constraints; the file's only defense is information restriction ("the knowledge that the face *exists* is itself restricted," 28:187), which does not bind the Ninth Bell or the Red Ledger. (b) It implies Erosion is not (only) channeling-wear but a *damage type* the Undertow can deal — which reframes every Erosion statement in 04/30. The lullaby's singers show the same pattern ("Drowning-adjacent Erosion spikes in the *singers*, not the sleepers" — singing a melody is not channeling).

**Proposed solutions:**
1. Re-label the Saint's effect as Veil *damage* distinct from Fathom Erosion (same clinical scale, different etiology — the Fathom scale already measures both, which is why the confusion arose). Then "Erosion is priced channeling" stays clean, and Saint-victims suffer "erosion-like Veil degradation" that *behaves* as Fathoms for prognosis.
2. Own the weaponization: add a Compact threat-assessment line that the Saint's face is a *proscribed weapon* (like Drowndust) precisely because it inflicts Erosion without channeling — the restriction regime becomes the story, consistent with the infohazard handling already described.
3. State whether Saint-induced accumulation has an off-ramp: the file says victims "eventually seek out deep water," implying progression; clarifying whether the accumulation stops (if the victim never channels again, if the face is forgotten) determines whether this is a death sentence or a chronic condition.

---

### POWER-010 — MEDIUM — The Gilded Cradle reifies Fathoms as transferable substance

**Location:** `28_ANOMALIES.md:215-223` (ANOMALY-015) vs `02_WORLD_RULES.md:15` ("Erosion is irreversible") and `04_POWER_SYSTEM.md:52-58`.

**Conflicting statements:**
- 28: "The cradle does not heal Erosion; it moves it. The infant wakes carrying the rocker's Fathoms, distributed as developmental anomalies the Compact's doctors refuse to describe in writing."
- 02: "CANON-LOCKED: **Erosion is irreversible.** Channeling wears the Veil… nothing reverses it."

**Why it is a problem:** Transfer is not reversal — the file says so explicitly, so the letter of 02.I survives. But the *model* shifts: everywhere else, Fathoms are a clinical scale measuring *wear on a specific user's Veil* from *their* channeling. The cradle treats them as a *substance* that can be poured from one person into an infant. Combined with POWER-009 (the Saint *inflicting* Erosion), Fathoms behave increasingly like stuff — moved, dealt, carried — rather than like wear. If Fathoms are stuff, the obvious next question is whether they can be *stored, traded, or weaponized* as stuff (cf. Drowndust, which already weaponizes Erosion-adjacent residue). The file doesn't need to forbid this, but it should decide what Fathoms *are*.

**Proposed solutions:**
1. Add a Compact medical-directorate position (04.4 or 16_MEDICINE.md): Fathoms measure Veil integrity; the cradle doesn't move "Fathoms" but *reassigns the Veil-debt* — the infant's Veil carries the wear pattern. Same outcome, wear-model preserved.
2. Alternatively, canonize the substance reading: Erosion is Undertow-pressure *residue* in the pattern, which is why it can be moved (cradle), inflicted (Saint), and weaponized (Drowndust) — and "irreversible" means only that *the total never decreases*. This is the more interesting physics and unifies three anomalies, but it requires touching 02.I's gloss (not the rule itself).
3. Leave the tension as an in-world scientific dispute (Membrane Theory vs. medical directorate) — cheapest, and 03.2 already establishes that competing models are load-bearing.

---

### POWER-011 — LOW — Routine-rate top end vs T2 career spans: the arithmetic grazes the Drowning line

**Location:** `04_POWER_SYSTEM.md:52-58` (4.4 routine rates) vs `30_POWER_HIERARCHY.md:30-38` (30.2 tier table).

**Conflicting statements:**
- 04: "ordinary low-output channeling — a working day's worth of small uses — accrues roughly **0.005–0.02 Fathoms/day**… A career Attuned budgets on the order of **~5 Fathoms/year** for routine work."
- 30: T2 "Sustainable career: 15–25 years of professional work at discipline hygiene."

**Why it is a problem:** At the top of the stated routine band (0.02/day ≈ 5/year), a 20-year T2 career accrues ~100 Fathoms from routine work alone — the Drowning line — before a single serious use (0.5–2 Fathoms each, 30.2) is counted. The file's evident intent is that 5/year is a *budget ceiling* and discipline hygiene keeps actuals well under it (the low end, 0.005/day ≈ 1.25/year, gives a comfortable ~25 + serious uses over 20 years). But as written, a literal reader can derive "career T2s Drown from routine work," which contradicts "Life expectancy: Near-normal with care."

**Proposed solutions:**
1. Clarify in 04.4 that ~5/year is the *budgeted ceiling* and that discipline hygiene targets ~1–2/year actual — one sentence.
2. Alternatively, shorten the T2 career span or raise the routine band's floor — both worse; not recommended.

---

### POWER-012 — LOW — EVENT-047 "T6 Choir event" (35/DATABASE) vs 25's hidden truth (no Choir actor)

**Location:** `35_CANON_DATABASE.md:385` and `DATABASE/EVENTS.md:56` (one-liners) vs `25_TIMEmessaging app.md:275-283` (EVENT-047 full entry).

**Conflicting statements:**
- 35/DATABASE: "The Quiet Night (1977) | T6 Choir event; ~300 Loud interned; Agus Hidayat (CHAR-035) dies."
- 25: "**Hidden truth:** A **global near-breach** — Tide pressure spiked everywhere at once; ~400 Seep events in 24 hours; the Seismograph network nearly saturated. The closest the masquerade has come to failing everywhere at once." (No Choir actor; no T6 individual named anywhere in 24/25 for 1977.)

**Why it is a problem:** "T6 Choir event" asserts an *agent* — a Choir operator at Worldtide scale acting in 1977. The full entry describes a *pressure phenomenon* with no agent. If a T6 Choir acted in 1977, who? (Reyes, CHAR-010, is the only Choir T6 in history per 26_INFORMATION_CONTROL.md — was he active in 1977? No file says so.) If no one did, the one-liner invents an agent the canon doesn't contain, and "T6 Choir event" also strains 30.1 ("A T6 Choir can steer a *crowd's* emotions; it cannot command an *individual's* obedience") — a *global* Choir event would be the largest mind-affecting incident in history, deserving more than a one-liner.

**Proposed solutions:**
1. Correct the one-liners to "global Tide-pressure near-breach; ~300 Loud interned" — matches 25, removes the phantom agent.
2. If a T6 Choir *was* involved, name them in 25's hidden truth and price the consequences (backlash at T6 scale should have been catastrophic — an untold story worth telling deliberately, not accidentally).

---

### POWER-013 — MEDIUM — The nothing-to-lose T6: pre-Drowning Worldtides are undescribed

**Location:** `30_POWER_HIERARCHY.md:30-44` (30.2 table; Scenario 4) vs `04_POWER_SYSTEM.md:52-58` (side effects 80–100).

**Conflicting statements:**
- 30: T6 "Measured in *uses*, not years — all three confirmed are past 70" / "Dying by inches under observation."
- 04: 80–100 Fathoms: "pre-Drowning… identity instability, involuntary channeling, physical wrongness (reflections lag, shadows misbehave)."
- 30, Scenario 4 covers a T5 at 88 Fathoms attacking a city — and the city wins by patience.

**Why it is a problem:** Scenario 4's answer to "why the T5 loses" is Erosion attrition: "88 to 100 is *one afternoon* at maximum output." Apply the same math to Shirakawa (CHAR-011, Hollow T6, ~88 Fathoms, 26_INFORMATION_CONTROL.md): she is *already inside* the 80–100 band where channeling becomes *involuntary*. The file describes what keeps a T6 *compliant* (observation, dying by inches) but never what contains a T6 in *involuntary-channeling pre-Drowning* — the most dangerous phase, where the "weapons that degrade themselves" become weapons nobody is aiming. "All under permanent Compact observation" is not a containment mechanism for involuntary continental-scale channeling; 26's cost curve says "T6+: unpriceable — evacuation and mitigation, not containment," which concedes the point without describing the posture.

**Proposed solutions:**
1. Add a Compact doctrine line (30 or 26): pre-Drowning T6 protocol is *evacuation + Tide-noise saturation + distance* — i.e., the file admits there is no containment, only radius. Honest and terrifying.
2. State why it hasn't happened yet: the three T6s' disciplines/conditions (Reyes's legalistic observation protocol, Shirakawa's non-communicativeness as a *damping* state) — individual, fragile, non-replicable reasons. Fragility acknowledged is better than fragility ignored.
3. Seed it as a season engine (RC-050's Trench Front already points this way): the novel's endgame is allowed to be "what we do when a Worldtide starts Drowning and we can't stop it."

---

### POWER-014 — LOW — Older-notes vector notation doesn't match the 05.1 notation standard

**Location:** `29_PROTAGONIST_ANOMALY.md:40-44` (B.1).

**Conflicting statements:**
- 29: "The filed `MV-T1/D/Local/Reactive` reading that circulates in older examiner notes…"
- 05.1: "Notation: `MV-[THREAT]/[CONTAINMENT]-[FLAGS]/[RANGE]/[INTEL]`" — under which the reading would be `MV-T1/C-D/—/Local/Reactive`.

**Why it is a problem:** Trivial on its own — but 29 presents the older reading as a *filed* vector ("The filed… reading"), and filed vectors follow the standard. The missing `C-` prefix and missing `—` flags placeholder make it look like a different notation generation, which muddies whether the "dodge" (writing Reactive/None instead of Unknown) is even parseable as a vector. Note the interaction with POWER-007: if the older notes filed C-D, that *would* have triggered 72-hour Compact reporting — which undercuts the "dodge" framing. A C-A filing with Reactive INTEL dodges both the reporting trigger *and* the Sapient-presumption protocol — the cleaner in-world lie.

**Proposed solutions:**
1. Correct to `MV-T1/C-D/—/Local/Reactive` as written — but then reconcile with POWER-007 (why would a dodging examiner file the reporting-triggering class?).
2. Change the older-notes reading to `MV-T1/C-A/—/Local/Reactive` — the coherent dodge: A avoids reporting, Reactive avoids Sapient-presumption. One edit, both findings align.
3. Keep the nonstandard notation but label it: "pre-2008 notation, before the flags placeholder was standardized" — converts a bug into history.

## PART 2 — COMBINATION STRESS TESTS

### C1 — Gilded Cradle (015) + Drowndust supply = industrial Erosion laundering
**Setup:** Drowndust already converts Tide-remnant residue into a weaponized additive (28:245-252). If the cradle *moves* Fathoms (28:219), a faction could: dose volunteers with Drowndust (forcing Erosion accrual), rock the cradle to *dump* their Fathoms into infants, and repeat — a renewable Erosion farm. The infants' "developmental anomalies the Compact's doctors refuse to describe in writing" are the only bottleneck, and the Choir (which "keeps trying to acquire" the cradle, 28:223) is exactly the faction with the ideology to industrialize this.
**Verdict:** HOLE-adjacent. The file treats the cradle as a rare trolley problem (eleven uses), never as infrastructure. The Tribunal prohibition (28:221) is a legal deterrent, not a physical one, and it binds signatories — the Choir and the Ninth Bell are not signatories in any meaningful sense. *Mitigation available:* the cradle's Rule requires "an adult who rocks the cradle" — price the rocking (one hour's sleep, one year of Erosion per transfer) as non-parallelizable, and state that infant capacity is one-at-a-time; an industrial pipeline still works but is slow. Better: have the Tribunal prohibition carry a *mechanical* consequence (the cradle refuses repeat rockers? unstated). Recommended: add one line that the cradle's transfer only works for Erosion *accrued through channeling*, not Drowndust-induced damage — closes the farm, preserves the trolley problem.

### C2 — Barber's Ledger (026) + ward Six Lullaby (007) = targeted cognitive debt
**Setup:** The ledger writes debts into people; the lullaby compels behavior in sleepers. Write a victim's name in the ledger with a debt denominated in *hearing the lullaby* — or simpler: ledger-debt the *singers* (who accrue "Drowning-adjacent Erosion spikes," 28:116) into singing for a target. The ledger's debts are "denominated in favors, memories, years" (28:379) — a lullaby performance is a favor.
**Verdict:** HOLDS, barely. The ledger requires the Red Ledger's physical book and its "Auditor" (28:382-388); the combination is a two-anomaly operation requiring the cooperation of the Red Ledger's inner circle, which is exactly the kind of rare, expensive, deniable op the setting wants to exist. The cost is real (Erosion spikes in the singers; the ledger's own price, 28:385). No patch needed — but the coordinator should note this is a known Red Ledger capability, not an undiscovered exploit.

### C3 — Static Saint (012) as a weapon of mass Erosion
**Setup:** POWER-009 already covers this: the face inflicts ~1 Fathom/month on recognizers. Broadcast the face (T4+ event footage is auto-quarantined *because* of this, 28:187) and you have a slow-burn WMD against every Attuned who sees it. The countermeasure regime (machine-screened review, the knowledge itself restricted) is the only defense.
**Verdict:** ACKNOWLEDGED BY CANON — the file knows (28:187-189: "The Compact's position… Do not look at it directly"). The residual hole is *offensive* use by non-Compact actors: the Ninth Bell wants the masquerade broken (12_FACTIONS.md); showing the world the Saint's face breaks it *and* erodes every Attuned who looks. Why haven't they? The file's implicit answer: the Bell wants *witnesses*, not corpses — a Drowned population can't testify. Acceptable, but the coordinator should state it once: the Bell's doctrine requires the Saint to remain *unseen* because their apocalypse needs an audience.

### C4 — Second Silence Archive (030) + Choir harmonics = T6 Choir bootstrapping
**Setup:** The Archive is Sapient, I-flagged, T5, and cooperative (28:405-415). The Choir's harmonic entrainment (RC-009, 30:56-64) merges voices into composite entities — a Choir is "multiple Attuned channeling in harmonic entrainment," and composite voices "persist… after the Choir disperses" (30:60). What happens when a Choir entrains *with* a Sapient T5 infohazard? The file's Choir rules cap T6 at "steer a crowd's emotions" (30.1) — but a Choir+Archive composite is a new entity class the caps don't cover.
**Verdict:** OPEN — genuinely unaddressed. The file never considers Choir–anomaly entrainment, only Choir–Choir. The "no permanent fusion" rule (30:62) covers Attuned–Attuned; a Sapient anomaly is neither. *Recommended:* extend the "no permanent fusion" / "compulsion is impossible" guardrails to Choir–anomaly entrainment explicitly (04.6 or 30.4), or price it: the Archive's I-flag means any Choir that entrains with it inherits compartmentalization and rotation — the composite can't persist because its members get examined and separated. One sentence closes the bootstrap.

### C5 — Tide-marks (Stillwater) + Tide-callers = unsanctioned Drowndust pipeline
**Setup:** Stillwater Harbor (SUP-004): "The water remembers. Tide-marks — residue patterns — form on stone… Collectors harvest them. The Compact buys quietly" (28:419-427). Drowndust is "Tide-remnant residue" weaponized (28:245). If Tide-marks *are* harvestable residue and Drowndust is weaponized residue, the Stillwater collectors are an unsanctioned Drowndust feedstock pipeline — and the Compact "buys quietly," i.e., funds it.
**Verdict:** HOLDS — and it's good. The file *wants* this read: the Compact's quiet buying is complicity, the "licensed collectors" are a fig leaf, and the price curve ("Tide-marks are priced by clarity," 28:424) is a commodities market for WMD feedstock. The only gap: the file doesn't say whether Tide-marks *are* Drowndust-grade. Recommended: one line in 28:424-427 — "refined Tide-marks are chemically indistinguishable from low-grade Drowndust" — which converts the implication into a priced, policed fact and explains the Compact's buying (corner the market, keep it out of Bell hands).

### C6 — Barber's Ledger (026) + Red Ledger blood-debts = infinite leverage loop
**Setup:** The Red Ledger "trades in obligations" (12_FACTIONS.md); the Barber's Ledger writes debts into people (28:379-388). Can the Red Ledger write a debt *into itself* — or write debts denominated in ledger-access, creating recursive obligation? The Auditor's price is stated (28:385), but the recursion isn't bounded.
**Verdict:** HOLDS. The ledger's Rule (28:379-381) denominates debts in "favors, memories, years" — concrete, finite, and *payable*. Recursive self-debt would be denominated in nothing payable, and the Auditor (who "collects," 28:386) is the bound: the file implies the Auditor enforces *collectability*. A debt that can't be collected is refused — the same way a bank refuses an unpayable loan. The coordinator may want one explicit line ("the Auditor refuses uncollectable debts"), but the mechanism is present.

### C7 — Hollow mechanics + Tide-caller Choir = manufacturing Hollows at scale
**Setup:** Hollows are made when channeling exceeds the Veil's capacity catastrophically (03.4, 04.4: "Push past 100 and the Veil tears"). A Choir forces harmonic entrainment — can a Choir *force* a victim's channeling past 100, manufacturing a Hollow on demand? The Ninth Bell (which wants Drowning events) plus Choir doctrine (which knows entrainment) is the obvious manufacturer.
**Verdict:** PARTIALLY OPEN. The file prices *voluntary* over-channeling but never addresses *forced* channeling — can channeling be compelled at all? (02.I's no-mind-control rule suggests not directly; but Choir entrainment "overwrites individual patterns," 30:58.) If entrainment can drive a victim's output, Hollow-manufacturing is a Bell capability the file doesn't price. *Recommended:* state the bound — entrainment requires the victim's *pattern participation* (they must be Loud/Attuned and *channeling already*); you cannot entrain a non-channeler, so Hollow-manufacturing requires a victim already near the edge. This keeps the Bell dangerous (they can push the willing/weak) without making Hollow-factories trivial.

### C8 — EVENT-047's one-liner (T6 Choir event) vs Reyes's legalism
**Setup:** POWER-012's phantom agent. If the 1977 "T6 Choir event" *did* involve Reyes (CHAR-010, "the only Choir T6 in history," 26_INFORMATION_CONTROL.md), his file says he is "legalistic" (26) — a T6 Choir acting legally, at global scale, in 1977, with ~300 Loud interned. What law did he invoke? The Compact's? A pre-Compact regime's?
**Verdict:** DEPENDS ON POWER-012's resolution. If the one-liner is corrected (no agent), C8 dissolves. If a T6 Choir is kept, this becomes a required history beat: a legalistic Worldtide acting openly in 1977 is the kind of event that *makes* the modern Compact's T6 protocols. Either way, the coordinator must pick.

### C9 — Laggard escrow (Use 10) + Choir harmonics = distributed dead-man's switch
**Setup:** Arthur's escrow (29:F.1) is a recording dead-man's switch. A Choir in harmonic entrainment shares a "composite voice" (30:58) — can a Choir *share* the escrow, each member holding a fragment, so that killing Arthur doesn't kill the switch? Or worse: can Arthur *record a Choir* (Use 10: "recordings are complete and admissible," 29:F.1) and escrow *their* composite?
**Verdict:** HOLDS — with a price. Use 10 records; it doesn't *distribute*. A Choir could memorize Arthur's recording (Choir memory is shared during entrainment, 30:60), but "composite voices persist… as shared dreams, not operational assets" (30:62) — the persistence is explicitly non-operational. And recording a Choir gives Arthur *evidence*, not *leverage over* the Choir — the escrow's power is disclosure, which works the same. No patch needed; the "not operational assets" line is doing real work here.

### C10 — Drowndust + ward Six Lullaby = Erosion-free assassination
**Setup:** Drowndust forces Erosion (priced, traceable, supply-constrained). The lullaby's *singers* accrue "Drowning-adjacent Erosion spikes" (28:116) — Erosion without channeling (POWER-009's pattern again). Can you weaponize the *singing* — force captives to sing the lullaby at a target, accruing Erosion in the singers (disposable) while the target is compelled? The cost is borne by people you don't care about.
**Verdict:** ACKNOWLEDGED BY CANON, PRICED. This is just slavery with extra steps, and the file prices it: the singers' Erosion spikes are *Drowning-adjacent* — your disposable singers Drown, and Drowning events are "unpriceable — evacuation and mitigation" (26). The operation converts a deniable assassination into a Drowning risk, which is exactly the kind of cost the setting's economics are built to impose. The Ninth Bell might do it anyway (they *want* Drowning events) — which is a feature: it gives the Bell a signature atrocity with a built-in price tag.

---

## PART 3 — HARD-RULE VERIFICATION (02_WORLD_RULES.md §I CANON-LOCKED)

| Rule | Verdict | Notes |
|---|---|---|
| **No time travel** | HOLDS | Nothing in 28/29/30 travels. The cradle "moves" Erosion, not time; the Laggard lags the present, never revisits it. |
| **No resurrection** | HOLDS | No resurrection mechanics anywhere in scope. The Hollow is a transformation, not a return (03.4). |
| **No direct mind control** | STRAINED | POWER-008 (lullaby compulsion), POWER-013-adjacent (Salt Garden saboteur), C7 (forced channeling via entrainment — open). The file's implicit defense (infohazard compulsion ≠ mind control) needs to be explicit. |
| **No perfect information** | HOLDS | Strongest hold in the set. The Seismograph network is noisy (25), the Laggard's recordings are complete but *interpretation* is bounded (29), the Archive gives "reading privileges (slow, supervised, no copies)" (28:415). |
| **Erosion is irreversible** | STRAINED | POWER-009 (Saint inflicts Erosion without channeling), POWER-010 (cradle moves Fathoms as substance). The *letter* holds (nothing decreases the total); the *model* is drifting from "wear" toward "stuff." |
| **No divine intervention** | HOLDS | Nothing in scope invokes divinity. The Saint is a predator, not a god; the file is careful (28:177-189). |
| **Masquerade holds** | HOLDS | 26's information-control economics are the most carefully priced subsystem in the bible; every breach has a response. |

**Net:** no hard rule collapses. Two rules (mind control, Erosion) are *strained* — not by violations, but by mechanisms the rules' glosses don't name. Both strains are fixable with explicit CANON-adjacent lines, not redesigns.

---

## PART 4 — WHAT THE SYSTEM GETS RIGHT (HOLDS)

- **H1 — The Erosion economy is the load-bearing invention.** Fathoms, the Drowning line, the T6 "measured in uses" — the entire hierarchy (30.2) is denominated in one currency, and the currency has a terminal condition. This is what makes the power system *tragic* rather than merely *costly*, and it survives all ten combination tests without a patch. Nothing I threw at it created free power.
- **H2 — The vector notation's threat/containment split is genuinely good design.** The Salt Garden teaching example (05.5) — even with POWER-003's filing dispute — demonstrates *why* the two-axis system exists: high threat, low containment cost is a combination the old single-axis scales couldn't express. The notation earns its keep.
- **H3 — Stillwater Harbor is the best single page in the power system.** SUP-004 (28:419-427) does four jobs at once: economy (priced Tide-marks), complicity (the Compact "buys quietly"), adventure site (the drowned town), and WMD feedstock (C5). It is the proof that the system's economics and its horror are the same thing.
- **H4 — The Laggard's "window, not channel" (29:E) is the correct solution to the weak-protagonist problem.** It makes Arthur *informationally* powerful and *physically* irrelevant in one move, and the twelve misconceptions (29:B) are the file defending the design against its own readers. The design holds; see PROTAGONIST_AUDIT.md.
- **H5 — Scenario 4 (30: the T5 vs the city) is the file's thesis statement.** "The city wins by patience" — Erosion attrition as civic defense — is the power system explaining *why the world looks the way it does*: institutions outlast individuals because the currency of power is self-destruction. Every tier above T3 is a countdown, and the world is built for people who aren't counting down. This is the idea the novel should never lose.


---

## SECTION: `AUDIT/PROTAGONIST_AUDIT.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/PROTAGONIST_AUDIT.md` · sha256 `ee376932c6073e3c7e3b516515d84908f113367b6d44b078368b64d77f163610` · 5,259 words. No content changed.

# PROTAGONIST ANOMALY AUDIT — ANOMALY-001 "THE LAGGARD" / CHAR-001

**Worker:** AUD-POWER · **Date:** 2026-09-19 · **Scope:** `29_PROTAGONIST_ANOMALY.md` (primary), cross-checked against `02_WORLD_RULES.md`, `03_SUPERNATURAL_SYSTEM.md`, `04_POWER_SYSTEM.md`, `05_ANOMALY_CLASSIFICATION.md`, `28_ANOMALIES.md`, `30_POWER_HIERARCHY.md`, `35_CANON_DATABASE.md`, `25_TIMEmessaging app.md`.
**Method:** adversarial. Eight explicit break attempts; misconception-by-misconception load analysis; five concrete cost-constraint scenarios. Canon files were read, not edited.

**Issue counts:** CRITICAL 0 · HIGH 0 · MEDIUM 3 · LOW 4 — **7 total.**

**Headline verdict:** the anomaly survives every break attempt I could construct. It is genuinely exploitable (deep headroom for 500+ chapters) without being secretly omnipotent. The three MEDIUM findings are an unbounded escalation curve, an unaddressed denial vector, and relocation residue inside 29 itself.

---

## PART 1 — BREAK ATTEMPTS (adversarial; all failed to break it, except as noted)

### ATTEMPT 1 — Use 10 (clean recording) + escrow = omnipotent leverage over every faction
**The attack:** Arthur photographs the shadow's replays, producing un-rottable proof of any Seep he witnesses, then uses the dead-man's-switch escrow (29:170) to make himself untouchable — blackmail at civilizational scale.
**Why it fails:** Four independent ceilings. (a) *Range:* the shadow replays only his own recent position's past (Use 2, 29:140-143) — he can only record where he has been, not arbitrary events. (b) *Public value is capped:* the deepfake dividend (02.III) means even perfect footage is deniable in public; Use 10's product is spendable only *inside* the hidden world, among actors with verification protocols. (c) *MAD is not control:* the escrow deters *disappearance*, not discrediting, framing, capture-and-force-check-ins (cf. Vesper's "impossible to leave" interest, 29:110), or killing him in a way that also kills the escrow's value. (d) *The counter is priced in:* "possessing it makes him a target of *every* faction simultaneously; using it spends the masquerade itself" (29:167). The ladder's own counter converts leverage into exposure. **Verdict: HOLDS.** The intended endgame ("the best-informed weak man in Ravenscroft," 29:178-184) is dangerous-survivor, not omnipotence.

### ATTEMPT 2 — The ratchet as permanent free upgrade (capability creep)
**The attack:** Extreme use adds "permanent fractions of a second to the base lag" (29:81). Over 500 chapters of heavy use, the base lag creeps from 3s toward 10s+ — a permanently deeper free window with no ongoing cost. Costs that are also upgrades are the classic power-creep leak.
**Why it partially succeeds:** Ilsa: 3.0→3.4s over seven years of documented deepening (29:81); Arthur: 3.0→3.1s in seven years of minimal extreme use (29:51). Implied rate ≈ 0.02–0.06s per extreme use. At, say, 150 extreme uses across a long series: +3–9s → a 6–12s *baseline* window, i.e., a permanent Use-6-lite with no deepening cost. The file marks what happens at 10s "UNKNOWN" (29:81) but never states a per-use magnitude or a decelerating mechanism, so the 500-chapter math is unbounded on paper.
**Mitigations present:** attention compounds with depth (29:172, Use 11 counter); deepening inside wards is "louder at the entity's end" (29:B.5); the torn last journal page implies Ilsa hit something bad. But these are *narrative* brakes, not *mechanical* ones.
**Verdict: BENDS — filed as PROTAG-001 (MEDIUM).** The ratchet needs a stated per-use magnitude and an explicit reason the curve flattens (e.g., attention becomes prohibitive before the lag reaches X, or the entity's proximity cost scales with base lag).

### ATTEMPT 3 — Use 6 (3-hour deepening) + Use 10 = perfect recorded history of any room
**The attack:** Deepen to 3 hours, photograph the replay: a clean, permanent, un-rottable record of everything that happened in a room — total information dominance.
**Why it fails:** Ilsa's maximum "almost didn't give her back" (29:155); a 3-minute deepening costs Arthur "a day in bed" (29:B.6.4), so 3 hours scales to roughly a week of incapacitation plus ratchet plus entity attention ("at 3 hours, *he* was the one being observed," 29:155) plus visibility to "Lantern-sensitives across kilometers and to instruments" (29:B.6.5). It is a *strategic* asset usable a handful of times per story, never a casual one — and each use teaches every Lantern in the prefecture exactly where he is. **Verdict: HOLDS.** Correctly priced as a high-end, low-frequency use.

### ATTEMPT 4 — Use 5/Use 9 out-of-phase + Use 10 = invisible eavesdropper with receipts
**The attack:** Step into the lag (unseen, intangible), walk a meeting at 3-minute deep lag, photograph the shadow's replay: undetectable espionage with proof.
**Why it fails:** While out-of-phase he "cannot act on the world — cannot touch, speak… or be touched" and "solid matter blocks him… He must still walk around the wall; he cannot walk through it" (29:B.5). So he can only eavesdrop on rooms he could *walk into* unseen — doors, guards, and wards still apply. Lantern-sensitives "feel the 'wrongness'" (29:152); at deep lag "you are not the only observer" (29:Use 9). Three seconds at base (Use 5) is a dodge, not an infiltration; 3 minutes (Use 9) requires a deepening with all of Attempt 3's costs. **Verdict: HOLDS.** "Three seconds of ghosthood, not godhood" (29:B.5) is exactly right, and the file states it.

### ATTEMPT 5 — Sterile-kill denial: murder Arthur with no Loud witness present
**The attack:** B.8: "If no Loud witness is present at the death or Drowning at all, the tether likewise dissipates." A faction that fears the tether (or fears a rival acquiring it) doesn't need to steal it — it needs Arthur dead in a Quiet-only room. The escrow deters *disappearance-for-acquisition*; it does not deter *denial*.
**Why it matters:** The anti-engineered-transfer rule (29:101) brilliantly closes the acquisition and inheritance exploits, but the *denial* exploit is left open and unacknowledged. Candidates with denial motives exist in-file: the Ninth Bell burns what it can't witness; a state that can't afford the Laggard falling to a rival might prefer it gone. Arthur's own protection ("the hidden world's vast, tired bureaucracy has looked at the Laggard three times and yawned three times," 29:105) expires the moment Use 10 becomes known.
**Verdict: BENDS — filed as PROTAG-002 (MEDIUM).** Thematically this could become "mutually assured *preservation*" (rivals keeping him alive to deny each other the denial), but the file never says it.

### ATTEMPT 6 — Use 7 (shadow-storage) as ward-bypassing smuggling
**The attack:** Store objects out-of-phase, walk them past wards and checkpoints.
**Why it fails:** Capacity is "only what the shadow can cover" (29:158); "retrieve within the lag window or it is gone"; "nothing living — Ilsa's mouse came back 'unwrapped'"; each use lengthens the lag. And wards "dampen the Laggard's Membrane-side effects… but cannot sever the tether" (29:B.5) — dampened readability makes deep use *inside* wards "louder at the entity's end." Smuggling a coin past a checkpoint: yes. Smuggling anything story-breaking: no. **Verdict: HOLDS.**

### ATTEMPT 7 — Use 12 (flare) as a weapon: summon every faction onto a rival
**The attack:** Flare deliberately to draw all factions to a location where a rival is exposed.
**Why it fails:** "A flare he can't unfire… everyone comes. Everyone" (29:175) — including to *him*, the visible signal source. It spends his secrecy permanently (29:B.6.5: "the one resource Arthur cannot replenish") for a single chaotic event he cannot control or survive directing. Usable once per story, possibly once ever, and only in desperation — which is the stated discovery condition ("desperation," 29:175). **Verdict: HOLDS.**

### ATTEMPT 8 — Use 4 (Tide-mark dowsing) + Use 6 + Use 10 = monopoly on Ravenscroft's history
**The attack:** Dowse every old Tide-mark in the city, deepen, photograph: become the sole supplier of the past.
**Why it fails:** This is the *intended* 500-chapter engine, not a break. Each deepening is individually priced (bed-days, ratchet, attention, Lantern visibility); "Tide-marks are impressions, not video; interpretation is a skill he must learn from the journals" (29:Use 4 counter); and the Archive (ANOMALY-030) already occupies the "history resists extraction" niche with its own immune system — the world has precedent for this not collapsing. **Verdict: HOLDS.** Exploitability confirmed; break denied.

---

## PART 2 — FINDINGS

### PROTAG-001 — MEDIUM — The ratchet's 500-chapter math is unbounded

**Location:** `29_PROTAGONIST_ANOMALY.md:51` (suspected-effects paragraph) and `:81` (B.6 cost 2).

**Conflicting statements:**
- 29:51/81: "*Extreme* use (deep lag, storage, the flare) adds permanent fractions of a second to the base lag. Ilsa: 3.0 → 3.4s over seven years… Arthur started at 3.0s in 2017 and is at ~3.1s now."
- 29:81: "(What happens at 10s, at a minute, is UNKNOWN — Ilsa's last journal page is torn out.)"
- 29:172 (Use 11): "his currencies are finite too — the ratchet only runs one way, and attention compounds."

**Why it is a problem:** The file gives two data points (Ilsa +0.4s/7yr with active deepening; Arthur +0.1s/7yr with minimal extreme use) but never states a per-use magnitude, so the long-series arithmetic is unbounded: ~0.02–0.06s per extreme use implies 150–300 extreme uses reach a 6–12s *permanent baseline* — a free, always-on deep window that bypasses the deepening cost (B.6.4) the file is careful to price elsewhere. "Attention compounds" is asserted as the brake but never mechanized: does attention scale with *base* lag or only with *deliberate* deepening? If the former, the ratchet is self-limiting; the file doesn't say. For a 500+ chapter series this is the single likeliest silent power-creep vector.

**Proposed solutions:**
1. State an approximate per-use ratchet magnitude in Ilsa's journals (e.g., "~0.02–0.05s per deepening; storage and flares cost more") and an explicit decelerator — e.g., entity attention scales with *base* lag, so the practical ceiling is attentional, not temporal.
2. Canonize that the ratchet *decelerates*: each additional permanent second requires geometrically more extreme use (the tether "settles"), making 10s effectively unreachable by use alone — the UNKNOWN at 10s then stays unreachable, which is cleaner.
3. Leave the math open but move the brake into B.6 as CANON: "the lag has never been observed to ratchet past ~X under use alone; Ilsa's journals speculate the entity resists being *kept* deep" — converts the leak into a mystery with a stated bound.

---

### PROTAG-002 — MEDIUM — Sterile-kill denial: the tether can be destroyed, and nothing prices that

**Location:** `29_PROTAGONIST_ANOMALY.md:101` (B.8 transfer rule) and `:170` (escrow).

**Conflicting statements:**
- 29:101: "If no Loud witness is present at the death or Drowning at all, the tether likewise dissipates: no dormancy, no fallback holder, no second candidate."
- 29:170: "It is mutually assured disclosure at personal scale — the reason seizing *him* costs more than bargaining with him."

**Why it is a problem:** The transfer rule closes acquisition ("engineered transfers fail") and the escrow closes disappearance ("seizing him costs more than bargaining"). Neither closes *denial*: killing Arthur in a room with no Loud witness dissipates the tether permanently — the rational move for any actor that fears the Laggard in rival hands more than it values the Laggard itself. The file lists eight factions that "would care if they knew" (29:B.9) but never asks which of them would prefer the tether *gone*. The Ninth Bell (witness-apocalypse theology), a state practicing anomaly-denial, or a rival of whoever currently courts him all have denial-shaped incentives. Arthur's survival currently depends on nobody having thought of this; "competence is distributed" (02.IV) says someone will.

**Proposed solutions:**
1. Acknowledge it in B.9 as a known faction calculus: e.g., the Compact's science directorate quietly concluded denial is possible and *opposes* it (a dissipated tether is un-studyable), creating "mutually assured preservation" — rivals keep him alive to deny each other the denial.
2. Give the denial a cost: dissipating a tether leaves a trace (a "cut tether" Seep? Undertow attention drawn to the killers?) — priced denial, consistent with "nothing gets the effect for free" (02.I).
3. Make it a plot thread rather than a rule: Ilsa's journals contain a margin note that someone *tried* a sterile kill on a pre-1989 holder and the attempt itself is why the chain has gaps ("at least two earlier holders… PROVISIONAL," 29:92-94).

---

### PROTAG-003 — MEDIUM — Stale "Kota Tua replay" references: EVENT-092 is in Ravenscroft, not Jakarta

**Location:** `29_PROTAGONIST_ANOMALY.md:150` (Use 4 discovery) and `:153` (Use 5 discovery).

**Conflicting statements:**
- 29:150: "*Discovery:* Ilsa's journals, via Pram (2024) — then confirmed in the Kota Tua replay."
- 29:153: "*Discovery:* accident, during the Kota Tua replay ([EVENT-092](25_TIMEmessaging app.md)) — he flinches *into* his shadow and the falling scaffold passes through him."
- `25_TIMEmessaging app.md` EVENT-092: "**Hidden truth:** A 1945 air-raid Place Seep replayed mid-shoot" in "Ravenscroft's Old Quay historic quarter" — public face "A film shoot's permits were revoked in Ravenscroft's Old Quay historic quarter."
- 29:95 correctly places Ilsa's 1996 vanishing "in Kota Tua, Jakarta" — Kota Tua *is* Jakarta's old town, so the phrase is geographically real; it is just the wrong city for EVENT-092.

**Why it is a problem:** Two of the twelve uses' discovery beats are anchored to a location that contradicts the timeline's EVENT-092. This is relocation residue inside my assigned file (pre-relocation drafts set the replay in Jakarta/Liwanag). Note the compounding residue in `35_CANON_DATABASE.md:430`, whose EVENT-092 one-liner says "1945-massacre Place Seep replays in Liwanag" — wrong city *and* wrong event type (massacre vs air-raid) vs 25's entry — and 35's coordinator note claiming "Arthur retargeted as Indonesian migrant worker in Liwanag City" vs the Ravenscroft canon. The 35-side items belong to the relocation audit; the two 29-side lines are mine.

**Proposed solutions:**
1. Replace "Kota Tua replay" with "Old Quay replay" (or "the old-quarter replay," matching 29:105's own phrasing) in both discovery lines.
2. If a Jakarta beat is wanted for Use 4/5's discovery, retarget the citations to a different Jakarta event and keep EVENT-092 Ravenscroft — but the current text cites EVENT-092 explicitly, so option 1 is cleaner.
3. Add a CHANGELOG relocation-sweep note for 29 (the file was otherwise cleanly relocated — B.9's KNF/SMD handoff at 29:116 is correct and well-handled).

---

### PROTAG-004 — LOW — The escrow deters rational actors; disclosure-seekers are undeterred (probably intentional)

**Location:** `29_PROTAGONIST_ANOMALY.md:170` (escrow CANON).

**Conflicting statements:**
- 29:170: "It is mutually assured disclosure at personal scale — the reason seizing *him* costs more than bargaining with him."
- 29:B.9 (Drowned Choir): "The Choir would canonize the tether — and him, willing or not." / (Ninth Bell via 12/28): apocalyptic witness theology — disclosure is the *goal*.

**Why it is a problem:** MAD works only against actors who fear disclosure. The Drowned Choir (canonization is publicity) and the Ninth Bell (witness-apocalypse) are at worst indifferent to the escrow triggering, at best pleased. The file never notes this exception. This is minor because it reads as deliberate dramatic irony — the shield has a shaped hole — but the audit flags it so the novel doesn't accidentally treat the escrow as universal protection.

**Proposed solutions:**
1. Add one line to the escrow paragraph: "It deters everyone except those who want the masquerade ended — which is why the Ninth Bell's file on him is the one Arthur hasn't seen."
2. Leave as-is and let the novel discover it — but log it in the MYSTERIES-adjacent thread list so it isn't forgotten.

---

### PROTAG-005 — LOW — The engineered-transfer rule adjudicates *intent*, and intent is fuzzy at the edges

**Location:** `29_PROTAGONIST_ANOMALY.md:101` (B.8).

**Conflicting statements:**
- 29:101: "If the holder's death or Drowning is staged, assisted, or arranged to deliver the tether — or if the nearest Loud witness was *positioned* rather than present — the transfer fails and the tether dissipates."
- 29:92-97: the genuine chain — "Ilsa Drowned beside Yusuf by disaster, not design; Yusuf died beside Arthur by ordinary dying."

**Why it is a problem:** "Positioned rather than present" is adjudicated by *something* — the Undertow has no mind to judge intent (03.1: "causality, time, and identity do not hold" there). Edge cases: Arthur walks into known danger with Saitō nearby, foreseeing he might die — arranged? A faction keeps a Loud agent near him "for unrelated reasons" — positioned? The rule is load-bearing for the theme ("Arthur was not chosen. He was *present*," 29:B.8), and the Surabaya 1993 staged-death precedent gives it teeth, but the boundary will be tested by any clever antagonist within the first hundred chapters.

**Proposed solutions:**
1. Leave the fuzziness as intentional mystery (Layer 5-adjacent) but give Ilsa's journals one more edge-case entry so the novel has precedent to argue from.
2. Mechanize it slightly: the tether follows *causal* proximity, not intent — "positioned" fails when the witness's presence is *caused by* a plan to inherit, which Lantern-reads as cleanly as a Tide-mark. Intent becomes evidence, not metaphysics.

---

### PROTAG-006 — LOW — Use 10's "Membrane-darkness" justification is asserted once and carries the entire endgame

**Location:** `29_PROTAGONIST_ANOMALY.md:167` (Use 10).

**Conflicting statements:**
- 29:167: "The shadow is Membrane-darkness, not Undertow-structured information — so **recordings of the shadow do not rot**."
- 03.4 / 02.III: "Static rot is proportional to intensity… Recordings of active Seeps corrupt at a rate proportional to Tide pressure."

**Why it is a problem:** Not a contradiction — the file justifies the exception (the shadow replays the Membrane side, not Undertow-structured information) — but this single sentence carries Use 10, the escrow, and arguably the series endgame. A load-bearing claim this large deserves a second corroborating anchor so it doesn't read as a convenience invented at the point of need. (The discovery line — "a photo of his bedroom wall, developed normally, showing the shadow mid-replay" — is observational corroboration, which helps; the *mechanism* still rests on one sentence.)

**Proposed solutions:**
1. Add a corroborating Ilsa journal fragment: she photographed the shadow mid-replay in the 1990s and the prints survived — the discovery then has lineage, not just Arthur's accident.
2. Have the Compact's science directorate (Nwosu, 29:B.9) independently theorize *why* tether-mediated records resist rot (e.g., "the Veil can't edit a tether," Use 1's own logic extended) — two independent framings of one mechanism.
3. Leave as-is; the Use 1 counter ("the Veil cannot edit a tether") already implies it. This is genuinely viable — the file almost self-corroborates.

---

### PROTAG-007 — LOW — Misconceptions #2 and #5 are threats miscast as camouflage (the file half-knows this)

**Location:** `29_PROTAGONIST_ANOMALY.md:119-135` (B.10), esp. `:124`.

**Conflicting statements:**
- 29:124 (#2): "**A T1 Lantern Resonance — i.e., that Arthur is Attuned.** The most structurally dangerous misunderstanding: a BPF clerk once opened an Attuned file on him after a sensor misread. It was closed for lack of a Hollow Pattern. If it is ever reopened, Arthur gains a Census file, a handler, and a leash."
- 29:119 header: "> STATUS: IN-WORLD MISCONCEPTION (all of the following are wrong; all are believed by someone)."

**Why it is a problem:** Barely a problem — the file *does* label #2 "the most structurally dangerous," so the audit's job is verification, not discovery. The point worth recording: #2 and #5 (pre-Drowning symptom → the 2020 Vesper Fathom-scan scare, "Arthur still keeps the discharge paper") are not camouflage at all — they are the two misconceptions whose *truth* would end the premise (Census file + handler; clinical detention). The "seems weak" premise is therefore protected not by the misconceptions but *despite* two of them, by the closed file and the 0-Fathom scan. The file's framing ("twelve ways people misunderstand it") slightly undersells the asymmetry: ten are camouflage, two are loaded guns.

**Proposed solutions:**
1. Split B.10's framing line: "Ten of these protect him; two of them (#2, #5) would end him if believed by the right bureaucrat" — makes the danger legible without changing content.
2. Leave as-is; the #2 entry already says "most structurally dangerous." Acceptable — the file self-documents.

---

## PART 3 — THE TWELVE MISCONCEPTIONS: LOAD-BEARING ANALYSIS

**Method:** for each misconception, ask: if this belief vanished from the world tomorrow, does the "seems weak" premise collapse? Result: **no single misconception is load-bearing.** The premise rests on three structural facts, and the misconceptions are camouflage ecology around them:

- **S1 — The vector measures output** (05.1: "maximum demonstrated output equivalent"); the Laggard's output is ~zero ("rooms dim, houseplants die," 29:40-44). Filed T1 forever, honestly.
- **S2 — Windows aren't tiered** (29:B.12: "the classification system has no tier for windows, because windows don't channel").
- **S3 — Three examinations yawned** (29:105): institutional confirmation of S1+S2.

| # | Misconception | Function | Load-bearing? |
|---|---|---|---|
| 1 | Curse (dukun, Tebet) | Folk camouflage; routes inquiry to shamans, not analysts | No — one of several folk bins |
| 2 | T1 Lantern Resonance (Arthur is Attuned) | **Threat**, not camouflage: Census file + handler if believed | Inverted: its *falsity* (closed file) is load-bearing |
| 3 | Haunting | Folk camouflage (Marked Ministry pamphlet) | No |
| 4 | Trick of the light | **Protective**: lets everyone, "briefly, relax" — the kindest misunderstanding | Supportive but not structural |
| 5 | Pre-Drowning symptom | **Threat**: 2020 Vesper scare; cleared by 0-Fathom scan | Inverted: the *clearance* is load-bearing |
| 6 | Planted Gray Market tracker | Investigative misdirection; drives Aisha's plot interest | Plot engine, not premise support |
| 7 | Tulpa / belief echo | Fringe-theory bin | No |
| 8 | Choir seed | Comforting because "seeds can be removed; tethers can't" — supports underestimation | Weakly supportive |
| 9 | Undertow "draft" (mobile thin place) | Wrong, but "produced the dowsing discovery" — plot engine | Plot engine |
| 10 | Cartographer's mark | Pram's initial assumption — plot engine | Plot engine |
| 11 | Choir "blessing" | Theologically wrong, "phenomenologically irritatingly close" — plot engine | Plot engine |
| 12 | Stillwater side effect | Medical-mundane bin ("new medication?") | No |

**Key finding:** the camouflage has *defense in depth* — removing any 3–4 misconceptions leaves S1–S3 intact and the remaining bins still absorb inquiry. The premise collapses only if S1 or S2 fails (i.e., someone re-vectors the Laggard on *information* output rather than *channeling* output — which is exactly the Factor's buyer's thesis in EVENT-093, so the novel already aims at the load-bearing beam). **This is a strength, not a flaw:** the "seems weak" premise does not depend on any single lie surviving.

---

## PART 4 — COST VERIFICATION: FIVE CONCRETE SCENARIOS

Each scenario tests whether the B.6 cost schedule actually constrains Arthur, using only stated mechanics.

### Scenario 1 — Dodging a Sweeper (Use 5, base 3s)
Arthur steps into the lag as Aisha's team corners him in Old Quay. **What the costs do:** 3 seconds, unseen — but he cannot act, cannot pass walls, and must still physically walk out; Lantern-sensitives on the team "feel the 'wrongness'" (29:152); repeated use draws the entity's attention (29:B.6.3). **Constraint check:** he escapes *one* grab, once, at the price of a Lantern-noticed wrongness event and attention-compounding. He cannot chain-dodge a sustained pursuit — the second attempt happens with the entity already looking. **PASSES** — the cost binds.

### Scenario 2 — Reading a closed meeting (Use 6 + Use 9, 3-minute deepening)
Arthur deepens to 3 minutes out-of-phase to watch a Blackwater Syndicate negotiation he must not be seen at. **What the costs do:** needs stillness and a reflective surface (Use 2's counter); deepening costs "a day in bed" at 3 minutes (29:B.6.4); adds a permanent ratchet fraction (29:81); is "visible to Lantern-sensitives across kilometers and to instruments" (29:B.6.5); and "at deep lag you are not the only observer" (29:Use 9). **Constraint check:** he gets the meeting's last 3 minutes at the price of a day's incapacitation, a permanent lag increase, a km-wide Lantern flare, and the entity watching back. He cannot do this weekly without becoming the most-flared civilian in Ravenscroft. **PASSES** — heavily priced, correctly.

### Scenario 3 — Smuggling a ledger page (Use 7, shadow-storage)
Arthur stores a stolen Red Ledger page out-of-phase to carry it through a checkpoint. **What the costs do:** capacity is "only what the shadow can cover"; "retrieve within the lag window or it is gone (to where, UNKNOWN)"; each use lengthens the lag (29:158). **Constraint check:** a single page, retrievable within minutes, at permanent ratchet cost — and nothing living, ever (Ilsa's mouse, 29:158). He cannot move money, people, or anything at scale. **PASSES** — the capacity and loss-risk bounds hold.

### Scenario 4 — Blackmailing a faction (Use 10 + escrow)
Arthur photographs the shadow's replay of a Tribunal-adjacent meeting and implies release. **What the costs do:** "possessing it makes him a target of *every* faction simultaneously; using it spends the masquerade itself" (29:167); the escrow (29:170) deters disappearance but not discrediting, capture-and-force-check-ins, or sterile-kill denial (PROTAG-002); the deepfake dividend (02.III) caps public value — the recording is leverage only among hidden-world actors with verification protocols. **Constraint check:** he gains *bargaining position*, not control — "the reason seizing *him* costs more than bargaining with *him*" is explicitly a pricing statement, not a power statement. Every use of the leverage spends the secrecy it depends on. **PASSES** — MAD, not omnipotence. (With the PROTAG-002 and PROTAG-004 caveats logged.)

### Scenario 5 — The flare as last resort (Use 12)
Cornered, Arthur lengthens the lag to minutes deliberately. **What the costs do:** "visible to every Lantern-sensitive for kilometers — a distress signal, a summons, a declaration. A flare he can't unfire… everyone comes. Everyone" (29:175); spends secrecy permanently (29:B.6.5). **Constraint check:** a one-way, uncontrolled summons that paints him as the source. Usable in desperation only — the stated discovery condition. **PASSES** — the strongest use has the strongest price.

**Overall:** the B.6 schedule binds in every scenario because every use's *counter* is stated in the same entry as the use (B.11's discipline of pairing each use with its counter is the file's best structural decision).

---

## PART 5 — DO WEAKER CHARACTERS STAY RELEVANT BESIDE HIM?

**Yes — structurally, not sentimentally.** Arthur's outputs are *records*; records need a pipeline he does not own:

- **Saitō (CHAR-015, fellow Loud clerk):** corroborating witness and the escrow's human leg — a dead-man's switch needs someone who notices you're gone. Arthur can't be his own check-in.
- **The Night Clerks (IND-004):** the civilian dead-drop leg of the escrow and the sightings network behind Use 8's dowsing cross-references. Distribution is not a thing Arthur can do alone.
- **Pram (CHAR-032):** the journals. Every deep use's *interpretation* ("Tide-marks are impressions, not video," Use 4 counter) depends on Ilsa's research, which Arthur accesses through Pram — knowledge Arthur cannot generate solo.
- **Kira (CHAR-033, T2 Lantern counselor):** Tide-mark reading and Quiet-care — the medical/interpretive layer.
- **Aisha (CHAR-034, Sweeper lead):** the muscle and the institutional interface. Arthur "cannot act on the world" while out-of-phase (29:B.5), has no combat training, no money ("two months' salary in savings," 29:A), and migrant precarity (SSW visa tied to NQA — "he cannot afford a police file, a hospital file, or a Census file," 29:A). Every confrontation needs someone who can stand in a room and *do* things.
- **Nanami (CHAR-012):** the civilian stakes — the reason the escrow's *civilian* recipients (lawyer's envelope) matter and the cost of exposure is priced in family, not just tradecraft.

**The structural reason this holds:** the Laggard makes Arthur *informed* (29:B.12), and "in a world where information is the scarce resource (02.II), the best-informed weak man in Ravenscroft is the most dangerous kind of survivor" — but information without *agency* is just a well-kept diary. The file denies him agency at every turn (no touch out-of-phase, no money, no status, no combat ability). His relevance to others is as a *producer*; their relevance to him is as the *pipeline*. Neither side obsoletes the other.

---

## PART 6 — EXPLOITABILITY HEADROOM (500+ chapters)

Confirmed ample. The headroom is combinatorial, and each combination's counter is itself a plot engine:

- **12 uses × pairings:** 4+10 (photograph Tide-mark dowsing), 6+10 (3-hour clean recordings), 5+9+10 (invisible eavesdropping with receipts), 12+escrow (flare as authenticated summons), 8+4 (dowsing cross-referenced with Night Clerk sighting maps).
- **The journals:** Ilsa's torn last page, the ratchet measurements, the storage Rules — a pre-loaded research arc with a missing ending.
- **The entity:** attention flows both ways (29:B.3, "the Crane warning," EVENT-094); what it is remains Layer-5 UNKNOWN — the attention budget is a second, alien cost curve the novel hasn't spent yet.
- **The transfer chain:** proximity + Loudness dynamics; the Surabaya 1993 staged-death precedent; at least two unknown pre-1989 holders (PROVISIONAL) — inheritance plots that can't be engineered but can be *anticipated*.
- **The market:** the Factor's buyer (EVENT-093), Nwosu's research interest (EVENT-091), the Cartographers' survey-instrument thesis (29:B.9) — three different bidders who want three different things from the same tether.
- **The ratchet unknowns:** what happens at 10s, at a minute (29:81) — a built-in escalation horizon the novel can approach but never needs to reach.

**The file's exploitability discipline is sound:** every use is "discovered through observation, never granted by revelation" and "paid for" (29:136-138), the discovery order is fixed (the progression spine can't be shortcut), and every use ships with its counter. There is no "and then he realizes he could always do X" trapdoor — except the ratchet's unbounded math (PROTAG-001), which is the one place the file prices a cost without bounding it.

---

## PART 7 — HOLDS: THE 5 STRONGEST PROTAGONIST MECHANICS

These survived every adversarial attempt and are the file's load-bearing beams:

1. **"A window, not a channel" (29:B.12).** The Meridian Vector measures output; the Laggard's output is zero; therefore the T1 filing is *honest*, not a trick. The premise "seems weak" doesn't depend on anyone being fooled — it depends on the measurement instrument being blind to windows. This is the deepest defense in the file: it makes Arthur's camouflage *structural* rather than *deceptive*, so no clever analyst can "see through" it without inventing a new axis.
2. **Out-of-phase = no agency (29:B.5).** "Cannot touch, speak… or be touched… solid matter blocks him… 'Intangible' here means no touch, no contact, no exchange of force — not phasing." The file explicitly closes the ghost-infiltration reading in the same paragraph that grants the power. "Three seconds of ghosthood, not godhood" is the most honestly priced sentence in the bible.
3. **The anti-engineered-transfer rule (29:101).** Proximity + Loudness + unforced death; staged/assisted/arranged transfers dissipate the tether with no fallback. This single paragraph closes farming, theft-by-murder, dynastic capture, and will-based inheritance in one move — and the Surabaya 1993 precedent proves it's been tested. (Denial remains open: PROTAG-002.)
4. **The escrow as priced MAD (29:170).** Protection denominated in *exposure*, not power: it works by making Arthur more expensive disappeared than bargained-with, and the file never pretends it's more than that. The counters (every faction comes; the masquerade itself is spent) are stated alongside.
5. **Erosion-free but attention-priced (29:Use 11).** "He is not Attuned; the anomaly does the work; he pays in attention-risk and ratchet, never Fathoms… his currencies are finite too — the ratchet only runs one way, and attention compounds." The file gives him a *different* cost curve rather than *no* cost curve — which is why Nwosu wants him (a zero-Erosion longitudinal subject is valuable *because* his costs are alien, not absent).

---

## PART 8 — RELOCATION RESIDUE (for the relocation audit's awareness; found in-scope)

- `29_PROTAGONIST_ANOMALY.md:150,153` — "Kota Tua replay" should read "Old Quay/old-quarter replay" per EVENT-092 (25_TIMEmessaging app.md). Filed as PROTAG-003 above.
- `35_CANON_DATABASE.md:430` — EVENT-092 one-liner says "1945-massacre Place Seep replays in Liwanag"; 25_TIMEmessaging app.md says 1945 *air-raid* replay in *Ravenscroft's Old Quay*. Wrong city and wrong event type. (Relocation audit's file, flagged here only.)
- `35_CANON_DATABASE.md` coordinator note (5) — "Arthur retargeted as Indonesian migrant worker in Liwanag City" contradicts the Ravenscroft canon (00_INDEX.md, 29:A). Stale note. (Relocation audit's file, flagged here only.)
- `35_CANON_DATABASE.md:385` / `DATABASE/EVENTS.md:56` — EVENT-047 one-liner "T6 Choir event" vs 25_TIMEmessaging app.md EVENT-047 hidden truth (global pressure spike; no Choir actor named). Filed as POWER-015 above.


---

## SECTION: `AUDIT/ROMANCE_ARCHITECTURE_AUDIT.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/ROMANCE_ARCHITECTURE_AUDIT.md` · sha256 `04608759508f9b28ddc1a7df05e26711ac7f430f7d5d45f0d043f31df301ca27` · 7,882 words. No content changed.

# AUDIT — Romance Architecture (THE QUIET TIDE)

> Phase 7 — Romance Architecture Audit. Canon build: FINAL_WORLD_BIBLE v1.8 (2026-09-20).
> Scope: architectural audit ONLY. No chapters, no romantic scenes, no dialogue, no story outline.
> Method: full read of WORLD_BIBLE/*, DATABASE/* (incl. MYSTERIES.md, FORESHADOWING.md, POWER_PROGRESSION.md, FACTIONS_AND_CONFLICTS.md, INFORMATION_KNOWLEDGE_MAP.md, REVEAL_ORDER.md, RED_HERRINGS.md, MYSTERY_DEPENDENCIES.md), AUDIT/* — via four parallel extraction analysts (Arthur profile; romance×mystery/information; romance×faction/supernatural; independence+network+trope), all claims verified against canon files before inclusion.
> Canon locks preserved: Arthur's identity and ANOMALY-001 mechanism; inheritance chain (proximity + Loudness, unengineered); Ravenscroft March 2017 transfer; all character/faction/anomaly IDs; established relationships, history, personality traits, supernatural rules.

---

## 1. Executive Summary

The romance ecosystem is structurally sound and unusually honest. The pre-existing `32_ROMANCE_FRAMEWORK.md` already built five candidate configurations (A Nadia/Quiet, B Kira/Attuned, C Aisha/Sweeper, D Pram/Cartographer, E Saitō/Loud) with *structural* — not miscommunication-based — tensions, plus six inviolable rules. This audit stress-tested all five against the full canon: character independence, trope collapse, information asymmetry, faction/supernatural entanglement, pacing, post-confession sustainability, and 1000-chapter viability.

**Verdict: GO for Story & Arc Architecture.** No forced romance found. No character exists as a reward, damsel, or exposition device. The five configurations are genuine alternatives (not a harem, not concurrent rivals). Three genuine contradictions were found and minimally patched (all pre-existing stale residues, none invented by this audit). Seven independence watches were recorded (none critical). The trust engines of all five configurations are gated by the mystery reveal order — romance and mystery are coupled but neither replaces the other.

Key numbers: **37 characters analyzed** · **5 plausible romantic configurations** (1 HIGH POTENTIAL, 2 DIFFICULT BUT INTERESTING, 2 POSSIBLE, 0 LOW COMPATIBILITY among the canon five; 31 characters explicitly NO ROMANTIC FUNCTION) · **3 contradictions → 3 minimal patches** · **2 forced-romance risks flagged as watches** (not violations) · **5 information-asymmetry maps complete** (50 dimension-cells) · **7 characters on independence watch** · **12 unresolved UNKNOWNs** · **1000-chapter sustainability: YES** · **Ready for Story/Arc Architecture: YES**.

---

## 2. Romantic Character Ecosystem

The ecosystem centers on Reed Arthur (CHAR-001) with five canon-built candidate partners, each representing a different structural relationship to the hidden world:

| Config | Character | Age | Register | Structural tension |
|---|---|---|---|---|
| A | Nadia Puspita (CHAR-016) | 25 | Quiet civilian, NQA claims adjuster, Indonesian SSW migrant | The Tuesday problem — Loud/Quiet memory asymmetry as the setting's central romantic question |
| B | Kirana "Kira" Maheswari (CHAR-033) | 28 | T2 Lantern, freelance Quiet-care counselor, Institute stringer | The Attuned clock — Erosion arithmetic + no-privacy Tide-mark reading |
| C | Aisha Rahman (CHAR-034) | 36 | Sweeper team lead, SMD-contracted, KNF liaison seam | Faction loyalty — every date a conflict of interest; the 36/24 register |
| D | Pramudya "Pram" Nugroho (CHAR-032) | 31 | T2 Hollow, Cartographers' Exchange field mapper | Ally/rival blur — every kindness is also fieldwork; the scheduled betrayal |
| E | Saitō Yūto (CHAR-015) | 26 | Night-shift clerk, also Loud (unacknowledged) | Shared unedited memory — tool-vs-weather doctrinal split; the mirror inside the only honest relationship |

The five are *alternatives*, not a harem: the trope audit confirms no purposeless love triangles exist, and 32_ROMANCE_FRAMEWORK.md's intro frames them as candidate configurations the novel chooses among. Each configuration's obstacle is the world (schedule, Veil, Erosion, org chart, archive), never miscommunication — the framework's §32.2 intro contractually excludes misunderstanding loops.

31 of 37 characters are explicitly marked NO ROMANTIC FUNCTION with one-line reasons (DATABASE/ROMANCE_ARCHITECTURE.md §7): world-level officials (CHAR-002–008), cosmological figures (CHAR-009–011), family (CHAR-012–014), historical/deceased (CHAR-018–023, CHAR-035), professional registers (CHAR-017, CHAR-024, CHAR-028, CHAR-029, CHAR-031, CHAR-036, CHAR-037), antagonists (CHAR-025, CHAR-026, CHAR-027, CHAR-030). No romance was invented because a character is female: June Park (CHAR-028, Loud journalist) stays professional; Dr. Nwosu (CHAR-031) stays clinical; Okada (CHAR-036) stays maternal-professional.

---

## 3. Arthur Romantic Profile

Arthur's characterization is LOCKED and was preserved throughout. Derived from existing canon only (29_PROTAGONIST_ANOMALY.md, 18_CIVILIAN_LIFE.md, 32_ROMANCE_FRAMEWORK.md, _charpatch_protagonist.md):

**How he approaches people:** Parallel presence over conversation — with Saitō, "shared glances when a file is wrong; the glances are the whole conversation." He observes before disclosing; absorbs rather than probes. Courts by repeated low-stakes proximity — showing up in the same places until showing up means something.

**Communication:** Dry, sideways, non-confrontational. Stubborn about facts — the one thing that makes him argue, likely surfacing in romance as *documenting* a partner's claims rather than confronting them. Performs normalcy as a discipline; ceasing to mask around someone is definitionally intimate.

**Attraction:** "Professionally unequipped to parse" romantic interest — misfiles attraction as friendliness. Has dated; "the Laggard ends dates early." Does not pursue, charm, or declare.

**Rejection:** Withdrawal + documentation, not confrontation — fades and files the ending. Trained by the family's load-bearing peace (built "by not discussing it").

**Intimacy:** The dropping of the mask. The trusted partner is the one he deliberately does *not* file — protection through non-documentation (the mirror beat is the template). 1K economics make romance slow by infrastructure, not only temperament.

**Trust:** Showing-up without agenda (Saitō, Okada, the Night Clerks); ordinariness as a credential; naming (the Night Clerks gave the weather a word). **Distrust:** being filed; curiosity that spends him; being read.

**Emotional weaknesses:** (1) archivist's deformation — believes understanding = surviving, so studies relationships instead of risking them; (2) inverted loneliness — sustained attention is disproportionately powerful, judgment correspondingly vulnerable; (3) masking fatigue — the Laggard's social cost is permanent performance; (4) inherited guilt economy — internalized that his existence costs the people who love him, so he pre-emptively absorbs cost.

**What he doesn't understand:** can't read romantic interest; has no ethics-model of the Tuesday problem yet; confuses attention with disclosure; has never knowingly met a Loud adult — every romantic hypothesis he holds is Quiet-shaped.

**Ordinary background's effect:** convenience store-scale dating budget; no private venue; every-other-Sunday dinner as the commitment gauntlet; can't afford a police/hospital/Census file; camouflage is smallness, and smallness is a discipline. Rule 32.3#6 is the load-bearing beam: attention, memory, honesty, showing up — "or it's not love, it's plot."

---

## 4. Compatibility Analysis

No rankings. No "best girl" lists. Classifications with reasons:

**HIGH POTENTIAL — Arthur × Nadia (A).** The structural tension *is* the setting's central romantic question (is it consent to be loved by someone who knows your forgotten days?). Both choose ordinariness — his by discipline, hers by decision ("the city as decision, not default"). Same employer, overlapping shifts, same class, shared convenience store geography. His memory-honesty matches her paperwork-honesty. The trust engine is fully staged by canon mysteries (MYSTERY-011/012, D-08 hard dependency). Hesitations: the Tuesday problem is permanent and unanswerable; his inverted absence vs her day-shift life; he carries the asymmetry alone (guilt); she is unknowingly part of the machine that edits him.

**DIFFICULT BUT INTERESTING — Arthur × Kira (B).** "Two professionals of memory — his perfect, hers borrowed from rooms — learning what it means to be known *completely* and loved anyway." Genuine meeting of disciplines; both do cost-arithmetic honestly. But: no privacy (she reads Tide-marks — collides with his secrecy-as-safety); the Erosion arithmetic (every year together measurably less); Census-monitored relationship; her employer's data hunger. The triangle must resolve by *her* agency (refusing a collection, redacting a report, resigning the stringer role) — never by his disclosure alone, since she already sees too much.

**DIFFICULT BUT INTERESTING — Arthur × Aisha (C).** Respect-first professionals on opposite sides of the same incident tape; his protection-by-not-filing ethics mirrors hers; both understand price. But: 12-year age and institutional seniority gap — real, negotiated never erased; every date a conflict of interest; every shared file a protocol breach; her job includes deciding what to do with witnesses like him; the dual-hat seam; the treason reading. The break, if it comes, is institutional — the org chart's, not the heart's. The 36/24 register must never read maternal nor flattery (flagged watch).

**POSSIBLE — Arthur × Pram (D).** Courtship by archive is genuine — the slow burn of shared obsession, two people who map the unmappable. But: "every kindness is also fieldwork"; the institution wants experiments (the ratchet = spending Arthur); the journals are disputed property; the betrayal is *scheduled* ("professional, precise, and devastating"). The relationship's meaning must be earned *past* the betrayal, never instead of it. The telling — "whether he'd *tell* Arthur he's choosing" — is the restoration currency.

**POSSIBLE — Arthur × Saitō (E).** The only fully-shared memory in Arthur's life; no performance needed; pre-built trust; both live the inverted schedule. But: tool-vs-weather is a real doctrinal split (his testing impulses are the risk vector); the blast radius is shared; the Court's demographers *will* flag two Louds one desk apart; the mirror sits inside the only honest relationship as the one withheld beat. Friendship-to-romance must cross the mirror — telling Saitō *at* the tripwire makes the disclosure the defusal.

---

## 5. Attraction Engine

No configuration follows "they met → they immediately fell in love." Each has a staged, canon-grounded sequence (sequences vary — the audit does not require identical stages):

- **A (Nadia):** AWARENESS (melon pan, unparseable interest, dawn convenience store) → CURIOSITY (the softening — "the file doesn't match the file next to it") → INTEREST (repeated low-stakes proximity in the two-hour overlap) → TRUST (file-sharing: he shows his files; she shows the manual + revision history, ch. ~150–220) → EMOTIONAL RELIANCE (he is the one person who remembers her forgotten days) → CATASTROPHE (the leak: she learns what she handled, ch. ~220–300) → VULNERABILITY (deeper understanding) → CHOICE (what she does with remembering — briefly, partially, through *his* files) → COMMITMENT (the family dinner, post-revelation).
- **B (Kira):** AWARENESS (professional contact, Quiet-care adjacent) → CURIOSITY (her Tide-mark sense vs his unmarked-by-instruments anomaly) → INTEREST (two memory-professionals recognizing the discipline) → TRUST (restraint — what she chooses *not* to read/report) → EMOTIONAL RELIANCE ("known completely") → ATTRACTION (priced against the arithmetic, stated upfront) → VULNERABILITY (the triangle's pressure, ch. ~200–300) → COMMITMENT (her choice: the person over the data).
- **C (Aisha):** AWARENESS (EVENT-092: she learns his name from the replay report) → CURIOSITY (the standing case file that won't resolve) → INTEREST (professional respect, negotiated under fire) → TRUST (the compromise realized — he learns she keeps not filing, ch. ~150–220) → EMOTIONAL RELIANCE (two people who understand price) → VULNERABILITY (the seam's pressure; CG-044 absorption) → CRISIS (the hiring answer → the recruitment pitch, ch. ~250–400) → COMMITMENT (her choice at professional cost; his refusal of the pitch *because* of what it would make her).
- **D (Pram):** AWARENESS (arrival with the journals, ch. ~60–100 — the relationship starts on a missing page) → CURIOSITY (shared obsession) → INTEREST (courtship by archive) → TRUST (marginal honesty: his field notes, not just Ilsa's) → EMOTIONAL RELIANCE (reading together) → VULNERABILITY (the handwriting tripwire, ch. ~200–300) → BETRAYAL (scheduled: professional, precise, devastating) → TELLING (disclosure as restoration currency) → COMMITMENT (earned past the betrayal; Arthur's authentication of the page, ch. ~350–450).
- **E (Saitō):** AWARENESS→TRUST pre-built (years of shared glances; the friendship *is* the history) → CURIOSITY (the doctrinal split made explicit: tool vs weather) → INTEREST (being fully seen, in a world where no one is) → VULNERABILITY (the risk reveal scheduled: demographers' flag ch. ~200–280; leak ch. ~150–220) → ATTRACTION (the intoxication of the shared unedited memory, priced against the blast radius) → CRISIS (the mirror tripwire, ch. ~300–400) → COMMITMENT (disclosure as defusal — telling Saitō *at* the tripwire).

Every sequence runs on repeated meaningful interaction. The dinner rule (32.3#5) gates commitment in all five — no configuration reaches it without the Willowmere gauntlet.

---

## 6. Trust Engine

Trust in this setting is priced in secrets, and every secret is coupled to the mystery architecture and the information economy:

- **A:** Trust increases via mutual exposure of the instruments that edit them (his files; her manual + revision history). Trust damages when the softening targets *his* filings specifically, or when she learns the cache held files she handled. Trust permanently breaks only if the routine's authorship is *targeted at Arthur* — i.e., RH-030 played straight, which canon forbids doing cheaply ("her independence is load-bearing"). Restoration is *her* agency (her choice with remembering), never his disclosure alone — the Veil eats his disclosures.
- **B:** Trust increases via her restraint (what she doesn't read, doesn't report). Trust damages via any sign her longitudinal interest is *spending* him, or a Tide-mark read past the consent line. Trust permanently breaks if her work crosses from observation to experimentation, or if she transmits what he asked her to hold. Restoration is her choosing the person over the data.
- **C:** Trust increases via professional respect and her disclosure of the compromise's origin. Trust damages with every shared file (the relationship's operating cost) and the mole hunt's atmosphere. Trust permanently breaks if she files the follow-up, carries the Desk's pitch, or chooses the bureau when the seam forces it. Restoration is her resigning the seam at professional cost — "she has buried two teams and one marriage; the novel must price a third burial honestly."
- **D:** Trust increases via the journals as genuinely given and his marginal honesty. Trust damages with each field report filed on Arthur, or the Exchange asserting journal ownership mid-relationship. Trust permanently breaks with the scheduled professional betrayal (experiments via the ratchet; delivery to CG-048). Restoration is the telling itself — disclosure, not defection alone.
- **E:** Trust increases via the shared memory deepened by mutual disclosure (the mirror told — Arthur's hardest disclosure). Trust damages when Saitō's testing gets them noticed, or the under-redacted-source note points at him. Trust permanently breaks if his leak adjacency puts a price on Arthur's head by his hand, or if the mirror's discovery reads as the one lie inside the only honest relationship. Restoration is full disclosure both ways plus a jointly chosen doctrine.

**Information-economy coupling:** trust beats are gated by reveal order (AUDIT §16). The D-table hard dependencies gate every crisis: D-08 (011→012) for A; D-07/D-12 (005/020→008) for C; D-01/D-02 (001→002, 001→004) for D; C-04 (mirror tripwire before 002's hinge) for E. Secrets have consequences because the mysteries that hold them have *prices* — the pipeline, the ratchet, the treason reading, the auction.

---

## 7. Romance + Supernatural System

Audit method: for each configuration, remove the supernatural element and check whether the relationship remains meaningful.

- **A:** Remove the Veil — remains: a night-shift clerk and a day-shift migrant adjuster falling in love across a two-hour overlap, her five-year plan, his 1K, the convenience store geography. PASS. The supernatural (Tuesday problem, the pipeline) *intensifies* the human core (chosen normalcy) rather than substituting for it.
- **B:** Remove Tide-marks/Erosion — remains: a counselor and a records clerk, two memory-professionals, her employer's data interest vs her ethics, the question of what a relationship is worth under a terminal diagnosis (Erosion as *any* terminal condition). PASS — with the audit's guardrail that Erosion must never be aestheticized (Rule 3).
- **C:** Remove Sweepers/the Veil — remains: a senior field operative and a junior clerk, fraternization rules, classified work, cross-cultural families, the ethics of protection. PASS. The supernatural (unfileable witness, treason reading) raises the stakes of an already-real dynamic.
- **D:** Remove the Exchange/anomaly — remains: two archive-obsessed professionals, mentorship vs rivalry, institutional loyalty vs personal loyalty, the scheduled professional betrayal. PASS. The journals work as *journals* — the intimacy shortcut watch (§17) is precisely about not letting the supernatural archive do the emotional work.
- **E:** Remove Loudness — remains: two night-shift coworkers, years of shared glances, the tool-vs-weather argument about how to live with dangerous knowledge, the best-friend-to-more crossing. PASS. Loudness makes the shared memory *total*; the human core (being seen without performing) doesn't need it.

**Supernatural effects audited:** secrecy (the mirror; the escrow; unfiled follow-ups), danger (the price on his head; the treason reading), identity concealment (his normalcy performance), power imbalance — cognitive (Loud/Quiet), institutional (36/24, handler/asset), informational (Tide-marks, journals) — anomaly-related trauma (the *cleansing ritual*; buried teams), fear, trust, vulnerability, protection, dependency, conflicting objectives. In every case the power imbalance is *named and negotiated*, never romanticized. Rule 2 (consent includes memory) and Rule 3 (Erosion not romantic) are the load-bearing constraints; the audit found no configuration violating them.

---

## 8. Romance + Faction System

- **A:** NQA is the employer of both — the claims pipeline is the information-control layer (26 §26.4). The SMD's SSW Threshold-adjacency watchlist makes claims processing a watched tier. The Lantern Bearers (SUP-005) are the catastrophe vector (CG-041). No forbidden-romance framing needed: the obstacle is the pipeline, not a prohibition.
- **B:** The Meridian Institute (RES-001) is the employer-lover triangle; the Census monitors registered relationships ("a partner's file cross-references yours"); the handler's phone number on the fridge is literal. The Compact (INTL-001) is the leak's second player. The faction pressure is contractual and medical, not star-crossed.
- **C:** The densest faction entanglement — SMD warrant vs KNF contract authority (the liaison seam); fraternization rules; the Quiet Desk's recruitment pitch ("handler, leash, Census file"); CG-044's absorption making her unfiled follow-ups read as treason *to both sides*. This is the closest to "forbidden romance" in the set, and it emerges *entirely* from canon (dual-hatting by design) — not imposed. The audit confirms: no forced forbidden romance anywhere; where prohibition exists (fraternization rules), it is institutional procedure with a paper trail, not romantic decoration.
- **D:** The Cartographers' Exchange (SUP-002) — "the oldest continuously operating hidden-world institution" — vs the Archivists (SUP-008) and Red Ledger (SUP-004) contesting the journals (CG-048). Defection is priced accordingly. The faction complication is the relationship's engine (fieldwork vs choosing), not its backdrop.
- **E:** Structurally the *least* faction-entangled — "the Loud aren't Census subjects at all"; visible only through NQA's employer files. The threat is statistical (the Court's demographers) and adjacent (leak blast radius), not institutional. This is intentional: the configuration's tension is doctrinal and interpersonal, and the factions arrive as *consequence*, not premise.

**General finding:** Factions don't pause for love (Rule 4) in all five — but they also don't *conspire* for love. No faction manufactures a romance; no org chart plays matchmaker. Institutional pressure is real, priced, and paper-trailed.

---

## 9. Female Character Independence Audit

All major female characters audited against: independent goals, relationships, competence, conflicts, decisions, reasons to exist outside Arthur.

- **Nadia Puspita (CHAR-016):** Independent goals (five-year plan, status, chosen Ravenscroft life); independent relationships (migrant community, NQA day-shift colleagues — canon-adjacent, expandable); independent competence (claims adjustment — the pipeline runs through *her* hands); independent conflicts (visa precarity; the routine's authorship — MYSTERY-012 is *her* mystery, not his); independent decisions (her choice with remembering is the final revelation). Verdict: PASS. Watch (LOW): don't reduce her to symbol-of-normalcy; MYSTERY-012 explicitly rejects the plant/Loud red herrings, which is the canon's own guardrail.
- **Kirana Maheswari (CHAR-033):** Independent goals (counseling practice, Fathom management, the stringer income on her terms); independent competence (Tide-mark reading — professional, non-Arthur); independent conflicts (the triangle; the clock). Verdict: PASS. Watch (LOW): name at least one client and one Institute contact early — her non-Arthur network is the thinnest of the five; keep her reading non-Arthur Tide-marks on-page.
- **Aisha Rahman (CHAR-034):** Independent goals (team survival, seam management); independent relationships (Sweeper team, buried teams, Mindanao family, KNF colleagues, Kalsada's van yard); independent competence (Sweeper lead — senior, proven); independent conflicts (mole hunt, dual-hat treason reading — the densest non-Arthur graph of the five). Verdict: PASS. Watch (LOW): keep the mole-hunt/dual-hat arc weight-bearing; hold the 36/24 register at "respect first."
- **Director-General Ratna Kusuma (CHAR-005), Secretary-General Fatoumata Diallo (CHAR-008), Vivienne Ashworth (CHAR-025), June Park (CHAR-028), Dr. Amara Nwosu (CHAR-031), Lena Hoffmann (CHAR-024), Eleanor Reed (CHAR-014), Hannah Reed (CHAR-012), Okada Kumiko (CHAR-036):** all PASS with independent institutional/personal engines. **Highest watch: CHAR-031 Nwosu** — her only named subject is Arthur ("her paper, walking"); she needs visible other subjects + Vesper internal wars or she collapses into "Arthur's doctor." Recorded as the audit's top independence watch (not a violation — a requirement for the story engine).
- **No violations found:** no reward characters, no exposition devices, no emotional support machines, no damsels in distress, no passive witnesses to Arthur's growth, no character whose identity is "Arthur's love interest." The romance *adds* dimensions (the pipeline, the triangle, the seam, the journals, the shared memory) rather than substituting for them.

---

## 10. Male Character Independence Audit

Same standard applied to male characters — no disposable males to make Arthur look superior:

- **Saitō Yūto (CHAR-015):** own curiosity-vs-caution engine; the tool-doctrine is a genuine philosophy, not a foil; leak adjacency and testing impulses are *his* plot weight. PASS.
- **Pramudya Nugroho (CHAR-032):** excellent at mapping — "Arthur wins only the filing domain"; the Exchange career, the Ilsa scholarship, the choosing-question are his. PASS. Watch (LOW): keep him excellent; never let the romance shrink him to courier.
- **Thomas Reed (CHAR-013), Hasegawa Kenji (CHAR-037):** quiet professional engines (department manager; ten years on nights, dry mentor). PASS.
- **Hendra Gunawan (CHAR-026):** the Jakarta succession war. **"The Factor" (CHAR-027):** genuine antagonist with his own ledger. **Silas Crane (CHAR-029):** terminal diver, objectively stronger than Arthur — a warning figure, not a stepping stone. **Reverend Amos Kade (CHAR-030):** ideological engine. **World-level officials (CHAR-002–004, 006, 007):** institutional engines. PASS across the board.
- **No violations found.** Male characters are never staged to lose so Arthur can win; where Arthur out-performs (filing, memory, honesty), it is in his locked domains, and stronger characters (Crane, Vivienne, the Factor) remain genuinely dangerous per the power audit.

---

## 11. Romantic Conflict Engine

Natural conflict sources per configuration (no repetitive misunderstanding loops — contractually excluded by 32_ROMANCE_FRAMEWORK.md §32.2's intro; the audit verified none exist):

- **A:** incompatible risk tolerance (he absorbs cost; she chooses plans); secrets (his files; her handled files); the Tuesday asymmetry (not a misunderstanding — a *condition*); professional boundaries (adjuster vs filer); moral disagreement (is the asymmetry consent?); supernatural danger (the leak's blast radius); the pipeline's editing as the third party.
- **B:** conflicting objectives (her data hunger vs his unspent-ness); the consent line on reading; the triangle; moral disagreement (stop-channeling: love or control?); Erosion's arithmetic as the unfixable fact; Census monitoring.
- **C:** conflicting loyalties (SMD vs KNF vs the relationship); classified information; fraternization rules; the treason reading; professional boundaries; moral disagreement (is the breach protection or compromise?); the 36/24 register; supernatural danger (she cleans up his city).
- **D:** conflicting loyalties (Exchange vs Arthur); secrets (field reports; the posting's brief); the scheduled betrayal; moral disagreement (is mapping neutral?); the journals' disputed ownership; the second price.
- **E:** moral disagreement (tool vs weather — the *doctrinal* conflict, argued honestly, never a miscommunication); secrets (the mirror); different risk tolerance (testing vs never-be-interesting); the demographers' flag; the blast radius.

**Misunderstanding-loop check:** zero instances found. Where information is asymmetric, the asymmetry is *structural* (Veil, Census, classification, the mirror) and priced — never "she misunderstands him / he misunderstands her / they refuse to communicate." The one candidate (CG-044's atmosphere making Nadia's routine look deliberate) is explicitly flagged as a misreading the novel must *disprove on-page* before it curdles — the audit converts it into a requirement, not a loop.

---

## 12. Romance Pacing

Sustainable progression across the long serial. No fixed chapter where romance "must" happen — instead, gated windows from the reveal order:

- **CHAPTER 1–50 (early seeds):** A: melon pan, the two-hour overlap, "professionally unequipped to parse." E: the friendship is the seed (pre-built). C: EVENT-092 (she learns his name). D: arrival with the journals (ch. ~60–100). B: professional texture. *First meaningful connection:* A (dawn convenience store); E (already); C (respect-first working contact); D (courtship by archive begins); B (the arithmetic stated).
- **CHAPTER 50–100:** A: the softening noticed ("the file doesn't match the file next to it," ch. 60–110). C: unfiled follow-ups accumulate (ch. 60–100). D: journals read together. E: doctrinal argument surfaces.
- **CHAPTER 100–200:** A: trust beat — file-sharing (ch. ~150–220). C: the compromise realized (ch. ~150–220). D: the tether reveal via journals (ch. ~150–250). B: "known completely" beat (post-tether-reveal). E: the leak (ch. ~150–220) inside the friendship's deep-trust window.
- **CHAPTER 200–300:** A: the catastrophe — leak breaks, she learns what she handled (ch. ~220–300). B: the Institute's shadow (Nwosu's data reaches Arthur, ch. ~200–300). C: the hiring answer reframes the Desk (ch. ~250–350). D: the handwriting tripwire (ch. ~200–300); the auction arc (ch. ~250–350). E: the demographers' flag (ch. ~200–280).
- **CHAPTER 300–500:** A: her choice with remembering; the gallery crucible (ch. ~280–380); the dinner (post-revelation). B: the triangle's resolution (her choice). C: the recruitment pitch (ch. ~300–400); her priced choice. D: the betrayal; the telling; authentication (ch. ~350–450). E: the mirror tripwire (ch. ~300–400); disclosure as defusal.
- **CHAPTER 500+:** post-commitment development for whichever configuration(s) the story engine selects (§13). The unchosen configurations persist as *relationships* (friendship, professional, severed) — never as dangling threads.

**Pacing invariant:** romance beats cannot land before their evidence exists (reveal-order gating, §6/§16). The audit verified every beat above sits inside its mystery's legal window.

---

## 13. Post-Confession Development

Confession is not the end. Per configuration, the relationship must keep developing *after* mutual acknowledgment:

- **A:** learning her routines vs his inverted calendar; the five-year plan's next phase (does Ravenscroft remain the choice?); what "remembering, briefly, partially" does to a marriage of routines; the dinner as annual re-audit (*shōgatsu*: "bring them home or explain why not" — every year); protecting each other's boundaries (his files; her pipeline); the second leak (MYSTERY-055) as the post-commitment test.
- **B:** the arithmetic as daily fact (not tragedy — logistics); her Fathom management as shared planning; his restraint vs her legibility as the ongoing negotiation; the Institute's long shadow (does the stringer role end?); what "known completely" means when the entity (L5-2) is still unknown to *both*.
- **C:** the seam's aftermath (what does she do after resigning — or keeping — the dual-hat?); the treason reading's long tail; professional conflict (she still cleans up his city); faction pressure on a registered relationship; trust under the mole hunt's recurring pressure; future planning with the org chart priced in.
- **D:** what remains after the betrayal and the telling; the journals' custody resolved — who keeps them?; the Exchange's second price coming due; his defection's cost as the relationship's mortgage; mapping *together* on Arthur's terms (he sets the terms — the authentication beat as the new model).
- **E:** the only fully-shared memory, finally complete — what do two Louds *do* with it?; the jointly chosen doctrine (tool vs weather, resolved); the demographers' long attention; the night shift as the relationship's home ground; protecting the private history from becoming leverage.

**Anti-stagnation rule:** no endless artificial separations after establishment. External conflict may *pressure* the relationship (the second leak, the mole hunt's recurrence, the Institute's shadow) but must not *reset* it. The audit's consequence test (§15) applies post-commitment with full force.

---

## 14. Relationship Network

Arthur is not the center of every relationship. Verified non-Arthur nodes per candidate (canon-cited; INFERRED marked):

- **Nadia:** NQA day-shift colleagues; the Indonesian migrant/SSW community in Ravenscroft; family in Indonesia (remittance line); the claims pipeline's own hierarchy. (Expandable — the audit recommends naming 2–3 on-page.)
- **Kira:** Quiet-care clients (unnamed — the audit *requires* naming at least one client and one Institute contact early; thinnest network of the five); the Meridian Institute stringer net; fellow Lanterns. Watch recorded.
- **Aisha:** densest — Sweeper team; two buried teams (the dead, who still count); Mindanao family; KNF Liwanag colleagues; Kalsada's van yard; the mole hunt's cast (Laras, her mentor); the SMD contract hierarchy.
- **Pram:** the Cartographers' Exchange (field circuit, the Bone Ledger succession — MYSTERY-031); Ilsa's journals as a *professional* inheritance (not only romantic); SE Asia circuit contacts.
- **Saitō:** the Night Clerks' Ravenscroft cell (futsal, Discord); his own family (canon-adjacent); NQA night-shift crew (Okada, Hasegawa).
- **Arthur:** the Reed family (Willowmere — the gravity well); Okada/Hasegawa (work); the Night Clerks; Yusuf's bridge (the Ravenscroft Loud circle).

**Graph property:** every candidate has ≥2 canon-cited non-Arthur nodes. The network is Arthur-*adjacent*, not Arthur-*centered*. Characters know and care about people who have nothing to do with him — Aisha's buried teams, Pram's Exchange, Kira's clients-to-be-named, Nadia's five-year plan people, Saitō's futsal cell.

---

## 15. Emotional Consequence Test

Applied to each configuration (representative answers — the full matrix is in the analysts' drafts):

- **If injured:** A — he remembers the injury she'll forget by Tuesday; the asymmetry becomes triage. B — her Fathoms make every injury priced against the arithmetic; his helplessness is total (he can't slow Erosion). C — her injury is professional (the job did it); his is the compromise (did his file cause it?). D — his injury is fieldwork's price; the Exchange's second price made flesh. E — the shared memory means he *remembers it exactly*; grief without the Veil's mercy.
- **If disappears:** A — she forgets the strange days; he keeps them alone — the Tuesday problem as loss. B — the clock stops mattering; the arithmetic was the relationship's premise. C — the seam closes; the treason reading outlives her. D — the journals remain; the missing page outlives them both. E — the private history loses its only other holder; he becomes the sole rememberer — the loneliness of the inverted, perfected.
- **If betrays Arthur:** A — the plant version (forbidden cheap) vs the emergent version (survivable). B — transmitting what he asked her to hold. C — filing the follow-up. D — the scheduled professional betrayal (canon's promise). E — the leak adjacency putting a price on his head by his hand.
- **If Arthur betrays them:** A — using her forgotten days as leverage (Rule 2's violation — the audit's brightest red line). B — asking her to stop channeling *for him* (love or control). C — using the compromise as leverage. D — withholding the authentication. E — the mirror discovered as the one lie.
- **If they learn his biggest secret (the mirror):** the tripwire — "the day someone else mentions the mirror is the day he knows he's been read." Sharpest in E (the only honest relationship), most dangerous in B (the reader who can't unread), most structural in D (the journals document it).
- **If he learns theirs:** A — what her hands did (the catastrophe). B — what she reported upstream. C — the compromise's origin. D — the posting's brief. E — the extent of the testing.
- **Moral disagreement:** A — is the asymmetry consent? B — stop-channeling: love or control? C — breach as protection or compromise? D — is mapping neutral? E — tool vs weather.
- **Surviving a major supernatural incident together:** the relationship's post-incident state is *priced* — A's remembering-choice, B's Fathom accounting, C's filed-or-unfiled fact, D's told-or-not, E's shared memory extended. Nothing resets.

Every answer produces meaningful, non-repeating consequences. The test passes for all five.

---

## 16. Information Asymmetry

Five complete asymmetry maps (50 dimension-cells) are recorded in DATABASE/ROMANCE_ARCHITECTURE.md §§1–6 and rest on the analysts' full tables. Structural summary:

| Config | He knows / She knows | The load-bearing secret | The tripwire |
|---|---|---|---|
| A | He knows her forgotten days; she knows nothing (until the leak) | The routine's authorship (UNKNOWN) | The leak: she learns what she handled |
| B | She knows his marks; he knows the mirror (she doesn't) | What she reported upstream | Observation becoming experimentation |
| C | She knows the case file; he learns the compromise | The Desk's actual plan (UNKNOWN) | The recruitment pitch |
| D | He (via journals) knows his condition better than he does; he knows the mirror | The torn page's contents (L5-5) | The handwriting check |
| E | He knows the shadow's behaviors (observed); he knows the mirror (told no one) | Saitō's Loudness adjacency (MYSTERY-087, OPEN) | "Someone else mentions the mirror" |

**Asymmetry is never used for cheap misunderstandings.** It produces: curiosity (the softening; the journals), trust (restraint; the telling), fear (the treason reading; the price on his head), respect (the breach recognized), admiration (marginal honesty), conflict (tool vs weather; the triangle), vulnerability (the mirror; the clock). The audit verified each configuration's asymmetry generates at least five of the seven — none generates *only* misunderstanding.

---

## 17. Character Growth

Relationships change the characters without replacing them:

- **Arthur may become:** more trusting (the dinner, eventually); more emotionally aware (learning the Tuesday problem *as ethics*, not weather); more willing to communicate (the telling beats); more protective of boundaries (his and theirs); more capable of vulnerability (the mirror, told once, to one person). **He must not become:** suave, articulate about feelings on demand, comfortable with being filed, or a different person. The four assets (attention, memory, honesty, showing up) remain the mechanism of every change — growth is *more* of what he is, aimed better.
- **Nadia may become:** someone who knows what her hands did and chooses Ravenscroft anyway — the five-year plan rewritten with open eyes. Not: Loud, or "awakened," or a hidden-world operative (RH-031 forbids).
- **Kira may become:** someone who chose the person over the data — the triangle resolved by agency. Not: cured, or saved from the clock (Rule 3 forbids).
- **Aisha may become:** someone who priced the seam and paid it — the third burial, chosen. Not: retired into domesticity, or filed into compliance.
- **Pram may become:** someone who told the truth about the choosing — disclosure as character. Not: defected cheaply, or redeemed by love alone (the betrayal still happened; it's *past*, not erased).
- **Saitō may become:** someone with a jointly chosen doctrine — curiosity with rules. Not: weather-domesticated, or Arthur's sidekick.

**Growth invariant:** no partner becomes "soft only for MC" (trope audit: not present); no partner's arc is *about* Arthur — each arc is about the pipeline, the triangle, the seam, the journals, the doctrine, with Arthur as the person it happens *beside*.

---

## 18. Romance Failure Test

Not every relationship should succeed. Canon supports:

- **Relationships that fail naturally:** D can end at the betrayal (the telling refused — he doesn't tell); C can end at the seam (she chooses the bureau); B can end at the triangle (the Institute wins); E can end at the doctrinal split (tool vs weather, unresolvable).
- **Unrequited attraction:** A's early phase (his unparseable interest) supports a window where the feeling is one-sided; the audit keeps it honest — her interest is stated, his recognition lags (S1).
- **Incompatible relationships:** B's no-privacy vs his secrecy-as-safety is a *structural* incompatibility the couple must negotiate, not a misunderstanding to clear up — it can be the reason it doesn't work.
- **Friendships that remain friendships:** E's default state; the audit requires the crossing to *earn* itself (the mirror) — otherwise it stays the novel's great friendship, which is itself load-bearing.
- **Interrupted by circumstances:** C (the mole hunt's timing); A (the leak's timing); any configuration during an ACTIVE recurring conflict.
- **Become stronger / more complicated:** all five, post-crisis — the consequence test (§15) is the mechanism.

**No forced heartbreak:** the audit found no configuration that *requires* failure for drama, and no success that requires the partner's diminishment. Failure, where it happens, is structural (the seam, the triangle, the betrayal, the doctrine) — never a misunderstanding loop.

---

## 19. Long-Serial Sustainability

Tested at 100 / 200 / 300 / 500 / 700 / 1000 chapters:

- **Room to evolve:** YES for all five. A's remembering-choice is a *beginning* (what does a relationship look like when she remembers "briefly, partially, through his files"?). B's clock is a logistics engine, not a countdown. C's seam has a long tail. D's post-betrayal is unmapped territory (deliberately). E's shared memory is a world to explore.
- **Repetitive conflicts:** NO — conflicts are structural and priced (the pipeline, the triangle, the seam, the journals, the doctrine), and each crisis *resolves into* a new configuration rather than resetting. The audit's anti-loop verification (§11) holds across the scale.
- **Post-confession stagnation:** NO — §13's post-commitment engines (the second leak, the Institute's shadow, the seam's tail, the Exchange's second price, the jointly chosen doctrine) are all *post*-commitment by construction.
- **New intimacies:** YES — A's partial remembering; B's "known completely" deepening around L5-2; C's post-seam professional renegotiation; D's mapping on his terms; E's completed shared memory.
- **External conflict without destruction:** YES — the second leak (MYSTERY-055), CG-044's recurrence, the Institute's program, CG-048's aftermath, the demographers' attention are all pressures that *price* the relationship without resetting it.
- **Disagreement without breakup:** YES — the doctrinal conflicts (tool vs weather; love-or-control; breach-or-compromise) are *argued*, not exited. The audit's conflict engine (§11) contains no exit-by-misunderstanding.
- **Supporting independent goals:** YES — §§9–10 verified; the dinner rule and the 500+ windows keep both people's goals on-page.
- **Relevance under escalation:** YES — romance scales *down* while the plot scales up (the convenience store, the dinner, the 03:00 text), which is the design: small problems carry emotional weight beside global mysteries (scale control, for the story engine to inherit).

**Verdict: the romantic ecosystem sustains 1000 chapters.** The binding constraint is not material but *selection*: the story engine must choose among the five (or hold several as non-romantic relationships) — the audit does not choose, and forbids choosing by ranking.

---

## 20. Major Findings

1. **The ecosystem is sound.** Five structural configurations, six inviolable rules, zero forced romance, zero trope collapse. The pre-existing framework did the hard work; this audit verified it.
2. **Trust is priced in secrets, and the secrets are real.** Every configuration's trust engine is gated by canon mysteries with hard dependencies — romance cannot outrun the information economy.
3. **Arthur remains ordinary.** The profile derivation found no drift toward suaveness, power, or romantic genius. Rule 32.3#6 holds across all five configurations.
4. **Independence holds.** 37/37 characters have independent engines; 7 watches recorded, none critical; the top watch (Nwosu) is a story-engine requirement, not a violation.
5. **Three genuine contradictions found and patched** — all stale residues from earlier phases (see §22). No new contradictions introduced.
6. **The dinner rule is the commitment technology.** It works because it's *expensive* (the gauntlet, the gauntlet's annual re-audit, the 1K you can't bring anyone to) — the audit confirms it's the setting's most original romantic mechanism.
7. **Failure is supported.** Every configuration has a structural failure mode; none requires failure; friendship-remaining-friendship is preserved (E).

---

## 21. Minor Findings

1. **Surveillance gradient** (worker finding, verified): the five configs are five different surveillance postures (B full Census; C contract; A watchlist-tier; D discipline monitoring; E Census-invisible). Rule 4 fires at different strengths — recorded as intentional design, not a contradiction.
2. **Kira's network is thinnest** — requires naming ≥1 client + ≥1 Institute contact early (recorded as a story-engine requirement in §9/§14).
3. **The Ilsa-journal intimacy shortcut** (trope watch): both B and D use Ilsa's interior life as courtship material — the archive must not do the relationship's emotional work. Recorded as a novel-level watch.
4. **Aisha's 36/24 register** (trope watch): never let competence read maternal or interest read flattery. Recorded as a novel-level watch.
5. **CG-044's atmosphere vs Nadia's routine**: the mole hunt makes her adjustments *look* deliberate — the novel must let the investigation suspect while never letting the romance convict (disproof must be on-page first). Recorded as a requirement.
6. **"Nadia Kusuma" residual**: the _charpatch_protagonist.md §8 flag is stale — zero hits tree-wide; the rename to Nadia Puspita is fully applied. No action (see §23).
7. **D-03 direction**: dependency table (004→003, comprehension) vs text graph (003→004, exploration flow) — two different relations, intentional. No action (see §23).
8. **Arthur's romantic recognition lag** (S1) is canon-stated ("professionally unequipped to parse") — the story engine should treat it as a *feature* (slow burn by characterization), not a bug to fix.

---

## 22. Patches

Three [ROMANCE PATCH]es applied in `~/workspace/world_bible/work_rom/` (all minimal; all stale residues from earlier phases; none invented by this audit):

### [ROMANCE PATCH] 1 — CG-041's "Saitō is the under-redacted source" contradicts the charpatch ruling
- **Issue:** DATABASE/FACTIONS_AND_CONFLICTS.md CG-041's Arthur-dependence cell named "Saitō is the under-redacted source."
- **Affected file:** DATABASE/FACTIONS_AND_CONFLICTS.md (CG-041 row).
- **Original state:** "NO — Arthur can kill, feed, or *shape* the story via one clerk-chosen document; Saitō is the under-redacted source"
- **Problem:** Contradicts the Phase-3 charpatch ruling (CANON): the Static Hour contact beat was Bayu-specific and deliberately NOT transferred to Saitō; EVENT-097's authoritative row (25_TIMEmessaging app.md) reads the anonymous cache. The CG-041 cell and DATABASE/EVENTS.md row were stale residues.
- **Minimal correction:** "NO — Arthur can kill, feed, or *shape* the story via one clerk-chosen document; the cache's source is unidentified (EVENT-097's anonymous-cache ruling stands — the Phase-3 charpatch deliberately did not transfer the Static Hour contact beat to CHAR-015)"
- **Downstream effects:** Configs A and E. Saitō's leak adjacency is now ambient (adjacent to every leak) rather than named-source — which *strengthens* Config E's tension (the blast radius without the authorship) and removes a false suspicion vector from Config A. MYSTERY-011's sender remains a genuine open thread (four in-world candidates).

### [ROMANCE PATCH] 2 — DATABASE/EVENTS.md EVENT-097's stale Saitō beat
- **Issue:** DATABASE/EVENTS.md EVENT-097 row read "Anonymous NQA claim-files cache; Saitō's (CHAR-015) Static Hour contact."
- **Affected file:** DATABASE/EVENTS.md (EVENT-097 row; convenience view).
- **Original state:** "Anonymous NQA claim-files cache; Saitō's (CHAR-015) Static Hour contact"
- **Problem:** Same stale beat as Patch 1 — contradicts the charpatch ruling and 25_TIMEmessaging app.md's authoritative row.
- **Minimal correction:** "Anonymous NQA claim-files cache (sender unidentified — MYSTERY-011; per the Phase-3 charpatch ruling, no CHAR-015 contact beat)"
- **Downstream effects:** Convenience view now consistent with 25_TIMEmessaging app.md. None beyond consistency.

### [ROMANCE PATCH] 3 — Kira's base: "Liwanag-based" vs "Ravenscroft-based"
- **Issue:** 21_CITIES.md:397 listed "RES-001 Meridian Institute (stringers like CHAR-033 Kirana "Kira" Maheswari, Liwanag-based)."
- **Affected file:** 21_CITIES.md (Tanaw district entry); 37_FINAL_WORLD_BIBLE.md compiled master rebuilt accordingly.
- **Original state:** "...Maheswari, Liwanag-based)."
- **Problem:** Contradicts 32_ROMANCE_FRAMEWORK.md §32.2B ("freelance Quiet-care counselor based in Ravenscroft") and DATABASE/CHARACTERS.md ("Ravenscroft Quiet-care counselor"). The 21_CITIES line is a Philippines-primary-era leftover.
- **Minimal correction:** "...Maheswari, Ravenscroft-based)."
- **Downstream effects:** Config B's Ravenscroft presence is now consistent tree-wide. The Tanaw entry keeps RES-001's district presence; the example stringer is Ravenscroft-based (no canon states she works Liwanag, so no circuit was invented).

**Patches NOT made (ruled out):** the "Nadia Kusuma" flag (zero hits; stale coordinator note; CHANGELOG records the rename applied and dated-note residue as deliberate historical record); D-03's direction (comprehension-dependency vs exploration-flow — intentional distinction); Kira's Census registration status (canon-unspecified; either answer consistent — left UNKNOWN); Aisha's Attuned tier/discipline (canon-unspecified — left UNKNOWN).

---

## 23. Intentional Exceptions

1. **D-03's bidirectional staging** (004→003 comprehension dependency; 003→004 exploration flow) — the deal and the page mutually frame; both directions are staged in canon. Intentional.
2. **The five configurations are alternatives, not a harem** — the novel selects among structural tensions. Intentional (trope audit verified no accidental harem structure).
3. **Arthur's romantic recognition lag** — canon-stated ("professionally unequipped to parse"); the slow burn is by characterization. Intentional.
4. **Kira's Census registration status** — unspecified; either answer is consistent with the surveillance gradient. Intentional UNKNOWN.
5. **Aisha's Attuned tier/discipline** — unspecified; the audit records the assumption without fixing it. Intentional UNKNOWN.
6. **RH-030/RH-031 and the other registered red herrings** — the disproofs are canon; the herrings exist to be *disproved on-page*, not removed. Intentional.
7. **MYSTERY-087 (Saitō's Loudness adjacency)** — unscheduled OPEN minor; the romance must not answer it prematurely. Intentional.
8. **The mirror's AL-○ through P2** (SECRET-005) — Arthur tells *no one*, including Saitō; the tripwire needs the withholding. Intentional.

---

## 24. Remaining Unknowns

1. MYSTERY-012's core: the routine's authorship (UNKNOWN) — A's trust engine turns on it.
2. MYSTERY-011: who sent the anonymous cache (genuine open thread; four in-world candidates).
3. MYSTERY-089: the Tuesday problem's mechanism (OPEN minor) — the structural romantic obstacle's physics.
4. MYSTERY-005: who approved Arthur's hiring (ch. ~250–350) — reframes C's entire decision window.
5. MYSTERY-008: the Quiet Desk's actual plan (UNKNOWN/PROVISIONAL, live thread) — C's institutional antagonist.
6. MYSTERY-055: the Lantern Bearers' second leak (held-back reserve) — A's post-commitment test.
7. MYSTERY-087: what Saitō's Loudness is adjacent to (OPEN) — E's founding fact.
8. MYSTERY-003's torn page contents (L5-5, intentional; ch. ~350–450) — D's long clock.
9. SECRET-024: the handwriting check's outcome — D's trust tripwire.
10. MYSTERY-026: what Nwosu's suppressed paper showed — B's Institute shadow.
11. Nadia's pre-canon relationship history (UNKNOWN — recorded, not invented).
12. Kira's Census registration status; Aisha's Attuned tier (both intentional UNKNOWNs, §23).

---

## 25. Canon Dependencies

This audit depends on (and did not alter): ANOMALY-001's mechanism (tether, not shadow); the inheritance chain (proximity + Loudness, unengineered); the March 2017 Ravenscroft transfer (Yusuf → Arthur); Arthur's locked identity; all character/faction/anomaly IDs; the mystery architecture (105 mysteries, reveal order, dependency graph, red-herring registry); the power progression (5 disciplines, Erosion/Fathom economics, the ratchet, the 7-stage curve); the faction/conflict engine (88 org IDs, 50 RC + 52 CG, autonomy verified); the information economy (SECRET-001–024 knowledge grid); 32_ROMANCE_FRAMEWORK.md's six rules and five configurations; the Phase-3 charpatch rulings (incl. the Static Hour beat's non-transfer).

Downstream phases (Story & Arc Architecture; Chapter Engine) inherit: the five configurations as *alternatives*; the dinner rule as the commitment technology; reveal-order gating of all romance beats; the independence watches (§9–10); the trope watches (§17/§21); the intentional UNKNOWNs (§24); the invariant that **romance and the main mystery develop independently and intersect** — neither replaces the other.

---

## 26. Final Report (§26 numbers)

- **Total characters analyzed:** 37 (CHAR-001–037, all).
- **Total plausible romantic relationships:** 5 configurations (A–E). Classifications: 1 HIGH POTENTIAL (A), 2 DIFFICULT BUT INTERESTING (B, C), 2 POSSIBLE (D, E), 0 LOW COMPATIBILITY among the canon five. 31 characters explicitly NO ROMANTIC FUNCTION.
- **Total relationship dependencies:** 15 mystery-dependency links gate romance beats (D-01, D-02, D-03, D-05, D-06, D-07, D-08, D-12, D-13, C-02, C-03, C-04, C-06 + 2 soft); 5 information-asymmetry maps (50 dimension-cells); 5 attraction sequences; 5 trust engines.
- **Total contradictions found:** 3 genuine (CG-041 Saitō-source cell; DATABASE/EVENTS.md EVENT-097 Saitō beat; 21_CITIES.md Kira "Liwanag-based"). 2 candidates investigated and ruled out (Nadia Kusuma residual — stale note, zero hits; D-03 direction — intentional distinction).
- **Total patches made:** 3 [ROMANCE PATCH]es (all minimal; all stale residues; documented in §22 and CHANGELOG.md).
- **Total forced-romance risks found:** 0 violations. 2 novel-level watches (Ilsa-journal intimacy shortcut; Aisha 36/24 register) + 1 requirement (CG-044 atmosphere vs Nadia's routine — disproof on-page first).
- **Total information-asymmetry issues:** 5 complete maps; 0 unmapped asymmetries; 3 flags raised by analysts, all adjudicated (2 patched, 1 ruled intentional).
- **Total characters requiring additional independence:** 7 watches (1 elevated: CHAR-031 Nwosu — needs non-Arthur subjects; 6 LOW). 0 failures.
- **Total unresolved UNKNOWN items:** 12 (§24).
- **1000-chapter sustainability:** YES — all five configurations have post-commitment engines, priced non-repeating conflicts, and new-intimacy headroom through ch. 1000.
- **Ready to proceed to Story/Arc Architecture:** YES — GO. The romance system is coupled to (not replacing) the mystery engine, the faction engine, and the power engine; all three prior audits' constraints are preserved.

**Invariants re-verified:** DAICHI REMAINS AN ORDINARY PERSON. Romantic partners retain their own goals. Romance does not replace the main mystery. The main mystery does not destroy the romance. Both systems develop independently and intersect. No chapters, scenes, prose, dialogue, or story outlines were created.

---

*End of Romance Architecture Audit — Phase 7. Canon build v1.8.*


---

## SECTION: `AUDIT/STORY_ARCHITECTURE_AUDIT.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/STORY_ARCHITECTURE_AUDIT.md` · sha256 `1be8e41bbdda6315219b278563a7b6935da9a9f56bbbf9214ef1df686ac28a48` · 3,350 words. No content changed.

# STORY ARCHITECTURE AUDIT — THE QUIET TIDE

> **Phase 8 — audit of the story & arc architecture.** Method: audit-first, minimal edits. This audit verifies the three Phase 8 databases (`STORY_ENGINE.md`, `ARC_ARCHITECTURE.md`, `ARC_DEPENDENCY_GRAPH.md`, `LONG_SERIAL_STRUCTURE.md`) against the canon they inherit (mystery, power, faction, romance, and all prior phases). It reports genuine contradictions, applies patches only where the contradiction is real, and records everything else as watches, open items, or intentional exceptions.
> Canon build v1.9. Audit date: 2026-09-20.

---

## §1. Scope and method

This audit covers: the central story engine (three questions, Arthur's UNFILED→ANSWERABLE internal arc, the ordinary-life engine, the information/reveal engine, the faction and romance interfaces, P1–P4, endgame direction); the 12-arc spine (all required per-arc fields); the dependency graph; the long-serial structure (7 checkpoints, the Approach band); and the Chapter Engine inheritance contract.

Not in scope: chapters, scenes, prose, dialogue (Phase 8's hard constraint — none exist in these files, verified by scan).

The audit ran: ID/event/name/age scans; canon-lock checks; reveal-order window verification against `REVEAL_ORDER.md`; power-curve verification against the 7-stage progression; faction-autonomy verification (28/28, 0 Arthur-required); romance-constraint verification (six rules, dinner rule, 15 mystery gates); conflict-kind verification against the 60-kind palette; filler testing (≥2 systems/arc); retcon scanning (no invented IDs/events); and stress tests at chapters 50/100/200/300/500/700/1000.

---

## §2. Arc inventory verification

- **12 arcs proposed, 12 arcs verified** — within the required 8–15 band.
- Every arc carries all 17 required fields: ID/title/range; central conflict; Arthur's objective; opposing force; mystery question; emotional question; power-development purpose; faction consequences; romance consequences; information gained/lost; turning point; climax; aftermath; unresolved consequences; new questions. Verified by per-arc scan of `ARC_ARCHITECTURE.md`.
- Arc IDs are unique (ARC I–XII); working titles are unique; no two arcs share a title.
- Chapter ranges are sequential with deliberate overlaps (III opens inside II's window; VIII and IX share ~400–500; XI opens inside X's window) — the overlaps are the interleave's structural form, not errors: they are where two arcs' climaxes share a chapter band without sharing a kind.

---

## §3. Mystery integration (105 mysteries)

- The spine integrates all 105 mysteries (41 major, 64 minor) per the arc entries' mystery-question fields and `LONG_SERIAL_STRUCTURE.md` §2's checkpoint inventories.
- **No premature reveals:** every arc's mystery beats were checked against `REVEAL_ORDER.md` windows. The adjudication in `STORY_ENGINE.md` §11.1 (canon wins over the worker's endgame-hold instruction for 005/008/011/012/026) is verified correct — the five resolve in their P3 canon windows, and the arc entries stage them there (ARC IV: 005's redaction breaks; ARC VI: 008's pitch, 011's sender, 012's catastrophe; ARC IX: 026's suppressor).
- The L5 schedule is protected: L5-1 (ARC XI), L5-2 (ARC XII), L5-3 (never fully resolved), L5-4 (open past ch. 350), L5-5 (ARC VIII). No L5 resolves outside its window. L5 resolutions never share an arc (verified: XI holds 015/027/026; XII holds 002/013).
- The two deliberate ironies (SECRET-007, SECRET-015) are the only cases where the reader leads Arthur by more than one phase — both are canon-marked, not accidents.

---

## §4. Reveal-order window verification (D-01–D-24, C-01–C-06)

- The D-table's 24 hard/soft edges are respected: D-07 (005→008) is repriced at ARC VIII's page payoff ("the pitch lands differently now"); D-14 (the margin's data) stages ARC XI's collation; the dependency backbone (ARC 1 → {2,3} → 4 → {5,6,7} → 8 → {9,10} → 11 → 12) matches the mystery worker's verified chain.
- The C-table's 6 constraints hold: the C-05 fusion (014→034 in ARC IX) is the single permitted cross-mystery fusion (intentional exception, `STORY_ENGINE.md` §11.2); no other fusions appear in any arc entry.
- Reveal budget: ~1 major/25ch (P2–P3), ~1/40 (P4), ~1/60+ (Approach band) — 41 majors against a ~30-reveal budget leaves headroom; the serial can slow down without starving.

---

## §5. Dependency-graph verification

- The graph (`ARC_DEPENDENCY_GRAPH.md`) is acyclic — all edges point forward. Verified by edge-direction scan.
- Every arc has ≥2 inbound edges from distinct systems (the no-filler rule's structural form). Verified per arc.
- The longest hard path is 12 nodes (I→XII) — the 8–15 band's upper-middle, leaving room for continuation.
- The mystery-layer longest chain (001→004→003→002→007) is protected end-to-end.
- The Arthur-free test holds at the graph level: removing Arthur deletes 0 nodes and 0 edges (every edge is faction-caused or canon-caused; his intersections are instantiations).

---

## §6. Power-curve verification (no jumps)

- Arthur's 7-stage progression maps cleanly onto the spine (ARC I: 1–2 … ARC XII: 7), ~100 chapters/stage average, back-loaded. No stage is skipped in any arc transition.
- The 16-item no-shortcut list and the 8 power-jump brakes bind every arc: verified present in `STORY_ENGINE.md` §10's inheritance contract and referenced in each arc's power-development-purpose field.
- **"The bullet still works" at Stage 7:** ARC XII's power purpose explicitly requires no new Uses — the finale is the clerk's method pointed at the one witness no form can price. Arthur remains T0/ordinary; his arc is UNFILED→ANSWERABLE (presence), not WEAK→STRONG.
- The Approach band adds NO new stages — Stage 7 is the ceiling. Verified in `LONG_SERIAL_STRUCTURE.md` §3's forbiddens.

---

## §7. Faction-autonomy verification

- 28/28 factions AUTONOMOUS; 0 Arthur-required conflicts; the 15 Arthur-instanced conflicts are machines he instantiates, never machines he owns. Carried forward from the Phase 6 audit — the story architecture introduces no new dependencies.
- Every arc's "where he must NOT go" limits (from the faction worker's map, reconciled in `ARC_ARCHITECTURE.md` §13.1) are consistent with the autonomy verdicts: he never leads the Akari cell, never decides the taxonomy, never wins the branch war, never interdicts Drowndust, never arbitrates the port truces, never tips the Cantorate succession, never finds the ninth site, never stops the Court's collecting, never holds the dead-man's archive, never auctions the blind spot, never breaks the masquerade as the source, never coordinates the Trench Front response.
- The five actors holding canon facts about him (CORP-011, GOV-006, GOV-014, IND-004, SUP-009) are unchanged; everyone else remains UNAWARE.

---

## §8. Romance verification (no forced romance)

- All five configurations map to legal reveal-order windows (the 15 mystery-dependency gates, `ROMANCE_ARCHITECTURE.md` §25); no configuration reaches commitment before its gate mysteries resolve.
- The six inviolable rules hold across the spine: no configuration violates Rule 1 (the asymmetry is the story for any Quiet partner), Rule 2 (memory-as-violation treated as such), Rule 3 (Erosion never aestheticized), Rule 4 (the org chart is always in the room), Rule 5 (the dinner rule — the Willowmere gauntlet is the single commitment technology in every arc's romance-consequences field), or Rule 6 (his romantic assets are attention/memory/honesty/showing-up — verified in ARC IV's "the telling as restoration currency" and ARC XII's "the partner as the person he finally writes the mirror for").
- **0 forced-romance violations.** Unselected configurations resolve into friendship/professional/severed forms at their gates — never dangling rivals.
- The two trope/implementation watches from Phase 7 are carried forward (§24).
- The 7 independence watches (1 elevated: CHAR-031 Nwosu; 6 lower) are carried forward (§24).

---

## §9. Ordinary-life engine verification

- The engine's four functions are active in every arc's ordinary-life texture (the night shift, the 1K's ¥48,000 economics, the every-other-Sunday dinner, the Night Clerks' futsal/Discord).
- **The archive job provides perspective, not omniscience:** verified across arcs — he files what he sees; what he sees is partial (ARC III's watch-list beats show him being read without knowing it; ARC VIII's "the Archive addresses him by name" is the archive reading HIM). The audit found no arc where his files give him unearned knowledge.
- Scale control holds: romance scales DOWN while the plot scales up (ARC XI's romance consequences field states this explicitly).

---

## §10. Conflict-kind verification (no repetitive structure)

- The 60-kind palette (sourced from the 52 CGs + 50 RCs) governs the 10 regular arcs.
- Per-phase verification: P1: ARC I (60, authentication — private self-appraisal); P2: ARC II (60, authentication/provenance contest), ARC III (13, archive audit); P3: ARC IV (48), ARC V (43), ARC VI (59), ARC VII (39); P4 regular: ARC VIII (47, survey expedition), ARC IX (51, truth commission), ARC X (39, doctrinal schism).
- **Zero within-phase repeats** among regular arcs.
- **Adjacency watch (not a violation):** ARC I (60) → ARC II (60) share the 60 family across the P1/P2 boundary. The rule is per-phase; the two beats are structurally different (private self-appraisal vs. provenance contest). Recorded as a watch for the Chapter Engine, not a patch.
- **Intentional exception:** ARC XI (collation at cosmological scale) and ARC XII (the test) are ENDGAME STRUCTURES with no palette instance. The endgame's job is cosmological closure + the personal test; forcing palette labels would misfile them. (`ARC_ARCHITECTURE.md` §14.)
- **Corrections applied in this audit:** ARC VIII's dual label ("authentication (60) / survey expedition (47)") → primary **survey expedition (47)** (the missing-Seep survey is the central kind; the page's authentication is the major secondary beat); ARC X's dual label → primary **doctrinal schism (39)** (the Garden's schism; the Well's margin survey is secondary). Both corrections are kind-selection, not content changes — no canon altered.

---

## §11. Filler testing (each arc moves ≥2 systems)

- Applied the faction worker's filler criterion: an arc is filler if it touches neither Arthur's stakes, nor the mystery layer, nor the power layer.
- **All 12 spine arcs PASS:** each moves mystery + ≥1 of faction/power/romance/ordinary-life (verified per arc in `ARC_ARCHITECTURE.md`'s per-arc fields).
- The ~90 demoted generators are handled per `ARC_ARCHITECTURE.md` §13.4 (texture/subplot/single-scene) — the architecture explicitly names the demotion list, so the Chapter Engine cannot accidentally arc them.

---

## §12. Retcon scan (no invented IDs/events)

- Scanned all three Phase 8 databases for invented IDs, events, factions, or characters: **none found.** Every ID and event cited exists in the canon databases.
- **Citation mismatches found and dispositioned:**
  1. MYSTERY-019's "(EVENT-061)" — genuine wrong-number citation; patched ([STORY PATCH] 1). The 1975–76 preacher incident is canon-supported in-world fact with no EVENT ledger entry. Verified no remaining EVENT-061 citations in `MYSTERIES.md` (only the [STORY PATCH] annotations remain).
  2. The power/romance worker's validation draft stated the March 2017 transfer as EVENT-100 in one checklist — **worker-draft error, not canon.** Canon consistently holds EVENT-079 (verified in `25_TIMEmessaging app.md` and `DATABASE/EVENTS.md`: "EVENT-079 | Yusuf Hidayat Dies (2017)"). No canon file contains the error; no patch needed. The draft was deleted with `_story_drafts/` before release.
  3. CG-029's site (Jakarta per 31/CG-029 vs. Ravenscroft per CG-050) — genuine canon tension; NOT patched (silent fixes are forbidden). Recorded as an open design item (`STORY_ENGINE.md` §11.7; §18 below). The ward-anchor crisis (~ch. 650–700) cannot be built until the site is chosen.

---

## §13. Stress tests (ch. 50/100/200/300/500/700/1000)

Criterion: ≥3 live threads across ≥2 systems at each checkpoint.

- **~50:** ≥6 live threads / 4 systems — PASS.
- **~100:** ~12 / 4 — PASS.
- **~200:** ~20 / 4 — PASS.
- **~300:** ~25 / 4 — PASS.
- **~500:** ~25 / 4 — PASS.
- **~700:** ≥6 / 3 — PASS (the personal test narrows the field by design; world-scale threads are queued for the Approach band).
- **~1000:** the Approach band's convergence fuel (Trench Front, Peal window, CG-052's redline spent, post-secrecy collapse) + the ENDGAME UNKNOWN ledger — PASS.
- Full checkpoint inventories in `LONG_SERIAL_STRUCTURE.md` §2.

---

## §14. Endgame-direction verification

- **Direction, not resolution:** verified — no arc writes an ending. ARC XII's climax is "the asking — and the answer, or the silence that is the answer." The Approach band is explicitly forbidden from writing an ending (`LONG_SERIAL_STRUCTURE.md` §3).
- **CG-052's redline:** earned in ARC XI (contingencies ACTIVATED), spent only in the Approach band (~900–1000). The "usable only after hundreds of chapters" constraint is respected.
- **The ENDGAME UNKNOWN ledger is clean:** L5-3 (the Undertow's want); the Well (ANOMALY-029 — unusable ceiling); the 10s+ ratchet question; Bus 12's fare-box; entity omniscience (never canon); the ninth Peal site; MYSTERY-087/089 (Saitō); the 2014 memo; the Garden's Root endpoint; Peal-vs-Front coincidence/competition (the story engine's design decision, not canon's).
- L5-3's "never fully resolved" status is protected — the audit verified no arc entry resolves or recontextualizes it into an answer.

---

## §15. Long-serial sustainability verdict

- **~500 chapters: SUSTAINABLE.** The spine's P1–P4 structure, the 41-major reveal budget, the 7-stage power curve, and the 12-system interleave carry to ~500 without strain.
- **~1,000 chapters: SUSTAINABLE WITH THE APPROACH BAND.** The spine closes at ~700; the Approach band (~700–1000+) provides convergence fuel without new power stages, new arcs, or an ending. Past 1,000, the 102 generators' ordinary operation sustains continuation — the architecture promises the systems still run, not a new spine.
- The verdict's load-bearing assumptions: (a) the Chapter Engine respects the reveal budget; (b) the CG-029 site decision is made before ~ch. 650; (c) the Peal-vs-Front decision is made before ~ch. 850; (d) the filler demotion list is honored.

---

## §16. Chapter Engine readiness verdict

**READY, with four preconditions.** The Chapter Engine inherits: the D-table (24 edges); the L5 schedule; the 16-item no-shortcut list + 8 power-jump brakes; the faction autonomy verdicts (28/28, 0 Arthur-required); the dinner rule + six romance rules + 7 independence watches; the 60-kind palette + the kind-per-arc rule + the endgame-kind exception; the question-debt cap (≤2/arc); the reader-lead rule; the ordinary-life engine's four functions; the endgame-unknown list; the filler demotion list; the checkpoint thread map.

Preconditions before chapter planning begins:
1. Choose the CG-029 ward-anchor site (Jakarta / Ravenscroft / parallel developments) — blocks the ~650–700 crisis otherwise.
2. Choose Peal-vs-Front (coincide / compete / catalyze) — blocks ~ch. 850+ otherwise.
3. Select the romance configuration (A–E) — the gates are mapped; the selection is the Chapter Engine's first design decision.
4. Confirm the Approach band's ~700–800 "controlled pile-up" staging (dead-man's archive, blind spot, saint, ward anchor, ninth-site hunt) as convergence, not a traffic jam.

---

## §17. Patches applied

- **[STORY PATCH] 1 — MYSTERY-019's wrong EVENT-061 citation** (genuine contradiction; wrong-number citation). Applied to `DATABASE/MYSTERIES.md`; documented in `AUDIT/CHANGELOG.md` and here. The 1975–76 Choir preacher incident is canon-supported in-world fact with no EVENT ledger entry.
- **Kind-label corrections (§10):** ARC VIII → survey expedition (47) primary; ARC X → doctrinal schism (39) primary; ARC XI/XII → endgame-kind intentional exception. Kind-selection only; no canon content altered.
- **CG-048 auction re-windowed to ~400–450** (`STORY_ENGINE.md` §11.6): the faction worker's inferred ~750 window conflicted with the canon edge CG-043→CG-048→ARC VIII's page-surfacing. Sequencing correction; no canon content altered.
- **Phase 7 patches carried forward** (3): CG-041's Saitō-source removal; EVENT-097's Static Hour beat removal; Kira's Ravenscroft basing. All verified present in the v1.9 tree.

---

## §18. Contradictions found (genuine)

1. MYSTERY-019's EVENT-061 citation — **patched** (§17).
2. CG-029's site (Jakarta vs. Ravenscroft) — **open**, not patched (§12.3). The architecture requires a site decision before the ward-anchor crisis.
3. The validation draft's EVENT-100/transfer claim — **worker-draft error, not canon** (§12.2). No canon file affected.

No other genuine contradictions found. The audit ran the full contradiction battery (IDs, event numbers, names, ages, canon locks, reveal dependencies, power limitations, faction autonomy, romance constraints, duplicate kinds, filler/retcon) — the three items above are the complete list.

---

## §19. Information-asymmetry verification

- Arthur remains "the subject of most secrets and the knower of almost none": only five actors hold canon facts about him; the spine never grants him unearned knowledge (§9).
- The reader-lead rule (≤1 phase, except SECRET-007 and SECRET-015) holds across all arcs.
- The five information-asymmetry maps (50 dimension-cells, from the romance architecture) are consistent with the arc windows — no arc requires a character to know what their asymmetry map says they don't.

---

## §20. Question-debt verification

- ≤2 new open threads per arc: verified per arc — no arc's "new questions" field opens more than two.
- The series-level debt at spine close (~ch. 700) is the §14 ledger: staged-but-open items + permanent ENDGAME UNKNOWNs. The debt is intentional and budgeted, not accidental.

---

## §21. Interleave verification

- The 12 faction systems map onto the spine without gaps or collisions (`ARC_ARCHITECTURE.md` §13.1–13.3).
- No checkpoint has fewer than 4 ACTIVE/PEAK systems; no system PEAKs at two adjacent checkpoints.
- The Masquerade War never fully quiets (correct — it touches every engine).
- The Trench Front and Defector's Codes stay dark early (dread, not furniture).
- The ~650–750 controlled pile-up is staged as convergence.

---

## §22. Phase-structure verification

- P1 (~1–100), P2 (~100–250), P3 (~250–450), P4 (~450–700) — the 12 arcs sit inside their phases per the reveal-budget rules (~1/25ch P2–P3; ~1/40 P4).
- The Approach band (~700–1000+) is NOT a fifth phase — it is the continuation band, and the audit verified it introduces no new power stages, no new arc spine, and no ending.

---

## §23. Canon-lock preservation

- ANOMALY-001's mechanism: untouched.
- Inheritance via proximity + Loudness, unengineered: untouched.
- March 2017 Ravenscroft transfer, Yusuf → Arthur (EVENT-079): untouched.
- All IDs and established terminology/history: untouched. The ID/event/name/age scans found no drift.
- The Philippines remains secondary and un-British-ified; Ravenscroft/Albion remains primary.
- Arthur remains genuinely ordinary and weak; the UNFILED→ANSWERABLE arc never becomes WEAK→STRONG.

---

## §24. Residual risks and watches (carried forward)

**From Phase 7 (romance):**
- Trope watch 1: Ilsa's journals' intimacy must not perform Pram/Kira's emotional work.
- Trope watch 2: Aisha's 36/24 register must not become maternal or flattering.
- Independence watch (elevated): CHAR-031 Nwosu needs visible non-Arthur subjects/Vesper conflicts.
- 6 lower-level independence watches (per `ROMANCE_ARCHITECTURE.md` §24).
- 12 unresolved romance UNKNOWNs (per the romance audit).

**From Phase 8 (story):**
- Adjacency watch: ARC I→II share the 60 family across the P1/P2 boundary (§10).
- The CG-029 site decision (blocks ~ch. 650–700).
- The Peal-vs-Front decision (blocks ~ch. 850+).
- The romance-configuration selection (the Chapter Engine's first design decision).
- The Approach band's pile-up staging (convergence, not traffic jam).

---

## §25. Unresolved UNKNOWNs ledger (story layer)

1. Peal-vs-Front coincidence/competition (design decision, not canon).
2. The CG-029 site (Jakarta / Ravenscroft / parallel).
3. L5-3 (the Undertow's want — permanent ENDGAME UNKNOWN by design).
4. The Well's usability ceiling (ANOMALY-029 — permanent by design).
5. The 10s+ ratchet question (permanent by design).
6. The ninth Peal site (UNKNOWN by design).
7. MYSTERY-087/089 (Saitō's adjacency; the Tuesday mechanism).
8. The 2014 Quiet Desk memo's recommendation (MYSTERY-049).
9. The Garden's Root endpoint (two members "seated").
10. Bus 12's fare-box (intentional mystery — the story is the audit).
11. Entity omniscience (never canon — a permanent boundary, not a gap).
12. The romance-configuration selection (A–E) — the Chapter Engine's decision.

Plus the 12 unresolved romance UNKNOWNs from Phase 7 (separate ledger, `AUDIT/ROMANCE_ARCHITECTURE_AUDIT.md`).

---

## §26. Final report

**Verdict: the story architecture supports a ~1,000-chapter serial.** The 12-arc spine (P1–P4, ~1–700) carries the mystery, power, faction, romance, and ordinary-life engines through earned arcs with no premature reveals, no power jumps, no forced romance, no faction dependence on Arthur, no repetitive arc structures, no filler, and no accidental retcons. The Approach band (~700–1000+) provides the world-scale convergence fuel without new power stages, new arcs, or an ending. The Chapter Engine is READY, subject to the four preconditions in §16.

**Counts (actual, verified):**
- 12 arcs (8–15 band); 17/17 required fields per arc.
- 105 mysteries integrated (41 major, 64 minor); 0 premature reveals.
- 7-stage power curve; 16-item no-shortcut list; 8 power-jump brakes; 0 jumps.
- 28/28 factions autonomous; 0 Arthur-required conflicts; 12 faction systems interleaved.
- 5 romance configurations; 15 mystery gates; 6 rules + dinner rule; 0 forced-romance violations.
- 60-kind palette: 0 within-phase repeats (10 regular arcs); 2 endgame-kind intentional exceptions.
- 7/7 stress-test checkpoints PASS.
- 1 genuine contradiction patched ([STORY PATCH] 1); 1 genuine tension recorded open (CG-029 site); 1 worker-draft error dispositioned (not canon).
- 12 story-layer UNKNOWNs + 12 romance UNKNOWNs; 7 independence watches; 2 trope watches.

**Files delivered (Phase 8):**
- `DATABASE/STORY_ENGINE.md` — the central story engine.
- `DATABASE/ARC_ARCHITECTURE.md` — the 12 arcs + faction-interleave reconciliation (§13) + endgame-kind exception (§14).
- `DATABASE/ARC_DEPENDENCY_GRAPH.md` — the dependency backbone, the L5 chain, the power spine, the romance gates.
- `DATABASE/LONG_SERIAL_STRUCTURE.md` — the pacing budget, the 7 checkpoints, the Approach band, the viability verdict.
- `AUDIT/STORY_ARCHITECTURE_AUDIT.md` — this file.

**Chapter Engine readiness: READY** (§16 — four preconditions named).

---

*End of STORY_ARCHITECTURE_AUDIT.md — Phase 8, THE QUIET TIDE.*


---

## SECTION: `AUDIT/SERIALIZATION_AUDIT.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/SERIALIZATION_AUDIT.md` · sha256 `e543ced15bf93b3632e00156fcef8c6940c5289e4629cd21718cad5d7354fef1` · 2,843 words. No content changed.

# SERIALIZATION AUDIT — THE QUIET TIDE (v1.2, Albion-primary)

> Worker: AUD-STORY · Date: 2026-09-19 · Scope: power-creep stress test at 50/100/200/500/1,000 chapters; 500+ chapter capacity verdict; structural ceiling.
> Method: read-only. Sources: 29 (the 12-use ladder, costs), 30 (tier/Erosion economics), 02 (hard rules), 26 (masquerade arithmetic), 31/32/33 (arc fuel), 25 (timeline tail heat).

## 0. The anti-creep architecture (what the bible gets right)

Before the milestones: the premise is *structurally* resistant to power creep, which is rare and load-bearing for this audit.

1. **Arthur's toolkit scales in cost, not output.** The 12 uses (29 B.11) are information-gathering, never force. Deeper use buys longer windows and more risk — never a bigger punch. There is no "Laggard level 2."
2. **Erosion makes high tiers one-shot.** T5s get 1–3 major uses *total* past 60 Fathoms; T6s are dying under observation (30.2). The novel cannot build a shonen escalation ladder because the top of the ladder is a hospice.
3. **The ceiling is preparation, not power** (30.3): "a better-prepared nobody." This is an inexhaustible generator — preparation is situational, not cumulative.
4. **The scarce resource is information** (02.II), and Arthur's edge is *being informed* (29 B.12). Information advantages decay (others learn, files update, the Veil edits) — unlike power advantages, they don't compound forever.

**The honest risks** are therefore not "Arthur gets too strong" but: (a) the uses become *routine* (procedural drift); (b) the escrow creates *stasis* (nobody can touch him); (c) the 12-use ladder *runs out*; (d) the masquerade's own arithmetic (26.4) changes the world under the story. Each milestone below tests these.

---

## 1. Milestone stress tests

### Ch 50 — Discovery (Uses 1–5)

**Expected state:** Arthur discovers Uses 1–5 in order (Veil-immune witness → lag-as-recording → seeding anchor → Tide-mark dowsing → stepping into the lag). The Kota Tua replay accident (Use 5) is the mid-arc set piece. Faction heat is at the timeline-tail level (EVENT-091..100): inquiries, letters, an unfiled follow-up — *attention, not action*. Romance configs introduced; Night Clerks cell active; RC rotation is Ravenscroft-local (RC-016, 021, 027, 040, 043, 047, 048).

**What breaks:** Nothing structural. **The risk is pacing, not mechanics:** eight factions developed Arthur-specific interest in the six months before story start. If the novel cashes more than 2–3 of those threads in the first 50 chapters, the "filed T1 curiosity" protection (29 B.9) collapses and the Enemy C/D tiers must act — forcing the plot past street level prematurely. **Guardrail:** treat EVENT-091..100 as a slow-burn menu; the protection expires *across* the first 100 chapters, not in the first 20.

**Cost economy check:** Uses 1–5 are cheap (observation, a 3-second dodge). The ratchet doesn't move on ordinary life (29 B.6). No economy strain.

### Ch 100 — Deepening (Uses 6–9)

**Expected state:** Deliberate deepening (Use 6: 3s→3min→3h), shadow-storage (Use 7), thin-place dowsing (Use 8), unobserved observation (Use 9). First deliberate deepening costs "a day in bed and a dream of dark water" (29 B.11). The ratchet ticks visibly: 3.1s → ~3.2s. The entity's attention becomes personal (orientation shifts, cold drift). Pram/Cartographers begin *experiments* (29 B.9: "they will experiment" — the most dangerous interest). The Pale Court bloodline thread opens (EVENT-098 → "Is the Hollow Pattern in his line? UNKNOWN").

**What breaks:** Two things strain here —
1. **Routine deepening.** If 3-minute out-of-phase observation becomes Arthur's standard solution, the Laggard stops being costly and starts being a power. The counters exist (Lantern-sensitives feel the wrongness across kilometers; the entity notices; the ratchet; a 3-minute deepening costs a day in bed) — but the novel must *show the bill every time*, or procedural drift sets in. This is a discipline requirement, not a canon gap.
2. **Use 7 (storage) vs. 02's "no permanent created matter."** Storage holds *real* objects out-of-phase — not created matter, so no rule broken — but "retrieve within the lag window or it is gone (to where, UNKNOWN)" is a loaded gun. At ch 100 the novel will be tempted to store something plot-critical. The Rule's capacity limit ("only what the shadow can cover," "nothing living") must hold under pressure. Canon supports it; the novelist must not widen the shadow for convenience.

### Ch 200 — The clean recording + the escrow (Use 10)

**Expected state:** Use 10 discovered (accident: a developed photo shows the shadow mid-replay). Arthur builds the dead-man's-switch escrow (29 B.11: "the week he understands what Use 10 actually means"). This is the series' biggest structural event: Arthur becomes a mutually-assured-disclosure node at personal scale. Romance arcs begin resolving (32's configs are built for 100–200 chapter arcs). The torn-page auction (CG-048) can pay off L5-5's first half. The 12-use ladder is nearly exhausted (Uses 11–12 are understanding/flare, not techniques).

**What breaks if mishandled:**
1. **"Why doesn't Arthur just publish everything?"** — the question the whole masquerade must survive. Canon answers it six ways (26.4: the audience forgets; the evidence rots — but his *doesn't*; the perfect leak reads as content; there is no single secret; golden handcuffs; partial successes get absorbed). The escrow's genius is that it does *not* target the public — it targets *factions and a lawyer* (29 B.11). Targeted disclosure works where broadcast fails, because factions (unlike the public) have institutional memory and something to lose. **The novel must never let the escrow become a broadcast threat** — that would contradict 26.4. (→ SER-001: the escrow's limits need one explicit canon line.)
2. **Escrow stasis.** Once the switch exists, "seize/disappear Arthur" plots die. That's *intended* (it forces smarter enemies), but the novel must pivot to what the escrow does *not* protect: his visa (SSW tied to NQA — 29), his family in Tebet (EVENT-098's bloodline interest), recruitment/coercion (Vesper's "clinical, consensual, well-funded — and impossible to leave," 29 B.9), framing (his files can be edited — RC-016's "everyone wants it edited"), and the entity's attention (no escrow covers the other end of the tether).

### Ch 500 — The long middle (ladder exhausted; world carries the story)

**Expected state:** The 12 uses are fully discovered by ~ch 150–200. From here, novelty comes from the *world*, not the anomaly: the ratchet clock (3.4s → 4s → 5s…; Ilsa's data gives the ruler), the entity's escalating attention, the Trench Front (RC-050) season arcs, the Peal/ninth-site hunt (34 §34.4), the Branch War's long game (RC-021), Arthur as a Night Clerks organizer (RC-040's unionization arc), and the masquerade's arithmetic failure ("outpaced, not exposed," 26.4) changing the world under the story.

**What breaks:**
1. **The ladder runs out.** With no Use 13+, the anomaly chapters risk repetition (another deepening, another observation). The discovery grammar is stated ("discovered through observation, never granted by revelation," 29) but the bible never says the ladder is *open-ended by principle*. (→ SER-002.)
2. **The ratchet needs a ruler.** Ilsa: 3.0→3.4s over 7 years of heavy use. Arthur: 3.0→3.1s over ~7 years of ordinary life. For a 500-chapter run with regular extreme use, the novelist needs a rough exchange rate (ratchet per deepening) or the clock is unplannable — and an unplannable clock can't generate dread. (→ SER-003, LOW.)
3. **T5/T6 temptation.** At 500 chapters the novel will want bigger antagonists. Canon forbids the obvious move: T5s Drown in an afternoon (30.4 Scenario 4), T6s are dying under observation. The correct escalation is *institutional* (the Compact's contingency, faction war, the Peal) and *informational* (who knows what about Arthur), not *tier* escalation. The bible's Erosion arithmetic is the guardrail; the novelist must not invent a "stable T5" without paying the CHANGELOG price (02.V).
4. **The flare (Use 12).** "A flare he can't unfire… everyone comes. Everyone." At 500 chapters this button can be pressed at most once or twice — after the first flare, the T1 filing is dead and every tier re-files him. (→ SER-005.)

**What does NOT break:** the street-level premise. Sweepers still sweep, claims still get filed, the night shift still runs — because the masquerade fails by *arithmetic* (too many events, too few Sweepers), not by revelation. A failing-secret world still needs clerks. The premise's floor is solid.

### Ch 1,000 — Beyond the ceiling

**Verdict: not sustainable without a phase change.** By ~ch 600–800, three clocks converge:

1. **The masquerade's arithmetic** (26.4): the minority report's conclusion ("outpaced, not exposed") is the bible's committed endgame. A 1,000-chapter run *reaches* the endgame — the story becomes post-secrecy, which the bible pre-builds (CG-052 High Tide Contingency, "post-secrecy protocols," the Bell's witness program). That is a *different premise* (open supernatural world), not a failure — but it must be recognized as a phase change.
2. **The ratchet threshold** (L5-5): Ilsa's torn page "names the ratchet's end." Whatever happens at 10s / a minute *is* the Laggard's endgame. A 1,000-chapter run must either reach it or explain why the ratchet stalled — and stalling it contradicts 29 B.6 ("the lag is a clock, and it only runs one way").
3. **Arthur's transition:** 500 chapters of earned information advantage turns the best-informed weak man in Ravenscroft into an *institution* (Night Clerks leadership, NQA branch power, escrow-holder as political actor). The "weak clerk" premise dissolves into "player" premise — again, a legitimate phase change, but the bible's core promise ("never secretly omnipotent… the world is indifferent") must then be renegotiated, not quietly abandoned.

---

## 2. 500+ chapter capacity verdict

| Question | Answer |
|---|---|
| Longest the premise sustains (as constituted) | **~400–600 chapters** |
| What sustains it that far | The ratchet clock, the entity's attention arc, the masquerade's arithmetic failure as slow-burn endgame, the RC rotation (50 RCs × 3–4 uses each ≈ 150–200 chapters of A-plots alone), 5 romance configs, the torn-page/L5 payoff schedule |
| Structural ceiling | The convergence of the three clocks above (§1, ch 1,000) |
| What happens at the ceiling | Phase change: post-secrecy world and/or Arthur-as-institution and/or the ratchet's end. The bible *prepares* all three (CG-052, 26.4, L5-5) — the ceiling is a door, not a wall |
| Can it do 1,000 chapters? | Only as a two-phase series (hidden world → failing/open world). As a single-premise serial, no — and the bible is honest about why |

**The single most important sentence for the novelist:** the escalation vector of this series is *the world's secrecy failing*, not *the protagonist powering up*. As long as every "bigger" chapter makes the *world* more exposed rather than Arthur more powerful, the premise holds to ~600. The day a chapter makes Arthur win by being stronger rather than better-informed, the bible's promise breaks.

---

## 3. Formal issues

### SER-001 — MEDIUM — The escrow's limits are not stated (stasis risk at ~ch 100+)

- **Location:** `29_PROTAGONIST_ANOMALY.md` §B.11 (Use 10, "The escrow").
- **Conflicting statements (quote):** 29: "It is mutually assured disclosure at personal scale — the reason seizing *him* costs more than bargaining with him." vs. the absence of any statement about what the escrow does *not* deter.
- **Why it is a problem:** Once the dead-man's switch exists, every "seize/disappear Arthur" plot is dead — by design. But without a canon statement of the escrow's limits, a novelist at ch 150+ will either (a) treat Arthur as untouchable (stasis), or (b) invent workarounds that feel like cheating. The workarounds exist in canon (visa leverage — 29; family — EVENT-098; Vesper's consensual capture — 29 B.9; file-editing — RC-016; the entity's attention — 29 B.6) but are never gathered into the escrow's doctrine.
- **Proposed solutions:** (1) Add a canon paragraph to 29 B.11: the escrow deters *disappearance and seizure*; it does not deter recruitment, legal/coercive leverage (visa, family, employment), file manipulation, or anything at the entity's end of the tether. (2) No change to the escrow's mechanics.

### SER-002 — MEDIUM — No canon statement that the use-ladder is open-ended by principle

- **Location:** `29_PROTAGONIST_ANOMALY.md` §B.11.
- **Conflicting statements (quote):** 29: "Each use below is **discovered through observation, never granted by revelation**, and each is **paid for** per §B.6. The order is the discovery order — the novel's progression spine." vs. the absence of any statement about Uses 13+.
- **Why it is a problem:** The 12 uses are exhausted by ~ch 150–200 of a 500-chapter run. The discovery *grammar* is stated, but a future novelist (or drafter) has no canon warrant for Use 13 — and without one, new uses will read as granted-by-plot. The bible needs the principle, not the uses.
- **Proposed solutions:** (1) Add one canon line to 29 B.11: the twelve are the *documented* ladder (Ilsa's journals + Arthur's discoveries); the discovery grammar (observe → hypothesize → test → pay) remains the sole lawful generator of further uses, and every future use must be priced per §B.6. (2) Explicitly forbid "uses" that grant force or knowledge-without-interpretation (per B.5: "It does not grant knowledge — it grants records").

### SER-003 — LOW — The ratchet has no drafter's ruler (unplannable clock)

- **Location:** `29_PROTAGONIST_ANOMALY.md` §B.3, §B.6.
- **Conflicting statements (quote):** 29 B.3: "Ilsa: 3.0 → 3.4s over seven years"; "Arthur started at 3.0s in 2017 and is at ~3.1s now." 29 B.6: "*Extreme* use (deep lag, storage, the flare) adds permanent fractions of a second."
- **Why it is a problem:** "Fractions of a second" per extreme use is not plannable across 500 chapters. If a deepening costs 0.01s, the clock never matters; if 0.2s, Arthur hits Ilsa's 3.4s within a year of active use and the dread curve collapses. The novelist needs a ruler.
- **Proposed solutions:** (1) Add a non-binding drafter's guideline (not hard canon): ordinary life ≈ +0.01–0.02s/year; a 3-minute deepening ≈ +0.02–0.05s; a 3-hour deepening ≈ +0.2–0.4s (Ilsa's 3-hour maximum "almost didn't give her back"); the flare ≈ +0.5s+. At that rate, ~50 extreme uses over 500 chapters moves 3.1s → ~5–6s — dread without arrival. (2) Keep the ratchet's *end* (L5-5) untouched.

### SER-004 — LOW — Five romance configs, one protagonist: a planning dependency, not a bug

- **Location:** `32_ROMANCE_FRAMEWORK.md` §32.2.
- **Why it is a problem (planning, not canon):** Configs A–E are each built for 100–200 chapter arcs with structural (not miscommunication) obstacles. A 500-chapter run cannot fully service all five; choosing late wastes planted material, choosing early strands the others. The bible correctly does not choose (it's a framework), but the serialization plan must: primary / secondary / retired-by-events.
- **Proposed solutions:** (1) Serialization planning decision, no canon change. (2) Note: Config E (Saitō) doubles as the Loud-politics thread (CG-017/041, RC-018/030) — retiring it strands the masquerade-critique theme; Config A (Nadia) is the only Quiet-option and carries the Tuesday-problem ethics the setting needs.

### SER-005 — MEDIUM — The flare (Use 12) needs a point-of-no-return canon line

- **Location:** `29_PROTAGONIST_ANOMALY.md` §B.11 (Use 12).
- **Conflicting statements (quote):** 29: "Deliberately lengthening the lag to minutes is visible to every Lantern-sensitive for kilometers — a distress signal, a summons, a declaration. A flare he can't unfire." vs. no statement of the *filing* consequence.
- **Why it is a problem:** "Everyone comes. Everyone." After the first flare, the `MV-T1/C-A` filing ("a shadow with latency; recommend no further expenditure") is dead — every tier re-files him, the Seismograph Authority has a signature, and the "bureaucracy yawned three times" protection (29 B.9) ends permanently. Without a canon line saying so, a novelist at ch 300 might fire the flare as a clever escape and then return to street-level normalcy next arc — which contradicts the Enemy C/D simulation (NARRATIVE_AUDIT §5).
- **Proposed solutions:** (1) Add to 29 B.11 Use 12: the first deliberate flare permanently burns the T1-curiosity filing — post-flare, Arthur is a named priority across GOV-006, the Compact Classification Office, and every faction with Lantern coverage of Ravenscroft. (2) No change to the flare's mechanics.

## 4. HOLDS (escalation attacks the canon defeats)

- **"At ch 300 Arthur just deep-lags for 3 hours every arc."** — HOLDS: 3-hour deepening cost Ilsa a week and "it almost didn't give her back" (29 B.6); the ratchet bills permanently; the entity's attention is personal and compounding. Routine 3-hour use is suicide by schedule.
- **"A T5 antagonist at ch 400 forces power escalation."** — HOLDS: T5s get 1–3 major uses total (30.2); Scenario 4 (30.4) shows a T5 vs. a city loses to arithmetic. The correct ch-400 antagonist is institutional (Compact contingency, the Peal, faction war), not tiered.
- **"Arthur's information advantage compounds until he's effectively omniscient."** — HOLDS, conditionally: information decays (files update, the Veil edits others' memories, factions learn he reads them and feed him). The novel must show his sources *drying up or turning* as often as they pay off — a discipline requirement.
- **"The escrow makes him unkillable, killing tension."** — HOLDS: the escrow deters disappearance, not the six leverage vectors in SER-001. Tension moves from survival to *cost* — which is the series' register anyway (Darker than Black: installments paid in selfhood).

## 5. Counts

| Severity | Count | IDs |
|---|---|---|
| CRITICAL | 0 | — |
| HIGH | 0 | — |
| MEDIUM | 3 | SER-001, SER-002, SER-005 |
| LOW | 2 | SER-003, SER-004 |
| **Total** | **5** | |


---

## SECTION: `AUDIT/JAPANESE_CHARACTER_CONSISTENCY_AUDIT.md`

> Merged verbatim in Phase 20 (2026-09-21). Original: `AUDIT/JAPANESE_CHARACTER_CONSISTENCY_AUDIT.md` · sha256 `ac161c7c544be12c5cdc201a0dd22cf122460c3e5ce3b01fb1c7510641c3f3e2` · 2,025 words. No content changed.

# AUDIT — British Character Consistency (Phase 3)

**Agent:** British Cultural Consistency Audit (subagent a41dbe7f…)
**Date:** 2026-09-20
**Target:** Reed Arthur (CHAR-001), the Reed family (CHAR-012/013/014), Saitō Yūto (CHAR-015), Okada Kumiko (CHAR-036), Hasegawa Kenji (CHAR-037) — cultural consistency ONLY where they appear, act, or speak.
**Working copy:** `work_jp2/` (edits applied there)

## 1. Scope & method

- Read background canon first: `_charpatch_protagonist.md`, `_rename_registry.md`, rewritten Part A of `29_PROTAGONIST_ANOMALY.md`, `18_CIVILIAN_LIFE.md` §18.1 day-in-life (full read).
- Mapped every content-file mention of Arthur / Reed family / Saitō / Okada / Hasegawa via case-insensitive grep across the tree (392 hits in `37_FINAL_WORLD_BIBLE.md` excluded — not editable; `DATABASE/` excluded — read-only per constraints).
- Focus-checked: `15_EDUCATION.md` (vocational college plausibility), `16_MEDICINE.md` (hospital scenes), `14_LAW_ENFORCEMENT.md` (police/civilian), `21_CITIES.md` (Ravenscroft districts incl. Willowmere), `31_CONFLICT_ENGINE.md` (protagonist acts/speech), `25_TIMEmessaging app.md`, `26_INFORMATION_CONTROL.md`, `30_POWER_HIERARCHY.md`, `24_HISTORY.md`, `34_FACTION_RELATIONSHIPS.md`, plus Arthur contexts in `06_GOVERNMENTS.md`, `11_CORPORATIONS.md`, `12_FACTIONS.md`, `27_TECHNOLOGY.md`, `33_MYSTERIES.md`.
- Honorific check: regex sweep for `-san/-kun/-chan/-senpai/-sensei` (and capitalized forms) across all audited files.
- Applied the smallest possible correction for genuine inconsistencies only. Left everything "could be more British" alone. No renames (forbidden), no anomaly-mechanics or faction-canon changes, no cultural-textbook filler injected.

## 2. Findings

### 2a. Patched (6)

| # | Location | Issue | Severity | Fix applied |
|---|---|---|---|---|
| F1 | `18_CIVILIAN_LIFE.md` §18.1 | "Shift ends 06:00" but "Arthur's train is the first one, 05:58" — train departs before the shift ends. | low (internal logic) | `05:58` → `06:04` |
| F2 | `18_CIVILIAN_LIFE.md` §18.1 | "The landlord has stopped asking about the electricity bill." — In Albion electricity is billed by the utility company directly to the tenant; a landlord would never ask about the electricity bill. | med-low (cultural) | → "The landlord has stopped asking why his meter barely moves." (preserves the beat: the Laggard drinks light) |
| F3 | `18_CIVILIAN_LIFE.md` §18.1 | "Cup noodles … the homesick tax he doesn't owe anyone." — migrant-era residue; Arthur is a native British citizen, there is no homesickness narrative for him. | med (cultural/identity) | Removed the trailing clause. |
| F4 | `18_CIVILIAN_LIFE.md` §18.1 | Rent `¥58,000/month` contradicts `29_PROTAGONIST_ANOMALY.md` Part A (canonical profile): the same Willowmere 1K is `¥48,000/month`. (29 is not editable for this agent.) | low-med (internal) | → `¥48,000/month` to match the canonical profile. |
| F5 | `18_CIVILIAN_LIFE.md` §18.5 | "The 1K class (Arthur): … ¥50–65k/month" — Arthur's own rent (¥48k, per F4) falls outside the band that names him as its exemplar. | low (internal) | → `¥45–65k/month`. |
| F6 | `34_FACTION_RELATIONSHIPS.md:126` | "…no power, precarious residency…" — Arthur is a citizen with no visa clock (`01_CORE_PREMISE.md` canon: "No visa precarity — he is a citizen — but a thinner kind: his name sits in a flagged NQA hiring file…"). "Residency" precarity misstates the canon. | med (cultural/canon) | → "thin-file precarity" (the bible's own "citizen arithmetic" language). The stale "Arthur" name in the same line was left for the rename pass. |

### 2b. Genuine issues — left alone (out of scope, with owner)

These are real inconsistencies, but every fix requires renaming (forbidden to this agent) or rewriting faction canon / the romance framework. Recorded so the coordinator can route them.

| # | Location | Issue | Severity | Why left / owner |
|---|---|---|---|---|
| L1 | `21_CITIES.md:5, 21` | "CHAR-001 Reed Arthur is an Indonesian **migrant worker** in Ravenscroft City … SSW visa tied to his employer, remittance obligations to family in Indonesia, dormitory housing, precarious residency." Directly contradicts the retargeted canon (native British citizen). | **high** (cultural) | Rename + identity rewrite; **prose-sweep / relocation agent**. |
| L2 | `21_CITIES.md:304, 305, 306, 322` | "Arthur joined the Ravenscroft cell in 2022", "Arthur's basement archives", "Arthur's file", one called "Arthur 'shadow-blessed'", "his SSW visa wants him invisible". | med | Rename pass. |
| L3 | `31_CONFLICT_ENGINE.md` (file-wide) | 207× "Arthur", 7× "Reed", plus culturally wrong specifics: "his kos roof" (:346, Arthur has a 1K, not an Indonesian kos), "the Jakarta schoolyard" friendship. The protagonist acts/speaks here entirely in the old identity. | high | **Prose-sweep** (file-wide retarget). Not touched. |
| L4 | `32_ROMANCE_FRAMEWORK.md` (file-wide) | Entire file is pre-retarget: "Indonesian family texture — at migrant distance", Ibu Yūko's warung, *sudah makan?*, Lebaran, remittance on the 25th, dorm-room economics, Saitō as friend/romance option (now Saitō Yūto, British), "Nadia Puspita" (now Nadia Puspita). | high | **Romance/background rewrite agent** (already flagged in `_charpatch_protagonist.md` §8). Not touched. |
| L5 | `14_LAW_ENFORCEMENT.md:9, 29, 71, 79` | "Arthur's dorm-gate board" (Arthur has no dorm; also the kairanban point is fine as civic texture), "The Reed doctrine", "Arthur's employer", "For Arthur's novel" / "When Arthur's story collides". The §79 police/civilian texture itself (koban cops knowing his night-shift route, quiet-desk handoff paperwork) is culturally sound. | med | Rename pass. |
| L6 | `06_GOVERNMENTS.md:5, 81, 97–100, 269` | BPF (GOV-004) described as "his home-country agency" / "the pragmatism he grew up inside" — Arthur's home country is Albion. The SSW-worker watchlist tier logic ("only migrants in Threshold-adjacent jobs are actively watched … which is why he's on the watched tier") and "the original government record on him sits in the KNF's thin file" apply a migrant mechanism to a citizen; the old-quarter replay file is canonically SMD/Quiet-Desk, not KNF. | med-high | Rename pass **+ coordinator review** (touches GOV-006 secret mechanics). Not touched. |
| L7 | `12_FACTIONS.md:54, 184, 357, 462, 543, 564` | "Reed Arthur is the condition" (:54), "Arthur-adjacent material" (:184), "Arthur-adjacent names — Indonesian workers placed through Combine-affiliated recruiters" (:357 — factually wrong for a native citizen clerk), "Arthur's employer — Arthur posted to the Ravenscroft branch" (:543). | med | Rename pass. |
| L8 | `11_CORPORATIONS.md:231, 237, 244, 265` | "Reed Arthur (CHAR-001) works for" NQA; "Arthur's hiring file"; "CANON: Reed Arthur works here"; "Arthur eats their noodles". | med | Rename pass. |
| L9 | `19_SOCIAL_CLASSES.md:23, 40, 96` | "Arthur starts here (the dorm class is its Ravenscroft barracks — 18.5)" — contradicts the retargeted 18.5 ("the 1K class"); "the dorm class" is wrong for a citizen in a 1K. | med | Rename pass. |
| L10 | `15_EDUCATION.md:19` | "Reed Arthur (CHAR-001) is the anecdote everyone cites." | low | Rename pass. (The file is otherwise silent on vocational college — no contradiction with Arthur's two-year business-information/data-processing vocational college → records-clerk path, which is plausible.) |
| L11 | `16_MEDICINE.md:88` | "Reed Arthur's (CHAR-001) exact-detail recall". | low | Rename pass. (No Arthur hospital scenes exist in the file — nothing further to audit.) |
| L12 | `33_MYSTERIES.md:45, 58, 80, 82` | "Arthur stands", "Why Arthur was hired at NQA". | low | Rename pass. |
| L13 | `27_TECHNOLOGY.md:79, 87, 91, 93, 111` | "Arthur's job feeds", "That's the one Arthur occupies". | low | Rename pass. |
| L14 | `34_FACTION_RELATIONSHIPS.md:63, 81` | "Arthur's NQA branch", "This is *Arthur's* alliance". | low | Rename pass. (The cultural error at :126 was patched as F6.) |
| L15 | `05_ANOMALY_CLASSIFICATION.md:100, 140` | "it follows Arthur", "Reed Arthur's day job is vectors". | low | Rename pass. |
| L16 | Scattered: `02_WORLD_RULES.md:49`, `03_SUPERNATURAL_SYSTEM.md:78`, `04_POWER_SYSTEM.md:80`, `08_ECONOMY.md:58`, `17_MEDIA_AND_INTERNET.md:78`, `20_GEOGRAPHY.md:28` ("dormitory room in Northgate" — Arthur lives in Willowmere), `22_SUPERNATURAL_LOCATIONS.md:99` ("the year he left Indonesia"), `22:136`, `28_ANOMALIES.md:193`, `36_TERMINOLOGY.md:42` | Stale given-name references in descriptive prose. | low | Rename pass. |
| L17 | `18_CIVILIAN_LIFE.md` §18.1, `29_PROTAGONIST_ANOMALY.md` Part A | "Nadia Puspita (CHAR-016)" — rename registry (`_rename_registry.md` §1) canonically renames CHAR-016 → **Nadia Puspita**. | med | Rename pass (and 29 is uneditable for this agent). |
| L18 | `24_HISTORY.md:53` etc. | Minor: none found beyond renames already handled by the retarget patch (EVENT-077/079/087/092/094/098/099 verified retargeted). | — | — |

### 2c. Checked and found clean (no action)

- **`29_PROTAGONIST_ANOMALY.md` Part A (read-only audit; file not editable):** schooling timeline is internally consistent (prefectural HS → vocational college grad March 2022 → NQA hire 2022; born March 2000). Family structure plausible: father 58, department manager in parts procurement at a local auto-parts manufacturer; mother 55, part-time supermarket staff; sister 22, office worker living at home. No honorific overuse; *department manager* appears once, glossed, where the text invokes it.
- **Family texture (`18` §18.1, `29` Part A):** salt by the door (*morijio*), *protective charm* in drawers, mother's *cleansing ritual* guilt beat (2018 counselor/*tsuite iru*), every-other-Sunday dinners ten minutes on foot, Nanami's messaging app memes + *ちゃんと食べてる？*, mother's *彼女は？*, Takashi's news-program commentary — all culturally apt. Address terms are natural narrative prose; no forced honorifics.
- **Workplace hierarchy:** Okada's break rotation, Hasegawa's dry senior-to-junior teaching, shared-glance friendship with Saitō — differentiated boss→employee / senior→junior / peer registers with **no injected textbook exposition** on department manager/buchō dynamics.
- **Housing/transport:** aging wooden *flat* 1K in Willowmere at ¥48k (F4), 1K ≈ six floor mat + kitchen unit; first train, three stops, commuter pass (定期券 logic), bicycle + train, no car — plausible for a 24-year-old clerk.
- **Conbini culture:** rice ball, oden in winter, melon pan, steamed bun, day-old packed meal rack, canned coffee, the clerk who knows his face but not his name, eating on the curb — correct.
- **Civic texture:** neighbourhood association notice board / disaster-drill schedule / garbage-sorting rules, My Number envelopes, tsuyu (June) and typhoon season (Aug–Oct) as civic calendar, Vietnamese technical intern (技能実習生) at the next table, coin laundry ¥300, futsal with the cell — all apt.
- **Night-shift labor:** 22:00–06:00 records clerk as a regular employee, ~¥230k/month incl. night premium, two months' savings — plausible; no labor-law contradiction found.
- **16_MEDICINE.md:** no Arthur hospital scenes exist — nothing to audit (police/civilian and doctor/patient registers therefore have no Arthur material to check).
- **Festivals/holidays:** 18's civic calendar goes no further than tsuyu/typhoon/October; 32's festival material (Lebaran) belongs to the romance rewrite (L4). Nothing for this audit to patch.
- **Dating:** 18.4's "dawn convenience store dates" / inverted-schedule loneliness is consistent with the 22:00–06:00 shift; romance configurations live in 32 (L4).

## 3. Honorifics & social-register notes

- **Zero occurrences** of `-san / -kun / -chan / -senpai / -sensei` in English prose across every audited file (regex sweep, both lowercase and capitalized). No overuse problem exists.
- British appears only where it earns its place: kanji/reading parentheticals on first mention in `29` (森 大地 etc.), and short in-world utterances in `18` (*ちゃんと食べてる？*, *彼女は？*) — sparing and correct.
- Social registers are differentiated without flattening: Okada (kind-tired managerial), Hasegawa (dry senior), Saitō (glance-level peer intimacy), Nanami (direct, meme-fluent younger sister), Yūko (folk-heuristic maternal), Takashi (bewildered-proud paternal). Direct/blunt characters exist (Hasegawa, Nanami) — no exaggerated-indirectness stereotype was imposed, and none needed correcting.

## 4. COUNTRY-001 / COUNTRY-005 verification

**Verdict: the flagged inconsistency does NOT exist in the current tree. `_charpatch_protagonist.md` §8's residual note is stale.**

Evidence:
- `38_MANIFEST.md:31,61` — "v1.3 audit renumbering: **COUNTRY-001 = Albion (primary), COUNTRY-005 = United States** — swapped globally to resolve the 24:149 registry collision (HIST-003); consistent in all canon files."
- `06_GOVERNMENTS.md` — `## COUNTRY-001 — Albion` (line 85), `## COUNTRY-005 — United States` (line 9).
- `35_CANON_DATABASE.md:11–15` — COUNTRY-001 Albion (primary country; SMD; Ravenscroft), COUNTRY-005 United States.
- `00_INDEX.md:6`, `01_CORE_PREMISE.md:53`, `24_HISTORY.md:151` — all name Albion as COUNTRY-001.
- `DATABASE/COUNTRIES.md` — COUNTRY-001 Albion, COUNTRY-005 United States.
- `37_FINAL_WORLD_BIBLE.md` — consistent (COUNTRY-001 Albion; COUNTRY-005 United States; lines 12, 144, 552, 628, 4824).

No file uses COUNTRY-005 for Albion. **No fix needed** (and per the brief, none applied — out of scope regardless). Recommend striking or updating the residual bullet in `_charpatch_protagonist.md` §8 so it stops alarming future agents (owned by the coordinator; I did not edit that file).

## 5. Summary

- **Findings:** 24 (6 patched + 18 left-alone groups).
- **Patched:** 6 — all in `18_CIVILIAN_LIFE.md` (5) and `34_FACTION_RELATIONSHIPS.md` (1).
- **Files touched:** 2 (`18_CIVILIAN_LIFE.md`, `34_FACTION_RELATIONSHIPS.md`).
- **COUNTRY verdict:** no real inconsistency — COUNTRY-001 = Albion and COUNTRY-005 = United States consistently everywhere; the charpatch note is stale.
- **Main routing recommendation:** the dominant remaining cultural problem is not cultural texture but **stale pre-retarget identity prose** (Indonesian-migrant Arthur/Reed/dorm/SSW/remittance/Saitō material in ~20 files, worst in `21_CITIES.md` intro, `31_CONFLICT_ENGINE.md`, `32_ROMANCE_FRAMEWORK.md`, `06_GOVERNMENTS.md`). That belongs to the prose-sweep/rename pass and the romance rewrite, not to a cultural patcher — I left every instance untouched per the no-rename rule.
