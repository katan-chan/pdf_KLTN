# Cách sinh đồ thị cho mỗi test

Tài liệu mô tả ngắn gọn 7 mô hình sinh đồ thị synthetic đang được dùng trong sweep NCut + Mixed Matrix. Mỗi mô hình đính kèm: tham số, công thức xác suất cạnh, đặc tính cộng đồng (có / không ground-truth), và lý do chọn vào bộ test.

Tất cả module ở `fake_data/` — wrapper mỏng quanh `networkx` generator + chuẩn hoá output về `SyntheticGraph(A, labels_gt, n_nodes, n_communities, name)` qua `graph.io.to_csr` (CSR int32 binary symmetric no-self-loop).

---

## 1. LFR — Lancichinetti-Fortunato-Radicchi (2008)

**Module**: `fake_data/lfr.py` · **NetworkX**: `LFR_benchmark_graph`

**Tham số**:
| Tham số | Ý nghĩa |
|---------|---------|
| `n` | số node |
| `tau1` | exponent power-law của bậc (mặc định 3.0) |
| `tau2` | exponent power-law của size cộng đồng (mặc định 1.5) |
| `mu ∈ (0,1)` | **mixing parameter** — tỷ lệ cạnh đi ra ngoài cộng đồng |
| `average_degree` | bậc trung bình mong muốn |
| `min_community / max_community` | giới hạn size cộng đồng |

**Cơ chế**:
1. Sample bậc cho mỗi node từ phân phối power-law với exponent `tau1`
2. Sample size cộng đồng từ power-law `tau2`, gán node vào các community sao cho tổng size = n
3. Mỗi node v có bậc `k_v` được phân thành: `(1-mu)·k_v` cạnh trong cụm + `mu·k_v` cạnh ra ngoài
4. Configuration model rewire để đạt đúng phân bố bậc

**Đặc tính**:
- **Có ground-truth community** (frozenset attribute "community" trên mỗi node)
- Bậc heterogeneous (power-law) — sát với mạng thực
- Cộng đồng size đa dạng — không đều
- `mu` quyết định độ khó: `mu < 0.3` dễ, `mu = 0.5` rất khó

**Sweep đang chạy**: `mu ∈ {0.1, 0.2, 0.3, 0.35, 0.4, 0.5}` × `N ∈ {100, 250, 500, 1000, 2000, 5000}`

**Lý do**: De facto benchmark cho community detection từ 2008 — sparse + power-law degree → W_M có cấu trúc khác A → mixed matrix có cơ hội phát huy.

---

## 2. SBM — Stochastic Block Model

**Module**: `fake_data/sbm.py` · **NetworkX**: `stochastic_block_model`

**Tham số**:
| Tham số | Ý nghĩa |
|---------|---------|
| `sizes: list[int]` | size mỗi block (k blocks) |
| `p_matrix: k×k` | `p_matrix[i][j]` = P(cạnh giữa block i và j) |

**Công thức**: `P(edge (u,v)) = p_matrix[block(u)][block(v)]`, độc lập giữa các cặp.

**Đặc tính**:
- **Có ground-truth** (block ID lấy từ attribute "block")
- Tổng quát nhất — cho phép từng cặp block có xác suất riêng (asymmetric community structure)
- Bậc trong block xấp xỉ Bin(size_block, p_in) → không heterogeneous như LFR

**Sweep đang chạy**: 3 blocks size đều, `p_in ∈ [0.01, 0.08]` (sparse), `p_out` sweep theo `p_out/p_in ∈ [0.1, 0.5]`.

**Lý do**: Random graph cộng đồng "kinh điển" — kiểm chứng baseline. Sparse SBM có ít tam giác → expected W_M ≈ rỗng → dùng để cho thấy mixed matrix KHÔNG luôn giúp.

---

## 3. Planted Partition

**Module**: `fake_data/planted.py` · **NetworkX**: `planted_partition_graph`

**Tham số**:
| Tham số | Ý nghĩa |
|---------|---------|
| `k` | số cộng đồng |
| `size_per_community` | size mỗi cụm (đều nhau) |
| `p_in / p_out` | xác suất cạnh nội/ngoại cụm (đồng nhất) |

**Cơ chế**: Trường hợp đặc biệt của SBM với `sizes = [s, s, ..., s]` và `p_matrix[i][j] = p_in if i==j else p_out`. Node `v` thuộc block `v // size_per_community`.

**Đặc tính**:
- **Có ground-truth** (deterministic theo node ID)
- Cộng đồng đối xứng hoàn toàn — đơn giản nhất
- Khi `p_in = p_out` ⇒ ER pure

**Sweep đang chạy**: `k=5`, `p_in ∈ [0.025, 0.15]`, `p_out` sweep.

**Lý do**: Sanity baseline — nếu thuật toán không xử lý được Planted thì không hoạt động ở đâu cả.

---

## 4. GRPG — Gaussian Random Partition Graph

**Module**: `fake_data/grpg.py` · **NetworkX**: `gaussian_random_partition_graph`

**Tham số**:
| Tham số | Ý nghĩa |
|---------|---------|
| `n` | tổng số node |
| `s` | size cụm trung bình |
| `v` | shape parameter (variance cụm = `s/v`) |
| `p_in / p_out` | xác suất cạnh nội/ngoại cụm |

