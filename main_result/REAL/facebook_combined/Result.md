# Result — Top 5 REAL

5 bộ test có ΔQ lớn nhất khi dùng mixed matrix, không filter Q(A).

## Ranking

| Rank | Test | Q(A) | Best λ | Q(best) | ΔQ |
|---:|------|-----:|:------:|--------:|---:|
| 1 | `facebook_combined-ncut-k50` | 0.7810 | `W_M` | 0.7820 | +0.0010 |
| 2 | `facebook_combined-ncut-k100` | 0.6837 | `1.0` | 0.7013 | +0.0175 |
| 3 | `facebook_combined-ncut-k200` | 0.4615 | `1.0` | 0.4785 | +0.0170 |
| 4 | `facebook_combined-ncut-k400` | 0.3216 | `10.0` | 0.3245 | +0.0030 |
| 5 | `facebook_combined-ncut-k500` | 0.2319 | `1.0` | 0.2838 | +0.0519 |

## Bảng modularity Q × λ cho 5 test

| Test | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M | best λ | ΔQ |
|---|---:|---:|---:|---:|---:|---:|---:|
| #1 facebook_combined-ncut-k50 | 0.7810 | 0.7750 | 0.7755 | 0.7819 | 0.7820 | `W_M` | +0.0010 |
| #2 facebook_combined-ncut-k100 | 0.6837 | 0.7013 | 0.6513 | 0.6909 | 0.6960 | `1.0` | +0.0175 |
| #3 facebook_combined-ncut-k200 | 0.4615 | 0.4785 | 0.4614 | 0.4558 | 0.4689 | `1.0` | +0.0170 |
| #4 facebook_combined-ncut-k400 | 0.3216 | 0.3196 | 0.3165 | 0.3245 | 0.2989 | `10.0` | +0.0030 |
| #5 facebook_combined-ncut-k500 | 0.2319 | 0.2838 | 0.2804 | 0.2805 | 0.2679 | `1.0` | +0.0519 |

## #1. `facebook_combined-ncut-k50`

- File: [`data_facebook_combined_ncut_k50.jsonp.js`](../../visualize/data_facebook_combined_ncut_k50.jsonp.js)  · Export folder: [`facebook_combined-ncut-k50/`](../../exports/) (tên file `facebook_combined-ncut-k50` có thể chứa ký tự đặc biệt)
- Nodes: 4039, Edges: 88234, cc_global: 0.605547

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.7810 | 0.7750 | 0.7755 | 0.7819 | 0.7820 |
| quality · **cc_avg** | 0.6561 | 0.6412 | 0.6650 | 0.6587 | 0.6548 |
| quality · **cc_weighted** | 0.6061 | 0.6194 | 0.6181 | 0.6132 | 0.6192 |
| cut · **edges_cut** | 10532 | 11297 | 11229 | 10516 | 10426 |
| cut · **motifs_cut** | 133962 | 140983 | 141111 | 129482 | 121622 |
| cut · **motifs_internal** | 1478048 | 1471027 | 1470899 | 1482528 | 1490388 |
| stability · **jaccard_vs_base** | 1 | 0.7473 | 0.7688 | 0.7957 | 0.7692 |

**Highlights**:  Q(A)=0.7810 → Q(λ=W_M)=0.7820 (ΔQ=+0.0010).
  Edges cut: A=10532 → λ=W_M: 10426.
  Motifs cut: A=133962 → λ=W_M: 121622.

## #2. `facebook_combined-ncut-k100`

- File: [`data_facebook_combined_ncut_k100.jsonp.js`](../../visualize/data_facebook_combined_ncut_k100.jsonp.js)  · Export folder: [`facebook_combined-ncut-k100/`](../../exports/) (tên file `facebook_combined-ncut-k100` có thể chứa ký tự đặc biệt)
- Nodes: 4039, Edges: 88234, cc_global: 0.605547

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.6837 | 0.7013 | 0.6513 | 0.6909 | 0.6960 |
| quality · **cc_avg** | 0.6561 | 0.6598 | 0.6643 | 0.6684 | 0.6684 |
| quality · **cc_weighted** | 0.6358 | 0.6466 | 0.6508 | 0.6480 | 0.6461 |
| cut · **edges_cut** | 20200 | 18580 | 24303 | 19556 | 18956 |
| cut · **motifs_cut** | 250221 | 226361 | 384251 | 241482 | 224190 |
| cut · **motifs_internal** | 1361789 | 1385649 | 1227759 | 1370528 | 1387820 |
| stability · **jaccard_vs_base** | 1 | 0.8112 | 0.7093 | 0.8185 | 0.7653 |

