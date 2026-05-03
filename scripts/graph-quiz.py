#!/usr/bin/env -S uv run --
"""
Graph quiz tool for studying functions ↔ graphs.

Two modes, both writing PNGs that Claude Code can show inline.

    plot <formula> [--domain LO HI] [--out PATH]
        Plot a given expression in x. Use to test "expression → graph": predict the
        shape mentally, then run this and compare.

    random [--family NAME] [--seed N] [--out PATH]
        Pick a function family from the catalog, sample clean coefficients, render
        the curve only (no label, no title), and hide the answer in a sidecar
        "<out>.answer.txt". Use to test "graph → expression": guess the family and
        coefficients, then `reveal`.

    reveal [--out PATH]
        Print the sidecar answer file for the most recent random plot.

Allowed names in expressions: x, sin, cos, tan, exp, log, sqrt, abs, pi, e
(numpy-backed). The expression is evaluated with eval — this is a personal tool,
do not feed it untrusted input.
"""

import argparse
import math
import random as rnd
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


SAFE_NS = {
    "__builtins__": {},
    "sin": np.sin, "cos": np.cos, "tan": np.tan,
    "exp": np.exp, "log": np.log, "sqrt": np.sqrt,
    "abs": np.abs, "pi": np.pi, "e": np.e,
}
DEFAULT_OUT = Path("/tmp/graph-quiz.png")


def evaluate(formula: str, x: np.ndarray) -> np.ndarray:
    ns = {**SAFE_NS, "x": x}
    with np.errstate(divide="ignore", invalid="ignore", over="ignore"):
        y = eval(formula, ns)
    return np.asarray(y, dtype=float)


def render(curves, domain, out: Path, title: str | None) -> None:
    lo, hi = domain
    fig, ax = plt.subplots(figsize=(7, 6))
    finite_pool: list[float] = []
    for ys, label in curves:
        ys_plot = np.where(np.isfinite(ys), ys, np.nan)
        ax.plot(np.linspace(lo, hi, ys.size), ys_plot, linewidth=2,
                label=label if label else None)
        finite_pool.extend(ys[np.isfinite(ys)].tolist())
    if finite_pool:
        arr = np.asarray(finite_pool)
        lo_y, hi_y = np.percentile(arr, [2, 98])
        if hi_y - lo_y < 1e-6:
            lo_y, hi_y = lo_y - 1, hi_y + 1
        pad = (hi_y - lo_y) * 0.2
        ax.set_ylim(lo_y - pad, hi_y + pad)
    ax.axhline(0, color="black", linewidth=0.6)
    ax.axvline(0, color="black", linewidth=0.6)
    ax.grid(True, which="both", alpha=0.3)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    if title:
        ax.set_title(title)
    if any(label for _, label in curves):
        ax.legend()
    fig.tight_layout()
    fig.savefig(out, dpi=120)
    plt.close(fig)


def _pick(seq, rng: rnd.Random):
    return seq[rng.randrange(len(seq))]


# Each family returns (display_name, formula_string, plot_domain). Coefficients
# are drawn from small "clean" sets so the inverse problem stays a reasoning
# exercise, not parameter fitting.
def family_linear(rng):
    a = _pick([-2, -1, -0.5, 0.5, 1, 2, 3], rng)
    b = _pick([-3, -2, -1, 0, 1, 2, 3], rng)
    return ("linear", f"{a}*x + {b}", (-5, 5))


def family_quadratic(rng):
    a = _pick([-1, -0.5, 0.5, 1, 2], rng)
    h = _pick([-2, -1, 0, 1, 2], rng)
    k = _pick([-3, -1, 0, 1, 3], rng)
    return ("quadratic (vertex form)", f"{a}*(x-({h}))**2 + ({k})", (-5, 5))


def family_rational(rng):
    a = _pick([-2, -1, 1, 2], rng)
    h = _pick([-2, -1, 0, 1, 2], rng)
    k = _pick([-2, -1, 0, 1, 2], rng)
    return ("rational (1/x shape)", f"{a}/(x-({h})) + ({k})", (h - 5, h + 5))


