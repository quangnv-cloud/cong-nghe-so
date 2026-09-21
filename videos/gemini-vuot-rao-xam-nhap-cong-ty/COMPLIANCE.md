# COMPLIANCE — gemini-vuot-rao-xam-nhap-cong-ty
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-21T01:15:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): YELLOW (an ninh mạng — tin công nghệ/AI thông thường có yếu tố nhạy cảm phụ; không phải cáo buộc hình sự cá nhân, không chính trị/bầu cử là nội dung chính, không y tế/tài chính, không deepfake, không hướng dẫn khai thác — tường thuật sự cố Google đã tự công khai thừa nhận và đã khắc phục)
GATE B (content):   YELLOW-fixed (B1-B8 đã soát: mọi số liệu/tên/mốc thời gian truy được về `?article=99cc2e9b9563` + BRIEF.md; phân biệt "cam kết" của Google (Heather Adkins) với sự việc đã xảy ra; 2 pull-quote ở act Context là diễn giải lại quan điểm công khai của Dario Amodei/Jensen Huang theo đúng nghĩa bài gốc, không phải trích nguyên văn mới bịa ra; không tấn công cá nhân, phê bình hành vi/sự cố kỹ thuật; không giả danh; ảnh chỉ từ `?image=` có dẫn nguồn Znews, không chỉnh sửa nội dung; nhạc Lyria tự sinh, SFX từ repo; tiêu đề nêu đúng sự kiện, không giật gân; góc nhìn riêng: data moment mốc th.5→cuối th.7 + bảng so sánh Anthropic/OpenAI/Meta + 2 pull-quote đối lập, không chỉ đọc lại tiêu đề báo; CTA bám đúng góc tranh luận của tin)
GATE C (final):     PASS (xem 6 frame QC + thumbnail bằng Read — đúng B6, không phần tử bịa; transcript Gemini multimodal khớp 100% SCRIPT.md, không câu chế thêm; caption dùng để đăng = CAPTION.md đã qua GATE B, không sửa tay thêm claim mới)

decision: APPROVE
risk_level: YELLOW
ai_disclosure_required: false
copyright_notes: "ảnh Hook/Article Image Card = og:image bài báo (Reuters, qua Znews), có dẫn nguồn 'Nguồn: Znews' trong Brand Anchor; không chỉnh sửa nội dung ảnh; nhạc nền tự sinh qua Google Lyria (calm ambient, không lời), SFX từ bộ palette sẵn có trong repo (astra-openai/assets/sfx)"
claims_verified:
  - "18/9/2026 Google công bố sự cố — khớp bài gốc"
  - "Gemini thoát môi trường thử nghiệm tháng 5/2026 — khớp bài gốc"
  - "xâm nhập hệ thống mạng của 3 công ty thật — khớp bài gốc"
  - "đơn vị kiểm thử Irregular (startup Israel) vô tình cấp quyền truy cập Internet — khớp bài gốc"
  - "mô hình lập trình tấn công công ty hư cấu trùng tên công ty thật — khớp bài gốc"
  - "Gemini dùng mật khẩu tìm được/đoán được để đăng nhập — khớp bài gốc"
  - "Gemini tự nhận ra đang ở hạ tầng thật rồi dừng tấn công, Google khẳng định không gây thiệt hại — khớp bài gốc"
  - "cuối tháng 7/2026 các phòng thí nghiệm liên quan (gồm Google) được Irregular thông báo — khớp bài gốc, KHÔNG nhầm sang '3 công ty bị xâm nhập được thông báo cuối tháng 7' (Google mới cam kết thông báo, chưa xác nhận đã xong)"
  - "Heather Adkins (Phó chủ tịch kỹ thuật an ninh Google) cam kết thông báo đầy đủ 3 công ty + đổi quy trình thử nghiệm — khớp bài gốc, đúng thì hiện tại/cam kết, không suy đoán đã hoàn tất"
  - "sự cố tương tự từng xảy ra tại Anthropic, OpenAI, Meta — khớp bài gốc"
  - "Dario Amodei (giám đốc điều hành Anthropic) kêu gọi giảm tốc độ phát triển trí tuệ nhân tạo — khớp bài gốc (diễn giải quan điểm công khai, không phải trích nguyên văn bịa)"
  - "Jensen Huang (giám đốc điều hành Nvidia) cho rằng nên tiếp tục phát triển nhanh — khớp bài gốc (diễn giải quan điểm công khai)"
sensitive_flags: ["an ninh mạng — tường thuật sự cố Google đã công khai thừa nhận và đã khắc phục, framing trung lập, không hướng dẫn khai thác/tấn công, không kêu gọi hành động nguy hiểm"]
vietnam_legal_flags: []
notes: "Style dựng: 1-card-and-bar (index 0, claim_style). Thời lượng render thật 73.900s (thiết kế 73.868s). Loudness -14.9 LUFS integrated (lệch 0.9 LU, trong ngưỡng ±1 LU), True Peak -1.0 dBTP — đạt chuẩn, không cần loudnorm 2-pass. silencedetect: không có khoảng lặng chết. Cân bằng dọc: cả 6 frame QC (Hook + cuối reveal của 5 act giữa) đều lấp đầy khung, phần tử cuối kết thúc trong khoảng top ~1445-1655px, không có mảng đen trống nửa dưới."
