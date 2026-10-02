# COMPLIANCE — gemini-4-argon-ky-su-hoai-nghi
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-10-02T01:30:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): GREEN
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh hero = og:image/ảnh báo thật từ Thanh Niên (?image=628b98c704e9, sự kiện Google I/O 'Ready, Set, I/O'), có dẫn nguồn trong Article Image Card; không chỉnh sửa/bịa nội dung ảnh; nhạc nền tự sinh qua Google Lyria (lyria-recipe.py, CALM preset, negative-prompt chặn vocal, không cần fallback ElevenLabs Music); SFX từ bộ chuẩn kênh (chime/click-soft/impact-bass/pop/whoosh); giọng đọc Vbee TTS AI narrator chung, không giả giọng người thật"
claims_verified:
  - "Google ra mắt Gemini 4 Argon ngày 30/9/2026, sau nhiều tháng trì hoãn — khớp ?article=628b98c704e9 (Thanh Niên, dẫn Bloomberg)"
  - "Google tuyên bố mô hình hiệu năng cao nhất từng xây dựng, vượt Astra (OpenAI) về bảo mật — khớp ?article=628b98c704e9 + đối chiếu ?article=bb05f9cea9ae (VnExpress, CWE-bench)"
  - "Theo Bloomberg, nhân viên Google nói mô hình kém hiệu quả hơn khi dùng thực tế, khó ở một số tác vụ lập trình — khớp ?article=628b98c704e9"
  - "Mỗi sản phẩm Google Search/Maps/Gmail/Chrome có hơn 1 tỷ người dùng — khớp ?article=628b98c704e9 nguyên văn"
  - "Jeff Dean, Sanjay Ghemawat, Oriol Vinyals, TS. Quốc Lê rời Google lập startup Discovery Loop tháng 7/2026 — khớp ?article=628b98c704e9 nguyên văn"
  - "Edwin Chen (nhà sáng lập Surge AI) nhận định ngành AI chạy theo điểm số benchmark hơn sản phẩm dễ dùng — khớp ?article=628b98c704e9, diễn giải đúng nghĩa gốc"
sensitive_flags: []
vietnam_legal_flags: []
notes: "Video kết hợp 2 nguồn báo VN hợp lệ (Thanh Niên chính + VnExpress đối chiếu số liệu benchmark), đều lấy qua endpoint ?article= được cấp phép, không WebFetch trực tiếp trang báo. Góc nhìn nguyên bản: không chỉ đọc lại tiêu đề mà tổng hợp mâu thuẫn tuyên bố-benchmark vs thực tế sử dụng + bối cảnh chảy máu chất xám + cảnh báo chuyên gia ngành — đạt B7. Render + verify 5 bước đều sạch (duration 59.9s, không khoảng lặng chết, loudnorm -14.0 LUFS/-2.2 dBTP sau 2-pass, cân bằng dọc xác nhận bằng frame thật, transcript khớp script câu-theo-câu qua Gemini STT fallback do ElevenLabs STT hết quota). Caption karaoke dùng Gemini fallback (ElevenLabs STT quota_exceeded) — ước lượng timing, không ảnh hưởng nội dung lời đọc thật (vẫn Vbee TTS)."
