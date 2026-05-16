# Result — Top 6 REAL

6 bộ test có ΔQ lớn nhất khi dùng mixed matrix, không filter Q(A).

## Ranking

| Rank | Test | Q(A) | Best λ | Q(best) | ΔQ |
|---:|------|-----:|:------:|--------:|---:|
| 1 | `cit-HepTh_adj-ncut-k50` | 0.5962 | `1.0` | 0.6227 | +0.0265 |
| 2 | `cit-HepTh_adj-ncut-k100` | 0.5731 | `1.0` | 0.6021 | +0.0290 |
| 3 | `cit-HepTh_adj-ncut-k200` | 0.5257 | `10.0` | 0.5709 | +0.0452 |
| 4 | `cit-HepTh_adj-ncut-k300` | 0.4916 | `5.0` | 0.5302 | +0.0386 |
| 5 | `cit-HepTh_adj-ncut-k400` | 0.4695 | `5.0` | 0.5044 | +0.0349 |
| 6 | `cit-HepTh_adj-ncut-k500` | 0.4508 | `1.0` | 0.4839 | +0.0330 |

## Bảng modularity Q × λ cho 5 test

| Test | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M | best λ | ΔQ |
|---|---:|---:|---:|---:|---:|---:|---:|
| #1 cit-HepTh_adj-ncut-k50 | 0.5962 | 0.6227 | 0.6180 | 0.6128 | 0.6080 | `1.0` | +0.0265 |
| #2 cit-HepTh_adj-ncut-k100 | 0.5731 | 0.6021 | 0.5968 | 0.5957 | 0.5786 | `1.0` | +0.0290 |
| #3 cit-HepTh_adj-ncut-k200 | 0.5257 | 0.5498 | 0.5472 | 0.5709 | 0.5405 | `10.0` | +0.0452 |
| #4 cit-HepTh_adj-ncut-k300 | 0.4916 | 0.5174 | 0.5302 | 0.5280 | 0.5145 | `5.0` | +0.0386 |
| #5 cit-HepTh_adj-ncut-k400 | 0.4695 | 0.4927 | 0.5044 | 0.4978 | 0.4842 | `5.0` | +0.0349 |
| #6 cit-HepTh_adj-ncut-k500 | 0.4508 | 0.4839 | 0.4746 | 0.4765 | 0.4527 | `1.0` | +0.0330 |

## #1. `cit-HepTh_adj-ncut-k50`

- File: [`data_cit-HepTh_adj_ncut_k50.jsonp.js`](../../visualize/data_cit-HepTh_adj_ncut_k50.jsonp.js)  · Export folder: [`cit-HepTh_adj-ncut-k50/`](../../exports/) (tên file `cit-HepTh_adj-ncut-k50` có thể chứa ký tự đặc biệt)
- Nodes: 27400, Edges: 352021, cc_global: 0.313915

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.5962 | 0.6227 | 0.6180 | 0.6128 | 0.6080 |
| quality · **cc_avg** | 0.3871 | 0.4135 | 0.4301 | 0.4312 | 0.5087 |
| quality · **cc_weighted** | 0.3867 | 0.4129 | 0.4225 | 0.4254 | 0.4477 |
| cut · **edges_cut** | 113872 | 105965 | 107418 | 110329 | 116979 |
| cut · **motifs_cut** | 504167 | 418238 | 426418 | 446158 | 461382 |
| cut · **motifs_internal** | 974531 | 1060460 | 1052280 | 1032540 | 1017316 |
| stability · **jaccard_vs_base** | 1 | 0.4351 | 0.3541 | 0.3626 | 0.2566 |

**Highlights**:  Q(A)=0.5962 → Q(λ=1.0)=0.6227 (ΔQ=+0.0265).
  Edges cut: A=113872 → λ=1.0: 105965.
  Motifs cut: A=504167 → λ=1.0: 418238.

## #2. `cit-HepTh_adj-ncut-k100`

- File: [`data_cit-HepTh_adj_ncut_k100.jsonp.js`](../../visualize/data_cit-HepTh_adj_ncut_k100.jsonp.js)  · Export folder: [`cit-HepTh_adj-ncut-k100/`](../../exports/) (tên file `cit-HepTh_adj-ncut-k100` có thể chứa ký tự đặc biệt)
- Nodes: 27400, Edges: 352021, cc_global: 0.313915

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.5731 | 0.6021 | 0.5968 | 0.5957 | 0.5786 |
| quality · **cc_avg** | 0.4005 | 0.4336 | 0.4436 | 0.4428 | 0.5241 |
| quality · **cc_weighted** | 0.4024 | 0.4319 | 0.4422 | 0.4441 | 0.4665 |
| cut · **edges_cut** | 134516 | 125308 | 127428 | 125672 | 135996 |
| cut · **motifs_cut** | 607004 | 504552 | 511036 | 509227 | 554622 |
| cut · **motifs_internal** | 871694 | 974146 | 967662 | 969471 | 924076 |
| stability · **jaccard_vs_base** | 1 | 0.3884 | 0.3588 | 0.3551 | 0.2290 |

**Highlights**:  Q(A)=0.5731 → Q(λ=1.0)=0.6021 (ΔQ=+0.0290).
  Edges cut: A=134516 → λ=1.0: 125308.
  Motifs cut: A=607004 → λ=1.0: 504552.

## #3. `cit-HepTh_adj-ncut-k200`

