# COMPLIANCE — gpt6-astra-tranh-cai
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-07T13:40:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): YELLOW
GATE B (content):   YELLOW-fixed
GATE C (final):     PASS

decision: APPROVE
risk_level: YELLOW
ai_disclosure_required: false
copyright_notes: "Ảnh Hook/Article Image Card = ảnh biên tập gốc từ bài VnExpress (ok:true qua ?image=f37b2330cded, có watermark VNEXPRESS, không chỉnh sửa nội dung); nhạc nền sinh bằng Google Lyria (calm ambient, instrumental, negative-prompt loại vocal), không lời, sở hữu của dự án; SFX từ palette repo (chime/impact-bass/whoosh, dùng nguyên bản không đổi tốc độ/pitch)."
claims_verified:
  - "GPT-6 Astra ra mắt 3/9/2026, OpenAI tự nhận đạt AGI — đối chiếu ?article=f37b2330cded"
  - "72,6% OSWorld 2.0 — đối chiếu bài gốc"
  - "Nhanh hơn 47% so với GPT-5.6 Sol — đối chiếu bài gốc"
  - "100% ExploitBench, phát hiện 2 lỗ hổng zero-day — đối chiếu bài gốc"
  - "AII: Astra 61,2 / Sol 60,9 / Claude Fable 5.1 65,7 điểm — đối chiếu bài gốc"
  - "Giá Astra gấp 2,5 lần Sol — đối chiếu bài gốc"
  - "Kỹ thuật 'độ sâu lặp lại' (recurrent depth) khiến giám sát CoT khó hơn — đối chiếu bài gốc"
  - "Phát biểu Buck Shlegeris (Redwood Research), Zvi Mowshowitz, Ryan Greenblatt trên X — đối chiếu bài gốc, trích dẫn nguyên nghĩa không thêm kết luận"
sensitive_flags:
  - "AI an toàn / lo ngại mất khả năng giám sát mô hình — framing trung lập: trình bày cả hai phía (OpenAI/Nvidia CEO ca ngợi AGI vs giới an toàn AI cảnh báo), dẫn nguyên phát biểu chuyên gia thay vì kết luận thay, không tuyên bố thảm hoạ chắc chắn xảy ra."
vietnam_legal_flags: []
notes: "Tin quốc tế qua góc nhìn báo VN (VnExpress, nguồn category=vn, không cần dịch). Video có góc phân tích riêng (so sánh AII 3 model, đối chiếu điểm sáng tạo/giá) chứ không chỉ đọc lại tiêu đề báo (B7). Style dựng: 3-ticker-tape (index 2, claim_state 2026-09-07T13:11:21Z). Verify 4 bước: (1) ffprobe duration=72.80s khớp thiết kế; (2) silencedetect noise=-35dB d=0.6 không phát hiện khoảng lặng; (3) trích + soát 7 frame qua Read — đúng brand, cân bằng dọc, không phần tử bịa; (4) transcript Gemini flash-latest khớp SCRIPT.md nguyên văn, chỉ lệch phiên âm gần giống 'Sol'→'Son' (chấp nhận được theo quy định), không có câu nào bị chế thêm."
