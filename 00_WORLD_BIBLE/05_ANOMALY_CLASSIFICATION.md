# 05 — ANOMALY CLASSIFICATION (The Meridian Vector)

> CANON: Every anomaly handled by a signatory state or the Compact is described in a five-axis **Meridian Vector**. The vector is the hidden world's common language — the thing a Jakarta Sweeper, a Geneva arbitrator, and a reinsurance actuary all mean when they say "we have a problem."

## 5.1 The vector, defined

**Notation:** `MV-[THREAT]/[CONTAINMENT]-[FLAGS]/[RANGE]/[INTEL]`

Example: `MV-T3/C-C/I+R/Urban/Reactive` — a Threat-3 anomaly, contained-at-cost, carrying infohazard and reality-distortion flags, urban in range, reactive but non-sapient.

### Axis 1 — THREAT (T0–T7)

> CANON: Threat uses the same T-scale as Attuned tiers (see [Power System](04_POWER_SYSTEM.md)) — deliberately. It measures **maximum demonstrated output equivalent**: what tier of Attuned would be needed to match what the anomaly just did. It measures output, not malice, not Erosion, not cleverness.

A T1 object that always points north is filed T0 (no meaningful output). A T2 place-seep that rearranges exits is T2. The scale is retrospective and revisable upward — vectors are living documents, re-audited on triggers (see 5.5).

### Axis 2 — CONTAINMENT (A–E)

| Class | Meaning | Typical cost |
|---|---|---|
| **A** | Contained, stable. Passive measures suffice (a vault, a locked room, a warning sign the locals obey). | Negligible |
| **B** | Containable with known active procedures. Routine staffing, scheduled maintenance. | Budgeted |
| **C** | Contained **at cost**. Continuous active intervention: rotating teams, ward maintenance, Stillwater dosing, community management. | Significant, ongoing |
| **D** | Uncontained but **tracked**. Free in the wild; monitored; response on standby. | Surveillance + readiness |
| **E** | Uncontainable by any known means. Mitigation and evacuation only. | Whatever it takes |

> CANON: Containment class is orthogonal to Threat. A T5 can be class A (a city-killer asleep in a vault) and a T1 can be class E (a harmless rumor that cannot be un-known). Budget fights are almost always about the C-class middle: expensive enough to hurt, common enough to multiply.

> CANON (Classification Office policy, **person-bound filings**): where the anomaly is bound to a living person, the containment class describes the *relationship*, not the object — a person cannot be "uncontained," so person-bound anomalies are filed **C-A by default** even when the effort looks D-class (mobile, tracked, response on standby). The Laggard's `C-A` is this policy, not a cover-up: BPF Jakarta files it A, staffs it D, and the file carries a standing 5-year re-audit trigger precisely because the classification and the effort disagree. Auditors are trained to read person-bound C-A as *"contained for now, watched like it's loose"* — the policy's own guidance note. (Old-notation guidance: pre-Compact and pre-1962 files may use the BPF/colonial single-letter notation — treat any single-letter containment grade in an old file as approximate and re-file before citing.)

### Axis 3 — Hazard flags

Flags compose freely. An anomaly can carry none, one, or several.

| Flag | Meaning | Handling consequence |
|---|---|---|
| **I** | **Infohazard.** Knowledge of the anomaly is itself dangerous. | Need-to-know compartmentalization; possession of I-material is a crime in most signatories (see [Law Enforcement](14_LAW_ENFORCEMENT.md)) |
| **B** | **Biohazard.** Affects living tissue / spreads biologically. | Medical-directorate protocols; quarantine authority |
| **P** | **Psychohazard.** Attacks cognition, identity, or sanity without being "information" per se. | Rotation limits for exposed staff; Quiet-care mandatory |
| **R** | **Reality distortion.** Locally rewrites physical law (borrowed matter, causal bubbles, spatial wrongness). | Warded containment required; Lantern survey before approach |
| **M** | **Memetic.** Propagates through imitation, culture, media — behaves like an idea with a Rule. | Memetic-range assessment mandatory; noise-farming countermeasures |
| **V** | **Vector / propagating.** Actively spreads itself (not merely carried). | Highest response priority within its threat band |

> CANON: The **V flag** was added in 2014 after the Ward Six reclassification (see 5.6, case 4). Before that, propagating anomalies were filed under M and consistently under-resourced.

