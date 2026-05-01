# Calculus foundations

Vocabulary and intuition every later calculus topic rests on: what a function is, how to classify it (injective / surjective / bijective), composition, and inverse.

## Status

`[~]` in progress — functions block covered (with cards in active rotation); algebra and trigonometry blocks from material 01 still pending.

## Materials

| # | Source | Topic |
|---|--------|-------|
| 01 | [YouTube](https://www.youtube.com/watch?v=MaszunEszVM) | Functions, injectivity, surjectivity, bijectivity |

## Cards

- [`cards/calculus-foundations.txt`](../../cards/calculus-foundations.txt) — 9 cards covering the functions block (definition, dom/codom, injectivity/surjectivity independence, invertibility characterization, domain restriction, arcsin principal branch, composition non-commutativity, composition compatibility, inverse via composition).

## Theory

What follows is the settled prose version of what was worked out in conversation while studying material 01. The cards in `cards/calculus-foundations.txt` test the same content from different angles; this section is for re-reading before review.

### 1. What a function is

A function is a rule that assigns to **each** input **exactly one** output. The "exactly one" is the load-bearing part and combines two requirements:

- **Determinism** — the same input always produces the same output. A coin-tossing machine that maps an integer to `0` or `1` based on a flip is *not* a function, because feeding it the same integer twice may yield different outputs.
- **Uniqueness** — only one output per input, never several at once.

A relation that violates either property is not a function, even if it appears to "depend on" the input in some loose sense.

### 2. A function is rule + domain + codomain

The formula alone does not specify a function. The full data of a function is:

- a **domain** `A` — the set of legal inputs;
- a **codomain** `B` — the set of conceivable outputs;
- a **rule** that, for each `x ∈ A`, designates a unique `f(x) ∈ B`.

Notation: `f: A → B`. Two functions with the same rule but different domain or codomain are *different functions*. For example, all of these obey `f(x) = x²` but are not the same:

| Function | Properties |
|----------|------------|
| `f: ℝ → ℝ` | not injective, not surjective |
| `f: ℝ → [0, ∞)` | not injective, surjective |
| `f: [0, ∞) → ℝ` | injective, not surjective |
| `f: [0, ∞) → [0, ∞)` | bijective (invertible) |

### 3. Injectivity, surjectivity, bijectivity

Given `f: A → B`:

- **Injective** (one-to-one): different inputs go to different outputs. Formally, `f(x₁) = f(x₂) ⟹ x₁ = x₂`.
- **Surjective** (onto): every element of the codomain is hit by some input. Formally, for every `y ∈ B` there is some `x ∈ A` with `f(x) = y`.
- **Bijective**: both injective and surjective.

The two properties are **independent**: each can hold or fail without forcing the other (see the table above — all four cells are realizable by `x²` with the right (co)domain choice). Tightening the domain affects injectivity; tightening the codomain affects surjectivity.

### 4. When `f` has an inverse that is itself a function

`f: A → B` has an inverse function `f⁻¹: B → A` **if and only if `f` is bijective**. The two halves of "bijective" each preserve a different requirement of "being a function" in the inverse:

- **Injectivity of `f`** ⟹ **uniqueness in `f⁻¹`**. Each `y ∈ B` is the image of at most one `x`, so `f⁻¹(y)` is well-defined as a single value rather than a set.
- **Surjectivity of `f`** ⟹ **totality of `f⁻¹`**. Every `y ∈ B` is the image of at least one `x`, so `f⁻¹` is defined on the whole codomain `B`, not just part of it.

Drop either half and `f⁻¹` ceases to be a function.

### 5. Restricting the domain to force invertibility

Many natural rules are not injective on their full domain (`x²`, `sin x`, …). The standard technique to recover invertibility is to **restrict the domain to an interval where the function is strictly monotonic**:

- **Strict monotonicity** (strictly increasing or strictly decreasing) implies injectivity for free.
- The interval should be **closed at the endpoints where the function reaches the extremes of its codomain**, so that surjectivity onto the chosen codomain is preserved.

**Worked case — `arcsin`**. The function `sin: ℝ → [-1, 1]` is surjective but very far from injective. To define an inverse, restrict to a maximal monotonic interval. The standard choice is `sin: [-π/2, π/2] → [-1, 1]`:

- Strictly increasing on `[-π/2, π/2]` — injective ✓
- Closed at both endpoints, where `sin` reaches `-1` and `+1` — image is exactly `[-1, 1]` ✓
- Hence bijective on this restriction; the inverse `arcsin: [-1, 1] → [-π/2, π/2]` is a function.

This restriction is the **principal branch** of `arcsin`. Different conventions are possible (the principal branch is a *choice*, not a discovery), but `[-π/2, π/2]` is the universal one. Other interval choices fail one of the two requirements:

- `[0, 2π)` — fails injectivity. `sin` is not monotonic on it (`sin(π/4) = sin(3π/4)`).
- `[0, π/2]` — fails surjectivity onto `[-1, 1]`. The image is only `[0, 1]`; negative outputs are unreachable.

### 6. Composition

Given `f: A → B` and `g: B → C`, the **composition** `g ∘ f : A → C` is the function defined by `(g ∘ f)(x) = g(f(x))` — first apply `f`, then `g`.

Two facts that surprise beginners:

- **Composition is not commutative**: in general `g ∘ f ≠ f ∘ g`. Example with `f(x) = x + 1` and `g(x) = x²`: `(g ∘ f)(3) = g(4) = 16`, `(f ∘ g)(3) = f(9) = 10`.
- **Compatibility of (co)domains is required**. `g ∘ f` is well-defined as a function only when `image(f) ⊆ domain(g)` — every output of `f` must be a legal input of `g`. Otherwise the composition is undefined for some inputs and not a function. Example: `f: ℝ → ℝ, f(x) = x − 5` and `g: [0, ∞) → ℝ, g(x) = √x`. Then `(g ∘ f)(2) = g(-3)` is undefined.

### 7. Inverse via composition

If `f: A → B` is bijective with inverse `f⁻¹: B → A`, then:

- `f⁻¹ ∘ f = id_A` (the identity on `A`)
- `f ∘ f⁻¹ = id_B` (the identity on `B`)

where `id_X(x) = x`. This rephrasing of "the inverse undoes `f`" as an **equation between functions** is more than cosmetic: it is the algebraic definition of inverse, and it is the form that generalizes to other settings (group inverses, matrix inverses, inverse maps in category theory). Whenever an algebraic structure admits identity elements and a notion of composition, "inverse" is *defined* as "the element whose composition is the identity".

## Study log

- **2026-05-01** — Topic created. First material downloaded and transcribed.
- **2026-05-01** — Conversation on the *functions* block of material 01 (definition, inj/surj, restriction → arcsin, composition, inverse). Closed with 9 self-authored cards in `cards/calculus-foundations.txt`.
