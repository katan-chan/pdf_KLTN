# Result — Top 4 REAL

4 bộ test có ΔQ lớn nhất khi dùng mixed matrix, không filter Q(A).

## Ranking

| Rank | Test | Q(A) | Best λ | Q(best) | ΔQ |
|---:|------|-----:|:------:|--------:|---:|
| 1 | `musae_facebook_edges-ncut-k200` | 0.7515 | `1.0` | 0.7542 | +0.0027 |
| 2 | `musae_facebook_edges-ncut-k300` | 0.7320 | `5.0` | 0.7409 | +0.0089 |
| 3 | `musae_facebook_edges-ncut-k400` | 0.7134 | `10.0` | 0.7265 | +0.0131 |
| 4 | `musae_facebook_edges-ncut-k500` | 0.6949 | `10.0` | 0.7151 | +0.0202 |

## Bảng modularity Q × λ cho 5 test

| Test | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M | best λ | ΔQ |
|---|---:|---:|---:|---:|---:|---:|---:|
| #1 musae_facebook_edges-ncut-k200 | 0.7515 | 0.7542 | 0.7510 | 0.7538 | 0.7200 | `1.0` | +0.0027 |
| #2 musae_facebook_edges-ncut-k300 | 0.7320 | 0.7324 | 0.7409 | 0.7376 | 0.7069 | `5.0` | +0.0089 |
| #3 musae_facebook_edges-ncut-k400 | 0.7134 | 0.7213 | 0.7255 | 0.7265 | 0.6798 | `10.0` | +0.0131 |
| #4 musae_facebook_edges-ncut-k500 | 0.6949 | 0.7015 | 0.7132 | 0.7151 | 0.6597 | `10.0` | +0.0202 |

## #1. `musae_facebook_edges-ncut-k200`

- File: [`data_musae_facebook_edges_ncut_k200.jsonp.js`](../../visualize/data_musae_facebook_edges_ncut_k200.jsonp.js)  · Export folder: [`musae_facebook_edges-ncut-k200/`](../../exports/) (tên file `musae_facebook_edges-ncut-k200` có thể chứa ký tự đặc biệt)
- Nodes: 22470, Edges: 170823, cc_global: 0.359738

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.7515 | 0.7542 | 0.7510 | 0.7538 | 0.7200 |
| quality · **cc_avg** | 0.4209 | 0.4339 | 0.4561 | 0.4508 | 0.6439 |
| quality · **cc_weighted** | 0.4091 | 0.4291 | 0.4395 | 0.4425 | 0.4737 |
| cut · **edges_cut** | 36998 | 36531 | 37403 | 36442 | 42534 |
| cut · **motifs_cut** | 116388 | 92849 | 98564 | 92244 | 103655 |
| cut · **motifs_internal** | 678565 | 702104 | 696389 | 702709 | 691298 |
| stability · **jaccard_vs_base** | 1 | 0.4490 | 0.3914 | 0.3764 | 0.0700 |

**Highlights**:  Q(A)=0.7515 → Q(λ=1.0)=0.7542 (ΔQ=+0.0027).
  Edges cut: A=36998 → λ=10.0: 36442.
  Motifs cut: A=116388 → λ=10.0: 92244.

## #2. `musae_facebook_edges-ncut-k300`

- File: [`data_musae_facebook_edges_ncut_k300.jsonp.js`](../../visualize/data_musae_facebook_edges_ncut_k300.jsonp.js)  · Export folder: [`musae_facebook_edges-ncut-k300/`](../../exports/) (tên file `musae_facebook_edges-ncut-k300` có thể chứa ký tự đặc biệt)
- Nodes: 22470, Edges: 170823, cc_global: 0.359738

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.7320 | 0.7324 | 0.7409 | 0.7376 | 0.7069 |
| quality · **cc_avg** | 0.4206 | 0.4277 | 0.4442 | 0.4487 | 0.6619 |
| quality · **cc_weighted** | 0.4134 | 0.4319 | 0.4442 | 0.4479 | 0.4780 |
| cut · **edges_cut** | 41315 | 41314 | 39401 | 40022 | 45278 |
| cut · **motifs_cut** | 131713 | 116968 | 106482 | 108735 | 117282 |
| cut · **motifs_internal** | 663240 | 677985 | 688471 | 686218 | 677671 |
| stability · **jaccard_vs_base** | 1 | 0.5205 | 0.4759 | 0.4652 | 0.0578 |

