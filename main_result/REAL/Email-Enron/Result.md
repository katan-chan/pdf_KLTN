# Result — Top 5 REAL

5 bộ test có ΔQ lớn nhất khi dùng mixed matrix, không filter Q(A).

## Ranking

| Rank | Test | Q(A) | Best λ | Q(best) | ΔQ |
|---:|------|-----:|:------:|--------:|---:|
| 1 | `Email-Enron-ncut-k100` | 0.5046 | `5.0` | 0.5206 | +0.0160 |
| 2 | `Email-Enron-ncut-k200` | 0.4675 | `10.0` | 0.5111 | +0.0436 |
| 3 | `Email-Enron-ncut-k300` | 0.4264 | `5.0` | 0.4904 | +0.0640 |
| 4 | `Email-Enron-ncut-k400` | 0.4052 | `1.0` | 0.4528 | +0.0476 |
| 5 | `Email-Enron-ncut-k500` | 0.3880 | `10.0` | 0.4268 | +0.0388 |

## Bảng modularity Q × λ cho 5 test

| Test | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M | best λ | ΔQ |
|---|---:|---:|---:|---:|---:|---:|---:|
| #1 Email-Enron-ncut-k100 | 0.5046 | 0.5103 | 0.5206 | 0.5204 | 0.4777 | `5.0` | +0.0160 |
| #2 Email-Enron-ncut-k200 | 0.4675 | 0.5049 | 0.5110 | 0.5111 | 0.4378 | `10.0` | +0.0436 |
| #3 Email-Enron-ncut-k300 | 0.4264 | 0.4743 | 0.4904 | 0.4901 | 0.4051 | `5.0` | +0.0640 |
| #4 Email-Enron-ncut-k400 | 0.4052 | 0.4528 | 0.4526 | 0.4474 | 0.3739 | `1.0` | +0.0476 |
| #5 Email-Enron-ncut-k500 | 0.3880 | 0.4184 | 0.4188 | 0.4268 | 0.3595 | `10.0` | +0.0388 |

## #1. `Email-Enron-ncut-k100`

- File: [`data_Email-Enron_ncut_k100.jsonp.js`](../../visualize/data_Email-Enron_ncut_k100.jsonp.js)  · Export folder: [`Email-Enron-ncut-k100/`](../../exports/) (tên file `Email-Enron-ncut-k100` có thể chứa ký tự đặc biệt)
- Nodes: 33696, Edges: 180811, cc_global: 0.50919

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.5046 | 0.5103 | 0.5206 | 0.5204 | 0.4777 |
| quality · **cc_avg** | 0.5067 | 0.5502 | 0.5428 | 0.5432 | 0.7592 |
| quality · **cc_weighted** | 0.4844 | 0.4938 | 0.5002 | 0.5040 | 0.4959 |
| cut · **edges_cut** | 70540 | 51537 | 51925 | 50321 | 66232 |
| cut · **motifs_cut** | 426094 | 282535 | 282283 | 269401 | 317825 |
| cut · **motifs_internal** | 299217 | 442776 | 443028 | 455910 | 407486 |
| stability · **jaccard_vs_base** | 1 | 0.2883 | 0.3078 | 0.2960 | 0.1219 |

**Highlights**:  Q(A)=0.5046 → Q(λ=5.0)=0.5206 (ΔQ=+0.0160).
  Edges cut: A=70540 → λ=10.0: 50321.
  Motifs cut: A=426094 → λ=10.0: 269401.

## #2. `Email-Enron-ncut-k200`

- File: [`data_Email-Enron_ncut_k200.jsonp.js`](../../visualize/data_Email-Enron_ncut_k200.jsonp.js)  · Export folder: [`Email-Enron-ncut-k200/`](../../exports/) (tên file `Email-Enron-ncut-k200` có thể chứa ký tự đặc biệt)
- Nodes: 33696, Edges: 180811, cc_global: 0.50919

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.4675 | 0.5049 | 0.5110 | 0.5111 | 0.4378 |
| quality · **cc_avg** | 0.5079 | 0.5582 | 0.5596 | 0.5612 | 0.7574 |
| quality · **cc_weighted** | 0.4713 | 0.4890 | 0.4904 | 0.4892 | 0.4894 |
| cut · **edges_cut** | 87223 | 70557 | 68796 | 69573 | 92554 |
| cut · **motifs_cut** | 526208 | 406609 | 400928 | 399660 | 496007 |
| cut · **motifs_internal** | 199103 | 318702 | 324383 | 325651 | 229304 |
| stability · **jaccard_vs_base** | 1 | 0.2348 | 0.2223 | 0.2037 | 0.0543 |

