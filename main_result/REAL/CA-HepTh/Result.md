# Result — Top 6 REAL

6 bộ test có ΔQ lớn nhất khi dùng mixed matrix, không filter Q(A).

## Ranking

| Rank | Test | Q(A) | Best λ | Q(best) | ΔQ |
|---:|------|-----:|:------:|--------:|---:|
| 1 | `CA-HepTh-ncut-k50` | 0.6878 | `5.0` | 0.7128 | +0.0250 |
| 2 | `CA-HepTh-ncut-k100` | 0.6949 | `1.0` | 0.7128 | +0.0179 |
| 3 | `CA-HepTh-ncut-k200` | 0.6863 | `5.0` | 0.7029 | +0.0165 |
| 4 | `CA-HepTh-ncut-k300` | 0.6680 | `5.0` | 0.6899 | +0.0219 |
| 5 | `CA-HepTh-ncut-k400` | 0.6514 | `5.0` | 0.6664 | +0.0150 |
| 6 | `CA-HepTh-ncut-k500` | 0.6349 | `5.0` | 0.6527 | +0.0179 |

## Bảng modularity Q × λ cho 5 test

| Test | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M | best λ | ΔQ |
|---|---:|---:|---:|---:|---:|---:|---:|
| #1 CA-HepTh-ncut-k50 | 0.6878 | 0.7030 | 0.7128 | 0.7087 | 0.6491 | `5.0` | +0.0250 |
| #2 CA-HepTh-ncut-k100 | 0.6949 | 0.7128 | 0.7111 | 0.7098 | 0.6546 | `1.0` | +0.0179 |
| #3 CA-HepTh-ncut-k200 | 0.6863 | 0.6962 | 0.7029 | 0.7008 | 0.6401 | `5.0` | +0.0165 |
| #4 CA-HepTh-ncut-k300 | 0.6680 | 0.6830 | 0.6899 | 0.6822 | 0.6164 | `5.0` | +0.0219 |
| #5 CA-HepTh-ncut-k400 | 0.6514 | 0.6608 | 0.6664 | 0.6657 | 0.5991 | `5.0` | +0.0150 |
| #6 CA-HepTh-ncut-k500 | 0.6349 | 0.6473 | 0.6527 | 0.6512 | 0.5776 | `5.0` | +0.0179 |

## #1. `CA-HepTh-ncut-k50`

- File: [`data_CA-HepTh_ncut_k50.jsonp.js`](../../visualize/data_CA-HepTh_ncut_k50.jsonp.js)  · Export folder: [`CA-HepTh-ncut-k50/`](../../exports/) (tên file `CA-HepTh-ncut-k50` có thể chứa ký tự đặc biệt)
- Nodes: 8638, Edges: 24806, cc_global: 0.481564

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.6878 | 0.7030 | 0.7128 | 0.7087 | 0.6491 |
| quality · **cc_avg** | 0.4977 | 0.5256 | 0.5325 | 0.5337 | 0.7043 |
| quality · **cc_weighted** | 0.4863 | 0.5065 | 0.5169 | 0.5142 | 0.5557 |
| cut · **edges_cut** | 6641 | 6502 | 6122 | 5861 | 7886 |
| cut · **motifs_cut** | 5772 | 4935 | 4406 | 4166 | 4826 |
| cut · **motifs_internal** | 22097 | 22934 | 23463 | 23703 | 23043 |
| stability · **jaccard_vs_base** | 1 | 0.2080 | 0.2138 | 0.2039 | 0.0616 |

**Highlights**:  Q(A)=0.6878 → Q(λ=5.0)=0.7128 (ΔQ=+0.0250).
  Edges cut: A=6641 → λ=10.0: 5861.
  Motifs cut: A=5772 → λ=10.0: 4166.

## #2. `CA-HepTh-ncut-k100`

- File: [`data_CA-HepTh_ncut_k100.jsonp.js`](../../visualize/data_CA-HepTh_ncut_k100.jsonp.js)  · Export folder: [`CA-HepTh-ncut-k100/`](../../exports/) (tên file `CA-HepTh-ncut-k100` có thể chứa ký tự đặc biệt)
- Nodes: 8638, Edges: 24806, cc_global: 0.481564

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.6949 | 0.7128 | 0.7111 | 0.7098 | 0.6546 |
| quality · **cc_avg** | 0.5220 | 0.5265 | 0.5366 | 0.5376 | 0.7107 |
| quality · **cc_weighted** | 0.4919 | 0.5075 | 0.5189 | 0.5219 | 0.5589 |
| cut · **edges_cut** | 6955 | 6523 | 6640 | 6659 | 7992 |
| cut · **motifs_cut** | 5967 | 5060 | 5140 | 4913 | 4965 |
| cut · **motifs_internal** | 21902 | 22809 | 22729 | 22956 | 22904 |
| stability · **jaccard_vs_base** | 1 | 0.2959 | 0.2124 | 0.2429 | 0.0568 |

**Highlights**:  Q(A)=0.6949 → Q(λ=1.0)=0.7128 (ΔQ=+0.0179).
  Edges cut: A=6955 → λ=1.0: 6523.
  Motifs cut: A=5967 → λ=10.0: 4913.

## #3. `CA-HepTh-ncut-k200`

