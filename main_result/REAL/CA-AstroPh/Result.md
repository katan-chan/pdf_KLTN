# Result — Top 6 REAL

6 bộ test có ΔQ lớn nhất khi dùng mixed matrix, không filter Q(A).

## Ranking

| Rank | Test | Q(A) | Best λ | Q(best) | ΔQ |
|---:|------|-----:|:------:|--------:|---:|
| 1 | `CA-AstroPh-ncut-k50` | 0.5266 | `10.0` | 0.5687 | +0.0421 |
| 2 | `CA-AstroPh-ncut-k100` | 0.5331 | `5.0` | 0.5652 | +0.0321 |
| 3 | `CA-AstroPh-ncut-k200` | 0.5221 | `10.0` | 0.5525 | +0.0304 |
| 4 | `CA-AstroPh-ncut-k300` | 0.5111 | `5.0` | 0.5407 | +0.0296 |
| 5 | `CA-AstroPh-ncut-k400` | 0.4973 | `5.0` | 0.5344 | +0.0372 |
| 6 | `CA-AstroPh-ncut-k500` | 0.4879 | `10.0` | 0.5191 | +0.0313 |

## Bảng modularity Q × λ cho 5 test

| Test | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M | best λ | ΔQ |
|---|---:|---:|---:|---:|---:|---:|---:|
| #1 CA-AstroPh-ncut-k50 | 0.5266 | 0.5598 | 0.5623 | 0.5687 | 0.5677 | `10.0` | +0.0421 |
| #2 CA-AstroPh-ncut-k100 | 0.5331 | 0.5638 | 0.5652 | 0.5630 | 0.5581 | `5.0` | +0.0321 |
| #3 CA-AstroPh-ncut-k200 | 0.5221 | 0.5510 | 0.5484 | 0.5525 | 0.5471 | `10.0` | +0.0304 |
| #4 CA-AstroPh-ncut-k300 | 0.5111 | 0.5371 | 0.5407 | 0.5376 | 0.5340 | `5.0` | +0.0296 |
| #5 CA-AstroPh-ncut-k400 | 0.4973 | 0.5207 | 0.5344 | 0.5304 | 0.5257 | `5.0` | +0.0372 |
| #6 CA-AstroPh-ncut-k500 | 0.4879 | 0.5162 | 0.5154 | 0.5191 | 0.5123 | `10.0` | +0.0313 |

## #1. `CA-AstroPh-ncut-k50`

- File: [`data_CA-AstroPh_ncut_k50.jsonp.js`](../../visualize/data_CA-AstroPh_ncut_k50.jsonp.js)  · Export folder: [`CA-AstroPh-ncut-k50/`](../../exports/) (tên file `CA-AstroPh-ncut-k50` có thể chứa ký tự đặc biệt)
- Nodes: 17903, Edges: 196972, cc_global: 0.632823

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.5266 | 0.5598 | 0.5623 | 0.5687 | 0.5677 |
| quality · **cc_avg** | 0.7046 | 0.7082 | 0.7102 | 0.7041 | 0.7518 |
| quality · **cc_weighted** | 0.6365 | 0.6590 | 0.6606 | 0.6592 | 0.6717 |
| cut · **edges_cut** | 68151 | 71240 | 68058 | 71086 | 69604 |
| cut · **motifs_cut** | 499215 | 462330 | 434191 | 440239 | 431616 |
| cut · **motifs_internal** | 850799 | 887684 | 915823 | 909775 | 918398 |
| stability · **jaccard_vs_base** | 1 | 0.1960 | 0.2277 | 0.2178 | 0.2018 |

**Highlights**:  Q(A)=0.5266 → Q(λ=10.0)=0.5687 (ΔQ=+0.0421).
  Edges cut: A=68151 → λ=5.0: 68058.
  Motifs cut: A=499215 → λ=W_M: 431616.

## #2. `CA-AstroPh-ncut-k100`

- File: [`data_CA-AstroPh_ncut_k100.jsonp.js`](../../visualize/data_CA-AstroPh_ncut_k100.jsonp.js)  · Export folder: [`CA-AstroPh-ncut-k100/`](../../exports/) (tên file `CA-AstroPh-ncut-k100` có thể chứa ký tự đặc biệt)
- Nodes: 17903, Edges: 196972, cc_global: 0.632823

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.5331 | 0.5638 | 0.5652 | 0.5630 | 0.5581 |
| quality · **cc_avg** | 0.7053 | 0.7063 | 0.7030 | 0.7070 | 0.7499 |
| quality · **cc_weighted** | 0.6531 | 0.6697 | 0.6737 | 0.6730 | 0.6859 |
| cut · **edges_cut** | 81885 | 80033 | 78154 | 79236 | 82285 |
| cut · **motifs_cut** | 598172 | 492970 | 477205 | 476784 | 501750 |
| cut · **motifs_internal** | 751842 | 857044 | 872809 | 873230 | 848264 |
| stability · **jaccard_vs_base** | 1 | 0.1899 | 0.2204 | 0.1978 | 0.1340 |

**Highlights**:  Q(A)=0.5331 → Q(λ=5.0)=0.5652 (ΔQ=+0.0321).
  Edges cut: A=81885 → λ=5.0: 78154.
  Motifs cut: A=598172 → λ=10.0: 476784.

## #3. `CA-AstroPh-ncut-k200`

