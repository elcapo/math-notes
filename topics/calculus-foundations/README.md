# Calculus foundations

Vocabulary and intuition every later calculus topic rests on: what a function is, how to classify it (as injective, surjective, or bijective), composition, and inverse.

## Status

`[~]` in progress — functions block covered (with cards in active rotation); function-families block (graph ↔ formula) under way, no cards yet; algebra and trigonometry blocks from material 01 still pending.

## Materials

| # | Source | Topic |
|---|--------|-------|
| 01 | [The Language of Calculus I Wish I Had Learned First](https://www.youtube.com/watch?v=MaszunEszVM) | Functions, injectivity, surjectivity, bijectivity |

## Cards

- [`cards/calculus-foundations.txt`](../../cards/calculus-foundations.txt) — 9 cards covering the functions block (definition, dom/codom, injectivity/surjectivity independence, invertibility characterization, domain restriction, arcsin principal branch, composition non-commutativity, composition compatibility, inverse via composition).

## Theory

What follows is the settled prose version of what was worked out in conversation while studying the materials. The cards test the same content from different angles; this section is for re-reading before review.

### 1. What a function is

A function is a rule that assigns to **each** input **exactly one** output. The "exactly one" is the load-bearing part and combines two requirements:

- **Determinism** — the same input always produces the same output. A coin-tossing machine that maps an integer to $0$ or $1$ based on a flip is *not* a function, because feeding it the same integer twice may yield different outputs.
- **Uniqueness** — only one output per input, never several at once.

A relation that violates either property is not a function, even if it appears to "depend on" the input in some loose sense.

### 2. A function is rule + domain + codomain

The formula alone does not specify a function. The full data of a function is:

- a **domain** $A$ — the set of legal inputs;
- a **codomain** $B$ — the set of conceivable outputs;
- a **rule** that, for each $x \in A$, designates a unique $f(x) \in B$.

Notation: $f: A \to B$. Two functions with the same rule but different domain or codomain are *different functions*. For example, all of these obey $f(x) = x^2$ but are not the same:

| Function | Properties |
|----------|------------|
| $f: \mathbb{R} \to \mathbb{R}$ | not injective, not surjective |
| $f: \mathbb{R} \to [0, \infty)$ | not injective, surjective |
| $f: [0, \infty) \to \mathbb{R}$ | injective, not surjective |
| $f: [0, \infty) \to [0, \infty)$ | bijective (invertible) |

### 3. Injectivity, surjectivity, bijectivity

Given $f: A \to B$:

- **Injective** (one-to-one): different inputs go to different outputs. Formally, $f(x_1) = f(x_2) \implies x_1 = x_2$.
- **Surjective** (onto): every element of the codomain is hit by some input. Formally, for every $y \in B$ there is some $x \in A$ with $f(x) = y$.
- **Bijective**: both injective and surjective.

The two properties are **independent**: each can hold or fail without forcing the other (see the table above — all four cells are realizable by $x^2$ with the right (co)domain choice). Tightening the domain affects injectivity; tightening the codomain affects surjectivity.

### 4. When $f$ has an inverse that is itself a function

$f: A \to B$ has an inverse function $f^{-1}: B \to A$ **if and only if $f$ is bijective**. The two halves of "bijective" each preserve a different requirement of "being a function" in the inverse:

- **Injectivity of $f$** $\implies$ **uniqueness in $f^{-1}$**. Each $y \in B$ is the image of at most one $x$, so $f^{-1}(y)$ is well-defined as a single value rather than a set.
- **Surjectivity of $f$** $\implies$ **totality of $f^{-1}$**. Every $y \in B$ is the image of at least one $x$, so $f^{-1}$ is defined on the whole codomain $B$, not just part of it.

Drop either half and $f^{-1}$ ceases to be a function.

### 5. Restricting the domain to force invertibility

Many natural rules are not injective on their full domain ($x^2$, $\sin x$, …). The standard technique to recover invertibility is to **restrict the domain to an interval where the function is strictly monotonic**:

- **Strict monotonicity** (strictly increasing or strictly decreasing) implies injectivity for free.
- The interval should be **closed at the endpoints where the function reaches the extremes of its codomain**, so that surjectivity onto the chosen codomain is preserved.

**Worked case — $\arcsin$**. The function $\sin: \mathbb{R} \to [-1, 1]$ is surjective but very far from injective. To define an inverse, restrict to a maximal monotonic interval. The standard choice is $\sin: [-\pi/2, \pi/2] \to [-1, 1]$:

- Strictly increasing on $[-\pi/2, \pi/2]$ — injective ✓
- Closed at both endpoints, where $\sin$ reaches $-1$ and $+1$ — image is exactly $[-1, 1]$ ✓
- Hence bijective on this restriction; the inverse $\arcsin: [-1, 1] \to [-\pi/2, \pi/2]$ is a function.

This restriction is the **principal branch** of $\arcsin$. Different conventions are possible (the principal branch is a *choice*, not a discovery), but $[-\pi/2, \pi/2]$ is the universal one. Other interval choices fail one of the two requirements:

- $[0, 2\pi)$ — fails injectivity. $\sin$ is not monotonic on it ($\sin(\pi/4) = \sin(3\pi/4)$).
- $[0, \pi/2]$ — fails surjectivity onto $[-1, 1]$. The image is only $[0, 1]$; negative outputs are unreachable.

### 6. Composition

Given $f: A \to B$ and $g: B \to C$, the **composition** $g \circ f : A \to C$ is the function defined by $(g \circ f)(x) = g(f(x))$ — first apply $f$, then $g$.

Two facts that surprise beginners:

- **Composition is not commutative**: in general $g \circ f \neq f \circ g$. Example with $f(x) = x + 1$ and $g(x) = x^2$: $(g \circ f)(3) = g(4) = 16$, $(f \circ g)(3) = f(9) = 10$.
- **Compatibility of (co)domains is required**. $g \circ f$ is well-defined as a function only when $\operatorname{image}(f) \subseteq \operatorname{domain}(g)$ — every output of $f$ must be a legal input of $g$. Otherwise the composition is undefined for some inputs and not a function. Example: $f: \mathbb{R} \to \mathbb{R}, f(x) = x - 5$ and $g: [0, \infty) \to \mathbb{R}, g(x) = \sqrt{x}$. Then $(g \circ f)(2) = g(-3)$ is undefined.

### 7. Inverse via composition

If $f: A \to B$ is bijective with inverse $f^{-1}: B \to A$, then:

- $f^{-1} \circ f = \operatorname{id}_A$ (the identity on $A$)
- $f \circ f^{-1} = \operatorname{id}_B$ (the identity on $B$)

where $\operatorname{id}_X(x) = x$. This rephrasing of "the inverse undoes $f$" as an **equation between functions** is more than cosmetic: it is the algebraic definition of inverse, and it is the form that generalizes to other settings (group inverses, matrix inverses, inverse maps in category theory). Whenever an algebraic structure admits identity elements and a notion of composition, "inverse" is *defined* as "the element whose composition is the identity".

### 8. Identifying a function family from its graph

The seven elementary families from material 01 — **polynomial, rational, exponential, logarithmic, trigonometric, absolute value, piecewise** — each have a visual signature. Reading a graph is a two-step problem: first decide which family it belongs to, then recover the parameters within it.

> [!NOTE]
> The `graph-quiz.py` catalog only samples *one shape per family* — degree-1 and degree-2 polynomials, the $1/x$ form of rational, sine for trigonometric, etc.
> The theory below is about the families themselves; the quiz script trains a slice of each.

#### Triage: three questions before the family-by-family pass

Before drilling into individual signatures, three coarse questions narrow the search dramatically. They sort the seven families into branches that the next subsection then refines.

- **Are there asymptotes?** Vertical or horizontal walls/shelves the curve approaches but never reaches.
  - *Yes* ⇒ rational, exponential, logarithmic, or tangent (within trigonometric).
  - *No* ⇒ polynomial, sine/cosine, absolute value, or piecewise (without asymptote-bearing pieces).

- **Is the function bounded?** Confined between two horizontal levels for all $x$.
  - *Yes* ⇒ sine/cosine — the only families that oscillate between fixed bounds.
  - *No* ⇒ everything else.

- **Is the curve smooth everywhere?** No corners, no cusps, no jumps; slope defined and continuous at every point.
  - *Yes* ⇒ polynomial, rational, exponential, logarithmic, sine/cosine, or tangent.
  - *No* ⇒ absolute value or piecewise — the gluing point is the giveaway.

#### Family-by-family signatures

##### **Polynomial** — $p(x) = a_n x^n + \dots + a_1 x + a_0$

Once triage has placed the curve here (no asymptotes, unbounded, smooth), the remaining question is **degree**, read off two cues that must agree:

- **Number of turning points** (local maxima/minima): a degree-$n$ polynomial has at most $n-1$ of them. A straight line has $0$, a parabola has $1$, a cubic up to $2$, and so on.
- **End behavior** at $\pm\infty$:
  - *Even degree* ⇒ both ends go the same way (both up if leading coefficient $a_n > 0$, both down if $a_n < 0$).
  - *Odd degree* ⇒ ends go opposite ways (down-then-up if $a_n > 0$, up-then-down if $a_n < 0$).

Linear ($n = 1$) and quadratic ($n = 2$, vertex form $a(x-h)^2 + k$ with vertex $(h, k)$) are the cases the quiz currently samples, but the family extends to cubics, quartics, and beyond.

##### **Rational** — $f(x) = \dfrac{p(x)}{q(x)}$ with $p, q$ polynomials

The defining trait: **vertical asymptotes at the real roots of $q$ that are not also roots of $p$** (a shared root produces a hole instead, but the visual is similar — a missing point on an otherwise continuous curve).

- **End behavior at $\pm\infty$** is governed by the degrees of $p$ and $q$:
  - $\deg p < \deg q$ ⇒ horizontal asymptote at $y = 0$.
  - $\deg p = \deg q$ ⇒ horizontal asymptote at $y = a_n / b_m$ (ratio of leading coefficients).
  - $\deg p = \deg q + 1$ ⇒ **oblique** (slant) asymptote — the curve approaches a non-horizontal line.
  - $\deg p > \deg q + 1$ ⇒ no straight-line asymptote; the curve grows polynomial-like at infinity.

The hyperbola $\dfrac{a}{x - h} + k$ (one vertical asymptote at $x = h$, one horizontal at $y = k$, two disconnected branches) is the simplest case — it is what the quiz samples — but the family includes any ratio of polynomials. Multiple vertical asymptotes, oblique asymptotes, and several connected components are all on the table.

##### **Exponential** — $f(x) =a\, e^{c x} + k$

One end shoots off, the other flattens onto a **horizontal asymptote at $y = k$**. No vertical asymptote — defined for every $x$.

- Sign of the exponent coefficient sets the direction of growth (positive ⇒ growth to the right, negative ⇒ decay to the right). Sign of $a$ flips the curve above or below the asymptote.
- Mirror image of the logarithmic family across $y = x$ — they are inverses of each other, and the asymptote-axis swap is a direct consequence of that reflection.

##### **Logarithmic** — $f(x) = a\,\log_b(x - h) + k$

**Vertical asymptote at $x = h$**; no horizontal asymptote (the curve keeps going, just slowly).

- Defined only for $x > h$, with slow unbounded growth.
- Sign of $a$ controls direction (rise if $a > 0$, fall if $a < 0$).
- Distinguishing it from exponential is a question of *which axis the asymptote sits along*: horizontal for exponential, vertical for logarithmic.

##### **Trigonometric** — sine, cosine, tangent (and their reciprocals/combinations)

Two distinct visual sub-signatures inside this family:

- **Sine and cosine**: smooth, **bounded periodic oscillation** between two horizontal levels. Boundedness alone is enough to land here. Cosine is sine phase-shifted by $\pi/2$ — same shape, different starting position. For $a\sin(bx)$ or $a\cos(bx)$: amplitude $= |a|$, period $= 2\pi / b$. The inverse relation between $b$ and period is the standard slip — large $b$ ⇒ short period (more oscillations per unit), because $b$ is angular frequency, not period.
- **Tangent**: periodic but **unbounded**, with **vertical asymptotes** at every $\pi/2 + k\pi$. Each branch climbs from $-\infty$ to $+\infty$ within one period of length $\pi$. The combination "asymptotes + repeating identical branches" is the giveaway.

Periodicity is the family-wide trait — whether the periodic motion is bounded (sine/cosine) or punctured by asymptotes (tangent) tells you which sub-family.

##### **Absolute value** — $f(x) = a\,|x - h| + k$

A V (or inverted V if $a < 0$): two straight rays meeting at a **sharp corner**. Continuous, but not smooth at the vertex.

- Vertex at $(h, k)$; the V opens up if $a > 0$, down if $a < 0$; $|a|$ = slope of each ray.

It is the simplest piecewise function: $a|x-h| + k$ equals $a(x-h) + k$ for $x \geq h$ and $-a(x-h) + k$ for $x < h$ — two linear pieces glued at $x = h$. So it is also a special case of the next family.

##### **Piecewise** — $f(x) = \begin{cases} f_1(x) & x \in I_1 \\ f_2(x) & x \in I_2 \\ \vdots \end{cases}$

Defined by different rules on different intervals of the domain. Each piece $f_i$ is itself a function from one of the families above.

Visual signatures at the gluing points $x = c$ between intervals:

- **Corner**: pieces meet (same value) but with different slopes — continuous, not smooth. The absolute value is the canonical example.
- **Jump**: pieces do not meet — there is a vertical gap. The function is discontinuous at $c$.
- **Removable**: a single missing point sitting off the curve, often filled by a separately-defined value.

The dead giveaway is *any visible discontinuity in value or in slope*. If a curve is smooth everywhere except at one or two distinguished $x$-values, suspect piecewise.

#### Recovering parameters: how many observations are enough

Once the family is fixed, parameter recovery is a question of having enough independent constraints.

- **Asymptote-anchored families (rational, exponential, logarithmic, tangent)** give one or two parameters for free: the asymptote locations directly read off $h$ or $k$. The remaining parameters need additional points.
- **A single point under-constrains a family with more than one free coefficient.** For a logarithmic curve $a\log(x-h) + k$ with $h$ fixed by the asymptote, $a$ and $k$ still form a two-parameter family, and one observed $(x, y)$ pair satisfies infinitely many of them. Two independent observations (e.g. an intercept *and* the value at one other identifiable $x$) are needed to pin them down.
- **For sine and cosine, amplitude and period are independent observations.** Read amplitude off the vertical extent and period off the horizontal distance between consecutive zero-crossings (or peaks); then convert period to the angular-frequency coefficient via $b = 2\pi / \text{period}$.
- **For polynomials, degree is constrained jointly by turning-point count and end behavior** — neither alone is sufficient (a high-degree polynomial can have fewer turning points than its maximum). Once degree is fixed, $n + 1$ independent points determine all coefficients uniquely.

## Study log

- **2026-05-01** — Topic created. First material downloaded and transcribed.
- **2026-05-01** — Conversation on the *functions* block of material 01 (definition, inj/surj, restriction → arcsin, composition, inverse). Closed with [9 self-authored cards](cards/calculus-foundations.txt).
- **2026-05-03** — `scripts/` migrated to a `uv` project; new [`scripts/graph-quiz.py`](../../scripts/graph-quiz.py) renders quizzes for the *function families* block (random graph → identify family + recover formula, or formula → predicted graph). Conversation on the seven elementary families and the visual signature of each, settling on three rasgos that fingerprint a polynomial vs the rest (no asymptotes + unbounded + smooth). Started identification quizzes — sine (got family + amplitude, inverted the frequency coefficient) and logarithmic (got asymptote and intercept, missed the multiplicative coefficient because a single point under-constrains the parameters). To resume: more quizzes, then cards.
