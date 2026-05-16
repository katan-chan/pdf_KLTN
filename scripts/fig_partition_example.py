"""Vẽ minh họa một phân hoạch đồ thị với 20 đỉnh và 4 cụm.

Output: figures/partition_example.png
Dùng cho: Mục 1.1 Phát biểu bài toán (Chương 1).
"""

from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def build_graph(seed: int = 7) -> tuple[nx.Graph, list[list[int]]]:
    """Sinh đồ thị 20 đỉnh, 4 cụm dạng SBM.

    Mỗi cụm 5 đỉnh; cạnh nội cụm dày, cạnh liên cụm thưa.
    """
    rng = np.random.default_rng(seed)
    cluster_sizes = [5, 5, 5, 5]
    p_in, p_out = 0.75, 0.06

    g = nx.Graph()
    clusters: list[list[int]] = []
    next_id = 0
    for size in cluster_sizes:
        members = list(range(next_id, next_id + size))
        clusters.append(members)
        g.add_nodes_from(members)
        next_id += size

    n = g.number_of_nodes()
    for u in range(n):
        for v in range(u + 1, n):
            cu = next(i for i, c in enumerate(clusters) if u in c)
            cv = next(i for i, c in enumerate(clusters) if v in c)
            p = p_in if cu == cv else p_out
            if rng.random() < p:
                g.add_edge(u, v)

    # Đảm bảo đồ thị liên thông để minh họa rõ ràng.
    if not nx.is_connected(g):
        comps = list(nx.connected_components(g))
        for a, b in zip(comps, comps[1:]):
            g.add_edge(next(iter(a)), next(iter(b)))

    return g, clusters


def draw(g: nx.Graph, clusters: list[list[int]], outpath: Path) -> None:
    palette = ["#4C72B0", "#DD8452", "#55A868", "#C44E52"]
    color_map = {}
    for i, members in enumerate(clusters):
        for v in members:
            color_map[v] = palette[i]

    pos = nx.spring_layout(g, seed=42, k=0.9, iterations=200)

    fig, ax = plt.subplots(figsize=(7.5, 5.5))

    # Phân loại cạnh nội cụm và cạnh liên cụm.
    intra_edges, inter_edges = [], []
    membership = {v: i for i, c in enumerate(clusters) for v in c}
    for u, v in g.edges():
        (intra_edges if membership[u] == membership[v] else inter_edges).append((u, v))

    nx.draw_networkx_edges(
        g, pos, edgelist=intra_edges, width=1.4, edge_color="#444444",
        alpha=0.7, ax=ax,
    )
    nx.draw_networkx_edges(
        g, pos, edgelist=inter_edges, width=1.0, edge_color="#999999",
        style="dashed", alpha=0.7, ax=ax,
    )
    nx.draw_networkx_nodes(
        g, pos,
        node_color=[color_map[v] for v in g.nodes()],
        node_size=560, edgecolors="black", linewidths=1.0, ax=ax,
    )
    nx.draw_networkx_labels(
        g, pos, font_size=10, font_color="white", font_weight="bold", ax=ax,
    )

    ax.set_axis_off()
    ax.margins(0.05)
    fig.tight_layout()
    fig.savefig(outpath, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    out = root / "figures" / "partition_example.pdf"
    out.parent.mkdir(parents=True, exist_ok=True)

    g, clusters = build_graph()
    draw(g, clusters, out)
    print(f"Saved {out}  ({g.number_of_nodes()} đỉnh, {g.number_of_edges()} cạnh)")


if __name__ == "__main__":
    main()
