# COMPLIANCE GATE — cổng kiểm duyệt bắt buộc trước khi xuất bản

Rút gọn 2 policy engine (`youtube-google-policy-engine.md` + `meta-policy-engine.md`) thành
**checklist thao tác** cho routine tự động dựng video tin công nghệ / AI tiếng Việt → đăng
**Facebook Reel + YouTube Shorts**. Routine PHẢI chạy cổng này; RED/ORANGE/BLACK → **DỪNG, không đăng**.

Đọc bản đầy đủ khi gặp trường hợp không chắc — 2 file cùng thư mục này.

## Nguyên tắc nền

- 4 quyết định TÁCH RIÊNG: `post_allowed` · `recommendation` · `monetization` · `advertising`.
  Routine chỉ tự quyết `post_allowed` + đánh giá rủi ro monetization; không tự khẳng định "chắc chắn bật kiếm tiền".
- KHÔNG bịa: nguồn, số liệu, trích dẫn, screenshot, "case study", quy định pháp luật, chính sách nền tảng.
- KHÔNG hard-code ngưỡng chính sách cũ — với tin nhạy cảm phải nêu "cần kiểm tra nguồn chính thức".
- Mục tiêu KHÔNG phải "né nền tảng" mà là nội dung **nguyên bản, chính xác, hữu ích, minh bạch, bền vững cấp kênh**.

## GATE A — sàng lọc lúc CHỌN TIN (chạy ngay sau bước chọn tin, trước khi tốn công dựng)

Bỏ tin (chọn tin khác) nếu tin thuộc:

| Loại | Xử lý |
|---|---|
| Cáo buộc hình sự / bê bối cá nhân người thật chưa có kết luận | BỎ (ORANGE — routine không đủ năng lực verify) |
| Chính trị / bầu cử / xung đột vũ trang / sự kiện nhạy cảm | BỎ (ORANGE/HUMAN REVIEW) |
| Tin y tế: "thuốc thần", cam kết chữa khỏi, khuyên bỏ điều trị | BỎ (RED) |
| Tin tài chính: cam kết lợi nhuận, "insider", pump-and-dump, đầu tư "không rủi ro" | BỎ (RED) |
| Deepfake / phát ngôn giả của người thật là NỘI DUNG CHÍNH của tin | BỎ nếu không thể đưa tin trung lập; nếu đưa thì chỉ tường thuật, KHÔNG tái dựng |
| Nội dung khai thác trẻ em, bạo lực nghiêm trọng, lừa đảo, phishing | BỎ (BLACK) — không bao giờ dựng |
| Nguồn tin không rõ / chỉ 1 nguồn thứ cấp cho 1 claim lớn | BỎ hoặc chọn tin có nguồn tốt hơn |

Tin công nghệ / AI thông thường (ra mắt sản phẩm, benchmark, tính năng, đầu tư, chính sách công nghệ,
hướng dẫn) → **GREEN**, tiếp tục.

Tin công nghệ có yếu tố nhạy cảm phụ (vd: AI và việc làm, kiểm soát xuất khẩu chip, quyền riêng tư,
kiện tụng bản quyền AI) → **YELLOW**: được dựng nhưng phần GATE B siết chặt (framing trung lập,
"cáo buộc" ≠ "sự thật", nêu cần kiểm chứng).

## GATE B — kiểm duyệt NỘI DUNG (chạy sau khi có SCRIPT.md + CAPTION.md + ảnh, trước render)

**B1. Sự thật & nguồn**
- [ ] Mọi số liệu / mốc thời gian / tên riêng / phát ngôn trong SCRIPT + CAPTION đều truy được về
  `?article=` (bài gốc) hoặc BRIEF. KHÔNG có con số nào routine tự nghĩ ra.
- [ ] Phân biệt rõ **cáo buộc / tin đồn / dự đoán** vs **sự thật đã xác nhận**. Dùng "được cho là",
  "theo …", "chưa được xác nhận" khi cần.
- [ ] Viết lại giữ đúng nghĩa bài gốc, KHÔNG thêm diễn giải/kết luận không có trong nguồn.
- [ ] Nếu tin có claim đang tranh cãi / chính sách nền tảng / pháp lý → thêm 1 câu "cần theo dõi
  thông báo/nguồn chính thức", KHÔNG chốt như sự thật tuyệt đối.

