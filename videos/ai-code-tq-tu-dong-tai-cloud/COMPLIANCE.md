# COMPLIANCE — ai-code-tq-tu-dong-tai-cloud

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-22T07:30:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): YELLOW — tin công nghệ chạm yếu tố nhạy cảm phụ "quyền riêng tư / bảo mật dữ
liệu" (công cụ AI tự động tải dữ liệu người dùng lên cloud). Không phải cáo buộc hình sự / chính
trị / y tế / tài chính bị cấm ở GATE A. Đây là sự cố bảo mật sản phẩm của một công ty (Z.ai/Zhipu
AI), không nhắm cá nhân cụ thể. Tiếp tục dựng với framing trung lập.

GATE B (content): YELLOW-fixed
- B1: Mọi số liệu (313 MB, 564 lần, 15 KB, ngày 18/9, tính năng "Codebase Indexing") đều truy được
  về ?article=927c5be35e24 (GenK). KHÔNG dùng chi tiết "6 dự án bị rò rỉ / mật khẩu database" vì
  tuyên bố đó đã bị chính người đăng rút lại trong bài gốc — loại khỏi SCRIPT/CAPTION để tránh
  trình bày một claim chưa xác nhận như sự thật.
- B2: Không công kích cá nhân; phê bình sản phẩm/tính năng (ZCode, Codebase Indexing) và hành vi
  công ty (Z.ai). Tên blogger Ferstar chỉ dùng như nguồn phát hiện, không phải mục tiêu công kích.
- B3: Không giả danh nền tảng/hãng/cơ quan/chuyên gia. Không testimonial giả. CTA là câu hỏi quan
  điểm thật, không engagement bait.
- B4 (AI media): giọng ElevenLabs "Khánh Lâm" = GREEN, không cần disclosure. Ảnh Hook/Article Image
  Card lấy từ ?image=927c5be35e24 (og:image bài báo, dẫn nguồn GenK) = GREEN. Đồ hoạ style 5-map-
  and-geo (ghim địa danh, route line, bản đồ chấm nền) là minh hoạ ý niệm bằng CSS/SVG, KHÔNG phải
  ảnh AI tái dựng cảnh thật/người thật. ai_disclosure_required = false.
- B5: Ảnh chỉ từ ?image=, không watermark. Nhạc nền Lyria tự sinh (calm, density 0.25/brightness
  0.4, negative-prompt loại vocal). SFX từ bộ có sẵn trong repo (astra-openai/assets/sfx). Video
  100% tự dựng bằng hyperframes, không reup.
- B6: Tiêu đề "Công cụ AI Trung Quốc tự động tải cả dự án lập trình viên lên cloud — không có nút
  tắt" = sự kiện + số liệu ngụ ý, không giật gân sai sự thật. Thumbnail (frame Hook) phản ánh đúng
  nội dung. Caption có 📌 Nguồn + 7 hashtag liên quan, không nhồi hashtag lạ.
- B7 (nguyên bản): Góc trình bày riêng — ẩn dụ "luồng dữ liệu" (máy người dùng → máy chủ Z.ai →
  cloud Alibaba tại Trung Quốc) qua style 5-map-and-geo, không chỉ đọc lại tiêu đề báo. Không trùng
  bố cục video liền trước (chip-nvidia-vuot-cam-van-trung-quoc dùng style 4-split-comparison). Act 7
  CTA đặt đúng câu hỏi tranh luận của tin ("tiện lợi tự động hay rủi ro dữ liệu").
- B8 (pháp lý VN): Tin không chạm trực tiếp an ninh mạng/pháp luật Việt Nam (bối cảnh là công ty
  Trung Quốc, người dùng toàn cầu) — không có flag pháp lý VN cụ thể.
- Kỹ thuật: tên blogger "Ferstar" bị ElevenLabs eleven_v3 đọc sai (ElevenLabs STT nghe ra
  "Firststar") — đã bỏ khỏi lời thoại act 3 (SCRIPT.md dòng 3 sửa thành "Một blogger công nghệ
  Trung Quốc..."), tên vẫn giữ trên chữ hiển thị (03-facts.html) và trong BRIEF.md. Voice line 3 +
  STT + caption karaoke đã sinh lại đúng theo bản sửa.

GATE C (final): PASS
- Đã xem thumbnail + 7 frame render (1 mỗi act): đúng B6, không phần tử bịa, cân bằng dọc đạt
  (03-facts và 05-context ban đầu kết thúc sớm ~1330-1374px, đã sửa CSS spacing, render lại — nay
  cả hai kết thúc trong khoảng 1400-1680px như quy định).
- Transcript (ElevenLabs STT word-level + Gemini flash-lite multimodal, language=Vietnamese) khớp
  SCRIPT.md — không câu nào bị "chế thêm"; chỉ khác biệt phiên âm tên riêng chấp nhận được
  (Zi Cốt/ZCode, Zhi Pu/Zhipu/Jipu/Zepu — cùng 1 âm đọc, do ASR tự chọn cách viết).
- Caption dùng để đăng = CAPTION.md đã qua GATE B, không sửa tay thêm claim mới.

decision: APPROVE
risk_level: YELLOW
ai_disclosure_required: false
copyright_notes: "ảnh og:image bài báo GenK (?image=927c5be35e24), có dẫn nguồn; nhạc nền Lyria tự
sinh (Google, instrumental, không lời); SFX từ bộ có sẵn trong repo; logo kênh tự thiết kế"
claims_verified:
  - "ZCode / Z.ai (Zhipu AI, Trung Quốc) — đối chiếu ?article=927c5be35e24"
  - "Phát hiện 18/9/2026 bởi blogger công nghệ Trung Quốc — đối chiếu ?article="
  - "Tệp nén 313 MB, thử tải 564 lần thất bại — đối chiếu ?article="
  - "Tệp 15 KB tải lên thành công — đối chiếu ?article="
  - "Tính năng Codebase Indexing bật mặc định, không có nút tắt — đối chiếu ?article="
  - "Z.ai vô hiệu hoá tính năng, xin lỗi, vá lỗi, cam kết mở mã nguồn ZCode — đối chiếu ?article="
sensitive_flags:
  - "Quyền riêng tư / bảo mật dữ liệu — framing trung lập, chỉ dùng chi tiết đã xác nhận từ nguồn,
    không dùng tuyên bố đã bị rút lại (6 dự án / mật khẩu database)"
vietnam_legal_flags: []
notes: "Style dựng: 5-map-and-geo (index 4, claim_style). Tổng thời lượng video: 56.47s (dưới 75s).
Video liền trước (chip-nvidia-vuot-cam-van-trung-quoc) dùng style 4-split-comparison — không trùng."
```
