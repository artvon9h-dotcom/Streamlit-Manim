"""Trang web học liệu: Khoảng cách giữa hai mặt phẳng song song (Toán 11).
Chạy trên máy: streamlit run app.py
"""
import os
import re

import streamlit as st
import streamlit.components.v1 as components

from cau_hinh import LINK_GEOGEBRA, TEN_NHOM, VIDEO
from noi_dung import BAI_TAP

THU_MUC = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(
    page_title="Khoảng cách giữa hai mặt phẳng song song",
    page_icon="📐",
    layout="wide",
)

st.markdown(
    """
    <style>
    .block-container {padding-top: 1.5rem; max-width: 1100px;}
    .the-muc-do {display:inline-block; padding:2px 10px; border-radius:12px;
                 background:#e7f1fb; color:#1f4e79; font-size:0.9rem; margin-bottom:0.5rem;}
    .khung-de {background:#f7f7f5; border-left:4px solid #1f4e79; padding:0.8rem 1rem;
               border-radius:4px; margin-bottom:1rem;}
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------------- GeoGebra
def lay_ma_geogebra(link: str):
    """Lấy mã tài liệu từ link chia sẻ, ví dụ https://www.geogebra.org/m/abcd1234 -> abcd1234."""
    if not link:
        return None
    m = re.search(r"geogebra\.org/(?:m|material/show/id|classic|3d|calculator)/([A-Za-z0-9]+)", link)
    return m.group(1) if m else None


def nhung_geogebra(link: str, cao: int = 520):
    ma = lay_ma_geogebra(link)
    if not ma:
        st.info("Chưa có link GeoGebra cho bài này. Dán link vào file **cau_hinh.py**.")
        return
    html = f"""
    <div id="ggb-element"></div>
    <script src="https://www.geogebra.org/apps/deployggb.js"></script>
    <script>
      var rong = Math.min(document.body.clientWidth || 900, 1000);
      var params = {{
        "material_id": "{ma}",
        "width": rong, "height": {cao},
        "showToolBar": false, "showAlgebraInput": false, "showMenuBar": false,
        "enableShiftDragZoom": true, "showResetIcon": true,
        "enableRightClick": false, "showFullscreenButton": true
      }};
      var applet = new GGBApplet(params, true);
      applet.inject("ggb-element");
    </script>
    """
    components.html(html, height=cao + 20)
    st.caption(f"Không hiện hình? [Mở trực tiếp trên GeoGebra]({link})")


# ---------------------------------------------------------------- Trang chủ
def trang_chu():
    st.title("Khoảng cách giữa hai mặt phẳng song song")
    st.markdown("**Toán 11 – Học liệu dạy học trực quan**")
    st.markdown(
        "Trang web gồm **6 bài tập** xếp từ mức nhận biết đến vận dụng cao. "
        "Mỗi bài có mô hình **GeoGebra 3D** để xoay hình, kéo điểm, và một số bài có "
        "**video hoạt họa Manim** minh họa lời giải."
    )
    st.markdown("#### Định nghĩa")
    st.markdown(
        '<div class="khung-de">Khoảng cách giữa hai mặt phẳng song song là khoảng cách '
        "từ một điểm <b>bất kỳ</b> của mặt phẳng này đến mặt phẳng kia.</div>",
        unsafe_allow_html=True,
    )
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Dành cho học sinh")
        st.markdown(
            "1. Chọn một bài ở thanh bên trái.\n"
            "2. Đọc đề, tự vẽ hình và thử giải trước.\n"
            "3. Bị kẹt thì mở **Gợi ý 1**, chưa ra mới mở **Gợi ý 2**.\n"
            "4. Xoay, kéo hình GeoGebra để kiểm tra dự đoán.\n"
            "5. Làm xong mới mở **Lời giải** để đối chiếu."
        )
    with c2:
        st.markdown("#### Dành cho giáo viên")
        st.markdown(
            "- Bật **Chế độ giáo viên** ở thanh bên trái để lời giải hiện sẵn khi trình chiếu.\n"
            "- Bấm nút toàn màn hình ở góc khung GeoGebra để chiếu to hơn.\n"
            "- Video Manim có ở Bài 1, Bài 4 và Bài 5."
        )
    st.markdown("#### Danh sách bài")
    bang = "| Bài | Nội dung | Mức độ | GeoGebra | Video |\n|---|---|---|---|---|\n"
    for b in BAI_TAP:
        co_ggb = "Có" if lay_ma_geogebra(LINK_GEOGEBRA.get(b["so"], "")) else "Chưa có link"
        co_video = "Có" if b["so"] in VIDEO else "–"
        bang += f"| {b['so']} | {b['ten']} | {b['muc_do']} | {co_ggb} | {co_video} |\n"
    st.markdown(bang)


# ---------------------------------------------------------------- Trang bài tập
def trang_bai(b, che_do_gv: bool):
    st.title(f"Bài {b['so']}. {b['ten']}")
    st.markdown(f'<span class="the-muc-do">Mức độ: {b["muc_do"]}</span>', unsafe_allow_html=True)

    st.markdown("#### Đề bài")
    st.markdown(b["de"])

    st.markdown("#### Mô hình GeoGebra 3D")
    nhung_geogebra(LINK_GEOGEBRA.get(b["so"], ""))

    if b["so"] in VIDEO:
        duong_dan = os.path.join(THU_MUC, VIDEO[b["so"]])
        st.markdown("#### Video minh họa")
        if os.path.exists(duong_dan):
            st.video(duong_dan)
        else:
            st.warning(f"Không tìm thấy file video: {VIDEO[b['so']]}")

    st.markdown("#### Gợi ý và lời giải")
    for i, g in enumerate(b["goi_y"], 1):
        with st.expander(f"Gợi ý {i}", expanded=False):
            st.markdown(g)
    with st.expander("Lời giải", expanded=che_do_gv):
        st.markdown(b["loi_giai"])


# ---------------------------------------------------------------- Bố cục
with st.sidebar:
    st.header("Nội dung")
    lua_chon = ["Trang chủ"] + [f"Bài {b['so']}. {b['ten']}" for b in BAI_TAP]
    trang = st.radio("Chọn trang", lua_chon, label_visibility="collapsed")
    st.divider()
    che_do_gv = st.toggle("Chế độ giáo viên", help="Hiện sẵn lời giải để trình chiếu")
    st.caption(TEN_NHOM)

if trang == "Trang chủ":
    trang_chu()
else:
    so = lua_chon.index(trang)
    trang_bai(BAI_TAP[so - 1], che_do_gv)
