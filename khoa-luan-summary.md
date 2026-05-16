# Khóa luận: Motif-enhanced Spectral Clustering trên ma trận hỗn hợp $W_\lambda$

**Tác giả:** Lê Bình Minh
**Tổng hợp từ:** lịch sử thảo luận và thực nghiệm

---

## 1. Đặt vấn đề và giới thiệu bài toán

*[Phần này để trống — sẽ viết sau]*

---

## 2. Cơ sở lý thuyết

Phần này trình bày các kết quả nền tảng đã được kiểm chứng trong literature, được dùng làm công cụ cho phần lý thuyết mới (Phần 3). Cấu trúc gồm ba nhóm: **metrics đánh giá phân hoạch**, **các dạng đồ thị**, và **thuật toán spectral clustering**.

### 2.1. Metrics đánh giá phân hoạch

Cho đồ thị $G = (V, E)$ với $|V| = n$, $|E| = m$, ma trận kề $A$, bậc $d_i = \sum_j A_{ij}$. Một phân hoạch là $\mathcal{C} = \{C_1, \ldots, C_K\}$ với $V = \bigsqcup_k C_k$.

#### 2.1.1. Conductance và thương Rayleigh

**Định nghĩa cut và volume.** Với tập $S \subset V$:

$$\text{cut}(S, \bar{S}) = \sum_{i \in S, j \in \bar{S}} A_{ij}, \qquad \text{vol}(S) = \sum_{i \in S} d_i$$

**Conductance** của tập $S$:

$$\phi(S) = \frac{\text{cut}(S, \bar{S})}{\min(\text{vol}(S), \text{vol}(\bar{S}))}$$

Conductance tối thiểu $\phi^* = \min_S \phi(S)$ đo "cổ chai" của đồ thị — phân hoạch tốt là phân hoạch có conductance nhỏ. Mẫu số $\min(\text{vol}(S), \text{vol}(\bar{S}))$ (không phải chỉ $\text{vol}(S)$) đảm bảo conductance đối xứng giữa $S$ và phần bù.

**Thương Rayleigh.** Với ma trận đối xứng $M$ và vector $x \neq 0$:

$$R(M, x) = \frac{x^T M x}{x^T x}$$

**Tính chất biến phân (Courant-Fischer):**

$$\lambda_k(M) = \min_{\substack{U \subset \mathbb{R}^n \\ \dim U = k}} \max_{x \in U \setminus \{0\}} R(M, x) = \max_{x \perp v_1, \ldots, v_{k-1}} R(M, x)$$

Đặc biệt $\lambda_1(M) = \min_x R(M, x)$ và $\lambda_n(M) = \max_x R(M, x)$. Đây là cách kết nối eigenvalue (đại số) với tối ưu hóa (giải tích) — nền tảng cho mọi spectral relaxation.

**Tổng quát hóa Ky Fan.** Với $S \in \mathbb{R}^{n \times k}$ thỏa $S^T S = I$:

$$\max_{S^T S = I} \text{Tr}(S^T M S) = \sum_{i=1}^k \lambda_{n-i+1}(M) \quad (\text{nghiệm } S^* = [v_n, \ldots, v_{n-k+1}])$$

$$\min_{S^T S = I} \text{Tr}(S^T M S) = \sum_{i=1}^k \lambda_i(M) \quad (\text{nghiệm } S^* = [v_1, \ldots, v_k])$$

Đây là tổng quát hóa Rayleigh từ một vector sang $k$ vector — cho phép spectral relaxation các bài toán phân hoạch $K$ cụm.

**Bất đẳng thức Cheeger.** Cho normalized Laplacian $\mathcal{L} = I - D^{-1/2} A D^{-1/2}$ với eigenvalue $0 = \lambda_1 \leq \lambda_2 \leq \ldots \leq \lambda_n$:

$$\frac{\lambda_2}{2} \leq \phi^* \leq \sqrt{2\lambda_2}$$

Bất đẳng thức này phát biểu cho **mọi đồ thị có trọng số không âm và đối xứng** — đây là điểm then chốt sẽ được dùng cho $W_\lambda$ ở Phần 3.

#### 2.1.2. Modularity

**Modularity matrix.** Null model là đồ thị ngẫu nhiên cùng degree sequence: kỳ vọng cạnh giữa $i$ và $j$ là $d_i d_j / (2m)$.

$$B = A - \frac{d d^T}{2m}$$

**Modularity của phân hoạch:**

$$Q(\mathcal{C}) = \frac{1}{2m} \sum_{ij} \left( A_{ij} - \frac{d_i d_j}{2m} \right) \delta(c_i, c_j)$$

