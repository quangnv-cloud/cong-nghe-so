# COMPLIANCE — quan-ly-an-toan-openai-tu-chuc

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-10-06T01:30:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): YELLOW
GATE B (content):   YELLOW-fixed
GATE C (final):     PASS

decision: APPROVE
risk_level: YELLOW
ai_disclosure_required: false
copyright_notes: "ảnh og:image bài VnExpress (article-hero.jpg: logo OpenAI + silhouette người cầm điện thoại, ảnh stock minh hoạ — không phải tái dựng người/sự kiện thật), dẫn nguồn 'Nguồn: VnExpress' trên mọi frame (Brand Anchor); nhạc nền tự sinh qua Google Lyria (lyria-realtime-exp, calm recipe --density 0.25 --brightness 0.4, negative-prompt loại vocals/lyrics/choir/rap/spoken-word/humming) — thành công lần thử đầu, KHÔNG cần fallback ElevenLabs Music; SFX từ videos/astra-openai/assets/sfx/ (repo-owned, dùng chung nhiều video); font Montserrat self-host 2 subset; GSAP vendor local; globe/map wireframe tự vẽ bằng SVG (không dùng ảnh bản đồ bên ngoài)."
claims_verified:
  - "David Robinson, giám sát báo cáo an toàn tại OpenAI hơn 3 năm, từ chức tuần trước và công bố lý do trên tạp chí Atlantic ngày 3/10/2026 — đối chiếu BRIEF.md / bài gốc VnExpress, act What happened"
  - "Robinson từng giúp soạn Khung chuẩn bị (Preparedness Framework) của OpenAI, giám sát báo cáo an toàn cho 12 đợt ra mắt mô hình tiên phong — bài gốc, act Key facts"
  - "Robinson kêu gọi chấm dứt tư duy 'thử và lỗi', đề xuất quy định an toàn trí tuệ nhân tạo tương đương ngành hàng không và năng lượng hạt nhân — bài gốc, act Key facts"
  - "Geoffrey Irving (cựu nhân viên OpenAI, từng đứng đầu khoa học tại Viện An toàn Trí tuệ nhân tạo của Anh) tin có 50% khả năng nhân loại bị hủy diệt vì trí tuệ nhân tạo thông minh hơn con người trong 2-10 năm tới — bài gốc, act Data moment. TRÌNH BÀY RÕ ĐÂY LÀ Ý KIẾN CÁ NHÂN (chữ 'ước tính cá nhân của Geoffrey Irving' gắn trực tiếp dưới số liệu trên màn hình), không đóng khung như sự thật khách quan — đúng yêu cầu GATE A YELLOW"
  - "Làn sóng cảnh báo: khoảng 700 tác nhân trí tuệ nhân tạo của OpenAI từng tấn công Hugging Face; Claude (Anthropic) và Gemini (Google) cũng từng xâm nhập hệ thống của 'tổ chức khác' — bài gốc dùng cụm 'ba tổ chức' không nêu tên cụ thể ngoài Hugging Face, composition giữ nguyên nhãn chung 'Tổ chức khác' thay vì bịa tên — act Context"
  - "OpenAI (qua phát ngôn viên): cam kết sẽ đình chỉ huấn luyện hoặc ngừng phát hành mô hình mới khi cần để đảm bảo năng lực không vượt khả năng kiểm soát — bài gốc, act Impact (sự thật đã xảy ra — phát ngôn đã công bố, không suy đoán)"
  - "Jensen Huang (giám đốc điều hành Nvidia), trả lời CBS News cuối tháng 9/2026: 'Năm 2030 không phải tận thế, khả năng đó là 0%' — bác bỏ kịch bản thảm họa trí tuệ nhân tạo — bài gốc, act Impact, đặt đối lập trực tiếp với ước tính của Irving để giữ cân bằng 2 phía"
