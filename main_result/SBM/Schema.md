# Schema — Top 5 SBM

**Mô hình**: Stochastic Block Model
**Ground truth**: Có

## Mô tả mô hình

Mỗi node thuộc 1 block. Xác suất tồn tại cạnh giữa node `u` và `v` chỉ phụ thuộc block của chúng: `P(edge) = p_matrix[block(u)][block(v)]`. Tổng quát nhất trong các mô hình cộng đồng.

**Tham số chính**: p_in (nội cụm) vs p_out (ngoại cụm). p_out/p_in càng cao càng khó.

## Pipeline NCut + Mixed Matrix

Mỗi bộ test chạy NCut (sklearn SpectralClustering, affinity=precomputed) trên `W_λ = A + λ · W^(M)` với W^(M) là triangle motif matrix `(A·A) ⊙ A`.

## 5 bộ test được chọn

Tiêu chí chọn: `Q(A) ≥ 0.1` (loại nghiệm tầm thường) và score = `max Q(λ>0) − Q(A)` lớn nhất.

### #1. `SBM-1500-pin0.02-pout0.008`

- **File**: [`data_sbm_1500_pout0008_ncut.jsonp.js`](../../visualize/data_sbm_1500_pout0008_ncut.jsonp.js)
- **Nodes**: 1500    **Edges**: 13569
- **cc_global**: 0.01282
- **k_gt**: 3
- **Config**: `N=1500`    `p_out=0.0008`
- **Lambdas**: `['A', 0.5, 1.0, 2.0, 5.0, 10.0, 'W_M', 'GT']`

### #2. `SBM-3000-pin0.012-pout0.005`

- **File**: [`data_sbm_3000_pout0005_ncut.jsonp.js`](../../visualize/data_sbm_3000_pout0005_ncut.jsonp.js)
- **Nodes**: 3000    **Edges**: 32935
- **cc_global**: 0.007838
- **k_gt**: 3
- **Config**: `N=3000`    `p_out=0.0005`
- **Lambdas**: `['A', 0.5, 1.0, 2.0, 5.0, 10.0, 'W_M', 'GT']`

### #3. `SBM-300-pin0.08-pout0.02`

- **File**: [`data_sbm_300_pout002_ncut.jsonp.js`](../../visualize/data_sbm_300_pout002_ncut.jsonp.js)
- **Nodes**: 300    **Edges**: 1752
- **cc_global**: 0.04267
- **k_gt**: 3
- **Config**: `N=300`    `p_out=0.002`
- **Lambdas**: `['A', 0.5, 1.0, 2.0, 5.0, 10.0, 'W_M', 'GT']`

### #4. `SBM-600-pin0.05-pout0.02`

- **File**: [`data_sbm_600_pout002_ncut.jsonp.js`](../../visualize/data_sbm_600_pout002_ncut.jsonp.js)
- **Nodes**: 600    **Edges**: 5289
- **cc_global**: 0.031787
- **k_gt**: 3
- **Config**: `N=600`    `p_out=0.002`
- **Lambdas**: `['A', 0.5, 1.0, 2.0, 5.0, 10.0, 'W_M', 'GT']`

### #5. `SBM-300-pin0.08-pout0.005`

- **File**: [`data_sbm_300_pout0005_ncut.jsonp.js`](../../visualize/data_sbm_300_pout0005_ncut.jsonp.js)
- **Nodes**: 300    **Edges**: 1267
- **cc_global**: 0.051821
- **k_gt**: 3
- **Config**: `N=300`    `p_out=0.0005`
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