trong đó $c_i$ là cụm chứa $i$. Viết dưới dạng ma trận với $S \in \{0,1\}^{n \times K}$ ($S_{ik} = 1$ nếu $i \in C_k$):

$$Q = \frac{1}{2m} \text{Tr}(S^T B S)$$

**Ý nghĩa:** $Q$ đo "mật độ cạnh nội cụm trừ kỳ vọng ngẫu nhiên". $Q > 0$ nghĩa là phân hoạch tốt hơn random, $Q$ càng lớn càng phân hoạch tốt theo nghĩa cộng đồng (Newman 2006).

**Bài toán NP-hard.** $\max_S Q$ trên $S \in \{0,1\}^{n \times K}$ là NP-hard. Spectral relaxation dùng Ky Fan: thay constraint $S \in \{0,1\}$ bằng $S^T S = I$, nghiệm là $K$ eigenvector ứng với $K$ eigenvalue **lớn nhất** của $B$ (vì đây là max trace).

**Liên hệ với Laplacian.** Với đồ thị $d$-regular ($d_i = d$ với mọi $i$):

$$B = A - \frac{d}{n} J = d I - \mathcal{L}^{\text{unnorm}} - \frac{d}{n} J$$

Eigenvalue của $B$ là phép dịch và scale của eigenvalue Laplacian. Cùng cấu trúc bài toán: rời rạc → relaxation → eigenvalue, chỉ khác **min vs max** và **$\mathcal{L}$ vs $B$**.

**Resolution limit.** Modularity bỏ qua các cụm nhỏ hơn $O(\sqrt{m})$ — chúng bị merge vào cụm lớn hơn dù thực sự là cộng đồng riêng. Đây là giới hạn cấu trúc của $B$.

#### 2.1.3. Hệ số phân cụm (Clustering coefficient)

**CC của đỉnh.** Hệ số phân cụm cục bộ của đỉnh $v$:

$$cc(v) = \frac{2 \cdot T_v}{d_v(d_v - 1)}$$

trong đó $T_v$ là số tam giác chứa $v$. $cc(v) = 0$ nếu $d_v \leq 1$. Trực giác: trong số $\binom{d_v}{2}$ cặp hàng xóm của $v$, có bao nhiêu cặp thực sự nối với nhau.

**CC trung bình mỗi cụm.** Cho cụm $C_j$:

$$\text{CC}(C_j) = \frac{1}{|C_j|} \sum_{v \in C_j} cc(v)$$

**CC_AVG (trung bình các cụm):**

$$\text{CC\_AVG} = \frac{1}{K} \sum_{j=1}^K \text{CC}(C_j)$$

**CC_WEIGHTED (trung bình có trọng số theo kích thước cụm):**

$$\text{CC\_WEIGHTED} = \frac{\sum_{j=1}^K |C_j| \cdot \text{CC}(C_j)}{\sum_{j=1}^K |C_j|} = \frac{1}{n} \sum_{v \in V} cc(v)$$

**CC_AVG vs CC_WEIGHTED — artifact của cụm nhỏ.** CC_AVG bị thiên lệch khi có cụm rất nhỏ: một cụm 3 đỉnh tạo thành tam giác có CC = 1, kéo CC_AVG lên cao dù cụm này không có ý nghĩa cộng đồng. CC_WEIGHTED phạt cụm nhỏ vì trọng số tỷ lệ với $|C_j|$. Trong khóa luận, CC_WEIGHTED được dùng làm primary metric.

**Tính chất quan trọng.** $cc(v)$ tính trên đồ thị **gốc** $A$, không phụ thuộc $\lambda$. Khi $\lambda$ thay đổi, **CC từng đỉnh không đổi** — cái thay đổi là **phân hoạch** (đỉnh nào ở cụm nào), nên CC trung bình cụm thay đổi vì thành viên cụm thay đổi.

**CC nội cụm.** Một biến thể đếm chỉ tam giác mà cả 3 đỉnh cùng cụm:

$$cc_C(v) = \frac{2 \cdot T_v^{(C)}}{d_v^{(C)}(d_v^{(C)} - 1)}$$

trong đó $T_v^{(C)}$ là số tam giác chứa $v$ với cả 3 đỉnh trong cụm chứa $v$, $d_v^{(C)}$ là số hàng xóm của $v$ trong cùng cụm. Đây là metric phù hợp khi quan tâm đến mức độ "đóng kín" của motif trong cộng đồng.

### 2.2. Các dạng đồ thị

#### 2.2.1. Motif