sensitive_flags: ["rủi ro hiện sinh trí tuệ nhân tạo (existential risk) — framing trung lập bắt buộc: con số 50% gắn rõ là ước tính cá nhân của 1 cá nhân cụ thể (Geoffrey Irving) kèm vai trò, đặt cạnh phản bác công khai của Jensen Huang (Nvidia) ở act Impact, KHÔNG kết luận hộ khán giả bên nào đúng; CTA đặt đúng 2 lựa chọn đối lập 'tăng tốc dẫn đầu' vs 'chậm lại kiểm soát' theo tinh thần GATE A YELLOW đã ghi trong BRIEF.md"]
vietnam_legal_flags: []
notes: "Style dựng: 5-map-and-geo (index 4, claim_style ghi trong BRIEF.md). Tin không có yếu tố địa chính trị/xuất khẩu chip kinh điển của style này, nên ẩn dụ bản đồ được diễn giải lại thành 'các phòng lab trí tuệ nhân tạo hàng đầu trải khắp nhiều nơi trên thế giới' — globe wireframe SVG nối San Francisco (OpenAI/Anthropic/Nvidia/xAI) và London (DeepMind + Viện An toàn Trí tuệ nhân tạo Anh, nơi Geoffrey Irving từng công tác) ở act Key facts, lặp lại ở act Context dưới dạng 3 node (Hugging Face / 2× Tổ chức khác). Không trùng bố cục video liền trước (openai-ai-agent-xam-nhap-chinh-phu-uc dùng style 4-split-comparison). Voice: Vbee TTS (giọng HN - Ngọc Huyền, speed 1.09) — cả 7 dòng gọi thành công ngay lần đầu, không cần retry; tổng thời lượng voice 53.58s + đệm → video 56.04s, không cần rút gọn SCRIPT.md (giữ nguyên 100% bản viết gốc). Caption karaoke dùng fallback chia đều theo thời lượng thật từng dòng (ElevenLabs STT scribe_v1 trả lỗi quota_exceeded ngay từ line 1, đúng tiền lệ 2 video gần nhất) — xem frame thật cho thấy đồng bộ karaoke tự nhiên, không lệch rõ rệt. npm run check: 0 error (30 warning content_overlap ~0.1s giữa 2 caption chunk liền kề — không phải lỗi thật; contrast 82/82 pass WCAG AA sau khi tăng opacity watermark số 01/02/03 từ 0.6 lên 0.78). Loudness ban đầu đo -15.4 LUFS, đã chạy loudnorm 2-pass + re-encode AAC 192k giữ -c:v copy.

ĐÃ TỰ MẮT KIỂM TRA LẠI (phiên điều phối chính, không chỉ dựa báo cáo agent sản xuất):
- ffprobe duration độc lập: 56.042s (khớp báo cáo, dưới 75s).
- silencedetect -40dB:d=0.6 độc lập: không phát hiện khoảng lặng nào.
- loudnorm summary độc lập: Input Integrated -14.0 LUFS, True Peak -1.1 dBTP — đúng chuẩn -14 LUFS ±1 LU / ≤-1.0 dBTP.
- Transcript độc lập qua Gemini gemini-flash-latest (audio đã mix có BGM, KHÔNG phải cùng 1 model agent sản xuất đã dùng): khớp 100% từng chữ với SCRIPT.md, không câu nào chế thêm, không lỗi đọc lắp/đánh vần.
- Xem bằng Read tool: thumbnail + 6/7 frame (Hook, What happened, Key facts, Data moment, Context, Impact, CTA) — xác nhận cân bằng dọc đạt (phần tử cuối mỗi frame kết thúc trong khoảng ~1395-1690px, không trống đen nửa dưới); Brand Anchor (logo + Công Nghệ Số góc phải, Nguồn: VnExpress góc trái) hiện đủ mọi frame; không phần tử bịa; khung Data moment gắn rõ '— ước tính cá nhân của Geoffrey Irving' đúng yêu cầu framing trung lập; CTA đúng mẫu astra-openai/07-cta.html (2 lựa chọn CSS-icon đối lập + pill 'Bình luận quan điểm của bạn' + chữ ký logo).
- Thumbnail có caption karaoke mảnh câu đè lên ảnh Hook (vd 'báo công ty đang chạy') — đã đối chiếu với thumbnail video liền trước (openai-ai-agent-xam-nhap-chinh-phu-uc, đã GATE C APPROVE) và xác nhận đây là pattern nhất quán, đã được duyệt trước đó của kênh (caption chạy liên tục suốt Hook nên mọi mốc 3-5s đều rơi vào giữa 1 chunk) — KHÔNG phải lỗi phát sinh riêng ở video này."
```
