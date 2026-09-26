# BRIEF — Google mở miễn phí công cụ tạo video AI "Vids" cho mọi người

Routine sáng 26/9/2026. Style xoay vòng: **10-stock-terminal** (index 9, `claim_style` trả về lúc
2026-09-26T00:44:25.644Z).

## Nguồn
- Thanh Niên — "Google bất ngờ miễn phí công cụ AI mạnh mẽ cho mọi người", đăng 25/9/2026.
  https://thanhnien.vn/google-bat-ngo-mien-phi-cong-cu-ai-manh-me-cho-moi-nguoi-18526092501105181.htm
- Ảnh: og:image bài báo (ảnh minh hoạ giao diện Google Vids) → `assets/img/article-hero.jpg`.
- Bài đã là tiếng Việt — viết lại gọn theo văn phong bản tin của kênh, không chỉ đọc lại tiêu đề báo.

## GATE A
Tin công nghệ / AI thông thường (mở rộng tính năng / miễn phí hoá sản phẩm AI có sẵn) → **GREEN**.
Không cáo buộc hình sự, không chính trị/bầu cử, không y tế/tài chính giật gân, không deepfake người
thật, không nội dung BLACK. Góc CTA có chạm nhẹ chủ đề "AI sáng tạo nội dung & tác động nghề làm
video" — xử lý như yếu tố nhạy cảm phụ: framing trung lập, đặt câu hỏi mở, không kết luận thay khán
giả (ghi `sensitive_flags` trong COMPLIANCE.md).

## Số liệu / dữ kiện xác nhận (KHÔNG bịa thêm ngoài danh sách này — mọi số liệu truy được về bài gốc)
- Google mở rộng công cụ tạo video bằng **trí tuệ nhân tạo** mang tên **Google Vids**.
- Từ nay **bất kỳ ai có tài khoản Google hoặc Google Workspace đều dùng được miễn phí** — bản mới
  KHÔNG phải bản rút gọn.
- Phiên bản mới chạy trên mô hình **Gemini Omni 1.1 Flash**, giúp tạo video từ đầu và kiểm soát kết
  quả tốt hơn.
- Cho phép **mở rộng một cảnh quay có sẵn** mà vẫn giữ chi tiết quan trọng: nhân vật, môi trường,
  ánh sáng.
- Người dùng có thể **chỉ định độ dài đoạn phim** do AI tạo ra, dễ ghép vào kịch bản hơn.
- Chất lượng nâng cấp: tạo cảnh quay mới ở **độ phân giải 1080p**, nâng cấp video AI cũ hiện có lên
  **HD**.
- Có sẵn **mẫu dựng nhanh** giúp chuyển ảnh sản phẩm / tài liệu thành video hoàn chỉnh.
- Sắp tích hợp **chuyển văn bản thành giọng nói** dựa trên mô hình **Gemini 3.8 Flash-Lite**, hỗ trợ
  hơn **100 ngôn ngữ**.
- Video tạo bằng Omni 1.1 có gắn **hình mờ SynthID của Google** để nhận diện nguồn gốc AI.
- Gói AI trả phí vẫn tồn tại song song: cho **giới hạn tạo nội dung cao hơn** với tài khoản cá nhân;
  khách hàng **Workspace Business / Enterprise** nhận thêm dung lượng + quyền quản trị.

## Góc tranh luận cho act CTA
Google mở công cụ tạo video AI mạnh — từng chỉ có ở gói trả phí — miễn phí cho TẤT CẢ mọi người có
tài khoản Google (dân chủ hoá công cụ sáng tạo) — NHƯNG khi ai cũng tạo được video AI chân thực chỉ
bằng vài dòng lệnh, nội dung do AI tạo ra sẽ tràn lan hơn, và ranh giới thật/giả trên mạng càng khó
phân biệt hơn (dù có watermark SynthID). → Cơ hội sáng tạo cho tất cả, hay thêm một bước "ngập lụt"
nội dung AI khó kiểm chứng?

## Voice
ElevenLabs, giọng "Khánh Lâm - tin tức, thời sự" (`voice_id RCmOaM1iiIH5xX3QXjIF`), `model_id
eleven_v3`, speed ~1.09.

## Ghi chú kỹ thuật
- Không copy state file từ project cũ — `hyperframes init` mới.
- Style 10-stock-terminal (benchmark board): "câu chuyện" ở đây không phải benchmark hiệu năng
  thuần số như mô tả mẫu (dùng cho tin giá/benchmark) — diễn giải sáng tạo thành "bảng nâng cấp
  tính năng" kiểu terminal: mỗi tính năng cũ → mới hiển thị như 1 dòng mã / chỉ số trên bảng điều
  khiển (line-chart nhỏ chạy phía sau Data moment cho mốc "miễn phí / 1080p", cột bar cho Key facts
  mở rộng cảnh — chi tiết — mẫu dựng, sparkline cho Impact).
