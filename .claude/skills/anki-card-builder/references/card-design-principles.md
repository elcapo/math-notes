# Card design principles

An applied synthesis of Piotr Wozniak's "20 rules for formulating knowledge" (creator of SuperMemo) and the practice of encoding **principles** rather than facts described in `spaced-repetition-foundations.md`.

## The golden rule

> If the card can be answered correctly without understanding the underlying concept, it is a bad card.

Every card must force the learner to **derive, transfer, or apply** a principle. Memorizing the literal answer without comprehension is equivalent to not having studied at all.

## 1. Understand before memorizing

Never create a card on material the learner does not understand. Memorizing without comprehension produces cards that are chronically failed and erode motivation. When the material is confusing, study it first, then distill it.

**Bad**: copying a technical paragraph onto the back of the card exactly as it appears in the textbook.
**Good**: explaining the principle in one's own words, and creating a card that applies it.

## 2. Encode the principle, not the fact

When several facts share a generative rule, create a card about the rule (plus optional application cards), not one card per fact.

**Bad** (3 cards, 3 facts):

```
orthodoxy → traditional belief
orthopedics → bone medicine
orthodontics → straightening teeth
```

**Good** (1 card for the principle + application cards solved by the principle):

```
Front: What does the Greek root "ortho-" mean?
Back: Correct, straight, right.

Front: Knowing that "ortho-" = straight and "doxa" = belief, what is orthodoxy?
Back: A "straight"/correct belief — the traditionally accepted position.
```

The second card also works for *orthography*, *orthoptics*, *orthodontics*, etc. — the principle transfers.

## 3. Minimum-information principle

Every card must ask **one atomic thing**. The smaller the card, the easier it is to learn, recall, and maintain.

Atomicity composes with rule 2 — it is *orthogonal*, not in tension. Atomicity governs the **shape** of the card (one question, one answer); principle-encoding governs the **content** of that one thing (a transferable rule, not a dead fact). The target is *atomic principle-application cards*, not atomic trivia. A principle does not live inside a single dense card; it lives **distributed across N atomic cards** that exercise it from different angles.

**Bad** (one dump card, also fact-based):

```
Front: Greek/Latin roots in medical terminology.
Back: "cardio-" = heart, "-itis" = inflammation, "-logy" = study, "-ectomy" = removal,
      "hepato-" = liver, "neuro-" = nerve, "-pathy" = disease...
```

**Good** (atomic cards, each one applies a compositional principle):

```
Knowing "-itis" = inflammation, what does hepatitis affect? → The liver (from "hepato-").
Knowing "-ectomy" = surgical removal, what is an appendectomy? → Removal of the appendix.
Knowing "neuro-" = nerve and "-pathy" = disease, what is a neuropathy? → A disease of the nerves.
```

Each card is atomic (one question, one answer) **and** transferable: the same roots unlock *gastritis*, *nephrology*, *cardiectomy*, *neuropathy*, etc. without ever having seen those words specifically.

Compare the failure mode of trivia atomization:

```
How many chambers does the heart have? → 4
Approximate weight of the adult heart? → 250–350 g
```

These are atomic but inert — they do not generalize, they fail to cue applied reasoning, and they are exactly the brittle facts that bloat decks to 50,000 cards. If a card cannot be reframed to apply a principle, ask whether it deserves to exist at all.

## 4. Avoid large enumerations

Lists of more than ~5 items memorized as a single block are fragile: forgetting one fails the entire card. Strategies:

- **Mnemonics**: turn the list into an acronym or phrase. "MRS GREN" for the characteristics of living things (Movement, Respiration, Sensitivity, Growth, Reproduction, Excretion, Nutrition).
- **Partial Cloze**: use Cloze to hide one element at a time, keeping the rest visible as context.
- **Split**: convert into N independent cards with the question framed by position or role.

Partial-Cloze example:

```
Notetype: Cloze
Text: The taxonomic kingdoms are: {{c1::Animalia}}, {{c2::Plantae}}, {{c3::Fungi}}, {{c4::Protista}}, {{c5::Monera}}.
```

Generates 5 cards, each hiding only one item.

## 5. Fight interference with explicit contrast

