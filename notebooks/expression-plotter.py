import marimo

__generated_with = "0.23.5"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    import sympy as sp

    return mo, np, plt, sp


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Expression plotter

    Type an expression in $x$ (for example `x**2 - 4`, `sin(x)/x`, or
    `exp(-x**2)`) and it will be plotted on the chosen domain. The
    expression is parsed by SymPy, so `sin`, `cos`, `tan`, `exp`, `log`,
    `sqrt`, `Abs`, `pi`, `E`, etc. are available.
    """)
    return


@app.cell
def _(mo):
    expr = mo.ui.text(
        value="x**2 * sin(1/x)",
        label=r"$f(x) =$",
        full_width=True,
    )
    expr
    return (expr,)


@app.cell(hide_code=True)
def _(mo):
    x_min = mo.ui.number(value=-.5, step=0.1, label=r"$x_{\min}$")
    x_max = mo.ui.number(value=.5, step=0.1, label=r"$x_{\max}$")
    resolution = mo.ui.slider(
        start=100, stop=5000, step=100, value=1000, label="points", show_value=True
    )

    y_override = mo.ui.checkbox(value=False, label="fix $y$-axis")
    y_min = mo.ui.number(value=-.25, step=0.1, label=r"$y_{\min}$")
    y_max = mo.ui.number(value=.25, step=0.1, label=r"$y_{\max}$")

    controls = mo.hstack(
        [
            mo.vstack([mo.md("**Domain**"), x_min, x_max]),
            mo.vstack([mo.md("**$y$-axis**"), y_override, y_min, y_max]),
            mo.vstack([mo.md("**Sampling**"), resolution]),
        ],
        justify="start",
        gap=2,
    )
    controls
    return resolution, x_max, x_min, y_max, y_min, y_override


@app.cell(hide_code=True)
def _(expr, mo, sp):
    x_sym = sp.symbols("x")
    parsed = None
    error = None
    try:
        parsed = sp.sympify(expr.value, locals={"x": x_sym})
        extra = parsed.free_symbols - {x_sym}
        if extra:
            error = f"Only the variable `x` is allowed. Extra symbols: {extra}."
            parsed = None
    except (sp.SympifyError, SyntaxError, TypeError) as e:
        error = f"Cannot parse the expression: `{e}`."

    mo.stop(parsed is None, mo.md(f"⚠️ {error}"))
    mo.md(rf"$$f(x) = {sp.latex(parsed)}$$")
    return parsed, x_sym


@app.cell(hide_code=True)
def _(
    np,
    parsed,
    plt,
    resolution,
    sp,
    x_max,
    x_min,
    x_sym,
    y_max,
    y_min,
    y_override,
):
    f = sp.lambdify(x_sym, parsed, modules=["numpy"])

    lo, hi = sorted([x_min.value, x_max.value])
    if hi - lo < 1e-9:
        hi = lo + 1.0  # avoid degenerate domain; the plot stays visible

    xs = np.linspace(lo, hi, int(resolution.value))
    with np.errstate(divide="ignore", invalid="ignore", over="ignore"):
        ys = np.broadcast_to(np.asarray(f(xs), dtype=float), xs.shape).copy()
    ys = np.where(np.isfinite(ys), ys, np.nan)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(xs, ys, linewidth=2)
    ax.axhline(0, color="black", linewidth=0.6)
    ax.axvline(0, color="black", linewidth=0.6)
    ax.grid(True, alpha=0.3)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_xlim(lo, hi)

    if y_override.value:
        ylo, yhi = sorted([y_min.value, y_max.value])
        if yhi - ylo < 1e-9:
            yhi = ylo + 1.0
        ax.set_ylim(ylo, yhi)
    else:
        finite = ys[np.isfinite(ys)]
        if finite.size:
            p_lo, p_hi = np.percentile(finite, [2, 98])
            if p_hi - p_lo < 1e-6:
                p_lo, p_hi = p_lo - 1, p_hi + 1
            pad = (p_hi - p_lo) * 0.15
            ax.set_ylim(p_lo - pad, p_hi + pad)

    fig.tight_layout()
    fig
    return


if __name__ == "__main__":
    app.run()
