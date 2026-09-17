# COMPLIANCE — natif-tai-tro-ai-doanh-nghiep

policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-17T01:10:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): GREEN — tin chính sách công nghệ trong nước (Bộ Khoa học và Công nghệ /
Quỹ Đổi mới công nghệ quốc gia tài trợ AI cho doanh nghiệp). Không cáo buộc hình sự, không
chính trị/bầu cử/xung đột, không y tế "thuốc thần", không tài chính "cam kết lãi", không
deepfake, không khai thác trẻ em/bạo lực/lừa đảo.

GATE B (content): GREEN
- B1: mọi số liệu (3 tỷ đồng, 15 nhiệm vụ, 12 tháng, 10/10/2026, Nghị định 77/2026) truy được
  về `?article=4a33617f87d0` (VnExpress) / BRIEF.md. Không con số tự nghĩ.
- B2: không bạo lực/thù ghét/quấy rối/doxxing/tình dục.
- B3: không giả danh nền tảng/cơ quan/chuyên gia; CTA là câu hỏi quan điểm thật, không
  engagement bait; không link độc hại.
- B4: giọng AI narrator chung (ElevenLabs "Khánh Lâm") — không cần disclosure. Ảnh Hook/Article
  Image Card là ảnh thật từ `?image=4a33617f87d0` (VnExpress, robot hình người tại triển lãm
  ICT Comm TP.HCM), có dẫn nguồn — không tái dựng AI cảnh thật/người thật. Toàn bộ minh hoạ
  còn lại là đồ hoạ CSS/SVG (icon, card, biểu đồ) — không phải ảnh AI.
- B5: ảnh chỉ từ `?image=`; nhạc Lyria tự sinh (không lời, có negative-prompt loại vocal); SFX
  từ bộ SFX dùng chung của kênh; video 100% tự dựng, không reup.
- B6: tiêu đề = sự kiện + số liệu ("3 tỷ đồng tài trợ AI"), không giật gân sai bằng chứng;
  thumbnail phản ánh đúng nội dung; caption không nhồi hashtag.
- B7: góc nhìn riêng — tương phản "3 tỷ đồng tối đa" vs "chỉ 15 suất cả nước" (Data moment),
  câu hỏi CTA bám đúng góc tranh luận "cú hích thật hay rào cản cho doanh nghiệp nhỏ"; không
  chỉ đọc lại tiêu đề báo; style `4-split-comparison` chưa dùng liên tiếp gần đây.
- B8: tin thuộc chính sách khoa học công nghệ / tài trợ nhà nước, không phải quảng cáo tài
  chính cá nhân có điều kiện; chỉ trích dẫn đúng số Nghị định 77/2026 có trong bài gốc, không
  bịa số điều khoản.

GATE C (final): PASS
- Thumbnail (t=3.5s) + 6 frame render (t=4,12,22,28,44,56) đã xem lại bằng Read: đúng B6, logo
  + tên kênh + badge nguồn + tiêu đề + 2 tag hiện đủ rõ, không phần tử bịa, không lộ lỗi layout
  (npm run check: 0 error).
- Transcript (Gemini `gemini-flash-latest`, đối chiếu SCRIPT.md): khớp toàn bộ nội dung, không
  câu nào "chế thêm". 1 sai khác nhỏ do ASR (nghe "Nghị định 77 năm 2024" thay vì "77/2026") —
  đối chiếu lại bằng ElevenLabs STT word-level trên file `line6.mp3` gốc (không lẫn BGM) xác
  nhận giọng đọc thực tế nói đúng "77/2026" — kết luận đây là lỗi nghe của công cụ phiên âm
  full-mix (có BGM), không phải lỗi phát âm của giọng đọc.
- Caption đăng = CAPTION.md đã qua GATE B, không sửa tay thêm claim mới.
- Verify kỹ thuật: duration 60.3s (<75s); silencedetect không có khoảng lặng chết; loudnorm
  2-pass đưa Integrated về -14.4 LUFS (lệch +0.4 LU, trong ±1 LU), True Peak -1.3 dBTP (≤-1.0
  dBTP); cân bằng dọc xác nhận qua frame thật mỗi act, không trống đen bất thường.

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh og:image VnExpress (triển lãm ICT Comm, TP.HCM), có dẫn nguồn; nhạc Lyria tự sinh, negative-prompt loại vocal; SFX bộ dùng chung kênh"
claims_verified:
  - "Tài trợ tối đa 3 tỷ đồng/nhiệm vụ — đối chiếu ?article=4a33617f87d0"
  - "Dự kiến chọn 15 nhiệm vụ trong 2026 — đối chiếu ?article=4a33617f87d0"
  - "Cơ chế đồng tài trợ, doanh nghiệp đối ứng phần còn lại — đối chiếu ?article=4a33617f87d0"
  - "Thời gian thực hiện tối đa 12 tháng — đối chiếu ?article=4a33617f87d0"
  - "Hạn nộp hồ sơ 17h ngày 10/10/2026, nộp online tại oms.natif.vn, cần chữ ký số — đối chiếu ?article=4a33617f87d0"
  - "Nghị định 77/2026 về tổ chức, hoạt động của NATIF vừa có hiệu lực — đối chiếu ?article=4a33617f87d0"
sensitive_flags: []
vietnam_legal_flags: []
notes: "Tin chính sách công nghệ trong nước thông thường, không có yếu tố nhạy cảm phụ (không chạm AI & việc làm, xuất khẩu chip, quyền riêng tư, hay kiện bản quyền AI)."
