# COMPLIANCE — openai-doc-hoi-thoai-nguoi-dung

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-17T07:40:00Z
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
notes: "Style dựng: 5-map-and-geo (index 4, claim_style). Vì tin không có yếu tố địa lý cụ thể, đã diễn giải sáng tạo ẩn dụ 'bản đồ' thành bản đồ/mạng lưới ngành công nghệ (OpenAI – Gemini – Anthropic là các node trên mạng lưới), đúng tinh thần 'ẩn dụ hình ảnh, không phải màu mới' của CONSTRUCTION-STYLES.md. Góc nhìn riêng (B7): trình bày dữ liệu qua ẩn dụ bản đồ ngành + timeline 'nội bộ → bị phanh phui' + 2 thẻ tác động, không chỉ đọc lại tiêu đề báo. Render lần 2 sau khi merge origin/master phát hiện 2 chuẩn mới (docs 2026-09-16): áp dụng đủ mục 'Kỹ thuật hình ảnh nâng cao' (nền có chiều sâu blob+sao PRNG seed cố định, glow brand-color trên mọi card/badge/pin, caption karaoke 62 chunk / 236 từ đồng bộ ElevenLabs STT scribe_v1 word-timestamps — text hiển thị lấy từ SCRIPT.md gốc đối chiếu 1:1 với STT, không dùng text ASR để tránh lỗi chính tả) và 'Chuẩn xuất bản video' (1080x1920/30fps, render --quality high --video-bitrate 10M --browser-timeout 60, loudness đo được -14.8 LUFS / True Peak -1.1 dBTP, trong ngưỡng ±1 LU / ≤-1.0 dBTP)."
```

## Chi tiết kiểm tra GATE C

- Thumbnail (`output/thumbnail.jpg`, trích tại t=3.5s trong cửa sổ Hook, render lần 2) xem lại bằng Read: logo + tên kênh "Công Nghệ Số" (góc trên-trái panel dưới), badge nguồn "Nguồn: VnExpress · 17/9/2026", tiêu đề "Project Lily" rõ to, 2 tag tương phản "Con người đọc" (xanh) / "Rủi ro riêng tư" (cam) — đều hiện đủ, rõ, không mờ/cắt. Caption karaoke "hội thoại thật của" hiện ở dải dưới, không che các phần tử bắt buộc.
- Đã xem 7/7 frame cuối mỗi act (t = 4, 8.5, 19.0, 31.3, 36.2, 46.9, 59.6, 69.5s) qua Read trên bản render lần 2 — không phần tử bịa, đúng B6, cân bằng dọc đạt (nội dung mỗi act kết thúc trong khoảng top ~1420–1590px, không trống đen quá nửa dưới); glow brand-color + nền chiều sâu (blob mờ + sao PRNG) hiển thị đúng trên mọi frame, không phát sinh khung hình đen (đã quét thêm 15 mốc rải đều 1–69s để loại trừ rủi ro "composition_heavy_overlay_count_high" mà `npx hyperframes check` cảnh báo — không mốc nào đen/lỗi).
- Transcript (Gemini `gemini-flash-lite-latest`, audio 16kHz mono trích từ file render thật) khớp gần như nguyên văn `SCRIPT.md` — không câu nào "chế thêm". Sai khác duy nhất: 1 từ ASR nghe nhầm "biểu tượng" → "điệu tượng" (lỗi nhận dạng giọng nói, không phải lỗi phát âm TTS hay viết tắt); "50" được ASR chuẩn hoá thành số thay vì "năm mươi"; "ChatGPT" tách thành "chat GPT" — đều là biến thể ASR bình thường, không ảnh hưởng nội dung. Word-level timestamps từ cùng lần STT này (scribe_v1) đối chiếu 1:1 số từ với SCRIPT.md ở cả 7 dòng — dùng để build caption karaoke, text hiển thị lấy nguyên văn SCRIPT.md (không lấy text ASR).
- Caption dùng để đăng = `CAPTION.md` (phần trên dấu `---`), đã qua GATE B, không sửa tay thêm claim mới.
- `npx hyperframes check` (render lần 2): 0 error, 64 warning (studio_missing_editable_id trên các caption-chunk div — chỉ ảnh hưởng UX Studio, không ảnh hưởng render; container_overflow đã gắn `data-layout-allow-overflow` cho 3 blob nền — tràn có chủ đích để tạo hiệu ứng mờ mềm; timeline_track_too_dense/composition_heavy_overlay_count_high — đã xác nhận bằng tay không gây khung hình đen qua quét 15+ mốc thời gian thực tế), 0 lint error, 55/55 (rồi 67/67 trước khi thêm glow) contrast checks pass WCAG AA.
