# Hướng dẫn chạy trang web học liệu

## Cấu trúc thư mục

```
web_khoang_cach/
  app.py            <- chương trình chính (không cần sửa)
  noi_dung.py       <- đề bài, gợi ý, lời giải 6 bài (sửa khi cần đổi nội dung)
  cau_hinh.py       <- DÁN LINK GEOGEBRA VÀO ĐÂY
  requirements.txt  <- danh sách thư viện cho Streamlit Cloud
  videos/           <- 3 video Manim (720p)
```

## Bước 1. Dán link GeoGebra

Mở `cau_hinh.py`, dán link chia sẻ của từng tệp vào giữa hai dấu ngoặc kép, ví dụ:

```python
1: "https://www.geogebra.org/m/abcd1234",  # Tệp 1 - Căn phòng
```

## Bước 2. Chạy thử trên máy

Mở Terminal trong thư mục `web_khoang_cach`:

```
pip install streamlit
streamlit run app.py
```

Trình duyệt tự mở trang `http://localhost:8501`. Máy phải có mạng thì khung GeoGebra mới hiện.

## Bước 3. Đưa lên mạng miễn phí (Streamlit Community Cloud)

1. Tạo tài khoản GitHub, tạo một kho (repository) mới, chế độ **Public**.
2. Tải toàn bộ các file và thư mục `videos/` lên kho đó (nút "Add file" → "Upload files").
3. Vào https://share.streamlit.io, đăng nhập bằng GitHub, bấm **Create app**.
4. Chọn kho vừa tạo, mục *Main file path* ghi `app.py`, bấm **Deploy**.
5. Sau 2–3 phút sẽ có link dạng `https://ten-cua-ban.streamlit.app` để gửi thầy và học sinh.

Mỗi lần sửa file trên GitHub, trang web tự cập nhật.

## Lưu ý

- Ứng dụng miễn phí trên Streamlit Cloud sẽ "ngủ" nếu lâu không ai mở. Lần đầu mở lại phải chờ khoảng 30 giây.
- Muốn thay video: render lại bằng Manim, đổi tên đúng như trong `cau_hinh.py`, chép đè vào thư mục `videos/`.