**Định nghĩa motif.** Motif $M$ là một đồ thị con nhỏ, cố định, dùng làm "đơn vị cấu trúc" để phân tích đồ thị lớn. Trong khóa luận: $M = K_3$ (tam giác).

**Motif instance.** Một instance của $M$ trong $G$ là một đồ thị con của $G$ đẳng cấu với $M$. Với $K_3$: bộ 3 đỉnh đôi một nối với nhau.

**Tại sao chọn $K_3$.**

- **Đơn vị cộng đồng tự nhiên trong mạng xã hội:** triadic closure (A bạn B, B bạn C → A có xu hướng bạn C) tạo tam giác có chủ đích, không ngẫu nhiên. Đây là cơ chế xã hội tạo ra cấu trúc cộng đồng.
- **Đếm tam giác hiệu quả** trên đồ thị thưa.
- **Đối xứng tự nhiên:** không cần xử lý directionality như các motif phức tạp hơn.

**So sánh edge vs motif — ví dụ trực quan.**

*Trường hợp 1:* Hai cụm 6 đỉnh, nối nhau bởi 5 cạnh nhưng không cạnh nào tạo tam giác cross-cluster. Edge conductance: 5 cạnh cắt → vừa phải. Motif conductance: 0 → rất nhỏ (cut hoàn hảo từ góc nhìn motif).

*Trường hợp 2:* Hai cụm 6 đỉnh, nối nhau bởi 2 cạnh nhưng 2 cạnh tạo thành tam giác cross-cluster. Edge conductance: 2 cạnh cắt → nhỏ. Motif conductance: > 0 → không nhỏ.

Hai trường hợp này, edge conductance và motif conductance cho **kết luận trái ngược** về chất lượng cut — đây là động lực cho việc kết hợp cả hai.

#### 2.2.2. Đồ thị $G_M$ và motif adjacency matrix

**Motif adjacency matrix:**

$$W^{(M)}_{ij} = |\{\text{instance của } M \text{ chứa cả } i \text{ và } j\}|$$

**Đồ thị motif $G_M$.** Đồ thị có cùng tập đỉnh $V$, ma trận kề $W^{(M)}$. Cạnh $(i,j)$ trong $G_M$ có trọng số = số motif chứa cả hai đỉnh.

**Tính chất.** $W^{(M)}$ đối xứng và không âm → $G_M$ là weighted undirected graph hợp lệ → áp dụng được toàn bộ spectral theory cho weighted graph (Cheeger, NCut, modularity).

**Motif degree:** $d_i^{(M)} = \sum_j W^{(M)}_{ij}$. Motif volume: $\text{vol}_M(S) = \sum_{i \in S} d_i^{(M)}$.

**Motif conductance** (Benson, Gleich, Leskovec 2016):

$$\phi_M(S) = \frac{|\{\text{motif instance bị cắt bởi } (S, \bar{S})\}|}{\min(\text{vol}_M(S), \text{vol}_M(\bar{S}))}$$

**Higher-order Cheeger inequality.** Spectral clustering trên $W^{(M)}$ đảm bảo near-optimal cut theo $\phi_M$, với cùng dạng bound như Cheeger cổ điển vì $G_M$ là weighted undirected graph hợp lệ.

**Hạn chế của $G_M$ thuần:**

1. **Có thể disconnect:** đỉnh không thuộc bất kỳ motif nào sẽ cô lập trong $G_M$, dù trong $G$ gốc có thể có nhiều cạnh kề.
2. **Mất thông tin cạnh gốc:** cạnh không thuộc tam giác nào bị xóa hoàn toàn trong $G_M$, dù có thể mang thông tin cộng đồng quan trọng.

Hai hạn chế này là động lực trực tiếp cho ma trận hỗn hợp $W_\lambda$ ở Phần 3.

### 2.3. Thuật toán spectral clustering

#### 2.3.1. Ý tưởng tổng quát

Thay vì giải trực tiếp bài toán phân hoạch tổ hợp (NP-hard), spectral clustering thực hiện hai bước:

1. **Embed** đồ thị vào không gian Euclidean qua eigenvector của Laplacian (hoặc adjacency).
2. **Cluster** trong không gian Euclidean bằng thuật toán đơn giản (k-means).

Bước embed dùng thông tin toàn cục (eigenvector chứa thông tin về mọi đỉnh), tránh bẫy cục bộ của các thuật toán greedy.

#### 2.3.2. Normalized Cut (NCut)

**Bài toán cut tối thiểu.** Tìm $S \subset V$ minimize $\text{cut}(S, \bar{S})$ → bias mạnh về cụm rất nhỏ (cụm 1 đỉnh có cut = $d_v$). Đây là lý do cần normalize.

