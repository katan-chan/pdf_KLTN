# Result — Top 6 REAL

6 bộ test có ΔQ lớn nhất khi dùng mixed matrix, không filter Q(A).

## Ranking

| Rank | Test | Q(A) | Best λ | Q(best) | ΔQ |
|---:|------|-----:|:------:|--------:|---:|
| 1 | `musae_DE_edges-ncut-k50` | 0.0469 | `W_M` | 0.1625 | +0.1156 |
| 2 | `musae_DE_edges-ncut-k100` | 0.0758 | `W_M` | 0.1675 | +0.0917 |
| 3 | `musae_DE_edges-ncut-k200` | 0.0943 | `10.0` | 0.1513 | +0.0570 |
| 4 | `musae_DE_edges-ncut-k300` | 0.0956 | `1.0` | 0.1198 | +0.0241 |
| 5 | `musae_DE_edges-ncut-k400` | 0.0870 | `5.0` | 0.1147 | +0.0277 |
| 6 | `musae_DE_edges-ncut-k500` | 0.0770 | `10.0` | 0.1071 | +0.0301 |

## Bảng modularity Q × λ cho 5 test

| Test | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M | best λ | ΔQ |
|---|---:|---:|---:|---:|---:|---:|---:|
| #1 musae_DE_edges-ncut-k50 | 0.0469 | 0.1581 | 0.1513 | 0.1469 | 0.1625 | `W_M` | +0.1156 |
| #2 musae_DE_edges-ncut-k100 | 0.0758 | 0.1476 | 0.1506 | 0.1525 | 0.1675 | `W_M` | +0.0917 |
| #3 musae_DE_edges-ncut-k200 | 0.0943 | 0.1493 | 0.1511 | 0.1513 | 0.1380 | `10.0` | +0.0570 |
| #4 musae_DE_edges-ncut-k300 | 0.0956 | 0.1198 | 0.1156 | 0.1161 | 0.1139 | `1.0` | +0.0241 |
| #5 musae_DE_edges-ncut-k400 | 0.0870 | 0.1116 | 0.1147 | 0.1144 | 0.1070 | `5.0` | +0.0277 |
| #6 musae_DE_edges-ncut-k500 | 0.0770 | 0.1053 | 0.1036 | 0.1071 | 0.0994 | `10.0` | +0.0301 |

## #1. `musae_DE_edges-ncut-k50`

- File: [`data_musae_DE_edges_ncut_k50.jsonp.js`](../../visualize/data_musae_DE_edges_ncut_k50.jsonp.js)  · Export folder: [`musae_DE_edges-ncut-k50/`](../../exports/) (tên file `musae_DE_edges-ncut-k50` có thể chứa ký tự đặc biệt)
- Nodes: 9498, Edges: 153138, cc_global: 0.200886

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.0469 | 0.1581 | 0.1513 | 0.1469 | 0.1625 |
| quality · **cc_avg** | 0.1386 | 0.2432 | 0.2631 | 0.2630 | 0.4103 |
| quality · **cc_weighted** | 0.1132 | 0.2746 | 0.2885 | 0.2810 | 0.3531 |
| cut · **edges_cut** | 140187 | 121823 | 123695 | 124389 | 122786 |
| cut · **motifs_cut** | 586297 | 528220 | 544905 | 546784 | 543404 |
| cut · **motifs_internal** | 16791 | 74868 | 58183 | 56304 | 59684 |
| stability · **jaccard_vs_base** | 1 | 0.1106 | 0.1018 | 0.0968 | 0.0657 |

**Highlights**:  Q(A)=0.0469 → Q(λ=W_M)=0.1625 (ΔQ=+0.1156).
  Edges cut: A=140187 → λ=1.0: 121823.
  Motifs cut: A=586297 → λ=1.0: 528220.

## #2. `musae_DE_edges-ncut-k100`

- File: [`data_musae_DE_edges_ncut_k100.jsonp.js`](../../visualize/data_musae_DE_edges_ncut_k100.jsonp.js)  · Export folder: [`musae_DE_edges-ncut-k100/`](../../exports/) (tên file `musae_DE_edges-ncut-k100` có thể chứa ký tự đặc biệt)
- Nodes: 9498, Edges: 153138, cc_global: 0.200886

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.0758 | 0.1476 | 0.1506 | 0.1525 | 0.1675 |
| quality · **cc_avg** | 0.1568 | 0.2879 | 0.3095 | 0.3213 | 0.4586 |
| quality · **cc_weighted** | 0.1493 | 0.3105 | 0.3299 | 0.3318 | 0.3922 |
| cut · **edges_cut** | 138256 | 127378 | 126927 | 126067 | 124447 |
| cut · **motifs_cut** | 578537 | 551514 | 554340 | 550572 | 544492 |
| cut · **motifs_internal** | 24551 | 51574 | 48748 | 52516 | 58596 |
| stability · **jaccard_vs_base** | 1 | 0.1496 | 0.1357 | 0.1309 | 0.0650 |

**Highlights**:  Q(A)=0.0758 → Q(λ=W_M)=0.1675 (ΔQ=+0.0917).
  Edges cut: A=138256 → λ=W_M: 124447.
  Motifs cut: A=578537 → λ=W_M: 544492.

## #3. `musae_DE_edges-ncut-k200`

