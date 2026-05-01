# Calculus foundations

Vocabulary and intuition every later calculus topic rests on: what a function is, how to classify it (as injective, surjective, or bijective), composition, and inverse.

## Status

`[~]` in progress — functions block covered (with cards in active rotation); algebra and trigonometry blocks from material 01 still pending.

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

## Study log

- **2026-05-01** — Topic created. First material downloaded and transcribed.
- **2026-05-01** — Conversation on the *functions* block of material 01 (definition, inj/surj, restriction → arcsin, composition, inverse). Closed with [9 self-authored cards](cards/calculus-foundations.txt).
