# Schema — Top 4 PLANTED

**Mô hình**: Planted Partition Model
**Ground truth**: Có

## Mô tả mô hình

Trường hợp đặc biệt của SBM với các block kích thước **bằng nhau** và mọi cặp block dùng cùng `p_in` (nội cụm) và `p_out` (ngoại cụm). Đơn giản nhất — phù hợp làm sanity baseline.

**Tham số chính**: p_in / p_out đồng nhất giữa các block.

## Pipeline NCut + Mixed Matrix

Mỗi bộ test chạy NCut (sklearn SpectralClustering, affinity=precomputed) trên `W_λ = A + λ · W^(M)` với W^(M) là triangle motif matrix `(A·A) ⊙ A`.

## 4 bộ test được chọn

Tiêu chí chọn: `Q(A) ≥ 0.1` (loại nghiệm tầm thường) và score = `max Q(λ>0) − Q(A)` lớn nhất.

### #1. `Planted_k5_s100_pin0.08_pout0.025`

- **File**: [`data_planted_500_pout0025_ncut.jsonp.js`](../../visualize/data_planted_500_pout0025_ncut.jsonp.js)
- **Nodes**: 500    **Edges**: 4422
- **cc_global**: 0.037882
- **k_gt**: 5
- **Config**: `N=500`    `p_out=0.0025`
- **Lambdas**: `['A', 0.5, 1.0, 2.0, 5.0, 10.0, 'W_M', 'GT']`

### #2. `Planted_k5_s40_pin0.15_pout0.03`

- **File**: [`data_planted_200_pout003_ncut.jsonp.js`](../../visualize/data_planted_200_pout003_ncut.jsonp.js)
- **Nodes**: 200    **Edges**: 1088
- **cc_global**: 0.067309
- **k_gt**: 5
- **Config**: `N=200`    `p_out=0.003`
- **Lambdas**: `['A', 0.5, 1.0, 2.0, 5.0, 10.0, 'W_M', 'GT']`

### #3. `Planted_k5_s400_pin0.025_pout0.006`

- **File**: [`data_planted_2000_pout0006_ncut.jsonp.js`](../../visualize/data_planted_2000_pout0006_ncut.jsonp.js)
- **Nodes**: 2000    **Edges**: 19783
- **cc_global**: 0.012342
- **k_gt**: 5
- **Config**: `N=2000`    `p_out=0.0006`
- **Lambdas**: `['A', 0.5, 1.0, 2.0, 5.0, 10.0, 'W_M', 'GT']`

### #4. `Planted_k5_s200_pin0.05_pout0.005`

- **File**: [`data_planted_1000_pout0005_ncut.jsonp.js`](../../visualize/data_planted_1000_pout0005_ncut.jsonp.js)
- **Nodes**: 1000    **Edges**: 6869
- **cc_global**: 0.028177
- **k_gt**: 5
- **Config**: `N=1000`    `p_out=0.0005`
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
