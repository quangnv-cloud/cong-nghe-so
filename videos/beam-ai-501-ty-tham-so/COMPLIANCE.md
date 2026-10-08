# COMPLIANCE — beam-ai-501-ty-tham-so
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-10-08T01:35:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): GREEN
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "Ảnh article-hero.png là ảnh minh hoạ ý niệm (mạng nơ-ron trừu tượng, không phải cảnh/người thật) lấy qua endpoint ?image=881d9f699fce (do Apps Script tải hộ từ nguồn báo, có dẫn nguồn trong COMPLIANCE/BRIEF); nhạc nền sinh bằng Google Lyria (lyria-recipe.py, thành công lần đầu, không cần fallback ElevenLabs Music), không lời, thuộc quyền dự án; SFX từ assets/sfx/ repo chuẩn kênh; giọng đọc Vbee TTS AI narrator chung, không giả giọng người thật cụ thể."
claims_verified:
  - "Beam — mô hình AI của Reflection AI, 501 tỷ tham số — đối chiếu ?article=881d9f699fce"
  - "Mô hình mở trọng số (open-weight), cho tải về/triển khai/tinh chỉnh — đối chiếu bài gốc"
  - "Kiến trúc Mixture-of-Experts, chỉ kích hoạt ~23 tỷ tham số mỗi lần — đối chiếu bài gốc"
  - "Tiền huấn luyện trên 23.800 tỷ token, 6.144 GPU Nvidia GB300 NVL72, <4 tuần — đối chiếu bài gốc"
  - "Học tăng cường dùng 10.500 GPU Nvidia GB300, liên tục 4 tuần — đối chiếu bài gốc"
  - "Hơn 100 triệu chuỗi tương tác thử nghiệm, ~1,3 tỷ sandbox, tới 170.000 sandbox đồng thời — đối chiếu bài gốc"
  - "Hiệu năng suy luận tương đương GLM-5.2, ước tính tốn ít compute hơn 3-4 lần (ước tính của Reflection AI, không phải đo trực tiếp — giữ nguyên qualifier 'ước tính' trong SCRIPT/CAPTION)"
sensitive_flags: []
vietnam_legal_flags: []
notes: |
  Tin công nghệ/AI thông thường (ra mắt mô hình, số liệu kỹ thuật huấn luyện) — GREEN ngay từ
  GATE A, không yếu tố nhạy cảm phụ (không chạm AI & việc làm / kiểm soát xuất khẩu chip / quyền
  riêng tư / kiện bản quyền AI — thuần kỹ thuật sản phẩm).

  GATE B: B1 mọi số liệu đối chiếu ?article=881d9f699fce, không con số tự bịa; phân biệt rõ "ước
  tính" (so sánh GLM-5.2) vs sự thật đã công bố; act 6/Impact chỉ nêu sự thật đã xảy ra (Beam ĐÃ
  là mô hình mở trọng số), không dùng chi tiết "dự kiến công bố đầy đủ trong tháng 10" (đó là dự
  định tương lai, đã loại khỏi script theo đúng yêu cầu act 6 không suy đoán). B2-B3 không vi phạm.
  B4: ảnh minh hoạ ý niệm (concept art mạng nơ-ron) = GREEN không cần disclosure; giọng AI narrator
  chung = GREEN. B5 nhạc/ảnh/SFX đúng nguồn được phép. B6 tiêu đề = sự kiện + số liệu, không giật
  gân. B7 góc nhìn riêng: dùng style Timeline Chronology (lần đầu dùng cho kênh, index 6) kể câu
  chuyện qua các mốc huấn luyện, không chỉ đọc lại tiêu đề báo; CTA đặt câu hỏi tranh luận thật bám
  tin ("minh bạch & hiệu quả" vs "đua tài nguyên lãng phí"). B8 không chạm vấn đề pháp lý VN.

  GATE C: xem lại thumbnail (hiện đủ logo, tên kênh, badge nguồn, tiêu đề, 2 tag, không mờ/cắt) +
  nhiều frame render ở các mốc kết thúc reveal của từng act (đúng B6, không phần tử bịa, cân bằng
  dọc — nội dung mỗi act kết thúc trong khoảng top:1400-1550px, không dừng sớm ở ~1000px). Transcript
  (Gemini gemini-flash-lite-latest trên audio đã mix) khớp 100% ý nghĩa SCRIPT.md — chỉ 2 lỗi nhận
  dạng ASR vô hại (nghe "Beam" thành "BiM", "card" thành "các" — lỗi âm thanh gần giống của bộ nhận
  dạng, không phải lỗi phát âm TTS hay viết tắt lọt vào SCRIPT.md). Caption dùng để đăng = CAPTION.md
  đã qua GATE B, không sửa tay thêm claim mới. Smash-cut nội bộ act 3 (Key facts) xác nhận hoạt động
  đúng qua chuỗi frame liên tiếp quanh t≈21.17s.

  Kỹ thuật: Lyria BGM thành công lần đầu, không cần fallback ElevenLabs Music. Loudness đo lần đầu
  -18.0 LUFS (lệch quá ±1 LU) → chạy loudnorm 2 pass (target -14 LUFS, TP -1.5 dBTP để có biên an
  toàn) → đạt -14.1 LUFS / -1.4 dBTP (verify độc lập xác nhận). Thời lượng cuối 72.3s (dưới giới
  hạn 75s). Vbee TTS cả 7 dòng thành công lần gọi đầu (poll SUCCESS), không cần rút gọn SCRIPT.md.
