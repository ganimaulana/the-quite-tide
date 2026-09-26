# 39 â€” CONTRACT SYSTEM

> **STATUS: AUTHOR-LOCKED â€” 2026-09-25**
> This file defines Arthur's exclusive Contract System and its private Contract UI/interface. The UI is the visible interface; the Contract System is the underlying mechanism. This file does not replace individual Contract rules, the Uncarved Seal, the Academy assessment system, or the existing ERROR/UNDEFINED classification. Individual Contract files remain authoritative for their actual mechanics.

## 39.1 Purpose

The Contract System is an **exclusive Contract mechanism**, and its UI is a **minimal information interface**. Neither is a character-statistics system or an independent power system.

The UI's purpose is to let Arthur see a small amount of structured Contract information that would otherwise be difficult to carry naturally through combat, training, examinations, survival situations, and ordinary movement.

The UI therefore reports **basic identity, basic skills, Contract terms, integration state, and discovered Contract conditions**. It does not turn Arthur into an RPG character sheet.

### Exclusive-access rule

The Contract System belongs to Arthur alone.

- No other person can perceive Arthur's private Contract UI.
- No other person can activate, inherit, copy, steal, or independently reproduce the Contract System.
- Other people may possess natural abilities and may interact with Arthur's Contracts in the ordinary world, but they do not gain access to the interface.
- Arthur may not initially know whether the Contract System is unique to him; the exclusivity is an objective canon rule, not necessarily his first assumption.

> **LOCKED PRINCIPLE:** The UI tells Arthur what he has been given or what has been verified. It does not tell him everything he can do with it.

---

## 39.2 Natural Skills vs Contract Skills

Arthur's ordinary/natural abilities and Contract-derived abilities must remain visibly distinct.

### Natural Skill presentation

Natural skills are listed briefly and descriptively. No numerical attributes are required.

Example:

```text
ARTHUR REED

Age: 18

Skills:

â€¢ Motion Sense
  1. Reads the movement of nearby people.
  2. Reads the movement of objects.
```

The UI must **not** display STR, DEX, INT, HP, MP, stamina values, power scores, combat ratings, stat points, levels, or equivalent numerical character attributes.

The exact age, academy identity, and other basic identity fields remain governed by the active Academy character canon; the example above is interface grammar only where it conflicts with no active canon.

### Contract Skill presentation

Contract abilities are presented as **rules with conditions and consequences**, not as ordinary skills.

The distinction is load-bearing:

> **Natural skill = capability.**
>
> **Contract skill = capability bound to a ruleset.**

Every Contract therefore has a meaningful possibility of restriction, cost, consequence, or uncertainty.

---

## 39.3 Contract Discovery / Offer

A new Contract may become available when an independent in-world trigger is satisfied. The UI does not provide a shopping menu and does not preview future Contracts.

The offer is intentionally incomplete.

Canonical presentation grammar:

```text
NEW CONTRACT SKILL AVAILABLE

LUGH

A contract derived from Lugh,
the legendary warrior associated with
the mastery of 999 weapons.

Integration parameters are unknown.

WARNING:
The benefits, restrictions, and consequences
of this Contract may not be fully known before
acceptance.

Unknown consequences may exist.

Accept the contract?

[ ACCEPT ]   [ DECmessaging app ]
```

### Warning rule

The warning is **mandatory for a new Contract whose consequences are not fully settled or known**.

It exists to establish the system's core risk before Arthur makes his decision.

The warning must not explain the hidden consequence. It only establishes that the information available to Arthur is incomplete.

The UI may state that a consequence is **UNKNOWN**. It may not invent a consequence merely to make the acceptance dramatic.

### Randomness rule

Contract consequences may be **random from Arthur's perspective**, but they are not arbitrary from the world's underlying rules.

> **Random to the holder does not mean random to the system.**

The eventual consequence must remain consistent with the Contract's underlying logic and may be discoverable through later observation and testing.

---

## 39.4 Acceptance and Integration

After acceptance, the UI reports only what has actually been settled or verified.

Integration is not required to have one universal form. A Contract may be:

- **Temporary Integration** â€” usable only for a bounded period or condition.
- **Partial Integration** â€” only part of the Contract's possible terms are settled or accessible.
- **Upgradeable Integration** â€” the Contract has a discoverable development path.
- **Full Integration** â€” the settled Contract is fully available under its known terms.

These labels describe the state of Arthur's relationship with the Contract. They do not constitute power levels.

### Active Contract slots

Arthur has a hard maximum of **6 active Contract slots**.

- Slot expansion is not a normal progression mechanic.
- Acquiring a Contract does not create a permanent new slot.
- A previously occupied slot may eventually be cleared so another acquired Contract can be installed.
- Clearing a slot does **not** automatically erase or destroy the underlying Contract.
- The Contract's own rules govern whether and how a cleared Contract can be installed again.

The UI may display slot occupancy when relevant, but slots are not generic inventory or skill points.

Example:

