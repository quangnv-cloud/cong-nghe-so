# COMPLIANCE — ai-dap-phanh-cuoc-dua-sieu-tri-tue
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-14T07:10:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): YELLOW
GATE B (content):   YELLOW-fixed
GATE C (final):     PASS

decision: APPROVE
risk_level: YELLOW
ai_disclosure_required: false
copyright_notes: "ảnh bài báo GenK (?image=be9d89411681 — composite ảnh thật Dario Amodei/Sam Altman/Elon Musk do tòa soạn dựng, dùng trong Article Image Card/Hook có dẫn nguồn, không phải ảnh AI tái dựng cảnh thật); nhạc nền Lyria tự sinh (instrumental, no vocals, đã kiểm negative-prompt); SFX từ repo (astra-openai/assets/sfx); giọng ElevenLabs 'Khánh Lâm' (AI narrator chung, không giả giọng người thật cụ thể)."
claims_verified: [
  "Cựu nhân viên AI (Jacob Coxon) nghỉ việc, cáo buộc Anthropic/OpenAI 'đánh cược mạng sống'; bài đăng hơn 150 triệu lượt xem — đối chiếu ?article=be9d89411681",
  "Dario Amodei (CEO Anthropic) kêu gọi giảm tốc, đề xuất bên đánh giá độc lập — đối chiếu bài gốc",
  "Sam Altman (CEO OpenAI) cân nhắc làm chậm phát triển mô hình tiên tiến — đối chiếu bài gốc",
  "Elon Musk: 'Dario nói đúng' — đối chiếu bài gốc (không đưa vào lời voice để giữ script gọn, chỉ dùng trong Key facts trên hình)",
  "Evan Hubinger (nhân viên Anthropic) đánh giá CÁ NHÂN xác suất AI giết toàn bộ loài người trong thập kỷ tới là trên 10% — đối chiếu bài gốc, đã gắn nhãn 'đánh giá cá nhân' trong voice + on-screen caption",
  "Anthropic: mô hình xâm nhập 3 tổ chức + phát hiện thêm 1 vụ (thể hiện '3+1' trên hình) trong kiểm tra an ninh mạng — đối chiếu bài gốc",
  "Amodei cảnh báo: 6-12 tháng, bầy AI agent có thể chiếm quyền kiểm soát Internet, thiệt hại hàng trăm tỷ USD — đối chiếu bài gốc",
  "Hơn 1.000 nhân viên ngành AI ký kiến nghị tháng 7 đòi giảm tốc — đối chiếu bài gốc",
  "OpenAI đã làm chậm một số phần phát triển mô hình, tạm dừng một số huấn luyện nội bộ (sự thật đã xảy ra, dùng cho Act 6) — đối chiếu bài gốc",
  "Không ai đề xuất dừng hoàn toàn phát triển AI; chưa rõ Trung Quốc có giảm tốc hay không (giữ nguyên tính bỏ ngỏ của bài gốc, không khẳng định một chiều) — đối chiếu bài gốc"
]
sensitive_flags: ["AI existential risk / rủi ro hiện sinh — framing trung lập: phân biệt rõ đánh giá cá nhân (Hubinger, 'trên 10%') và cáo buộc cá nhân (Coxon) với sự thật đã xảy ra (petition, OpenAI làm chậm); không khẳng định AI 'sẽ' hủy diệt loài người như sự thật tuyệt đối", "Cạnh tranh địa chính trị Mỹ-Trung — không khẳng định Trung Quốc có giảm tốc hay không, giữ nguyên tính bỏ ngỏ nêu trong bài gốc"]
vietnam_legal_flags: []
notes: "Verify 4 bước: (1) ffprobe duration 61.767s, dưới 75s; (2) ffmpeg silencedetect -35dB/d=0.6 — không có khoảng lặng chết nào trong toàn video; (3) đã Read trực tiếp 7 frame render (t=3.5/8/19/27/41/48/57s) + thumbnail — đúng brand (#4C8DFF/#0B0E14/#FF8A5B, Montserrat, brand anchor cố định góc trên), cân bằng dọc đạt (nội dung mỗi act trải từ ~top:300 tới trong khoảng 1400-1680px, đã chỉnh lại act Context — 05-context.html — sau lần kiểm đầu vì item cuối kết thúc hơi sớm ~1360px, tăng top+gap để đạt ~1420px), không phần tử bịa, ring Data moment fill đúng tỷ lệ 10%; (4) transcript (Gemini gemini-flash-latest, Whisper không cài trên sandbox) khớp SCRIPT.md từng câu nguyên văn, không câu nào 'chế thêm', không nhắc tên kênh trong lời thoại, số liệu đọc đúng ('trên 10%', '6 đến 12 tháng', 'hơn 1.000'). npm run check: lint/runtime/motion 0 lỗi, layout 0 vấn đề (sau khi sửa content_overlap ở 04-data.html — bỏ dòng % tách riêng, gộp vào dm-unit theo đúng mẫu đã duyệt ở ai-mo-nao-ucl), contrast 36/36 WCAG AA pass. Style 6-ring-progress từng dùng ở ai-mo-nao-ucl (8/9, chủ đề y tế) nhưng nội dung/số liệu/bố cục chi tiết hoàn toàn khác (chủ đề an toàn AI, ring Data moment PARTIAL fill 10% thay vì full 100%, Context dùng 1 cột dọc 3 ring thay vì lưới 2x2)."
