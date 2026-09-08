# COMPLIANCE — dlss5-chay-tren-amd
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-08T01:10:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): GREEN
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "Ảnh Hook/Article Image Card = ảnh minh hoạ chính thức của bài báo GenK (đăng lại/biên tập từ thanhnienviet.vn), ok:true qua ?image=d198c6fd963a, ghi nguồn 'Nguồn: GenK · 6/9/2026'; ảnh là graphic so sánh in-game (nhân vật game + card Radeon), không phải ảnh người thật, không chỉnh sửa nội dung; nhạc nền sinh bằng Google Lyria (calm ambient, instrumental, negative-prompt loại vocal/percussion), không lời, sở hữu của dự án; SFX từ palette repo (impact-bass/whoosh/pop/chime, dùng nguyên bản không đổi tốc độ/pitch)."
claims_verified:
  - "Modder danielblnc tạo công cụ DLSS-NR-on-AMD — đối chiếu ?article=d198c6fd963a"
  - "DLSS 5 Neural Rendering ban đầu chỉ dành cho GeForce RTX 50, ra mắt trên NBA 2K27 — đối chiếu bài gốc"
  - "Chạy được trên Radeon RDNA 4 và một số RDNA 3, chỉ với game DirectX 12 có FSR — đối chiếu bài gốc"
  - "Radeon RX 9070 XT, Cyberpunk 2077 đạt khoảng 33 FPS ở 1080p (tăng từ 28-30 FPS bản đầu) — đối chiếu bài gốc"
  - "Một hệ thống khác (Tom's Hardware) giảm từ hơn 80 FPS xuống 11-12 FPS — đối chiếu bài gốc"
  - "Mục tiêu hiệu năng ngang RTX 5070 Ti, khoảng cách hiện tại còn rất xa — đối chiếu bài gốc"
  - "Công cụ không phải lớp dịch CUDA, viết lại riêng cho kiến trúc AMD (HIP kernel) — đối chiếu bài gốc (không đưa chi tiết kỹ thuật này vào voice, chỉ BRIEF)"
  - "Chưa được Nvidia/AMD xác nhận chính thức; một số người dùng Reddit cho biết Windows Defender cảnh báo tệp cài là Trojan, bài gốc lưu ý chưa chứng minh chứa mã độc — đối chiếu bài gốc, giữ đúng sắc thái 'chưa chứng minh' trong voice + on-screen"
sensitive_flags: []
vietnam_legal_flags: []
notes: "Tin nguồn vn (GenK/thanhnienviet), không cần dịch. Video có góc phân tích riêng (bảng FPS đối chiếu, sơ đồ nguyên nhân Tensor-core vs phần cứng AMD, khung 'khoảng cách tới mục tiêu') chứ không chỉ đọc lại tiêu đề báo (B7). Style dựng: 5-map-and-geo (index 4, claim_style lúc 2026-09-08T00:33:57Z) — diễn giải ẩn dụ bản đồ/ghim/tuyến-vượt-biên cho chủ đề phần cứng vì tin không có yếu tố địa lý thật. Khác hẳn bố cục/chủ đề 2 video gần nhất (đều xoay quanh OpenAI/AGI). Verify 4 bước: (1) ffprobe duration=72.40s, khớp thiết kế 72.39s, dưới 75s; (2) silencedetect noise=-35dB d=0.6 không phát hiện khoảng lặng chết; (3) trích + soát 7 frame (Hook, What, Facts, Data, Context, Impact, CTA) qua Read — đúng brand (#4C8DFF/#0B0E14/#FF8A5B), cân bằng dọc đạt (frame Hook/What/Data/Context/Impact/CTA đều có phần tử cuối kết thúc trong khoảng top 1400-1680px sau khi sửa lỗi phát hiện ở act 2 lúc soát; act 3 kết thúc ~1440px, chấp nhận được), không phần tử bịa, không emoji (icon = CSS shapes); (4) transcript qua Gemini flash-lite-latest khớp SCRIPT.md gần như nguyên văn (act 3-7 khớp verbatim) — chỉ lệch phiên âm ở 2 chỗ chấp nhận được theo quy định: 'AMD' được máy phiên âm thành 'Amade' (đọc chữ cái viết tắt, không phải lỗi cấu trúc/nghĩa) và tên tự tạo 'danielblnc' phiên âm thành 'Daniel Pliency' (tên riêng bịa không có trong từ điển, TTS đọc đúng âm tiết nhưng máy phiên âm đoán nhầm chính tả) — không có câu nào bị chế thêm/bịa nghĩa, không viết tắt lọt lỗi cấu trúc. Thumbnail (trích t=3.0s trong cửa sổ Hook, sau khi toàn bộ animation Hook ổn định ở ~2.5s theo timeline 01-hook.html) xác nhận đủ logo, tên kênh, badge nguồn, tiêu đề DLSS 5, 2 tag tương phản, rõ nét không cắt."
