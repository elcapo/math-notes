# Limits and derivatives

The bridge from functions to calculus proper: limits as the formal tool for "approaching", derivatives as the rate of change at a point, and L'Hôpital's rule as the first non-trivial payoff that connects both.

## Status

`[x]` covered — material 01 added, full proof chain (Fermat → Rolle → Lagrange → Cauchy → L'Hôpital) discussed in conversation, 22 cards in active rotation.

## Materials

| # | Source | Topic |
|---|--------|-------|
| 01 | [How to Get to Derivatives & de L'Hôpital Rule Naturally](https://youtu.be/sInn2CkPRWs) | Limits, derivatives, L'Hôpital's rule |

## Cards

22 cards in `cards/limits-and-derivatives.txt`, split across subdecks: Limits (7), Derivative (3), L'Hôpital (5), Continuity (1), Mean Value Theorems (5), Conceptual (1).

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

**A discrete preview — racing to zero:**

Before reaching for L'Hôpital, it helps to see why $\frac{0}{0}$ can still produce a clear answer. Consider the sequence $\frac{a_n}{b_n}$ defined recursively by

$$a_{n+1} = \frac{a_n}{2}, \qquad b_{n+1} = b_n^{\,2}$$

with $a_1, b_1 \in (0, 1)$. Both $a_n \to 0$ and $b_n \to 0$, so naively $\frac{a_n}{b_n}$ has the shape $\frac{0}{0}$. But squaring a small number shrinks it far more aggressively than halving it: after a few iterations, $a_n$ is still "moderately small" while $b_n$ is effectively zero. The quotient then behaves like "fixed-ish number / vanishingly small" and runs off to $\infty$.

The lesson: an indeterminate form is the symptom of two competing *rates* of approach to zero (or to infinity). Once we identify which side moves faster, the apparent ambiguity disappears. L'Hôpital automates exactly this comparison for continuous functions, using derivatives as the rate-of-change yardstick.

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

**Continuity of composition:**

A fundamental property emerges from continuity: we can exchange limits with continuous functions.

> **Theorem (Continuity of Composition):**
> If $\lim_{x \to a} g(x) = L$ and $f$ is continuous at $L$, then:
> $$\lim_{x \to a} f(g(x)) = f\left(\lim_{x \to a} g(x)\right) = f(L)$$

**Why it works:**
- $g(x) \to L$ means we can get arbitrarily close to $L$ by choosing $x$ close enough to $a$
- $f$ being continuous at $L$ means: if $y$ is close to $L$, then $f(y)$ is close to $f(L)$
- Chaining: $g(x)$ close to $L$ $\implies$ $f(g(x))$ close to $f(L)$

**Practical consequence:**
If $f$ is continuous everywhere (polynomials, $\sin, \cos, e^x$, etc.), we can always interchange limits and function application — as long as $\lim g(x)$ exists.

**Example:**
$\lim_{x \to 0} e^{\sin x} = e^{\lim_{x \to 0} \sin x} = e^0 = 1$

Here $\sin x \to 0$ and $e^y$ is continuous at $0$.

**Counterexample (when it fails):**
Let $f(x) = \begin{cases} 0 & x = 0 \\ 1 & x \neq 0 \end{cases}$ (discontinuous at $0$)
Let $g(x) = x$ with $\lim_{x \to 0} g(x) = 0$

Then $\lim_{x \to 0} f(g(x)) = \lim_{x \to 0} f(x) = 1$, but $f(\lim_{x \to 0} g(x)) = f(0) = 0$.

The theorem requires $f$ to be continuous at the limit point — otherwise the exchange fails.

### 2. The derivative: slope of the tangent line

**The tangent line:**

At any point $x_0$ on a smooth curve $f(x)$, there is a unique straight line that "just touches" the curve at that point — it crosses the curve at exactly one point (assuming no sharp corners). This is the **tangent line**.

**Why the tangent matters:**

The angle each tangent line makes with the horizontal tells us how steep the curve is at that point. This is incredibly useful:
- In physics: instantaneous velocity of a moving particle
- In economics: marginal cost or marginal revenue
- In optimization: direction of fastest increase/decrease

A tangent line pointing upward (positive slope) means the function is increasing; downward means decreasing.

**Slope and angle are the same number:**

If a tangent line makes angle $\theta$ with the horizontal, its slope is exactly $\tan(\theta)$:

- $\theta = 0°$: slope $= \tan(0°) = 0$ (horizontal tangent, function locally flat).
- $\theta = 45°$: slope $= \tan(45°) = 1$ (function rising "1 unit up per 1 unit right").
- $\theta = -45°$: slope $= \tan(-45°) = -1$ (falling at the same rate).
- $\theta \to 90°$: slope $\to \infty$ (vertical tangent, no well-defined derivative).

This is not a coincidence in naming. In the right triangle formed by the tangent line, the *rise* is the side opposite to $\theta$ and the *run* is the side adjacent to $\theta$. Their ratio is the definition of the trigonometric tangent:

$$\text{slope} = \frac{\text{rise}}{\text{run}} = \frac{\text{opposite}}{\text{adjacent}} = \tan(\theta)$$

So "slope of the tangent line" and "trigonometric tangent of the tangent line's angle" are the same number. This is the bridge from the geometric picture (an angle) to the algebraic object we will compute via a limit.

**The derivative as a limit:**

The slope of the tangent line at $x = a$ is defined as the limit of the slope of secant lines as the second point approaches $a$:

$$f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$$

- $h$ is the horizontal distance between two points on the curve
- The fraction $\frac{f(a+h) - f(a)}{h}$ is the slope of the secant line
- Taking the limit as $h \to 0$ gives the instantaneous rate of change — the slope of the tangent

This limit may not exist (e.g., at a corner or cusp), and when it does, we say $f$ is **differentiable** at $a$.

**Derivative notation:**

- $f'(a)$ — "f prime of a"
- $\frac{df}{dx}$ — Leibniz notation, read as "dee-f over dee-x"
- $D_x f(x)$ — operator notation

**Interpretation:**

The derivative $f'(a)$ answers: "If I move a tiny bit away from $a$, how fast does $f$ change?"

- $f'(a) > 0$: $f$ is increasing at $a$
- $f'(a) < 0$: $f$ is decreasing at $a$
- $f'(a) = 0$: $f$ is stationary (flat) at $a$

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

**Geometric interpretation:**

Since the derivative at a point is the slope of the tangent line — which equals $\tan(\theta)$ of the angle that tangent makes with the horizontal — the ratio $\frac{f'}{g'}$ has a clean visual meaning.

Recall the unit-circle picture of the tangent function: starting from the origin, draw a ray at angle $\theta$ and extend it until it crosses the vertical line $x = 1$; the height at which it meets that vertical is exactly $\tan(\theta)$. Drawing this construction for the numerator's tangent angle $\theta_N$ and the denominator's tangent angle $\theta_D$ at the same point produces two heights on the *same* vertical reference:

$$\tan(\theta_N) = f'(x), \qquad \tan(\theta_D) = g'(x)$$

The L'Hôpital quotient becomes a literal ratio of two visible segments:

$$\frac{f'(x)}{g'(x)} = \frac{\tan(\theta_N)}{\tan(\theta_D)}$$

If this ratio equals $3$ at some point, it means the numerator's tangent fits three copies of the denominator's tangent on that vertical line — the numerator is climbing three times as steeply right there. Repeating the comparison at every point near $a$ tells us which function "wins the race" using directly comparable lengths.

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

**From Fermat to L'Hôpital — a formal derivation:**

The "racing" intuition becomes fully rigorous by climbing a short ladder of four theorems, each one a small step beyond the previous.

**Fermat's theorem.**

> If $f$ has a local extremum at an interior point $c \in (a, b)$ and $f'(c)$ exists, then $f'(c) = 0$.

*Geometric reading:* at a local maximum or minimum, the tangent line must be horizontal. There is no consistent "uphill" or "downhill" direction at such a point — both sides of $c$ have already been beaten in height (max) or undercut (min) by the function value at $c$ itself, so the slope cannot favor either side.

*Proof sketch (step by step):*

At a local maximum $c$, for sufficiently small $h$ we have $f(c+h) \leq f(c)$.

**From the right ($h > 0$):**
Since $f(c+h) - f(c) \leq 0$ and $h > 0$ (positive, preserves sign):
$$\frac{f(c+h) - f(c)}{h} \leq 0$$
Taking the limit as $h \to 0^+$:
$$f'(c) \leq 0$$

**From the left ($h < 0$):**
Since $f(c+h) - f(c) \leq 0$ and $h < 0$ (negative, inverts sign):
$$\frac{f(c+h) - f(c)}{h} \geq 0$$
Taking the limit as $h \to 0^-$:
$$f'(c) \geq 0$$

**Combining both sides:**
If $f'(c)$ exists, both one-sided limits must agree and equal $f'(c)$. We get:
$$f'(c) \leq 0 \quad \text{and} \quad f'(c) \geq 0 \implies f'(c) = 0$$

The key is that the sign of $h$ determines whether the inequality is preserved or inverted when dividing. For a local minimum, the inequalities flip ($f(c+h) \geq f(c)$), but the conclusion is the same.

This is the only step in the chain with genuine analytical content — one-sided difference quotients squeezing $f'(c)$ to zero. Everything that follows builds on Fermat plus the extreme value theorem.

**Rolle's theorem.**

> If $f$ is continuous on $[a, b]$, differentiable on $(a, b)$, and $f(a) = f(b)$, then there exists $c \in (a, b)$ such that $f'(c) = 0$.

*Geometric reading:* if a smooth curve starts and ends at the same height, it must turn around somewhere in between, and at the turning point the tangent is horizontal.

*Derivation from Fermat:* by the extreme value theorem, $f$ attains a maximum and a minimum on $[a, b]$. Two cases:

- If either extremum is reached at an interior point $c \in (a, b)$, Fermat's theorem gives $f'(c) = 0$.
- If both extrema occur at the endpoints, then since $f(a) = f(b)$, the max and min coincide; $f$ is constant on $[a, b]$ and $f'(c) = 0$ for every $c \in (a, b)$.

Either way we get a point with zero derivative.

**Lagrange's Mean Value Theorem.**

> If $f$ is continuous on $[a, b]$ and differentiable on $(a, b)$, then there exists $c \in (a, b)$ such that
> $$f'(c) = \frac{f(b) - f(a)}{b - a}$$

*Geometric reading:* the slope of the secant line joining the endpoints is achieved as the instantaneous slope at some interior point — somewhere, the tangent is parallel to the chord.

*Derivation from Rolle (step by step):*

**Step 1: Build the secant line.**
The line passing through $(a, f(a))$ and $(b, f(b))$ is:
$$\varphi(x) = f(a) + \frac{f(b) - f(a)}{b - a}(x - a)$$

This is the straight line that connects the endpoints — its slope is the slope of the chord.

**Step 2: Define the auxiliary function.**
Let $h(x)$ be the vertical distance between $f(x)$ and the secant:
$$h(x) = f(x) - \varphi(x)$$

**Step 3: Verify $h$ satisfies Rolle's conditions.**
- $h$ is continuous on $[a, b]$ (difference of continuous functions)
- $h$ is differentiable on $(a, b)$ (difference of differentiable functions)
- At the endpoints:
  - $h(a) = f(a) - \varphi(a) = f(a) - f(a) = 0$
  - $h(b) = f(b) - \varphi(b) = f(b) - f(b) = 0$
  So $h(a) = h(b) = 0$.

**Step 4: Apply Rolle.**
Since $h(a) = h(b) = 0$, Rolle guarantees $c \in (a, b)$ with $h'(c) = 0$.

**Step 5: Compute $h'(x)$ and evaluate at $c$.**
$$h'(x) = f'(x) - \varphi'(x) = f'(x) - \frac{f(b) - f(a)}{b - a}$$

At $x = c$:
$$h'(c) = f'(c) - \frac{f(b) - f(a)}{b - a} = 0$$

**Step 6: Rearrange.**
$$f'(c) = \frac{f(b) - f(a)}{b - a}$$

The geometric intuition: $h(x)$ measures how far $f$ deviates from the secant. Since $h(a) = h(b) = 0$, the deviation is zero at both ends. Rolle says there's a point $c$ where $h$ is "flat" — the curve $f$ has the same slope as the secant there.

**Corollary — sign of the derivative.**

> If $f$ is continuous on $[a, b]$, differentiable on $(a, b)$, and $f'(x) > 0$ for all $x \in (a, b)$, then $f$ is strictly increasing on $[a, b]$. (Symmetrically, $f'(x) < 0$ on $(a, b)$ implies $f$ is strictly decreasing.)

*Derivation from Lagrange:* take any two points $x_1 < x_2$ in $[a, b]$. Lagrange's Mean Value Theorem on $[x_1, x_2]$ gives some $c \in (x_1, x_2)$ with

$$f(x_2) - f(x_1) = f'(c) \cdot (x_2 - x_1)$$

The right-hand side is a product of two positives (by hypothesis $f'(c) > 0$, and $x_2 - x_1 > 0$ by choice), so $f(x_2) > f(x_1)$ — that is exactly the definition of strictly increasing.

The derivative section earlier stated, informally, that:

> $f'(a) > 0$ means $f$ is increasing at $a$

The corollary above is its rigorous form, with one important asymmetry to flag: the §2 claim is *pointwise* ($f' > 0$ at the single point $a$), while the corollary requires $f' > 0$ *on a whole interval* to conclude monotonicity. Strict monotonicity on an interval is an interval property — a single positive value of $f'$ at one point does not, by itself, guarantee that $f$ is increasing in any neighborhood of it.

**Cauchy's Mean Value Theorem (Generalized Mean Value Theorem).**

> If $f$ and $g$ are continuous on $[a, b]$, differentiable on $(a, b)$, and $g'(x) \neq 0$ on $(a, b)$, then there exists $c \in (a, b)$ such that
> $$\frac{f'(c)}{g'(c)} = \frac{f(b) - f(a)}{g(b) - g(a)}$$

*Geometric reading:* think of $(g(t), f(t))$ as a parametric curve in the plane. Cauchy's Mean Value Theorem says that somewhere along this curve, the *ratio* of instantaneous rates of change matches the *ratio* of total changes over the interval — the parametric tangent direction is parallel to the chord direction. When $g(x) = x$, this collapses back to Lagrange.

*Derivation from Rolle:* apply Rolle to the auxiliary function

$$h(x) = [f(x) - f(a)] \cdot [g(b) - g(a)] - [g(x) - g(a)] \cdot [f(b) - f(a)]$$

which satisfies $h(a) = h(b) = 0$. Rolle yields a $c$ with $h'(c) = 0$, and rearranging gives the stated identity (here we use $g'(c) \neq 0$ to divide).

**L'Hôpital follows in one line.**

Suppose $f(a) = g(a) = 0$ and we want $\lim_{x \to a} \frac{f(x)}{g(x)}$. For any $x$ near $a$, apply Cauchy's Mean Value Theorem on the interval between $a$ and $x$: there exists $c$ strictly between $a$ and $x$ with

$$\frac{f(x)}{g(x)} = \frac{f(x) - f(a)}{g(x) - g(a)} = \frac{f'(c)}{g'(c)}$$

(the first equality uses $f(a) = g(a) = 0$). Now let $x \to a$. Since $c$ is squeezed between $a$ and $x$, we also have $c \to a$, so

$$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{c \to a} \frac{f'(c)}{g'(c)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$

whenever the right-hand limit exists. That is precisely L'Hôpital's rule for the $\frac{0}{0}$ case.

The $\frac{\infty}{\infty}$ case is true as well but requires a more delicate $\varepsilon$-$\delta$ argument (or a Stolz–Cesàro-style trick); the engine, however, is the same — Cauchy's Mean Value Theorem lets us trade a quotient of function values for a quotient of derivatives evaluated at some intermediate point.

## Study log

- **2026-05-09** — Topic created. Material 01 (DiBeos follow-up to "The Language of Calculus") downloaded and transcribed.
- **2026-05-15** — Theory expanded with three geometric pieces from the transcript: discrete preview of $\frac{0}{0}$ as a race to zero, slope/angle identity ($m = \tan\theta$), and visual interpretation of L'Hôpital as a ratio of tangent-line segments on a shared vertical reference. Added a formal derivation of L'Hôpital's rule via Rolle → Lagrange → Cauchy, with the geometric reading and Rolle-based proof sketch for each Mean Value Theorem variant. Extended the chain at both ends: Fermat's theorem as the foundational lemma underpinning Rolle (one-sided difference quotients with opposite signs forcing $f'(c) = 0$ at an interior extremum) and a sign-of-derivative corollary placed after Lagrange that retroactively formalizes the claim "$f'(a) > 0 \Rightarrow$ $f$ increasing at $a$", flagging the pointwise-vs-interval asymmetry.
- **2026-05-15** — Second round of cards (7 added, total 22): one for continuity of composition, one per link of the Fermat → Rolle → Lagrange → Cauchy chain, one for the pointwise-vs-interval sign-of-derivative corollary, and one for the Cauchy-based closure to L'Hôpital. Topic closed.