**Highlights**:  Q(A)=0.7320 → Q(λ=5.0)=0.7409 (ΔQ=+0.0089).
  Edges cut: A=41315 → λ=5.0: 39401.
  Motifs cut: A=131713 → λ=5.0: 106482.

## #3. `musae_facebook_edges-ncut-k400`

- File: [`data_musae_facebook_edges_ncut_k400.jsonp.js`](../../visualize/data_musae_facebook_edges_ncut_k400.jsonp.js)  · Export folder: [`musae_facebook_edges-ncut-k400/`](../../exports/) (tên file `musae_facebook_edges-ncut-k400` có thể chứa ký tự đặc biệt)
- Nodes: 22470, Edges: 170823, cc_global: 0.359738

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.7134 | 0.7213 | 0.7255 | 0.7265 | 0.6798 |
| quality · **cc_avg** | 0.4097 | 0.4323 | 0.4399 | 0.4387 | 0.6673 |
| quality · **cc_weighted** | 0.4190 | 0.4391 | 0.4468 | 0.4490 | 0.4875 |
| cut · **edges_cut** | 44850 | 43528 | 42535 | 42246 | 50541 |
| cut · **motifs_cut** | 148048 | 130669 | 126306 | 121891 | 149964 |
| cut · **motifs_internal** | 646905 | 664284 | 668647 | 673062 | 644989 |
| stability · **jaccard_vs_base** | 1 | 0.5455 | 0.4824 | 0.5073 | 0.0498 |

**Highlights**:  Q(A)=0.7134 → Q(λ=10.0)=0.7265 (ΔQ=+0.0131).
  Edges cut: A=44850 → λ=10.0: 42246.
  Motifs cut: A=148048 → λ=10.0: 121891.

## #4. `musae_facebook_edges-ncut-k500`

- File: [`data_musae_facebook_edges_ncut_k500.jsonp.js`](../../visualize/data_musae_facebook_edges_ncut_k500.jsonp.js)  · Export folder: [`musae_facebook_edges-ncut-k500/`](../../exports/) (tên file `musae_facebook_edges-ncut-k500` có thể chứa ký tự đặc biệt)
- Nodes: 22470, Edges: 170823, cc_global: 0.359738

| metric | λ=0.0 | λ=1.0 | λ=5.0 | λ=10.0 | λ=W_M |
|---|---:|---:|---:|---:|---:|
| quality · **modularity** | 0.6949 | 0.7015 | 0.7132 | 0.7151 | 0.6597 |
| quality · **cc_avg** | 0.4066 | 0.4255 | 0.4356 | 0.4413 | 0.6748 |
| quality · **cc_weighted** | 0.4251 | 0.4427 | 0.4523 | 0.4543 | 0.4934 |
| cut · **edges_cut** | 48273 | 47419 | 44950 | 44629 | 54384 |
| cut · **motifs_cut** | 153171 | 164835 | 134970 | 133235 | 178961 |
| cut · **motifs_internal** | 641782 | 630118 | 659983 | 661718 | 615992 |
| stability · **jaccard_vs_base** | 1 | 0.5953 | 0.5813 | 0.5583 | 0.0399 |

**Highlights**:  Q(A)=0.6949 → Q(λ=10.0)=0.7151 (ΔQ=+0.0202).
  Edges cut: A=48273 → λ=10.0: 44629.
  Motifs cut: A=153171 → λ=10.0: 133235.

---
*Generated by `experiments/main_result.py` — family=REAL, không filter Q(A), n=4.*