- File: [`data_cit-HepTh_adj_ncut_k200.jsonp.js`](../../visualize/data_cit-HepTh_adj_ncut_k200.jsonp.js)  · Export folder: [`cit-HepTh_adj-ncut-k200/`](../../exports/) (tên file `cit-HepTh_adj-ncut-k200` có thể chứa ký tự đặc biệt)
- Nodes: 27400, Edges: 352021, cc_global: 0.313915

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.5257 | 0.5498 | 0.5472 | 0.5709 | 0.5405 |
| quality · **cc_avg** | 0.4136 | 0.4461 | 0.4564 | 0.4545 | 0.5574 |
| quality · **cc_weighted** | 0.4192 | 0.4509 | 0.4616 | 0.4599 | 0.4862 |
| cut · **edges_cut** | 159875 | 150666 | 151547 | 140849 | 154375 |
| cut · **motifs_cut** | 734954 | 645607 | 655057 | 580664 | 654561 |
| cut · **motifs_internal** | 743744 | 833091 | 823641 | 898034 | 824137 |
| stability · **jaccard_vs_base** | 1 | 0.4004 | 0.3638 | 0.3667 | 0.1940 |

**Highlights**:  Q(A)=0.5257 → Q(λ=10.0)=0.5709 (ΔQ=+0.0452).
  Edges cut: A=159875 → λ=10.0: 140849.
  Motifs cut: A=734954 → λ=10.0: 580664.

## #4. `cit-HepTh_adj-ncut-k300`

- File: [`data_cit-HepTh_adj_ncut_k300.jsonp.js`](../../visualize/data_cit-HepTh_adj_ncut_k300.jsonp.js)  · Export folder: [`cit-HepTh_adj-ncut-k300/`](../../exports/) (tên file `cit-HepTh_adj-ncut-k300` có thể chứa ký tự đặc biệt)
- Nodes: 27400, Edges: 352021, cc_global: 0.313915

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.4916 | 0.5174 | 0.5302 | 0.5280 | 0.5145 |
| quality · **cc_avg** | 0.4262 | 0.4498 | 0.4603 | 0.4638 | 0.5807 |
| quality · **cc_weighted** | 0.4366 | 0.4624 | 0.4727 | 0.4745 | 0.4995 |
| cut · **edges_cut** | 173867 | 164343 | 159226 | 159944 | 165525 |
| cut · **motifs_cut** | 790894 | 721879 | 682132 | 689963 | 723332 |
| cut · **motifs_internal** | 687804 | 756819 | 796566 | 788735 | 755366 |
| stability · **jaccard_vs_base** | 1 | 0.4453 | 0.3923 | 0.4064 | 0.1724 |

**Highlights**:  Q(A)=0.4916 → Q(λ=5.0)=0.5302 (ΔQ=+0.0386).
  Edges cut: A=173867 → λ=5.0: 159226.
  Motifs cut: A=790894 → λ=5.0: 682132.

## #5. `cit-HepTh_adj-ncut-k400`

- File: [`data_cit-HepTh_adj_ncut_k400.jsonp.js`](../../visualize/data_cit-HepTh_adj_ncut_k400.jsonp.js)  · Export folder: [`cit-HepTh_adj-ncut-k400/`](../../exports/) (tên file `cit-HepTh_adj-ncut-k400` có thể chứa ký tự đặc biệt)
- Nodes: 27400, Edges: 352021, cc_global: 0.313915

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.4695 | 0.4927 | 0.5044 | 0.4978 | 0.4842 |
| quality · **cc_avg** | 0.4323 | 0.4575 | 0.4699 | 0.4712 | 0.5947 |
| quality · **cc_weighted** | 0.4451 | 0.4711 | 0.4825 | 0.4836 | 0.5120 |
| cut · **edges_cut** | 182894 | 174402 | 169828 | 172433 | 177712 |
| cut · **motifs_cut** | 850826 | 781883 | 747100 | 769133 | 782431 |
| cut · **motifs_internal** | 627872 | 696815 | 731598 | 709565 | 696267 |
| stability · **jaccard_vs_base** | 1 | 0.4133 | 0.3766 | 0.3731 | 0.1412 |

**Highlights**:  Q(A)=0.4695 → Q(λ=5.0)=0.5044 (ΔQ=+0.0349).
  Edges cut: A=182894 → λ=5.0: 169828.
  Motifs cut: A=850826 → λ=5.0: 747100.

## #6. `cit-HepTh_adj-ncut-k500`

- File: [`data_cit-HepTh_adj_ncut_k500.jsonp.js`](../../visualize/data_cit-HepTh_adj_ncut_k500.jsonp.js)  · Export folder: [`cit-HepTh_adj-ncut-k500/`](../../exports/) (tên file `cit-HepTh_adj-ncut-k500` có thể chứa ký tự đặc biệt)
- Nodes: 27400, Edges: 352021, cc_global: 0.313915

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.4508 | 0.4839 | 0.4746 | 0.4765 | 0.4527 |
| quality · **cc_avg** | 0.4286 | 0.4609 | 0.4773 | 0.4728 | 0.6074 |
| quality · **cc_weighted** | 0.4503 | 0.4796 | 0.4910 | 0.4923 | 0.5253 |
| cut · **edges_cut** | 190076 | 177788 | 181559 | 180708 | 189706 |
| cut · **motifs_cut** | 884956 | 794828 | 823438 | 819089 | 863428 |
| cut · **motifs_internal** | 593742 | 683870 | 655260 | 659609 | 615270 |
| stability · **jaccard_vs_base** | 1 | 0.4017 | 0.3979 | 0.3694 | 0.1220 |

**Highlights**:  Q(A)=0.4508 → Q(λ=1.0)=0.4839 (ΔQ=+0.0330).
  Edges cut: A=190076 → λ=1.0: 177788.
  Motifs cut: A=884956 → λ=1.0: 794828.

---
*Generated by `experiments/main_result.py` — family=REAL, không filter Q(A), n=6.*
