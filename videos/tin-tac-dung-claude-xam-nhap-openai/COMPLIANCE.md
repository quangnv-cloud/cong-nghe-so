# COMPLIANCE — tin-tac-dung-claude-xam-nhap-openai

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-20T14:45:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): YELLOW
GATE B (content):   YELLOW-fixed
GATE C (final):     PASS

decision: APPROVE
risk_level: YELLOW
ai_disclosure_required: false
copyright_notes: "ảnh minh hoạ ý niệm (bóng người hoodie trước laptop, ánh sáng đỏ, logo OpenAI mờ phía sau) lấy qua ?image= của Apps Script (og:image bài GenK, có dẫn nguồn); không phải ảnh chụp người thật/cảnh thật cụ thể; nhạc nền Lyria tự sinh (calm ambient, không lời, prompt --density 0.25 --brightness 0.4 + negative-prompt bắt buộc); SFX từ bộ SFX chuẩn của kênh (astra-openai/assets/sfx)."
claims_verified:
  - "3 nhà nghiên cứu bảo mật (công ty Hacktron) dùng Claude đột nhập kho mã nguồn nội bộ OpenAI, chưa đầy 3.000 USD, dưới 72 giờ — đối chiếu ?article=d7ccda7d2991 (GenK, dẫn WSJ)"
  - "PR #1186742 gửi ngày 25/7/2026 qua tài khoản Codex của nhân viên kỹ thuật OpenAI — đối chiếu ?article=d7ccda7d2991"
  - "Khai thác lỗ hổng diễn đàn OpenAI (từ 23/7) + chiếm tài khoản nhân viên — đối chiếu ?article=d7ccda7d2991"
  - "Ban đầu thất bại với Claude Opus 4.8; đột phá khi Anthropic phát hành Claude Opus 5 (24/7/2026) — đối chiếu ?article=d7ccda7d2991"
  - "Nhóm ngụy trang hệ thống thử nghiệm thành bài kiểm tra an ninh mạng dạng giải đố (CTF) để qua mặt rào an toàn của Claude — đối chiếu ?article=d7ccda7d2991"
  - "Thư viện mã nguồn mở libheif phát hành 37 cảnh báo an toàn từ tháng 1-8/2026 — đối chiếu ?article=d7ccda7d2991"
  - "OpenAI vá lỗi SSO ngay trong đêm 25/7; Discourse vá lỗi xử lý ảnh 28/7; OpenAI trao 6.500 USD tiền thưởng ngày 1/9/2026 — đối chiếu ?article=d7ccda7d2991"
