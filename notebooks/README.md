# Notebooks

[Marimo](https://marimo.io/) notebooks for interactively experimenting with the concepts in this repository. This is a standalone `uv` project with its own `pyproject.toml` and `uv.lock`, just like `scripts/`.

## Prerequisites

- [`uv`](https://docs.astral.sh/uv/) — manages the virtual environment and dependencies.

## Running a notebook

Marimo has two main modes:

```bash
cd notebooks/

# Reactive edit mode (the usual one during study)
uv run marimo edit expression-plotter.py

# Read-only "app" mode (hides the code)
uv run marimo run expression-plotter.py
```

The first run downloads and installs dependencies into `notebooks/.venv/` (gitignored).

## Notebooks

### `expression-plotter.py`

Type an expression in $x$ (for example `x**2 - 4`, `sin(x)/x`, `exp(-x**2)`) and it is plotted on the fly. Exposed parameters:

- **Expression** — parsed by `sympy.sympify`, so `sin`, `cos`, `tan`, `exp`, `log`, `sqrt`, `Abs`, `pi`, `E`, etc. are accepted. The result is rendered in LaTeX as confirmation.
- **Domain** $[x_{\min}, x_{\max}]$ — independent number inputs.
- **$y$-axis** — autoscaled to the 2–98 percentile by default (discards asymptote spikes). Tick *fix $y$-axis* to impose manual limits.
- **Sampling** — number of points in the $x$ grid (100 to 5000).

Only the variable `x` is allowed; any other free symbol is rejected with a message.

### `expression-comparer.py`

Same as above, but with **two** expressions $f(x)$ and $g(x)$ plotted on the same axes in distinct colors (`tab:blue` for $f$, `tab:orange` for $g$). Useful for contrasting families, translations, or approximations (e.g. $\sin x$ vs. its order-3 Taylor polynomial).

Additional parameters on top of `expression-plotter.py`:

- **Show $f-g$** — overlays the difference as a dashed green line (a quick sanity check of where two curves coincide).

### `riemann-darboux-sums.py`

Same as `expression-plotter.py` (same expression $f(x)$, same domain and $y$-axis, same sampling), but adds a section to visualize the sums covered in `topics/integration-of-one-variable`: given an interval $[a, b]$ and a number of partitions $n$, it draws the rectangles of the **Darboux sums** (lower and upper) and of the **Riemann sums** (left endpoint, right endpoint, and midpoint) in two separate plots, each with its own multi-select to choose which family to show.

Added controls:

- **Interval $[a, b]$** — independent of the plot domain (the plot extends automatically to include it). If $a = b$, the notebook warns and aborts the computation.
- **Partition $n$** — slider from 1 to 200 (uniform).
- **Darboux sums** — multi-select between *Lower* (`tab:blue`) and *Upper* (`tab:red`). The $\inf$ / $\sup$ on each subinterval is approximated by densely sampling $f$ inside it, so as long as the resolution comfortably exceeds $n$ the numerical value matches the analytical one for regular $f$.
- **Riemann sums** — multi-select between *Left* (`tab:green`), *Right* (`tab:orange`), and *Midpoint* (`tab:purple`).

Below the plots there is a table with the five values and the trapezoidal rule as reference, useful to visually confirm that $L(f, P) \le S(f, P, \{c_i\}) \le U(f, P)$ and how all of them converge as the partition is refined.

### `parametric-curves-2d.py`

Define two parametric curves $\gamma_1(t) = (x_1(t), y_1(t))$ and $\gamma_2(t) = (x_2(t), y_2(t))$ on a common interval $t \in [t_{\min}, t_{\max}]$ and draws them superimposed on the plane. Useful for circles, ellipses, spirals, Lissajous figures, or comparing two trajectories.

The four components are parsed by `sympy.sympify` and only the variable `t` is allowed; any other free symbol is rejected with a message. The result is rendered in LaTeX as confirmation before plotting.

Parameters:

- **Domain in $t$** — number inputs $t_{\min}$ and $t_{\max}$ (default $[0, 2\pi]$).
- **Axes** — by default $x$ and $y$ are autoscaled to the 2–98 percentile of the sampled values of each curve. Tick *fix axes* to impose manual limits on both axes.
- **1:1 aspect** — on by default (circles look circular). Turn it off if you prefer the curve to fill the axes.
- **Sampling** — number of points in $t$ (100 to 5000).

Colors: `tab:blue` for $\gamma_1$, `tab:orange` for $\gamma_2$.
