# COMPLIANCE — kien-cham-phat-trien-ai

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-21T14:25:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): YELLOW
GATE B (content):   YELLOW-fixed
GATE C (final):     PASS

decision: APPROVE
risk_level: YELLOW
ai_disclosure_required: false
copyright_notes: "ảnh minh hoạ ý niệm (biểu tượng OpenAI/Google/Anthropic/SpaceXAI trên toà nhà, hình người cách điệu, cán cân công lý, búa toà án) lấy qua ?image= của Apps Script (ảnh minh hoạ của bài Thanh Niên, có dẫn nguồn); là đồ hoạ ý niệm rõ ràng — KHÔNG phải ảnh chụp cảnh thật/người thật cụ thể; nhạc nền Lyria tự sinh (calm ambient, không lời, --density 0.25 --brightness 0.4 + negative-prompt bắt buộc, loop crossfade + fade-out 2.5s); SFX từ bộ SFX chuẩn của kênh (astra-openai/assets/sfx)."
claims_verified:
  - "Vụ kiện tập thể chống độc quyền tại Mỹ nhắm vào OpenAI, Google, Anthropic, SpaceXAI — đối chiếu ?article=fa94cda3a2c9 (Thanh Niên, dẫn Tom's Hardware)"
  - "Cáo buộc: 4 công ty phối hợp làm chậm tốc độ phát triển AI thay vì tự quyết định cân bằng cạnh tranh/an toàn — đối chiếu ?article=fa94cda3a2c9"
  - "Khởi xướng bởi 4 người dùng trả phí ChatGPT, Claude, Grok, Gemini — đối chiếu ?article=fa94cda3a2c9"
  - "Nguyên đơn cho rằng phối hợp bắt đầu từ tháng 7/2026, sau tuyên bố chung của các phòng thí nghiệm AI hàng đầu — đối chiếu ?article=fa94cda3a2c9"
  - "Đề xuất hợp tác của Dario Amodei (nhà sáng lập Anthropic) bị nguyên đơn gọi là 'lối tắt' thay trách nhiệm từng công ty bằng kiềm chế tập thể — đối chiếu ?article=fa94cda3a2c9"
  - "Luật sư Nick Rowley (đại diện nguyên đơn) phản đối tiêu chuẩn an toàn AI quyết định qua thoả thuận riêng giữa các công ty — đối chiếu ?article=fa94cda3a2c9"
  - "Sam Altman (CEO OpenAI) nói ủng hộ khung liên bang thống nhất, ngành không cần chờ luật mới — đối chiếu ?article=fa94cda3a2c9"
  - "Đây là lập luận từ phía nguyên đơn, CHƯA phải kết luận của toà án — đối chiếu ?article=fa94cda3a2c9 (nêu rõ trong bài gốc)"