**B2. An toàn cộng đồng**
- [ ] Không kêu gọi / đe dọa / hướng dẫn bạo lực, tự hại, hành vi nguy hiểm actionable.
- [ ] Không công kích / phi nhân hóa / kích động thù ghét theo đặc điểm được bảo vệ. Phê bình
  **hành vi / sản phẩm / chính sách**, không phải con người.
- [ ] Không quấy rối, bôi nhọ, doxxing, lộ thông tin cá nhân không cần thiết.
- [ ] Không nội dung tình dục / khiêu dâm / liên quan trẻ em.

**B3. Chính hãng & liêm chính**
- [ ] KHÔNG giả danh: nền tảng (YouTube/Meta), ngân hàng, cơ quan nhà nước, hãng công nghệ,
  người nổi tiếng, chuyên gia. Kênh "Công Nghệ Số" là kênh tin độc lập, KHÔNG mạo nhận là nguồn
  chính thức của hãng nào.
- [ ] Không testimonial giả, doanh thu giả, dashboard giả, "khách hàng của tôi kiếm X".
- [ ] Không engagement bait ("comment YES để lên xu hướng"). CTA phải là câu hỏi quan điểm thật.
- [ ] Không lừa đảo, phishing, fake giveaway, link độc hại trong caption/description.

**B4. AI / synthetic media (QUAN TRỌNG với tuyến này)**
- Giọng đọc: AI narrator chung (ElevenLabs "Khánh Lâm") = **GREEN**, KHÔNG cần disclosure
  (không giả giọng người thật cụ thể).
- Ảnh Hook / minh hoạ:
  - Ảnh thật lấy từ bài báo (`?image=`) trong Article Image Card có ghi nguồn = **GREEN** (dùng
    tin tức có dẫn nguồn). KHÔNG chỉnh sửa ảnh để bịa nội dung.
  - Ảnh do AI tạo kiểu **minh hoạ ý niệm / hoạt hoạ / cảnh hư cấu** (robot, sơ đồ, biểu tượng)
    = **GREEN**, KHÔNG cần disclosure.
  - ❌ TUYỆT ĐỐI KHÔNG dùng AI để: tái dựng **cảnh thật / người thật một cách như-ảnh-chụp**,
    tạo "hiện trường" giả, phát ngôn giả, ảnh bằng chứng giả, footage tin tức giả. Nếu 1 tin cần
    hình ảnh một sự kiện thật mà không có ảnh thật → dùng minh hoạ ý niệm rõ ràng là đồ hoạ, KHÔNG
    render ảnh giả như thật.
  - Nếu (ngoại lệ) có cảnh AI tả người/sự kiện thật ở mức dễ nhầm là thật → PHẢI thêm dòng chữ
    trên hình + trong description: **"Hình ảnh minh hoạ do AI tạo."** và khai AI content trong
    YouTube Studio. Mặc định tuyến này tránh trường hợp này.

**B5. Bản quyền & nhạc**
- [ ] Ảnh: chỉ dùng `?image=` (og:image bài báo, có dẫn nguồn) hoặc ảnh AI tự tạo / stock có quyền.
  KHÔNG lấy ảnh có watermark rồi cắt/xoá.
- [ ] Nhạc nền: Lyria tự sinh (không lời) = quyền của dự án. KHÔNG lấy nhạc từ video khác.
- [ ] SFX: bộ SFX trong repo. KHÔNG cố né Content ID (đổi tốc độ/pitch/mirror).
- [ ] Video KHÔNG phải reup / cắt ghép video của kênh khác — 100% tự dựng.

**B6. Tiêu đề & thumbnail (title/caption/description)**
- [ ] Tiêu đề = `sự kiện / số liệu chính` + góc tò mò hợp lý. KHÔNG "SỐC!!!", "100% CHẮC CHẮN",
  "YouTube xoá kênh ngày mai" khi không có bằng chứng.
- [ ] Thumbnail (frame Hook) phản ánh đúng nội dung, không gây hiểu sai, không giật gân quá mức,
  không hình ảnh bịa.
- [ ] Caption/description: giải thích nội dung + `📌 Nguồn` + hashtag liên quan. KHÔNG nhồi hashtag,
  KHÔNG hashtag không liên quan, KHÔNG từ khoá ẩn gây hiểu nhầm.

