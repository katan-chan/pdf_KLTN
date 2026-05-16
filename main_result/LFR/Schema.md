# Schema — Top 5 LFR

**Mô hình**: Lancichinetti–Fortunato–Radicchi benchmark (2008)
**Ground truth**: Có

## Mô tả mô hình

Sinh đồ thị với phân bố bậc power-law (exponent `tau1`) và phân bố kích thước cộng đồng power-law (`tau2`). Mỗi node v có `(1-mu)·k_v` cạnh trong cộng đồng và `mu·k_v` cạnh ra ngoài. Đây là **de facto benchmark** cho community detection.

**Tham số chính**: mu — mixing parameter ∈ (0, 1). mu càng lớn càng khó.

## Pipeline NCut + Mixed Matrix

Mỗi bộ test chạy NCut (sklearn SpectralClustering, affinity=precomputed) trên `W_λ = A + λ · W^(M)` với W^(M) là triangle motif matrix `(A·A) ⊙ A`.

## 5 bộ test được chọn

Tiêu chí chọn: `Q(A) ≥ 0.1` (loại nghiệm tầm thường) và score = `max Q(λ>0) − Q(A)` lớn nhất.

### #1. `LFR-100-mu035`

- **File**: [`data_lfr100_mu035_ncut.jsonp.js`](../../visualize/data_lfr100_mu035_ncut.jsonp.js)
- **Nodes**: 98    **Edges**: 178
- **cc_global**: 0.051302
- **k_gt**: 6
- **Config**: `N=100`    `mu=0.35`
- **Lambdas**: `['A', 0.5, 1.0, 2.0, 5.0, 10.0, 'W_M', 'GT']`

### #2. `LFR-100-mu0.2`

- **File**: [`data_lfr100_mu020_ncut.jsonp.js`](../../visualize/data_lfr100_mu020_ncut.jsonp.js)
- **Nodes**: 97    **Edges**: 176
- **cc_global**: 0.136774
- **k_gt**: 6
- **Config**: `N=100`    `mu=0.2`
- **Lambdas**: `['A', 0.5, 1.0, 2.0, 5.0, 10.0, 'W_M', 'GT']`

### #3. `LFR-500-mu0.4`

- **File**: [`data_lfr500_mu040_ncut.jsonp.js`](../../visualize/data_lfr500_mu040_ncut.jsonp.js)
- **Nodes**: 500    **Edges**: 2916
- **cc_global**: 0.059723
- **k_gt**: 7
- **Config**: `N=500`    `mu=0.4`
- **Lambdas**: `['A', 0.5, 1.0, 2.0, 5.0, 10.0, 'W_M', 'GT']`

### #4. `LFR-2000-mu050`

- **File**: [`data_lfr2000_mu050_ncut.jsonp.js`](../../visualize/data_lfr2000_mu050_ncut.jsonp.js)
- **Nodes**: 2000    **Edges**: 14115
- **cc_global**: 0.022667
- **k_gt**: 12
- **Config**: `N=2000`    `mu=0.5`
- **Lambdas**: `['A', 0.5, 1.0, 2.0, 5.0, 10.0, 'W_M', 'GT']`

### #5. `LFR-500-mu035`

- **File**: [`data_lfr500_mu035_ncut.jsonp.js`](../../visualize/data_lfr500_mu035_ncut.jsonp.js)
- **Nodes**: 500    **Edges**: 2905
- **cc_global**: 0.067381
- **k_gt**: 7
- **Config**: `N=500`    `mu=0.35`
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
