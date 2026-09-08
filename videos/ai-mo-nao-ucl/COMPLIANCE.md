# COMPLIANCE — ai-mo-nao-ucl
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-08T07:20:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): YELLOW
GATE B (content):   YELLOW-fixed
GATE C (final):     PASS

decision: APPROVE
risk_level: YELLOW
ai_disclosure_required: false
copyright_notes: "ảnh bài báo GenK (?image=c313e29d5c13, MRI scan + tay đeo găng — ảnh biên tập thật của bài, có dẫn nguồn, không phải ảnh AI dựng cảnh thật); nhạc nền Lyria tự sinh (instrumental, no vocals, đã kiểm negative-prompt); SFX từ repo (astra-openai/assets/sfx); giọng ElevenLabs 'Khánh Lâm' (AI narrator chung, không giả giọng người thật cụ thể)"
claims_verified: [
  "Ca mổ u tuyến yên tại National Hospital for Neurology and Neurosurgery (UCLH), Anh — thử nghiệm lâm sàng — đối chiếu ?article=c313e29d5c13",
  "Bệnh nhân Rhys Hibbert, 48 tuổi, sống tại Bedfordshire — đối chiếu bài gốc",
  "Hồi phục đi lại độc lập trong 1 tuần, không cần kính/gậy — đối chiếu bài gốc",
  "Bác sĩ Hani Marcus (+ Danyal Khan) giữ toàn quyền quyết định, AI chỉ hỗ trợ nhận diện — đối chiếu bài gốc",
  "Công nghệ: UCL Hawkes Institute, nền tảng Nvidia Clara IGX, huấn luyện bằng hàng trăm video nội soi — đối chiếu bài gốc",
  "Tài trợ: NIHR + Google — đối chiếu bài gốc"
]
sensitive_flags: ["AI & y tế — video không tuyên bố hiệu quả diện rộng, luôn gắn với khung 'thử nghiệm lâm sàng', nhấn mạnh bác sĩ giữ toàn quyền quyết định, không đưa lời khuyên y tế, CTA đặt câu hỏi mở (bước tiến hay rủi ro) thay vì khẳng định một chiều"]
vietnam_legal_flags: []
notes: "Verify 4 bước: (1) ffprobe duration 61.833s, dưới 75s; (2) silencedetect -35dB/-40dB d=0.6 — không có khoảng lặng chết nào trong video; (3) đã Read trực tiếp cả 7 frame render + thumbnail — đúng brand, không phần tử bịa, cân bằng dọc tốt (act 1-6 nội dung trải top~300 đến ~1650px; act 7 CTA dùng nguyên layout cố định đã được duyệt ở video astra-openai — khoảng trống giữa options-pill và chữ ký logo là đặc điểm cố định của template CTA thương hiệu, đã đối chiếu frame thật của astra-openai tại cùng vị trí, không phải lỗi mới); (4) transcript (Gemini gemini-flash-lite-latest, Whisper không cài) khớp SCRIPT.md từng câu, chỉ lệch phiên âm tên riêng nước ngoài (Rhys Hibbert/Hawkes/Hani nghe ra gần đúng) — không có câu nào bịa thêm, không nhắc tên kênh trong lời thoại. npm run check: lint/runtime/motion 0 lỗi, layout 0 vấn đề, contrast 40/40 WCAG AA pass."