- File: [`data_CA-HepTh_ncut_k200.jsonp.js`](../../visualize/data_CA-HepTh_ncut_k200.jsonp.js)  · Export folder: [`CA-HepTh-ncut-k200/`](../../exports/) (tên file `CA-HepTh-ncut-k200` có thể chứa ký tự đặc biệt)
- Nodes: 8638, Edges: 24806, cc_global: 0.481564

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.6863 | 0.6962 | 0.7029 | 0.7008 | 0.6401 |
| quality · **cc_avg** | 0.5142 | 0.5332 | 0.5402 | 0.5332 | 0.7162 |
| quality · **cc_weighted** | 0.4953 | 0.5185 | 0.5256 | 0.5293 | 0.5662 |
| cut · **edges_cut** | 7483 | 7267 | 7064 | 7098 | 8533 |
| cut · **motifs_cut** | 6688 | 5897 | 5520 | 5585 | 5542 |
| cut · **motifs_internal** | 21181 | 21972 | 22349 | 22284 | 22327 |
| stability · **jaccard_vs_base** | 1 | 0.2963 | 0.2860 | 0.2638 | 0.0489 |

**Highlights**:  Q(A)=0.6863 → Q(λ=5.0)=0.7029 (ΔQ=+0.0165).
  Edges cut: A=7483 → λ=5.0: 7064.
  Motifs cut: A=6688 → λ=5.0: 5520.

## #4. `CA-HepTh-ncut-k300`

- File: [`data_CA-HepTh_ncut_k300.jsonp.js`](../../visualize/data_CA-HepTh_ncut_k300.jsonp.js)  · Export folder: [`CA-HepTh-ncut-k300/`](../../exports/) (tên file `CA-HepTh-ncut-k300` có thể chứa ký tự đặc biệt)
- Nodes: 8638, Edges: 24806, cc_global: 0.481564

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.6680 | 0.6830 | 0.6899 | 0.6822 | 0.6164 |
| quality · **cc_avg** | 0.5178 | 0.5341 | 0.5443 | 0.5458 | 0.7206 |
| quality · **cc_weighted** | 0.5043 | 0.5251 | 0.5299 | 0.5321 | 0.5715 |
| cut · **edges_cut** | 8037 | 7675 | 7452 | 7690 | 9239 |
| cut · **motifs_cut** | 7264 | 6487 | 6003 | 6324 | 6536 |
| cut · **motifs_internal** | 20605 | 21382 | 21866 | 21545 | 21333 |
| stability · **jaccard_vs_base** | 1 | 0.3549 | 0.2840 | 0.2869 | 0.0369 |

**Highlights**:  Q(A)=0.6680 → Q(λ=5.0)=0.6899 (ΔQ=+0.0219).
  Edges cut: A=8037 → λ=5.0: 7452.
  Motifs cut: A=7264 → λ=5.0: 6003.

## #5. `CA-HepTh-ncut-k400`

- File: [`data_CA-HepTh_ncut_k400.jsonp.js`](../../visualize/data_CA-HepTh_ncut_k400.jsonp.js)  · Export folder: [`CA-HepTh-ncut-k400/`](../../exports/) (tên file `CA-HepTh-ncut-k400` có thể chứa ký tự đặc biệt)
- Nodes: 8638, Edges: 24806, cc_global: 0.481564

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.6514 | 0.6608 | 0.6664 | 0.6657 | 0.5991 |
| quality · **cc_avg** | 0.5156 | 0.5385 | 0.5465 | 0.5417 | 0.7191 |
| quality · **cc_weighted** | 0.5069 | 0.5252 | 0.5328 | 0.5314 | 0.5743 |
| cut · **edges_cut** | 8501 | 8272 | 8122 | 8136 | 9704 |
| cut · **motifs_cut** | 7818 | 7166 | 6906 | 6870 | 7117 |
| cut · **motifs_internal** | 20051 | 20703 | 20963 | 20999 | 20752 |
| stability · **jaccard_vs_base** | 1 | 0.3541 | 0.3199 | 0.2879 | 0.0294 |

**Highlights**:  Q(A)=0.6514 → Q(λ=5.0)=0.6664 (ΔQ=+0.0150).
  Edges cut: A=8501 → λ=5.0: 8122.
  Motifs cut: A=7818 → λ=10.0: 6870.

## #6. `CA-HepTh-ncut-k500`

- File: [`data_CA-HepTh_ncut_k500.jsonp.js`](../../visualize/data_CA-HepTh_ncut_k500.jsonp.js)  · Export folder: [`CA-HepTh-ncut-k500/`](../../exports/) (tên file `CA-HepTh-ncut-k500` có thể chứa ký tự đặc biệt)
- Nodes: 8638, Edges: 24806, cc_global: 0.481564

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.6349 | 0.6473 | 0.6527 | 0.6512 | 0.5776 |
| quality · **cc_avg** | 0.5199 | 0.5334 | 0.5485 | 0.5544 | 0.7239 |
| quality · **cc_weighted** | 0.5150 | 0.5268 | 0.5336 | 0.5337 | 0.5780 |
| cut · **edges_cut** | 8938 | 8637 | 8484 | 8531 | 10264 |
| cut · **motifs_cut** | 8320 | 7563 | 7194 | 7343 | 7862 |
| cut · **motifs_internal** | 19549 | 20306 | 20675 | 20526 | 20007 |
| stability · **jaccard_vs_base** | 1 | 0.4010 | 0.3101 | 0.2854 | 0.0232 |

**Highlights**:  Q(A)=0.6349 → Q(λ=5.0)=0.6527 (ΔQ=+0.0179).
  Edges cut: A=8938 → λ=5.0: 8484.
  Motifs cut: A=8320 → λ=5.0: 7194.

---
*Generated by `experiments/main_result.py` — family=REAL, không filter Q(A), n=6.*