def family_exponential(rng):
    a = _pick([0.5, 1, 2], rng)
    b = _pick([-1, -0.5, 0.5, 1], rng)
    k = _pick([-2, -1, 0, 1, 2], rng)
    return ("exponential", f"{a}*exp({b}*x) + ({k})", (-3, 3))


def family_logarithmic(rng):
    a = _pick([-1, 0.5, 1, 2], rng)
    h = _pick([-2, -1, 0], rng)
    k = _pick([-2, -1, 0, 1, 2], rng)
    return ("logarithmic", f"{a}*log(x-({h})) + ({k})", (h + 0.05, h + 8))


def family_sine(rng):
    a = _pick([0.5, 1, 2], rng)
    b = _pick([0.5, 1, 2], rng)
    return ("sine", f"{a}*sin({b}*x)", (-2 * math.pi, 2 * math.pi))


def family_absolute(rng):
    a = _pick([-2, -1, 0.5, 1, 2], rng)
    h = _pick([-2, -1, 0, 1, 2], rng)
    k = _pick([-2, -1, 0, 1, 2], rng)
    return ("absolute value", f"{a}*abs(x-({h})) + ({k})", (-5, 5))


CATALOG = {
    "linear": family_linear,
    "quadratic": family_quadratic,
    "rational": family_rational,
    "exponential": family_exponential,
    "logarithmic": family_logarithmic,
    "sine": family_sine,
    "absolute": family_absolute,
}


def cmd_plot(args) -> int:
    xs = np.linspace(args.domain[0], args.domain[1], 1000)
    ys = evaluate(args.formula, xs)
    render([(ys, args.formula)], tuple(args.domain), args.out, title=None)
    print(f"[ok] plotted: {args.formula}  ->  {args.out}")
    return 0


def cmd_random(args) -> int:
    rng = rnd.Random(args.seed)
    name = args.family or rng.choice(list(CATALOG))
    label, formula, domain = CATALOG[name](rng)
    xs = np.linspace(domain[0], domain[1], 2000)
    ys = evaluate(formula, xs)
    render([(ys, "")], domain, args.out, title=None)
    answer = args.out.with_suffix(args.out.suffix + ".answer.txt")
    answer.write_text(
        f"family:  {label}\n"
        f"formula: {formula}\n"
        f"domain:  {domain}\n"
        f"seed:    {args.seed}\n"
    )
    print(f"[ok] random graph ({name})  ->  {args.out}")
    print(f"     formula hidden in {answer}")
    print(f"     reveal with: ./graph-quiz.py reveal --out {args.out}")
    return 0


def cmd_reveal(args) -> int:
    answer = args.out.with_suffix(args.out.suffix + ".answer.txt")
    if not answer.exists():
        print(f"no answer sidecar at {answer}", file=sys.stderr)
        return 1
    sys.stdout.write(answer.read_text())
    return 0


def main() -> int:
    p = argparse.ArgumentParser(
        description="Plot a formula or quiz yourself with a random graph.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    pp = sub.add_parser("plot", help="plot a given formula")
    pp.add_argument("formula", help="expression in x, e.g. 'x**2 - 2*x' or 'sin(x)'")
    pp.add_argument("--domain", type=float, nargs=2, default=[-5.0, 5.0],
                    metavar=("LO", "HI"))
    pp.add_argument("--out", type=Path, default=DEFAULT_OUT)
    pp.set_defaults(func=cmd_plot)

    pr = sub.add_parser("random", help="random graph from catalog (answer hidden)")
    pr.add_argument("--family", choices=sorted(CATALOG))
    pr.add_argument("--seed", type=int, default=None)
    pr.add_argument("--out", type=Path, default=DEFAULT_OUT)
    pr.set_defaults(func=cmd_random)

    rv = sub.add_parser("reveal", help="reveal the formula behind a random plot")
    rv.add_argument("--out", type=Path, default=DEFAULT_OUT)
    rv.set_defaults(func=cmd_reveal)

    args = p.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