**Highlights**:  Q(A)=0.6837 → Q(λ=1.0)=0.7013 (ΔQ=+0.0175).
  Edges cut: A=20200 → λ=1.0: 18580.
  Motifs cut: A=250221 → λ=W_M: 224190.

## #3. `facebook_combined-ncut-k200`

- File: [`data_facebook_combined_ncut_k200.jsonp.js`](../../visualize/data_facebook_combined_ncut_k200.jsonp.js)  · Export folder: [`facebook_combined-ncut-k200/`](../../exports/) (tên file `facebook_combined-ncut-k200` có thể chứa ký tự đặc biệt)
- Nodes: 4039, Edges: 88234, cc_global: 0.605547

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.4615 | 0.4785 | 0.4614 | 0.4558 | 0.4689 |
| quality · **cc_avg** | 0.6424 | 0.6661 | 0.6768 | 0.6866 | 0.7078 |
| quality · **cc_weighted** | 0.6872 | 0.6979 | 0.6993 | 0.7057 | 0.7044 |
| cut · **edges_cut** | 43329 | 41566 | 43306 | 43835 | 42495 |
| cut · **motifs_cut** | 757872 | 697556 | 747664 | 753537 | 717456 |
| cut · **motifs_internal** | 854138 | 914454 | 864346 | 858473 | 894554 |
| stability · **jaccard_vs_base** | 1 | 0.6743 | 0.6754 | 0.6689 | 0.6460 |

**Highlights**:  Q(A)=0.4615 → Q(λ=1.0)=0.4785 (ΔQ=+0.0170).
  Edges cut: A=43329 → λ=1.0: 41566.
  Motifs cut: A=757872 → λ=1.0: 697556.

## #4. `facebook_combined-ncut-k400`

- File: [`data_facebook_combined_ncut_k400.jsonp.js`](../../visualize/data_facebook_combined_ncut_k400.jsonp.js)  · Export folder: [`facebook_combined-ncut-k400/`](../../exports/) (tên file `facebook_combined-ncut-k400` có thể chứa ký tự đặc biệt)
- Nodes: 4039, Edges: 88234, cc_global: 0.605547

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.3216 | 0.3196 | 0.3165 | 0.3245 | 0.2989 |
| quality · **cc_avg** | 0.5316 | 0.5723 | 0.6096 | 0.6167 | 0.6089 |
| quality · **cc_weighted** | 0.6622 | 0.6936 | 0.7099 | 0.7131 | 0.7069 |
| cut · **edges_cut** | 56677 | 56798 | 57104 | 56340 | 59070 |
| cut · **motifs_cut** | 1011983 | 988882 | 982337 | 968043 | 1109001 |
| cut · **motifs_internal** | 600027 | 623128 | 629673 | 643967 | 503009 |
| stability · **jaccard_vs_base** | 1 | 0.5963 | 0.5523 | 0.5635 | 0.5109 |

**Highlights**:  Q(A)=0.3216 → Q(λ=10.0)=0.3245 (ΔQ=+0.0030).
  Edges cut: A=56677 → λ=10.0: 56340.
  Motifs cut: A=1011983 → λ=10.0: 968043.

## #5. `facebook_combined-ncut-k500`

- File: [`data_facebook_combined_ncut_k500.jsonp.js`](../../visualize/data_facebook_combined_ncut_k500.jsonp.js)  · Export folder: [`facebook_combined-ncut-k500/`](../../exports/) (tên file `facebook_combined-ncut-k500` có thể chứa ký tự đặc biệt)
- Nodes: 4039, Edges: 88234, cc_global: 0.605547

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.2319 | 0.2838 | 0.2804 | 0.2805 | 0.2679 |
| quality · **cc_avg** | 0.4948 | 0.5225 | 0.5243 | 0.5313 | 0.5490 |
| quality · **cc_weighted** | 0.6405 | 0.6694 | 0.6760 | 0.6797 | 0.6831 |
| cut · **edges_cut** | 65785 | 60098 | 60408 | 60391 | 61610 |
| cut · **motifs_cut** | 1359650 | 1010729 | 1014012 | 1011117 | 1034475 |
| cut · **motifs_internal** | 252360 | 601281 | 597998 | 600893 | 577535 |
| stability · **jaccard_vs_base** | 1 | 0.4533 | 0.4465 | 0.4471 | 0.4239 |

**Highlights**:  Q(A)=0.2319 → Q(λ=1.0)=0.2838 (ΔQ=+0.0519).
  Edges cut: A=65785 → λ=1.0: 60098.
  Motifs cut: A=1359650 → λ=1.0: 1010729.

---
*Generated by `experiments/main_result.py` — family=REAL, không filter Q(A), n=5.*
