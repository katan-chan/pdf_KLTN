# Schema — Top 6 REAL

**Mô hình**: Real-world dataset (SNAP / MUSAE)
**Ground truth**: Không

## Mô tả mô hình

Đồ thị thực tế (citation / social / email). **Không có ground-truth** community → chỉ đánh giá Q, conductance, edges_cut, motifs_cut.

**Tham số chính**: k — số cluster cần tìm (input của NCut).

## Pipeline NCut + Mixed Matrix

Mỗi bộ test chạy NCut (sklearn SpectralClustering, affinity=precomputed) trên `W_λ = A + λ · W^(M)` với W^(M) là triangle motif matrix `(A·A) ⊙ A`.

## 6 bộ test được chọn

Tiêu chí chọn: **không filter** (đồ thị thật ít cấu trúc đậm), score = `max Q(λ>0) − Q(A)` lớn nhất.

### #1. `cit-HepTh_adj-ncut-k50`

- **File**: [`data_cit-HepTh_adj_ncut_k50.jsonp.js`](../../visualize/data_cit-HepTh_adj_ncut_k50.jsonp.js)
- **Nodes**: 27400    **Edges**: 352021
- **cc_global**: 0.313915
- **Config**: `k_input=50`
- **Lambdas**: `['0', '1', '5', '10', 'W_M']`

### #2. `cit-HepTh_adj-ncut-k100`

- **File**: [`data_cit-HepTh_adj_ncut_k100.jsonp.js`](../../visualize/data_cit-HepTh_adj_ncut_k100.jsonp.js)
- **Nodes**: 27400    **Edges**: 352021
- **cc_global**: 0.313915
- **Config**: `k_input=100`
- **Lambdas**: `['0', '1', '5', '10', 'W_M']`

### #3. `cit-HepTh_adj-ncut-k200`

- **File**: [`data_cit-HepTh_adj_ncut_k200.jsonp.js`](../../visualize/data_cit-HepTh_adj_ncut_k200.jsonp.js)
- **Nodes**: 27400    **Edges**: 352021
- **cc_global**: 0.313915
- **Config**: `k_input=200`
- **Lambdas**: `['0', '1', '5', '10', 'W_M']`

### #4. `cit-HepTh_adj-ncut-k300`

- **File**: [`data_cit-HepTh_adj_ncut_k300.jsonp.js`](../../visualize/data_cit-HepTh_adj_ncut_k300.jsonp.js)
- **Nodes**: 27400    **Edges**: 352021
- **cc_global**: 0.313915
- **Config**: `k_input=300`
- **Lambdas**: `['0', '1', '5', '10', 'W_M']`

### #5. `cit-HepTh_adj-ncut-k400`

- **File**: [`data_cit-HepTh_adj_ncut_k400.jsonp.js`](../../visualize/data_cit-HepTh_adj_ncut_k400.jsonp.js)
- **Nodes**: 27400    **Edges**: 352021
- **cc_global**: 0.313915
- **Config**: `k_input=400`
- **Lambdas**: `['0', '1', '5', '10', 'W_M']`

### #6. `cit-HepTh_adj-ncut-k500`

- **File**: [`data_cit-HepTh_adj_ncut_k500.jsonp.js`](../../visualize/data_cit-HepTh_adj_ncut_k500.jsonp.js)
- **Nodes**: 27400    **Edges**: 352021
- **cc_global**: 0.313915
- **Config**: `k_input=500`
- **Lambdas**: `['0', '1', '5', '10', 'W_M']`

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
