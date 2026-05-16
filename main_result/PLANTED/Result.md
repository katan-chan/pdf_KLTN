# Result — Top 4 PLANTED

4 bộ test có ΔQ lớn nhất khi dùng mixed matrix, filter Q(A) ≥ 0.1.

## Ranking

| Rank | Test | Q(A) | Best λ | Q(best) | ΔQ |
|---:|------|-----:|:------:|--------:|---:|
| 1 | `Planted_k5_s100_pin0.08_pout0.025` | 0.1203 | `0.5` | 0.2185 | +0.0982 |
| 2 | `Planted_k5_s40_pin0.15_pout0.03` | 0.2424 | `0.5` | 0.3164 | +0.0740 |
| 3 | `Planted_k5_s400_pin0.025_pout0.006` | 0.2960 | `0.5` | 0.2974 | +0.0014 |
| 4 | `Planted_k5_s200_pin0.05_pout0.005` | 0.5156 | `0.5` | 0.5156 | +0.0000 |

## Bảng modularity Q × λ cho 5 test

| Test | λ=A | λ=0.5 | λ=1.0 | λ=2.0 | λ=5.0 | λ=10.0 | λ=W_M | best λ | ΔQ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| #1 Planted_k5_s100_pin0.08_pout0.025 | 0.1203 | 0.2185 | 0.2087 | 0.1937 | 0.1825 | 0.1738 | 0.1549 | `0.5` | +0.0982 |
| #2 Planted_k5_s40_pin0.15_pout0.03 | 0.2424 | 0.3164 | 0.3068 | 0.2862 | 0.2955 | 0.2709 | 0.2307 | `0.5` | +0.0740 |
| #3 Planted_k5_s400_pin0.025_pout0.006 | 0.2960 | 0.2974 | 0.2930 | 0.2774 | 0.2379 | 0.1965 | 0.1089 | `0.5` | +0.0014 |
| #4 Planted_k5_s200_pin0.05_pout0.005 | 0.5156 | 0.5156 | 0.5146 | 0.5107 | 0.5009 | 0.4915 | 0.3810 | `0.5` | +0.0000 |

## #1. `Planted_k5_s100_pin0.08_pout0.025`

- File: [`data_planted_500_pout0025_ncut.jsonp.js`](../../visualize/data_planted_500_pout0025_ncut.jsonp.js)  · Export folder: [`Planted_k5_s100_pin0.08_pout0.025/`](../../exports/) (tên file `Planted_k5_s100_pin0.08_pout0.025` có thể chứa ký tự đặc biệt)
- Nodes: 500, Edges: 4422, cc_global: 0.037882
- k_gt: 5

| metric | λ=A | λ=0.5 | λ=1.0 | λ=2.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.1203 | 0.2185 | 0.2087 | 0.1937 | 0.1825 | 0.1738 | 0.1549 |
| quality · **cc_avg** | 0.0575 | 0.0859 | 0.0931 | 0.1117 | 0.1269 | 0.1412 | 0.1344 |
| quality · **cc_weighted** | 0.0604 | 0.0855 | 0.0935 | 0.1117 | 0.1273 | 0.1394 | 0.1540 |
| cut · **edges_cut** | 2992 | 2562 | 2608 | 2673 | 2721 | 2744 | 2862 |
| cut · **motifs_cut** | 747 | 618 | 599 | 576 | 551 | 544 | 564 |
| cut · **motifs_internal** | 243 | 372 | 391 | 414 | 439 | 446 | 426 |
| stability · **jaccard_vs_base** | 1 | 0.3078 | 0.2177 | 0.1930 | 0.1747 | 0.1556 | 0.1323 |
| compare_to_GT · **nmi** | 0.2043 | 0.3332 | 0.3170 | 0.1936 | 0.1658 | 0.1424 | 0.1143 |
| compare_to_GT · **jaccard** | 0.2149 | 0.3075 | 0.2899 | 0.2001 | 0.1803 | 0.1664 | 0.1489 |

**Highlights**:  Q(A)=0.1203 → Q(λ=0.5)=0.2185 (ΔQ=+0.0982).
  Edges cut: A=2992 → λ=0.5: 2562.
  Motifs cut: A=747 → λ=10.0: 544.
  NMI: A=0.2043 → λ=0.5: 0.3332.

## #2. `Planted_k5_s40_pin0.15_pout0.03`

- File: [`data_planted_200_pout003_ncut.jsonp.js`](../../visualize/data_planted_200_pout003_ncut.jsonp.js)  · Export folder: [`Planted_k5_s40_pin0.15_pout0.03/`](../../exports/) (tên file `Planted_k5_s40_pin0.15_pout0.03` có thể chứa ký tự đặc biệt)
- Nodes: 200, Edges: 1088, cc_global: 0.067309
- k_gt: 5