### Axis 4 — RANGE

**Local** (a room, a building, a vehicle) → **Urban** (a city or metro area) → **Regional** (a province, an island group, a river basin) → **Continental** → **Global** → **Memetic** (geography is irrelevant; it moves through information networks).

> CANON: **Memetic** range is not "worse than Global" — it is *differently shaped*. A Memetic-range T2 can be harder to contain than a Continental-range T4, because you cannot evacuate an idea. This is the single most common intuition failure among new analysts.

### Axis 5 — INTEL (None / Reactive / Sapient / Unknown)

- **None:** no detectable response to stimuli. Most object seeps.
- **Reactive:** responds to stimuli in fixed, non-novel ways (the stair counts; the fog arrives on schedule).
- **Sapient:** demonstrates novel problem-solving, communication, or negotiation. Triggers the **Sapient protocols** (2017 Accords): rules of engagement change, the Tribunal's remit extends, and — in one jurisdiction — asylum becomes possible (see [Governments](06_GOVERNMENTS.md), GOV-010).
- **Unknown:** insufficient data. **Treated as Sapient for rules of engagement until disproven** — the Sapient-presumption protocol, adopted after the Oslo case (5.6).

## 5.2 Why classification exists

Classification is not science for science's sake. It is load-bearing infrastructure, and it exists for four buyers:

1. **Resource triage.** Containment capacity is finite: warded vaults, Sweeper teams, Stillwater supplies, Lantern examiners. The vector is the language of the annual budget. A C-class anomaly costs roughly 40× a B-class one; the difference between filing C-B and C-C is a staffing decision with a salary attached. Every misclassification is, downstream, somebody's overtime or somebody's funeral. The corps-level arithmetic — headcount, event volumes, the cost curve, the voted-down funding gap — is tabulated in [26_INFORMATION_CONTROL.md](26_INFORMATION_CONTROL.md) (classified).
2. **Legal triggers.** Accords obligations attach to vector thresholds, not to vibes:

| Threshold | Trigger |
|---|---|
| T3+ or C-D+ | Report to the Compact Classification Office within 72 hours |
| T4+ or Range ≥ Regional | Joint Containment Command placed on standby; Seismograph Authority notified |
| I flag | Infohazard protocols; possession criminalized in signatory law |
| V flag | Response priority within threat band; cross-border notification |
| INTEL: Sapient (or Unknown) | Sapient rules of engagement; Tribunal remit; asylum law engaged |

3. **Insurance.** Quiet Insurance is underwritten on vectors. [Meridian Re](07_INTERNATIONAL_RELATIONS.md) (CORP-004) reinsures on vector bands; a C-class Urban anomaly within 5 km raises commercial premiums measurably. the legacy workplace employer, [Nusantara Quiet Assurance](06_GOVERNMENTS.md) (CORP-011), prices every policy it sells against the national vector register. The vector is, among other things, a price tag.
4. **Jurisdiction.** Vectors decide who leads: below T3/C-C, the national agency; above it, the Compact can assert concurrent jurisdiction; at T4+/Regional+, the [Joint Containment Command](07_INTERNATIONAL_RELATIONS.md) can take command. The [Ledger](07_INTERNATIONAL_RELATIONS.md) requires registration of every anomaly at T2+/C-B+ or higher — which makes the vector also a property deed.

## 5.3 Who controls it

> CANON: The **Classification Office** of the [Meridian Compact](07_INTERNATIONAL_RELATIONS.md) (Geneva) owns the standard: it defines the axes, ratifies vectors, and hears appeals. It does not do field classification.

Field classification works in three stages:

1. **Provisional (field team, 24 hours).** The responding Sweeper team files a provisional vector. It is valid for 30 days and carries legal force — which is why field teams are trained to file *up*, not down: over-classification wastes money; under-classification kills people.
2. **National mirror (7 days).** Each signatory's agency runs a classification bureau (the BTA's Office of Threshold Taxonomy, the Jade Office's Classification Section, the BPF's… two overworked analysts in Jakarta) that confirms or amends.
3. **Compact ratification (30 days).** The Classification Office ratifies, amends, or remands. Its decisions are binding on signatories and appealable only to the Compact Arbitration Court — a process that takes years, during which the amended vector stands.

