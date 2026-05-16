# Result — Top 6 REAL

6 bộ test có ΔQ lớn nhất khi dùng mixed matrix, không filter Q(A).

## Ranking

| Rank | Test | Q(A) | Best λ | Q(best) | ΔQ |
|---:|------|-----:|:------:|--------:|---:|
| 1 | `lastfm_asia_edges-ncut-k50` | 0.7486 | `10.0` | 0.7545 | +0.0059 |
| 2 | `lastfm_asia_edges-ncut-k100` | 0.6701 | `10.0` | 0.7167 | +0.0466 |
| 3 | `lastfm_asia_edges-ncut-k200` | 0.5662 | `5.0` | 0.6261 | +0.0599 |
| 4 | `lastfm_asia_edges-ncut-k300` | 0.5020 | `5.0` | 0.5663 | +0.0643 |
| 5 | `lastfm_asia_edges-ncut-k400` | 0.4571 | `5.0` | 0.5348 | +0.0777 |
| 6 | `lastfm_asia_edges-ncut-k500` | 0.4155 | `10.0` | 0.4970 | +0.0815 |

## Bảng modularity Q × λ cho 5 test

| Test | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M | best λ | ΔQ |
|---|---:|---:|---:|---:|---:|---:|---:|
| #1 lastfm_asia_edges-ncut-k50 | 0.7486 | 0.7493 | 0.7517 | 0.7545 | 0.6505 | `10.0` | +0.0059 |
| #2 lastfm_asia_edges-ncut-k100 | 0.6701 | 0.7039 | 0.6933 | 0.7167 | 0.5899 | `10.0` | +0.0466 |
| #3 lastfm_asia_edges-ncut-k200 | 0.5662 | 0.5933 | 0.6261 | 0.6096 | 0.4885 | `5.0` | +0.0599 |
| #4 lastfm_asia_edges-ncut-k300 | 0.5020 | 0.5488 | 0.5663 | 0.5585 | 0.4105 | `5.0` | +0.0643 |
| #5 lastfm_asia_edges-ncut-k400 | 0.4571 | 0.5100 | 0.5348 | 0.5104 | 0.3513 | `5.0` | +0.0777 |
| #6 lastfm_asia_edges-ncut-k500 | 0.4155 | 0.4742 | 0.4906 | 0.4970 | 0.3212 | `10.0` | +0.0815 |

## #1. `lastfm_asia_edges-ncut-k50`

- File: [`data_lastfm_asia_edges_ncut_k50.jsonp.js`](../../visualize/data_lastfm_asia_edges_ncut_k50.jsonp.js)  · Export folder: [`lastfm_asia_edges-ncut-k50/`](../../exports/) (tên file `lastfm_asia_edges-ncut-k50` có thể chứa ký tự đặc biệt)
- Nodes: 7624, Edges: 27806, cc_global: 0.219418

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.7486 | 0.7493 | 0.7517 | 0.7545 | 0.6505 |
| quality · **cc_avg** | 0.2212 | 0.2473 | 0.2662 | 0.2681 | 0.6044 |
| quality · **cc_weighted** | 0.2328 | 0.2491 | 0.2626 | 0.2633 | 0.3146 |
| cut · **edges_cut** | 5119 | 5232 | 5068 | 4955 | 7942 |
| cut · **motifs_cut** | 3207 | 2819 | 2394 | 2247 | 3541 |
| cut · **motifs_internal** | 37226 | 37614 | 38039 | 38186 | 36892 |
| stability · **jaccard_vs_base** | 1 | 0.6396 | 0.5588 | 0.5395 | 0.0757 |

**Highlights**:  Q(A)=0.7486 → Q(λ=10.0)=0.7545 (ΔQ=+0.0059).
  Edges cut: A=5119 → λ=10.0: 4955.
  Motifs cut: A=3207 → λ=10.0: 2247.

## #2. `lastfm_asia_edges-ncut-k100`

- File: [`data_lastfm_asia_edges_ncut_k100.jsonp.js`](../../visualize/data_lastfm_asia_edges_ncut_k100.jsonp.js)  · Export folder: [`lastfm_asia_edges-ncut-k100/`](../../exports/) (tên file `lastfm_asia_edges-ncut-k100` có thể chứa ký tự đặc biệt)
- Nodes: 7624, Edges: 27806, cc_global: 0.219418

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.6701 | 0.7039 | 0.6933 | 0.7167 | 0.5899 |
| quality · **cc_avg** | 0.2158 | 0.2372 | 0.2552 | 0.2539 | 0.6345 |
| quality · **cc_weighted** | 0.2390 | 0.2594 | 0.2724 | 0.2727 | 0.3326 |
| cut · **edges_cut** | 8156 | 6966 | 7343 | 6448 | 10176 |
| cut · **motifs_cut** | 9123 | 4786 | 5967 | 3977 | 8129 |
| cut · **motifs_internal** | 31310 | 35647 | 34466 | 36456 | 32304 |
| stability · **jaccard_vs_base** | 1 | 0.4528 | 0.4172 | 0.4141 | 0.0406 |

**Highlights**:  Q(A)=0.6701 → Q(λ=10.0)=0.7167 (ΔQ=+0.0466).
  Edges cut: A=8156 → λ=10.0: 6448.
  Motifs cut: A=9123 → λ=10.0: 3977.

## #3. `lastfm_asia_edges-ncut-k200`

