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
    # Curvas paramétricas en 2D

    Define dos curvas paramétricas $\gamma_1(t) = (x_1(t),\, y_1(t))$ y
    $\gamma_2(t) = (x_2(t),\, y_2(t))$ sobre un mismo intervalo $t \in
    [t_{\min}, t_{\max}]$ y se dibujan superpuestas en el plano. Útil
    para visualizar circunferencias, elipses, figuras de Lissajous,
    espirales, o comparar dos trayectorias.
    """)
    return


@app.cell
def _(mo):
    x1 = mo.ui.text(value="cos(t)", label=r"$x_1(t) =$", full_width=True)
    y1 = mo.ui.text(value="sin(t)", label=r"$y_1(t) =$", full_width=True)
    x2 = mo.ui.text(value="t*cos(2*pi*t) / (2*pi)", label=r"$x_2(t) =$", full_width=True)
    y2 = mo.ui.text(value="t*sin(2*pi*t) / (2*pi)", label=r"$y_2(t) =$", full_width=True)

    mo.hstack(
        [
            mo.vstack([mo.md("**Curva 1**"), x1, y1]),
            mo.vstack([mo.md("**Curva 2**"), x2, y2]),
        ],
        justify="start",
        gap=2,
        widths="equal",
    )
    return x1, x2, y1, y2


@app.cell(hide_code=True)
def _(mo):
    t_min = mo.ui.number(value=0.0, step=0.1, label=r"$t_{\min}$")
    t_max = mo.ui.number(value=6.283185307179586, step=0.1, label=r"$t_{\max}$")
    resolution = mo.ui.slider(
        start=100, stop=5000, step=100, value=1000, label="puntos", show_value=True
    )

    axes_override = mo.ui.checkbox(value=False, label="fijar ejes")
    x_min = mo.ui.number(value=-1.5, step=0.1, label=r"$x_{\min}$")
    x_max = mo.ui.number(value=1.5, step=0.1, label=r"$x_{\max}$")
    y_min = mo.ui.number(value=-1.5, step=0.1, label=r"$y_{\min}$")
    y_max = mo.ui.number(value=1.5, step=0.1, label=r"$y_{\max}$")

    equal_aspect = mo.ui.checkbox(value=True, label="aspecto 1:1")

    controls = mo.hstack(
        [
            mo.vstack([mo.md("**Dominio en $t$**"), t_min, t_max]),
            mo.vstack(
                [mo.md("**Ejes**"), axes_override, x_min, x_max, y_min, y_max]
            ),
            mo.vstack([mo.md("**Muestreo**"), resolution, equal_aspect]),
        ],
        justify="start",
        gap=2,
    )
    controls
    return (
        axes_override,
        equal_aspect,
        resolution,
        t_max,
        t_min,
        x_max,
        x_min,
        y_max,
        y_min,
    )


@app.cell(hide_code=True)
def _(mo, sp, x1, x2, y1, y2):
    t_sym = sp.symbols("t")

    def _parse(src: str):
        try:
            e = sp.sympify(src, locals={"t": t_sym})
        except (sp.SympifyError, SyntaxError, TypeError) as exc:
            return None, f"`{exc}`"
        extra = e.free_symbols - {t_sym}
        if extra:
            return None, f"símbolos extra: {extra}"
        return e, None

    parsed_x1, err_x1 = _parse(x1.value)
    parsed_y1, err_y1 = _parse(y1.value)
    parsed_x2, err_x2 = _parse(x2.value)
    parsed_y2, err_y2 = _parse(y2.value)

    problems = []
    for label, err in [
        ("$x_1$", err_x1),
        ("$y_1$", err_y1),
        ("$x_2$", err_x2),
        ("$y_2$", err_y2),
    ]:
        if err:
            problems.append(f"- {label}: {err}")

    mo.stop(
        problems,
        mo.md("⚠️ No se puede interpretar la expresión:\n\n" + "\n".join(problems)),
    )

    mo.md(
        rf"""
        $$\gamma_1(t) = \bigl({sp.latex(parsed_x1)},\; {sp.latex(parsed_y1)}\bigr)
        \qquad
        \gamma_2(t) = \bigl({sp.latex(parsed_x2)},\; {sp.latex(parsed_y2)}\bigr)$$
        """
    )
    return parsed_x1, parsed_x2, parsed_y1, parsed_y2, t_sym


@app.cell(hide_code=True)
def _(
    axes_override,
    equal_aspect,
    np,
    parsed_x1,
    parsed_x2,
    parsed_y1,
    parsed_y2,
    plt,
    resolution,
    sp,
    t_max,
    t_min,
    t_sym,
    x_max,
    x_min,
    y_max,
    y_min,
):
    fx1 = sp.lambdify(t_sym, parsed_x1, modules=["numpy"])
    fy1 = sp.lambdify(t_sym, parsed_y1, modules=["numpy"])
    fx2 = sp.lambdify(t_sym, parsed_x2, modules=["numpy"])
    fy2 = sp.lambdify(t_sym, parsed_y2, modules=["numpy"])

    lo, hi = sorted([t_min.value, t_max.value])
    if hi - lo < 1e-9:
        hi = lo + 1.0  # avoid degenerate interval; the plot stays visible

    ts = np.linspace(lo, hi, int(resolution.value))

    def _eval(f):
        with np.errstate(divide="ignore", invalid="ignore", over="ignore"):
            vs = np.broadcast_to(np.asarray(f(ts), dtype=float), ts.shape).copy()
        return np.where(np.isfinite(vs), vs, np.nan)

    xs1, ys1 = _eval(fx1), _eval(fy1)
    xs2, ys2 = _eval(fx2), _eval(fy2)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(
        xs1, ys1, linewidth=2, color="tab:blue",
        label=rf"$\gamma_1 = ({sp.latex(parsed_x1)},\, {sp.latex(parsed_y1)})$",
    )
    ax.plot(
        xs2, ys2, linewidth=2, color="tab:orange",
        label=rf"$\gamma_2 = ({sp.latex(parsed_x2)},\, {sp.latex(parsed_y2)})$",
    )

    ax.axhline(0, color="black", linewidth=0.6)
    ax.axvline(0, color="black", linewidth=0.6)
    ax.grid(True, alpha=0.3)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(loc="best")

    if axes_override.value:
        xlo, xhi = sorted([x_min.value, x_max.value])
        if xhi - xlo < 1e-9:
            xhi = xlo + 1.0
        ylo, yhi = sorted([y_min.value, y_max.value])
        if yhi - ylo < 1e-9:
            yhi = ylo + 1.0
        ax.set_xlim(xlo, xhi)
        ax.set_ylim(ylo, yhi)
    else:
        x_pool = np.concatenate([v[np.isfinite(v)] for v in [xs1, xs2]])
        y_pool = np.concatenate([v[np.isfinite(v)] for v in [ys1, ys2]])
        if x_pool.size:
            p_lo, p_hi = np.percentile(x_pool, [2, 98])
            if p_hi - p_lo < 1e-6:
                p_lo, p_hi = p_lo - 1, p_hi + 1
            pad = (p_hi - p_lo) * 0.15
            ax.set_xlim(p_lo - pad, p_hi + pad)
        if y_pool.size:
            p_lo, p_hi = np.percentile(y_pool, [2, 98])
            if p_hi - p_lo < 1e-6:
                p_lo, p_hi = p_lo - 1, p_hi + 1
            pad = (p_hi - p_lo) * 0.15
            ax.set_ylim(p_lo - pad, p_hi + pad)

    if equal_aspect.value:
        ax.set_aspect("equal", adjustable="datalim")

    fig.tight_layout()
    fig
    return


if __name__ == "__main__":
    app.run()
