# BRIEF — Ngành CNTT Ấn Độ 315 tỷ USD chao đảo vì AI, kỹ sư giá rẻ đứng trước nguy cơ

Video routine sáng (7h30) cho kênh "Công Nghệ Số". Tuyến tin công nghệ Việt Nam (theo
`videos/PRODUCTION-WORKFLOW.md`).

## Nguồn
- GenK, đăng lại từ doisongphapluat.nguoiduatin.vn — "Ngành CNTT Ấn Độ trị giá 315 tỷ USD chao đảo
  vì AI, thời của hàng triệu kỹ sư giá rẻ có thể sắp kết thúc", 13/9/2026.
  https://doisongphapluat.nguoiduatin.vn/315-ty-usd-nganh-cntt-an-do-chao-dao-vi-ai-thoi-cua-hang-trieu-ky-su-gia-re-co-the-sap-ket-thuc-a661360.html
- Lấy nội dung qua `?article=275a5169efcb` (Apps Script CNS News Fetch) — KHÔNG WebFetch trực tiếp.
- Ảnh: og:image bài báo → `assets/img/article-hero.jpg` (qua `?image=275a5169efcb`).

## Style dựng
`claim_style` → index 4, **"5-map-and-geo"**. Diễn giải: bản đồ Ấn Độ + các "vùng" doanh nghiệp
CNTT lớn (Tata Consultancy Services, Wipro, HCLTech, Cognizant) và nhóm doanh nghiệp tầm trung
(Persistent Systems, Coforge) tăng trưởng nhanh hơn — dùng ẩn dụ địa lý (bản đồ, ghim, vùng
highlight) cho các hãng theo GATE A/CONSTRUCTION-STYLES.md, KHÔNG có yếu tố địa chính trị thật (chỉ
mượn ẩn dụ bản đồ vì tin gốc là về Ấn Độ).

## GATE A
Tin công nghệ thông thường có yếu tố nhạy cảm phụ: **AI và việc làm** → **YELLOW**. Framing trung
lập, không kết luận "kỹ sư sẽ mất việc hàng loạt" như sự thật tuyệt đối — chỉ trình bày đúng những
gì bài báo nói (mô hình kim tự tháp tuyển dụng đang mất dần, nhu cầu kỹ sư cấp thấp giảm).

## Số liệu / dữ kiện xác nhận (KHÔNG bịa thêm ngoài danh sách này)
- Ngành CNTT Ấn Độ trị giá khoảng **315 tỷ USD/năm**.
- Các hãng lớn (Tata Consultancy Services, Wipro, HCLTech, Cognizant) đang chuyển từ tính phí theo
  giờ nhân sự sang tính phí theo kết quả đạt được.
- **Jimit Arora** (CEO hãng tư vấn Everest Group): thị trường nghiêng về phía khách hàng, nhà cung
  cấp phải cạnh tranh quyết liệt để giữ hợp đồng.
- **K Krithivasan** (CEO Tata Consultancy Services — TCS): khoảng **80% hợp đồng** ở mảng tài
  chính, nhân sự, dịch vụ doanh nghiệp hiện gắn với chỉ số hiệu quả thực tế — con số này **tăng gấp
  đôi** kể từ khi AI bùng nổ.
- Cognizant + Daimler Truck: cơ chế chia sẻ khoản chi phí tiết kiệm được nhờ AI.
- HCLTech quản lý cloud cho E.ON: khoản thanh toán từ năm thứ hai phụ thuộc hoàn toàn vào mức cải
  thiện hiệu suất kinh doanh.
- **Sandeep Kalra** (CEO Persistent Systems): nhiều đối tác yêu cầu giảm **25–30% chi phí** cho
  cùng khối lượng công việc, ép tiến độ nhanh hơn.
- AI làm suy yếu lợi thế quy mô của tập đoàn lớn — công ty tầm trung (Persistent Systems, Coforge)
  triển khai đội ngũ cấp cao nhanh hơn, giá linh hoạt hơn, cạnh tranh được với đối thủ lớn hơn.
- Quý II: doanh thu **Persistent Systems tăng 16%**, **Coforge tăng khoảng 1/3 (~33%)**; trong khi
  **TCS, Infosys, Wipro, HCLTech chỉ tăng 1–3%**.
- **V. Balakrishnan** (cựu CFO Infosys): mô hình kim tự tháp tuyển kỹ sư trẻ số lượng lớn đang mất
  dần — AI đảm nhiệm việc lập trình cơ bản, nhu cầu kỹ sư cấp thấp giảm.
- Câu hỏi khép bài gốc: ngành CNTT Ấn Độ đang bán sức lao động chân tay hay bán giá trị thực sự?

## Cấu trúc 7 act
Hook → What happened → Key facts → Data moment → Context → Impact (sự thật quý II đã xảy ra, không
suy đoán) → CTA (câu hỏi tranh luận: hiệu quả hoá công việc là bước tiến hay mối lo cho kỹ sư trẻ).

## Voice
ElevenLabs "Khánh Lâm - tin tức, thời sự" (`voice_id RCmOaM1iiIH5xX3QXjIF`), `model_id eleven_v3`,
speed ~1.09.
