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
    # Comparador de expresiones

    Escribe dos expresiones en $x$ y se grafican simultáneamente sobre los
    mismos ejes, con colores distintos. Útil para contrastar familias
    ($x^2$ vs $x^3$), traslaciones ($f(x)$ vs $f(x-1)$) o aproximaciones
    ($\sin x$ vs su Taylor de orden 3).
    """)
    return


@app.cell
def _(mo):
    expr_a = mo.ui.text(value="x**2", label=r"$f(x) =$", full_width=True)
    expr_b = mo.ui.text(value="x**3", label=r"$g(x) =$", full_width=True)
    mo.vstack([expr_a, expr_b])
    return expr_a, expr_b


@app.cell(hide_code=True)
def _(mo):
    x_min = mo.ui.number(value=-5.0, step=0.5, label=r"$x_{\min}$")
    x_max = mo.ui.number(value=5.0, step=0.5, label=r"$x_{\max}$")
    resolution = mo.ui.slider(
        start=100, stop=5000, step=100, value=1000, label="puntos", show_value=True
    )

    y_override = mo.ui.checkbox(value=False, label="fijar eje $y$")
    y_min = mo.ui.number(value=-10.0, step=1.0, label=r"$y_{\min}$")
    y_max = mo.ui.number(value=10.0, step=1.0, label=r"$y_{\max}$")

    show_diff = mo.ui.checkbox(value=False, label="mostrar $f-g$")

    controls = mo.hstack(
        [
            mo.vstack([mo.md("**Dominio**"), x_min, x_max]),
            mo.vstack([mo.md("**Eje $y$**"), y_override, y_min, y_max]),
            mo.vstack([mo.md("**Muestreo**"), resolution, show_diff]),
        ],
        justify="start",
        gap=2,
    )
    controls
    return resolution, show_diff, x_max, x_min, y_max, y_min, y_override


@app.cell(hide_code=True)
def _(expr_a, expr_b, mo, sp):
    x_sym = sp.symbols("x")

    def _parse(src: str):
        try:
            e = sp.sympify(src, locals={"x": x_sym})
        except (sp.SympifyError, SyntaxError, TypeError) as exc:
            return None, f"`{exc}`"
        extra = e.free_symbols - {x_sym}
        if extra:
            return None, f"símbolos extra: {extra}"
        return e, None

    parsed_a, err_a = _parse(expr_a.value)
    parsed_b, err_b = _parse(expr_b.value)

    problems = []
    if err_a:
        problems.append(f"- $f$: {err_a}")
    if err_b:
        problems.append(f"- $g$: {err_b}")

    mo.stop(
        problems,
        mo.md("⚠️ No se puede interpretar la expresión:\n\n" + "\n".join(problems)),
    )

    mo.md(
        rf"""
        $$f(x) = {sp.latex(parsed_a)} \qquad g(x) = {sp.latex(parsed_b)}$$
        """
    )
    return parsed_a, parsed_b, x_sym


@app.cell(hide_code=True)
def _(
    np,
    parsed_a,
    parsed_b,
    plt,
    resolution,
    show_diff,
    sp,
    x_max,
    x_min,
    x_sym,
    y_max,
    y_min,
    y_override,
):
    f_a = sp.lambdify(x_sym, parsed_a, modules=["numpy"])
    f_b = sp.lambdify(x_sym, parsed_b, modules=["numpy"])

    lo, hi = sorted([x_min.value, x_max.value])
    if hi - lo < 1e-9:
        hi = lo + 1.0

    xs = np.linspace(lo, hi, int(resolution.value))

    def _eval(f):
        with np.errstate(divide="ignore", invalid="ignore", over="ignore"):
            ys = np.broadcast_to(np.asarray(f(xs), dtype=float), xs.shape).copy()
        return np.where(np.isfinite(ys), ys, np.nan)

    ys_a = _eval(f_a)
    ys_b = _eval(f_b)

    fig, ax = plt.subplots(figsize=(8, 6))
    # Tab10 picks: distinct hues, colorblind-friendly, readable on white.
    ax.plot(xs, ys_a, linewidth=2, color="tab:blue", label=f"$f(x) = {sp.latex(parsed_a)}$")
    ax.plot(xs, ys_b, linewidth=2, color="tab:orange", label=f"$g(x) = {sp.latex(parsed_b)}$")
    if show_diff.value:
        ax.plot(
            xs, ys_a - ys_b, linewidth=1.5, color="tab:green", linestyle="--",
            label="$f - g$",
        )

    ax.axhline(0, color="black", linewidth=0.6)
    ax.axvline(0, color="black", linewidth=0.6)
    ax.grid(True, alpha=0.3)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_xlim(lo, hi)
    ax.legend(loc="best")

    if y_override.value:
        ylo, yhi = sorted([y_min.value, y_max.value])
        if yhi - ylo < 1e-9:
            yhi = ylo + 1.0
        ax.set_ylim(ylo, yhi)
    else:
        pool = [ys_a, ys_b] + ([ys_a - ys_b] if show_diff.value else [])
        finite = np.concatenate([y[np.isfinite(y)] for y in pool])
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
