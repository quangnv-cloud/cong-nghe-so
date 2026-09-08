# BRIEF — Công nghệ độc quyền DLSS 5 của Nvidia chạy được trên card AMD

Video định kỳ của kênh "Công Nghệ Số". Style xoay vòng: `5-map-and-geo` (index 4, claim lúc
2026-09-08T00:33:57Z). Tin không có yếu tố địa lý/địa chính trị rõ — diễn giải lại ẩn dụ "bản đồ"
thành "bản đồ lãnh thổ phần cứng": 2 vùng Nvidia / AMD, "ranh giới" công nghệ độc quyền bị vượt qua,
"điểm đến" hiệu năng mục tiêu (RTX 5070 Ti) còn rất xa.

## Nguồn
- GenK (đăng lại/biên tập từ thanhnienviet.vn) — "Công nghệ độc quyền mới nhất của Nvidia đã chạy
  được trên card AMD, nhưng có một đánh đổi lớn", ngày 6/9/2026.
  https://thanhnienviet.vn/cong-nghe-doc-quyen-moi-nhat-cua-nvidia-da-chay-duoc-tren-card-amd-nhung-co-mot-danh-doi-lon-209260906143526689.htm
- Ảnh: ảnh minh hoạ chính thức của bài báo (so sánh in-game trước/sau + card Radeon) →
  `assets/img/article-hero.jpg`.
- Nguồn `vn`, giữ nguyên số liệu, viết lại gọn theo văn phong bản tin (không phải tin `intl`, không
  cần dịch).

## Góc tranh luận (nuôi act CTA)
Thành tựu kỹ thuật đáng nể — chạy được công nghệ Neural Rendering độc quyền của Nvidia trên phần
cứng đối thủ — **vs** cái giá quá lớn: hiệu năng sụt nghiêm trọng, phần mềm không chính chủ, có
trường hợp bị Windows Defender cảnh báo là Trojan. "Bước đột phá kỹ thuật hay rủi ro không đáng thử?"

## Số liệu / dữ kiện xác nhận (KHÔNG bịa thêm ngoài danh sách này — đối chiếu `?article=d198c6fd963a`)
- Modder **danielblnc** tạo ra công cụ **DLSS-NR-on-AMD**, cho phép **DLSS 5 Neural Rendering** của
  Nvidia (mới ra mắt độc quyền trên NBA 2K27, ban đầu chỉ dành cho dòng **GeForce RTX 50**) chạy
  được trên card đồ hoạ **Radeon** của AMD.
- Hoạt động trên card kiến trúc **RDNA 4** và một số mẫu **RDNA 3**; chỉ dùng được với game
  **DirectX 12** đã hỗ trợ sẵn công nghệ **FSR** của AMD.
- Trên **Radeon RX 9070 XT**, game **Cyberpunk 2077** đạt khoảng **33 FPS** ở độ phân giải **1080p**
  khi bật DLSS 5 — tăng nhẹ so với **28–30 FPS** của bản đầu.
- Một thử nghiệm được **Tom's Hardware** dẫn lại: hệ thống giảm từ hơn **80 FPS** xuống còn khoảng
  **11–12 FPS** sau khi bật DLSS 5. Một người dùng Reddit khác: giảm từ khoảng **120 FPS** xuống
  còn **30 FPS**. (Bài gốc lưu ý các kết quả này chưa thể so sánh trực tiếp do khác game/thiết lập.)
- Đây **không phải lớp dịch CUDA sang AMD** — phần thực thi mạng thần kinh được viết lại riêng cho
  kiến trúc AMD (kernel HIP, bố trí bộ nhớ riêng). GPU Radeon RX 9000 hỗ trợ định dạng tính toán
  **FP8**, nhưng DLSS 5 vốn được Nvidia tối ưu cho **Tensor Core** chuyên dụng nên vẫn chậm hơn
  nhiều.
- Mục tiêu của nhà phát triển: đưa hiệu năng RX 9070 XT lên tương đương **RTX 5070 Ti** — khoảng
  cách hiện tại **vẫn còn rất xa**.
- RX 7000 (RDNA 3) có thể chạy nhưng dự đoán hiệu năng thấp hơn do không hỗ trợ FP8 như RDNA 4;
  Radeon đời cũ hơn chưa được hỗ trợ. Vulkan chưa hỗ trợ, đang trong kế hoạch.
- Công cụ **không được Nvidia hay AMD chính thức xác nhận/chứng thực**, mã nguồn phần thực thi
  chưa công bố đầy đủ (người dùng tải file EXE cài đặt); nhà phát triển nói người dùng tự chịu rủi
  ro. Không chứa mã hoặc dữ liệu của Nvidia — được mô tả là bản tái triển khai độc lập.
- Một số người dùng trên Reddit cho biết **Windows Defender** đã cách ly tệp cài đặt vì nhận diện là
  **Trojan** — bài gốc lưu ý điều này chưa chứng minh công cụ chứa mã độc (phần mềm mod hay bị cảnh
  báo nhầm), nhưng khuyến cáo thận trọng, không thử trên máy chứa dữ liệu quan trọng.
- Công cụ cũng không hoạt động trong game có bật hệ thống chống gian lận (anti-cheat).

## Voice
ElevenLabs, giọng "Khánh Lâm - tin tức, thời sự" (`voice_id RCmOaM1iiIH5xX3QXjIF`), `model_id
eleven_v3`, speed ~1.09.
