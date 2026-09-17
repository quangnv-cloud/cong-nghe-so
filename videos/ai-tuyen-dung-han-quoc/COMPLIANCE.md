# COMPLIANCE — ai-tuyen-dung-han-quoc

policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-16T07:15:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): YELLOW — tin công nghệ/nhân sự thông thường (khảo sát chính thức của Bộ Việc
làm và Lao động Hàn Quốc về ứng dụng trí tuệ nhân tạo trong tuyển dụng tại các doanh nghiệp lớn),
không cáo buộc hình sự/bê bối cá nhân, không chính trị/bầu cử/xung đột vũ trang, không y tế/tài
chính "cam kết lãi", không deepfake, không khai thác trẻ em/bạo lực/lừa đảo. Yếu tố nhạy cảm phụ:
AI & việc làm → framing trung lập, không kết luận thay khán giả, giữ câu hỏi tranh luận mở.

GATE B (content): YELLOW-fixed — B1: mọi số liệu (396 doanh nghiệp, 21,7%, 46,5% x2, 69,8%,
44→21 ngày, 36,6%, 65,4%, 42,3%, 86,6%) đều truy được về `?article=26ea180c732c` (GenK, dẫn khảo
sát Bộ Việc làm và Lao động Hàn Quốc + Cơ quan Thông tin Việc làm Hàn Quốc, và một thống kê phụ dẫn
lại từ Korea Economic Daily — có ghi rõ nguồn phụ trong on-screen chip và BRIEF.md); không con số
nào tự bịa; câu hỏi cốt lõi "ai đang đánh giá ai?" lấy nguyên ý từ bài gốc, không thêm kết luận
ngoài bài. B2: không bạo lực/thù ghét/quấy rối/doxxing/nội dung tình dục/trẻ em — nội dung phê bình
thực trạng công cụ/quy trình, không nhắm cá nhân nào. B3: kênh không mạo nhận nền tảng/hãng/cơ quan;
không testimonial giả; CTA là câu hỏi tranh luận thật bám tin, không phải engagement bait; không
link độc/lừa đảo. B4: giọng ElevenLabs "Khánh Lâm" = narrator AI chung, không giả giọng người thật
cụ thể → không cần disclosure; ảnh Hook/Article Image Card là ảnh thật lấy từ `?image=26ea180c732c`
(og:image bài GenK, cảnh phỏng vấn tuyển dụng tại Hàn Quốc, có dẫn nguồn qua Brand Anchor "Nguồn:
GenK") — KHÔNG dùng AI tái dựng cảnh thật/người thật; mọi hình ảnh còn lại trong composition là đồ
hoạ dữ liệu (chip, thẻ, thanh xếp hạng) tự dựng bằng CSS/GSAP, không phải ảnh AI minh hoạ người/sự
kiện. B5: ảnh chỉ từ `?image=`; nhạc nền sinh bằng Google Lyria (ambient, instrumental,
--negative-prompt loại vocal); SFX từ bộ SFX chuẩn của kênh (`assets/sfx/`); composition 100% tự
dựng, không reup. B6: tiêu đề = sự kiện + số liệu chính, không giật gân sai sự thật; thumbnail (frame
Hook) phản ánh đúng nội dung — không hình ảnh bịa; caption không nhồi hashtag, hashtag đều liên quan
chủ đề. B7: góc phân tích riêng — tổ chức lại số liệu bài gốc thành mạch "được/mất" (tốc độ và độ
phủ AI trong tuyển dụng → chính doanh nghiệp cũng nghi ngờ sự công bằng → ứng viên phản ứng lại bằng
AI, tạo vòng lặp "máy đấu máy"), dùng bảng xếp hạng ngang (leaderboard) để trực quan hoá 3 khâu tuyển
dụng theo tỷ lệ áp dụng AI — không chỉ đọc lại tiêu đề báo; style `2-chip-and-leaderboard` (index 1)
chưa từng dùng trong log trước đó, không trùng bố cục video gần nhất. B8: tin về thị trường lao động
Hàn Quốc, không chạm an ninh mạng/an ninh quốc gia/trật tự công cộng/dữ liệu cá nhân người Việt/quảng
cáo có điều kiện của Việt Nam — không có flag pháp lý Việt Nam.

GATE C (final): PASS — đã xem lại thumbnail + toàn bộ 7 frame render (hook/what/facts/data/context/
impact/cta) ở các mốc đã settle: đúng B6, không phần tử bịa, không lỗi hiển thị (đã phát hiện và sửa
2 lỗi trước khi chốt — xem mục "notes"). Transcript (Gemini `gemini-flash-latest`, toàn bộ audio 1
lần chạy) khớp SCRIPT.md về cấu trúc câu, toàn bộ số liệu (396, 21,7%, 46,5%, 69,8%, 44→21, 36,6%,
65,4%, 42,3%, 86,6%) và ý nghĩa — chỉ lệch dấu câu/ngắt câu tự nhiên của ASR, không câu nào "chế
thêm". Caption dùng để đăng = CAPTION.md đã qua GATE B, không sửa tay thêm claim mới.

decision: APPROVE
risk_level: YELLOW
ai_disclosure_required: false
copyright_notes: "Ảnh Hook/Article Image Card là og:image bài GenK (cảnh phỏng vấn tuyển dụng tại
Hàn Quốc, người trong ảnh quay lưng/không nhận diện được), có dẫn nguồn qua Brand Anchor 'Nguồn:
GenK'; nhạc nền sinh bằng Google Lyria (calm ambient, instrumental, --negative-prompt loại vocal);
SFX từ bộ SFX chuẩn của kênh; composition tự dựng 100% cho style 2-chip-and-leaderboard, không reup."
claims_verified:
  - "Khảo sát của Bộ Việc làm và Lao động Hàn Quốc + Cơ quan Thông tin Việc làm Hàn Quốc trên 396 doanh nghiệp (nhóm 500 doanh nghiệp doanh thu lớn nhất Hàn Quốc) — khớp bài gốc"
  - "21,7% doanh nghiệp đã chính thức dùng AI trong tuyển dụng — khớp bài gốc"
  - "46,5% dùng AI lọc hồ sơ; 69,8% dùng AI chấm năng lực & tính cách (phổ biến nhất); 46,5% dùng AI hỗ trợ đánh giá phỏng vấn — khớp bài gốc"
  - "Theo Korea Economic Daily (trích lại qua GenK): một doanh nghiệp giảm thời gian tuyển dụng từ 44 xuống 21 ngày nhờ phỏng vấn AI — khớp bài gốc, gắn rõ nguồn phụ"
  - "101/396 doanh nghiệp chưa dùng AI tuyển dụng; 36,6% trong số đó nói chưa đủ tin tưởng sự công bằng — khớp bài gốc"
  - "65,4% doanh nghiệp (khảo sát chung) muốn có hướng dẫn đạo đức & bảo vệ dữ liệu cá nhân khi dùng AI tuyển dụng — khớp bài gốc"
  - "42,3% người trẻ được khảo sát từng dùng AI chuẩn bị hồ sơ/luyện phỏng vấn; 86,6% trong số đó thấy hữu ích — khớp bài gốc"
