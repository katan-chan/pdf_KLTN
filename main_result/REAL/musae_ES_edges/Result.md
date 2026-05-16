# Result — Top 6 REAL

6 bộ test có ΔQ lớn nhất khi dùng mixed matrix, không filter Q(A).

## Ranking

| Rank | Test | Q(A) | Best λ | Q(best) | ΔQ |
|---:|------|-----:|:------:|--------:|---:|
| 1 | `musae_ES_edges-ncut-k50` | 0.1280 | `1.0` | 0.2183 | +0.0902 |
| 2 | `musae_ES_edges-ncut-k100` | 0.1216 | `1.0` | 0.1983 | +0.0767 |
| 3 | `musae_ES_edges-ncut-k200` | 0.1106 | `10.0` | 0.1589 | +0.0483 |
| 4 | `musae_ES_edges-ncut-k300` | 0.0960 | `1.0` | 0.1219 | +0.0259 |
| 5 | `musae_ES_edges-ncut-k400` | 0.0777 | `1.0` | 0.1084 | +0.0308 |
| 6 | `musae_ES_edges-ncut-k500` | 0.0680 | `1.0` | 0.0968 | +0.0288 |

## Bảng modularity Q × λ cho 5 test

| Test | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M | best λ | ΔQ |
|---|---:|---:|---:|---:|---:|---:|---:|
| #1 musae_ES_edges-ncut-k50 | 0.1280 | 0.2183 | 0.2156 | 0.2159 | 0.2070 | `1.0` | +0.0902 |
| #2 musae_ES_edges-ncut-k100 | 0.1216 | 0.1983 | 0.1832 | 0.1872 | 0.1823 | `1.0` | +0.0767 |
| #3 musae_ES_edges-ncut-k200 | 0.1106 | 0.1404 | 0.1587 | 0.1589 | 0.1278 | `10.0` | +0.0483 |
| #4 musae_ES_edges-ncut-k300 | 0.0960 | 0.1219 | 0.1174 | 0.1179 | 0.1117 | `1.0` | +0.0259 |
| #5 musae_ES_edges-ncut-k400 | 0.0777 | 0.1084 | 0.1063 | 0.1050 | 0.0922 | `1.0` | +0.0308 |
| #6 musae_ES_edges-ncut-k500 | 0.0680 | 0.0968 | 0.0922 | 0.0909 | 0.0726 | `1.0` | +0.0288 |

## #1. `musae_ES_edges-ncut-k50`

- File: [`data_musae_ES_edges_ncut_k50.jsonp.js`](../../visualize/data_musae_ES_edges_ncut_k50.jsonp.js)  · Export folder: [`musae_ES_edges-ncut-k50/`](../../exports/) (tên file `musae_ES_edges-ncut-k50` có thể chứa ký tự đặc biệt)
- Nodes: 4648, Edges: 59382, cc_global: 0.222496

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.1280 | 0.2183 | 0.2156 | 0.2159 | 0.2070 |
| quality · **cc_avg** | 0.1923 | 0.2858 | 0.3320 | 0.3504 | 0.4678 |
| quality · **cc_weighted** | 0.1793 | 0.3156 | 0.3481 | 0.3508 | 0.3968 |
| cut · **edges_cut** | 49497 | 43766 | 44087 | 44147 | 45177 |
| cut · **motifs_cut** | 170110 | 161643 | 164750 | 161826 | 167090 |
| cut · **motifs_internal** | 30034 | 38501 | 35394 | 38318 | 33054 |
| stability · **jaccard_vs_base** | 1 | 0.2021 | 0.1840 | 0.1816 | 0.1009 |

**Highlights**:  Q(A)=0.1280 → Q(λ=1.0)=0.2183 (ΔQ=+0.0902).
  Edges cut: A=49497 → λ=1.0: 43766.
  Motifs cut: A=170110 → λ=1.0: 161643.

## #2. `musae_ES_edges-ncut-k100`

- File: [`data_musae_ES_edges_ncut_k100.jsonp.js`](../../visualize/data_musae_ES_edges_ncut_k100.jsonp.js)  · Export folder: [`musae_ES_edges-ncut-k100/`](../../exports/) (tên file `musae_ES_edges-ncut-k100` có thể chứa ký tự đặc biệt)
- Nodes: 4648, Edges: 59382, cc_global: 0.222496

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.1216 | 0.1983 | 0.1832 | 0.1872 | 0.1823 |
| quality · **cc_avg** | 0.1893 | 0.2891 | 0.3151 | 0.3389 | 0.4840 |
| quality · **cc_weighted** | 0.1867 | 0.3436 | 0.3614 | 0.3631 | 0.4180 |
| cut · **edges_cut** | 50761 | 46167 | 47236 | 46903 | 47516 |
| cut · **motifs_cut** | 175318 | 166473 | 172851 | 171848 | 174078 |
| cut · **motifs_internal** | 24826 | 33671 | 27293 | 28296 | 26066 |
| stability · **jaccard_vs_base** | 1 | 0.2438 | 0.2097 | 0.1849 | 0.0715 |

**Highlights**:  Q(A)=0.1216 → Q(λ=1.0)=0.1983 (ΔQ=+0.0767).
  Edges cut: A=50761 → λ=1.0: 46167.
  Motifs cut: A=175318 → λ=1.0: 166473.

## #3. `musae_ES_edges-ncut-k200`

