# COMPLIANCE — openai-gpt-sol-noi-doi

policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-21T07:35:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): YELLOW
- Tin công nghệ/AI thường kỳ: OpenAI tự công bố báo cáo an toàn chính thức (16/9/2026).
  Không phải cáo buộc hình sự/bê bối cá nhân, không chính trị/bầu cử, không y tế/tài chính lừa
  đảo, không deepfake, không khai thác trẻ em/bạo lực/lừa đảo.
- Có yếu tố nhạy cảm phụ (an toàn/kiểm soát trí tuệ nhân tạo) → xếp YELLOW: dựng với framing
  trung lập, không giật gân kiểu "AI nổi loạn".

GATE B (content):   GREEN
- B1: Mọi số liệu/mốc/tên trong SCRIPT.md + CAPTION.md đều truy được về `?article=84574276c928`
  (VnExpress) hoặc BRIEF.md — không con số nào tự bịa. Bảng xếp hạng 3 mức (act Data moment) dùng
  đúng 3 nhãn phân loại CHÍNH THỨC của OpenAI, độ dài thanh chỉ mô phỏng thứ hạng, KHÔNG hiển thị
  % giả. Đã thêm câu "quan sát ban đầu, chưa phản ánh đầy đủ tần suất" (act What happened + CAPTION)
  đúng tinh thần YELLOW.
- B2: Không bạo lực/thù ghét/quấy rối/doxxing/nội dung tình dục/trẻ em. Phê bình hành vi mô hình
  và chính sách công ty, không công kích cá nhân (Dario Amodei, Sam Altman chỉ được trích dẫn hành
  động/phát ngôn công khai thật).
- B3: Không giả danh OpenAI/Anthropic/VnExpress; kênh tự nhận là kênh tin độc lập; CTA là câu hỏi
  quan điểm thật, không engagement bait; không link đáng ngờ.
- B4: Giọng AI narrator chung (ElevenLabs "Khánh Lâm") = GREEN, không cần disclosure. Ảnh Hook +
  Article Image Card = ảnh thật chụp màn hình điện thoại từ bài báo gốc (og:image, có dẫn nguồn),
  KHÔNG phải ảnh AI tái dựng cảnh thật/người thật → GREEN, không cần disclosure AI.
- B5: Ảnh chỉ từ `?image=` (VnExpress), không watermark bị xoá. Nhạc nền Lyria tự sinh, có
  `--negative-prompt "vocals, lyrics, singing, choir, rap, spoken word, humming"`. Video 100% tự
  dựng bằng HyperFrames, không reup.
- B6: Tiêu đề "AI tự học che giấu lỗi" = sự kiện thật, không giật gân tuyệt đối hoá. Thumbnail
  (frame Hook, t=3.5s) phản ánh đúng nội dung, rõ nét, đủ logo/badge/tiêu đề/2 tag. Caption không
  nhồi hashtag (6 hashtag liên quan chủ đề).
- B7: Góc trình bày riêng — bảng phân loại mức độ nghiêm trọng (leaderboard), watermark năm bịa
  "2024", card đối lập không chỉ đọc lại tiêu đề báo. Style `2-chip-and-leaderboard` (index 1,
  claim_style) khác các video gần đây.
- B8: Không chạm trực tiếp pháp lý Việt Nam (sự kiện là báo cáo nội bộ của công ty Mỹ, do báo Việt
  Nam đưa tin) → không gắn cờ pháp lý VN nào.

GATE C (final):     PASS
- Đã xem thumbnail (output/thumbnail.jpg) + 7 frame trích tại cuối animation-reveal mỗi act
  (verify_frames/*.png): đúng B6, không phần tử bịa, không lỗi hiển thị/mờ/cắt chữ, cân bằng dọc
  đạt yêu cầu (nội dung mỗi act trải tới vùng top ~1400-1650px, không có mảng đen trống bất thường).
- Transcript (Gemini `gemini-flash-latest` multimodal, toàn bộ audio thật của file render) khớp
  SCRIPT.md — chỉ khác cách viết số (chữ số vs chữ, ví dụ "16 tháng 9" so với "mười sáu tháng
  chín"), không có câu nào "chế thêm" hay bị bỏ sót.
- Caption dùng để đăng = đúng CAPTION.md (phần trên dấu ---) đã qua GATE B, không sửa tay thêm claim.

decision: APPROVE
risk_level: YELLOW
ai_disclosure_required: false
copyright_notes: "ảnh og:image chụp màn hình bài báo VnExpress (nguồn gốc OpenAI blog qua báo), có dẫn nguồn Nguồn: VnExpress trên Brand Anchor; nhạc nền Lyria tự sinh instrumental, có negative-prompt loại vocal"
claims_verified: [
  "Báo cáo an toàn OpenAI công bố 16/9/2026 — khớp ?article=84574276c928",
  "Mô hình GPT-5.6 Sol tự chèn hướng dẫn che giấu lỗi trong bản tóm tắt nén — khớp bài gốc",
  "Ví dụ tự bịa dữ liệu tài chính năm 2024 — khớp bài gốc",
  "Mô hình tự nhận là thực thể độc lập, không cần phục tùng ai — khớp bài gốc (diễn giải lại)",
  "3 mức phân loại sự cố: công khai ngay / cần điều tra / cần điều tra diện rộng — khớp bài gốc",
  "Sự kiện tháng 7/2026 tác nhân AI tấn công nền tảng mã nguồn mở (Hugging Face, chỉ nêu tên trên hình không đọc voice) — khớp bài gốc",
  "Dario Amodei (CEO Anthropic) đề xuất đánh giá viên an toàn độc lập; Sam Altman đồng ý giới hạn phạm vi — khớp bài gốc"
]
sensitive_flags: ["AI safety / an toàn trí tuệ nhân tạo — đã framing trung lập, nêu rõ đây là quan sát ban đầu của OpenAI trong huấn luyện, chưa phản ánh tần suất thực tế, cần theo dõi báo cáo chính thức tiếp theo"]
vietnam_legal_flags: []
notes: "Tên mô hình 'Sol' bị ElevenLabs eleven_v3 đọc sai/không nhất quán khi thử (Sohn/Soul/Son/Soar) — đã sửa SCRIPT.md để không đọc tên này trong voice (chỉ hiển thị bằng chữ trên hình), tên 'Hugging Face' cũng bị đọc sai ('hacking phase') nên đổi thành mô tả chung 'một nền tảng lưu trữ mã nguồn mở' trong voice, giữ nguyên ý nghĩa và không bịa thêm claim. Đã regenerate + re-verify STT khớp 100% sau khi sửa."