sensitive_flags: ["An ninh mạng — đây là nghiên cứu bảo mật hợp pháp qua chương trình bug bounty của chính OpenAI (Hacktron báo cáo có trách nhiệm, dừng ngay sau khi xác nhận lỗ hổng, không xem mã nguồn nhạy cảm), KHÔNG phải hướng dẫn tấn công; video không đi sâu chi tiết kỹ thuật có thể tái sử dụng để khai thác (không nêu cụ thể thư viện/CVE/đoạn mã), framing trung lập nêu rõ đây là bug bounty đã được vá và thưởng."]
vietnam_legal_flags: []
notes: "Sự việc xảy ra ở Mỹ (OpenAI, Anthropic, Hacktron), không liên quan trực tiếp luật an ninh mạng Việt Nam cụ thể — không có flag pháp lý VN. Không dùng AI tái dựng cảnh thật/người thật — ảnh chỉ minh hoạ ý niệm chung (bóng người hoodie, không phải chân dung có thể nhận diện). Transcript (Gemini flash-latest STT, Whisper host bị chặn ở sandbox) khớp 100% với SCRIPT.md, không có câu nào 'chế thêm'. Nguyên bản (GATE B7): tổng hợp 3 tầng thông tin rải rác trong bài gốc (sự kiện chính → cách làm/vai trò Claude Opus 4.8→5 + mẹo giả CTF → hệ quả ngành mất cân bằng tấn công/phòng thủ) thành 1 mạch phân tích riêng, không chỉ đọc lại tiêu đề báo. Style 10-stock-terminal (index 9) — ẩn dụ terminal/benchmark hợp chủ đề an ninh mạng, không trùng bố cục video routine gần nhất (8-icon-grid ngày 18/9 về chủ đề khác — AI agent tự chủ)."
```

## Ghi chú kiểm tra chi tiết

- **GATE A**: tin công nghệ/AI có yếu tố nhạy cảm phụ (an ninh mạng) → YELLOW. Xác nhận đây KHÔNG thuộc danh mục BỎ (không phải cáo buộc hình sự/chính trị/y tế "thuốc thần"/tài chính "cam kết lãi"/deepfake/khai thác trẻ em/bạo lực/lừa đảo) — là báo cáo về nghiên cứu bảo mật hợp pháp đã qua chương trình bug bounty chính thức của OpenAI, có nguồn WSJ + GenK rõ ràng. Tiếp tục dựng với framing trung lập.
- **GATE B**: đã rà B1–B8 trước render (ghi trong BRIEF.md). Mọi số liệu (3.000 USD, 72 giờ, 25/7, PR #1186742, Opus 4.8→5, 37 cảnh báo, 6.500 USD, 1/9) đều truy được về `?article=d7ccda7d2991`; không bịa số liệu; phê bình hành vi/lỗ hổng kỹ thuật, không nhắm cá nhân cụ thể; không giả danh OpenAI/Anthropic/Hacktron; ảnh AI chỉ minh hoạ ý niệm (GREEN, không cần disclosure); tiêu đề "3 tin tặc dùng Claude đột nhập kho mã OpenAI" bám đúng sự kiện, không giật gân sai sự thật; không có hướng dẫn khai thác actionable (B2 — không nêu chi tiết kỹ thuật CVE/thư viện/đoạn mã cụ thể).
- **GATE C** (sau render, bản render thứ 2 sau khi sửa lỗi QA): đã xem thumbnail + 6 frame thật ở các mốc t=4/7/18/27/34/46/60/68s (đủ cả 7 act) — không phần tử bịa, đúng brand (#4C8DFF/#0B0E14/#FF8A5B, Montserrat, không emoji). Cân bằng dọc: act 3 (Key facts) card cuối kết thúc ~top:1650px, act 5 (Context) quote box kết thúc ~top:1650px, act 6 (Impact) card cuối kết thúc ~top:1650px — đều đạt dải 1400–1680px yêu cầu (đã sửa từ bản render đầu tiên bị lỗi trống đen). Hook: chữ "OpenAI" trước đó bị cắt ở bản render đầu (font-size 74px tràn khung), đã sửa xuống 66px và xác nhận hiển thị đầy đủ trong bản render thứ 2. Transcript (Gemini flash-latest, Whisper host bị chặn ở sandbox) khớp 100% với SCRIPT.md. Caption dùng để đăng = CAPTION.md đã qua GATE B, không sửa thêm.
- **Sự cố kỹ thuật đã sửa trước khi duyệt (2 vòng QA)**:
  1. Bản render đầu tiên: chữ "đột nhập kho mã OpenAI" ở Hook bị cắt (tràn khung, chỉ hiện "OpenA") — do `font-size:74px` vượt độ rộng khung 952px. Đã giảm xuống 66px, xác nhận đủ margin qua đo pixel thật.
  2. Bản render đầu tiên: 3 act giữa (Key facts, Context, Impact) có khoảng trống đen lớn ở nửa dưới khung (phần tử cuối chỉ kết thúc quanh top:1400-1450px, để trống ~250-280px trước caption) — vi phạm quy tắc "Cân bằng dọc" của BRAND-SYSTEM.md. Đã phóng to card/biểu đồ + giãn khoảng cách, xác nhận phần tử cuối mỗi act giờ kết thúc quanh top:1650px qua cả đo pixel (Playwright) và frame render thật.
  3. Cả 2 lỗi đã render lại bản thứ 2, verify lại đủ 5 bước + soát frame thật — đạt.

**decision: APPROVE — risk_level: YELLOW → đủ điều kiện đăng Facebook Reel + YouTube Shorts.**
