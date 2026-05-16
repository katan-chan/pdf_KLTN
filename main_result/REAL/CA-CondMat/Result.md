# Result — Top 6 REAL

6 bộ test có ΔQ lớn nhất khi dùng mixed matrix, không filter Q(A).

## Ranking

| Rank | Test | Q(A) | Best λ | Q(best) | ΔQ |
|---:|------|-----:|:------:|--------:|---:|
| 1 | `CA-CondMat-ncut-k50` | 0.6254 | `10.0` | 0.6570 | +0.0316 |
| 2 | `CA-CondMat-ncut-k100` | 0.6588 | `10.0` | 0.6765 | +0.0177 |
| 3 | `CA-CondMat-ncut-k200` | 0.6553 | `10.0` | 0.6730 | +0.0178 |
| 4 | `CA-CondMat-ncut-k300` | 0.6538 | `5.0` | 0.6671 | +0.0134 |
| 5 | `CA-CondMat-ncut-k400` | 0.6452 | `10.0` | 0.6586 | +0.0134 |
| 6 | `CA-CondMat-ncut-k500` | 0.6383 | `10.0` | 0.6537 | +0.0154 |

## Bảng modularity Q × λ cho 5 test

| Test | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M | best λ | ΔQ |
|---|---:|---:|---:|---:|---:|---:|---:|
| #1 CA-CondMat-ncut-k50 | 0.6254 | 0.6539 | 0.6568 | 0.6570 | 0.6416 | `10.0` | +0.0316 |
| #2 CA-CondMat-ncut-k100 | 0.6588 | 0.6756 | 0.6752 | 0.6765 | 0.6587 | `10.0` | +0.0177 |
| #3 CA-CondMat-ncut-k200 | 0.6553 | 0.6694 | 0.6725 | 0.6730 | 0.6569 | `10.0` | +0.0178 |
| #4 CA-CondMat-ncut-k300 | 0.6538 | 0.6660 | 0.6671 | 0.6638 | 0.6479 | `5.0` | +0.0134 |
| #5 CA-CondMat-ncut-k400 | 0.6452 | 0.6585 | 0.6555 | 0.6586 | 0.6426 | `10.0` | +0.0134 |
| #6 CA-CondMat-ncut-k500 | 0.6383 | 0.6528 | 0.6524 | 0.6537 | 0.6320 | `10.0` | +0.0154 |

## #1. `CA-CondMat-ncut-k50`

- File: [`data_CA-CondMat_ncut_k50.jsonp.js`](../../visualize/data_CA-CondMat_ncut_k50.jsonp.js)  · Export folder: [`CA-CondMat-ncut-k50/`](../../exports/) (tên file `CA-CondMat-ncut-k50` có thể chứa ký tự đặc biệt)
- Nodes: 21363, Edges: 91286, cc_global: 0.641732

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.6254 | 0.6539 | 0.6568 | 0.6570 | 0.6416 |
| quality · **cc_avg** | 0.6538 | 0.6631 | 0.6653 | 0.6691 | 0.7370 |
| quality · **cc_weighted** | 0.6435 | 0.6576 | 0.6615 | 0.6640 | 0.6769 |
| cut · **edges_cut** | 29749 | 27433 | 27676 | 28085 | 29274 |
| cut · **motifs_cut** | 64417 | 52903 | 54022 | 55111 | 53802 |
| cut · **motifs_internal** | 106634 | 118148 | 117029 | 115940 | 117249 |
| stability · **jaccard_vs_base** | 1 | 0.1335 | 0.1082 | 0.1019 | 0.0788 |

**Highlights**:  Q(A)=0.6254 → Q(λ=10.0)=0.6570 (ΔQ=+0.0316).
  Edges cut: A=29749 → λ=1.0: 27433.
  Motifs cut: A=64417 → λ=1.0: 52903.

## #2. `CA-CondMat-ncut-k100`

- File: [`data_CA-CondMat_ncut_k100.jsonp.js`](../../visualize/data_CA-CondMat_ncut_k100.jsonp.js)  · Export folder: [`CA-CondMat-ncut-k100/`](../../exports/) (tên file `CA-CondMat-ncut-k100` có thể chứa ký tự đặc biệt)
- Nodes: 21363, Edges: 91286, cc_global: 0.641732

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.6588 | 0.6756 | 0.6752 | 0.6765 | 0.6587 |
| quality · **cc_avg** | 0.6641 | 0.6692 | 0.6778 | 0.6747 | 0.7548 |
| quality · **cc_weighted** | 0.6522 | 0.6653 | 0.6724 | 0.6714 | 0.6875 |
| cut · **edges_cut** | 29113 | 27498 | 27690 | 27342 | 29366 |
| cut · **motifs_cut** | 61760 | 53807 | 54225 | 52914 | 54869 |
| cut · **motifs_internal** | 109291 | 117244 | 116826 | 118137 | 116182 |
| stability · **jaccard_vs_base** | 1 | 0.1948 | 0.1744 | 0.1834 | 0.0966 |

**Highlights**:  Q(A)=0.6588 → Q(λ=10.0)=0.6765 (ΔQ=+0.0177).
  Edges cut: A=29113 → λ=10.0: 27342.
  Motifs cut: A=61760 → λ=10.0: 52914.

## #3. `CA-CondMat-ncut-k200`

