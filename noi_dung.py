# Nội dung 6 bài tập (lấy từ Sản phẩm 4 – Hệ thống bài tập).
# Công thức viết bằng LaTeX đặt giữa hai dấu $ ... $.

BAI_TAP = [
    {
        "so": 1,
        "ten": "Căn phòng",
        "muc_do": "Biết",
        "de": r"""Một căn phòng có dạng hình hộp chữ nhật $ABCD.A'B'C'D'$ với chiều dài $AB = 5$ m, chiều rộng $AD = 4$ m, chiều cao $AA' = 3$ m. Tính:

a) Khoảng cách giữa sàn $(ABCD)$ và trần $(A'B'C'D')$.

b) Khoảng cách giữa hai bức tường đối diện $(ABB'A')$ và $(DCC'D')$.""",
        "goi_y": [
            "Sàn và trần có vị trí tương đối như thế nào?",
            "Hãy chọn một điểm trên trần. Đường thẳng nào đi qua điểm đó và vuông góc với sàn? Kéo điểm $M$ trong GeoGebra để kiểm tra.",
        ],
        "loi_giai": r"""**Đáp số:** a) 3 m; b) 4 m.

a) $(ABCD) \parallel (A'B'C'D')$ và $AA' \perp (ABCD)$, $A'$ thuộc $(A'B'C'D')$, nên khoảng cách bằng $AA' = 3$ m.

b) $AD \perp AB$ và $AD \perp AA'$ nên $AD \perp (ABB'A')$. Vì $(ABB'A') \parallel (DCC'D')$ và $D$ thuộc $(DCC'D')$ nên khoảng cách bằng $AD = 4$ m.""",
    },
    {
        "so": 2,
        "ten": "Hình chóp và mặt phẳng qua trung điểm",
        "muc_do": "Hiểu",
        "de": r"""Cho hình chóp $S.ABCD$ có đáy là hình vuông cạnh $a$, $SA \perp (ABCD)$ và $SA = 2a$. Gọi $M, N, P, Q$ lần lượt là trung điểm của $SA, SB, SC, SD$. Chứng minh $(MNPQ) \parallel (ABCD)$ và tính khoảng cách giữa hai mặt phẳng đó.""",
        "goi_y": [
            "$MN$ và $MQ$ song song với những đường thẳng nào nằm trong mặt đáy?",
            "Điểm nào trên $(MNPQ)$ có sẵn đường vuông góc xuống đáy?",
        ],
        "loi_giai": r"""**Đáp số:** $a$.

- $MN$ là đường trung bình của tam giác $SAB$ nên $MN \parallel AB$; $MQ$ là đường trung bình của tam giác $SAD$ nên $MQ \parallel AD$.
- $MN$, $MQ$ cắt nhau tại $M$, nằm trong $(MNPQ)$ và cùng song song với $(ABCD)$, nên $(MNPQ) \parallel (ABCD)$.
- $M$ thuộc $(MNPQ)$, $M$ nằm trên $SA$ mà $SA \perp (ABCD)$ tại $A$, nên khoảng cách bằng $MA = \dfrac{SA}{2} = a$.""",
    },
    {
        "so": 3,
        "ten": "Lăng trụ tam giác đều",
        "muc_do": "Hiểu",
        "de": r"""Cho lăng trụ tam giác đều $ABC.A'B'C'$ có cạnh đáy bằng $a$ và cạnh bên $AA' = a\sqrt{3}$. Gọi $M, N, P$ lần lượt là trung điểm của $AA', BB', CC'$. Tính khoảng cách giữa hai mặt phẳng $(MNP)$ và $(A'B'C')$.""",
        "goi_y": [
            "Lăng trụ đều có phải là lăng trụ đứng không? Cạnh bên có vuông góc với đáy không?",
            "Chọn điểm $M$. Khoảng cách từ $M$ đến $(A'B'C')$ là đoạn thẳng nào?",
        ],
        "loi_giai": r"""**Đáp số:** $\dfrac{a\sqrt{3}}{2}$.

- $MA'$ và $NB'$ song song và bằng nhau nên $MNB'A'$ là hình bình hành, suy ra $MN \parallel A'B'$. Tương tự $MP \parallel A'C'$. Do đó $(MNP) \parallel (A'B'C')$.
- Lăng trụ đều là lăng trụ đứng nên $AA' \perp (A'B'C')$. $M$ thuộc $(MNP)$ nên khoảng cách bằng $MA' = \dfrac{AA'}{2} = \dfrac{a\sqrt{3}}{2}$.""",
    },
    {
        "so": 4,
        "ten": "Lăng trụ xiên",
        "muc_do": "Vận dụng",
        "de": r"""Cho lăng trụ $ABC.A'B'C'$ có đáy là tam giác đều cạnh $a$ và $AA' = a$. Hình chiếu vuông góc của $A'$ lên mặt phẳng $(ABC)$ là trọng tâm $G$ của tam giác $ABC$. Tính khoảng cách giữa hai mặt đáy $(ABC)$ và $(A'B'C')$.""",
        "goi_y": [
            "Cạnh bên $AA'$ có vuông góc với mặt đáy không? Nếu không thì $AA'$ có phải là khoảng cách không?",
            "Đường nào từ $A'$ vuông góc với $(ABC)$? Tính đường đó trong tam giác vuông nào?",
        ],
        "loi_giai": r"""**Đáp số:** $\dfrac{a\sqrt{6}}{3}$.

- Hai đáy của lăng trụ song song. $A'$ thuộc $(A'B'C')$ và $A'G \perp (ABC)$, nên khoảng cách cần tìm bằng $A'G$.
- $G$ là trọng tâm tam giác đều cạnh $a$ nên $AG = \dfrac{2}{3}\cdot\dfrac{a\sqrt{3}}{2} = \dfrac{a\sqrt{3}}{3}$.
- Tam giác $A'GA$ vuông tại $G$: $A'G^2 = AA'^2 - AG^2 = a^2 - \dfrac{a^2}{3} = \dfrac{2a^2}{3}$, suy ra $A'G = \dfrac{a\sqrt{6}}{3}$.

**Lỗi hay gặp:** lấy khoảng cách bằng cạnh bên $AA' = a$. Cạnh bên chỉ là khoảng cách khi lăng trụ là lăng trụ đứng.""",
    },
    {
        "so": 5,
        "ten": "Hình lập phương",
        "muc_do": "Vận dụng",
        "de": r"""Cho hình lập phương $ABCD.A'B'C'D'$ cạnh $a$. Chứng minh $(AB'D') \parallel (C'BD)$ và tính khoảng cách giữa hai mặt phẳng đó.""",
        "goi_y": [
            "Tìm trong $(C'BD)$ hai đường thẳng lần lượt song song với $AB'$ và $AD'$.",
            "Đường chéo nào của hình lập phương vuông góc với cả hai mặt phẳng?",
        ],
        "loi_giai": r"""**Đáp số:** $\dfrac{a\sqrt{3}}{3}$.

- $AB'C'D$ là hình bình hành nên $AB' \parallel DC'$; $ABC'D'$ là hình bình hành nên $AD' \parallel BC'$. Hai đường cắt nhau $AB'$, $AD'$ cùng song song với $(C'BD)$, nên $(AB'D') \parallel (C'BD)$.
- $B'D' \perp A'C'$ và $B'D' \perp CC'$ nên $B'D' \perp A'C$. Tương tự $AB' \perp A'C$. Vậy $A'C \perp (AB'D')$, do đó $A'C$ cũng vuông góc với $(C'BD)$.
- Gọi $I, J$ là giao điểm của $A'C$ với $(AB'D')$ và $(C'BD)$. Tứ diện $A'.AB'D'$ vuông tại $A'$: $\dfrac{1}{A'I^2} = \dfrac{3}{a^2}$, suy ra $A'I = \dfrac{a\sqrt{3}}{3}$. Tương tự $CJ = \dfrac{a\sqrt{3}}{3}$.
- $IJ = A'C - A'I - CJ = a\sqrt{3} - \dfrac{2a\sqrt{3}}{3} = \dfrac{a\sqrt{3}}{3}$. Hai mặt phẳng chia đường chéo $A'C$ thành ba đoạn bằng nhau.""",
    },
    {
        "so": 6,
        "ten": "Hình hộp chữ nhật",
        "muc_do": "Vận dụng",
        "de": r"""Cho hình hộp chữ nhật $ABCD.A'B'C'D'$ có $AB = a$, $AD = AA' = 2a$. Chứng minh $(A'BD) \parallel (CB'D')$ và tính khoảng cách giữa hai mặt phẳng đó.""",
        "goi_y": [
            "$BD$ và $A'B$ song song với những đường thẳng nào nằm trong $(CB'D')$?",
            "$AB'$ cắt mặt phẳng $(A'BD)$ tại đâu? Điểm đó chia $AB'$ theo tỉ số nào? Từ đó so sánh khoảng cách từ $B'$ và từ $A$ đến $(A'BD)$.",
        ],
        "loi_giai": r"""**Đáp số:** $\dfrac{a\sqrt{6}}{3}$.

- $BDD'B'$ là hình chữ nhật nên $BD \parallel B'D'$; $A'BCD'$ là hình bình hành nên $A'B \parallel D'C$. Do đó $(A'BD) \parallel (CB'D')$.
- $B'$ thuộc $(CB'D')$ nên khoảng cách cần tìm bằng $d(B', (A'BD))$.
- $AB'$ cắt $A'B$ tại trung điểm $I$ của $AB'$, mà $I$ thuộc $(A'BD)$, nên $d(B', (A'BD)) = d(A, (A'BD))$.
- Tứ diện $A.A'BD$ có $AB, AD, AA'$ đôi một vuông góc: $\dfrac{1}{h^2} = \dfrac{1}{a^2} + \dfrac{1}{4a^2} + \dfrac{1}{4a^2} = \dfrac{3}{2a^2}$, suy ra $h = \dfrac{a\sqrt{6}}{3}$.""",
    },
]