**The structural tension:** states systematically **under-classify** to avoid reporting obligations (sovereignty cost, Compact oversight) and systematically **over-classify** when they want to seize an asset (a T4/C-D filing justifies seizure without compensation in most jurisdictions). The Classification Office exists largely to arbitrate these two opposite lies. Its auditors are the most hated and most necessary people in the hidden world.

## 5.4 How vectors are born, live, and die

- **Birth:** provisional filing within 24h of first response.
- **Re-audit triggers (mandatory):** any new behavior outside the filed Rule description; any range expansion; any intel upgrade (Reactive → Sapient); any cross-substrate discovery (a Place Seep found to have an Information component); every 5 years for C-class and above.
- **Death:** decommissioning (the seep's Rule ends — rare, usually by Drowning of a bound Attuned or destruction of the substrate) or reclassification to T0/C-A (dormant). Decommissioned vectors are archived, never deleted — the Compact has never once been embarrassed by keeping an old file.

## 5.5 Worked examples

All anomalies below are catalogued in [28_ANOMALIES.md](28_ANOMALIES.md) (Drafter C). Vectors shown are Compact-ratified unless noted.

1. **ANOMALY-001 "The Laggard"** — `MV-T1/C-A/—/Local/Unknown`
   *A second shadow lagging ~3 seconds. Passive containment (it follows Arthur). INTEL: Unknown — it has never responded to stimuli, but no examiner will certify None. Filed by BPF Jakarta; the Unknown flag is why the file stays open.* (Full profile: [29_PROTAGONIST_ANOMALY.md](29_PROTAGONIST_ANOMALY.md).)
2. **ANOMALY-004 "The Counting Stair"** — `MV-T1/C-B/—/Local/Reactive`
   *Textbook B-class: a stairwell with a counting Rule, managed by a posted schedule and a part-time attendant. The kind of file that makes auditors weep with joy. The stair counts *back* — hence Reactive, corrected from an earlier None filing per the field catalog.*
3. **ANOMALY-006 "The Thursday Rain"** — `MV-T3/C-C/R/Regional/Reactive`
   *Upward rain, third Thursdays, three provinces. C-class because containment means regional weather-service coordination and road closures nine days a year, forever.*
4. **ANOMALY-007 "The Ward Six Lullaby"** — `MV-T4/C-D/I+M+V/Memetic/Reactive`
   *The case that created the V flag and the Memetic range (see 5.6). A melody that propagates itself and degrades the singer's memory of having sung it. Currently D-class: it is in the wild, in sampled form, in at least eleven tracks. The Compact's audio-fingerprint program is the containment.*
5. **ANOMALY-012 "The Static Saint"** — `MV-T5/C-D/I+M/Memetic/Sapient`
   *An information-seep with a congregation. Sapient, memetic, uncontained. The file is I-flagged; this paragraph is the most this bible says about it.*
6. **ANOMALY-013 "The Salt Garden"** — `MV-T4/C-B/R/Urban/Reactive`
   *High threat, low containment cost: the garden's Rule is geographically fixed and legible. The lesson auditors cite — threat and containment are orthogonal.*
7. **ANOMALY-020 "The Bell That Rings Backwards"** — `MV-T4/C-C/R+P/Urban/Reactive`
   *C-class because the P flag requires rotation limits: no examiner works the bell more than two sessions per quarter. Staffing cost, not heroics.*
8. **ANOMALY-025 "Bus 12"** — `MV-T3/C-D/—/Urban/Reactive`
   *A moving place-seep. D-class because you cannot ward a bus route without the city noticing, and the Veil only covers so much. Tracked by transit cameras and two Lanterns on rotating shifts.*
9. **ANOMALY-029 "The Well at the End of the Map"** — `MV-T6/C-E/R/Regional/Unknown`
   *One of the few E-class filings on earth. No known containment; mitigation is evacuation planning and a permanent JCC watch. INTEL: Unknown — and under the Sapient-presumption protocol, approached as Sapient.*
10. **ANOMALY-030 "The Second Silence Archive"** — `MV-T5/C-C/I/Memetic/Sapient`
    *Contained at cost: the archive is cooperative (Sapient) but I-flagged, so every researcher is compartmentalized, examined, and rotated. The most expensive library card in history.*

## 5.6 How classification goes wrong (case studies)

> CANON: The Classification Office publishes a redacted *Misclassification Review* every five years. The following are the most-cited entries. Competence is distributed (see [World Rules](02_WORLD_RULES.md)) — these were not stupid people. They were people with incentives, deadlines, and incomplete data, which is worse.

**Case 1 — Under-classification: the Surabaya Ledger (CASE-006).**
In 2017 a BPF field team filed a market place-seep in Surabaya as `MV-T1/C-A`: stalls whose goods rearranged overnight, a nuisance. It was actually an **Information Seep** riding the market's credit-ledger software — every bookkeeping file that recorded the rearranged inventory carried a fragment of the Rule, and the fragments propagated through accounting software across Java. Fourteen people died when a warehouse's inventory system "reconciled" its human staff. Re-audit put it at `MV-T3/C-C/I+V/Regional/Reactive`. Consequences: the BPF's regional budget was cut 30% (punishing the underfunded for being underfunded — the Office's critics still cite this), the classification chief resigned, and the **cross-substrate rule** was adopted: any C-flagged Place Seep with a transactional substrate gets automatic Information-component review. Director-General Ratna Kusuma (CHAR-005) still opens budget meetings with the Surabaya slide.