- File: [`data_musae_DE_edges_ncut_k200.jsonp.js`](../../visualize/data_musae_DE_edges_ncut_k200.jsonp.js)  · Export folder: [`musae_DE_edges-ncut-k200/`](../../exports/) (tên file `musae_DE_edges-ncut-k200` có thể chứa ký tự đặc biệt)
- Nodes: 9498, Edges: 153138, cc_global: 0.200886

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.0943 | 0.1493 | 0.1511 | 0.1513 | 0.1380 |
| quality · **cc_avg** | 0.1866 | 0.2795 | 0.3162 | 0.3445 | 0.4475 |
| quality · **cc_weighted** | 0.1977 | 0.3368 | 0.3587 | 0.3621 | 0.3932 |
| cut · **edges_cut** | 136306 | 128429 | 128182 | 128104 | 130411 |
| cut · **motifs_cut** | 572748 | 558230 | 558280 | 556296 | 564989 |
| cut · **motifs_internal** | 30340 | 44858 | 44808 | 46792 | 38099 |
| stability · **jaccard_vs_base** | 1 | 0.2000 | 0.1631 | 0.1568 | 0.0551 |

**Highlights**:  Q(A)=0.0943 → Q(λ=10.0)=0.1513 (ΔQ=+0.0570).
  Edges cut: A=136306 → λ=10.0: 128104.
  Motifs cut: A=572748 → λ=10.0: 556296.

## #4. `musae_DE_edges-ncut-k300`

- File: [`data_musae_DE_edges_ncut_k300.jsonp.js`](../../visualize/data_musae_DE_edges_ncut_k300.jsonp.js)  · Export folder: [`musae_DE_edges-ncut-k300/`](../../exports/) (tên file `musae_DE_edges-ncut-k300` có thể chứa ký tự đặc biệt)
- Nodes: 9498, Edges: 153138, cc_global: 0.200886

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.0956 | 0.1198 | 0.1156 | 0.1161 | 0.1139 |
| quality · **cc_avg** | 0.1839 | 0.2698 | 0.2951 | 0.3118 | 0.4433 |
| quality · **cc_weighted** | 0.2137 | 0.2981 | 0.3079 | 0.3207 | 0.3583 |
| cut · **edges_cut** | 136546 | 133306 | 133958 | 134042 | 134360 |
| cut · **motifs_cut** | 572384 | 570975 | 572826 | 573667 | 574991 |
| cut · **motifs_internal** | 30704 | 32113 | 30262 | 29421 | 28097 |
| stability · **jaccard_vs_base** | 1 | 0.2147 | 0.1721 | 0.1709 | 0.0524 |

**Highlights**:  Q(A)=0.0956 → Q(λ=1.0)=0.1198 (ΔQ=+0.0241).
  Edges cut: A=136546 → λ=1.0: 133306.
  Motifs cut: A=572384 → λ=1.0: 570975.

## #5. `musae_DE_edges-ncut-k400`

- File: [`data_musae_DE_edges_ncut_k400.jsonp.js`](../../visualize/data_musae_DE_edges_ncut_k400.jsonp.js)  · Export folder: [`musae_DE_edges-ncut-k400/`](../../exports/) (tên file `musae_DE_edges-ncut-k400` có thể chứa ký tự đặc biệt)
- Nodes: 9498, Edges: 153138, cc_global: 0.200886

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.0870 | 0.1116 | 0.1147 | 0.1144 | 0.1070 |
| quality · **cc_avg** | 0.1769 | 0.2624 | 0.2940 | 0.3132 | 0.4288 |
| quality · **cc_weighted** | 0.2139 | 0.3104 | 0.3212 | 0.3312 | 0.3695 |
| cut · **edges_cut** | 138234 | 134738 | 134399 | 134558 | 135749 |
| cut · **motifs_cut** | 576697 | 575116 | 573920 | 576093 | 579577 |
| cut · **motifs_internal** | 26391 | 27972 | 29168 | 26995 | 23511 |
| stability · **jaccard_vs_base** | 1 | 0.2077 | 0.1674 | 0.1498 | 0.0403 |

**Highlights**:  Q(A)=0.0870 → Q(λ=5.0)=0.1147 (ΔQ=+0.0277).
  Edges cut: A=138234 → λ=5.0: 134399.
  Motifs cut: A=576697 → λ=5.0: 573920.

## #6. `musae_DE_edges-ncut-k500`

- File: [`data_musae_DE_edges_ncut_k500.jsonp.js`](../../visualize/data_musae_DE_edges_ncut_k500.jsonp.js)  · Export folder: [`musae_DE_edges-ncut-k500/`](../../exports/) (tên file `musae_DE_edges-ncut-k500` có thể chứa ký tự đặc biệt)
- Nodes: 9498, Edges: 153138, cc_global: 0.200886

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.0770 | 0.1053 | 0.1036 | 0.1071 | 0.0994 |
| quality · **cc_avg** | 0.1680 | 0.2555 | 0.2961 | 0.3033 | 0.4175 |
| quality · **cc_weighted** | 0.2078 | 0.3068 | 0.3244 | 0.3413 | 0.3713 |
| cut · **edges_cut** | 139854 | 136002 | 136249 | 135830 | 137067 |
| cut · **motifs_cut** | 579507 | 579059 | 580758 | 581144 | 582682 |
| cut · **motifs_internal** | 23581 | 24029 | 22330 | 21944 | 20406 |
| stability · **jaccard_vs_base** | 1 | 0.1916 | 0.1437 | 0.1322 | 0.0323 |

**Highlights**:  Q(A)=0.0770 → Q(λ=10.0)=0.1071 (ΔQ=+0.0301).
  Edges cut: A=139854 → λ=10.0: 135830.
  Motifs cut: A=579507 → λ=1.0: 579059.

---
*Generated by `experiments/main_result.py` — family=REAL, không filter Q(A), n=6.*
