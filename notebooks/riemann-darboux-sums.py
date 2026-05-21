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
    # Sumas de Darboux y de Riemann

    Escribe una expresión en $x$ y elige el intervalo $[a, b]$ y el número
    de particiones $n$. Se dibujan dos gráficas: una con las sumas de
    Darboux (inferior $L(f, P)$ y superior $U(f, P)$) y otra con las sumas
    de Riemann (extremo izquierdo, extremo derecho y punto medio). Debajo,
    una tabla con los cinco valores numéricos más la regla del trapecio
    como referencia.

    El intervalo de integración $[a, b]$ es independiente del dominio
    mostrado: el plot se extiende automáticamente para incluir ambos. La
    aproximación del $\inf$ / $\sup$ de Darboux en cada subintervalo se
    obtiene muestreando densamente; basta con que la resolución sea
    cómodamente mayor que $n$ para que coincida con el valor analítico
    cuando $f$ es suficientemente regular.
    """)
    return


@app.cell
def _(mo):
    expr = mo.ui.text(
        value="1 - abs(sin(x))",
        label=r"$f(x) =$",
        full_width=True,
    )
    expr
    return (expr,)


@app.cell(hide_code=True)
def _(mo):
    x_min = mo.ui.number(value=-4.0, step=0.1, label=r"$x_{\min}$")
    x_max = mo.ui.number(value=4.0, step=0.1, label=r"$x_{\max}$")
    resolution = mo.ui.slider(
        start=100, stop=5000, step=100, value=1000, label="puntos", show_value=True
    )

    y_override = mo.ui.checkbox(value=False, label="fijar eje $y$")
    y_min = mo.ui.number(value=-2, step=0.5, label=r"$y_{\min}$")
    y_max = mo.ui.number(value=2, step=0.5, label=r"$y_{\max}$")

    controls = mo.hstack(
        [
            mo.vstack([mo.md("**Dominio**"), x_min, x_max]),
            mo.vstack([mo.md("**Eje $y$**"), y_override, y_min, y_max]),
            mo.vstack([mo.md("**Muestreo**"), resolution]),
        ],
        justify="start",
        gap=2,
    )
    controls
    return resolution, x_max, x_min, y_max, y_min, y_override


@app.cell(hide_code=True)
def _(mo):
    a = mo.ui.number(value=-2.0, step=0.1, label="$a$")
    b = mo.ui.number(value=2.0, step=0.1, label="$b$")
    n_parts = mo.ui.slider(
        start=1, stop=200, step=1, value=7, label="$n$", show_value=True,
    )
    darboux_sel = mo.ui.multiselect(
        options=["Inferior", "Superior"],
        value=["Inferior", "Superior"],
        label="Sumas de Darboux",
    )
    riemann_sel = mo.ui.multiselect(
        options=["Izquierda", "Derecha", "Punto medio"],
        value=["Izquierda", "Derecha"],
        label="Sumas de Riemann",
    )

    integ_controls = mo.hstack(
        [
            mo.vstack([mo.md(r"**Intervalo $[a, b]$**"), a, b]),
            mo.vstack([mo.md("**Partición**"), n_parts]),
            mo.vstack([mo.md("**Mostrar**"), darboux_sel, riemann_sel]),
        ],
        justify="start",
        gap=2,
    )
    integ_controls
    return a, b, darboux_sel, n_parts, riemann_sel


@app.cell(hide_code=True)
def _(expr, mo, sp):
    x_sym = sp.symbols("x")
    parsed = None
    error = None
    try:
        parsed = sp.sympify(expr.value, locals={"x": x_sym})
        extra = parsed.free_symbols - {x_sym}
        if extra:
            error = f"Solo se permite la variable `x`. Símbolos extra: {extra}."
            parsed = None
    except (sp.SympifyError, SyntaxError, TypeError) as e:
        error = f"No se puede interpretar la expresión: `{e}`."

    mo.stop(parsed is None, mo.md(f"⚠️ {error}"))
    mo.md(rf"$$f(x) = {sp.latex(parsed)}$$")
    return parsed, x_sym


@app.cell(hide_code=True)
def _(a, b, mo, n_parts, np, parsed, resolution, sp, x_max, x_min, x_sym):
    import warnings

    f = sp.lambdify(x_sym, parsed, modules=["numpy"])

    def _eval(xs):
        with np.errstate(divide="ignore", invalid="ignore", over="ignore"):
            raw = np.asarray(f(xs), dtype=float)
            ys = np.broadcast_to(raw, xs.shape).copy()
        return np.where(np.isfinite(ys), ys, np.nan)

    # Integration interval (degenerate case aborts downstream cells)
    lo, hi = sorted([a.value, b.value])
    mo.stop(
        hi - lo < 1e-9,
        mo.md("⚠️ El intervalo de integración es degenerado ($a = b$)."),
    )

    # Plot domain extended to always include [a, b]
    plo, phi = sorted([x_min.value, x_max.value])
    if phi - plo < 1e-9:
        phi = plo + 1.0
    xlo_plot = min(plo, lo)
    xhi_plot = max(phi, hi)
    xs_plot = np.linspace(xlo_plot, xhi_plot, int(resolution.value))
    ys_plot = _eval(xs_plot)

    n = int(n_parts.value)
    edges = np.linspace(lo, hi, n + 1)
    dx = (hi - lo) / n

    left_h = _eval(edges[:-1])
    right_h = _eval(edges[1:])
    mid_h = _eval((edges[:-1] + edges[1:]) / 2)

    # Darboux inf / sup approximated by dense sampling per subinterval.
    k = max(2, max(int(resolution.value), 50 * n) // n)
    t = np.linspace(0.0, 1.0, k)
    xs_grid = edges[:-1, None] + dx * t[None, :]
    ys_grid = _eval(xs_grid.ravel()).reshape(n, k)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        inf_h = np.nanmin(ys_grid, axis=1)
        sup_h = np.nanmax(ys_grid, axis=1)

    def _sum(h):
        return float(np.nansum(h) * dx)

    sums = {
        "Inferior": _sum(inf_h),
        "Superior": _sum(sup_h),
        "Izquierda": _sum(left_h),
        "Derecha": _sum(right_h),
        "Punto medio": _sum(mid_h),
    }

    # Trapezoidal reference on a dense grid over [a, b]
    xs_ref = np.linspace(lo, hi, max(2000, 50 * n))
    ys_ref = _eval(xs_ref)
    trapezoid = float(np.trapezoid(np.nan_to_num(ys_ref, nan=0.0), xs_ref))

    # Shared y-limits from the curve (percentile 2-98, ignores asymptotes)
    finite = ys_plot[np.isfinite(ys_plot)]
    if finite.size:
        ylo_auto, yhi_auto = np.percentile(finite, [2, 98])
        if yhi_auto - ylo_auto < 1e-6:
            ylo_auto, yhi_auto = ylo_auto - 1.0, yhi_auto + 1.0
        pad = (yhi_auto - ylo_auto) * 0.15
        ylo_auto -= pad
        yhi_auto += pad
    else:
        ylo_auto, yhi_auto = -1.0, 1.0

    sum_data = {
        "xs_plot": xs_plot,
        "ys_plot": ys_plot,
        "plot_xlim": (xlo_plot, xhi_plot),
        "edges": edges,
        "dx": dx,
        "lo": lo,
        "hi": hi,
        "heights": {
            "Inferior": inf_h,
            "Superior": sup_h,
            "Izquierda": left_h,
            "Derecha": right_h,
            "Punto medio": mid_h,
        },
        "sums": sums,
        "trapezoid": trapezoid,
        "y_auto": (ylo_auto, yhi_auto),
    }
    return (sum_data,)


@app.cell(hide_code=True)
def _(darboux_sel, plt, sum_data, y_max, y_min, y_override):
    def plot_darboux():
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(sum_data["xs_plot"], sum_data["ys_plot"], linewidth=2, color="black")
        ax.axhline(0, color="black", linewidth=0.6)
        ax.axvline(0, color="black", linewidth=0.6)
        ax.axvspan(sum_data["lo"], sum_data["hi"], color="gray", alpha=0.07)
        ax.grid(True, alpha=0.3)
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.set_title("Sumas de Darboux")
        ax.set_xlim(*sum_data["plot_xlim"])
    
        colors = {"Inferior": "tab:blue", "Superior": "tab:red"}
        for _kind in darboux_sel.value:
            h = sum_data["heights"][_kind]
            s = sum_data["sums"][_kind]
            ax.bar(
                sum_data["edges"][:-1], h, width=sum_data["dx"], align="edge",
                color=colors[_kind], alpha=0.3, edgecolor=colors[_kind],
                label=f"{_kind} ({s:.5f})",
            )
    
        if y_override.value:
            ylo, yhi = sorted([y_min.value, y_max.value])
            if yhi - ylo < 1e-9:
                yhi = ylo + 1.0
            ax.set_ylim(ylo, yhi)
        else:
            ax.set_ylim(*sum_data["y_auto"])
    
        if darboux_sel.value:
            ax.legend(loc="best")
    
        fig.tight_layout()
        return fig

    plot_darboux()
    return


@app.cell(hide_code=True)
def _(plt, riemann_sel, sum_data, y_max, y_min, y_override):
    def plot_riemann():
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(sum_data["xs_plot"], sum_data["ys_plot"], linewidth=2, color="black")
        ax.axhline(0, color="black", linewidth=0.6)
        ax.axvline(0, color="black", linewidth=0.6)
        ax.axvspan(sum_data["lo"], sum_data["hi"], color="gray", alpha=0.07)
        ax.grid(True, alpha=0.3)
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.set_title("Sumas de Riemann")
        ax.set_xlim(*sum_data["plot_xlim"])
    
        colors = {
            "Izquierda": "tab:green",
            "Derecha": "tab:orange",
            "Punto medio": "tab:purple",
        }
        for kind in riemann_sel.value:
            h = sum_data["heights"][kind]
            s = sum_data["sums"][kind]
            ax.bar(
                sum_data["edges"][:-1], h, width=sum_data["dx"], align="edge",
                color=colors[kind], alpha=0.3, edgecolor=colors[kind],
                label=f"{kind} ({s:.5f})",
            )
    
        if y_override.value:
            ylo, yhi = sorted([y_min.value, y_max.value])
            if yhi - ylo < 1e-9:
                yhi = ylo + 1.0
            ax.set_ylim(ylo, yhi)
        else:
            ax.set_ylim(*sum_data["y_auto"])
    
        if riemann_sel.value:
            ax.legend(loc="best")
    
        fig.tight_layout()
        return fig

    plot_riemann()
    return


@app.cell(hide_code=True)
def _(mo, sum_data):
    _s = sum_data["sums"]
    _rows = [
        ("Darboux inferior $L(f, P)$", _s["Inferior"]),
        ("Darboux superior $U(f, P)$", _s["Superior"]),
        ("Riemann izquierda", _s["Izquierda"]),
        ("Riemann derecha", _s["Derecha"]),
        ("Riemann punto medio", _s["Punto medio"]),
        ("Regla del trapecio (referencia)", sum_data["trapezoid"]),
    ]
    _body = "\n".join(f"| {_name} | {_val:.6f} |" for _name, _val in _rows)
    mo.md("| Suma | Valor |\n|---|---:|\n" + _body)
    return


if __name__ == "__main__":
    app.run()
