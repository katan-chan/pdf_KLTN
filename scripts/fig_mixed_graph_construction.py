"""Vẽ minh họa cách xây dựng đồ thị hỗn hợp G_lambda từ G và G_M.

Output: figures/mixed_graph_construction.pdf
Dùng cho: Mục 2.1 (Đồ thị hỗn hợp).

Ba panel:
  (a) Đồ thị gốc G, cạnh không trọng số.
  (b) Đồ thị Higher Order G_M = (V, W^(M)).
  (c) Đồ thị hỗn hợp G_lambda = (V, A + lambda * W^(M)).

Đồ thị mẫu được lấy giống Mục 1.3.3 để hai hình đối chiếu được:
  - 7 đỉnh, 3 tam giác {1,2,3}, {1,2,4}, {2,3,5}.
  - Đuôi 5--6--7 không nằm trong tam giác.
"""

from itertools import combinations
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx


LAMBDA = 1.0


def build_example_graph() -> nx.Graph:
    g = nx.Graph()
    g.add_nodes_from(range(1, 8))
    triangles = [(1, 2, 3), (1, 2, 4), (2, 3, 5)]
    for tri in triangles:
        for u, v in combinations(tri, 2):
            g.add_edge(u, v)
    g.add_edge(5, 6)
    g.add_edge(6, 7)
    return g


def motif_graph_K3(g: nx.Graph) -> nx.Graph:
    triangles_per_pair: dict[tuple[int, int], int] = {}
    nodes = sorted(g.nodes())
    for a, b, c in combinations(nodes, 3):
        if g.has_edge(a, b) and g.has_edge(b, c) and g.has_edge(a, c):
            for u, v in [(a, b), (a, c), (b, c)]:
                key = (u, v) if u < v else (v, u)
                triangles_per_pair[key] = triangles_per_pair.get(key, 0) + 1
    gm = nx.Graph()
    gm.add_nodes_from(nodes)
    for (u, v), w in triangles_per_pair.items():
        gm.add_edge(u, v, weight=w)
    return gm


def mixed_graph(g: nx.Graph, gm: nx.Graph, lam: float) -> nx.Graph:
    gl = nx.Graph()
    gl.add_nodes_from(sorted(g.nodes()))
    edges = set(g.edges()) | set(gm.edges())
    for u, v in edges:
        a = 1.0 if g.has_edge(u, v) else 0.0
        wm = gm[u][v]["weight"] if gm.has_edge(u, v) else 0.0
        gl.add_edge(u, v, weight=a + lam * wm)
    return gl


def fixed_layout() -> dict:
    return {
        1: (-1.4, 1.1),
        2: ( 0.0, 0.0),
        3: ( 0.4, 1.6),
        4: (-1.4, -1.0),
        5: ( 1.8, 0.9),
        6: ( 3.0, 0.0),
        7: ( 4.0, -0.8),
    }


def draw_unweighted(g: nx.Graph, pos: dict, ax: plt.Axes, title: str) -> None:
    nx.draw_networkx_edges(g, pos, edge_color="#444444", width=1.6, alpha=0.85, ax=ax)
    nx.draw_networkx_nodes(
        g, pos, node_color="#A0C4FF", node_size=620,
        edgecolors="black", linewidths=1.0, ax=ax,
    )
    nx.draw_networkx_labels(g, pos, font_size=11, font_weight="bold", ax=ax)
    ax.set_title(title, fontsize=12)
    ax.set_axis_off()
    ax.margins(0.12)


def draw_weighted(
    g: nx.Graph, pos: dict, ax: plt.Axes, title: str,
    node_color: str, isolate_color=None,
) -> None:
    isolated = [v for v in g.nodes() if g.degree(v) == 0]
    non_iso = [v for v in g.nodes() if g.degree(v) > 0]

    edges = list(g.edges(data=True))
    widths = [1.0 + 1.4 * d["weight"] for _, _, d in edges]
    nx.draw_networkx_edges(
        g, pos, edgelist=[(u, v) for u, v, _ in edges],
        width=widths, edge_color="#222222", alpha=0.9, ax=ax,
    )
    nx.draw_networkx_nodes(
        g, pos, nodelist=non_iso, node_color=node_color,
        node_size=620, edgecolors="black", linewidths=1.0, ax=ax,
    )
    if isolated:
        iso_col = nx.draw_networkx_nodes(
            g, pos, nodelist=isolated,
            node_color=isolate_color or "#EAEAEA",
            node_size=620, edgecolors="black", linewidths=1.0, ax=ax,
        )
        if iso_col is not None:
            iso_col.set_linestyle("dashed")
    nx.draw_networkx_labels(g, pos, font_size=11, font_weight="bold", ax=ax)

    edge_labels = {
        (u, v): (f"{d['weight']:.0f}" if float(d["weight"]).is_integer()
                 else f"{d['weight']:.1f}")
        for u, v, d in edges
    }
    nx.draw_networkx_edge_labels(
        g, pos, edge_labels=edge_labels,
        font_size=10, font_color="#B22222",
        bbox=dict(facecolor="white", edgecolor="none", pad=1.2, alpha=0.85), ax=ax,
    )
    ax.set_title(title, fontsize=12)
    ax.set_axis_off()
    ax.margins(0.12)


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    out = root / "figures" / "mixed_graph_construction.pdf"
    out.parent.mkdir(parents=True, exist_ok=True)

    g = build_example_graph()
    gm = motif_graph_K3(g)
    gl = mixed_graph(g, gm, LAMBDA)
    pos = fixed_layout()

    fig, axes = plt.subplots(1, 3, figsize=(17, 5))
    draw_unweighted(g, pos, axes[0], "(a) Đồ thị gốc $G$")
    draw_weighted(
        gm, pos, axes[1],
        "(b) Đồ thị Higher Order $G_M$ với $M = K_3$",
        node_color="#FFB4A2",
    )
    draw_weighted(
        gl, pos, axes[2],
        rf"(c) Đồ thị hỗn hợp $G_\lambda$ với $\lambda = {LAMBDA:g}$",
        node_color="#B5E48C",
    )
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)

    print(f"Saved {out}")
    print(f"  G:        {g.number_of_nodes()} đỉnh, {g.number_of_edges()} cạnh")
    print(f"  G_M:      {gm.number_of_nodes()} đỉnh, {gm.number_of_edges()} cạnh,",
          f"{sum(1 for v in gm.nodes() if gm.degree(v) == 0)} đỉnh cô lập")
    print(f"  G_lambda: {gl.number_of_nodes()} đỉnh, {gl.number_of_edges()} cạnh,",
          f"{sum(1 for v in gl.nodes() if gl.degree(v) == 0)} đỉnh cô lập")


if __name__ == "__main__":
    main()