**Normalized cut** (Shi-Malik 2000):

$$\text{NCut}(S, \bar{S}) = \frac{\text{cut}(S, \bar{S})}{\text{vol}(S)} + \frac{\text{cut}(S, \bar{S})}{\text{vol}(\bar{S})}$$

NCut chuẩn hóa theo volume nên không bị bias về cụm nhỏ. Liên hệ với conductance: $\text{NCut} \approx 2\phi(S)$ khi cụm cân bằng.

**Tổng quát hóa $K$ cụm:**

$$\text{NCut}(\mathcal{C}) = \sum_{k=1}^K \frac{\text{cut}(C_k, \bar{C_k})}{\text{vol}(C_k)}$$

#### 2.3.3. Spectral relaxation của NCut

Đặt $f \in \mathbb{R}^n$ là indicator vector chuẩn hóa của $S$. Bài toán $\min \text{NCut}$ tương đương:

$$\min_{f} \frac{f^T \mathcal{L}^{\text{unnorm}} f}{f^T D f} \quad \text{với constraint } f \perp D \mathbf{1}, \; f \in \{a, b\}^n$$

**Relaxation:** bỏ constraint rời rạc $f \in \{a, b\}^n$, cho $f \in \mathbb{R}^n$. Theo thương Rayleigh tổng quát, nghiệm là **eigenvector tương ứng eigenvalue nhỏ thứ hai** của bài toán generalized eigenvalue $\mathcal{L}^{\text{unnorm}} f = \lambda D f$, hay tương đương eigenvector thứ hai của normalized Laplacian:

$$\mathcal{L} = I - D^{-1/2} A D^{-1/2}$$

Vector này được gọi là **Fiedler vector**. Từ vector liên tục, dùng sweep cut hoặc k-means để rời rạc hóa thành phân hoạch.

#### 2.3.4. Thuật toán cho $K$ cụm

Cho ma trận trọng số $W$ đối xứng, không âm, và số cụm $K$:

1. Tính $D = \text{diag}(W \mathbf{1})$ (ma trận đường chéo của tổng hàng).
2. Tính normalized Laplacian $\mathcal{L} = I - D^{-1/2} W D^{-1/2}$.
3. Tính $K$ eigenvector $u_1, \ldots, u_K$ ứng với $K$ eigenvalue nhỏ nhất của $\mathcal{L}$.
4. Đặt $U = [u_1, \ldots, u_K] \in \mathbb{R}^{n \times K}$.
5. Chuẩn hóa hàng của $U$ thành unit norm.
6. Chạy $k$-means trên các hàng của $U$ → $K$ cụm.

Đầu ra là phân hoạch $\{C_1, \ldots, C_K\}$.

**Độ phức tạp:** $O(n^3)$ cho eigendecomposition đầy đủ; $O(K n m)$ với sparse Lanczos cho $K$ eigenvector đầu tiên trên đồ thị thưa.

#### 2.3.5. Cơ sở lý thuyết: tại sao spectral clustering hoạt động

**(1) Cheeger inequality** đảm bảo cut tìm bởi sweep trên Fiedler vector có conductance $\phi(S) \leq \sqrt{2\lambda_2}$. Khi $\lambda_2$ nhỏ — cộng đồng tách rõ — cut tìm được gần tối ưu.

**(2) Davis-Kahan theorem.** Cho ma trận đối xứng $A$ và perturbation $A + E$. Nếu eigenvalue gap $\delta = |\lambda_k(A) - \lambda_{k\pm1}(A)| > 0$ thì:

$$\sin\Theta(v_k(A), v_k(A+E)) \leq \frac{\|E\|}{\delta}$$

Ý nghĩa: nếu đồ thị có spectral gap rõ ràng và nhiễu nhỏ, eigenvector ổn định → phân hoạch ổn định.

**(3) Weyl's inequality.** Với $A, E$ symmetric: $\lambda_k(A) + \lambda_n(E) \leq \lambda_k(A + E) \leq \lambda_k(A) + \lambda_1(E)$. Cho phép bound eigenvalue của ma trận perturbation.

**(4) Ky Fan theorem.** $\max_{S^TS=I} \text{Tr}(S^T M S) = \sum_{i=1}^K \lambda_{\max,i}(M)$, nghiệm là $K$ top eigenvector. Đây là nền tảng spectral relaxation cho mọi bài toán $K$-way (NCut, modularity).

**(5) Template chứng minh consistency** (Lei-Rinaldo 2015, SCORE Jin 2015, Su-Wang-Zhang 2017):