sensitive_flags: ["AI & việc làm — đã framing trung lập, không kết luận thay khán giả, giữ câu hỏi tranh luận mở ở act CTA"]
vietnam_legal_flags: []
notes: "Bản render đầu tiên (07:04:51) có 2 lỗi phát hiện ở bước verify frame: (1) watermark số
khổng lồ ('3' ở frame Key facts, '2' ở frame Impact) render bị cắt/vỡ hình do font-size 1000px/900px
quá lớn trên div auto-size — đã sửa bằng cách bọc trong container width/height cố định + giảm
font-size xuống 560px/520px; (2) 2 frame (Key facts, Context) để trống quá nhiều nửa dưới khung
(vi phạm mục 'Cân bằng dọc' của BRAND-SYSTEM.md) — đã sửa bằng cách tăng padding/khoảng cách giữa
các card để nội dung kết thúc trong khoảng top:1400-1680px theo đúng quy định. Đã render lại lần 2
(07:10:18), re-chuẩn hoá loudness (loudnorm 2-pass, TP mục tiêu -2.0dBTP do AAC encode có thể làm
tăng true peak ~0.9-1.0dB so với input trước encode — xác nhận qua đo lại: input trước encode
TP=-1.0dBTP nhưng file AAC cuối cùng đo được TP=-0.9dBTP nếu chỉ target -1.5dBTP, nên đã hạ mục tiêu
xuống -2.0dBTP để đảm bảo file cuối luôn ≤-1.0dBTP; kết quả cuối: -14.3 LUFS / -1.9 dBTP, đạt chuẩn)
và soát lại toàn bộ 7 frame — không còn lỗi hiển thị."
