# REAL — Real-world datasets

**11 đồ thị thật**, mỗi đồ thị chạy NCut với nhiều k. Tổng 62 cấu hình (graph, k) sau filter.

## Sub-folders (1 folder/đồ thị)

- [`CA-AstroPh/`](./CA-AstroPh/) — n=17903, m=196972, k∈{50,100,200,300,400,500}, best ΔQ=+0.0421 tại k=50
- [`CA-CondMat/`](./CA-CondMat/) — n=21363, m=91286, k∈{50,100,200,300,400,500}, best ΔQ=+0.0316 tại k=50
- [`CA-GrQc/`](./CA-GrQc/) — n=4158, m=13422, k∈{50,100,200,300,400,500}, best ΔQ=+0.0476 tại k=500
- [`CA-HepTh/`](./CA-HepTh/) — n=8638, m=24806, k∈{50,100,200,300,400,500}, best ΔQ=+0.0250 tại k=50
- [`Email-Enron/`](./Email-Enron/) — n=33696, m=180811, k∈{100,200,300,400,500}, best ΔQ=+0.0640 tại k=300
- [`cit-HepTh_adj/`](./cit-HepTh_adj/) — n=27400, m=352021, k∈{50,100,200,300,400,500}, best ΔQ=+0.0452 tại k=200
- [`facebook_combined/`](./facebook_combined/) — n=4039, m=88234, k∈{50,100,200,400,500}, best ΔQ=+0.0519 tại k=500
- [`lastfm_asia_edges/`](./lastfm_asia_edges/) — n=7624, m=27806, k∈{50,100,200,300,400,500}, best ΔQ=+0.0815 tại k=500
- [`musae_DE_edges/`](./musae_DE_edges/) — n=9498, m=153138, k∈{50,100,200,300,400,500}, best ΔQ=+0.1156 tại k=50
- [`musae_ES_edges/`](./musae_ES_edges/) — n=4648, m=59382, k∈{50,100,200,300,400,500}, best ΔQ=+0.0902 tại k=50
- [`musae_facebook_edges/`](./musae_facebook_edges/) — n=22470, m=170823, k∈{200,300,400,500}, best ΔQ=+0.0202 tại k=500

## Global ranking (top 10 across all real graphs)

| # | Test | Q(A) | Best λ | Q(best) | ΔQ |
|---|------|-----:|:------:|--------:|---:|
| 1 | `musae_DE_edges-ncut-k50` | 0.0469 | `W_M` | 0.1625 | +0.1156 |
| 2 | `musae_DE_edges-ncut-k100` | 0.0758 | `W_M` | 0.1675 | +0.0917 |
| 3 | `musae_ES_edges-ncut-k50` | 0.1280 | `1.0` | 0.2183 | +0.0902 |
| 4 | `lastfm_asia_edges-ncut-k500` | 0.4155 | `10.0` | 0.4970 | +0.0815 |
| 5 | `lastfm_asia_edges-ncut-k400` | 0.4571 | `5.0` | 0.5348 | +0.0777 |
| 6 | `musae_ES_edges-ncut-k100` | 0.1216 | `1.0` | 0.1983 | +0.0767 |
| 7 | `lastfm_asia_edges-ncut-k300` | 0.5020 | `5.0` | 0.5663 | +0.0643 |
| 8 | `Email-Enron-ncut-k300` | 0.4264 | `5.0` | 0.4904 | +0.0640 |
| 9 | `lastfm_asia_edges-ncut-k200` | 0.5662 | `5.0` | 0.6261 | +0.0599 |
| 10 | `musae_DE_edges-ncut-k200` | 0.0943 | `10.0` | 0.1513 | +0.0570 |
