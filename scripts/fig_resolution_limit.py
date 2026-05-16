"""Vẽ ví dụ minh họa hiện tượng resolution limit của modularity.

Cấu trúc: một vòng các clique nhỏ, mỗi clique nối với hàng xóm bằng 1 cạnh.
Phân hoạch tự nhiên: mỗi clique là một cụm.
Modularity tối ưu: gộp các cặp clique kề nhau thành một cụm khi clique đủ nhỏ
so với tổng số cạnh m, theo Fortunato & Barthélemy 2007.

Hình hiển thị 2 phân hoạch cạnh nhau:
  (a) Phân hoạch tự nhiên: mỗi clique là một cụm.
  (b) Phân hoạch tối ưu modularity: gộp từng cặp clique kề nhau.

Output: figures/resolution_limit.png
Dùng cho: Mục 1.1.2 (Nhận xét hiện tượng resolution limit).
"""

from itertools import combinations
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def ring_of_cliques(num_cliques: int = 8, clique_size: int = 4) -> tuple[nx.Graph, list[list[int]]]:
    """Sinh vòng K_s clique nối nhau bằng 1 cạnh."""
    g = nx.Graph()
    cliques: list[list[int]] = []
    next_id = 0
    for _ in range(num_cliques):
        members = list(range(next_id, next_id + clique_size))
        cliques.append(members)
        for u, v in combinations(members, 2):
            g.add_edge(u, v)
        next_id += clique_size

    # Nối các clique liên tiếp bằng 1 cạnh tạo vòng.
    for i in range(num_cliques):
        a = cliques[i][0]
        b = cliques[(i + 1) % num_cliques][-1]
        g.add_edge(a, b)
    return g, cliques


def modularity_of(g: nx.Graph, partition: list[list[int]]) -> float:
    sets = [set(c) for c in partition]
    return nx.community.modularity(g, sets)


def merge_pairs(cliques: list[list[int]]) -> list[list[int]]:
    """Phân hoạch ghép từng cặp clique kề nhau."""
    merged = []
    for i in range(0, len(cliques), 2):
        merged.append(cliques[i] + cliques[(i + 1) % len(cliques)])
    return merged


def draw_partition(
    g: nx.Graph,
    pos: dict,
    partition: list[list[int]],
    palette: list[str],
    title: str,
    ax: plt.Axes,
) -> None:
    membership = {v: i for i, c in enumerate(partition) for v in c}
    color_map = {v: palette[membership[v] % len(palette)] for v in g.nodes()}

    intra, inter = [], []
    for u, v in g.edges():
        (intra if membership[u] == membership[v] else inter).append((u, v))

    nx.draw_networkx_edges(g, pos, edgelist=intra, width=1.0, edge_color="#444",
                           alpha=0.7, ax=ax)
    nx.draw_networkx_edges(g, pos, edgelist=inter, width=1.0, edge_color="#aaa",
                           style="dashed", alpha=0.8, ax=ax)
    nx.draw_networkx_nodes(g, pos,
                           node_color=[color_map[v] for v in g.nodes()],
                           node_size=240, edgecolors="black", linewidths=0.8, ax=ax)

    q = modularity_of(g, partition)
    ax.set_title(f"{title}\n$Q = {q:.4f}$", fontsize=11)
    ax.set_axis_off()


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    out = root / "figures" / "resolution_limit.pdf"
    out.parent.mkdir(parents=True, exist_ok=True)

    # Cần num_cliques đủ lớn để clique_size < sqrt(m/2) (Fortunato-Barthélemy 2007).
    # Với 16 clique cỡ K_3: m = 16*3 + 16 = 64 → sqrt(m/2) = 5.66 > 3 = số cạnh nội/clique.
    num_cliques, clique_size = 16, 3
    g, cliques = ring_of_cliques(num_cliques, clique_size)

    # Layout vòng: đặt các clique đều quanh đường tròn lớn,
    # mỗi clique tự xếp đỉnh quanh tâm cục bộ.
    big_radius = 5.0
    small_radius = 0.7
    pos = {}
    for i, members in enumerate(cliques):
        theta = 2 * np.pi * i / num_cliques
        cx, cy = big_radius * np.cos(theta), big_radius * np.sin(theta)
        for j, v in enumerate(members):
            phi = 2 * np.pi * j / len(members)
            pos[v] = (cx + small_radius * np.cos(phi),
                      cy + small_radius * np.sin(phi))

    palette = [
        "#4C72B0", "#DD8452", "#55A868", "#C44E52",
        "#8172B3", "#937860", "#DA8BC3", "#8C8C8C",
        "#CCB974", "#64B5CD", "#7F7F7F", "#BCBD22",
        "#17BECF", "#E377C2", "#9467BD", "#8C564B",
    ]

    natural = cliques
    merged = merge_pairs(cliques)

    fig, axes = plt.subplots(1, 2, figsize=(11, 5.5))
    draw_partition(g, pos, natural, palette,
                   "(a) Phân hoạch tự nhiên: mỗi clique một cụm", axes[0])
    draw_partition(g, pos, merged, palette,
                   "(b) Phân hoạch tối ưu modularity: gộp từng cặp clique", axes[1])

    fig.suptitle(
        f"Resolution limit: vòng {num_cliques} clique cỡ $K_{clique_size}$, "
        f"$m = {g.number_of_edges()}$",
        fontsize=12,
    )
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {out}")
    print(f"  Q(tự nhiên) = {modularity_of(g, natural):.4f}")
    print(f"  Q(gộp cặp)  = {modularity_of(g, merged):.4f}")


if __name__ == "__main__":
    main()