| metric | λ=A | λ=0.5 | λ=1.0 | λ=2.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.2424 | 0.3164 | 0.3068 | 0.2862 | 0.2955 | 0.2709 | 0.2307 |
| quality · **cc_avg** | 0.1315 | 0.1469 | 0.1809 | 0.1963 | 0.2171 | 0.2043 | 0.2887 |
| quality · **cc_weighted** | 0.1283 | 0.1458 | 0.1815 | 0.1939 | 0.2167 | 0.2072 | 0.2967 |
| cut · **edges_cut** | 601 | 524 | 533 | 555 | 543 | 565 | 613 |
| cut · **motifs_cut** | 148 | 116 | 109 | 108 | 100 | 99 | 92 |
| cut · **motifs_internal** | 112 | 144 | 151 | 152 | 160 | 161 | 168 |
| stability · **jaccard_vs_base** | 1 | 0.4546 | 0.4338 | 0.3810 | 0.3706 | 0.2985 | 0.2278 |
| compare_to_GT · **nmi** | 0.5076 | 0.5504 | 0.4843 | 0.4649 | 0.4774 | 0.3904 | 0.2991 |
| compare_to_GT · **jaccard** | 0.3972 | 0.4544 | 0.3903 | 0.3853 | 0.3731 | 0.2998 | 0.2420 |

**Highlights**:  Q(A)=0.2424 → Q(λ=0.5)=0.3164 (ΔQ=+0.0740).
  Edges cut: A=601 → λ=0.5: 524.
  Motifs cut: A=148 → λ=W_M: 92.
  NMI: A=0.5076 → λ=0.5: 0.5504.

## #3. `Planted_k5_s400_pin0.025_pout0.006`

- File: [`data_planted_2000_pout0006_ncut.jsonp.js`](../../visualize/data_planted_2000_pout0006_ncut.jsonp.js)  · Export folder: [`Planted_k5_s400_pin0.025_pout0.006/`](../../exports/) (tên file `Planted_k5_s400_pin0.025_pout0.006` có thể chứa ký tự đặc biệt)
- Nodes: 2000, Edges: 19783, cc_global: 0.012342
- k_gt: 5

| metric | λ=A | λ=0.5 | λ=1.0 | λ=2.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.2960 | 0.2974 | 0.2930 | 0.2774 | 0.2379 | 0.1965 | 0.1089 |
| quality · **cc_avg** | 0.0250 | 0.0290 | 0.0314 | 0.0398 | 0.0548 | 0.0653 | 0.1218 |
| quality · **cc_weighted** | 0.0250 | 0.0290 | 0.0313 | 0.0398 | 0.0545 | 0.0636 | 0.1147 |
| cut · **edges_cut** | 9969 | 9941 | 10026 | 10333 | 11098 | 11853 | 13936 |
| cut · **motifs_cut** | 778 | 706 | 683 | 629 | 580 | 618 | 655 |
| cut · **motifs_internal** | 829 | 901 | 924 | 978 | 1027 | 989 | 952 |
| stability · **jaccard_vs_base** | 1 | 0.8262 | 0.7439 | 0.6185 | 0.4130 | 0.2720 | 0.1177 |
| compare_to_GT · **nmi** | 0.7403 | 0.7441 | 0.7172 | 0.6370 | 0.4572 | 0.2747 | 0.0388 |
| compare_to_GT · **jaccard** | 0.7107 | 0.7170 | 0.6860 | 0.5976 | 0.4175 | 0.2688 | 0.1172 |

**Highlights**:  Q(A)=0.2960 → Q(λ=0.5)=0.2974 (ΔQ=+0.0014).
  Edges cut: A=9969 → λ=0.5: 9941.
  Motifs cut: A=778 → λ=5.0: 580.
  NMI: A=0.7403 → λ=0.5: 0.7441.

## #4. `Planted_k5_s200_pin0.05_pout0.005`

- File: [`data_planted_1000_pout0005_ncut.jsonp.js`](../../visualize/data_planted_1000_pout0005_ncut.jsonp.js)  · Export folder: [`Planted_k5_s200_pin0.05_pout0.005/`](../../exports/) (tên file `Planted_k5_s200_pin0.05_pout0.005` có thể chứa ký tự đặc biệt)
- Nodes: 1000, Edges: 6869, cc_global: 0.028177
- k_gt: 5

| metric | λ=A | λ=0.5 | λ=1.0 | λ=2.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.5156 | 0.5156 | 0.5146 | 0.5107 | 0.5009 | 0.4915 | 0.3810 |
| quality · **cc_avg** | 0.0479 | 0.0492 | 0.0501 | 0.0529 | 0.0599 | 0.0636 | 0.0939 |
| quality · **cc_weighted** | 0.0479 | 0.0492 | 0.0501 | 0.0529 | 0.0599 | 0.0636 | 0.0967 |
| cut · **edges_cut** | 1953 | 1953 | 1960 | 1987 | 2053 | 2118 | 3076 |
| cut · **motifs_cut** | 108 | 103 | 100 | 95 | 87 | 86 | 91 |
| cut · **motifs_internal** | 768 | 773 | 776 | 781 | 789 | 790 | 785 |
| stability · **jaccard_vs_base** | 1 | 0.9841 | 0.9763 | 0.9459 | 0.8954 | 0.8551 | 0.5286 |
| compare_to_GT · **nmi** | 0.9883 | 0.9883 | 0.9804 | 0.9529 | 0.9187 | 0.8839 | 0.6195 |
| compare_to_GT · **jaccard** | 0.9881 | 0.9881 | 0.9802 | 0.9495 | 0.9059 | 0.8650 | 0.5343 |

**Highlights**:  Q(A)=0.5156 → Q(λ=0.5)=0.5156 (ΔQ=+0.0000).
  Edges cut: A=1953 → λ=A: 1953.
  Motifs cut: A=108 → λ=10.0: 86.
  NMI: A=0.9883 → λ=A: 0.9883.

---
*Generated by `experiments/main_result.py` — family=PLANTED, filter Q(A) ≥ 0.1, n=4.*
