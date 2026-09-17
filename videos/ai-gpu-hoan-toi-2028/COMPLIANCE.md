# COMPLIANCE — ai-gpu-hoan-toi-2028
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-17T14:30:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): GREEN
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh sản phẩm GPU từ og:image bài GenK (?image=d4580e9550e9), có dẫn nguồn; nhạc nền Lyria tự sinh (calm, không lời); SFX từ bộ repo dùng chung."
claims_verified:
  - "GeForce RTX 60 series & phần lớn Radeon RDNA 5 đồn bị hoãn tới 2028 — đối chiếu ?article=d4580e9550e9"
  - "Nguồn tin Kepler_L2 (leaker AMD, diễn đàn AnandTech) — đối chiếu bài gốc"
  - "Ngoại lệ AT2 (AMD) có thể ra mắt 2027, hiệu năng ngang RTX 5080 — đối chiếu bài gốc"
  - "Tin đồn cũ (Moore's Law is Dead): RTX 60 nửa đầu 2027, bị Kepler_L2 bác bỏ — đối chiếu bài gốc"
  - "Navi 5X đồn đoán: 12.288 nhân, ~3,4GHz, 32GB GDDR7 — đối chiếu bài gốc"
  - "Nvidia đã công bố nền tảng Vera Rubin (data center), chưa hé lộ GeForce kế tiếp — đối chiếu bài gốc"
  - "Đối tác sản xuất card AMD chưa nhận lịch trình rõ ràng cho RDNA 5 — đối chiếu bài gốc"
sensitive_flags: []
vietnam_legal_flags: []
notes: "Tin công nghệ/thị trường thông thường (rò rỉ lịch phát hành phần cứng), không chạm yếu tố nhạy cảm phụ nào trong danh sách GATE A/B. Mọi mốc thời gian tương lai đều được hedge rõ ràng ('được cho là', 'dự kiến', 'chưa xác nhận chính thức') theo B1. Act 6 (Impact) chỉ nêu sự thật đã xảy ra (Nvidia công bố Vera Rubin; đối tác AMD xác nhận chưa có lịch), không suy đoán tương lai. Style dựng: 7-timeline-chronology (index 6, claim_style). Đã phát hiện và sửa lỗi cân bằng dọc (khoảng trống lớn giữa 3 fact ở act Key facts, và khoảng trống giữa 2 card ở act Context/Impact) trước khi chấp nhận render — đã re-render sau khi chuyển sang bố cục card đầy đủ, xác nhận bằng frame thật ở cuối animation-reveal mỗi act giữa. Verify 5 bước: (1) duration 69.27s khớp thiết kế 69.245s; (2) không khoảng lặng chết >0.6s; (3) loudness -14.5 LUFS (lệch 0.5 LU, trong ngưỡng ±1), True Peak -1.1 dBTP; (4) frame thật mỗi act xác nhận đúng nội dung, không phần tử bịa, cân bằng dọc đạt; (5) transcript (Gemini flash-latest multimodal) khớp SCRIPT.md, chỉ khác biệt ngữ âm nhỏ chấp nhận được ('card'→'cạc')."
