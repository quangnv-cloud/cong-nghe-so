# COMPLIANCE — khung-hoang-ram-ai-2028
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-10-03T01:40:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): GREEN
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh hero = ảnh thật/og:image từ Dân Trí (?image=0a8618713eb9, module RAM/bo mạch), có dẫn nguồn trong Article Image Card và Brand Anchor; không chỉnh sửa/bịa nội dung ảnh; nhạc nền tự sinh qua Google Lyria (lyria-recipe.py, CALM preset --density 0.25 --brightness 0.4, negative-prompt chặn vocal, thành công lần thử đầu, KHÔNG cần fallback ElevenLabs Music); SFX từ bộ chuẩn kênh (chime/click-soft/impact-bass/pop/whoosh); giọng đọc Vbee TTS (giọng HN - Ngọc Huyền) AI narrator chung, không giả giọng người thật; mọi đồ hoạ Data moment/Context/Impact đều là CSS/motion graphics tự dựng (thanh so sánh, icon, số liệu) — không dùng AI tái tạo cảnh thật/người thật như ảnh chụp."
claims_verified:
  - "Micron (một trong những hãng chip nhớ lớn nhất thế giới) cảnh báo thiếu hụt RAM giai đoạn 2027-2028 nghiêm trọng hơn cả 2026 — khớp ?article=0a8618713eb9 (Dân Trí, dẫn TechRadar/Micron)"
  - "Nguyên nhân: trung tâm dữ liệu trí tuệ nhân tạo gom mua bộ nhớ quy mô lớn — khớp nguyên văn nguồn"
  - "Hơn 75% sản lượng dự kiến năm 2027 của Micron đã được khách hàng cam kết mua — khớp nguyên văn nguồn"
  - "Robot hình người tương lai có thể cần hơn 200GB RAM, cao gấp nhiều lần mức 8-16GB phổ biến trên laptop — khớp nguyên văn nguồn; nêu rõ đây là dự báo (không phải cấu hình phổ biến hiện tại), robot có thể thành thị trường bộ nhớ quan trọng vào 2030 — giữ đúng tính dự báo của nguồn"
  - "Xây nhà máy chip nhớ mới mất nhiều năm, Micron chưa thể xác định khi nào thị trường bộ nhớ cân bằng trở lại — khớp nguyên văn nguồn"
  - "CEO Apple Tim Cook xác nhận hãng có kế hoạch tăng giá một số sản phẩm để bù chi phí bộ nhớ leo thang — khớp nguồn; KHÔNG gán cụ thể cho model iPhone 18 Pro Max vì nguồn chỉ nêu khả năng chung ('có thể') cho riêng chi tiết đó — act Impact chỉ dùng phần CEO đã phát biểu (sự thật đã xảy ra), không dùng phần suy đoán"
  - "Phân khúc laptop giá rẻ đối mặt nguy cơ đội giá — giữ nguyên tính dự báo ('có thể chịu sức ép') của nguồn, không chốt như sự thật tuyệt đối"
sensitive_flags: []
vietnam_legal_flags: []
notes: "Nguồn chính + duy nhất: Dân Trí (dẫn TechRadar/Micron), lấy qua endpoint ?article= được cấp phép, không WebFetch trực tiếp. Góc nhìn nguyên bản (B7): tổng hợp dữ liệu thành biểu đồ so sánh leaderboard (laptop 8-16GB vs robot >200GB) không có trong bài gốc, đóng khung rõ góc tranh luận 'AI bùng nổ vs người dùng chịu giá tăng' — không chỉ đọc lại tiêu đề báo. Style dựng: index 1 'Chip & Leaderboard' (claim_style), khác style 5 video gần nhất (1-card-and-bar, 9-editorial-clipping, 7-timeline-chronology, 6-ring-progress, ...). Render + verify 5 bước đều sạch: duration 63.5s, không khoảng lặng chết (silencedetect sạch), loudness -14.0 LUFS / True Peak -1.1 dBTP sau loudnorm 2-pass (input gốc -15.1 LUFS lệch hơn ±1 LU nên đã sửa), cân bằng dọc xác nhận bằng frame thật render cho cả 7 act (phần tử cuối mỗi act đều kết thúc trong khoảng top 1400-1680px, không trống đen nửa dưới), transcript (Gemini multimodal, model gemini-flash-lite-latest — ElevenLabs STT hết quota 0 credit, model gemini-flash-latest/gemini-3.8-flash cũng hết quota free-tier 20/ngày) khớp SCRIPT.md câu-theo-câu, chỉ lệch vài âm gần giống chấp nhận được (RAM nghe thành 'giam', khổng lồ thành 'khủng lồ' — không đổi nghĩa, không câu nào bị chế thêm/bớt). Caption karaoke: word-timestamp lấy qua Gemini multimodal fallback (model gemini-flash-lite-latest, do ElevenLabs STT hết quota và model gemini-flash-latest cũng hết quota free-tier) cho cả 7 dòng — đã rà lại content_overlap giữa các caption chunk (còn 4 info-level không đáng kể, không phải lỗi). BGM: Lyria thành công ngay lần thử đầu tiên, không cần fallback ElevenLabs Music."