$$\underbrace{\mathbb{E}[A] \text{ block}}_{\text{model}} \xrightarrow{\text{concentration}} \underbrace{\|A - \mathbb{E}[A]\| \text{ nhỏ}}_{\text{RMT}} \xrightarrow{\text{Davis-Kahan}} \underbrace{v(A) \approx v(\mathbb{E}[A])}_{\text{eigenvector ổn định}} \xrightarrow{k\text{-means}} \underbrace{\text{phân hoạch đúng}}_{\text{kết luận}}$$

---

## 3. Các ý tưởng thuật toán

Phần này trình bày đóng góp chính của khóa luận: ma trận hỗn hợp $W_\lambda$ và các diễn giải lý thuyết đi kèm.

### 3.1. Ma trận hỗn hợp $W_\lambda = A + \lambda W^{(M)}$

**Định nghĩa.** Với $\lambda \geq 0$:

$$W_\lambda = A + \lambda W^{(M)}$$

$W_\lambda$ là ma trận đối xứng, không âm — thỏa mãn mọi điều kiện của weighted graph theory. Do đó **kế thừa toàn bộ guarantee** của Cheeger inequality và spectral clustering trên weighted graph.

**Khắc phục hạn chế của $W^{(M)}$ thuần:**

- Đỉnh không thuộc tam giác nào vẫn liên thông qua thành phần $A$.
- Thông tin cạnh gốc được giữ lại với trọng số $1$.

**Lý do framing "motif-enhanced" thay vì "mixed graph":** thuật ngữ "mixed graph" trong graph theory đã được dùng cho đồ thị có cả cạnh có hướng và vô hướng — tránh lẫn lộn.

### 3.2. Diễn giải $\lambda$ như Pareto weight

NCut trên $W_\lambda$ tương đương minimize:

$$\text{cut}_\lambda(S) = \text{cut}_0(S) + \lambda \cdot \text{cut}_M(S)$$

Mỗi nhát cắt $S$ xác định một điểm $(\text{cut}_0(S), \text{cut}_M(S))$ trong $\mathbb{R}^2$. Ba bài toán tối ưu chọn điểm khác nhau trên mặt phẳng này:

- $\lambda = 0$: minimize $\text{cut}_0$ theo hướng $(1, 0)$ — tối ưu edge cut, bất chấp motif cut.
- $W_M$ thuần ($\lambda \to \infty$): minimize $\text{cut}_M$ theo hướng $(0, 1)$ — tối ưu motif cut, bất chấp edge cut.
- Mixed $\lambda > 0$: minimize $\text{cut}_0 + \lambda \, \text{cut}_M$ theo hướng $(1, \lambda)$ — điểm trên Pareto frontier.

Edge information đóng góp tỷ trọng $1/(1+\lambda)$, motif đóng góp $\lambda/(1+\lambda)$. Mọi $\lambda \in (0, \infty)$ là phương pháp **mới** kết hợp cả hai.

### 3.3. Thuật toán: NCut trên $W_\lambda$

Cho đồ thị $G = (V, E)$, motif $M$ (mặc định $K_3$), tham số $\lambda \geq 0$, số cụm $K$:

1. Tính ma trận motif $W^{(M)}_{ij} = $ số instance $M$ chứa cả $i$ và $j$.
2. Tính $W_\lambda = A + \lambda W^{(M)}$.
3. Chạy NCut trên $W_\lambda$:
   - $D_\lambda = \text{diag}(W_\lambda \mathbf{1})$
   - $\mathcal{L}_\lambda = I - D_\lambda^{-1/2} W_\lambda D_\lambda^{-1/2}$
   - Lấy $K$ eigenvector ứng với $K$ eigenvalue nhỏ nhất của $\mathcal{L}_\lambda$.
   - $k$-means trên các hàng → $K$ cụm.

Đầu ra là phân hoạch.

### 3.4. Hai chế độ phụ thuộc cấu trúc đồ thị

Phân tích lý thuyết và thực nghiệm cho thấy hai chế độ trái ngược, phụ thuộc tỷ lệ tín hiệu/nhiễu giữa edge và motif:

**Chế độ 1: Giàu motif, cộng đồng mạnh.** Motif tập trung trong cụm, ít motif cross-cluster. $W_M$ thuần đã tối ưu cả modularity lẫn CC — minimize $\text{cut}_M$ tự động kéo theo $\text{cut}_0$ nhỏ vì hai nguồn tương hợp. Mixed matrix trở nên dư thừa.