**Highlights**:  Q(A)=0.4675 → Q(λ=10.0)=0.5111 (ΔQ=+0.0436).
  Edges cut: A=87223 → λ=5.0: 68796.
  Motifs cut: A=526208 → λ=10.0: 399660.

## #3. `Email-Enron-ncut-k300`

- File: [`data_Email-Enron_ncut_k300.jsonp.js`](../../visualize/data_Email-Enron_ncut_k300.jsonp.js)  · Export folder: [`Email-Enron-ncut-k300/`](../../exports/) (tên file `Email-Enron-ncut-k300` có thể chứa ký tự đặc biệt)
- Nodes: 33696, Edges: 180811, cc_global: 0.50919

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.4264 | 0.4743 | 0.4904 | 0.4901 | 0.4051 |
| quality · **cc_avg** | 0.5194 | 0.5849 | 0.5925 | 0.5969 | 0.7479 |
| quality · **cc_weighted** | 0.4561 | 0.4756 | 0.4838 | 0.4843 | 0.4756 |
| cut · **edges_cut** | 99016 | 86746 | 80918 | 81898 | 102117 |
| cut · **motifs_cut** | 577097 | 504949 | 469953 | 477739 | 542170 |
| cut · **motifs_internal** | 148214 | 220362 | 255358 | 247572 | 183141 |
| stability · **jaccard_vs_base** | 1 | 0.2767 | 0.2169 | 0.2257 | 0.0406 |

**Highlights**:  Q(A)=0.4264 → Q(λ=5.0)=0.4904 (ΔQ=+0.0640).
  Edges cut: A=99016 → λ=5.0: 80918.
  Motifs cut: A=577097 → λ=5.0: 469953.

## #4. `Email-Enron-ncut-k400`

- File: [`data_Email-Enron_ncut_k400.jsonp.js`](../../visualize/data_Email-Enron_ncut_k400.jsonp.js)  · Export folder: [`Email-Enron-ncut-k400/`](../../exports/) (tên file `Email-Enron-ncut-k400` có thể chứa ký tự đặc biệt)
- Nodes: 33696, Edges: 180811, cc_global: 0.50919

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.4052 | 0.4528 | 0.4526 | 0.4474 | 0.3739 |
| quality · **cc_avg** | 0.5351 | 0.5856 | 0.5963 | 0.5964 | 0.7404 |
| quality · **cc_weighted** | 0.4511 | 0.4701 | 0.4700 | 0.4654 | 0.4645 |
| cut · **edges_cut** | 104452 | 93054 | 92905 | 94543 | 109951 |
| cut · **motifs_cut** | 600160 | 542622 | 536666 | 544996 | 580366 |
| cut · **motifs_internal** | 125151 | 182689 | 188645 | 180315 | 144945 |
| stability · **jaccard_vs_base** | 1 | 0.2944 | 0.2719 | 0.2876 | 0.0307 |

**Highlights**:  Q(A)=0.4052 → Q(λ=1.0)=0.4528 (ΔQ=+0.0476).
  Edges cut: A=104452 → λ=5.0: 92905.
  Motifs cut: A=600160 → λ=5.0: 536666.

## #5. `Email-Enron-ncut-k500`

- File: [`data_Email-Enron_ncut_k500.jsonp.js`](../../visualize/data_Email-Enron_ncut_k500.jsonp.js)  · Export folder: [`Email-Enron-ncut-k500/`](../../exports/) (tên file `Email-Enron-ncut-k500` có thể chứa ký tự đặc biệt)
- Nodes: 33696, Edges: 180811, cc_global: 0.50919

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.3880 | 0.4184 | 0.4188 | 0.4268 | 0.3595 |
| quality · **cc_avg** | 0.5383 | 0.5996 | 0.6046 | 0.6064 | 0.7424 |
| quality · **cc_weighted** | 0.4447 | 0.4519 | 0.4578 | 0.4631 | 0.4644 |
| cut · **edges_cut** | 108420 | 101093 | 101462 | 99754 | 113167 |
| cut · **motifs_cut** | 616455 | 567629 | 577268 | 574048 | 600930 |
| cut · **motifs_internal** | 108856 | 157682 | 148043 | 151263 | 124381 |
| stability · **jaccard_vs_base** | 1 | 0.3307 | 0.3325 | 0.3210 | 0.0284 |

**Highlights**:  Q(A)=0.3880 → Q(λ=10.0)=0.4268 (ΔQ=+0.0388).
  Edges cut: A=108420 → λ=10.0: 99754.
  Motifs cut: A=616455 → λ=1.0: 567629.

---
*Generated by `experiments/main_result.py` — family=REAL, không filter Q(A), n=5.*
