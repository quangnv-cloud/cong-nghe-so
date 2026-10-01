# COMPLIANCE — xe-dien-tq-mat-gia-thai-lan
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-10-01T02:35:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): GREEN
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "Ảnh Hook/Article Image Card = ảnh thật từ GenK (?image=9accc8a85b15), có dẫn nguồn trên hình (badge 'Nguồn: GenK') + CAPTION; không chỉnh sửa nội dung ảnh. Nhạc nền sinh bằng Google Lyria (lyria-realtime-exp, instrumental, calm ambient, negative-prompt loại vocal) — không dùng fallback ElevenLabs Music. SFX từ bộ palette repo (videos/astra-openai/assets/sfx/). Không dùng AI tái dựng cảnh thật/người thật như ảnh chụp — mọi minh hoạ còn lại là motion graphics / card / biểu đồ (CSS/SVG), không phải ảnh AI."
claims_verified:
  - "BYD Atto 3 đời 2022, đã chạy 156.789 km, rao bán 320.000 baht (~256 triệu đồng) tháng 9/2026 — đối chiếu ?article=9accc8a85b15"
  - "Giá niêm yết khi ra mắt 10/2022: 1.199.900 baht (~960 triệu đồng) — đối chiếu ?article=9accc8a85b15"
  - "Chợ xe cũ Yo Ratchada (đại diện Pinyo Thanawatcharaporn): tồn kho xe điện giảm từ hơn 40 chiếc xuống hơn 10 chiếc (2024) — đối chiếu ?article=9accc8a85b15"
  - "Chiang Mai: điểm ký gửi xe điện ưu tiên tiền mặt, chưa có vay ngân hàng cho xe điện cũ — đối chiếu ?article=9accc8a85b15"
  - "Krungthai COMPASS (3/2026): xe điện mới tại Thái Lan giảm giá 11–35% so với giá ra mắt — đối chiếu ?article=9accc8a85b15"
  - "2023–2025: 1.009 bãi xe cũ Thái Lan đóng cửa/phá sản; chỉ số giá xe cũ giảm ~25% — đối chiếu ?article=9accc8a85b15"
  - "Khảo sát Differential Thailand (2.651 chủ xe, cuối 9/2026): 69% chủ xe Nhật Bản / 60% xe Mỹ / 46% xe Trung Quốc muốn mua lại đúng hãng — đối chiếu ?article=9accc8a85b15"
  - "Thái Lan đi trước Việt Nam khoảng 3 năm trong việc đón xe điện Trung Quốc — nguyên văn từ bài gốc, không phải suy đoán của routine"
sensitive_flags: []
vietnam_legal_flags: []
notes: |
  - GATE A: tin thị trường tiêu dùng/công nghệ thông thường (giá xe điện, khảo sát), không thuộc
    bất kỳ nhóm BỎ TIN nào (không cáo buộc hình sự/chính trị/y tế "thuốc thần"/tài chính "cam kết
    lãi"/deepfake/BLACK). Không có yếu tố nhạy cảm phụ (không liên quan AI&việc làm, xuất khẩu
    chip, quyền riêng tư, kiện bản quyền AI) → GREEN thẳng, không cần framing YELLOW.
  - GATE B: B1 toàn bộ số liệu/tên riêng/trích dẫn truy được về ?article=9accc8a85b15 (liệt kê ở
    claims_verified), không số liệu tự bịa; văn phong giữ đúng nghĩa bài gốc, câu "Thái Lan đi
    trước Việt Nam ~3 năm" lấy nguyên ý bài gốc, không suy đoán tương lai cho VN. B2 không bạo
    lực/thù ghét/quấy rối/nội dung tình dục; phê bình chính sách giá của hãng, không công kích cá
    nhân (trích dẫn ông Pinyo trung lập, đúng nguyên văn ý kiến chuyên môn). B3 kênh không mạo danh
    hãng/nền tảng/chuyên gia; CTA là câu hỏi quan điểm thật, không engagement bait, không link/giveaway
    đáng ngờ. B4 giọng Vbee TTS chuẩn kênh = GREEN không cần disclosure; ảnh thật có dẫn nguồn = GREEN;
    không có cảnh AI tái dựng người/sự kiện thật dạng ảnh chụp. B5 ảnh chỉ từ ?image=, nhạc Lyria tự
    sinh, SFX từ repo, video 100% tự dựng. B6 tiêu đề "Xe điện Trung Quốc tại Thái Lan: bán lại chỉ
    còn khoảng 1/4 giá trị sau 4 năm" = sự kiện + số liệu, không giật gân sai sự thật; thumbnail
    (frame Hook t=4.0s) phản ánh đúng nội dung. B7 góc trình bày riêng (so sánh giá mới/bán lại +
    khảo sát ý định mua lại theo hãng, style Editorial Clipping với pull-quote), không chỉ đọc lại
    tiêu đề báo, không trùng bố cục video gần nhất. B8 không chạm an ninh mạng/chính trị/dữ liệu cá
    nhân/quảng cáo có điều kiện — không gắn cờ pháp lý VN.
  - GATE C: đã xem lại thumbnail + 7 frame đại diện (hook, act2–act6, cta) — đúng B6, không phần tử
    bịa, không lỗi hiển thị (đã phát hiện và sửa lỗi kỹ thuật: bar chart act 5 không hiện trong
    pipeline render hàng loạt do scaleY+transform-origin không ổn định với chụp frame kiểu
    screenshot — đã đổi sang animate height trực tiếp, verify lại bằng frame thật, bars hiện đúng).
    Transcript (Gemini gemini-flash-lite-latest, Whisper bị chặn egress) khớp SCRIPT.md — không câu
    nào "chế thêm", chỉ lệch âm gần giống ở 3 tên riêng nước ngoài (BYD→"BID", Yo Ratchada→"Joe
    Rachada", Krungthai→"Chromeh") — nhầm âm chấp nhận được theo quy tắc, không phải đọc sai ngôn
    ngữ/cấu trúc. Caption dùng để đăng = CAPTION.md nguyên bản đã qua GATE B, không sửa thêm claim.
  - Verify kỹ thuật: ffprobe 70.5s (<75s), 1080x1920/30fps; silencedetect không có khoảng lặng chết;
    loudnorm 2-pass đạt -14.0 LUFS / -1.6 dBTP (trong ngưỡng ±1 LU / ≤-1.0 dBTP); cân bằng dọc đã đo
    bằng frame thật ở cuối mỗi act giữa (act2≈1421px, act3≈1483px, act4≈1551px, act5≈1575px,
    act6≈1471px — đều trong dải 1400–1680px yêu cầu); karaoke caption, depth background, glow,
    smash-cut (act 2 & 5), scaleY→height bar chart đều đã áp dụng theo "Kỹ thuật hình ảnh nâng cao".
  - BGM: Google Lyria (model lyria-realtime-exp), thành công ngay lần thử đầu — KHÔNG cần fallback
    ElevenLabs Music.