When two concepts are frequently confused (afferent/efferent, mitosis/meiosis, rate/ratio), create a card that **directly contrasts** them, not one card per concept.

```
Front: Difference between rate and ratio in statistics.
Back: Rate = events per unit of time (incidence, velocity). Ratio = dimensionless proportion between two comparable quantities.
```

## 6. Use Cloze to preserve context

When the answer only makes sense inside its sentence, use Cloze. The full sentence stays on screen; only the key segment is hidden.

```
Notetype: Cloze
Text: Caffeine crosses the {{c1::blood–brain barrier}} because it is {{c2::lipophilic}}, which also explains why it can be absorbed via the {{c3::transdermal}} route.
```

3 cards, same context, each one asking about a different piece of the principle.

## 7. Hints that don't give the answer away

Hints help guide retrieval but must not reveal the answer. The syntax `{{c1::text::hint}}` shows the hint while the field is hidden.

```
{{c1::glucose::6-carbon sugar}}
```

## 8. A picture is worth a thousand words

For anatomy, maps, schematics, graphs, molecular structures: use images. Anki accepts `<img src="...">`. Visual memory is more durable than verbal memory for spatial content.

## 9. Personalize the material

Cards written by the learner are learned ~3× faster than pre-made decks. Elaboration (paraphrasing, integrating with prior knowledge, giving one's own examples) generates stronger memory traces.

When the user supplies material, **distill and rephrase it**, do not copy it verbatim.

## 10. Sources and references

Include a `Source` field (book page, URL, lesson number). When a card starts to fail chronically, being able to return to the source for context prevents blind memorization.

Recommended note type template:

| Field | Use |
|---|---|
| Front | Question that forces application of the principle |
| Back | Atomic answer |
| Extra | Explanation of the principle, mnemonic, related cases |
| Source | Reference to the original source |
| Tags | Topic, difficulty, date, conceptual deck |

## 11. Controlled redundancy

Create several cards that target the same principle from **different angles** (definition → example, example → definition, contrast, application to a new case). This reinforces the semantic network.

**Do not** create literal duplicates: the same question twice adds zero value.

## 12. Atomize before memorizing

When in doubt between creating 1 complex card or 3 simple ones, 3 simple is almost always the better choice. The cost of reviewing 3 atomic cards over years is lower than the cost of repeatedly failing 1 dense card.

## Anti-patterns (what NOT to do)

### Dump cards

Pasting a slide, paragraph, or full list. The card must be answerable in seconds. If the back fills half the screen, split it.

### Circular definitions

```
Front: What is entropy?
Back: A measure of the disorder of a system.
Front: What is the disorder of a system?
Back: Its entropy.
```

Break the loop with an application: "If I leave an ice cube in a room, does total entropy increase or decrease? Why?".

### Questions without context

```
Front: What is the value?
Back: 42.
```

Useless outside the session in which it was created. Every card must be self-sufficient.

### Hints that give the answer away

```
Front: The capital of France, a European city with the Eiffel Tower...
Back: Paris.
```

The front contains the answer. Rephrase without hints, or use Cloze.

### Mixing several principles in one card

```
Front: Explain photosynthesis, cellular respiration, and fermentation.
Back: [3 paragraphs]
```

These are three distinct cards, each with its own principle.

### Sets memorized as a block

```
Front: List the 12 cranial nerves in order.
Back: I olfactory, II optic, III oculomotor, ...
```

Forgetting one fails the whole card. Split or use mnemonic + partial Cloze.

## When to split vs. merge cards

**Split** a card when:

- The back is longer than ~3 lines.
- A conjunction is being memorized ("and", "also", "in addition").
- Only one part is failed repeatedly.

**Merge** two cards when:

- They are the same idea expressed with slight variation.
- One question is trivially derivable from the other.

## Final per-card checklist

- [ ] Does it test a principle, or an isolated fact?
- [ ] Does it make sense out of context?
- [ ] Does it carry one atomic idea?
- [ ] Does it force thinking (the front does not give the answer away)?
- [ ] Is the back short and specific?
- [ ] Is it linked to a source?
- [ ] If Cloze: does the context really matter for the answer?
