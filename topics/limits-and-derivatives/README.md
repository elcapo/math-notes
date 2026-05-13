# Limits and derivatives

The bridge from functions to calculus proper: limits as the formal tool for "approaching", derivatives as the rate of change at a point, and L'Hôpital's rule as the first non-trivial payoff that connects both.

## Status

`[~]` in progress — material 01 added, conversation pending.

## Materials

| # | Source | Topic |
|---|--------|-------|
| 01 | [How to Get to Derivatives & de L'Hôpital Rule Naturally](https://youtu.be/sInn2CkPRWs) | Limits, derivatives, L'Hôpital's rule |

## Cards

*(none yet)*

## Theory

### 1. Limits: the idea of "approaching"

**What is a limit?**

When we write $\lim_{x \to a} f(x) = L$, we are saying: "as $x$ gets closer and closer to $a$, $f(x)$ gets closer and closer to $L$".

The key word is *approaching*. It does not mean that $x$ reaches $a$ (nor that $f(a)$ exists), but that we can make $f(x)$ as close to $L$ as we want simply by choosing $x$ sufficiently close to $a$.

**The ε-δ definition (formalization of "approaching"):**

The intuition above can be turned into a precise mathematical statement:

> $\lim_{x \to a} f(x) = L$ means:
> for every $\varepsilon > 0$, there exists $\delta > 0$ such that
> if $0 < |x - a| < \delta$, then $|f(x) - L| < \varepsilon$.

Let's unpack what this says:

- $\varepsilon$ (epsilon) represents "how close we want $f(x)$ to be to $L$" — it's a tolerance in the vertical direction.
- $\delta$ (delta) represents "how close $x$ must be to $a$" to achieve that tolerance — it's a requirement in the horizontal direction.
- The condition $0 < |x - a| < \delta$ means "$x$ is within $\delta$ of $a$, but not equal to $a$" — we never actually require $x = a$.

**Why the order matters:** The definition says "for every $\varepsilon$, there EXISTS a $\delta$". This is crucial — the $\delta$ we choose may depend on $\varepsilon$, but the limit must work for ALL $\varepsilon$. We cannot pick a fixed $\delta$ that works for some tolerances but not others.

**A concrete example:**

Let $f(x) = 2x$ and let's prove that $\lim_{x \to 3} f(x) = 6$.

Given any $\varepsilon > 0$, we need to find $\delta > 0$ such that:
if $0 < |x - 3| < \delta$, then $|2x - 6| < \varepsilon$.

Since $|2x - 6| = 2|x - 3|$, we can choose $\delta = \varepsilon / 2$. Then:
$|2x - 6| = 2|x - 3| < 2 \cdot (\varepsilon / 2) = \varepsilon$.

Done — we found a $\delta$ that works for any $\varepsilon$ we are given.

**One-sided limits:**

- $\lim_{x \to a^+} f(x)$: $x$ approaches $a$ from the right (larger values).
- $\lim_{x \to a^-} f(x)$: $x$ approaches $a$ from the left (smaller values).

For $\lim_{x \to a} f(x)$ to exist, both one-sided limits must exist AND be equal.

**Algebraic properties:**

If $\lim_{x \to a} f(x) = L$ and $\lim_{x \to a} g(x) = M$ (both exist and are finite), then:

| Operation | Property |
|-----------|----------|
| Sum | $\lim_{x \to a} [f(x) + g(x)] = L + M$ |
| Difference | $\lim_{x \to a} [f(x) - g(x)] = L - M$ |
| Constant multiple | $\lim_{x \to a} [c \cdot f(x)] = c \cdot L$ |
| Product | $\lim_{x \to a} [f(x) \cdot g(x)] = L \cdot M$ |
| Quotient | $\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{L}{M}$, provided $M \neq 0$ |
| Power | $\lim_{x \to a} [f(x)]^n = L^n$, for any positive integer $n$ |

**Why these matter:**

These rules let us compute limits of complicated expressions by breaking them into simpler pieces — *as long as none of the individual limits lead to an indeterminate form*.

For example, to find $\lim_{x \to 2} (3x^2 + 5x - 1)$:

- $\lim_{x \to 2} 3x^2 = 3 \cdot (2)^2 = 12$
- $\lim_{x \to 2} 5x = 5 \cdot 2 = 10$
- $\lim_{x \to 2} (-1) = -1$

Summing: $12 + 10 - 1 = 21$.

No indeterminate forms appeared, so the answer is direct.

**The danger:** These rules *fail* when we encounter $\frac{0}{0}$ or $\frac{\infty}{\infty}$. In those cases, we need other tools — algebra, L'Hôpital, or the Squeeze theorem.

**The Squeeze theorem (Sandwich theorem):**

If we have three functions such that $g(x) \leq f(x) \leq h(x)$ near $a$, and if:

$$\lim_{x \to a} g(x) = \lim_{x \to a} h(x) = L$$

then we can "squeeze" $f(x)$ to the same limit:

$$\lim_{x \to a} f(x) = L$$

**Why it works:** $f(x)$ is trapped between two functions that both approach the same value $L$, so it has no choice but to approach $L$ as well.

**Classic example:** $\lim_{x \to 0} \frac{\sin x}{x}$

We know that for $x$ near 0 (in radians): $-|x| \leq \sin x \leq |x|$

Dividing by $|x|$ (positive): $-1 \leq \frac{\sin x}{|x|} \leq 1$

But more precisely, we can use the geometric fact that for $0 < x < \pi/2$:

$$\cos x \leq \frac{\sin x}{x} \leq 1$$

As $x \to 0$, both $\cos x$ and $1$ approach 1, so by the Squeeze theorem:

$$\lim_{x \to 0} \frac{\sin x}{x} = 1$$

This is a fundamental limit that appears constantly in calculus.

**Indeterminate forms:**

Some expressions have no direct answer:

- $\frac{0}{0}$ (zero divided by zero)
- $\frac{\infty}{\infty}$ (infinity divided by infinity)
- $\infty - \infty$, $0 \cdot \infty$, $0^0$, $\infty^0$

"Indeterminate" does not mean "does not exist" — it means we need further analysis to determine the limit. L'Hôpital is precisely a tool to resolve the most common ones ($\frac{0}{0}$ and $\frac{\infty}{\infty}$).

**Connection to derivatives:**

The limit is the foundational concept that allows us to define the derivative. The derivative at a point is:

$$f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$$

This is a limit where $h$ represents the "increment" in $x$, and we want to see what happens as that increment becomes infinitesimally small.

**Continuity:**

A function $f$ is *continuous at a point* $a$ if:

$$\lim_{x \to a} f(x) = f(a)$$

In words: the limit exists, the function value exists, and they are equal.

This combines three conditions:
1. $f(a)$ is defined (the point exists)
2. $\lim_{x \to a} f(x)$ exists
3. Both values coincide

**Discontinuities:** When any of these fails, we have a discontinuity. Common types:

- *Removable*: the limit exists but $f(a)$ is either undefined or different. Graphically, a "hole" in the curve.
- *Jump*: the one-sided limits exist but are different (like the step function).
- *Infinite*: the function grows without bound near $a$ (vertical asymptote).

**Why continuity matters for derivatives:**

For $f'(a)$ to exist, $f$ must be continuous at $a$. However, continuity alone is *not sufficient* — a function can be continuous at a point but still fail to have a derivative there (e.g., $f(x) = |x|$ at $x = 0$, where there's a "corner").

