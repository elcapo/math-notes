# Spaced repetition foundations

**Spaced repetition** is a study technique built on the forgetting curve: long-term memory consolidates best when we review material *just before* we are about to forget it. Instead of re-reading notes or revisiting all the material uniformly, an algorithm decides which card to review each day and stretches the intervals as we demonstrate retention.

This produces a compounding effect: the daily cost barely grows even as the body of knowledge expands, because mature cards consume almost no time. Tools like [Anki](https://apps.ankiweb.net/) implement this algorithm and are the de-facto standard, although what matters is not flashcards themselves — it is the spaced-repetition algorithm behind them.

## Four ideas to extract real value

1. **Prioritize principles over isolated facts.** A card that captures the *why* (e.g. the root *ortho-* means "correct/straight") unlocks dozens of derived cases and lets the learner answer questions they have never seen. Memorizing isolated facts blows up the card count without improving understanding.

2. **Do it 100% of days.** It is easier to make spaced repetition a non-negotiable habit — like brushing your teeth — than to decide every morning whether to do it. Skipping a day accumulates debt and discourages returning.

3. **Start small.** Five well-made cards are worth more than a pre-made deck of 50,000 that overwhelms and gets abandoned. A good card forces thinking, not recitation.

4. **If you fall behind, do not add new cards and cap daily reviews.** For example: 100 reviews/day, 0 new cards until you catch up. The alternative — staring at a backlog of thousands — leads to surrender.

## Why "principles, not facts" is the key insight

When several facts share a generative rule, encoding that rule once is dramatically cheaper than encoding each derived fact. The same single principle ("ortho- = correct/straight") explains *orthodontics*, *orthopedics*, *orthography*, *orthodoxy*, *orthoptics*, etc. — and lets the learner solve novel questions they have never specifically studied.

Conversely, if every fact is its own card, the deck grows linearly with content while comprehension stays flat. This is why pre-made decks of 30k–50k cards routinely break learners: each card was authored as an isolated fact, not as a shared principle. Practitioners who study principles-first typically end up with **about half the card count** for an equivalent knowledge base, with better transfer to new problems.

The card-design rule that operationalizes this insight: **if the card can be answered correctly without understanding the underlying concept, it is a bad card**. See `card-design-principles.md` for the full set of rules.

## Why daily consistency compounds

The spaced-repetition algorithm shows a card *the day you are most likely to forget it*. Skipping that day:

- Increases the probability you will forget the card permanently.
- Pushes the card to the next day's queue, doubling tomorrow's load.

Once a habit is "always" rather than "usually", the cognitive overhead disappears. Reviewing on a wedding day or while travelling is no harder than brushing your teeth — provided the deck is built sustainably (small, principle-based) so that daily review takes minutes, not hours.

## The math of compounding

If you make **one new card per day** and review consistently:

| Time | Cards known | Daily reviews |
|---|---|---|
| 7 months | ~210 | ~14 |
| 2.5 years | ~950 | ~17–18 |
| 5 years | ~1,800 | ~25 |

Daily review time stays under 10 minutes for years, because mature cards return at long intervals. Five new cards per day instead of one yields ~10,000 known items in a few years for roughly an hour of daily review.

This compounding only works when:

- The cards encode principles (otherwise they fail repeatedly and never mature).
- The habit is unbroken (otherwise the queue grows faster than retention).

## Reference

- Alec Palmerton, "I Reviewed 28,655 Flashcards Every Day for 17 Years. I Barely Had to Study." YouTube, <https://www.youtube.com/watch?v=7WtznlsP6M8>. The principle-based framing in this skill is largely an applied synthesis of Palmerton's account combined with Wozniak's "20 rules for formulating knowledge".
- Piotr Wozniak, "Effective learning: Twenty rules of formulating knowledge", <https://supermemo.guru/wiki/Twenty_rules_of_formulating_knowledge>.
- Anki Manual, <https://docs.ankiweb.net/>.