- File: [`data_lastfm_asia_edges_ncut_k200.jsonp.js`](../../visualize/data_lastfm_asia_edges_ncut_k200.jsonp.js)  · Export folder: [`lastfm_asia_edges-ncut-k200/`](../../exports/) (tên file `lastfm_asia_edges-ncut-k200` có thể chứa ký tự đặc biệt)
- Nodes: 7624, Edges: 27806, cc_global: 0.219418

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.5662 | 0.5933 | 0.6261 | 0.6096 | 0.4885 |
| quality · **cc_avg** | 0.2051 | 0.2326 | 0.2529 | 0.2556 | 0.6439 |
| quality · **cc_weighted** | 0.2465 | 0.2649 | 0.2820 | 0.2818 | 0.3477 |
| cut · **edges_cut** | 11490 | 10666 | 9612 | 10126 | 13414 |
| cut · **motifs_cut** | 17148 | 12491 | 10134 | 11391 | 15906 |
| cut · **motifs_internal** | 23285 | 27942 | 30299 | 29042 | 24527 |
| stability · **jaccard_vs_base** | 1 | 0.4196 | 0.3751 | 0.3681 | 0.0221 |

**Highlights**:  Q(A)=0.5662 → Q(λ=5.0)=0.6261 (ΔQ=+0.0599).
  Edges cut: A=11490 → λ=5.0: 9612.
  Motifs cut: A=17148 → λ=5.0: 10134.

## #4. `lastfm_asia_edges-ncut-k300`

- File: [`data_lastfm_asia_edges_ncut_k300.jsonp.js`](../../visualize/data_lastfm_asia_edges_ncut_k300.jsonp.js)  · Export folder: [`lastfm_asia_edges-ncut-k300/`](../../exports/) (tên file `lastfm_asia_edges-ncut-k300` có thể chứa ký tự đặc biệt)
- Nodes: 7624, Edges: 27806, cc_global: 0.219418

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.5020 | 0.5488 | 0.5663 | 0.5585 | 0.4105 |
| quality · **cc_avg** | 0.1881 | 0.2096 | 0.2391 | 0.2459 | 0.6560 |
| quality · **cc_weighted** | 0.2441 | 0.2630 | 0.2828 | 0.2867 | 0.3496 |
| cut · **edges_cut** | 13443 | 12047 | 11510 | 11756 | 15774 |
| cut · **motifs_cut** | 20365 | 15189 | 14061 | 15057 | 24316 |
| cut · **motifs_internal** | 20068 | 25244 | 26372 | 25376 | 16117 |
| stability · **jaccard_vs_base** | 1 | 0.4063 | 0.3477 | 0.3398 | 0.0154 |

**Highlights**:  Q(A)=0.5020 → Q(λ=5.0)=0.5663 (ΔQ=+0.0643).
  Edges cut: A=13443 → λ=5.0: 11510.
  Motifs cut: A=20365 → λ=5.0: 14061.

## #5. `lastfm_asia_edges-ncut-k400`

- File: [`data_lastfm_asia_edges_ncut_k400.jsonp.js`](../../visualize/data_lastfm_asia_edges_ncut_k400.jsonp.js)  · Export folder: [`lastfm_asia_edges-ncut-k400/`](../../exports/) (tên file `lastfm_asia_edges-ncut-k400` có thể chứa ký tự đặc biệt)
- Nodes: 7624, Edges: 27806, cc_global: 0.219418

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.4571 | 0.5100 | 0.5348 | 0.5104 | 0.3513 |
| quality · **cc_avg** | 0.1663 | 0.1993 | 0.2254 | 0.2436 | 0.6238 |
| quality · **cc_weighted** | 0.2347 | 0.2667 | 0.2840 | 0.2879 | 0.3442 |
| cut · **edges_cut** | 14771 | 13197 | 12467 | 13226 | 17517 |
| cut · **motifs_cut** | 22621 | 16693 | 15980 | 19839 | 30014 |
| cut · **motifs_internal** | 17812 | 23740 | 24453 | 20594 | 10419 |
| stability · **jaccard_vs_base** | 1 | 0.4028 | 0.3422 | 0.3298 | 0.0097 |

**Highlights**:  Q(A)=0.4571 → Q(λ=5.0)=0.5348 (ΔQ=+0.0777).
  Edges cut: A=14771 → λ=5.0: 12467.
  Motifs cut: A=22621 → λ=5.0: 15980.

## #6. `lastfm_asia_edges-ncut-k500`

- File: [`data_lastfm_asia_edges_ncut_k500.jsonp.js`](../../visualize/data_lastfm_asia_edges_ncut_k500.jsonp.js)  · Export folder: [`lastfm_asia_edges-ncut-k500/`](../../exports/) (tên file `lastfm_asia_edges-ncut-k500` có thể chứa ký tự đặc biệt)
- Nodes: 7624, Edges: 27806, cc_global: 0.219418

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.4155 | 0.4742 | 0.4906 | 0.4970 | 0.3212 |
| quality · **cc_avg** | 0.1550 | 0.1887 | 0.2137 | 0.2206 | 0.5510 |
| quality · **cc_weighted** | 0.2269 | 0.2651 | 0.2868 | 0.2870 | 0.3226 |
| cut · **edges_cut** | 15976 | 14282 | 13820 | 13590 | 18376 |
| cut · **motifs_cut** | 24322 | 20172 | 20533 | 18131 | 31332 |
| cut · **motifs_internal** | 16111 | 20261 | 19900 | 22302 | 9101 |
| stability · **jaccard_vs_base** | 1 | 0.3892 | 0.3464 | 0.3285 | 0.0078 |

**Highlights**:  Q(A)=0.4155 → Q(λ=10.0)=0.4970 (ΔQ=+0.0815).
  Edges cut: A=15976 → λ=10.0: 13590.
  Motifs cut: A=24322 → λ=10.0: 18131.

---
*Generated by `experiments/main_result.py` — family=REAL, không filter Q(A), n=6.*