**Case 2 — Over-classification as seizure: Halvorsen v. BTA (CASE-001).**
In 1992 the BTA filed a Minnesota family's inherited Object Seep — a teacup that refilled with lukewarm tea, genuinely `MV-T1/C-A` — as `MV-T4/C-D`, justifying warrantless seizure under emergency powers. The family sued. Nine years of litigation established that (a) the BTA had no evidence for the T4 filing, (b) the filing officer's emails showed budget-justification motives, and (c) the teacup was, in the court's words, "a teacup." Consequences: the **Classification Appeals Panel** (any owner can challenge a vector within 90 days), mandatory evidence standards for filings above T2, and $4.1M in damages. Every BTA classifier is still shown the teacup's file on their first day. The lesson the Compact draws: *over-classification is also a lie, and lies compound.*

**Case 3 — INTEL misclassification: the Oslo Underpass (1988).**
A place-seep under Oslo's central station was filed `Reactive`: signage that changed to direct pedestrians away from maintenance areas. For six years the containment team treated signage changes as hazard escalation and responded with ward-burns — aggressive suppression. In 1992 a Lantern examiner proved the signage had been **negotiating**: it was trying to establish a schedule, and the ward-burns read as attacks. It retaliated. The underpass was lost; three staff Drowned; the site is now `MV-T4/C-E/R/Urban/Sapient` and a permanent exclusion zone. Consequences: the **Sapient-presumption protocol** — INTEL:Unknown is approached as Sapient until disproven — and the standing rule that *no suppression action is taken against an INTEL:Unknown anomaly without a Lantern examiner's sign-off.* The Oslo file is why "Unknown" exists as a category at all.

**Case 4 — RANGE misclassification: the Ward Six Lullaby (ANOMALY-007).**
Filed in 2007 as `MV-T3/C-C/I/Urban/Reactive`: a hospital-lullaby infohazard, contained to one city's care homes. In 2012 a Lantern examiner recognized the melody — sampled, pitch-shifted — in a charting pop song. It had been propagating through audio for five years. Reclassification to `MV-T4/C-D/I+M+V/Memetic/Reactive` required inventing two new pieces of the standard: the **V flag** and the **Memetic range**. Consequences: the Compact's audio-fingerprint screening program, mandatory M-flag review for all I-flag filings, and the auditors' proverb: *"Urban is a hope, not a measurement."*

## 5.7 What the vector doesn't capture (known gaps)

> STATUS: THEORY (Classification Office internal position, 2022 review): the vector underweights **interaction effects** — two T2s whose Rules interfere can produce T4 consequences (see [Power System](04_POWER_SYSTEM.md) on Rule interference). A composite-vector proposal has been tabled three times and defeated three times, each time on cost grounds: the current system is wrong in known ways, and everyone prefers known wrong to unknown expensive.

> CANON: [LEGACY / PRE-ACADEMY] Arthur Reed's day job was vectors. As a records clerk at Nusantara Quiet Assurance, he files, cross-references, and redacts Meridian Vectors all night. He knows the system the way a bank clerk knows money: intimately, cynically, and from the paperwork side. This is why he survives later — he has read ten thousand vectors, and he knows exactly what a wrong one looks like.

