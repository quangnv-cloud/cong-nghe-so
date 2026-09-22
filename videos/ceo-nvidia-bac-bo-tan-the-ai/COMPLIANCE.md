# COMPLIANCE — ceo-nvidia-bac-bo-tan-the-ai
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-22T14:20:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): YELLOW — tin công nghệ chạm yếu tố nhạy cảm phụ "AI & an toàn / rủi ro hiện
  sinh" (CEO Nvidia Jensen Huang bác bỏ cảnh báo trí tuệ nhân tạo có thể gây tận thế, đối lập cảnh
  báo của cựu nghiên cứu viên Anthropic Jacob Coxon). Không phải cáo buộc hình sự, không chính trị/
  bầu cử/xung đột vũ trang là nội dung chính (chi tiết Huang ủng hộ chính sách AI của chính quyền Mỹ
  hiện tại chỉ nêu như bối cảnh lập trường, không bình luận đảng phái), không y tế "thuốc thần",
  không tài chính "cam kết lãi", không deepfake, không BLACK.

GATE B (content): YELLOW-fixed — framing trung lập, trình bày cả 2 phía tranh luận (Huang bác bỏ vs
  cảnh báo Coxon), không kết luận thay chuyên gia bên nào đúng. B1: mọi số liệu/tên/trích dẫn truy
  được về `?article=869761528678` (Znews, dẫn CBS News) — không con số nào bịa. B2: phê bình
  lập trường/phát ngôn công khai của nhân vật công chúng (CEO Nvidia), không công kích cá nhân,
  không doxxing. B3: kênh không mạo nhận nguồn chính thức, không testimonial giả, CTA là câu hỏi
  quan điểm thật, không engagement bait. B4: giọng AI narrator chung (ElevenLabs) không cần
  disclosure; ảnh Hook/Article Image Card là ảnh thật (Bloomberg qua Znews) có dẫn nguồn, KHÔNG dùng
  AI tái dựng cảnh/người thật — chỉ đồ hoạ ý niệm (vòng radial, icon CSS) cho phần data-viz. B5: ảnh
  từ `?image=`, nhạc nền Lyria tự sinh (Google Lyria RealTime, không lời, xác nhận qua nghe/soát),
  SFX từ repo, video 100% tự dựng. B6: tiêu đề "0%" + tên chủ thể, không giật gân sai sự thật;
  thumbnail phản ánh đúng nội dung. B7: góc nhìn riêng — chuyển hoá tuyên bố "0%" thành ẩn dụ vòng
  radial rỗng (style 6-ring-progress), đối chiếu với vị thế thị trường 5,3 nghìn tỷ đô la Mỹ của
  Nvidia và lập trường chính sách của Huang — không chỉ đọc lại tiêu đề báo; khác chủ đề & bố cục với
  2 video routine cùng ngày (chip-nvidia-vuot-cam-van-trung-quoc: kiểm soát xuất khẩu chip, style
  4-split-comparison; ai-code-tq-tu-dong-tai-cloud: quyền riêng tư dữ liệu, style 5-map-and-geo).
  B8: không chạm an ninh mạng/thông tin sai/dữ liệu cá nhân/quảng cáo có điều kiện của Việt Nam.

GATE C (final): PASS — đã soát thumbnail + 7 frame render thật (cuối animation-reveal mỗi act giữa)
  bằng Read, không phần tử bịa, cân bằng dọc đạt (phần tử cuối mỗi act giữa kết thúc trong khoảng
  top 1400-1680px, không trống đen nửa dưới). Transcript (Gemini `gemini-flash-lite-latest`, đối
  chiếu chéo với timestamp từ-cho-từ ElevenLabs STT `scribe_v1` dùng để dựng caption karaoke) khớp
  hoàn toàn nội dung SCRIPT.md, không câu nào "chế thêm". Caption dùng để đăng = CAPTION.md đã qua
  GATE B, không sửa tay thêm claim mới.

decision: APPROVE
risk_level: YELLOW
ai_disclosure_required: false
copyright_notes: "ảnh og:image bài Znews (nguồn ảnh gốc: Bloomberg), dùng trong Article Image Card
  có ghi rõ 'Nguồn: Znews'; nhạc nền sinh bằng Google Lyria RealTime (lyria-recipe.py, prompt
  ambient/instrumental, negative-prompt loại vocal) — không lấy nhạc ngoài; SFX từ bộ SFX repo."
claims_verified:
  - "Jensen Huang, CEO Nvidia, nói với CBS News: 'Năm 2030 sẽ không phải ngày tận thế. Khả năng đó
    xảy ra là 0%' — khớp ?article=869761528678"
  - "Jacob Coxon, cựu nghiên cứu viên Anthropic, cảnh báo trí tuệ nhân tạo có thể gây thảm hoạ
    trước cuối thập kỷ — khớp bài gốc"
  - "Huang: Mỹ chưa cần luật hoàn toàn mới riêng cho AI, có thể dùng quy định hiện hành về trách
    nhiệm sản phẩm/an ninh mạng — khớp bài gốc"
  - "Nvidia đạt giá trị thị trường khoảng 5.300 tỷ đô la Mỹ — khớp bài gốc"
  - "Huang ủng hộ cách tiếp cận ít hạn chế hơn của chính quyền Mỹ hiện tại với AI — khớp bài gốc"
  - "Giới công nghệ hiện chưa có đồng thuận về mức độ rủi ro AI tiên tiến — khớp bài gốc (đoạn kết
    luận của phóng viên Znews, dùng làm act 6 Impact, là sự thật đã xảy ra không suy đoán tương lai)"
sensitive_flags: ["AI & an toàn / rủi ro hiện sinh — đã framing trung lập, trình bày cả 2 phía,
  không kết luận thay chuyên gia"]
vietnam_legal_flags: []
notes: "BGM: Google Lyria RealTime thành công ngay lần thử đầu (model models/lyria-realtime-exp qua
  lyria-recipe.py) — KHÔNG cần fallback ElevenLabs Music. Audio verify: loudnorm 2-pass áp dụng để
  đưa Integrated Loudness từ -15.9 LUFS về -14.1 LUFS và True Peak về -1.4 dBTP (đạt chuẩn -14 LUFS
  ±1 LU / TP ≤ -1.0 dBTP) trước khi giao file."