- File: [`data_CA-AstroPh_ncut_k200.jsonp.js`](../../visualize/data_CA-AstroPh_ncut_k200.jsonp.js)  · Export folder: [`CA-AstroPh-ncut-k200/`](../../exports/) (tên file `CA-AstroPh-ncut-k200` có thể chứa ký tự đặc biệt)
- Nodes: 17903, Edges: 196972, cc_global: 0.632823

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.5221 | 0.5510 | 0.5484 | 0.5525 | 0.5471 |
| quality · **cc_avg** | 0.6909 | 0.6991 | 0.7070 | 0.7023 | 0.7583 |
| quality · **cc_weighted** | 0.6716 | 0.6845 | 0.6850 | 0.6889 | 0.7011 |
| cut · **edges_cut** | 91188 | 85316 | 85955 | 85030 | 86283 |
| cut · **motifs_cut** | 639495 | 529546 | 538479 | 535905 | 532129 |
| cut · **motifs_internal** | 710519 | 820468 | 811535 | 814109 | 817885 |
| stability · **jaccard_vs_base** | 1 | 0.2987 | 0.2746 | 0.2736 | 0.1783 |

**Highlights**:  Q(A)=0.5221 → Q(λ=10.0)=0.5525 (ΔQ=+0.0304).
  Edges cut: A=91188 → λ=10.0: 85030.
  Motifs cut: A=639495 → λ=1.0: 529546.

## #4. `CA-AstroPh-ncut-k300`

- File: [`data_CA-AstroPh_ncut_k300.jsonp.js`](../../visualize/data_CA-AstroPh_ncut_k300.jsonp.js)  · Export folder: [`CA-AstroPh-ncut-k300/`](../../exports/) (tên file `CA-AstroPh-ncut-k300` có thể chứa ký tự đặc biệt)
- Nodes: 17903, Edges: 196972, cc_global: 0.632823

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.5111 | 0.5371 | 0.5407 | 0.5376 | 0.5340 |
| quality · **cc_avg** | 0.7002 | 0.7044 | 0.7029 | 0.7030 | 0.7576 |
| quality · **cc_weighted** | 0.6823 | 0.6951 | 0.6941 | 0.6968 | 0.7089 |
| cut · **edges_cut** | 94179 | 88945 | 88194 | 88945 | 89581 |
| cut · **motifs_cut** | 652221 | 574966 | 557642 | 575962 | 566208 |
| cut · **motifs_internal** | 697793 | 775048 | 792372 | 774052 | 783806 |
| stability · **jaccard_vs_base** | 1 | 0.3182 | 0.2972 | 0.3021 | 0.1951 |

**Highlights**:  Q(A)=0.5111 → Q(λ=5.0)=0.5407 (ΔQ=+0.0296).
  Edges cut: A=94179 → λ=5.0: 88194.
  Motifs cut: A=652221 → λ=5.0: 557642.

## #5. `CA-AstroPh-ncut-k400`

- File: [`data_CA-AstroPh_ncut_k400.jsonp.js`](../../visualize/data_CA-AstroPh_ncut_k400.jsonp.js)  · Export folder: [`CA-AstroPh-ncut-k400/`](../../exports/) (tên file `CA-AstroPh-ncut-k400` có thể chứa ký tự đặc biệt)
- Nodes: 17903, Edges: 196972, cc_global: 0.632823

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.4973 | 0.5207 | 0.5344 | 0.5304 | 0.5257 |
| quality · **cc_avg** | 0.6879 | 0.7001 | 0.7017 | 0.7031 | 0.7529 |
| quality · **cc_weighted** | 0.6881 | 0.6994 | 0.7026 | 0.7029 | 0.7132 |
| cut · **edges_cut** | 97400 | 92770 | 89648 | 90629 | 91554 |
| cut · **motifs_cut** | 687593 | 615855 | 567755 | 590790 | 581028 |
| cut · **motifs_internal** | 662421 | 734159 | 782259 | 759224 | 768986 |
| stability · **jaccard_vs_base** | 1 | 0.3199 | 0.3215 | 0.3037 | 0.1773 |

**Highlights**:  Q(A)=0.4973 → Q(λ=5.0)=0.5344 (ΔQ=+0.0372).
  Edges cut: A=97400 → λ=5.0: 89648.
  Motifs cut: A=687593 → λ=5.0: 567755.

## #6. `CA-AstroPh-ncut-k500`

- File: [`data_CA-AstroPh_ncut_k500.jsonp.js`](../../visualize/data_CA-AstroPh_ncut_k500.jsonp.js)  · Export folder: [`CA-AstroPh-ncut-k500/`](../../exports/) (tên file `CA-AstroPh-ncut-k500` có thể chứa ký tự đặc biệt)
- Nodes: 17903, Edges: 196972, cc_global: 0.632823

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.4879 | 0.5162 | 0.5154 | 0.5191 | 0.5123 |
| quality · **cc_avg** | 0.6950 | 0.6976 | 0.6955 | 0.6954 | 0.7602 |
| quality · **cc_weighted** | 0.6957 | 0.7041 | 0.7068 | 0.7067 | 0.7177 |
| cut · **edges_cut** | 99538 | 93677 | 93857 | 92959 | 94465 |
| cut · **motifs_cut** | 710526 | 610169 | 631547 | 608218 | 610152 |
| cut · **motifs_internal** | 639488 | 739845 | 718467 | 741796 | 739862 |
| stability · **jaccard_vs_base** | 1 | 0.3491 | 0.3453 | 0.3488 | 0.1738 |

**Highlights**:  Q(A)=0.4879 → Q(λ=10.0)=0.5191 (ΔQ=+0.0313).
  Edges cut: A=99538 → λ=10.0: 92959.
  Motifs cut: A=710526 → λ=10.0: 608218.

---
*Generated by `experiments/main_result.py` — family=REAL, không filter Q(A), n=6.*
