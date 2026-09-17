# COMPLIANCE — openai-doc-hoi-thoai-nguoi-dung

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-17T07:20:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): YELLOW
GATE B (content):   YELLOW-fixed
GATE C (final):     PASS

decision: APPROVE
risk_level: YELLOW
ai_disclosure_required: false
copyright_notes: "Ảnh Hook/Article Image Card = ảnh thật từ bài báo VnExpress (lấy qua ?image=<id>, ảnh chụp điện thoại mở ChatGPT), có dẫn nguồn — không watermark, không chỉnh sửa nội dung. Nhạc nền tự sinh qua Google Lyria (calm ambient, không lời, không vocal). SFX từ thư viện dùng chung của kênh (videos/astra-openai/assets/sfx, copy nguyên văn). Không có yếu tố bản quyền bên thứ ba nào khác."
claims_verified:
  - "Dự án nội bộ bí mật 'Project Lily' — theo điều tra của 404 Media (bài gốc VnExpress)"
  - "OpenAI thuê hàng trăm người đọc hội thoại thật của người dùng ChatGPT để chấm điểm câu trả lời — bài gốc"
  - "Thù lao hơn 50 đô la Mỹ mỗi giờ — bài gốc"
  - "Tiêu chí chấm điểm: bỏ giọng văn máy móc / biểu tượng cảm xúc thừa / thái độ nịnh hót; ChatGPT không xưng 'tôi' kiểu nhân hoá — bài gốc"
  - "Quy tắc hướng dẫn liên tục thay đổi, có lúc mâu thuẫn (lời một người tham gia dự án) — bài gốc"
  - "Hội thoại qua bước 'làm sạch và ẩn danh'; OpenAI thừa nhận bộ lọc vẫn có thể để lọt dữ liệu cá nhân, nhất là đoạn chat ngắn — bài gốc"
  - "Tính năng 'Cho phép dùng dữ liệu cải thiện sản phẩm' mặc định bật sẵn trên hầu hết dịch vụ, kể cả gói trả phí; tắt đi không hồi tố dữ liệu đã thu thập — bài gốc"
  - "Theo Tom's Hardware: Gemini (Google) và Anthropic cũng công khai chính sách con người có thể xem lại một số đoạn chat đã lưu — bài gốc"
sensitive_flags:
  - "Quyền riêng tư dữ liệu người dùng — xử lý bằng framing trung lập ('được cho là', 'theo điều tra của 404 Media', 'OpenAI thừa nhận'); không kết luận OpenAI vi phạm tuyệt đối; không bịa số liệu ngoài bài gốc"
vietnam_legal_flags:
  - "Chạm yếu tố dữ liệu cá nhân / quyền riêng tư người dùng dịch vụ trí tuệ nhân tạo — nội dung chỉ tường thuật lại điều tra báo chí đã công bố (VnExpress dẫn 404 Media), không tự đưa ra kết luận pháp lý, không bịa số điều luật. Khuyến nghị theo dõi nguồn chính thức nếu có diễn biến mới."
notes: "Style dựng: 5-map-and-geo (index 4, claim_style). Vì tin không có yếu tố địa lý cụ thể, đã diễn giải sáng tạo ẩn dụ 'bản đồ' thành bản đồ/mạng lưới ngành công nghệ (OpenAI – Gemini – Anthropic là các node trên mạng lưới), đúng tinh thần 'ẩn dụ hình ảnh, không phải màu mới' của CONSTRUCTION-STYLES.md. Góc nhìn riêng (B7): trình bày dữ liệu qua ẩn dụ bản đồ ngành + timeline 'nội bộ → bị phanh phui' + 2 thẻ tác động, không chỉ đọc lại tiêu đề báo."
```

## Chi tiết kiểm tra GATE C

- Thumbnail (`output/thumbnail.jpg`, trích tại t=3.5s trong cửa sổ Hook) xem lại bằng Read: logo + tên kênh "Công Nghệ Số" (góc trên-trái panel dưới), badge nguồn "Nguồn: VnExpress · 17/9/2026", tiêu đề "Project Lily" rõ to, 2 tag tương phản "Con người đọc" (xanh) / "Rủi ro riêng tư" (cam) — đều hiện đủ, rõ, không mờ/cắt.
- Đã xem 7/7 frame cuối mỗi act (t = 4, 8.5, 19.0, 31.3, 36.2, 46.9, 59.6, 69.5s) qua Read — không phần tử bịa, đúng B6, cân bằng dọc đạt (nội dung mỗi act kết thúc trong khoảng top ~1420–1590px, không trống đen quá nửa dưới).
- Transcript (Gemini `gemini-flash-lite-latest`, audio 16kHz mono trích từ file render thật) khớp gần như nguyên văn `SCRIPT.md` — không câu nào "chế thêm". Sai khác duy nhất: 1 từ ASR nghe nhầm "biểu tượng" → "điệu tượng" (lỗi nhận dạng giọng nói, không phải lỗi phát âm TTS hay viết tắt); "50" được ASR chuẩn hoá thành số thay vì "năm mươi"; "ChatGPT" tách thành "chat GPT" — đều là biến thể ASR bình thường, không ảnh hưởng nội dung.
- Caption dùng để đăng = `CAPTION.md` (phần trên dấu `---`), đã qua GATE B, không sửa tay thêm claim mới.
