# Roadmap

Living index of the math curriculum being built here. The medium-term anchor is the [UPMC *Licence de mathématiques à distance*](https://sciences.sorbonne-universite.fr/formation-sciences/offre-de-formation/enseignement-distance/licence-de-mathematiques-distance) (L2 + L3), which I plan to enroll in for the 2027–2028 academic year. The roadmap mixes already-covered material with the UPMC syllabus so that the prerequisites are in place by then.

## Status legend

- `[ ]` candidate — identified as a future topic, not started.
- `[~]` in progress — material added, conversation under way, no cards yet.
- `[x]` covered — at least one round of cards exists in `cards/`, and the concepts have entered the spaced repetition rotation.

## Foundations covered so far

- `[x]` [**calculus-foundations**](https://www.youtube.com/watch?v=MaszunEszVM) — functions, injectivity, surjectivity, bijectivity, composition, inverse, function families, algebra, trigonometry. 38 cards.
- `[x]` [**limits-and-derivatives**](https://youtu.be/sInn2CkPRWs) — limits as the formal "approaching" tool, derivatives as instantaneous rate of change, full Fermat → Rolle → Lagrange → Cauchy → L'Hôpital proof chain. 22 cards.

## L1 prerequisites — to round off before entering L2

Topics that the UPMC L2 program assumes as already mastered. Sequence them before tackling the UPMC UEs.

- `[ ]` **set-theory-basics** — sets, relations, functions as relations, equivalence and order relations, quotient sets.
- `[ ]` **logic-and-proof** — propositional/predicate logic, quantifiers, proof techniques (direct, contrapositive, contradiction, induction).
- `[ ]` **real-numbers-and-sequences** — construction of $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$; convergence of sequences; Bolzano–Weierstrass in $\mathbb{R}$; completeness.
- `[ ]` **continuity** — $\varepsilon$–$\delta$ continuity, IVT, extreme value theorem, uniform continuity (motivation for L2 topology).
- `[ ]` **linear-algebra-basics** — vector spaces, bases, dimension, linear maps, matrices, rank, determinants in low dimension.
- `[~]` [**integration-of-one-variable**](topics/integration-of-one-variable/README.md) — Riemann integral, fundamental theorem of calculus, integration techniques (warm-up for `analyse-II`). Three MIT OCW 18.01 lecture notes (def. integrals + FTC I & II) downloaded; OpenStax and 3Blue1Brown wired in as references.

## UPMC L2 — Semester 3 (S3)

Source: [L2 2025-2026 UE descriptors (PDF)](https://www.licence.math.upmc.fr/offre_de_formation/unites_enseignement/fichiers/13/37/NouvelleMaquetteSynopsis.pdf).

- `[ ]` **LU2MA260 — Analyse I** (6 ECTS). $\limsup/\liminf$, Landau notation, generalized integrals; numerical series (Riemann, Bertrand, alternating); Cauchy sequences and completeness of $\mathbb{R}, \mathbb{C}$; sequences of functions (simple/uniform/normal convergence); power series and radius of convergence; Fourier series (Dirichlet, Parseval). Suggested slug: `series-and-function-sequences`.
- `[ ]` **LU2MA221 — Algèbre I** (6 ECTS). Groups, rings, fields, vector spaces; morphisms, kernels, images, ideals; arithmetic in $\mathbb{Z}$ and $k[X]$, Euclidean division, principal rings, primes and factorization; linear forms and duality (a non-zero linear form has hyperplane kernel); symmetric bilinear forms, quadratic forms, signature, positive-definite forms and inner products. Suggested slug: `algebra-I`.
- `[ ]` **LU2MA216 — Topologie et calcul différentiel** (6 ECTS). Norms on $\mathbb{R}^d$ and their equivalence; Cauchy–Schwarz; open/closed/compact subsets via Bolzano–Weierstrass; continuity via balls; extreme value theorem; partial derivatives, Jacobian matrix, differentiability, $\mathcal{C}^1$ functions, chain rule, mean value inequality; $\mathcal{C}^2$ functions; first- and second-order extremum conditions on open and compact domains. Suggested slug: `topology-and-differential-calculus`.
- `[ ]` **LU2MA220 — Algèbre et arithmétique** (6 ECTS). Likely follow-on to Algèbre I covering congruences in $\mathbb{Z}/n\mathbb{Z}$ and $k[X]/(P)$, Chinese remainder theorem, Fermat's little theorem, Euler's theorem (cross-check with `UL2MA322` content). Suggested slug: `algebra-arithmetic`.
- `[ ]` **LU2MA226 — Combinatoire et graphes** (6 ECTS). Counting (binomial/multinomial coefficients, inclusion–exclusion), formal power series and linear recurrences; graphs and representations, isomorphism, handshake lemma; chains/cycles/paths, connectedness, distance, Eulerian and Hamiltonian graphs, trees and forests; colorings, bipartite graphs, matchings, planarity. Suggested slug: `combinatorics-and-graphs`.

## UPMC L2 — Semester 4 (S4)

- `[ ]` **LU2MA241 — Probabilités I** (6 ECTS). Probability vocabulary on finite sets; events, probability measures; independence, conditional probability, Bayes' formula; discrete random variables, standard laws, cdf, expectation, variance, transfer formula; Markov and Bienaymé–Tchebychev inequalities; convergence in probability and weak law of large numbers; generating functions; introduction to Markov chains on countable state spaces (transition matrix, classification of states, invariant law, hitting times). Suggested slug: `discrete-probability`.
- `[ ]` **LU2MA100 — Python** (3 ECTS). Programming for numerical / data work. Suggested slug: `python-scientific`.
- `[ ]` **LU2MA211 — Analyse II (Intégrale de Lebesgue sur $\mathbb{R}^n$)** (6 ECTS). Riemann and generalized integrals; multidimensional integration (Fubini, change of variable, introduction to Green–Riemann); dominated convergence (proved in a simplified setting), Beppo–Levi; regularity of parameter integrals; convolution and approximations of the identity; Fourier transform. Suggested slug: `lebesgue-integration`.
- `[ ]` **LU2MA222 — Algèbre linéaire et bilinéaire IIa** (6 ECTS). Symmetric group and determinant; characteristic and minimal polynomials, annihilating polynomials, generalized eigenspaces, kernel lemma; Cayley–Hamilton, diagonalizability in the split case with simple roots; Jordan decomposition (nilpotent endomorphisms, triangulation over $\mathbb{C}$), matrix exponential, applications to linear ODEs and linear recurrences. Suggested slug: `algebra-II-jordan`.
- `[ ]` **LU2MA236 — Équations différentielles** (6 ECTS). Standard ODE course (specific syllabus to be confirmed from the L2 PDF when the UE description is published). Likely: linear ODEs, Cauchy–Lipschitz, qualitative study, simple non-linear examples. Suggested slug: `differential-equations`.
- `[ ]` **LU2LVAN2 — Anglais** (3 ECTS). Not a math UE; skip from study plan.

## UPMC L3 — Semester 5 (S5)

Source: [L3 2021-2022 UE descriptors (PDF)](https://www.licence.math.upmc.fr/offre_de_formation/unites_enseignement/fichiers/11/34/Contenus_L3_21-22.pdf).

- `[ ]` **LU3MA263 — Théorie de la mesure et probabilités** (6 ECTS). Sigma-algebras (tribes), Borel tribe, generated tribes; measures, Lebesgue measure on $\mathbb{R}^d$, Stieltjes measures; monotone classes and uniqueness of extension; measurable functions, integrals, Fatou's lemma, monotone and dominated convergence; almost-everywhere notions; image measure, abstract change of variable; parameter integrals; product measures and Fubini. Suggested slug: `measure-theory`.
- `[ ]` **LU3MA360 — Topologie et calcul différentiel** (9 ECTS) — corresponds to **LU3MA260** in the on-site cursus. Metric spaces (open, interior, topology, continuity, equivalent vs topologically equivalent distances); products and function spaces; completeness, fixed-point theorem, Baire's theorem; compactness, extracted sequences, adherence, uniform continuity; connectedness, path-connectedness; normed vector spaces, Banach spaces, Riesz's theorem; differential and partial derivatives, computation rules, free extrema, gradient; $\mathcal{C}^1$ maps, diffeomorphisms, local inversion theorem, implicit function theorem. Suggested slug: `topology-II-and-differential-calculus-II`.
- `[ ]` **LU3MA232 — Analyse numérique** (6 ECTS). ODEs: Cauchy problem, Cauchy–Lipschitz, Grönwall's lemma; numerical schemes (implicit/explicit, one-step/multistep), Euler's scheme; linear systems (direct/iterative, LU decomposition); stability, consistency, convergence, order; Taylor, Runge–Kutta, Adams schemes, Butcher tableau; Newton's method for $g(x)=0$; gradient method; numerical integration and interpolation. Suggested slug: `numerical-analysis-ode`.
- `[ ]` **LU3MA270 — Algèbre** (6 ECTS). Monoids, groups, rings, morphisms, isomorphisms; subgroups, generators, $\mathbb{Z}$-morphisms; equivalence relations and quotients, factorization; quotients by subgroups, Lagrange's theorem, normal subgroups; symmetric group; quotient rings; finite abelian groups and classification, Chinese remainder, Euler totient; group actions, Sylow theorems. Reference page: [F. Paugam](https://webusers.imj-prg.fr/~frederic.paugam/parts-fr/enseignement-actuel.html). Suggested slug: `algebra-III-groups`.
- `[ ]` **LU3LV001 — Anglais** (3 ECTS). Not a math UE; skip.

## UPMC L3 — Semester 6 (S6)

Core (all required):

- `[ ]` **LU3MA210 — Analyse fonctionnelle** (6 ECTS). Hölder, Minkowski, Jensen inequalities; normed vector spaces and Banach spaces, duality; $\mathscr{L}^p$ and $L^p$ spaces, Riesz–Fischer (completeness); Radon–Nikodym theorem; regularity and density theorems; convolution of functions and measures; Fourier transform on $\mathbb{R}$, injectivity and inversion formula. Suggested slug: `functional-analysis`.
- `[ ]` **LU3MA261 — Calcul différentiel et optimisation** (6 ECTS). Unconstrained continuous optimization: differential and convex analysis recalls, existence/uniqueness, first-order optimality, Newton's method, gradient method, quadratic optimization; constrained optimization: sub-manifolds, Lagrange multipliers, Karush–Kuhn–Tucker conditions, convex optimization. Course page: [P. Tan](https://sites.google.com/view/paulinetan/enseignement/3ma261). Suggested slug: `differential-calculus-and-optimization`.
- `[ ]` **LU3MA290 — Probabilités II** (6 ECTS). Measure-theoretic probability: probabilized space, random variables, expectation, variance, inequalities, laws and joint laws; independence, Borel–Cantelli; convergence of random variables, law of large numbers, characteristic function, convergence in law, central limit theorem; Gaussian vectors and multidimensional CLT; asymptotic tribe, Kolmogorov's 0–1 law, Kolmogorov's maximal inequality, convergence of random series, three-series theorem. Suggested slug: `measure-theoretic-probability`.

Pick one from each pair:

- `[ ]` **LU3MA247 — Statistique** (6 ECTS) — inferential statistics: convergences (law, probability, almost sure, quadratic mean); classical inequalities and limit theorems, strong LLN, CLT, continuity theorem, Slutsky's lemma; estimation (method of moments, MLE, bias); confidence intervals, quantiles, Gaussian case; Gaussian vectors, Cochran's theorem, statistical tests. Suggested slug: `inferential-statistics`.
- `[ ]` **LU3MA266 — Analyse complexe** (6 ECTS) — holomorphic functions: complex plane, Cauchy–Riemann equations, angle preservation; exp, trig, complex log, powers; curvilinear integrals and holomorphic primitives, Cauchy's theorem on star-shaped open sets, fundamental theorem; index theory; homotopic Cauchy theorem; Liouville, Morera, Riemann; series of holomorphic functions; maximum principle; Laurent series and classification of singularities; residue theorem and logarithmic residues; applications to integrals. Suggested slug: `complex-analysis`.

- `[ ]` **LU3MA209 — Histoire des mathématiques** (6 ECTS) — history of geometry, algebra and analysis from Greek antiquity to the first half of the 20th century. Course page: [D. Aubin](https://webusers.imj-prg.fr/~david.aubin/cours/lu3ma209.html). Suggested slug: `history-of-mathematics`.
- `[ ]` **LU3MA250 — Formule de Stokes et EDP** (6 ECTS) — generalization of the fundamental theorem of calculus to higher dimensions: definition of surfaces, perpendicular vectors, regular open sets, surface integrals; Green's formula (special case of Stokes); applications to gravitation, electrostatics, and fluid mechanics. Suggested slug: `stokes-formula-and-pde`.

## Sources

- Distance learning program page: <https://sciences.sorbonne-universite.fr/formation-sciences/offre-de-formation/enseignement-distance/licence-de-mathematiques-distance>
- UE descriptor index: <https://www.licence.math.upmc.fr/offre_de_formation/unites_enseignement/>
- L2 UE descriptors (2025–2026): [PDF](https://www.licence.math.upmc.fr/offre_de_formation/unites_enseignement/fichiers/13/37/NouvelleMaquetteSynopsis.pdf)
- L3 UE descriptors (2021–2022): [PDF](https://www.licence.math.upmc.fr/offre_de_formation/unites_enseignement/fichiers/11/34/Contenus_L3_21-22.pdf)

## Notes on sequencing

- Order is decided per-iteration, not committed in advance. The principle: the next topic should rest on what is already in `cards/` (in active spaced repetition rotation), so each step compounds rather than stacking on shaky foundations.
- The "L1 prerequisites" block should ideally be cleared before tackling L2 S3, because the UPMC topology and analysis I courses lean heavily on a working command of $\varepsilon$–$\delta$ continuity, real-number completeness, and linear algebra in finite dimension.
- Within each semester, suggested entry points:
  - **L2 S3:** Algèbre I → Analyse I → Topologie et calcul différentiel; Combinatoire et graphes is largely independent.
  - **L2 S4:** Analyse II builds on Analyse I; Algèbre II builds on Algèbre I; Probabilités I is self-contained on top of basic combinatorics.
  - **L3 S5:** Théorie de la mesure relies on Analyse II; Topologie et calcul différentiel II extends LU2MA216; Algèbre extends LU2MA221/220.
  - **L3 S6:** Analyse fonctionnelle and Probabilités II both rest on the measure-theory UE; Calcul différentiel et optimisation builds on Topologie II.
- The UE codes between the distance learning page (LU2MA…) and the L2 2025–2026 descriptor PDF (UL2MA…) differ slightly because UPMC has been transitioning naming conventions. Cross-check by title rather than code when in doubt.
