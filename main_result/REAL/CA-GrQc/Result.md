# Result — Top 6 REAL

6 bộ test có ΔQ lớn nhất khi dùng mixed matrix, không filter Q(A).

## Ranking

| Rank | Test | Q(A) | Best λ | Q(best) | ΔQ |
|---:|------|-----:|:------:|--------:|---:|
| 1 | `CA-GrQc-ncut-k50` | 0.8161 | `10.0` | 0.8191 | +0.0031 |
| 2 | `CA-GrQc-ncut-k100` | 0.8117 | `1.0` | 0.8173 | +0.0056 |
| 3 | `CA-GrQc-ncut-k200` | 0.7825 | `5.0` | 0.7930 | +0.0104 |
| 4 | `CA-GrQc-ncut-k300` | 0.7508 | `1.0` | 0.7639 | +0.0131 |
| 5 | `CA-GrQc-ncut-k400` | 0.7143 | `5.0` | 0.7364 | +0.0221 |
| 6 | `CA-GrQc-ncut-k500` | 0.6630 | `5.0` | 0.7105 | +0.0476 |

## Bảng modularity Q × λ cho 5 test

| Test | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M | best λ | ΔQ |
|---|---:|---:|---:|---:|---:|---:|---:|
| #1 CA-GrQc-ncut-k50 | 0.8161 | 0.8175 | 0.8160 | 0.8191 | 0.7745 | `10.0` | +0.0031 |
| #2 CA-GrQc-ncut-k100 | 0.8117 | 0.8173 | 0.8157 | 0.8139 | 0.7610 | `1.0` | +0.0056 |
| #3 CA-GrQc-ncut-k200 | 0.7825 | 0.7928 | 0.7930 | 0.7907 | 0.7325 | `5.0` | +0.0104 |
| #4 CA-GrQc-ncut-k300 | 0.7508 | 0.7639 | 0.7592 | 0.7623 | 0.7040 | `1.0` | +0.0131 |
| #5 CA-GrQc-ncut-k400 | 0.7143 | 0.7351 | 0.7364 | 0.7354 | 0.6744 | `5.0` | +0.0221 |
| #6 CA-GrQc-ncut-k500 | 0.6630 | 0.7097 | 0.7105 | 0.7105 | 0.6349 | `5.0` | +0.0476 |

## #1. `CA-GrQc-ncut-k50`

- File: [`data_CA-GrQc_ncut_k50.jsonp.js`](../../visualize/data_CA-GrQc_ncut_k50.jsonp.js)  · Export folder: [`CA-GrQc-ncut-k50/`](../../exports/) (tên file `CA-GrQc-ncut-k50` có thể chứa ký tự đặc biệt)
- Nodes: 4158, Edges: 13422, cc_global: 0.556878

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.8161 | 0.8175 | 0.8160 | 0.8191 | 0.7745 |
| quality · **cc_avg** | 0.5822 | 0.6035 | 0.6089 | 0.6056 | 0.7574 |
| quality · **cc_weighted** | 0.5677 | 0.5805 | 0.5872 | 0.5879 | 0.6167 |
| cut · **edges_cut** | 1918 | 1932 | 1931 | 1912 | 2477 |
| cut · **motifs_cut** | 1659 | 1518 | 1455 | 1422 | 1451 |
| cut · **motifs_internal** | 46120 | 46261 | 46324 | 46357 | 46328 |
| stability · **jaccard_vs_base** | 1 | 0.2850 | 0.2774 | 0.2787 | 0.0910 |

**Highlights**:  Q(A)=0.8161 → Q(λ=10.0)=0.8191 (ΔQ=+0.0031).
  Edges cut: A=1918 → λ=10.0: 1912.
  Motifs cut: A=1659 → λ=10.0: 1422.

## #2. `CA-GrQc-ncut-k100`

- File: [`data_CA-GrQc_ncut_k100.jsonp.js`](../../visualize/data_CA-GrQc_ncut_k100.jsonp.js)  · Export folder: [`CA-GrQc-ncut-k100/`](../../exports/) (tên file `CA-GrQc-ncut-k100` có thể chứa ký tự đặc biệt)
- Nodes: 4158, Edges: 13422, cc_global: 0.556878

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.8117 | 0.8173 | 0.8157 | 0.8139 | 0.7610 |
| quality · **cc_avg** | 0.5804 | 0.5957 | 0.6002 | 0.5999 | 0.7628 |
| quality · **cc_weighted** | 0.5723 | 0.5788 | 0.5858 | 0.5875 | 0.6195 |
| cut · **edges_cut** | 2094 | 2033 | 2047 | 2075 | 2765 |
| cut · **motifs_cut** | 2017 | 1857 | 1735 | 1787 | 2001 |
| cut · **motifs_internal** | 45762 | 45922 | 46044 | 45992 | 45778 |
| stability · **jaccard_vs_base** | 1 | 0.4295 | 0.3649 | 0.2903 | 0.0688 |

**Highlights**:  Q(A)=0.8117 → Q(λ=1.0)=0.8173 (ΔQ=+0.0056).
  Edges cut: A=2094 → λ=1.0: 2033.
  Motifs cut: A=2017 → λ=5.0: 1735.

## #3. `CA-GrQc-ncut-k200`

