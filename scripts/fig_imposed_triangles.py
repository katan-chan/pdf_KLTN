"""Vẽ hình 4 loại tam giác sinh ra qua phép chồng cạnh và tam giác trong SupSBM.

Output: figures/imposed_triangles.pdf
Dùng cho: Bổ đề kỳ vọng A_T trong Mục 3.3.5 (Chương 3 KLTN).

Bốn panel theo paper Paul, Milenkovic, Chen (2023):
  (a) E^3: ba cạnh i-j, j-k, i-k đều là cạnh từ G_E.
  (b) T^3: ba cạnh đều sinh từ tam giác trong G_T, mỗi cạnh kèm
          một đỉnh phụ k_1, k_2, k_3 hoàn thành tam giác trong G_T.
  (c) T^2 E: một cạnh từ G_E (i-j), hai cạnh sinh từ tam giác G_T
          (j-k với đỉnh phụ k_1, i-k với đỉnh phụ k_2).
  (d) T E^2: hai cạnh từ G_E (i-j, i-k), một cạnh sinh từ tam giác G_T
          (j-k với đỉnh phụ k_1).
"""

from pathlib import Path

import matplotlib.pyplot as plt


EDGE_COLOR = "#1976D2"
PHANTOM_COLOR = "#90A4AE"
NODE_FILL = "#FFFFFF"


def draw_triangle(ax, x_offset, label, edges, phantoms):
    """Vẽ một panel.

    edges: dict {(u,v): label_text} cho ba cạnh chính.
    phantoms: list [(u, v, k_name, k_pos)] mô tả đỉnh phụ k.
    """
    i = (x_offset + 1.0, 1.5)
    j = (x_offset + 0.0, 0.0)
    k = (x_offset + 2.0, 0.0)
    pos = {"i": i, "j": j, "k": k}

    # Vẽ đỉnh phụ và đường nét đứt
    for u, v, k_name, k_pos in phantoms:
        kx, ky = k_pos[0] + x_offset, k_pos[1]
        ax.plot([pos[u][0], kx], [pos[u][1], ky],
                color=PHANTOM_COLOR, lw=0.9, linestyle=":", zorder=1)
        ax.plot([pos[v][0], kx], [pos[v][1], ky],
                color=PHANTOM_COLOR, lw=0.9, linestyle=":", zorder=1)
        ax.text(kx, ky - 0.18, k_name, ha="center", va="top",
                fontsize=10, color="black")

    # Vẽ ba cạnh chính
    for (u, v), lbl in edges.items():
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        ax.plot([x1, x2], [y1, y2], color=EDGE_COLOR, lw=1.6, zorder=2)
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        # Đặt label cạnh ngoài tam giác
        if (u, v) == ("i", "j") or (u, v) == ("j", "i"):
            ax.text(mx - 0.22, my, lbl, ha="center", va="center", fontsize=11)
        elif (u, v) == ("i", "k") or (u, v) == ("k", "i"):
            ax.text(mx + 0.22, my, lbl, ha="center", va="center", fontsize=11)
        else:  # j-k
            ax.text(mx, my - 0.22, lbl, ha="center", va="center", fontsize=11)

    # Vẽ 3 đỉnh chính
    for name, (x, y) in pos.items():
        ax.scatter([x], [y], s=70, c=NODE_FILL, edgecolors="black",
                   linewidths=0.9, zorder=4)
        ax.text(x, y + 0.22, name, ha="center", va="bottom",
                fontsize=11, fontweight="bold")

    # Nhãn panel (a), (b), ...
    ax.text(x_offset + 1.0, -1.6, label, ha="center", va="center", fontsize=11)


def main():
    fig, ax = plt.subplots(figsize=(13, 3.2))
    ax.set_xlim(-0.6, 14.6)
    ax.set_ylim(-2.0, 2.4)
    ax.set_aspect("equal")
    ax.axis("off")

    # (a) E^3
    draw_triangle(ax, 0,
                  label="(a) $E^3$",
                  edges={("i", "j"): "$e$", ("i", "k"): "$e$", ("j", "k"): "$e$"},
                  phantoms=[])

    # (b) T^3
    draw_triangle(ax, 3.6,
                  label="(b) $T^3$",
                  edges={("i", "j"): "$t$", ("i", "k"): "$t$", ("j", "k"): "$t$"},
                  phantoms=[
                      ("j", "k", "$k_1$", (1.0, -1.1)),
                      ("i", "k", "$k_2$", (2.6, 1.5)),
                      ("i", "j", "$k_3$", (-0.6, 1.5)),
                  ])

    # (c) T^2 E
    draw_triangle(ax, 7.2,
                  label="(c) $T^2 E$",
                  edges={("i", "j"): "$e$", ("i", "k"): "$t$", ("j", "k"): "$t$"},
                  phantoms=[
                      ("j", "k", "$k_1$", (1.0, -1.1)),
                      ("i", "k", "$k_2$", (2.6, 1.5)),
                  ])

    # (d) T E^2
    draw_triangle(ax, 10.8,
                  label="(d) $T E^2$",
                  edges={("i", "j"): "$e$", ("i", "k"): "$e$", ("j", "k"): "$t$"},
                  phantoms=[
                      ("j", "k", "$k_1$", (1.0, -1.1)),
                  ])

    plt.tight_layout()
    out_dir = Path(__file__).resolve().parent.parent / "figures"
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "imposed_triangles.pdf"
    fig.savefig(out_path, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {out_path}")


if __name__ == "__main__":
    main()