**Cơ chế**: Sample size cụm từ Gaussian `N(s, s/v)` cho đến khi tổng đủ `n`, rồi sinh cạnh như Planted Partition trên các cụm đó.

**Đặc tính**:
- **Có ground-truth** (`G.graph["partition"]` — list các set node)
- Trung gian giữa Planted (đều) và LFR (power-law size)
- `v` lớn → cụm gần đều; `v` nhỏ → cụm rất chênh

**Sweep đang chạy**: `n ∈ [200, 2000]`, `s` tỉ lệ với n, `p_in ∈ [0.025, 0.15]`, `p_out` sweep.

**Lý do**: Test với size cụm đa dạng nhưng không cực đoan như power-law LFR — kiểm tra "moderate heterogeneity".

---

## Null models (không có ground-truth — dùng kiểm tra hallucination)

Mục tiêu null model: graph **không có cộng đồng thật**. Nếu thuật toán vẫn "tìm thấy" community với Q cao → hallucination (xấu). Mong muốn: Q thấp + Q(mixed) ≤ Q(A).

### 5. ER — Erdős–Rényi G(n, p)

**Module**: `fake_data/er.py` · **NetworkX**: `erdos_renyi_graph`

**Tham số**: `n` nodes, mỗi cạnh xuất hiện độc lập với xác suất `p`.

**Đặc tính**:
- Bậc Binomial(n−1, p) ≈ Poisson, **homogeneous** (không heavy-tail)
- **Không cộng đồng** — `labels_gt = 0` toàn bộ
- Số tam giác kỳ vọng `~ C(n,3)·p³` (rất ít khi p nhỏ)

**Sweep đang chạy**: `n ∈ {500..5000}`, `p` sao cho avg-degree ∈ [5, 15].

**Lý do**: Null đơn giản nhất — kiểm tra thuật toán không tạo "fake community" trên graph hoàn toàn ngẫu nhiên.

### 6. BA — Barabási–Albert preferential attachment

**Module**: `fake_data/ba.py` · **NetworkX**: `barabasi_albert_graph`

**Tham số**: `n` nodes, mỗi node mới kết nối `m` cạnh tới node cũ với xác suất tỷ lệ với bậc.

**Đặc tính**:
- Phân bố bậc power-law `P(k) ~ k^{-3}` (scale-free)
- **Không cộng đồng** — chỉ có hub
- Cluster coefficient → 0 khi n lớn (rất ít tam giác)

**Lý do**: Test xem thuật toán có bị bias bởi hub không — degree heterogeneity nhưng không có community → không nên có Q cao. 80% node thường isolated trong W_M (vì không tam giác đi qua) → W_M-only sụp đổ.

### 7. PLC — Power-Law Cluster (Holme–Kim 2002)

**Module**: `fake_data/plc.py` · **NetworkX**: `powerlaw_cluster_graph`

**Tham số**: `n`, `m` (như BA), thêm `p` = xác suất triad-formation step.

**Cơ chế**: Mở rộng BA — sau khi node mới chọn neighbor `u`, với xác suất `p` thêm cạnh tới một neighbor của `u` (tạo tam giác).

**Đặc tính**:
- Scale-free + clustering coefficient cao (giống mạng xã hội)
- **Không cộng đồng** ground-truth — chỉ có local triad clustering
- Nhiều tam giác hơn BA/ER nhưng triad là local (quanh hub) chứ không hình thành block

**Lý do**: Null model "khó nhất" — có clustering cao mà không có community thật. Nếu mixed matrix tăng Q rõ rệt ở đây ⇒ hallucination.

---

## Tóm tắt định lượng

| Model | Ground-truth | Bậc | Tam giác | Vai trò |
|-------|:------------:|-----|----------|---------|
| LFR | ✅ | Power-law | Trung bình | Sweet spot cho mixed |
| SBM | ✅ | ~Poisson trong block | Phụ thuộc p_in | Baseline sparse |
| Planted | ✅ | ~Poisson | Phụ thuộc p_in | Sanity check |
| GRPG | ✅ | ~Poisson | Phụ thuộc p_in | Trung gian |
| ER | ❌ | Binomial homogeneous | Rất ít | Null random |
| BA | ❌ | Power-law (γ=3) | Rất ít | Null hub |
| PLC | ❌ | Power-law | Cao (local) | Null hard |

---

## Pipeline áp dụng cho mọi mô hình

```
generator(params) → SyntheticGraph(A, labels_gt)
            ↓
   ensure_connected (lấy LCC nếu phân mảnh, remap GT)
            ↓
   k_gt = số cụm GT (đếm từ labels)
            ↓
   run_pipeline(A, lambdas=[0, 0.5, 1, 2, 5, 10], k=k_gt)
       ├─ λ=0  → A-only  (NCut trên A binary)
       ├─ λ>0  → mixed   (NCut trên A + λ·W_M)
       └─ W_M only       (NCut trên W_M)
            ↓
   metrics: Q, edges_cut, motifs_cut/internal, NMI, Jaccard
            ↓
   dump JSONP → visualize/data_<model>_<config>_ncut.jsonp.js
```

Với null model (ER/BA/PLC): không có `labels_gt` thật → NMI/Jaccard không tính, chỉ đánh giá Q và conductance.
