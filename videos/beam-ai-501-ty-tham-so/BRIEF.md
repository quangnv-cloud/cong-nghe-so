# BRIEF — Beam: mô hình AI 501 tỷ tham số, mở trọng số, huấn luyện bằng 10.500 GPU

Video routine SÁNG (7h30 giờ VN) cho kênh "Công Nghệ Số". Style xoay vòng: **7-timeline-chronology**
(index 6, claim_style ngày 2026-10-08, lần đầu style này được dùng cho kênh).

## Nguồn
- Thanh Niên — "Xuất hiện mô hình AI 500 tỉ tham số dùng tới 10.500 GPU để huấn luyện" (dẫn Wccftech),
  lấy qua `?article=881d9f699fce`, `pubDate` 2026-10-07.
- Ảnh: `?image=881d9f699fce` → `assets/img/article-hero.png` — ảnh minh hoạ ý niệm mạng nơ-ron
  (quả cầu node phát sáng kết nối nhau), KHÔNG phải ảnh người/cảnh thật, không watermark.

## Góc tranh luận cho CTA
Reflection AI mở công khai toàn bộ trọng số mô hình 501 tỷ tham số, chỉ kích hoạt ~23 tỷ tham số
mỗi lần (hiệu quả hơn) — nhưng để huấn luyện ra nó, hãng phải huy động tới 10.500 card đồ hoạ
Nvidia GB300 chạy liên tục 4 tuần. → CTA: "Mở trọng số minh bạch, tiết kiệm tài nguyên hơn — hay
chạy đua hàng chục nghìn card đồ hoạ chỉ để huấn luyện 1 mô hình là lãng phí?"

## Số liệu / dữ kiện xác nhận (KHÔNG bịa thêm ngoài danh sách này — đối chiếu `?article=`)
- **Beam** — mô hình AI mới do **Reflection AI** giới thiệu (theo Wccftech), có **501 tỷ tham số**.
  Hướng đến lập trình, suy luận và vận hành tác nhân AI (agent) nhiều bước.
- Đây là mô hình **open-weight (mở trọng số)** — cho phép nhà phát triển tải về, triển khai hoặc
  tiếp tục tinh chỉnh theo nhu cầu riêng. (Đây là trạng thái/thiết kế hiện tại, không phải dự đoán.)
- Dù có hơn 500 tỷ tham số, Beam chỉ **kích hoạt khoảng 23 tỷ tham số** tại một thời điểm, nhờ
  kiến trúc **Mixture-of-Experts (hỗn hợp chuyên gia — MoE)** — giảm lượng tính toán cần thiết so
  với huy động toàn bộ 501 tỷ tham số cho mọi tác vụ.
- Beam được **tiền huấn luyện (pretraining) trên 23.800 tỷ token**, thực hiện trong **chưa đầy 4
  tuần** trên cụm **6.144 card đồ hoạ (GPU) Nvidia GB300 NVL72**.
- Giai đoạn **học tăng cường (reinforcement learning)** dùng tới **10.500 card đồ hoạ Nvidia GB300**,
  chạy liên tục trong **4 tuần**.
- Hệ thống tạo ra **hơn 100 triệu chuỗi tương tác thử nghiệm**, sử dụng khoảng **1,3 tỷ sandbox**
  (môi trường thực thi cô lập); duy trì trung bình **110.000 rollout đồng thời**, hỗ trợ tới
  **170.000 sandbox hoạt động cùng lúc**.
- Theo kết quả Reflection AI công bố, Beam đạt điểm suy luận **tương đương GLM-5.2** ở một số
  phép thử, nhưng dùng lượng **inference compute** thấp hơn khoảng **3-4 lần** — đây là **ước tính**
  dựa trên số tham số hoạt động và lượng token tạo ra, **KHÔNG phải đo trực tiếp** toàn bộ chi phí
  vận hành thực tế (bài gốc nói rõ điều này — phải giữ nguyên qualifer "ước tính" khi dựng).
