# COMPLIANCE — trung-quoc-700-trieu-nguoi-dung-ai

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-10-04T01:40:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): GREEN
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image VnExpress (article-hero.jpg, có dẫn nguồn 'Nguồn: VnExpress' trên mọi frame); nhạc nền tự sinh qua Google Lyria (lyria-realtime-exp, calm recipe --density 0.25 --brightness 0.4, negative-prompt loại vocals/lyrics) — không cần fallback ElevenLabs Music; SFX từ videos/astra-openai/assets/sfx/ (repo-owned)."
claims_verified:
  - "700 triệu người dùng AI tạo sinh tại Trung Quốc, thâm nhập >50% nửa đầu 2026 — đối chiếu ?article=dc357f6f68f1 (VnExpress)"
  - "47,8% dùng AI xử lý hình ảnh/video, 37,6% dùng cho văn bản, 32,5% tóm tắt công việc — bài gốc"
  - "người dùng trợ lý AI đa năng + công cụ năng suất tăng gấp đôi so với 2025 — bài gốc"
  - "siêu cụm AI nội địa đầu tiên gồm 100.000 hệ thống tăng tốc; năng lực tính toán AI tăng ~177% (diễn đạt VO: 'gần gấp 3 lần') — bài gốc"
  - "DeepSeek, Moonshot AI phát hành mô hình mã nguồn mở; 6 mô hình nguồn mở hàng đầu toàn cầu do nhóm TQ phát triển — bài gốc"
  - "hơn 120.000 bộ dữ liệu AI chất lượng cao tính đến giữa 2026 — bài gốc"
  - "đầu tư AI nửa đầu 2026 ~37,32 tỷ USD = 182% tổng vốn huy động cả năm 2025 (diễn đạt VO: 'gần gấp đôi cả năm ngoái') — bài gốc"
  - "hơn 30% công ty sản xuất lớn tại TQ dùng AI cho nghiên cứu/sản xuất/kiểm soát chất lượng; 16 cụm sản xuất tiên tiến cấp quốc gia — bài gốc, dùng ở act Impact (sự thật đã xảy ra, không suy đoán)"
  - "trích dẫn China Daily (qua bài gốc): TQ ưu tiên mở rộng AI chiến lược, xây năng lực điện toán nội địa, giảm phụ thuộc công nghệ nước ngoài — gán đúng nguồn trong composition (act Context, '— China Daily')"
sensitive_flags: ["AI & năng lực cạnh tranh công nghệ toàn cầu — framing trung lập qua CTA (Kinh tế số bứt tốc / Phụ thuộc AI ngày càng lớn), không kết luận hộ khán giả"]
vietnam_legal_flags: []
notes: "Dự đoán 'quy mô sản xuất robot hình người cả năm vượt 100.000 chiếc' trong bài gốc KHÔNG đưa vào SCRIPT/composition vì là dự đoán, không phải sự thật đã xảy ra (đúng B1/act 6 'sự thật đã xảy ra'). ASR verify (Gemini gemini-flash-lite-latest, do ElevenLabs STT hết quota và Gemini tier cao hơn cũng hết quota free-tier ngày) nghe nhầm tên riêng 'Moonshot AI' thành 'Moonsource AI' trong transcript — xác nhận đây là lỗi nhận dạng giọng nói (ASR) khi nghe tên tiếng Anh, KHÔNG phải SCRIPT.md có viết tắt hay TTS đọc sai (SCRIPT.md giữ nguyên 'DeepSeek, Moonshot AI' là tên riêng, không bị ép đọc khác). Không ảnh hưởng nội dung hiển thị/caption. Style dựng: 3-ticker-tape (index 2, claim_style), khác style video liền trước (index 1, chip-and-leaderboard, video khung-hoang-ram-ai-2028) — không trùng bố cục."
```