```text
CONTRACT ACCEPTED

â€¢ Lugh Seal

  +
  Amplifies weapon performance.
  2Ã— amplification for 10 minutes.

  âˆ’
  Exceeding the active limit causes
  severe physical pain and loss of control.

  Integration:
  Partial
```

The exact mechanics of a real Contract always come from that Contract's canonical file. The Lugh example is interface grammar and does not, by itself, override Contract #2's locked mechanics.

---

## 39.5 Unknown Consequences

Unknown consequences are a deliberate part of Contract risk.

The UI must distinguish:

| State | Meaning |
|---|---|
| **KNOWN** | Verified and settled by the Contract/system evidence available to Arthur |
| **PARTIALLY KNOWN** | Some terms are verified; meaningful gaps remain |
| **UNKNOWN** | Arthur has insufficient information to determine the consequence |
| **UNRESOLVED** | A specific question remains open and may require further testing |

The UI must never silently convert UNKNOWN into a harmless assumption.

This is why Arthur can be cautious about accepting a Contract even when its visible benefit appears attractive.

---

## 39.6 Contract Development / Upgrade Triggers

Contracts do not use conventional character leveling.

However, a Contract can expose a **development path** after Arthur has demonstrated sufficient understanding, usage, or mastery of the Contract's rules.

The trigger is discovered; it is not guaranteed to appear merely because Arthur uses the Contract many times.

When a valid development path is discovered, the UI may reveal a concrete requirement.

Example:

```text
CONTRACT UPDATE

Lugh Seal

A new integration path has been discovered.

Upgrade Requirement:

Defeat 100 different opponents
using Lugh Seal.

Progress:
0 / 100
```

This count is a **Contract-specific condition**, not XP, a level, or a general progression meter.

### Requirement interpretation

Contract requirements must be interpreted according to their actual wording and underlying rule.

If a requirement says:

> **Defeat 100 different opponents**

then Arthur may test what qualifies as an "opponent."

Depending on the Contract's actual rule, valid instances might include:

- monsters;
- hostile humans;
- formal challengers;
- legitimate training opponents;
- other qualifying combatants.

The system must determine eligibility consistently. Arthur may discover that the literal wording is broader or narrower than his initial assumption.

This creates a legitimate **loophole-discovery** layer without allowing arbitrary cheating.

### Anti-farming rule

Repeatedly performing the same action must not automatically satisfy a requirement if the requirement contains a meaningful distinction such as "different," "firsthand," "genuine," or another qualifying condition.

The Contract's rule determines validity. Arthur's cleverness lies in discovering the boundary, not in persuading the system to ignore it.

---

## 39.7 Contract-Specific Development Paths

Every Contract may have a different method of development. There is no universal upgrade formula.

Possible development classes include:

1. **Challenge** â€” defeating or overcoming a defined opponent or situation.
2. **Mastery** â€” demonstrating deeper understanding of the Contract's rule.
3. **Ritual** â€” completing a specific sequence under defined conditions.
4. **Sacrifice** â€” surrendering something meaningful under the Contract's logic.
5. **Restriction** â€” succeeding while voluntarily limiting an available option.
6. **Discovery** â€” identifying a hidden rule or exception through testing.
7. **Choice** â€” making a decision that satisfies the Contract's underlying principle.
8. **Interaction** â€” discovering a valid interaction with another rule, medium, or Contract.

These are categories, not a mandatory checklist. A Contract may use one, several, or an unusual condition not represented here.

### Design rule

> **Different Contracts should demand different kinds of understanding.**

If every Contract upgrades through killing enemies, the system becomes a grind loop. The development condition must express something about the identity or ruleset of that Contract.

---

## 39.8 The Contract Does Not Necessarily "Level Up"

The UI may use the word **UPDATE**, **DEVELOPMENT**, **NEW INTEGRATION PATH**, or another neutral system term.

It must not imply that the Contract is an RPG object gaining arbitrary numerical levels.

The preferred progression model is:

```text
DISCOVERY
   â†“
ACCEPTANCE
   â†“
INTEGRATION
   â†“
USE
   â†“
OBSERVATION
   â†“
UNDERSTANDING
   â†“
TRIGGER DISCOVERED
   â†“
REQUIREMENT REVEALED
   â†“
CONDITION FULFILLED
   â†“
NEW INTEGRATION / DEVELOPMENT
```

The apparent "upgrade" is therefore earned through interaction with the Contract's rules.

---

## 39.9 Loophole Discovery

Loopholes are permitted only when they arise from a real ambiguity, boundary, or interaction in the Contract's wording and mechanics.

Example:

```text
Lugh Seal:
2Ã— weapon amplification for 10 minutes.
```

If the actual settled rule applies the ten-minute limit to the **currently selected weapon**, switching from sword â†’ spear may establish a new active weapon state.

That is not a free power-up. It is a discovery about the scope of the original condition.

The resulting advantage is therefore:

> **better interpretation, not arbitrary system generosity.**

