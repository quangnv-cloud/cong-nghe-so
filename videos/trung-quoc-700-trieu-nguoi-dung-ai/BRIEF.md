# BRIEF — Trung Quốc vượt mốc 700 triệu người dùng AI tạo sinh

## Nguồn
- VnExpress — "Người dùng AI tạo sinh vượt mốc 700 triệu tại Trung Quốc", 3-4/10/2026.
  https://vnexpress.net/nguoi-dung-ai-tao-sinh-vuot-moc-700-trieu-tai-trung-quoc-5127259.html
- Dẫn lại từ: Viện Chính sách và Hợp tác quốc tế (Trung tâm thông tin mạng Internet Trung Quốc) +
  China Daily.
- Ảnh: og:image của bài → `assets/img/article-hero.jpg` (lấy qua Apps Script `?image=`, có dẫn nguồn).
- id tin (Apps Script): `dc357f6f68f1`. Style claimed: index 2, `3-ticker-tape`.

## GATE A — sàng lọc chọn tin
Tin công nghệ/AI thông thường (số liệu thâm nhập thị trường, đầu tư, hạ tầng tính toán) — không
cáo buộc hình sự, không chính trị/bầu cử/xung đột, không y tế "thuốc thần", không tài chính "cam
kết lãi", không deepfake/phát ngôn giả, không nội dung khai thác trẻ em/bạo lực/lừa đảo.
→ **GREEN**, tiếp tục dựng.

## Số liệu / dữ kiện xác nhận (KHÔNG bịa thêm ngoài danh sách này — tất cả truy được về bài gốc)
- Trung Quốc là nước đầu tiên có số người dùng AI tạo sinh vượt **700 triệu** trong nửa đầu 2026,
  tỷ lệ thâm nhập hơn **50%**.
- Trong đó: **47,8%** dùng AI tạo sinh xử lý hình ảnh/video, **37,6%** cho văn bản, **32,5%** để
  tóm tắt công việc/biên bản/slide. Người dùng trợ lý AI đa năng + công cụ năng suất **tăng gấp đôi**
  so với 2025.
- Trung Quốc ưu tiên mở rộng ngành AI chiến lược, xây năng lực điện toán nội địa, giảm phụ thuộc
  công nghệ nước ngoài (theo China Daily).
- Hơn **30%** công ty sản xuất lớn dùng AI (nghiên cứu/thiết kế, sản xuất, kiểm tra chất lượng,
  bảo trì). Đến cuối tháng 6: **16 cụm** sản xuất tiên tiến cấp quốc gia (mạch tích hợp + AI).
- Năng lực tính toán AI đạt **2.185 EFLOPS** tính đến cuối tháng 6, **tăng 177%** so với cùng kỳ
  năm ngoái. Nửa đầu năm: vận hành siêu cụm AI tự phát triển đầu tiên gồm **100.000 hệ thống tăng
  tốc**, toàn bộ chip/điện toán/lưu trữ/mạng/làm mát công nghệ trong nước.
- Công ty nội địa (DeepSeek, Moonshot AI) phát hành nhiều mô hình mã nguồn mở; **6 mô hình** nguồn
  mở hàng đầu bảng xếp hạng toàn cầu đều do nhóm nghiên cứu Trung Quốc phát triển.
- Hơn **120.000 bộ dữ liệu** chất lượng cao tính đến giữa 2026. Embodied AI: hơn **400 model**
  robot hình người mới, quy mô sản xuất cả năm dự đoán vượt **100.000 chiếc**.
- Đầu tư: **1.255 giao dịch** đầu tư/tài chính liên quan AI nửa đầu 2026 = **78%** tổng giao dịch
  cả năm 2025. Tổng giao dịch ~**250,14 tỷ nhân dân tệ (37,32 tỷ USD)** = **182%** số tiền huy động
  được cả năm ngoái (tức đã vượt tổng năm 2025 gần gấp đôi chỉ trong 6 tháng).

## Góc tranh luận (CTA)
Tốc độ phổ cập AI tại Trung Quốc nhanh chưa từng thấy — bước tiến đáng mừng cho kinh tế số, hay
lời nhắc về khoảng cách công nghệ/sự phụ thuộc AI ngày càng lớn? (được/mất — bước tiến/mối lo).
Framing trung lập, không chốt kết luận hộ người xem — đúng GATE B (B1, B7).

## Cấu trúc 7 act (giữ khung: Hook → What happened → Key facts → Data moment → Context → Impact → CTA)
- Act 6 (Impact) là SỰ THẬT đã xảy ra (hơn 30% công ty sản xuất lớn đã dùng AI, 16 cụm sản xuất
  tiên tiến đã hình thành) — không suy đoán tương lai.
- `data-duration` mỗi frame = độ dài voice thật (ffprobe) + ~0.3-0.5s đệm.
- Style dựng: **3-ticker-tape** (dải release-feed/changelog kiểu terminal) — xem CONSTRUCTION-STYLES.md.

## Voice
**Vbee TTS** (đổi từ ElevenLabs 2026-09-30), giọng **"HN - Ngọc Huyền"**
(`voice_code: hn_female_ngochuyen_full_48k-fhg`), `speed_rate: 1.09`. Endpoint
`POST https://vbee.vn/api/v1/tts` (API legacy), key `VBEE_APP_ID` / `VBEE_TOKEN`.

## Tiêu đề tin (dùng cho FB/YouTube)
"Trung Quốc Vượt Mốc 700 Triệu Người Dùng AI Tạo Sinh"