**Chế độ 2: Cấu trúc cộng đồng yếu hoặc motif phân bố không tập trung.** $W_M$ thuần phá vỡ cấu trúc cụm lớn — minimize $\text{cut}_M$ cắt nhiều cạnh nội cụm, modularity giảm mạnh dù CC tăng. Mixed matrix có ý nghĩa: thành phần $A$ đóng vai trò regularize, ngăn motif "kéo" thuật toán đi quá xa khỏi phân hoạch tốt theo edge.

Hai chế độ này gợi ý: $\lambda^*$ tối ưu phụ thuộc vào tính chất nội tại của đồ thị (mật độ motif, độ mạnh cộng đồng), không phải hằng số toàn cục.

### 3.5. Chiến lược chọn $\lambda$ tối ưu

**Vấn đề đánh giá.** Dùng $Q_A$ (modularity gốc) để đánh giá phân hoạch tìm bằng $W_\lambda$ thì khập khiễng vì $W_\lambda$ tối ưu **mật độ motif**, không phải mật độ cạnh — như đo bài thi motif bằng thước cạnh.

**Hướng tiếp cận:**

- **Hướng 1 (Heuristic):** grid search $\lambda \in \{0, 0.5, 1, 2, 5, 10\}$, chọn theo objective tổng hợp giữa $Q$ và CC_WEIGHTED.
- **Hướng 2 (Mixed modularity):** định nghĩa $Q_\lambda$ trên $W_\lambda$ với null model thích hợp:

$$B_\lambda = W_\lambda - \frac{d_\lambda d_\lambda^T}{2 m_\lambda}, \quad (d_\lambda)_i = d_i + \lambda d_i^{(M)}, \quad m_\lambda = \frac{1}{2}\sum_i (d_\lambda)_i$$

Đây là metric nội tại, không bị thiên lệch khi đánh giá riêng theo $A$ hay $W^{(M)}$.

- **Hướng 3 (Hàm $f$ tổng quát):** thay $1 + \lambda$ bằng $f(e, \lambda)$ tinh tế hơn. Ví dụ: $1 + \lambda \cdot J(u,v)$ với $J$ là Jaccard coefficient của hai đầu cạnh, hoặc $1 + \lambda \cdot \log(1 + t_{uv})$ với $t_{uv}$ là số tam giác chứa cạnh.

---

## 4. Thực nghiệm

### 4.1. Thiết lập chung

**Thuật toán:** NCut trên $W_\lambda = A + \lambda W^{(M)}$ với $M = K_3$.

**Sweep:** $\lambda \in \{0, 0.5, 1, 2, 5, 10\}$ và $W_M$ thuần (tương ứng $\lambda \to \infty$).

**Số cụm:** $K = K_{\text{gt}}$ (ground truth) cho đồ thị có ground truth; eigengap heuristic cho đồ thị thật không có ground truth.

**Metrics đo lường (tính trên đồ thị gốc $A$):**

- **NMI** (Normalized Mutual Information): so với ground truth, khi có.
- **Modularity** $Q$: phản ánh mật độ cạnh nội cụm so với kỳ vọng ngẫu nhiên.
- **CC_AVG, CC_WEIGHTED:** clustering coefficient trung bình và có trọng số.
- **edges_cut:** số cạnh trong $A$ bị cắt bởi phân hoạch.
- **motifs_cut:** số motif instance trong $A$ bị cắt (có ít nhất 2 đỉnh ở hai cụm khác nhau).

### 4.2. Mô hình sinh dữ liệu

Để kiểm soát tính chất đồ thị một cách hệ thống, khóa luận sử dụng hai mô hình sinh dữ liệu chính bên cạnh đồ thị thật.

#### 4.2.1. LFR Benchmark (Lancichinetti, Fortunato, Radicchi 2008)

LFR là benchmark chuẩn cho community detection vì sinh ra đồ thị có **degree heterogeneity** và **cộng đồng kích thước không đều** — gần với tính chất của mạng thật hơn các mô hình đơn giản.

**Tham số sinh:**

- $n$: số đỉnh.
- Phân phối degree: power-law $P(d) \propto d^{-\gamma}$ với $\gamma \approx 2$.
- Phân phối kích thước cộng đồng: power-law với hệ số $\beta \approx 1$.
- Bậc trung bình $\langle d \rangle$ và bậc cực đại $d_{\max}$.
- **Mixing parameter** $\mu \in [0, 1]$: với mỗi đỉnh, tỷ lệ $\mu$ cạnh nối ra ngoài cụm và $(1-\mu)$ nội cụm. $\mu$ nhỏ → cộng đồng tách rõ; $\mu$ lớn → cộng đồng yếu.

**Cơ chế sinh.** Cạnh được sinh **độc lập** theo xác suất, rồi rewire để đảm bảo tỷ lệ $\mu$ cạnh cross-community.