- File: [`data_musae_ES_edges_ncut_k200.jsonp.js`](../../visualize/data_musae_ES_edges_ncut_k200.jsonp.js)  · Export folder: [`musae_ES_edges-ncut-k200/`](../../exports/) (tên file `musae_ES_edges-ncut-k200` có thể chứa ký tự đặc biệt)
- Nodes: 4648, Edges: 59382, cc_global: 0.222496

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.1106 | 0.1404 | 0.1587 | 0.1589 | 0.1278 |
| quality · **cc_avg** | 0.1841 | 0.2702 | 0.3240 | 0.3194 | 0.4423 |
| quality · **cc_weighted** | 0.2086 | 0.3065 | 0.3678 | 0.3610 | 0.3593 |
| cut · **edges_cut** | 51908 | 50251 | 49296 | 49249 | 51153 |
| cut · **motifs_cut** | 179522 | 181461 | 181497 | 181143 | 185165 |
| cut · **motifs_internal** | 20622 | 18683 | 18647 | 19001 | 14979 |
| stability · **jaccard_vs_base** | 1 | 0.2358 | 0.1712 | 0.1675 | 0.0508 |

**Highlights**:  Q(A)=0.1106 → Q(λ=10.0)=0.1589 (ΔQ=+0.0483).
  Edges cut: A=51908 → λ=10.0: 49249.
  Motifs cut: A=179522 → λ=0.0: 179522.

## #4. `musae_ES_edges-ncut-k300`

- File: [`data_musae_ES_edges_ncut_k300.jsonp.js`](../../visualize/data_musae_ES_edges_ncut_k300.jsonp.js)  · Export folder: [`musae_ES_edges-ncut-k300/`](../../exports/) (tên file `musae_ES_edges-ncut-k300` có thể chứa ký tự đặc biệt)
- Nodes: 4648, Edges: 59382, cc_global: 0.222496

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.0960 | 0.1219 | 0.1174 | 0.1179 | 0.1117 |
| quality · **cc_avg** | 0.1677 | 0.2609 | 0.2900 | 0.2855 | 0.4039 |
| quality · **cc_weighted** | 0.1992 | 0.2975 | 0.3074 | 0.3027 | 0.3500 |
| cut · **edges_cut** | 52934 | 51586 | 51896 | 51875 | 52289 |
| cut · **motifs_cut** | 182151 | 185683 | 187449 | 186910 | 187342 |
| cut · **motifs_internal** | 17993 | 14461 | 12695 | 13234 | 12802 |
| stability · **jaccard_vs_base** | 1 | 0.2122 | 0.1704 | 0.1626 | 0.0414 |

**Highlights**:  Q(A)=0.0960 → Q(λ=1.0)=0.1219 (ΔQ=+0.0259).
  Edges cut: A=52934 → λ=1.0: 51586.
  Motifs cut: A=182151 → λ=0.0: 182151.

## #5. `musae_ES_edges-ncut-k400`

- File: [`data_musae_ES_edges_ncut_k400.jsonp.js`](../../visualize/data_musae_ES_edges_ncut_k400.jsonp.js)  · Export folder: [`musae_ES_edges-ncut-k400/`](../../exports/) (tên file `musae_ES_edges-ncut-k400` có thể chứa ký tự đặc biệt)
- Nodes: 4648, Edges: 59382, cc_global: 0.222496

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.0777 | 0.1084 | 0.1063 | 0.1050 | 0.0922 |
| quality · **cc_avg** | 0.1574 | 0.2347 | 0.2712 | 0.2704 | 0.3749 |
| quality · **cc_weighted** | 0.1908 | 0.2874 | 0.2999 | 0.3082 | 0.3300 |
| cut · **edges_cut** | 54219 | 52491 | 52685 | 52758 | 53535 |
| cut · **motifs_cut** | 187376 | 187060 | 188869 | 191258 | 192903 |
| cut · **motifs_internal** | 12768 | 13084 | 11275 | 8886 | 7241 |
| stability · **jaccard_vs_base** | 1 | 0.2164 | 0.1668 | 0.1519 | 0.0295 |

**Highlights**:  Q(A)=0.0777 → Q(λ=1.0)=0.1084 (ΔQ=+0.0308).
  Edges cut: A=54219 → λ=1.0: 52491.
  Motifs cut: A=187376 → λ=1.0: 187060.

## #6. `musae_ES_edges-ncut-k500`

- File: [`data_musae_ES_edges_ncut_k500.jsonp.js`](../../visualize/data_musae_ES_edges_ncut_k500.jsonp.js)  · Export folder: [`musae_ES_edges-ncut-k500/`](../../exports/) (tên file `musae_ES_edges-ncut-k500` có thể chứa ký tự đặc biệt)
- Nodes: 4648, Edges: 59382, cc_global: 0.222496

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.0680 | 0.0968 | 0.0922 | 0.0909 | 0.0726 |
| quality · **cc_avg** | 0.1374 | 0.2213 | 0.2421 | 0.2534 | 0.3035 |
| quality · **cc_weighted** | 0.1785 | 0.2814 | 0.2874 | 0.2917 | 0.2812 |
| cut · **edges_cut** | 54906 | 53233 | 53553 | 53650 | 54754 |
| cut · **motifs_cut** | 188257 | 188535 | 190706 | 192169 | 195369 |
| cut · **motifs_internal** | 11887 | 11609 | 9438 | 7975 | 4775 |
| stability · **jaccard_vs_base** | 1 | 0.1889 | 0.1420 | 0.1248 | 0.0215 |

**Highlights**:  Q(A)=0.0680 → Q(λ=1.0)=0.0968 (ΔQ=+0.0288).
  Edges cut: A=54906 → λ=1.0: 53233.
  Motifs cut: A=188257 → λ=0.0: 188257.

---
*Generated by `experiments/main_result.py` — family=REAL, không filter Q(A), n=6.*
