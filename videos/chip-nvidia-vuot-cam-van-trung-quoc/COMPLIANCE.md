# COMPLIANCE — chip-nvidia-vuot-cam-van-trung-quoc

policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-22T01:35:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): YELLOW — tin công nghệ chạm yếu tố nhạy cảm phụ "kiểm soát xuất khẩu chip".
Không phải cáo buộc hình sự/chính trị/y tế/tài chính bị cấm ở GATE A. Tiếp tục dựng với framing
trung lập.

GATE B (content): YELLOW-fixed
- B1: Mọi số liệu (4,6 tỷ USD, 13,4 triệu USD, 56 chip/1,7 triệu USD, 8,7 triệu USD, các mã chip
  H100/A100/Blackwell/H200/MI325X) đều truy được về `?article=a86e828217ed` (đã liệt kê trong
  BRIEF.md mục "Số liệu / dữ kiện xác nhận"). Dùng "được cho là" cho claim về Megaspeed (chưa kết
  luận). Không thêm kết luận ngoài bài gốc.
- B2: Không bạo lực/thù ghét/quấy rối. Phê bình cơ chế/chính sách/công ty, KHÔNG nhắm cá nhân —
  cố ý bỏ tên riêng của cổ đông cá nhân được nhắc trong bài gốc để tránh rủi ro bê bối cá nhân
  chưa kết luận.
- B3: Không giả danh nền tảng/hãng/cơ quan/chuyên gia. Không testimonial giả. CTA là câu hỏi quan
  điểm thật, không engagement bait. Không link độc hại trong caption.
- B4 (AI media): giọng ElevenLabs generic = GREEN không cần disclosure. Ảnh Hook/Article Image
  dùng ảnh gốc từ `?image=a86e828217ed` (og:image bài GenK), có dẫn nguồn = GREEN. Không dùng AI
  tái dựng cảnh thật/người thật — mọi minh hoạ trong composition là đồ hoạ CSS/SVG (thẻ số, bảng,
  icon hình học), không phải ảnh AI tả người/sự kiện thật.
- B5: Ảnh chỉ từ `?image=`, không watermark. Nhạc Lyria tự sinh (calm ambient, không lời, đã kiểm
  negative-prompt). SFX từ bộ có sẵn trong repo (astra-openai). Video 100% tự dựng, không reup.
- B6: Tiêu đề "4,6 tỷ USD chip Nvidia bị cấm vẫn lọt vào Trung Quốc" = sự kiện + số liệu, không
  giật gân sai sự thật. Thumbnail phản ánh đúng nội dung (đã xem qua Read, đủ logo/tên kênh/badge
  nguồn/tiêu đề/2 tag). Caption có nguồn + hashtag liên quan, không nhồi nhét.
- B7 (nguyên bản): Góc trình bày riêng — chia nhỏ thành "3 con đường lách luật" + bảng so sánh
  "chính sách trên giấy vs thực tế vận chuyển" + nhấn mạnh Việt Nam là điểm trung chuyển (liên hệ
  khán giả VN) — không chỉ đọc lại tiêu đề báo. Style `4-split-comparison` (motif "chính sách" vs
  "thực tế" xuyên suốt 5 act giữa) — khác các video routine gần đây (ticker-tape, card-and-bar,
  chip-leaderboard). CTA là câu hỏi tranh luận thật bám đúng tin ("lá chắn cần thiết hay chậm
  chân?").
- B8 (pháp lý VN): tin có nhắc Việt Nam như một điểm trung chuyển hàng hoá theo báo cáo gốc (không
  buộc tội thực thể VN nào, chỉ nêu sự kiện logistics theo nguồn) — flag nhẹ, không phải nội dung
  vi phạm. Không bịa số điều luật.

GATE C (final): PASS
- Thumbnail + 6 frame thật (Hook/What/Facts/Data/Context/Impact/CTA — trích từ
  `output/chip-nvidia-vuot-cam-van-trung-quoc.mp4` bằng ffmpeg, xem bằng Read): đúng B6, không
  phần tử bịa, không lộ lỗi, cân bằng dọc đạt (nội dung mỗi act kết thúc trong khoảng
  top:1350-1680px, không trống đen nửa dưới).
- Transcript (ElevenLabs STT trên audio track mixer thật của file render, không phải file thô)
  khớp SCRIPT.md — không câu nào bị "chế thêm"; 1 lỗi phiên âm gần giống chấp nhận được
  ("Núp bóng" nghe thành "Nuốt bóng" — lỗi nhận dạng STT, không phải lỗi phát âm TTS).
- Caption dùng để đăng = CAPTION.md đã qua GATE B, không sửa tay thêm claim mới.
- Verify kỹ thuật đủ 5 bước: (1) duration 73.07s khớp thiết kế 73.06s; (2) silencedetect không có
  khoảng lặng chết ≥0.6s; (3) loudnorm Input Integrated -14.6 LUFS (lệch 0.6 LU, trong ngưỡng ±1),
  True Peak -1.0 dBTP (đạt ngưỡng ≤-1.0); (4) 7 frame trích tại mốc cuối animation-reveal mỗi act
  — xem bằng Read, không lỗi bố cục; (5) transcript khớp script (ở trên).

decision: APPROVE
risk_level: YELLOW
ai_disclosure_required: false
copyright_notes: "ảnh og:image từ GenK (dẫn nguồn qua ?image=), có ghi 'Nguồn: GenK' trên hình; nhạc nền Lyria tự sinh 100% instrumental, không lời; SFX từ bộ palette dùng chung của kênh (videos/astra-openai/assets/sfx)"
claims_verified:
  - "H100, A100, Blackwell bị Mỹ cấm bán cho Trung Quốc; H20 hạn chế; H200/MI325X xét theo trường hợp, thuế 25% — đối chiếu ?article=a86e828217ed"
  - "4,6 tỷ USD phần cứng Nvidia qua Megaspeed International vào Trung Quốc (2023-2025), được cho là — đối chiếu ?article=a86e828217ed"
  - "13,4 triệu USD GPU qua Việt Nam, Ấn Độ, Malaysia (2022-2025) — đối chiếu ?article=a86e828217ed"
  - "56 GPU trị giá 1,7 triệu USD qua nhà thầu nhỏ (7/2025-1/2026) — đối chiếu ?article=a86e828217ed"
  - "Báo cáo của nhóm giám sát thương mại tại Washington, phần lớn do chính phủ Mỹ tài trợ — đối chiếu ?article=a86e828217ed"
sensitive_flags:
  - "kiểm soát xuất khẩu chip trí tuệ nhân tạo — framing trung lập, không kết luận thay cơ quan chức năng, nêu rõ đây là báo cáo của 1 tổ chức giám sát thương mại (không phải kết luận điều tra chính phủ)"
vietnam_legal_flags:
  - "Tin nêu Việt Nam là 1 điểm trung chuyển logistics chip theo báo cáo gốc, không buộc tội thực thể Việt Nam nào — nêu nguyên văn theo nguồn, không suy diễn thêm"
notes: "Style dựng 4-split-comparison (index 3, claim_style lúc 2026-09-22T00:46:02Z). Tên cá nhân doanh nhân được nhắc trong bài gốc CỐ Ý không đưa vào SCRIPT/CAPTION/composition để giảm rủi ro B2 (bê bối cá nhân chưa kết luận với người không phải nhân vật công chúng)."
