# COMPLIANCE — gpt6-mien-phi-giao-dien-tuong-tac

policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-10-09T01:30:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): GREEN — tin ra mắt tính năng sản phẩm thông thường (OpenAI triển khai GPT-6 +
  Intelligent UI cho ChatGPT), nguồn là thông báo chính thức của OpenAI được Thanh Niên đưa tin lại.
  Không cáo buộc hình sự / chính trị / y tế / tài chính "cam kết lãi" / deepfake / bóc lột trẻ em /
  bạo lực / lừa đảo.

GATE B (content):   GREEN — B1 mọi số liệu/tên/mốc thời gian (7/10, 8/10, Sol, Luna, Plus/Pro/
  Business/Enterprise, ví dụ bữa tối, công cụ cá nhân hóa, Rắn săn mồi) đối chiếu đúng
  `?article=15b7361716ee`, không con số tự bịa. B2 không bạo lực/thù ghét/quấy rối/nội dung tình
  dục. B3 không giả danh OpenAI/ChatGPT/cơ quan nào — kênh là nguồn tin độc lập dẫn lại; không
  testimonial giả, không engagement bait (CTA là câu hỏi quan điểm thật). B4 giọng Vbee TTS chung =
  GREEN không cần disclosure; ảnh hero là ảnh thật từ bài báo (điện thoại hiển thị màn hình khởi
  động OpenAI), có dẫn nguồn; mọi minh hoạ khác trong composition là CSS/SVG hình học (icon lưới,
  biểu tượng đồng hồ cát, máy tính, rắn pixel) — không AI tái dựng cảnh thật/người thật. B5 ảnh chỉ
  từ `?image=`; nhạc nền tự sinh qua Google Lyria (density 0.25, brightness 0.4, negative-prompt
  loại vocal); SFX từ bộ repo chung; video 100% tự dựng. B6 tiêu đề "OpenAI Đưa GPT-6 Đến Người
  Dùng ChatGPT Miễn Phí" là sự kiện + góc tò mò hợp lý, không giật gân sai sự thật; thumbnail đúng
  nội dung Hook. B7 góc nhìn riêng: khung "dân chủ hóa trí tuệ nhân tạo vs làm phức tạp chatbot"
  không có trong bài gốc (bài gốc thuần mô tả tính năng); style `8-icon-grid` (index 7) lần đầu
  dùng cho kênh, không trùng bố cục video gần nhất. B8 không chạm an ninh mạng/an ninh quốc gia/
  thông tin sai/dữ liệu cá nhân/quảng cáo có điều kiện.

GATE C (final):     PASS — xem lại thumbnail (logo/tên kênh/badge nguồn/tiêu đề/2 tag đều hiện rõ,
  không mờ/cắt) + 7 frame render (Hook, What happened, Key facts, Data moment, Context, Impact,
  CTA) đúng brand (#4C8DFF/#0B0E14/#FF8A5B, Montserrat, không emoji, WCAG AA đạt 63/63). Transcript
  (Gemini gemini-flash-lite-latest trên audio mix đầy đủ) khớp 100% ý nghĩa SCRIPT.md, không câu
  nào "chế thêm" khi sinh voice — chỉ lệch nhận dạng ASR vô hại ("Sol"→"son", dính liền "ChatGPT"→
  "chat GPT", "nhờ"→"nhớ"), không phải lỗi phát âm/viết tắt. Caption đăng = CAPTION.md đã qua GATE B,
  không sửa tay thêm claim mới.

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "ảnh hero từ bài báo Thanh Niên (?image=15b7361716ee), có dẫn nguồn trên màn hình
  (Brand Anchor góc trên-trái); nhạc nền Lyria tự sinh (density 0.25/brightness 0.4, no-vocal); SFX
  từ assets/sfx/ repo chung; logo/font Montserrat self-host sẵn có."
claims_verified:
  - "GPT-6 + tính năng Intelligent UI (Giao diện thông minh) triển khai cho ChatGPT — đối chiếu ?article=15b7361716ee"
  - "Phản hồi có thể gồm đồ họa, nút bấm, biểu mẫu, sơ đồ tùy câu hỏi — đối chiếu bài gốc"
  - "Ví dụ lên kế hoạch bữa tối: bảng tính nguyên liệu, danh sách kiểm tra, biểu mẫu hỏi thêm — đối chiếu bài gốc"
  - "Trả lời khi đang xử lý, soạn thảo qua nhiều tin nhắn liên tiếp — đối chiếu bài gốc"
  - "Đã triển khai cho toàn bộ ChatGPT Plus/Pro/Business/Enterprise toàn cầu — đối chiếu bài gốc"
  - "Người trả phí dùng bản Sol từ 7/10; người miễn phí/giá rẻ dùng bản Luna từ 8/10 (1 ngày sau) — đối chiếu bài gốc"
  - "Người dùng tự tạo công cụ cá nhân hóa (hỗ trợ đầu tư, chia hóa đơn), tái hiện trò chơi Rắn săn mồi — đối chiếu bài gốc"
sensitive_flags: []
vietnam_legal_flags: []
notes: "Style claim_style trả index 7 (8-icon-grid) — lần đầu kênh dùng style này. BGM Lyria thành
  công lần gọi đầu, không cần fallback ElevenLabs Music. Vbee TTS cả 7 dòng thành công lần gọi đầu
  qua cơ chế POST tạo job + poll GET /api/v1/tts/{request_id}. Loudness ban đầu đo -18.0 LUFS (ngoài
  dung sai ±1 LU) → chạy loudnorm 2-pass (target -14 LUFS / TP -1.5 dBTP), đạt đúng -14.0 LUFS /
  -1.5 dBTP sau xử lý. Phát hiện và sửa lỗi cân bằng dọc nghiêm trọng ở vòng render đầu (act 3/5/6
  kết thúc nội dung quá sớm ~800-1000px, để trống đen lớn phía dưới trước khi đến caption ở 1460px)
  — đã mở rộng/dịch chuyển card xuống, rút ngắn khoảng cách tới caption, và áp lại đúng kích thước
  mẫu Hook/CTA chuẩn đã duyệt trước khi render lại; verify lại bằng frame thật sau khi sửa."