- File: [`data_CA-CondMat_ncut_k200.jsonp.js`](../../visualize/data_CA-CondMat_ncut_k200.jsonp.js)  · Export folder: [`CA-CondMat-ncut-k200/`](../../exports/) (tên file `CA-CondMat-ncut-k200` có thể chứa ký tự đặc biệt)
- Nodes: 21363, Edges: 91286, cc_global: 0.641732

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.6553 | 0.6694 | 0.6725 | 0.6730 | 0.6569 |
| quality · **cc_avg** | 0.6722 | 0.6770 | 0.6818 | 0.6827 | 0.7569 |
| quality · **cc_weighted** | 0.6601 | 0.6721 | 0.6751 | 0.6771 | 0.6921 |
| cut · **edges_cut** | 30500 | 29186 | 28862 | 28722 | 30150 |
| cut · **motifs_cut** | 67815 | 59639 | 58693 | 58465 | 57627 |
| cut · **motifs_internal** | 103236 | 111412 | 112358 | 112586 | 113424 |
| stability · **jaccard_vs_base** | 1 | 0.1919 | 0.1808 | 0.1543 | 0.0909 |

**Highlights**:  Q(A)=0.6553 → Q(λ=10.0)=0.6730 (ΔQ=+0.0178).
  Edges cut: A=30500 → λ=10.0: 28722.
  Motifs cut: A=67815 → λ=W_M: 57627.

## #4. `CA-CondMat-ncut-k300`

- File: [`data_CA-CondMat_ncut_k300.jsonp.js`](../../visualize/data_CA-CondMat_ncut_k300.jsonp.js)  · Export folder: [`CA-CondMat-ncut-k300/`](../../exports/) (tên file `CA-CondMat-ncut-k300` có thể chứa ký tự đặc biệt)
- Nodes: 21363, Edges: 91286, cc_global: 0.641732

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.6538 | 0.6660 | 0.6671 | 0.6638 | 0.6479 |
| quality · **cc_avg** | 0.6756 | 0.6794 | 0.6799 | 0.6871 | 0.7595 |
| quality · **cc_weighted** | 0.6667 | 0.6747 | 0.6773 | 0.6804 | 0.6954 |
| cut · **edges_cut** | 30854 | 29764 | 29542 | 29971 | 31450 |
| cut · **motifs_cut** | 68311 | 61563 | 60368 | 62303 | 61521 |
| cut · **motifs_internal** | 102740 | 109488 | 110683 | 108748 | 109530 |
| stability · **jaccard_vs_base** | 1 | 0.2438 | 0.2231 | 0.2035 | 0.1006 |

**Highlights**:  Q(A)=0.6538 → Q(λ=5.0)=0.6671 (ΔQ=+0.0134).
  Edges cut: A=30854 → λ=5.0: 29542.
  Motifs cut: A=68311 → λ=5.0: 60368.

## #5. `CA-CondMat-ncut-k400`

- File: [`data_CA-CondMat_ncut_k400.jsonp.js`](../../visualize/data_CA-CondMat_ncut_k400.jsonp.js)  · Export folder: [`CA-CondMat-ncut-k400/`](../../exports/) (tên file `CA-CondMat-ncut-k400` có thể chứa ký tự đặc biệt)
- Nodes: 21363, Edges: 91286, cc_global: 0.641732

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.6452 | 0.6585 | 0.6555 | 0.6586 | 0.6426 |
| quality · **cc_avg** | 0.6759 | 0.6817 | 0.6834 | 0.6823 | 0.7664 |
| quality · **cc_weighted** | 0.6714 | 0.6761 | 0.6805 | 0.6807 | 0.6996 |
| cut · **edges_cut** | 31834 | 30646 | 30911 | 30640 | 32111 |
| cut · **motifs_cut** | 71105 | 63961 | 65116 | 63967 | 63244 |
| cut · **motifs_internal** | 99946 | 107090 | 105935 | 107084 | 107807 |
| stability · **jaccard_vs_base** | 1 | 0.2517 | 0.2394 | 0.2347 | 0.1013 |

**Highlights**:  Q(A)=0.6452 → Q(λ=10.0)=0.6586 (ΔQ=+0.0134).
  Edges cut: A=31834 → λ=10.0: 30640.
  Motifs cut: A=71105 → λ=W_M: 63244.

## #6. `CA-CondMat-ncut-k500`

- File: [`data_CA-CondMat_ncut_k500.jsonp.js`](../../visualize/data_CA-CondMat_ncut_k500.jsonp.js)  · Export folder: [`CA-CondMat-ncut-k500/`](../../exports/) (tên file `CA-CondMat-ncut-k500` có thể chứa ký tự đặc biệt)
- Nodes: 21363, Edges: 91286, cc_global: 0.641732

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.6383 | 0.6528 | 0.6524 | 0.6537 | 0.6320 |
| quality · **cc_avg** | 0.6797 | 0.6841 | 0.6810 | 0.6880 | 0.7684 |
| quality · **cc_weighted** | 0.6736 | 0.6799 | 0.6825 | 0.6841 | 0.7012 |
| cut · **edges_cut** | 32648 | 31286 | 31298 | 31172 | 33188 |
| cut · **motifs_cut** | 73707 | 65858 | 66692 | 65458 | 67060 |
| cut · **motifs_internal** | 97344 | 105193 | 104359 | 105593 | 103991 |
| stability · **jaccard_vs_base** | 1 | 0.3196 | 0.2679 | 0.2594 | 0.0895 |

**Highlights**:  Q(A)=0.6383 → Q(λ=10.0)=0.6537 (ΔQ=+0.0154).
  Edges cut: A=32648 → λ=10.0: 31172.
  Motifs cut: A=73707 → λ=10.0: 65458.

---
*Generated by `experiments/main_result.py` — family=REAL, không filter Q(A), n=6.*
