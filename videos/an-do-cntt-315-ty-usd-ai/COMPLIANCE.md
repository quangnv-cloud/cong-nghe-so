# COMPLIANCE — an-do-cntt-315-ty-usd-ai
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-14T01:15:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): YELLOW — tin công nghệ thông thường (ra mắt mô hình tính phí mới, số liệu tài
  chính doanh nghiệp) có yếu tố nhạy cảm phụ: **AI và việc làm** (mô hình kim tự tháp tuyển kỹ sư
  trẻ đang mất dần). Không thuộc bất kỳ loại BỎ TIN nào ở GATE A (không cáo buộc hình sự / chính
  trị / y tế "thuốc thần" / tài chính "cam kết lãi" / deepfake / bóc lột trẻ em / bạo lực / lừa đảo).

GATE B (content): GREEN
  B1. Mọi số liệu (315 tỷ USD, 80%, ×2, 25–30%, +16%, ~33%, +1–3%) đều truy được về
      `?article=275a5169efcb` / BRIEF.md. Không con số tự bịa. Câu CTA đặt câu hỏi mở thay vì
      kết luận "kỹ sư sẽ mất việc" như sự thật tuyệt đối.
  B2. Không bạo lực / thù ghét / quấy rối / doxxing / nội dung tình dục — chỉ trích hành vi kinh
      doanh (mô hình tính phí), không nhắm cá nhân.
  B3. Không giả danh nền tảng / hãng / chuyên gia. Không testimonial giả, không engagement bait,
      không link lạ trong caption.
  B4. Giọng AI narrator chung (ElevenLabs Khánh Lâm) = GREEN, không cần disclosure. Ảnh Hook /
      Article Image Card dùng nguyên og:image từ `?image=275a5169efcb` (ảnh thật, có dẫn nguồn
      GenK) — KHÔNG chỉnh sửa nội dung ảnh. Không có ảnh AI tái dựng cảnh thật/người thật.
  B5. Ảnh chỉ từ endpoint `?image=`, không watermark bị xoá. Nhạc nền Lyria tự sinh (không lời).
      SFX từ palette repo (`videos/astra-openai/assets/sfx/`). Video 100% tự dựng qua hyperframes,
      không reup.
  B6. Tiêu đề "Ngành CNTT Ấn Độ 315 tỷ USD chao đảo vì AI, kỹ sư giá rẻ đứng trước nguy cơ" = sự
      kiện + số liệu, không giật gân sai sự thật. Thumbnail (frame Hook) phản ánh đúng nội dung.
      Caption không nhồi hashtag, hashtag liên quan chủ đề.
  B7. Góc trình bày riêng: ẩn dụ "bản đồ lãnh thổ doanh nghiệp" (style 5-map-and-geo) so sánh nhóm
      tập đoàn lớn vs nhóm tầm trung tăng trưởng nhanh hơn nhờ AI — không chỉ đọc lại tiêu đề báo.
      Bố cục khác các video trước (không trùng video gần nhất `a20-pro-vuot-cpu-desktop`, style
      4-split-comparison). Act 7 CTA bám đúng câu hỏi tranh luận của tin.
  B8. Không chạm an ninh mạng / an ninh quốc gia / bầu cử / dữ liệu cá nhân / quảng cáo có điều
      kiện — vietnam_legal_flags rỗng.

GATE C (final): PASS
  - Xem lại thumbnail + các frame render (Hook, What happened, Key facts, Data moment, Context,
    Impact, CTA) qua ffmpeg frame-extract + Read — brand đúng (#4C8DFF/#0B0E14/#FF8A5B), cân bằng
    dọc đạt yêu cầu (nội dung mỗi frame trải tới vùng top:1300–1650px, không trống đen nửa dưới
    ~1000px như lỗi đã ghi nhận trước đây), không phần tử bịa.
  - Transcript (Gemini `gemini-flash-latest`, do Whisper host bị chặn ở sandbox) khớp gần như
    tuyệt đối với SCRIPT.md — không câu nào "chế thêm" khi sinh voice, không lỗi đọc lắp/viết tắt.
  - Caption dùng để đăng = CAPTION.md đã qua GATE B ở trên, không sửa tay thêm claim mới.

decision: APPROVE
risk_level: YELLOW
ai_disclosure_required: false
copyright_notes: "ảnh og:image bài GenK (qua endpoint ?image=), có dẫn nguồn trong Brand Anchor + badge Hook; nhạc Lyria tự sinh, không lời, không lấy từ nguồn ngoài; SFX từ palette repo videos/astra-openai/assets/sfx/"
claims_verified:
  - "315 tỷ USD/năm quy mô ngành CNTT Ấn Độ — đối chiếu ?article=275a5169efcb"
  - "80% hợp đồng TCS gắn hiệu quả thực tế, tăng gấp đôi từ khi AI bùng nổ — đối chiếu bài gốc, phát ngôn CEO TCS Krithivasan"
  - "Đối tác yêu cầu giảm 25–30% chi phí — đối chiếu phát ngôn CEO Persistent Systems Sandeep Kalra"
  - "Quý II: Persistent Systems +16%, Coforge +~33%, TCS/Infosys/Wipro/HCLTech +1–3% — đối chiếu bài gốc"
sensitive_flags:
  - "AI và việc làm — framing trung lập, không kết luận tuyệt đối, CTA đặt câu hỏi mở mời tranh luận"
vietnam_legal_flags: []
notes: "Style claim_style index 4 (5-map-and-geo). Voice ElevenLabs eleven_v3, voice Khánh Lâm, speed 1.09, 7 dòng riêng. BGM Lyria calm (density 0.25, brightness 0.4), carve --strength 0.4 áp dụng thành công. Tổng thời lượng video 70.97s (dưới 75s)."
