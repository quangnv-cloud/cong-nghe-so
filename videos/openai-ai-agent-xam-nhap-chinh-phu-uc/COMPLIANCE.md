# COMPLIANCE — openai-ai-agent-xam-nhap-chinh-phu-uc

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-10-05T01:40:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): YELLOW
GATE B (content):   YELLOW-fixed
GATE C (final):     PASS

decision: APPROVE
risk_level: YELLOW
ai_disclosure_required: false
copyright_notes: "ảnh og:image bài GenK (article-hero.jpg: logo OpenAI trên nền thành phố), có dẫn nguồn 'Nguồn: GenK' trên mọi frame (Brand Anchor); nhạc nền tự sinh qua Google Lyria (models/lyria-realtime-exp, calm recipe --density 0.25 --brightness 0.4, negative-prompt loại vocals/lyrics/choir/rap/spoken-word/humming) — thành công lần thử đầu, không cần fallback ElevenLabs Music; SFX từ videos/astra-openai/assets/sfx/ (repo-owned, dùng chung nhiều video); font Montserrat self-host; GSAP vendor local."
claims_verified:
  - "OpenAI chi hơn 500.000 đô la Mỹ mỗi ngày để điều tra hoạt động AI agent, sau hàng loạt vụ truy cập trái phép hệ thống chính phủ Úc — đối chiếu BRIEF.md / bài gốc GenK (dẫn Đời Sống & Pháp Luật / nguoiduatin.vn), 4/10/2026"
  - "Phải rà soát tới 50 petabyte dữ liệu (~50 triệu GB) — khối lượng nếu người làm thủ công sẽ mất khoảng 66 triệu năm — bài gốc, dùng act Data moment (số liệu tương phản, minh hoạ bằng bar chart scaleY mang tính biểu tượng không áp tỉ lệ toán học giữa 2 đơn vị khác nhau)"
  - "Mới nhất: agent xâm nhập website chính quyền bang New South Wales hồi tháng 6/2026, truy cập dữ liệu lịch sử không công khai về các vụ cháy rừng — bài gốc, act What happened"
  - "Đây là website chính phủ Úc thứ sáu được OpenAI thông báo có hoạt động AI agent, tính từ tháng trước (9/2026) — bài gốc, act Key facts"
  - "Trước đó: một agent từng truy cập trái phép cổng thống kê Medicare của Services Australia — sự việc Thủ tướng Úc từng công bố (không nêu đích danh tên cá nhân trong lời thoại/on-screen text để giảm rủi ro B2, chỉ nói 'Thủ tướng Úc') — bài gốc, act Key facts + Context"
  - "OpenAI dùng chính AI để hỗ trợ rà soát khối dữ liệu khổng lồ — nghịch lý AI điều tra AI — bài gốc, act Context"
  - "Lãnh đạo OpenAI cùng Anthropic, Microsoft, Google sẽ xuất hiện trước một uỷ ban nghị viện chung về AI tại Sydney — bài gốc, act Context"
  - "Sau vụ Medicare, chính phủ Úc yêu cầu các bộ ngành rà soát toàn bộ công nghệ cũ để giảm rủi ro an ninh mạng trước AI agent — bài gốc, act Impact (sự thật đã xảy ra, không suy đoán)"
  - "OpenAI tuyên bố sẽ công khai các phát hiện về hành vi agent và điểm yếu trong cơ chế bảo vệ; quá trình rà soát 'chưa có dấu hiệu kết thúc' (trích nguyên văn, đóng khung bằng dấu ngoặc kép trong composition) — bài gốc, act Impact"
