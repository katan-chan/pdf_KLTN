"""Vẽ minh hoạ phép chồng hai tầng của mô hình Superimposed SBM.

Output: figures/supsbm_superposition.pdf
Dùng cho: Mục 3.3.1 (Mô hình Superimposed SBM).

Bốn panel:
  (a) G_T trước khi gộp cạnh trùng (multi-edge từ các tam giác).
  (b) G_T sau khi gộp thành đồ thị nhị phân.
  (c) G_E sinh theo cơ chế SBM dyadic.
  (d) G_s = G_E hợp G_T trên cùng tập đỉnh.

Đồ thị mẫu n = 7 đỉnh chia thành hai cộng đồng:
  Cluster 1: A, B, C, D
  Cluster 2: E, F, G
Các tam giác mô hình trong G_T: {A,B,C}, {B,C,D}, {E,F,G}
  (B-C xuất hiện trong hai tam giác → multi-edge ở panel (a))
Các cạnh dyadic trong G_E: A-D, C-F, D-E
"""

from itertools import combinations
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import networkx as nx


NODES = ["A", "B", "C", "D", "E", "F", "G"]
CLUSTER = {
    "A": 0, "B": 0, "C": 0, "D": 0,
    "E": 1, "F": 1, "G": 1,
}
POS = {
    "A": (0.0, 2.0),
    "B": (1.3, 2.3),
    "C": (0.4, 0.9),
    "D": (1.8, 1.0),
    "E": (3.6, 2.1),
    "F": (3.0, 0.6),
    "G": (4.1, 0.9),
}
TRIANGLES = [("A", "B", "C"), ("B", "C", "D"), ("E", "F", "G")]
DYADIC_EDGES = [("A", "D"), ("C", "F"), ("D", "E")]

CLUSTER_COLOR = {0: "#BBDEFB", 1: "#FFE0B2"}
EDGE_COLOR = "#37474F"
MULTI_EDGE_COLOR = "#1976D2"


def draw_nodes(ax, pos):
    for v in NODES:
        x, y = pos[v]
        ax.scatter(x, y, s=620, c=CLUSTER_COLOR[CLUSTER[v]],
                   edgecolors="black", linewidths=0.9, zorder=3)
        ax.text(x, y, v, ha="center", va="center", fontsize=10,
                fontweight="bold", zorder=4)


def draw_edges(ax, pos, edges, color=EDGE_COLOR, lw=1.4):
    for u, v in edges:
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        ax.plot([x1, x2], [y1, y2], color=color, lw=lw, zorder=2)


def draw_multi_edge(ax, pos, u, v, count, color=MULTI_EDGE_COLOR, lw=1.4):
    """Vẽ count cạnh song song nối u-v dưới dạng các đường cong nhẹ."""
    if count == 1:
        draw_edges(ax, pos, [(u, v)], color=color, lw=lw)
        return
    rads = [0.0]
    step = 0.18
    for k in range(1, count):
        sign = 1 if k % 2 == 1 else -1
        magnitude = ((k + 1) // 2) * step
        rads.append(sign * magnitude)
    for rad in rads:
        arrow = FancyArrowPatch(
            posA=pos[u], posB=pos[v],
            connectionstyle=f"arc3,rad={rad}",
            arrowstyle="-",
            color=color, lw=lw, zorder=2,
        )
        ax.add_patch(arrow)


def build_triangle_multi_edges():
    counts: dict[tuple[str, str], int] = {}
    for tri in TRIANGLES:
        for u, v in combinations(tri, 2):
            key = tuple(sorted((u, v)))
            counts[key] = counts.get(key, 0) + 1
    return counts


def build_triangle_collapsed_edges():
    edges = set()
    for tri in TRIANGLES:
        for u, v in combinations(tri, 2):
            edges.add(tuple(sorted((u, v))))
    return sorted(edges)


def build_observed_edges():
    edges = set(build_triangle_collapsed_edges())
    for u, v in DYADIC_EDGES:
        edges.add(tuple(sorted((u, v))))
    return sorted(edges)


def panel_label(ax, label):
    ax.text(0.5, -0.18, label, transform=ax.transAxes,
            ha="center", va="center", fontsize=11)


def setup_axes(ax, title):
    ax.set_xlim(-0.6, 4.7)
    ax.set_ylim(0.1, 2.9)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, fontsize=11)


def main():
    fig, axes = plt.subplots(1, 4, figsize=(14, 3.4))

    # Panel (a): G_T với multi-edge
    ax = axes[0]
    setup_axes(ax, r"$G_T$ trước khi gộp")
    counts = build_triangle_multi_edges()
    for (u, v), c in counts.items():
        draw_multi_edge(ax, POS, u, v, c)
    draw_nodes(ax, POS)
    panel_label(ax, "(a)")

    # Panel (b): G_T sau khi gộp
    ax = axes[1]
    setup_axes(ax, r"$G_T$ sau khi gộp")
    draw_edges(ax, POS, build_triangle_collapsed_edges(), color=MULTI_EDGE_COLOR)
    draw_nodes(ax, POS)
    panel_label(ax, "(b)")

    # Panel (c): G_E
    ax = axes[2]
    setup_axes(ax, r"$G_E$ (tầng cạnh)")
    draw_edges(ax, POS, DYADIC_EDGES, color="#388E3C")
    draw_nodes(ax, POS)
    panel_label(ax, "(c)")

    # Panel (d): G_s
    ax = axes[3]
    setup_axes(ax, r"$G_s = G_E \cup G_T$")
    triangle_edges = set(build_triangle_collapsed_edges())
    dyadic_edges = set(tuple(sorted(e)) for e in DYADIC_EDGES)
    only_triangle = triangle_edges - dyadic_edges
    only_dyadic = dyadic_edges - triangle_edges
    both = triangle_edges & dyadic_edges
    draw_edges(ax, POS, sorted(only_triangle), color=MULTI_EDGE_COLOR)
    draw_edges(ax, POS, sorted(only_dyadic), color="#388E3C")
    draw_edges(ax, POS, sorted(both), color="#6A1B9A")
    draw_nodes(ax, POS)
    panel_label(ax, "(d)")

    plt.tight_layout()
    out_dir = Path(__file__).resolve().parent.parent / "figures"
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "supsbm_superposition.pdf"
    fig.savefig(out_path, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {out_path}")


if __name__ == "__main__":
    main()
