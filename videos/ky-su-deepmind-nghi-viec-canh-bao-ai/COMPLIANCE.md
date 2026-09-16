# COMPLIANCE — ky-su-deepmind-nghi-viec-canh-bao-ai

policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-16T01:30:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): YELLOW — tin nội bộ ngành AI (kỹ sư an toàn AGI nghỉ việc + phát ngôn công khai
trên X), không cáo buộc hình sự/chính trị/bầu cử/xung đột vũ trang, không y tế/tài chính "cam kết
lãi", không deepfake, không khai thác trẻ em/bạo lực/lừa đảo. Yếu tố nhạy cảm phụ: AI & an toàn/rủi
ro hiện sinh → framing trung lập, phân biệt ước tính cá nhân với sự thật.

GATE B (content): YELLOW-fixed — B1 mọi số liệu/tên/mốc thời gian truy được về `?article=332e47b30dd0`
(GenK); ước tính rủi ro của Evan Hubinger và niềm tin cá nhân của Bilal Chughtai gắn rõ "ước tính",
"tin rằng" — không chốt như sự thật tuyệt đối. B2-B5 đạt (không công kích cá nhân, không giả danh,
ảnh chỉ từ `?image=` có dẫn nguồn, nhạc Lyria tự sinh không lời). B6 tiêu đề = sự kiện + tò mò hợp
lý, không giật gân. B7: góc phân tích riêng — đặt 3 trường hợp nghỉ việc (Coxon/Anthropic,
Engels+Chughtai/DeepMind) trên cùng khung thời gian thành "làn sóng", đối chiếu với thực tế CEO 2
hãng kêu gọi "đi chậm lại" nhưng ngành chưa chậm lại; không chỉ đọc lại tiêu đề báo; style xoay vòng
`1-card-and-bar` khác các video gần nhất. B8: không chạm pháp lý VN.

GATE C (final):     PASS — thumbnail + các frame render (hook/what/facts/data/context/impact/cta)
đúng B6, không phần tử bịa, không lỗi hiển thị. Transcript (2 lần chạy Gemini `gemini-flash-lite-latest`
trên toàn bộ audio) khớp SCRIPT.md về cấu trúc, số liệu (3 tuần, tháng 7, hơn 10%, 10 năm), tên tổ
chức và ý nghĩa câu — không câu nào bị "chế thêm". Caption dùng để đăng = CAPTION.md đã qua GATE B,
không sửa tay thêm claim mới.

decision: APPROVE
risk_level: YELLOW
ai_disclosure_required: false
copyright_notes: "Ảnh Hook/Article Image Card là og:image của bài GenK (biển hiệu trụ sở Google,
California), có dẫn nguồn qua Brand Anchor 'Nguồn: GenK'; nhạc nền sinh bằng Google Lyria (calm
ambient, instrumental, --negative-prompt loại vocal); SFX từ bộ SFX chuẩn của kênh; composition tự
dựng 100%, không reup."
claims_verified:
  - "2 kỹ sư (Josh Engels, Bilal Chughtai) từng làm an toàn AGI tại Google DeepMind, đã nghỉ việc — khớp bài gốc"
  - "Engels nghỉ ~3 tuần trước (tính từ 15/9/2026), gia nhập METR, từng từ chối Anthropic & OpenAI — khớp bài gốc"
  - "Chughtai nghỉ tháng 7/2026, tin AI có thể gây họa cho tất cả chúng ta — khớp bài gốc, gắn rõ là niềm tin cá nhân"
  - "Evan Hubinger (lãnh đạo khoa học căn chỉnh Anthropic) ước tính xác suất AI gây thảm họa nhân loại trong 10 năm tới là >10% — khớp bài gốc, gắn rõ là ước tính"
  - "Jacob Coxon (cựu nghiên cứu viên Anthropic) cảnh báo đầu tháng 9/2026 — khớp bài gốc"
  - "Dario Amodei (CEO Anthropic) kêu gọi ngành AI đi chậm lại — khớp bài gốc"
  - "Demis Hassabis (CEO Google DeepMind) đồng tình, thừa nhận AI vượt tốc hiểu biết rủi ro — khớp bài gốc"
sensitive_flags: ["AI an toàn / rủi ro hiện sinh — đã framing trung lập, phân biệt ước tính/niềm tin cá nhân với sự thật đã xảy ra"]
vietnam_legal_flags: []
notes: "Phiên âm ngược (Gemini) không ổn định với 2 tên riêng nước ngoài khó đọc (Bilal Chughtai,
Demis Hassabis) — chạy lại 2 lần trên cùng audio ra 2 biến thể phiên âm khác nhau cho cùng 1 file,
cho thấy đây là hạn chế của bộ nhận diện giọng nói (ASR) với tên nước ngoài hiếm gặp, không phải
bằng chứng giọng đọc sai ngôn ngữ hay sai số liệu — mọi số liệu/ngày/tên tổ chức đều khớp bài gốc ở
cả 2 lần chạy. Đã thử sinh lại giọng đọc cho dòng có 'Demis Hassabis' và dòng CTA một lần, xác nhận
qua 1 lần phiên âm sạch trước khi chốt, chấp nhận theo mức 'nhầm âm gần giống' của quy tắc voiceover."