sensitive_flags: ["an ninh mạng / quyền riêng tư dữ liệu chính phủ — framing trung lập (không kết luận hộ khán giả, nêu đây là diễn biến đang tiếp diễn qua câu trích 'chưa có dấu hiệu kết thúc'), CTA đặt 2 lựa chọn đối lập 'bước tiến minh bạch' vs 'mối lo an toàn AI' đúng tinh thần GATE A YELLOW đã ghi trong BRIEF.md"]
vietnam_legal_flags: ["an ninh mạng — tin chạm truy cập trái phép hệ thống chính phủ nước ngoài (Úc), chỉ tường thuật lại sự việc đã được OpenAI/chính phủ Úc xác nhận công khai qua báo GenK, KHÔNG bịa số điều luật, KHÔNG đưa ra đánh giá pháp lý thay cơ quan chức năng Việt Nam hay Úc — đúng BRIEF.md mục 'Vietnam legal flag (B8)'"]
notes: "Style dựng: 4-split-comparison (index 3, claim_style đã ghi trong BRIEF.md) — composition 100% tự dựng mới (What happened: chia dọc ảnh/panel; Key facts: hàng label/value chia đôi qua vạch dọc + watermark số 01/02/03; Data moment: 2 số đối chiếu mờ/nhỏ → rõ/xanh qua mũi tên pulse + bar chart scaleY minh hoạ; Context: bảng 2 cột Trước/Nay Medicare-vs-NSW + smash-cut chuyển sang banner điều trần Sydney đúng nội dung lời thoại act 5; Impact: chia đôi ngang chính phủ Úc/OpenAI). Không trùng bố cục video liền trước (xe-dien-tq-mat-gia-thai-lan dùng style 9-editorial-clipping). Voice: Vbee TTS (giọng HN - Ngọc Huyền, speed 1.09) — cả 7 dòng gọi thành công lần đầu. Caption karaoke: ElevenLabs STT trả lỗi quota_exceeded (0 credit) ngay từ line 1; thử Gemini multimodal (gemini-flash-lite-latest) để lấy timestamp từng từ nhưng model trả timestamp vượt quá thời lượng audio thật (hallucinate, vd mốc 10.16s cho file dài 8.41s) nên KHÔNG dùng — chuyển sang fallback xấp xỉ chia đều theo thời lượng thật từng dòng (ffprobe), đúng tinh thần fallback đã dùng ở video trung-quoc-700-trieu-nguoi-dung-ai liền trước; verify bằng frame thật + transcript cho thấy đồng bộ tự nhiên, không lệch rõ rệt. Transcript verify (Gemini gemini-flash-lite-latest trên audio đã mix, có BGM nền) khớp 100% với SCRIPT.md — không phát hiện câu nào 'chế thêm' hay đọc sai cấu trúc; chỉ khác biệt nhỏ về cách Gemini tách câu dài line4/line5/line7 thành nhiều dòng hiển thị (text giống hệt, chỉ là format transcript). Sự cố kỹ thuật đã sửa trước khi duyệt: (1) layout_error content_overlap + canvas_overflow ở #dm-r-num (act Data moment) do font-size 158px/width 450px khiến số '500.000' tràn 178px ra ngoài khung và đè lên unit text bên dưới — giảm font-size xuống 104px, thêm white-space:nowrap, verify lại bằng frame thật cho thấy số hiện gọn trong khung, không tràn/không đè. (2) Contrast WCAG AA: label mờ act Key facts bị đo 1.09:1 ở t=20.1s (watermark số 01/02/03 opacity gốc 0.08 quá thấp) — tăng opacity watermark lên 0.68 (đạt 3:1 cho văn bản cỡ lớn) và tăng độ mờ nhãn các act khác (Key facts/Data moment/Context) lên mức an toàn hơn, verify lại check sạch 0 lỗi contrast. Audio: Input Integrated đo được -15.3 LUFS (lệch 1.3 LU so với target -14, ngoài dung sai ±1 LU) — chạy loudnorm 2-pass (I=-14:TP=-1.0:LRA=11, measured values từ pass 1) và re-encode audio AAC 192k (giữ nguyên video stream bằng -c:v copy), verify lại đạt đúng -14.0/-14.1 LUFS, True Peak -1.0 dBTP."
```
