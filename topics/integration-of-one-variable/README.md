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

To be filled in conversation. The expected through-line, following the MIT lectures:

1. **Riemann sums and the definite integral.** Partitions of $[a, b]$, lower/upper sums, limit of Riemann sums, $\int_a^b f(x)\,dx$ as signed area. Conditions on $f$ for integrability (continuity is sufficient).
2. **First Fundamental Theorem of Calculus.** If $F' = f$ on $[a, b]$ and $f$ is continuous, then $\int_a^b f(x)\,dx = F(b) - F(a)$. The integral becomes computable via antiderivatives.
3. **Second Fundamental Theorem of Calculus.** If $f$ is continuous on $[a, b]$ and $G(x) = \int_a^x f(t)\,dt$, then $G$ is differentiable with $G'(x) = f(x)$. Every continuous function has an antiderivative — the integral *constructs* one.
4. **Duality with differentiation.** FTC1 and FTC2 together show that integration and differentiation are inverse operations on $\mathcal{C}^0([a, b])$, modulo an additive constant.

## Study log

- **2026-05-16** — Topic created. Materials 01–03 (MIT OCW lectures 18, 19, 20) downloaded; materials 04–05 (OpenStax, 3Blue1Brown) added as references without download. ROADMAP updated to mark the topic `[~]` in progress.