sensitive_flags: ["Kiện tụng công nghệ/AI (tranh chấp chống độc quyền giữa các công ty) — framing trung lập bắt buộc: dùng 'cáo buộc'/'nguyên đơn cho rằng' xuyên suốt SCRIPT + CAPTION, chốt rõ 'toà án chưa đưa ra kết luận' ở act Impact và act Context, không khẳng định 4 công ty có tội."]
vietnam_legal_flags: []
notes: "Sự việc xảy ra tại Mỹ (vụ kiện dân sự chống độc quyền giữa các công ty công nghệ Mỹ), không chạm luật an ninh mạng/an ninh quốc gia/dữ liệu cá nhân Việt Nam — không có flag pháp lý VN. Ảnh minh hoạ là đồ hoạ ý niệm rõ ràng (biểu tượng công ty, hình người cách điệu không thể nhận diện, cán cân công lý) — không phải AI tái dựng cảnh thật/người thật như ảnh chụp, đúng B4 GREEN. Transcript verify: ElevenLabs STT (scribe_v1, chạy trên từng file line1-7.mp3 thực tế đã dùng render) khớp SCRIPT.md cho cả 7 dòng, chỉ lệch nhỏ do ASR chuẩn hoá số/dấu ('SpaceX AI' thay vì 'SpaceXAI', '2026' thay vì đọc chữ, 'kìm chế' gần âm 'kiềm chế') — không có câu nào đọc sai cấu trúc/nghĩa hoặc 'chế thêm'; đối chiếu bổ sung bằng Gemini flash-latest multimodal (transcribe 5/7 dòng đầu trước khi bị giới hạn output) cho kết quả khớp y hệt. Nguyên bản (GATE B7): style 3-ticker-tape (index 2, lần gần nhất dùng 16/9 — cách 5 ngày, không trùng video liền kề) triển khai ẩn dụ 'release feed' riêng cho tin kiện tụng (dải LIVE ticker tên các bên, khung terminal 'ba mốc chính' kiểu log file, data moment xoay quanh con số 4 xuyên suốt vụ kiện, sparkline đối chiếu 3 phát biểu đối lập); góc phân tích riêng là trục 'con số 4' + đối chiếu trực tiếp lập luận Amodei/nguyên đơn/Altman thay vì chỉ tường thuật tuần tự theo bài gốc. Cân bằng dọc: đã verify bằng frame thật ở CUỐI mỗi act (t=3.8/12/26/34/45/55/63s) — tất cả act giữa đều có phần tử cuối cùng (card/box/chip/footer) kết thúc trong khoảng top 1400-1680px, không còn khoảng trống đen lớn (đã sửa 1 lỗi phát hiện ở 03-facts trong lúc soát Studio trước render — terminal box ban đầu để trống ~500px dưới nội dung, đã thêm dòng chú thích nguồn + tăng spacing để lấp đúng vùng an toàn)."
```

## Ghi chú kiểm tra chi tiết

- **GATE A**: tin thuộc nhóm kiện tụng công nghệ/AI (vụ kiện chống độc quyền công ty-với-công ty, không phải cáo buộc hình sự/bê bối cá nhân, không chính trị/bầu cử/xung đột vũ trang, không y tế "thuốc thần", không tài chính "cam kết lãi", không deepfake, không khai thác trẻ em/bạo lực/lừa đảo) → YELLOW theo bảng quyết nhanh COMPLIANCE-GATE.md (tương đương mục "kiện tụng bản quyền AI"). Nguồn Thanh Niên dẫn lại Tom's Hardware, tường thuật một vụ kiện đã nộp thật (public record), không phải tin đồn 1 nguồn thứ cấp không kiểm chứng được.
- **GATE B**: rà đủ B1-B8 trước render (ghi trong BRIEF.md). B1: toàn bộ số liệu (4 công ty, 4 dịch vụ, 4 người dùng, tháng 7/2026) và trích dẫn/phát biểu (Amodei, Rowley, Altman) đều truy được về `?article=fa94cda3a2c9`; SCRIPT/CAPTION dùng "cáo buộc"/"nguyên đơn cho rằng" nhất quán, không chốt như sự thật tuyệt đối. B2: không công kích cá nhân, phê bình hành vi/chính sách công ty. B3: không giả danh OpenAI/Google/Anthropic/SpaceXAI/toà án, không testimonial giả, CTA là câu hỏi quan điểm thật bám tin. B4: ảnh minh hoạ ý niệm (GREEN, không cần disclosure). B5: ảnh từ `?image=` có dẫn nguồn, nhạc Lyria tự sinh, SFX repo, video 100% tự dựng. B6: tiêu đề "Bốn hãng AI hàng đầu bị kiện tập thể" bám sự kiện, không giật gân sai sự thật; thumbnail phản ánh đúng nội dung. B7: góc phân tích riêng trục "con số 4" + đối chiếu Amodei/nguyên đơn/Altman, style ticker-tape không trùng video liền kề. B8: không có flag pháp lý VN (sự việc ở Mỹ).
- **GATE C**: xem lại thumbnail + 7 frame thật ở các mốc t=3.8/12/26/34/45/55/63s (đủ cả 7 act) — không phần tử bịa, đúng brand (#4C8DFF/#0B0E14/#FF8A5B, Montserrat, không emoji, 2 tag tương phản ở Hook, CTA đúng khuôn astra-openai/07-cta.html). Cân bằng dọc: đã sửa 03-facts (terminal box ban đầu để trống ~500px dưới 3 dòng fact, đã thêm f-foot + tăng spacing, phần tử cuối giờ kết thúc ~top:1600px), các act khác đều đạt dải 1400-1680px ngay từ đầu (02-what chips+footer ~1650px, 04-data stat chips ~1520px, 05-context footer ~1620px, 06-impact note ~1620px, 07-cta chữ ký logo ~1650px). Transcript (ElevenLabs STT scribe_v1 trên từng file line thật + đối chiếu Gemini flash-latest multimodal) khớp SCRIPT.md, không câu nào "chế thêm" khi sinh voice. Caption dùng để đăng = CAPTION.md đã qua GATE B, không sửa tay thêm claim mới.

**decision: APPROVE — risk_level: YELLOW → đủ điều kiện đăng Facebook Reel + YouTube Shorts.**