**Hệ quả với motif.** Tam giác xuất hiện **ngẫu nhiên** — không có cơ chế triadic closure. Mật độ tam giác trong cụm cao hơn ngoài cụm chỉ do chênh lệch mật độ cạnh ($\sim p_{\text{in}}^3$ vs $\sim p_{\text{out}}^3$), không phải vì cơ chế cộng đồng tự nhiên.

**Bộ tham số trong khóa luận:**

- $n \in \{100, 250, 500, 1000, 2000, 5000\}$.
- $\mu \in \{0.1, 0.2, 0.3, 0.35, 0.4, 0.5\}$.
- Tổng: 35 thí nghiệm trải qua các kích thước và độ khó khác nhau.

#### 4.2.2. Gaussian Random Partition Graph

Mô hình đơn giản hơn LFR, dùng để kiểm tra hành vi của thuật toán trong điều kiện đối xứng và dễ phân tích.

**Tham số sinh:**

- $n$: số đỉnh.
- $K$: số cộng đồng.
- Kích thước cộng đồng được lấy mẫu từ phân phối Gaussian quanh trung bình $n/K$.
- $p_{\text{in}}$: xác suất cạnh giữa hai đỉnh cùng cụm.
- $p_{\text{out}}$: xác suất cạnh giữa hai đỉnh khác cụm.

**Cơ chế sinh.** Cạnh được sinh **độc lập** Bernoulli theo $p_{\text{in}}$ hoặc $p_{\text{out}}$.

**Hệ quả với motif.** Giống LFR, tam giác xuất hiện ngẫu nhiên. Xác suất tam giác cross-cluster $\approx p_{\text{out}}^2 p_{\text{in}}$ rất nhỏ → motif gần như luôn đồng ý với cạnh, ít cho thông tin mới.

#### 4.2.3. So sánh hai mô hình sinh và đồ thị thật

Đặc điểm cốt lõi phân biệt mô hình sinh và đồ thị thật:

| Tiêu chí | LFR / Gaussian | Đồ thị social thật |
|---|---|---|
| Cơ chế sinh cạnh | Độc lập, ngẫu nhiên | Triadic closure, homophily, preferential attachment |
| Tam giác | Xuất hiện ngẫu nhiên, $\sim p^3$ | Xuất hiện có chủ đích, mật độ cao hơn nhiều kỳ vọng ngẫu nhiên |
| Clustering coefficient | Thấp | Cao (đặc trưng của social network) |
| Mật độ motif trong cụm vs ngoài cụm | Chỉ chênh do mật độ cạnh | Chênh do cơ chế xã hội — motif là tín hiệu mạnh độc lập |

Đây là lý do căn bản giải thích kết quả thực nghiệm trái ngược giữa hai loại đồ thị (xem Phần 4.5).

### 4.3. Kết quả trên LFR benchmark

**Tham số:** 35 thí nghiệm với $n \in \{100, 250, 500, 1000, 2000, 5000\}$ và $\mu \in \{0.1, 0.2, 0.3, 0.35, 0.4, 0.5\}$.

**Kết quả chính:**

| Quan sát | Kết quả |
|---|---|
| $W_M$ thuần vs $A$ thuần | $W_M$ luôn tệ hơn ở mọi bộ tham số |
| $\lambda^*$ tối ưu | $\lambda = 0.5$ tối ưu cho 26/35 thí nghiệm |
| Cải thiện ở vùng khó | $\mu = 0.3{-}0.5$: $\Delta$NMI lên tới $+0.186$ |
| $\lambda$ lớn | $\lambda \geq 5$ luôn tệ hơn $A$ thuần |

**Giải thích:** Trên LFR cạnh sinh độc lập → 20–68% đỉnh không thuộc tam giác → $W^{(M)}$ thưa và disconnect. Edge **không phải noise** mà là thông tin chính, motif chỉ bổ sung. Tam giác cross-cluster có xác suất rất nhỏ → motif gần như luôn đồng ý với cạnh, nên thêm $\lambda$ chỉ tăng trọng số đã giàu sẵn.

### 4.4. Kết quả trên đồ thị social thật

**Datasets:**

| Dataset | $n$ | Loại |
|---|---|---|
| musae_ES | 4,648 | Twitch social |
| CA-GrQc | 4,158 | Co-authorship |
| CA-HepTh | 8,638 | Co-authorship |
| musae_DE | 9,498 | Twitch social |

**Kết quả chính:**

- $W_M$ thuần cho **modularity cao nhất** *và* **CC cao nhất** — trái ngược hoàn toàn với LFR.
- Mixed matrix với $\lambda > 0$ pha loãng tín hiệu motif → tệ hơn $W_M$ thuần.