This makes sense: the derivative measures the slope of the tangent, and a corner has no unique tangent line.

### 3. L'Hôpital's rule

**The problem:** When we encounter limits like $\lim_{x \to a} \frac{f(x)}{g(x)}$ where both $f(a) = 0$ and $g(a) = 0$ (or both tend to $\infty$), the algebraic properties of limits break down. We get the indeterminate form $\frac{0}{0}$ or $\frac{\infty}{\infty}$.

**The solution:** L'Hôpital's rule lets us replace the quotient by the quotient of the derivatives:

> If $\lim_{x \to a} \frac{f(x)}{g(x)}$ gives $\frac{0}{0}$ or $\frac{\infty}{\infty}$, and both $f$ and $g$ are differentiable near $a$ (with $g'(x) \neq 0$ nearby), then:
>
> $$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$

**The intuition:**

Think of the numerator $f(x)$ and denominator $g(x)$ as two functions "racing" toward zero (or infinity). Which one gets there faster?

- The derivative $f'(x)$ tells us the *instantaneous rate of change* of $f$ at each point.
- The derivative $g'(x)$ tells us the *instantaneous rate of change* of $g$.
- Comparing $f'(x)$ to $g'(x)$ tells us which function is "winning" the race.

If $\frac{f'(x)}{g'(x)}$ still gives an indeterminate form, we can apply L'Hôpital again (and again, as needed).

**Example 1 — 0/0 at a point:**

$$\lim_{x \to 0} \frac{\sin x}{x}$$

Both $\sin(0) = 0$ and the denominator $x \to 0$. Apply L'Hôpital:

$$\lim_{x \to 0} \frac{\sin x}{x} = \lim_{x \to 0} \frac{\cos x}{1} = \frac{1}{1} = 1$$

**Example 2 — ∞/∞ at infinity:**

$$\lim_{x \to \infty} \frac{x^2}{e^x}$$

As $x \to \infty$, both numerator and denominator grow without bound. Apply L'Hôpital:

$$\lim_{x \to \infty} \frac{x^2}{e^x} = \lim_{x \to \infty} \frac{2x}{e^x}$$

Still $\frac{\infty}{\infty}$. Apply again:

$$\lim_{x \to \infty} \frac{2x}{e^x} = \lim_{x \to \infty} \frac{2}{e^x} = 0$$

**Caveats:**

- L'Hôpital only applies to $\frac{0}{0}$ or $\frac{\infty}{\infty}$. It *cannot* be used on other indeterminate forms like $0 \cdot \infty$ or $\infty - \infty$ — those must be rewritten first.
- The rule requires both functions to be differentiable in a neighborhood of $a$ (except possibly at $a$ itself).
- If $\lim \frac{f'(x)}{g'(x)}$ does not exist, L'Hôpital tells us nothing — the original limit might still exist.

**Connection to the theorem:**

L'Hôpital can be proved using the Cauchy Mean Value Theorem, which generalizes the Mean Value Theorem to two functions. The idea: if $f(a) = g(a) = 0$, then near $a$ there exists a point $c$ where the ratio of derivatives equals the ratio of function values.

### 4. Conceptual connection: why L'Hôpital works

L'Hôpital is not a magical trick — it's a direct consequence of how derivatives measure rate of change.

**The big picture:**

1. **Limits** give us the language of "approaching"
2. **Derivatives** give us the rate of change at a point — also defined as a limit
3. **L'Hôpital** uses derivatives (rates of change) to compare how fast two functions approach zero or infinity

The rule bridges these concepts: it's a tool that uses the derivative (section 2) to resolve indeterminate limits (section 1).

**Why derivatives help with 0/0:**

When $f(a) = 0$ and $g(a) = 0$, we can't compare the function values at $a$. But we can compare how they *leave* $a$ — their instantaneous rates of change. That's exactly what $f'(a)$ and $g'(a)$ tell us.

If $f$ "takes off faster" from zero than $g$, then $\frac{f'(a)}{g'(a)}$ captures that, and that's what the limit will be.

## Study log

- **2026-05-09** — Topic created. Material 01 (DiBeos follow-up to "The Language of Calculus") downloaded and transcribed.
