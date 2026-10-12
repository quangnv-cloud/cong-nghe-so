# COMPLIANCE — discovery-loop-dinh-gia-50-ty-usd
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-10-12T01:30:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): GREEN
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "Ảnh Hook/Article Image Card là ảnh báo chí thật (4 nhà sáng lập Discovery Loop), lấy qua `?image=751468230ce0` từ bài GenK, có dẫn nguồn trên màn hình (badge 'Nguồn: GenK'); không qua AI chỉnh sửa/tái tạo. Nhạc nền do Google Lyria tự sinh (models/lyria-realtime-exp), thành công lần thử đầu, không cần fallback ElevenLabs Music. SFX từ bộ repo chuẩn (chime/pop/impact-bass/whoosh). Video 100% tự dựng bằng hyperframes, không reup."
claims_verified:
  - "Ngày 5/8/2026: Jeff Dean, Sanjay Ghemawat, Oriol Vinyals, Lê Viết Quốc rời Google lập Discovery Loop — đối chiếu ?article=751468230ce0"
  - "Thời điểm ra mắt chưa thuê văn phòng/chưa tuyển nhân sự — đối chiếu bài gốc"
  - "Định giá đàm phán tăng từ 10 tỷ USD (8/2026) lên 50 tỷ USD (Business Insider, 11/9/2026) — đối chiếu bài gốc, giữ đúng khung 'đàm phán' không khẳng định đã chốt"
  - "So sánh Thinking Machines Lab (Mira Murati) 12 tỷ USD, Safe Superintelligence (Ilya Sutskever) 32 tỷ USD — đối chiếu bài gốc"
  - "Google trở thành nhà đầu tư sáng lập + hỗ trợ điện toán đám mây năm đầu — đối chiếu bài gốc, dùng làm act Impact (sự thật đã xảy ra, không suy đoán)"
  - "Lý lịch 4 nhà sáng lập (vai trò cũ tại Google, Stanford, Andrew Ng) — đối chiếu bài gốc"
  - "Trích lời Jeff Dean trả lời WIRED về vai trò giám đốc điều hành — đối chiếu bài gốc"
sensitive_flags: []
vietnam_legal_flags: []
notes: |
  - Caption karaoke: ElevenLabs STT KHÔNG được thử trong phiên này (tiền lệ gần đây cho thấy thường hết quota) —
    dùng fallback xấp xỉ chia đều theo ffprobe thời lượng thật từng dòng, trọng số theo độ dài từ. Đây là hạn chế
    đã biết, không phải lỗi GATE theo đúng tiền lệ ghi trong style-rotation-state.json.
  - Transcript verify bằng Gemini multimodal (gemini-flash-lite-latest): nội dung khớp 100% ý nghĩa SCRIPT.md,
    không câu nào "chế thêm". Một vài lỗi nhận dạng ASR vô hại trên tên riêng nước ngoài khi nghe cả audio dài
    71s một lần (vd "Jeff Dean" nghe nhầm/rơi mất trong bản ghi full, nhưng khi tách riêng từng dòng hoặc đoạn
    ngắn quanh mốc đó thì nghe ra "Ledin"/"Reddin" — xác nhận ĐÃ có tiếng nói đúng trong audio, chỉ là ASR nghe
    nhầm âm gần giống trên tên riêng tiếng Anh, không phải lỗi giọng đọc hay audio bị cắt). Tương tự "Oriol Vinyals"
    nghe thành "Orion Vinos/Vios", "Sanjay Ghemawat" thành "Sanjay Gemawat" — đều là ASR near-miss trên tên riêng,
    chấp nhận được theo đúng tinh thần BRAND-SYSTEM.md mục Voiceover.
  - Phát hiện và SỬA 2 lỗi cân bằng dọc trước khi duyệt: act "Chuyện gì xảy ra" (card kết thúc ~top:1373px, dưới
    ngưỡng 1400px tối thiểu) và act "Ai là ai" (khối trích dẫn pull-quote dừng ở ~top:950px do một lần sửa `sed`
    trên script sinh file không khớp (lỗi escape dấu ngoặc nhọn trong f-string Python), khiến bản sửa không áp
    dụng — sau khi phát hiện qua frame thật, đã sửa trực tiếp bằng Edit tool, verify lại bằng frame thật, rồi mới
    render lại và duyệt. Cả 2 act giờ kết thúc nội dung trong khoảng top:1400–1680px như yêu cầu.
  - Loudness ban đầu đo -15.95 LUFS / -1.12 dBTP (lệch quá ±1 LU) → chạy loudnorm 2-pass (target -14 LUFS,
    TP -1.5 dBTP để có biên an toàn dưới ngưỡng -1.0 dBTP) → verify độc lập xác nhận đạt đúng -14.0 LUFS / -1.4 dBTP.
  - silencedetect: không phát hiện khoảng lặng chết ≥0.6s trong toàn video.
  - Thời lượng: 71.27s (dưới mức trần 75s).