**B7. Nguyên bản (chống "inauthentic / mass-produced")** — rủi ro cao nhất với kênh tự động
- [ ] Video này có **ít nhất 1**: góc nhìn riêng / phân tích riêng / cách trình bày dữ liệu riêng /
  tổng hợp hữu ích. KHÔNG chỉ đọc lại tiêu đề báo.
- [ ] KHÔNG trùng bố cục/kịch bản với video gần nhất (đã có cơ chế `claim_style` xoay 10 style +
  quy tắc "mỗi video một cách dựng").
- [ ] Act 7 CTA đặt câu hỏi tranh luận THẬT bám tin, không phải bait chung chung.
- Ghi nhận: kênh đăng 3 video/ngày → phải giữ mỗi video có giá trị riêng, nếu 1 ngày không có tin
  đủ chất → thà bỏ 1 suất còn hơn đăng video rỗng (báo trong tóm tắt).

**B8. Pháp lý Việt Nam** — flag (ghi vào COMPLIANCE.md, KHÔNG tự dựng nếu dính) khi tin chạm:
an ninh mạng / an ninh quốc gia / trật tự công cộng / thông tin sai sự thật / bôi nhọ / dữ liệu
cá nhân / quảng cáo có điều kiện (tài chính, y tế, hàng kiểm soát) / sở hữu trí tuệ. KHÔNG tự bịa
số điều luật.

## GATE C — kiểm tra CUỐI (sau render + thumbnail, trước bước đăng)

- [ ] Xem lại thumbnail + 3-4 frame render: đúng B6, không có phần tử bịa, không lộ lỗi.
- [ ] Transcript (bước verify) khớp SCRIPT — không có câu nào routine "chế thêm" khi sinh voice.
- [ ] Caption dùng để đăng = CAPTION.md đã qua GATE B, không sửa tay thêm claim mới.

## OUTPUT — ghi `videos/<slug>/COMPLIANCE.md`

```
# COMPLIANCE — <slug>
policy_version: youtube v1.0 / meta v3.0
checked_at: <ISO>
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): GREEN | YELLOW | (nếu ORANGE/RED → đã bỏ tin, không tới đây)
GATE B (content):   GREEN | YELLOW-fixed
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN | YELLOW
ai_disclosure_required: false        # true nếu B4 ngoại lệ
copyright_notes: "ảnh og:image <nguồn>, có dẫn nguồn; nhạc Lyria tự sinh"
claims_verified: [<liệt kê số liệu/mốc + đã đối chiếu ?article=>]
sensitive_flags: []                  # vd ["AI & việc làm — framing trung lập"]
vietnam_legal_flags: []
notes: ""
```

Nếu **decision != APPROVE** hoặc **risk_level in [ORANGE, RED, BLACK]** → **DỪNG routine ở đây**,
KHÔNG đăng Facebook/YouTube, ghi lý do rõ ràng vào tóm tắt cuối (giống tinh thần "bước sản xuất
thất bại → dừng").

## Bảng quyết nhanh (tuyến tin công nghệ / AI)

| Tình huống | Kết quả |
|---|---|
| Ra mắt model/sản phẩm, benchmark, tính năng, đầu tư, hướng dẫn | GREEN → APPROVE |
| Tin công nghệ chạm việc làm / quyền riêng tư / kiện bản quyền AI / kiểm soát chip | YELLOW → framing trung lập, nêu cần theo dõi nguồn chính thức → APPROVE |
| Ảnh AI minh hoạ ý niệm (robot, sơ đồ) | GREEN, không cần disclosure |
| Ảnh AI tả người thật/sự kiện thật như ảnh chụp | RED → đổi sang minh hoạ ý niệm, hoặc bỏ tin |
| Số liệu không có trong bài gốc | RED → sửa/bỏ dòng đó, sinh lại voice |
| Tiêu đề giật gân quá bằng chứng | YELLOW → viết lại `sự kiện + tò mò hợp lý` |
| Cáo buộc hình sự / chính trị / bầu cử / y tế "thuốc thần" / tài chính "cam kết lãi" | ORANGE/RED → BỎ TIN ở GATE A |
| Deepfake/phát ngôn giả là nội dung chính | ORANGE → chỉ tường thuật trung lập, không tái dựng; nếu không được thì bỏ |
| Lừa đảo / phishing / khai thác trẻ em / bạo lực nghiêm trọng | BLACK → không bao giờ dựng |
