# COMPLIANCE — robot-bieu-tinh-ba-lan
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-15T01:12:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): YELLOW
GATE B (content):   YELLOW-fixed
GATE C (final):     PASS

decision: APPROVE
risk_level: YELLOW
ai_disclosure_required: false
copyright_notes: "ảnh thật từ bài báo GenK (?image=dce8b01d93d0 — ảnh chụp thật sự kiện robot cầm biểu ngữ trước trụ sở chính phủ Ba Lan), dùng trong Hook + Article Image Card (Act 2), có dẫn nguồn 'Nguồn: GenK'; không phải ảnh AI tái dựng cảnh thật. Nhạc nền Lyria tự sinh (instrumental, no vocals, đã kiểm negative-prompt). SFX từ repo (astra-openai/assets/sfx, dùng lại nguyên bản không chỉnh tốc độ/pitch). Giọng ElevenLabs 'Khánh Lâm' (AI narrator chung, không giả giọng người thật cụ thể)."
claims_verified: [
  "Khoảng 30 robot hình người và robot bốn chân xuất hiện trước trụ sở Bộ Các vấn đề Kỹ thuật số Ba Lan, cầm biểu ngữ, phát khẩu hiệu qua loa — đối chiếu ?article=dce8b01d93d0",
  "Khẩu hiệu: 'Chúng tôi muốn quy định, chúng tôi muốn luật lệ' / 'Đừng chờ đợi, hãy quản lý và bảo vệ việc làm' — đối chiếu bài gốc",
  "Sự kiện do tổ chức vận động xã hội Democratism dàn dựng, người tổ chức Grzegorz Kuliś — đối chiếu bài gốc",
  "Khẩu hiệu ghi âm sẵn, robot do con người điều khiển tại hiện trường (đây là màn dàn dựng công khai, KHÔNG phải robot tự hành động) — đối chiếu bài gốc, nêu rõ trong Key facts để tránh hiểu lầm",
  "Quote Kuliś: 'Nếu chúng ta không phản ứng ngay bây giờ, vấn đề có thể sớm xuất hiện' — có trong bài gốc (không đưa vào voice để giữ script gọn, ý được diễn giải qua Key facts)",
  "CEO hãng chip Arm dự báo robot AI có thể thay thế phần lớn công nhân nhà máy trong 5-10 năm tới — đối chiếu bài gốc, gắn nhãn RÕ RÀNG là 'dự báo — chưa xảy ra' trong Data moment, không lẫn với sự thật đã xảy ra",
  "Amazon dùng robot kho hàng nhiều năm; BMW lên kế hoạch đưa robot hình người của Figure vào dây chuyền sản xuất; đề xuất robot tại Hyundai khiến công đoàn cảnh báo 'cú sốc việc làm' — đối chiếu bài gốc, dùng cho Context (sự thật nền, không suy đoán)",
  "Act 6 (Impact, sự thật đã xảy ra không suy đoán): hình ảnh cuộc biểu tình đã lan truyền toàn cầu, khơi dậy tranh luận công khai về AI và việc làm; nhiều công ty công nghệ đã cắt giảm hàng chục nghìn vị trí khi dồn nguồn lực sang AI — đối chiếu bài gốc"
]
sensitive_flags: ["AI & việc làm — framing trung lập: phân biệt rõ dự báo (CEO Arm, '5-10 năm') với sự thật đã xảy ra (lan truyền toàn cầu, cắt giảm nhân sự); nêu rõ sự kiện robot là màn dàn dựng truyền thông có chủ đích (Democratism), không phải robot tự hành động/nổi dậy, tránh hiểu lầm gây hoang mang"]
vietnam_legal_flags: []
notes: "Verify 4 bước: (1) ffprobe duration 67.80s, dưới 75s; (2) ffmpeg silencedetect -35dB/d=0.6 — không phát hiện khoảng lặng chết nào; (3) đã Read trực tiếp 7 frame render từ file MP4 thật (t=3.5/9/21/31/40/52/62s) + thumbnail — đúng brand (#4C8DFF/#0B0E14/#FF8A5B, Montserrat, brand anchor cố định góc trên-phải/trên-trái), cân bằng dọc đạt sau 2 vòng chỉnh sửa (đã sửa 02-what.html bị dồn nội dung lên trên do line-wrap ngoài ý muốn — rút ngắn text + đẩy panel xuống top:1150; đã sửa 04-data.html bị lệch tâm do dm-quote position:absolute không tính vào flex-center — chuyển sang flex column center trong vùng top:320-1920 giống mẫu ai-dap-phanh-cuoc-dua-sieu-tri-tue), không phần tử bịa; (4) transcript (Gemini gemini-flash-lite-latest — gemini-flash-latest và Whisper đều bị chặn/hết quota free-tier trong phiên) khớp SCRIPT.md từng câu, không câu nào 'chế thêm', không nhắc tên kênh trong lời thoại, số liệu đọc đúng ('khoảng ba mươi', 'năm đến mười năm', tên riêng Grzegorz Kuliś/Figure đọc phiên âm gần đúng — chấp nhận được, không sai cấu trúc/nghĩa câu). npm run check: lint/runtime/motion 0 lỗi 0 cảnh báo; layout 2 info (content_overlap thoáng qua trong lúc animation reveal ở 03-facts/06-impact — do rotate transform khiến bounding-box check hiểu nhầm, đã xác nhận bằng ảnh render thật không có overlap thật); contrast 1 warning (dm-quote — dấu ngoặc kép khổng lồ mờ trang trí phía sau số liệu theo đúng ẩn dụ style 9-editorial-clipping, không phải text mang thông tin, không cần đạt AA). Style 9-editorial-clipping (index 8) — nội dung/góc nhìn/bố cục hoàn toàn khác các video style 9 hoặc chủ đề robot/việc làm trước đó (chưa video nào trong kênh khai thác chủ đề này)."
