"""Vẽ minh họa cách xây dựng đồ thị Higher Order G_M từ đồ thị gốc G.

Output: figures/higher_order_construction.pdf
Dùng cho: Mục 1.3.3 (Đồ thị Higher Order).

Hai panel:
  (a) Đồ thị gốc G với các cạnh không trọng số.
  (b) Đồ thị Higher Order G_M = (V, W^{(M)}) với M = K_3.
      Trọng số cạnh = số tam giác chứa cả hai đỉnh.

Đồ thị mẫu được chọn để minh họa ba hiện tượng cùng một lúc:
  - Trọng số cạnh khác nhau trong G_M (1 và 2).
  - Một số cạnh gốc bị xóa trong G_M (cạnh không thuộc tam giác nào).
  - Một số đỉnh trở nên cô lập trong G_M (đỉnh không thuộc tam giác nào).
"""

from itertools import combinations
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx


def build_example_graph() -> nx.Graph:
    """Đồ thị mẫu 7 đỉnh chứa 3 tam giác và một đuôi không có tam giác."""
    g = nx.Graph()
    g.add_nodes_from(range(1, 8))
    # Ba tam giác: {1,2,3}, {1,2,4}, {2,3,5}
    triangles = [(1, 2, 3), (1, 2, 4), (2, 3, 5)]
    for tri in triangles:
        for u, v in combinations(tri, 2):
            g.add_edge(u, v)
    # Đuôi không tam giác.
    g.add_edge(5, 6)
    g.add_edge(6, 7)
    return g


def motif_graph_K3(g: nx.Graph) -> nx.Graph:
    """Tính đồ thị Higher Order G_M với motif M = K_3.

    Trọng số W^{(M)}_{uv} = số tam giác trong G chứa cả u và v.
    """
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


def fixed_layout() -> dict:
    """Layout thủ công để hai panel có cùng vị trí đỉnh dễ đối chiếu."""
    return {
        1: (-1.4, 1.1),
        2: ( 0.0, 0.0),
        3: ( 0.4, 1.6),
        4: (-1.4, -1.0),
        5: ( 1.8, 0.9),
        6: ( 3.0, 0.0),
        7: ( 4.0, -0.8),
    }


def draw_original(g: nx.Graph, pos: dict, ax: plt.Axes) -> None:
    nx.draw_networkx_edges(g, pos, edge_color="#444444", width=1.6, alpha=0.85, ax=ax)
    nx.draw_networkx_nodes(
        g, pos, node_color="#A0C4FF", node_size=620,
        edgecolors="black", linewidths=1.0, ax=ax,
    )
    nx.draw_networkx_labels(
        g, pos, font_size=11, font_weight="bold", font_color="black", ax=ax,
    )
    ax.set_title("(a) Đồ thị gốc $G$", fontsize=12)
    ax.set_axis_off()
    ax.margins(0.12)


def draw_motif_graph(gm: nx.Graph, pos: dict, ax: plt.Axes) -> None:
    isolated = [v for v in gm.nodes() if gm.degree(v) == 0]
    non_isolated = [v for v in gm.nodes() if gm.degree(v) > 0]

    edges = list(gm.edges(data=True))
    edge_widths = [1.0 + 1.4 * d["weight"] for _, _, d in edges]
    nx.draw_networkx_edges(
        gm, pos,
        edgelist=[(u, v) for u, v, _ in edges],
        width=edge_widths, edge_color="#222222", alpha=0.9, ax=ax,
    )

    # Đỉnh thường: tô đậm; đỉnh cô lập: tô mờ + viền nét đứt.
    nx.draw_networkx_nodes(
        gm, pos, nodelist=non_isolated, node_color="#FFB4A2",
        node_size=620, edgecolors="black", linewidths=1.0, ax=ax,
    )
    iso_collection = nx.draw_networkx_nodes(
        gm, pos, nodelist=isolated, node_color="#EAEAEA",
        node_size=620, edgecolors="black", linewidths=1.0, ax=ax,
    )
    if iso_collection is not None:
        iso_collection.set_linestyle("dashed")
    nx.draw_networkx_labels(
        gm, pos, font_size=11, font_weight="bold", font_color="black", ax=ax,
    )

    edge_labels = {(u, v): str(d["weight"]) for u, v, d in edges}
    nx.draw_networkx_edge_labels(
        gm, pos, edge_labels=edge_labels,
        font_size=10, font_color="#B22222",
        bbox=dict(facecolor="white", edgecolor="none", pad=1.2, alpha=0.85), ax=ax,
    )
    ax.set_title("(b) Đồ thị Higher Order $G_M$ với $M = K_3$", fontsize=12)
    ax.set_axis_off()
    ax.margins(0.12)


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    out = root / "figures" / "higher_order_construction.pdf"
    out.parent.mkdir(parents=True, exist_ok=True)

    g = build_example_graph()
    gm = motif_graph_K3(g)
    pos = fixed_layout()

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    draw_original(g, pos, axes[0])
    draw_motif_graph(gm, pos, axes[1])
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)

    print(f"Saved {out}")
    print(f"  G:   {g.number_of_nodes()} đỉnh, {g.number_of_edges()} cạnh")
    print(f"  G_M: {gm.number_of_nodes()} đỉnh, {gm.number_of_edges()} cạnh có trọng số,",
          f"{sum(1 for v in gm.nodes() if gm.degree(v) == 0)} đỉnh cô lập")


if __name__ == "__main__":
    main()
