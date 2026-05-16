# Schema — Top 5 GRPG

**Mô hình**: Gaussian Random Partition Graph
**Ground truth**: Có

## Mô tả mô hình

Kích thước cụm sample từ Gaussian `N(s, s/v)`, rồi sinh cạnh theo Planted Partition trên các cụm đó. Trung gian giữa Planted (đều) và LFR (power-law).

**Tham số chính**: s (size trung bình), v (shape), p_in, p_out.

## Pipeline NCut + Mixed Matrix

Mỗi bộ test chạy NCut (sklearn SpectralClustering, affinity=precomputed) trên `W_λ = A + λ · W^(M)` với W^(M) là triangle motif matrix `(A·A) ⊙ A`.

## 5 bộ test được chọn

Tiêu chí chọn: `Q(A) ≥ 0.1` (loại nghiệm tầm thường) và score = `max Q(λ>0) − Q(A)` lớn nhất.

### #1. `GRPG-2000-pin0.025-pout0.006`

- **File**: [`data_grpg_2000_pout0.006_ncut.jsonp.js`](../../visualize/data_grpg_2000_pout0.006_ncut.jsonp.js)
- **Nodes**: 2000    **Edges**: 17338
- **cc_global**: 0.010385
- **k_gt**: 7
- **Config**: `N=2000`    `p_out=0.006`
- **Lambdas**: `['A', 0.5, 1.0, 2.0, 5.0, 10.0, 'W_M', 'GT']`

### #2. `GRPG-500-pin0.08-pout0.008`

- **File**: [`data_grpg_500_pout0.008_ncut.jsonp.js`](../../visualize/data_grpg_500_pout0.008_ncut.jsonp.js)
- **Nodes**: 500    **Edges**: 2778
- **cc_global**: 0.041996
- **k_gt**: 6
- **Config**: `N=500`    `p_out=0.008`
- **Lambdas**: `['A', 0.5, 1.0, 2.0, 5.0, 10.0, 'W_M', 'GT']`

### #3. `GRPG-500-pin0.08-pout0.015`

- **File**: [`data_grpg_500_pout0.015_ncut.jsonp.js`](../../visualize/data_grpg_500_pout0.015_ncut.jsonp.js)
- **Nodes**: 500    **Edges**: 3454
- **cc_global**: 0.037167
- **k_gt**: 6
- **Config**: `N=500`    `p_out=0.015`
- **Lambdas**: `['A', 0.5, 1.0, 2.0, 5.0, 10.0, 'W_M', 'GT']`

### #4. `GRPG-2000-pin0.025-pout0.001`

- **File**: [`data_grpg_2000_pout0.001_ncut.jsonp.js`](../../visualize/data_grpg_2000_pout0.001_ncut.jsonp.js)
- **Nodes**: 2000    **Edges**: 8816
- **cc_global**: 0.01651
- **k_gt**: 7
- **Config**: `N=2000`    `p_out=0.001`
- **Lambdas**: `['A', 0.5, 1.0, 2.0, 5.0, 10.0, 'W_M', 'GT']`

### #5. `GRPG-200-pin0.15-pout0.03`

- **File**: [`data_grpg_200_pout0.03_ncut.jsonp.js`](../../visualize/data_grpg_200_pout0.03_ncut.jsonp.js)
- **Nodes**: 200    **Edges**: 1167
- **cc_global**: 0.070729
- **k_gt**: 4
- **Config**: `N=200`    `p_out=0.03`
- **Lambdas**: `['A', 0.5, 1.0, 2.0, 5.0, 10.0, 'W_M', 'GT']`

## Ý nghĩa metric

- **Modularity Q** (Newman 2006): `Q = Σ_c [L_c/m − (D_c/(2m))²]`. Đo độ mạnh của cấu trúc cộng đồng — cao = nội cụm dày hơn so với random. Range [-0.5, 1]. Q > 0.3 thường coi là có cấu trúc cộng đồng.
- **Clustering Coefficient (average per cluster)**. Trung bình không trọng số của clustering coefficient các node trong cùng cụm (tính trên subgraph induced).
- **Clustering Coefficient (size-weighted)**. Trung bình clustering coefficient toàn bộ node, weighted bởi size cụm — `(1/|V|) Σ_v cc_intra(v, C(v))`.
- **Edges Cut**: số cạnh `(u,v) ∈ E` mà `labels[u] ≠ labels[v]`. Cut nhỏ ⇒ partition tốt (theo nghĩa NCut).
- **Motifs Cut**: số tam giác bị cắt qua biên cụm (≥1 đỉnh ở cụm khác). Bằng `motifs_total - Σ motifs_internal`.
- **Motifs Internal**: tổng số tam giác **hoàn toàn** trong các cụm (cả 3 đỉnh cùng cụm).
- **Jaccard vs Baseline (λ=A)**: pairwise Jaccard so với partition tại λ=0 (A only). Đo độ ổn định khi tăng λ — 1.0 = giống hệt baseline.
- **Normalized Mutual Information** vs ground truth ∈ [0, 1]. 1 = perfect match, 0 = random.
- **Jaccard similarity** (pair-counting) vs ground truth ∈ [0, 1]. `J = a/(a+b+c)` với `a` = cặp cùng cụm ở cả 2 partition.

**Lưu ý**: Mọi metric tính trên `A` gốc binary, không phải W_λ.
