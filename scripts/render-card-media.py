#!/usr/bin/env -S uv run --
"""
Render static visuals embedded in Anki cards for the calculus-foundations deck.

Outputs to cards/media/calculus-foundations/. Re-running is idempotent — the
PNGs are deterministic so the deck file's <img src="..."> references stay
stable across regenerations.

Each function below produces one PNG referenced by a specific card; the file
name encodes the card GUID so the link is traceable.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[1]
MEDIA_DIR = REPO_ROOT / "cards" / "media" / "calculus-foundations"


def render_exp_vs_log(out: Path) -> None:
    fig, ax = plt.subplots(figsize=(7, 7))

    x_exp = np.linspace(-3, 2, 400)
    ax.plot(x_exp, np.exp(x_exp), color="tab:blue", linewidth=2, label="curve A")

    x_log = np.linspace(0.05, 8, 400)
    ax.plot(x_log, np.log(x_log), color="tab:orange", linewidth=2, label="curve B")

    line = np.linspace(-3, 8, 50)
    ax.plot(line, line, color="gray", linewidth=1, linestyle="--", alpha=0.7,
            label="y = x")

    ax.axhline(0, color="black", linewidth=0.6)
    ax.axvline(0, color="black", linewidth=0.6)
    ax.set_xlim(-3, 8)
    ax.set_ylim(-3, 8)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(loc="upper left")

    fig.tight_layout()
    fig.savefig(out, dpi=120)
    plt.close(fig)


def render_discontinuities(out: Path) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(13, 4.5))

    # (A) Corner: y = |x|
    x = np.linspace(-3, 3, 400)
    axes[0].plot(x, np.abs(x), color="tab:blue", linewidth=2)
    axes[0].plot([0], [0], "o", color="tab:blue", markersize=8)
    axes[0].set_title("(A)")

    # (B) Jump: y = x + 1 for x < 0, y = x - 1 for x > 0
    x_left = np.linspace(-3, -0.005, 200)
    x_right = np.linspace(0.005, 3, 200)
    axes[1].plot(x_left, x_left + 1, color="tab:blue", linewidth=2)
    axes[1].plot(x_right, x_right - 1, color="tab:blue", linewidth=2)
    axes[1].plot([0], [1], "o", markerfacecolor="white",
                 markeredgecolor="tab:blue", markersize=8)
    axes[1].plot([0], [-1], "o", color="tab:blue", markersize=8)
    axes[1].set_title("(B)")

    # (C) Removable: y = x with hole at (1, 1), filled at (1, 3)
    x_minus = np.linspace(-2, 0.99, 200)
    x_plus = np.linspace(1.01, 3, 200)
    axes[2].plot(x_minus, x_minus, color="tab:blue", linewidth=2)
    axes[2].plot(x_plus, x_plus, color="tab:blue", linewidth=2)
    axes[2].plot([1], [1], "o", markerfacecolor="white",
                 markeredgecolor="tab:blue", markersize=8)
    axes[2].plot([1], [3], "o", color="tab:blue", markersize=8)
    axes[2].set_title("(C)")

    for ax in axes:
        ax.axhline(0, color="black", linewidth=0.6)
        ax.axvline(0, color="black", linewidth=0.6)
        ax.grid(True, alpha=0.3)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_xlim(-3, 3)
        ax.set_ylim(-3.5, 3.5)

    fig.tight_layout()
    fig.savefig(out, dpi=120)
    plt.close(fig)


def main() -> None:
    MEDIA_DIR.mkdir(parents=True, exist_ok=True)
    render_exp_vs_log(MEDIA_DIR / "cf_fams_12_exp_vs_log.png")
    render_discontinuities(MEDIA_DIR / "cf_fams_13_discontinuities.png")
    print(f"wrote PNGs to {MEDIA_DIR}")


if __name__ == "__main__":
    main()