- Beam hiện vẫn trong quá trình kiểm thử tìm điểm yếu/rủi ro; Reflection AI **dự kiến công bố** đầy
  đủ trọng số, báo cáo kỹ thuật trong **tháng 10** (đây LÀ dự định công ty tuyên bố, không phải sự
  kiện đã xảy ra — act 6/Impact KHÔNG dùng chi tiết "dự kiến tháng 10" này, chỉ dùng sự thật đã
  xảy ra: Beam ĐÃ là mô hình mở trọng số ở quy mô hiếm có).

## GATE A — kết quả
Tin công nghệ/AI thông thường (ra mắt mô hình AI mới, số liệu kỹ thuật/huấn luyện) → **GREEN**.
Không thuộc danh mục loại bỏ (không cáo buộc hình sự, không chính trị/bầu cử/xung đột, không y tế
"thuốc thần", không tài chính "cam kết lãi", không deepfake/phát ngôn giả, không khai thác trẻ em/
bạo lực/lừa đảo). Không có yếu tố nhạy cảm phụ (không chạm AI & việc làm / kiểm soát xuất khẩu chip /
quyền riêng tư / kiện bản quyền AI) — thuần kỹ thuật/sản phẩm. → tiếp tục dựng, không cần framing
YELLOW đặc biệt ngoài B1 (phân biệt ước tính vs đo thực tế, dự kiến vs đã xảy ra).

## Cấu trúc 7 act (style 7-timeline-chronology)
1. **Hook**: masthead + badge nguồn (Thanh Niên) + ngày (7/10/2026) + "BEAM" to + 2 tag: "● Mở
   trọng số" / "▲ 10.500 GPU".
2. **What happened**: ảnh bài báo trong card (badge mốc thời gian nhỏ cạnh kicker) + panel: Reflection
   AI ra mắt Beam, mô hình AI mở trọng số 501 tỷ tham số.
3. **Key facts**: 3 fact xếp dọc theo trục đứng bên trái (đường kẻ dọc + node tròn nở khi xuất hiện):
   kiến trúc MoE chỉ kích hoạt 23 tỷ tham số; tiền huấn luyện 23.800 tỷ token trên 6.144 GPU GB300,
   chưa đầy 4 tuần; học tăng cường dùng 10.500 GPU GB300 suốt 4 tuần.
4. **Data moment**: con số chính "10.500" (card đồ hoạ) tại 1 node lớn trên trục ngang giữa khung,
   trục vẽ dần trái→phải rồi dừng tại node khi số chốt — ẩn dụ trung tâm style.
5. **Context**: trục thời gian ngang đầy đủ 4 mốc (node + nhãn giai đoạn dưới, giá trị trên):
   Tiền huấn luyện (6.144 GPU) → Học tăng cường (10.500 GPU, 4 tuần) → Kiểm thử (100 triệu chuỗi,
   170.000 sandbox đồng thời) → So sánh hiệu năng (ngang GLM-5.2, ít hơn 3-4 lần compute — ước tính).
6. **Impact** (sự thật đã xảy ra, không suy đoán): 2 node cuối trục phóng to thành khối tác động —
   "Một trong số rất ít mô hình >500 tỷ tham số được mở trọng số công khai" / "Nhà phát triển toàn
   cầu có thể tải về, triển khai, tinh chỉnh tự do — khác phần lớn mô hình hàng đầu vẫn đóng kín".
7. **CTA**: "Mở trọng số minh bạch & tiết kiệm tài nguyên, hay chạy đua hàng chục nghìn card đồ hoạ
   là lãng phí?" + 2 lựa chọn đối lập (mũi tên lên xanh / tam giác cảnh báo cam) + pill "Bình luận
   quan điểm của bạn" + chữ ký logo.

## Voice
Vbee TTS, giọng "HN - Ngọc Huyền" (`voice_code: hn_female_ngochuyen_full_48k-fhg`),
`speed_rate: 1.09` (theo ROUTINE.md bước 6, thay ElevenLabs từ 2026-09-30).
