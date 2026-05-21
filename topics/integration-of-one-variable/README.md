# Integration of one variable

Closes the single-variable arc started in `limits-and-derivatives`: the integral as accumulation, the definite integral as a limit of Riemann sums, and the fundamental theorem of calculus tying it back to the derivative. Direct prerequisite for the UPMC L2 `Analyse II` UE (Lebesgue integration on $\mathbb{R}^n$), which uses the Riemann integral as motivation and reference point.

## Status

`[~]` in progress — three MIT OCW lecture notes (definite integrals + both halves of the FTC) downloaded; OpenStax and 3Blue1Brown wired in as references. No conversation yet, no cards yet.

## Materials

| # | Source | Topic |
|---|--------|-------|
| 01 | [MIT 18.01 Lecture 18 (PDF)](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/d1b3d809b6505825b5cde0cee823fa0f_lec18.pdf) | Definite integrals as limits of Riemann sums |
| 02 | [MIT 18.01 Lecture 19 (PDF)](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/817a2c46ddc23e2efda247a79ddeed34_lec19.pdf) | First Fundamental Theorem: $\int_a^b f = F(b) - F(a)$ |
| 03 | [MIT 18.01 Lecture 20 (PDF)](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/3cd98c68cec64e9214c8c9003f6cf983_lec20.pdf) | Second Fundamental Theorem: $\frac{d}{dx}\int_a^x f = f$ |
| 04 | [OpenStax Calculus Vol. 1, ch. 5–6](https://openstax.org/details/books/calculus-volume-1) | Textbook reference (not downloaded) |
| 05 | [3Blue1Brown — Essence of Calculus, ch. 8](https://www.youtube.com/watch?v=rfG8ce4nNh0) | Visual recap of integration and the FTC |

Main study material: MIT OCW 18.01 lecture notes (Prof. David Jerison, Fall 2006), under CC BY-NC-SA 4.0. OpenStax (also CC BY-NC-SA 4.0) is a textbook to consult when a topic needs more worked examples; 3Blue1Brown's chapter 8 is the visual perspective-opener.

If MIT 18.01 needs to be extended later, the integration unit continues with lectures 21–24 (applications: logarithms, volumes by disks/shells, work, numerical integration) and 26 (trig integrals, substitution).

## Cards

None yet — see `cards/integration-of-one-variable.txt` after the topic is closed.

## Theory

### 1. From accumulation to the definite integral

#### 1.1 Motivating problem

Differentiation measures *rate of change*. Integration is its mirror: it measures *accumulated total*. The archetypal question is "what is the area under the curve $y = f(x)$ between $x = a$ and $x = b$?", but the same machinery also computes total distance from a speed function, total charge from a current, total cost from a marginal cost, etc. The unifying picture is: we have a quantity that varies along $[a, b]$ and we want its accumulated total over the interval.

#### 1.2 Partitions and Darboux sums

A *partition* of $[a, b]$ is a finite increasing sequence

$$a = x_0 < x_1 < x_2 < \cdots < x_n = b,$$

cutting the interval into $n$ sub-intervals $[x_{i-1}, x_i]$ of length $\Delta x_i = x_i - x_{i-1}$. Given a bounded function $f$ on $[a, b]$, on each sub-interval set

$$m_i = \inf_{x \in [x_{i-1}, x_i]} f(x), \qquad M_i = \sup_{x \in [x_{i-1}, x_i]} f(x).$$

The *lower Darboux sum* and *upper Darboux sum* are

$$L(f, P) = \sum_{i=1}^n m_i \, \Delta x_i, \qquad U(f, P) = \sum_{i=1}^n M_i \, \Delta x_i.$$

Geometrically, $L$ is the area of the tallest staircase that stays below the graph, $U$ the shortest staircase that covers it. By construction $L(f, P) \le U(f, P)$ for every partition $P$.

![Darboux sums](./resources/darboux-sums.png)

#### 1.3 Riemann sums and the limit

A *Riemann sum* uses a free sample point $c_i \in [x_{i-1}, x_i]$ on each sub-interval, not the inf/sup:

$$S(f, P, \{c_i\}) = \sum_{i=1}^n f(c_i) \, \Delta x_i.$$

Always $L(f, P) \le S(f, P, \{c_i\}) \le U(f, P)$. If, as we refine the partition (taking the mesh $\max_i \Delta x_i$ to $0$), the lower and upper sums converge to the *same* limit, $f$ is called *Riemann integrable* on $[a, b]$, and that common limit is the **definite integral**

$$\int_a^b f(x)\,dx \;=\; \lim_{n \to \infty} \sum_{i=1}^n f(c_i)\,\Delta x_i.$$

The notation is suggestive: $\int$ is a stretched "S" for *sum*, $dx$ is an infinitesimal width, and the integrand $f(x)$ is the height being summed.

For uniform partitions on $[a, b]$ with $\Delta x = (b-a)/n$, the prototypical computation (MIT Lec 18, $f(x) = x^2$ on $[0, b]$) gives

$$\int_0^b x^2 \, dx = \lim_{n \to \infty} \frac{b^3}{n^3}(1^2 + 2^2 + \cdots + n^2) = \frac{b^3}{3},$$

using the staircase-pyramid bound $\tfrac{1}{3} n^3 < 1^2 + 2^2 + \cdots + n^2 < \tfrac{1}{3}(n+1)^3$.

![Riemann sums](./resources/riemann-sums.png)

#### 1.4 Sufficient conditions for integrability

The definition is delicate — not every bounded function is integrable. Two sufficient conditions cover essentially everything seen at this level:

- If $f$ is **continuous** on $[a, b]$, then $f$ is Riemann integrable on $[a, b]$.
- If $f$ is **bounded and piecewise continuous** (continuous except at finitely many points), then $f$ is Riemann integrable on $[a, b]$.

The classical pathology that *fails* is the Dirichlet function $\mathbf{1}_{\mathbb{Q} \cap [0, 1]}$: on every sub-interval $m_i = 0$ and $M_i = 1$, so $L \equiv 0$ and $U \equiv 1$ for every partition and the gap never closes. The Lebesgue integral, picked up in `LU2MA211 Analyse II`, is precisely the framework that makes such functions integrable.

#### 1.5 Signed area and basic properties

When $f \ge 0$, $\int_a^b f$ is the area under the graph. When $f$ dips below the axis, those contributions enter with a **minus sign** — the integral is a *signed* area:

$$\int_0^{2\pi} \sin x \, dx = 0$$

because the positive hump on $[0, \pi]$ and the negative hump on $[\pi, 2\pi]$ cancel.

The integral has three properties that get used constantly:

- **Linearity.** $\int_a^b \bigl(\alpha f + \beta g\bigr) = \alpha \int_a^b f + \beta \int_a^b g$.
- **Additivity over intervals.** $\int_a^b f + \int_b^c f = \int_a^c f$.
- **Monotonicity (estimation).** If $f \le g$ on $[a, b]$ with $a < b$, then $\int_a^b f \le \int_a^b g$. In particular $\bigl|\int_a^b f\bigr| \le \int_a^b |f|$.

By convention we extend the definition with

$$\int_a^a f(x)\,dx = 0, \qquad \int_b^a f(x)\,dx = -\int_a^b f(x)\,dx,$$

which makes additivity work for $a, b, c$ in any order and removes the ordering hypothesis from later statements.

### 2. First Fundamental Theorem of Calculus (evaluation form)

#### 2.1 Statement

> **FTC1.** Let $f$ be continuous on $[a, b]$ and let $F$ be any antiderivative of $f$ on $[a, b]$ (that is, $F' = f$). Then
>
> $$\int_a^b f(x)\,dx = F(b) - F(a).$$

The standard shorthand is $F(x)\Big|_a^b = F(b) - F(a)$. Two textbook applications:

$$\int_a^b x^2 \, dx = \left.\frac{x^3}{3}\right|_a^b = \frac{b^3 - a^3}{3}, \qquad \int_0^{\pi} \sin x \, dx = \bigl[-\cos x\bigr]_0^{\pi} = 2.$$

#### 2.2 Proof sketch (via FTC2 and the Mean Value Theorem)

The cleanest argument actually uses FTC2 (next section) plus a corollary of the Mean Value Theorem from [`limits-and-derivatives`](../limits-and-derivatives/README.md): on a connected interval, *two antiderivatives of the same function differ by a constant*.

Define $G(x) = \int_a^x f(t)\,dt$. By FTC2, $G' = f$. Since $F$ is also an antiderivative of $f$, the corollary above gives $F - G = c$ for some constant $c$. Evaluating at $a$ uses $G(a) = 0$, so $c = F(a)$. Then

$$F(b) - F(a) = G(b) + c - c = G(b) = \int_a^b f(x)\,dx. \qquad \blacksquare$$

So FTC1 is, logically, a corollary of FTC2 plus MVT.

#### 2.3 What FTC1 buys us

Without FTC1, computing $\int_0^b x^2 \, dx$ required summing $1^2 + 2^2 + \cdots + n^2$ and taking a limit. With FTC1, the same answer falls out of "an antiderivative of $x^2$ is $x^3/3$". Integration is converted from a limit problem into an **antiderivative search**. That changes the practical character of the subject: most of single-variable integral calculus from here on is a catalogue of techniques (substitution, parts, partial fractions, trig identities) for finding antiderivatives.

### 3. Second Fundamental Theorem of Calculus (construction form)

#### 3.1 Statement

> **FTC2.** Let $f$ be continuous on $[a, b]$. Define
>
> $$G(x) = \int_a^x f(t)\,dt \qquad \text{for } x \in [a, b].$$
>
> Then $G$ is differentiable on $[a, b]$ with $G'(x) = f(x)$.

In words: *integration with a variable upper limit constructs an antiderivative*. Every continuous function has an antiderivative — namely, its own running accumulation from a base point.

#### 3.2 Proof sketch

By definition of the derivative,

$$G'(x) = \lim_{h \to 0} \frac{G(x + h) - G(x)}{h}.$$

By additivity over intervals,

$$G(x + h) - G(x) = \int_a^{x+h} f(t)\,dt - \int_a^x f(t)\,dt = \int_x^{x+h} f(t)\,dt.$$

Geometrically this is the thin sliver of area between $x$ and $x + h$; its base is $h$ and its height is approximately $f(x)$, so

$$\frac{G(x + h) - G(x)}{h} = \frac{1}{h}\int_x^{x+h} f(t)\,dt$$

is the **average value** of $f$ over $[x, x+h]$. Continuity of $f$ at $x$ forces that average to converge to $f(x)$ as $h \to 0$ (formally: a $\varepsilon$-$\delta$ argument bounds $|f(t) - f(x)| < \varepsilon$ for $|t - x| < \delta$ and squeezes the average). Hence $G'(x) = f(x)$. $\quad\blacksquare$

#### 3.3 Existence of antiderivatives, and "new" functions

FTC2 has a striking consequence: **every continuous function has an antiderivative**, even if no closed-form formula exists for it. Examples of functions that are continuous but whose antiderivatives are *not* expressible in elementary terms:

$$e^{-x^2}, \qquad \frac{\sin x}{x}, \qquad \sin(x^2), \qquad \cos(x^2), \qquad \frac{1}{\ln x}.$$

The way to *name* their antiderivatives is to declare them as integrals. This is how several special functions enter mathematics:

- **Error function.** $\operatorname{erf}(x) = \dfrac{2}{\sqrt{\pi}} \int_0^x e^{-t^2}\,dt$ — ubiquitous in probability (Gaussian tails).
- **Logarithmic integral.** $\operatorname{Li}(x) = \int_2^x \dfrac{dt}{\ln t}$ — counts primes up to $x$ (prime number theorem).
- **Fresnel integrals.** $C(x) = \int_0^x \cos(t^2)\,dt$, $S(x) = \int_0^x \sin(t^2)\,dt$ — optics.

Computing their derivatives is trivial by FTC2: $\operatorname{erf}'(x) = \tfrac{2}{\sqrt{\pi}} e^{-x^2}$, $C'(x) = \cos(x^2)$, etc.

### 4. Duality between integration and differentiation

The two halves of FTC, read together, say that on $\mathcal{C}^0([a, b])$ (continuous functions on $[a, b]$) the operations

$$f \longmapsto G_f(x) = \int_a^x f(t)\,dt \qquad \text{and} \qquad F \longmapsto F'$$

are mutually inverse — *up to a constant*:

- **FTC2:** $\dfrac{d}{dx} \int_a^x f(t)\,dt = f(x)$. Integrate then differentiate $\Rightarrow$ recover $f$ exactly.
- **FTC1 rearranged:** $\int_a^x F'(t)\,dt = F(x) - F(a)$. Differentiate then integrate $\Rightarrow$ recover $F$ *up to the additive constant $F(a)$*.

The constant is unavoidable for a structural reason: differentiation kills constants, so the inverse cannot possibly recover them — every $F + c$ has the same derivative, and the integral can only pin down $F$ to within that one-dimensional ambiguity.

This duality is the central organizing fact of single-variable calculus. The whole story of `analyse-II` (Lebesgue integration on $\mathbb{R}^n$) is, in part, the question: *what is the right notion of integration so that this duality keeps working when $f$ is no longer continuous?*

### 5. Core techniques

Two techniques carry essentially all the working calculations done in `Analyse I` and `Analyse II`. Both are FTC1 read backwards: a derivative identity, run as an integration rule.

#### 5.1 Substitution (change of variable)

If $u = u(x)$ is differentiable and $g$ is continuous,

$$\int g(u(x))\, u'(x)\,dx = \int g(u)\,du.$$

For definite integrals, the bounds change too: with $u_1 = u(x_1)$ and $u_2 = u(x_2)$,

$$\int_{x_1}^{x_2} g(u(x))\, u'(x)\,dx = \int_{u_1}^{u_2} g(u)\,du.$$

Example: for $\int_1^2 (x^3 + 2)^4 \, x^2\,dx$, let $u = x^3 + 2$, so $du = 3x^2\,dx$. Bounds map $1 \mapsto 3$ and $2 \mapsto 10$, giving

$$\int_3^{10} u^4 \, \frac{du}{3} = \left.\frac{u^5}{15}\right|_3^{10} = \frac{10^5 - 3^5}{15}.$$

Substitution is the one-dimensional shadow of the *change-of-variable formula* in $\mathbb{R}^n$ (with a Jacobian determinant replacing $u'(x)$), which is a central object in `LU2MA211 Analyse II`.

#### 5.2 Integration by parts

Reading the product rule $(uv)' = u'v + uv'$ as an integration statement:

$$\int_a^b u(x)\, v'(x)\,dx = \bigl[u(x)\, v(x)\bigr]_a^b - \int_a^b u'(x)\, v(x)\,dx.$$

The point is to trade an integral we cannot do for one we can, by moving the derivative from $v$ onto $u$. Recurring uses: $\int x e^x\,dx$ (take $u = x$, $v' = e^x$), $\int \ln x\,dx$ (take $u = \ln x$, $v' = 1$), and a constant companion of Fourier coefficient estimates and integration-by-parts proofs in `LU2MA260 Analyse I`.

### 6. Applications (placeholder — not developed this round)

Listed as bookmarks; not worked through here. They become relevant if the topic needs a second pass before tackling `Analyse II`.

- **$\log$ via integral.** Defining $\log x = \int_1^x \tfrac{dt}{t}$ for $x > 0$ and recovering the algebraic properties of $\log$ purely from FTC + change of variable. The cleanest "axiomatic" entry into the logarithm. (MIT Lec 20 trailer; full treatment in Lec 21.)
- **Volumes by disks / shells.** $\int \pi [f(x)]^2\,dx$, $\int 2\pi x\, f(x)\,dx$. Standard physical-geometry applications.
- **Work and accumulated physical quantities.** Total work as $\int F(x)\,dx$, total charge as $\int I(t)\,dt$, etc. The "borrowing function" example in MIT Lec 18 is a version of this.
- **Numerical integration.** Trapezoid rule, Simpson's rule, error bounds. Relevant later in `LU3MA232 Analyse numérique`.

### 7. What this article deliberately leaves out

These are real and important but belong to later UEs; pulling them in here would just blur the boundaries.

- **Improper / generalized integrals** (integration over unbounded intervals or with unbounded integrands) $\to$ `LU2MA260 Analyse I`.
- **Multiple integrals, Fubini, multidimensional change of variable** $\to$ `LU2MA211 Analyse II`.
- **Lebesgue integral** (the framework that integrates functions like the Dirichlet function flagged in §1.4) $\to$ `LU2MA211 Analyse II`.

## Study log

- **2026-05-16** — Topic created. Materials 01–03 (MIT OCW lectures 18, 19, 20) downloaded; materials 04–05 (OpenStax, 3Blue1Brown) added as references without download. ROADMAP updated to mark the topic `[~]` in progress.
- **2026-05-18** — Theory section expanded from a 4-point through-line to a 7-section skeleton (titles + one-line intents). Scope deliberately bounded to Riemann + FTC + core techniques; improper, multidimensional, and Lebesgue integration left to `Analyse I` / `Analyse II`.
- **2026-05-18** — Theory section fully written: Riemann sums and Darboux integrability conditions (§1), FTC1 with its FTC2-based proof (§2), FTC2 with its average-value proof and "new functions" via integral definition (§3), the duality argument (§4), substitution and integration by parts (§5). §6 (applications) kept as bookmarks, §7 (out-of-scope) kept as boundary list. Source: MIT OCW 18.01 lectures 18–20 (materials 01–03).