Loopholes must remain bounded by:

- the actual Contract wording;
- the underlying phenomenon/Grantor rule;
- physical availability;
- tactical constraints;
- consequences;
- and any later-discovered restrictions.

---

## 39.10 UI Information Ceiling

The UI is intentionally shallow.

It should generally report:

- identity;
- age/basic identity fields;
- natural skill names and basic functions;
- Contract names;
- known positive effects;
- known restrictions/consequences;
- integration state;
- discovered development triggers;
- concrete Contract-specific requirements;
- requirement progress where a requirement itself contains a count.

It should not report:

- power scores;
- character attributes;
- combat ratings;
- HP/MP/stamina bars;
- generic EXP;
- character levels;
- rarity tiers;
- universal skill points;
- generalized damage numbers;
- hidden future Contracts;
- optimal strategies;
- unexplained success guarantees.

The UI is an **interface**, not the narrator and not a game master.

---

## 39.11 Relationship to the Academy ERROR

The UI must not be the explanation for Arthur's Academy ERROR/UNDEFINED result.

The Academy assessment and the private Contract/UI layer are separate systems.

The current canon remains:

- Arthur has no conventional Esper pattern;
- the assessment's ERROR/UNDEFINED result is not a secret power rank;
- Contract possession does not move his Rank or conventional Esper classification;
- the UI is private and does not make the Academy's instruments omniscient.

The UI may first become perceptible to Arthur **after the entrance assessment**, including after the ERROR event, without implying that the UI caused the ERROR.

This separation is mandatory.

---

## 39.12 Recommended First-Exposure Timing

**Recommended canon staging:**

1. **Entrance assessment first.** Arthur is evaluated normally.
2. **ERROR/UNDEFINED occurs.** The institutional system fails to classify him correctly/completely, while the result remains valid on its own terms.
3. **Private UI manifests.** The UI is a separate, personal phenomenon and is not visible to the Academy.
4. **The first UI exposure does not automatically grant a Contract.** The interface can exist while Arthur has no active Contract.
5. **The first Contract offer requires its own in-world trigger.** Contract availability is never caused merely by the UI being present.

This preserves the mystery around the ERROR while giving the UI a strong narrative relationship to the moment Arthur realizes that the institutional system cannot fully describe what is happening to him.

### Why the Academy result and Contract UI remain separate

If the UI explains the test result, readers may reasonably infer that the Contract System is the cause of the ERROR. That collapses two mysteries into one and weakens the institutional tension.

Keeping the assessment and UI as separate layers gives us:

> **Institution says: ERROR.**
>
> **Private system says: something else exists.**

Neither side completely explains the other.

That is stronger mystery architecture.

---

## 39.13 Lugh Placement Guardrail

The **Lugh** example is compatible with the current Weapon Contract architecture, but this file does **not** rename or replace Contract #1.

Current contract order remains:

1. **THE POLITE KNOCK** â€” Contract #1, locked.
2. **Weapon Amplification / Mastery Contract** â€” Contract #2 functional identity, locked.

If the author later adopts **Lugh** as the formal identity/name of Contract #2, the Contract #2 file must be updated as the authoritative mechanics source. This UI file then supplies only the presentation grammar.

The UI itself must never silently turn an illustrative example into canon.

---

## 39.14 Core Design Laws

1. **No stats.** The UI does not quantify Arthur as an RPG character.
2. **Contracts have consequences.** A visible benefit never implies a consequence-free acquisition.
3. **Unknown is allowed.** The UI can explicitly admit incomplete knowledge.
4. **Warning before acceptance.** Unknown or incompletely settled consequences must be disclosed as unknown before Arthur accepts.
5. **Random-to-Arthur is not arbitrary.** Consequences remain rule-consistent.
6. **Development is Contract-specific.** No universal leveling recipe exists.
7. **Requirements can be exploited intelligently.** Literal wording and boundary conditions can be tested.
8. **Loopholes must be earned by interpretation.** The UI does not grant loopholes; Arthur discovers them.
9. **Progress counts are local.** A count such as `37/100` belongs only to that specific Contract requirement; it is never general XP.
10. **The UI does not explain mysteries it cannot know.** Unknown remains unknown until legitimately discovered.
11. **The Academy cannot see the private UI.** Institutional assessment and Contract/UI information remain separate layers.
12. **The UI never replaces prose.** The reader learns what the Contract means through events, tests, consequences, and Arthur's reasoning.

---

## 39.15 Authorial Intent

The intended reader experience is:

> **"What did Arthur get?"**
>
> **"What does it actually cost?"**
>
> **"What does the wording really mean?"**
>
> **"What happens if he tests the boundary?"**
>
> **"What did he discover that the system never told him?"**

The system should reward **attention, experimentation, caution, and interpretation**, not grinding.

The defining progression principle is:

> **Arthur does not become stronger because the UI gives him higher numbers. He becomes more dangerous because he learns how to use the rules better than people who only see the surface.**

