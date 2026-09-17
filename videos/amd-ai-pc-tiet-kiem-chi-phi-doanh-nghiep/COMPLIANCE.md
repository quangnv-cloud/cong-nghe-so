# COMPLIANCE — amd-ai-pc-tiet-kiem-chi-phi-doanh-nghiep
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-16T14:30:00+07:00
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): GREEN
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "Ảnh Hook/Article Image Card = og:image bài GenK (đại diện AMD APAC), dẫn nguồn rõ trên badge 'Nguồn: GenK'; không watermark, không chỉnh sửa nội dung ảnh. Nhạc nền Lyria tự sinh (calm ambient, instrumental). SFX từ bộ SFX repo. Video 100% tự dựng, không reup."
claims_verified:
  - "53% lãnh đạo doanh nghiệp châu Á - Thái Bình Dương dùng AI agent (Microsoft Work Trend Index 2025) — đối chiếu article_full.txt, khớp"
  - "46% mức trung bình toàn cầu — đối chiếu article_full.txt, khớp"
  - "Đội 500 AI PC, xử lý một nửa cục bộ / một nửa cloud, tiết kiệm 40-60% chi phí hạ tầng trong 3 năm (phân tích AMD) — đối chiếu article_full.txt, khớp"
  - "Hơn 143 triệu AI PC dự kiến xuất xưởng 2026, ~55% thị trường PC toàn cầu (Gartner) — đối chiếu article_full.txt, khớp"
  - "Phát ngôn ông Alexey Navolokin, Tổng giám đốc AMD châu Á - Thái Bình Dương, trả lời GenK — đối chiếu article_full.txt, khớp"
  - "Ba lớp phần cứng CPU/GPU/NPU và dòng sản phẩm Ryzen AI / EPYC / Instinct theo AMD — đối chiếu article_full.txt, khớp"
sensitive_flags: []
vietnam_legal_flags: []
notes: "Tin công nghệ/doanh nghiệp thông thường (ra mắt phân tích chi phí + khảo sát ngành), không chạm chính trị/y tế/tài chính rủi ro/deepfake. Act 6 (Impact) chỉ nêu sự thật đã xảy ra (dịch chuyển cách lập ngân sách + khuyến nghị hybrid của AMD), không suy đoán tương lai. Act 7 CTA là câu hỏi tranh luận thật bám tin (tiết kiệm thật hay bài toán trên giấy), có 2 lựa chọn đối lập, không đề cập tên kênh trong voice. Style dựng '3-ticker-tape' (index 2) khác các video gần nhất (index 9, 0, 1) — không trùng bố cục. Verify bước 10: (1) ffprobe duration 65.97s khớp thiết kế 65.95s, dưới trần 75s; (2) silencedetect chỉ phát hiện khoảng lặng cuối video (65.32-65.96s, đúng fade-out sau voice cuối), không có khoảng lặng chết giữa video; (3) đã trích 8 frame trải đều 7 act + soát cân bằng dọc, không phần tử bịa, logo/nguồn hiện đủ mọi frame; (4) transcript verify: Whisper local bị chặn (HTTP 403 tải model, đúng như dự kiến sandbox); fallback Gemini multimodal theo đúng quy trình — endpoint /v1beta/models liệt kê model khả dụng, models/gemini-2.5-flash và models/gemini-2.5-flash-lite đã bị khai tử cho key này (404), models/gemini-flash-latest bị quá tải 503/timeout sau 4 lần thử; thành công với models/gemini-flash-lite-latest và models/gemini-3.5-flash-lite (2 lần độc lập, kết quả nhất quán) — transcript khớp SCRIPT.md từng câu, không có câu nào 'chế thêm' khi sinh voice, chỉ khác cách STT tách câu 7 thành 2 dòng (không đổi nội dung) và biến thể chính tả phiên âm tên riêng 'Navolokin' (không ảnh hưởng nội dung)."