**Giải thích:** Trong mạng xã hội thật, tam giác xuất hiện do **triadic closure** (cơ chế xã hội), không ngẫu nhiên. Motif structure mạnh **tuyệt đối** hơn edge structure — minimize motif cut đồng thời minimize edge cut vì hai nguồn thông tin tương hợp. Edge đóng vai trò gần như nhiễu so với motif.

### 4.5. Tổng hợp

| Loại đồ thị | Phương pháp tốt nhất | Lý do |
|---|---|---|
| LFR / Gaussian (sinh ngẫu nhiên) | Mixed ($\lambda \in [0.5, 1]$) | Edge = thông tin chính, $W_M$ thưa và disconnect |
| Social thật | $W_M$ thuần | Triadic closure → motif $\gg$ edge, edge $\approx$ nhiễu |

**Insight cốt lõi:** $\lambda^*$ tối ưu phụ thuộc vào tỷ lệ tín hiệu/nhiễu giữa edge và motif. NCut trên $W_\lambda$ minimize $\text{cut}_0 + \lambda \, \text{cut}_M$ — mỗi $\lambda$ cho một điểm trên Pareto frontier. Trên đồ thị mà edge và motif **mâu thuẫn** (LFR), mixed matrix cân bằng. Trên đồ thị mà hai nguồn **tương hợp** (social thật), $W_M$ thuần đã tối ưu cả hai.

Sự trái ngược giữa hai loại đồ thị **không phải bug của thuật toán**, mà là hệ quả trực tiếp của khác biệt cơ chế sinh dữ liệu được trình bày ở Phần 4.2.3.

---

## 5. Kết luận

**Đóng góp của khóa luận.**

1. **Khung lý thuyết.** Đề xuất ma trận hỗn hợp $W_\lambda = A + \lambda W^{(M)}$ kế thừa toàn bộ guarantee Cheeger của weighted graph spectral clustering. Diễn giải $\lambda$ như Pareto weight giữa edge cut và motif cut, với hai chế độ trái ngược phụ thuộc tính chất đồ thị.

2. **Thực nghiệm hệ thống.** 35 thí nghiệm trên LFR benchmark (kiểm soát qua $n$ và $\mu$) + 4 đồ thị social thật, phát hiện hai chế độ trái ngược: trên đồ thị nhân tạo $\lambda^*$ nhỏ ($\approx 0.5$), trên đồ thị thật $W_M$ thuần tối ưu. Insight: $\lambda^*$ phụ thuộc tỷ lệ tín hiệu/nhiễu giữa edge và motif, được giải thích thông qua sự khác biệt cơ chế sinh dữ liệu (cạnh độc lập vs triadic closure).

3. **Phân tích sự khác biệt LFR/Gaussian vs đồ thị thật.** Chỉ ra rằng kết quả trái ngược không phải lỗi thuật toán mà là hệ quả tất yếu của bản chất sinh dữ liệu — mô hình sinh ngẫu nhiên không capture được cơ chế xã hội tạo motif.

**Hạn chế.**

- Chưa có công thức lý thuyết $\lambda^*(n, K, \rho_{\text{motif}})$ tiên đoán $\lambda$ tối ưu từ tính chất đồ thị.
- Chỉ thực nghiệm trên $K_3$; chưa kiểm soát so với higher-order motifs (4-clique, bi-fan).
- Chưa phát biểu chặt giả thiết cấu trúc cần thiết để đảm bảo $\lambda^*$ tồn tại và có ý nghĩa.

**Hướng phát triển.**

- **Chứng minh tính đúng:** xây dựng khung chứng minh $Q_A(S_\lambda) \geq Q_A(S_0)$ dựa trên template chuẩn của spectral consistency literature (Weyl + Davis-Kahan + Rayleigh), kèm phát biểu chặt điều kiện "motif có ý nghĩa trên $G$".
- **Mở rộng hàm trọng số:** thay $A + \lambda W^{(M)}$ bằng $f(e, \lambda)$ cá nhân hóa theo cạnh — Jaccard, clustering coefficient, hoặc per-node $\lambda$.
- **Mixed modularity $Q_\lambda$** với null model chính xác, thay vì dùng $Q_A$ làm metric đánh giá.
- **Mở rộng sang directed graphs** qua node-splitting BiAttractor/BiCommunity construction.
- **Higher-order motif comparison:** kiểm tra $K_3$ có phải "đơn vị cộng đồng" tự nhiên nhất không — so với $K_4$, bi-fan, các motif 4-node khác.
