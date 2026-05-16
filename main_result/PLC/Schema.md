# Schema — Top 5 PLC

**Mô hình**: Power-Law Cluster (Holme–Kim 2002) — null model
**Ground truth**: Không

## Mô tả mô hình

Mở rộng BA với bước triad-formation: với xác suất `p`, mỗi cạnh mới tạo thêm tam giác. Clustering coefficient cao nhưng **không** community thật → test hallucination khó nhất.

**Tham số chính**: p — xác suất triad formation. p càng cao clustering càng cao.

## Pipeline NCut + Mixed Matrix

Mỗi bộ test chạy NCut (sklearn SpectralClustering, affinity=precomputed) trên `W_λ = A + λ · W^(M)` với W^(M) là triangle motif matrix `(A·A) ⊙ A`.

## 5 bộ test được chọn

Tiêu chí chọn: `Q(A) ≥ 0.1` (loại nghiệm tầm thường) và score = `max Q(λ>0) − Q(A)` lớn nhất.

### #1. `PLC_n1000_m3_p0.1`

- **File**: [`data_plc_1000_p01_ncut.jsonp.js`](../../visualize/data_plc_1000_p01_ncut.jsonp.js)
- **Nodes**: 1000    **Edges**: 2990
- **cc_global**: 0.079232
- **Config**: `N=1000`    `p=0.01`
- **Lambdas**: `['A', 0.5, 1.0, 2.0, 5.0, 10.0, 'W_M']`

### #2. `PLC_n500_m3_p0.1`

- **File**: [`data_plc_500_p01_ncut.jsonp.js`](../../visualize/data_plc_500_p01_ncut.jsonp.js)
- **Nodes**: 500    **Edges**: 1490
- **cc_global**: 0.113196
- **Config**: `N=500`    `p=0.01`
- **Lambdas**: `['A', 0.5, 1.0, 2.0, 5.0, 10.0, 'W_M']`

### #3. `PLC_n1000_m3_p0.5`

- **File**: [`data_plc_1000_p05_ncut.jsonp.js`](../../visualize/data_plc_1000_p05_ncut.jsonp.js)
- **Nodes**: 1000    **Edges**: 2990
- **cc_global**: 0.293684
- **Config**: `N=1000`    `p=0.05`
- **Lambdas**: `['A', 0.5, 1.0, 2.0, 5.0, 10.0, 'W_M']`

### #4. `PLC_n500_m3_p0.5`

- **File**: [`data_plc_500_p05_ncut.jsonp.js`](../../visualize/data_plc_500_p05_ncut.jsonp.js)
- **Nodes**: 500    **Edges**: 1490
- **cc_global**: 0.303337
- **Config**: `N=500`    `p=0.05`
- **Lambdas**: `['A', 0.5, 1.0, 2.0, 5.0, 10.0, 'W_M']`

### #5. `PLC_n2000_m3_p0.5`

- **File**: [`data_plc_2000_p05_ncut.jsonp.js`](../../visualize/data_plc_2000_p05_ncut.jsonp.js)
- **Nodes**: 2000    **Edges**: 5990
- **cc_global**: 0.279742
- **Config**: `N=2000`    `p=0.05`
- **Lambdas**: `['A', 0.5, 1.0, 2.0, 5.0, 10.0, 'W_M']`

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
