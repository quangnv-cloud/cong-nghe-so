# COMPLIANCE — chuyen-gia-tq-day-ai-thay-minh
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-15T14:10:15Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): YELLOW — tin công nghệ/AI thường có yếu tố nhạy cảm phụ "AI & việc làm";
  không phải chính trị/bầu cử/xung đột/y tế/tài chính-cam-kết-lãi/deepfake/khai-thác-trẻ-em — không
  bị BỎ ở GATE A. Framing trung lập (nêu cả góc "thêm thu nhập" lẫn "nguy cơ mất việc"), không kết
  luận thay khán giả (act 7 để ngỏ câu hỏi).

GATE B (content): GREEN
  B1 Sự thật & nguồn: mọi số liệu (50.000 chuyên gia Xpert/ByteDance, nền tảng Siriser/Alibaba,
     15-74 USD/nhiệm vụ, 1,1 tỷ USD thị trường dữ liệu huấn luyện AI Trung Quốc 2026 +25% theo IDC,
     ví dụ kỹ sư phần mềm Thượng Hải bị thay bằng lao động hợp đồng) đối chiếu đúng BRIEF.md /
     `?article=20bc23846203`. Không con số tự bịa. Act 6 (Impact) là sự thật đã xảy ra ("công ty đã
     thay một số kỹ sư toàn thời gian bằng lao động hợp đồng"), không suy đoán tương lai.
  B2 An toàn cộng đồng: không bạo lực/thù ghét/quấy rối/doxxing/nội dung tình dục hay trẻ em. Phê
     bình hiện tượng thị trường lao động, không nhắm cá nhân.
  B3 Chính hãng: kênh không mạo nhận ByteDance/Alibaba/IDC/GenK; không testimonial giả, không
     engagement bait, không link lừa đảo.
  B4 AI/synthetic media: giọng ElevenLabs "Khánh Lâm" = GREEN không cần disclosure. Ảnh Hook/Article
     Image Card lấy từ `?image=20bc23846203` (og:image bài báo GenK, có dẫn nguồn) = GREEN, không
     chỉnh sửa bịa nội dung. Không có cảnh AI tái dựng người thật/sự kiện thật như ảnh chụp.
     ai_disclosure_required = false.
  B5 Bản quyền: ảnh từ `?image=`, nhạc nền Lyria tự sinh (Google Lyria RealTime, prompt calm ambient
     instrumental, negative-prompt loại vocal), SFX từ bộ SFX repo (astra-openai). Video tự dựng
     100% qua HyperFrames, không reup.
  B6 Tiêu đề/thumbnail: tiêu đề "Trung Quốc: hàng nghìn chuyên gia kiếm tiền bằng cách dạy AI làm
     thay chính mình" = sự kiện + số liệu, không giật gân sai sự thật. Thumbnail (frame Hook, t=4s)
     phản ánh đúng nội dung. Caption không nhồi hashtag (6 hashtag liên quan chủ đề).
  B7 Nguyên bản: góc trình bày riêng — style "10-stock-terminal" (bảng benchmark/terminal, sparkline)
     áp cho 5 act giữa, khác bố cục các video gần nhất (9-editorial-clipping, 6-ring-progress...).
     Act 7 CTA đặt đúng câu hỏi tranh luận riêng của tin ("khôn ngoan hay tự đẩy nhanh nguy cơ mất
     việc?"), không bait chung chung.
  B8 Pháp lý VN: không chạm an ninh mạng/an ninh quốc gia/bầu cử/y tế/quảng cáo có điều kiện — tin
     là hiện tượng thị trường lao động Trung Quốc, không liên quan pháp lý VN trực tiếp.

GATE C (final):     PASS
  - Verify 1 (duration): ffprobe = 71.500000s, khớp thiết kế data-duration="71.50" của index.html.
  - Verify 2 (silencedetect noise=-35dB:d=0.6): không có khoảng lặng chết giữa video; chỉ có
    silence 70.90s→71.51s (0.61s) ở đúng đoạn fade-out BGM cuối clip — đúng thiết kế.
  - Verify 3 (frame check): trích + xem 15 frame trải đều 7 act (t=2,4,9,19,27,30,33,39,45,51,58,
    63,65,68,70s). Brand anchor (logo "Công Nghệ Số" góc trên-phải, "Nguồn: GenK" góc trên-trái)
    đúng vị trí xuyên suốt. Cân bằng dọc: trạng thái "đã hiện đủ" của mỗi act kết thúc trong dải
    top ~1400-1690px (03-facts ~1450px, 04-data ~1420px, 05-context ~1400px, 06-impact ~1440px,
    07-cta ~1690px) — không có nửa dưới trống đen tĩnh; các khung "trống" bắt gặp khi trích frame
    chỉ là trạng thái giữa-animation (reveal chưa tới), không phải bug bố cục. Thumbnail (t=4s, sau
    khi animation Hook ổn định) hiện đủ rõ logo + tên kênh + badge nguồn + tiêu đề + 2 tag tương
    phản, không mờ/cắt.
  - Verify 4 (transcript vs SCRIPT.md): dùng Gemini multimodal (`gemini-3.5-flash-lite` —
    `gemini-flash-latest`/`gemini-omni-1.1-flash` bị 429/503 hết quota free-tier lúc chạy; Whisper
    cục bộ bị chặn egress `openaipublic.azureedge.net` đúng như PRODUCTION-WORKFLOW.md đã lường
    trước). Transcript khớp SCRIPT.md cả 7 dòng, không câu nào "chế thêm". 1 sai khác chấp nhận
    được: dòng 3 ASR nghe nhầm "Xpert (ByteDance)" thành "Expert (Baidu)" — âm gần giống + model
    STT tự "sửa" theo tên hãng quen thuộc hơn, không phải lỗi kịch bản/giọng đọc (script/audio gốc
    đúng "Xpert"/"ByteDance", đối chiếu BRIEF.md).
  - Caption dùng để đăng = CAPTION.md đã qua GATE B, không sửa tay thêm claim mới.

decision: APPROVE
risk_level: YELLOW
ai_disclosure_required: false
copyright_notes: "ảnh Hook/Article Image Card lấy từ ?image=20bc23846203 (og:image GenK, có dẫn nguồn); nhạc nền Lyria tự sinh (Google Lyria RealTime, instrumental, không lời); SFX từ bộ SFX repo dùng chung (videos/astra-openai/assets/sfx)"
claims_verified:
  - "Nền tảng Xpert của ByteDance tuyển hơn 50.000 chuyên gia từ 2025 — đối chiếu ?article=20bc23846203"
  - "Alibaba vận hành Siriser, tuyển giáo viên/kỹ sư cơ khí làm huấn luyện viên AI — đối chiếu ?article="
  - "Thù lao mỗi nhiệm vụ 15-74 USD — đối chiếu ?article="
  - "Thị trường dữ liệu huấn luyện AI Trung Quốc dự báo 1,1 tỷ USD năm 2026, tăng 25% (IDC) — đối chiếu ?article="
  - "Một kỹ sư phần mềm Thượng Hải: công ty đã thay một số kỹ sư toàn thời gian bằng lao động hợp đồng — đối chiếu ?article="
sensitive_flags: ["AI & việc làm — framing trung lập, không kết luận thay khán giả"]
vietnam_legal_flags: []
notes: "Video này resume từ WIP tạo lúc routine chiều 15/9/2026 (script/voice/composition/GATE A/B đã xong), bị chặn ở bước BGM do sandbox lúc đó thiếu lyria-recipe.py/carve.mjs. Routine tối 15/9/2026 chạy bước 0 (cài skill hyperframes qua `npx hyperframes@0.8.30 skills` + `pip install google-genai` + apt install ffmpeg) rồi hoàn tất BGM/carve/check/render/verify/GATE C. Đã sửa 1 lỗi layout content_overlap (05-context.html .cx-bars height cố định gây tràn) + 3 lỗi contrast WCAG (ticker rgba mờ) + 1 GSAP lint warning (immediateRender) phát hiện ở `npm run check` trước khi render."
