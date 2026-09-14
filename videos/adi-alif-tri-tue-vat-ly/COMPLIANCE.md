# COMPLIANCE — adi-alif-tri-tue-vat-ly
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-14T07:26:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): GREEN — thương vụ mua bán - sáp nhập (M&A) ngành bán dẫn, số liệu tài chính
  doanh nghiệp cụ thể. Không thuộc bất kỳ loại BỎ TIN nào ở GATE A (không cáo buộc hình sự / chính
  trị / bầu cử / y tế "thuốc thần" / tài chính "cam kết lãi" / deepfake / bóc lột trẻ em / bạo lực /
  lừa đảo). Không có yếu tố nhạy cảm phụ nào cần siết framing (không kiểm soát xuất khẩu chip,
  không tranh chấp pháp lý, không quyền riêng tư cụ thể trong bài gốc).

GATE B (content): GREEN
  B1. Mọi số liệu (1,35 tỷ USD, tối đa 200 triệu USD, 11 tỷ USD doanh thu ADI FY2025, ngày 11/9,
      "trước cuối 2026") đều truy được về `?article=9d74dd6b74c8` / BRIEF.md. Không con số tự bịa.
      Không có claim gây tranh cãi cần gắn "được cho là" — toàn bộ là sự kiện M&A đã ký kết chính
      thức, không phải cáo buộc/dự đoán.
  B2. Không bạo lực / thù ghét / quấy rối / doxxing / nội dung tình dục — chỉ tường thuật một
      thương vụ doanh nghiệp, không nhắm cá nhân tiêu cực.
  B3. Không giả danh nền tảng / hãng / chuyên gia. Không testimonial giả, không engagement bait,
      không link lạ trong caption. Kênh "Công Nghệ Số" trình bày rõ là nguồn tin độc lập.
  B4. Giọng AI narrator chung (ElevenLabs Khánh Lâm) = GREEN, không cần disclosure. Ảnh Hook /
      Article Image Card dùng nguyên ảnh bài báo (đồ hoạ công bố chính thức "Analog Devices x Alif
      Semiconductor — Congratulations on the acquisition") lấy qua `?image=9d74dd6b74c8` — ảnh
      thật do hai công ty công bố, có dẫn nguồn GenK trong Brand Anchor + badge Hook, KHÔNG chỉnh
      sửa nội dung ảnh, KHÔNG phải ảnh AI tái dựng cảnh thật/người thật.
  B5. Ảnh chỉ từ endpoint `?image=`, không watermark bị xoá. Nhạc nền Lyria tự sinh (calm ambient,
      density 0.25/brightness 0.4, kèm negative-prompt loại vocal/lời). SFX từ palette repo
      (`videos/astra-openai/assets/sfx/`). Video 100% tự dựng qua hyperframes, không reup.
  B6. Tiêu đề "Analog Devices mua Alif Semiconductor, đặt cược lớn vào trí tuệ vật lý" = sự kiện +
      số liệu chính, không giật gân sai sự thật. Thumbnail (frame Hook) phản ánh đúng nội dung —
      logo, nguồn, tiêu đề, 2 tag tương phản đều rõ, không cắt/mờ. Caption không nhồi hashtag (6
      hashtag: 2 bắt buộc + 4 liên quan chủ đề).
  B7. Góc trình bày riêng: ẩn dụ "trục thời gian thương vụ" (style 7-timeline-chronology — trục dọc
      3 mốc ở Key facts, node lớn ở Data moment, trục ngang 4 mốc tăng dần ở Context, 2 khối tác
      động nối trục ở Impact) — không chỉ đọc lại tiêu đề báo, có phân tích riêng (đối chiếu quy mô
      doanh thu ADI với giá trị thương vụ, đặt câu hỏi "đặt cược quá lớn hay không"). Không trùng
      style/bố cục với 2 video gần nhất (`an-do-cntt-315-ty-usd-ai` — 5-map-and-geo,
      `ai-dap-phanh-cuoc-dua-sieu-tri-tue` — 6-ring-progress). Act 7 CTA bám đúng câu hỏi tranh
      luận của tin (AI rời đám mây vào thẳng chip vật lý — bước tiến hay đặt cược quá lớn).
  B8. Không chạm an ninh mạng / an ninh quốc gia / bầu cử / dữ liệu cá nhân / quảng cáo có điều
      kiện — vietnam_legal_flags rỗng. Đây là thương vụ M&A doanh nghiệp Mỹ, không liên quan pháp
      lý Việt Nam.

GATE C (final): PASS
  - Đã Read trực tiếp thumbnail + 7/7 frame render (Hook qua thumbnail t≈2.7s, What happened
    t≈14.5s, Key facts t≈25s, Data moment t≈34.5s, Context t≈44.5s, Impact t≈54.5s, CTA t≈67.5s) —
    brand đúng (#4C8DFF/#0B0E14/#FF8A5B, Montserrat, Brand Anchor cố định góc trên, không emoji
    trong composition), không phần tử bịa, số liệu trên hình khớp BRIEF.md.
  - Phát hiện lỗi cân bằng dọc ở frame CTA (act 7) trong lần soát đầu: khối nội dung dồn lên ~55%
    trên, để trống đen lớn (~800px) giữa pill và chữ ký logo ở đáy khung — đã sửa lại bằng cách gộp
    toàn bộ nhóm (kicker → headline → 2 icon đối lập → pill → chữ ký) thành 1 khối canh giữa dọc
    trong vùng an toàn, chữ ký kết thúc ~top:1425px. Re-render + soát lại: đạt, không còn khoảng
    đen bất thường ở giữa khung. Tất cả 7 frame khác đã đạt yêu cầu cân bằng dọc (phần tử cuối kết
    thúc trong khoảng top:1420–1500px) từ lần dựng đầu.
  - Transcript (Gemini `gemini-flash-latest`, do Whisper không cài trên sandbox) khớp gần như
    tuyệt đối với SCRIPT.md cho cả 7 dòng, kể cả số liệu ("1,35 tỷ đô la Mỹ", "200 triệu đô la Mỹ",
    "11 tháng 9", "hơn 11 tỷ đô la Mỹ") — không câu nào "chế thêm". Một lỗi ASR không đáng kể
    ("Analog Device" thiếu "s" 1 lần trong dòng 5, các lần khác đọc đúng "Analog Devices") — lỗi
    nhận dạng giọng nói, không phải giọng đọc sai.
  - Caption dùng để đăng = CAPTION.md đã qua GATE B ở trên, không sửa tay thêm claim mới.

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh công bố chính thức Analog Devices/Alif Semiconductor (qua endpoint ?image=), có dẫn nguồn GenK trong Brand Anchor + badge Hook; nhạc Lyria tự sinh, không lời, không lấy từ nguồn ngoài; SFX từ palette repo videos/astra-openai/assets/sfx/"
claims_verified:
  - "Ngày 11/9/2026 ADI ký thỏa thuận mua Alif Semiconductor — đối chiếu ?article=9d74dd6b74c8"
  - "Giá trị 1,35 tỷ USD tiền mặt + tối đa 200 triệu USD thưởng điều kiện — đối chiếu bài gốc"
  - "Dự kiến khép lại trước cuối 2026, chờ duyệt chống độc quyền Hart-Scott-Rodison tại Mỹ — đối chiếu bài gốc"
  - "Alif trụ sở California, chip AI-native tích hợp NPU, xử lý tại thiết bị — đối chiếu bài gốc"
  - "ADI doanh thu hơn 11 tỷ USD năm tài chính 2025 — đối chiếu bài gốc"
  - "Thương vụ mở rộng thị trường ADI sang trung tâm dữ liệu, quốc phòng, robot, y tế số, thiết bị đeo — đối chiếu phát ngôn CEO Vincent Roche trong bài gốc"
sensitive_flags: []
vietnam_legal_flags: []
notes: "Style claim_style index 6 (7-timeline-chronology). Voice ElevenLabs eleven_v3, voice Khánh Lâm, speed 1.09, 7 dòng riêng, tổng voice 72.78s + đệm 0.3s/frame = 74.877s thiết kế, render thực tế 74.9s (dưới 75s). BGM Lyria calm (density 0.25, brightness 0.4, negative-prompt bắt buộc), carve --strength 0.4 áp dụng thành công, data-volume 0.30. npm run check: 0 lỗi. Đã sửa 1 lỗi cân bằng dọc ở frame CTA trước khi duyệt (xem GATE C). Lưu ý vận hành: phát hiện một phiên routine khác chạy song song trong cùng khung giờ chiều 14/9 đã hoàn tất + commit video khác (ai-dap-phanh-cuoc-dua-sieu-tri-tue, GATE C APPROVE) — đã merge lịch sử git an toàn, không mất dữ liệu của phiên nào; quyết định có đăng video này lên Facebook/YouTube hay giữ lại do trùng khung giờ được báo cáo riêng cho người dùng, không tự ý đăng thêm."