- File: [`data_CA-GrQc_ncut_k200.jsonp.js`](../../visualize/data_CA-GrQc_ncut_k200.jsonp.js)  · Export folder: [`CA-GrQc-ncut-k200/`](../../exports/) (tên file `CA-GrQc-ncut-k200` có thể chứa ký tự đặc biệt)
- Nodes: 4158, Edges: 13422, cc_global: 0.556878

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.7825 | 0.7928 | 0.7930 | 0.7907 | 0.7325 |
| quality · **cc_avg** | 0.5768 | 0.5887 | 0.6036 | 0.5977 | 0.7628 |
| quality · **cc_weighted** | 0.5787 | 0.5894 | 0.5970 | 0.5966 | 0.6291 |
| cut · **edges_cut** | 2608 | 2451 | 2447 | 2480 | 3236 |
| cut · **motifs_cut** | 4572 | 2461 | 2418 | 2412 | 2749 |
| cut · **motifs_internal** | 43207 | 45318 | 45361 | 45367 | 45030 |
| stability · **jaccard_vs_base** | 1 | 0.5282 | 0.4552 | 0.4370 | 0.0466 |

**Highlights**:  Q(A)=0.7825 → Q(λ=5.0)=0.7930 (ΔQ=+0.0104).
  Edges cut: A=2608 → λ=5.0: 2447.
  Motifs cut: A=4572 → λ=10.0: 2412.

## #4. `CA-GrQc-ncut-k300`

- File: [`data_CA-GrQc_ncut_k300.jsonp.js`](../../visualize/data_CA-GrQc_ncut_k300.jsonp.js)  · Export folder: [`CA-GrQc-ncut-k300/`](../../exports/) (tên file `CA-GrQc-ncut-k300` có thể chứa ký tự đặc biệt)
- Nodes: 4158, Edges: 13422, cc_global: 0.556878

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.7508 | 0.7639 | 0.7592 | 0.7623 | 0.7040 |
| quality · **cc_avg** | 0.5731 | 0.5903 | 0.5930 | 0.6030 | 0.7678 |
| quality · **cc_weighted** | 0.5801 | 0.5914 | 0.5953 | 0.5981 | 0.6275 |
| cut · **edges_cut** | 3096 | 2892 | 2968 | 2917 | 3649 |
| cut · **motifs_cut** | 6089 | 3961 | 4115 | 3964 | 3421 |
| cut · **motifs_internal** | 41690 | 43818 | 43664 | 43815 | 44358 |
| stability · **jaccard_vs_base** | 1 | 0.5375 | 0.5183 | 0.4954 | 0.0353 |

**Highlights**:  Q(A)=0.7508 → Q(λ=1.0)=0.7639 (ΔQ=+0.0131).
  Edges cut: A=3096 → λ=1.0: 2892.
  Motifs cut: A=6089 → λ=W_M: 3421.

## #5. `CA-GrQc-ncut-k400`

- File: [`data_CA-GrQc_ncut_k400.jsonp.js`](../../visualize/data_CA-GrQc_ncut_k400.jsonp.js)  · Export folder: [`CA-GrQc-ncut-k400/`](../../exports/) (tên file `CA-GrQc-ncut-k400` có thể chứa ký tự đặc biệt)
- Nodes: 4158, Edges: 13422, cc_global: 0.556878

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.7143 | 0.7351 | 0.7364 | 0.7354 | 0.6744 |
| quality · **cc_avg** | 0.5488 | 0.5736 | 0.5871 | 0.5984 | 0.7532 |
| quality · **cc_weighted** | 0.5769 | 0.5865 | 0.5953 | 0.5995 | 0.6167 |
| cut · **edges_cut** | 3609 | 3307 | 3289 | 3303 | 4058 |
| cut · **motifs_cut** | 7517 | 4511 | 4524 | 4559 | 3953 |
| cut · **motifs_internal** | 40262 | 43268 | 43255 | 43220 | 43826 |
| stability · **jaccard_vs_base** | 1 | 0.5733 | 0.5572 | 0.5378 | 0.0285 |

**Highlights**:  Q(A)=0.7143 → Q(λ=5.0)=0.7364 (ΔQ=+0.0221).
  Edges cut: A=3609 → λ=5.0: 3289.
  Motifs cut: A=7517 → λ=W_M: 3953.

## #6. `CA-GrQc-ncut-k500`

- File: [`data_CA-GrQc_ncut_k500.jsonp.js`](../../visualize/data_CA-GrQc_ncut_k500.jsonp.js)  · Export folder: [`CA-GrQc-ncut-k500/`](../../exports/) (tên file `CA-GrQc-ncut-k500` có thể chứa ký tự đặc biệt)
- Nodes: 4158, Edges: 13422, cc_global: 0.556878

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.6630 | 0.7097 | 0.7105 | 0.7105 | 0.6349 |
| quality · **cc_avg** | 0.5197 | 0.5622 | 0.5716 | 0.5886 | 0.7347 |
| quality · **cc_weighted** | 0.5564 | 0.5850 | 0.5902 | 0.5912 | 0.6104 |
| cut · **edges_cut** | 4329 | 3657 | 3646 | 3646 | 4615 |
| cut · **motifs_cut** | 11807 | 4886 | 4914 | 4896 | 8094 |
| cut · **motifs_internal** | 35972 | 42893 | 42865 | 42883 | 39685 |
| stability · **jaccard_vs_base** | 1 | 0.5315 | 0.5163 | 0.4974 | 0.0249 |

**Highlights**:  Q(A)=0.6630 → Q(λ=5.0)=0.7105 (ΔQ=+0.0476).
  Edges cut: A=4329 → λ=5.0: 3646.
  Motifs cut: A=11807 → λ=1.0: 4886.

---
*Generated by `experiments/main_result.py` — family=REAL, không filter Q(A), n=6.*
