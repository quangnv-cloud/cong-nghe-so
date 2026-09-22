# BRIEF — ai-code-tq-tu-dong-tai-cloud

## Nguồn
- Nguồn: GenK (dẫn lại từ đời sống & pháp luật / nguoiduatin.vn)
- Tiêu đề gốc: "Công cụ AI Trung Quốc âm thầm tải cả dự án của lập trình viên lên cloud, không có nút tắt"
- Ngày: 22/9/2026
- article id (Apps Script): 927c5be35e24
- Style claimed: index 4 — `5-map-and-geo`

## Tóm tắt sự việc (đối chiếu ?article=)
- Công cụ: **ZCode**, sản phẩm hỗ trợ lập trình của **Z.ai** (tên công ty đầy đủ: **Zhipu AI**), công ty trí tuệ nhân tạo Trung Quốc.
- Phát hiện ngày **18/9**, bởi blogger công nghệ Trung Quốc tên **Ferstar**.
- Ferstar phát hiện 1 tệp nén **313 MB** đang chờ tải lên dịch vụ đám mây của **Alibaba**.
- Hệ thống đã thử tải tệp này lên **564 lần** nhưng đều thất bại (do dung lượng quá lớn).
- 1 tệp nhỏ hơn, khoảng **15 KB**, đã tải lên **thành công**.
- Tệp lớn là bản sao 1 dự án thương mại, gồm cả **lịch sử thay đổi mã nguồn trên Git**.
- Dữ liệu được mã hoá nhưng khoá giải mã nằm trên máy chủ Z.ai → người dùng không tự kiểm tra được chính xác điều gì đã xảy ra.
- Nguyên nhân: tính năng **"Codebase Indexing"** được **bật mặc định**, người dùng **không có nút tắt**.
- Sau khi bị phát hiện: Z.ai đã **vô hiệu hoá tính năng**, **xin lỗi**, vá lỗi, và **cam kết mở mã nguồn ZCode** để cộng đồng/bên thứ ba kiểm tra độc lập.
- Một doanh nghiệp Trung Quốc từng nói 6 dự án của họ bị tải lên (gồm mã nguồn, mật khẩu database, thông tin cá nhân nhân viên) — nhưng sau đó **rút lại tuyên bố**, nói bằng chứng ban đầu không chính xác. → KHÔNG dùng chi tiết này trong SCRIPT (chưa xác nhận, dễ gây hiểu lầm là sự thật).
- Z.ai khẳng định dữ liệu bị xoá ngay sau khi tải lên; một tổ chức tiêu chuẩn công nghệ thuộc Bộ Công nghiệp Trung Quốc + công ty an ninh mạng NSFOCUS xác nhận điều này qua đánh giá độc lập.
- Một kỹ sư tại 1 công ty robot lớn của Trung Quốc nói doanh nghiệp mình đã cấm dùng công cụ Z.ai vì lo ngại bảo mật.

## Góc tranh luận (nuôi act CTA)
Tiện lợi của trợ lý AI lập trình tự động (index code, gợi ý, tự xử lý dữ liệu) **vs** rủi ro giao toàn bộ mã nguồn/dữ liệu nội bộ cho một công cụ AI mà người dùng không kiểm soát được — đặc biệt khi tính năng thu thập dữ liệu bật mặc định và không có cách tắt.

## GATE A
Tin công nghệ có yếu tố nhạy cảm phụ: **quyền riêng tư / bảo mật dữ liệu** → **YELLOW**. Framing trung lập: nêu rõ đây là sự cố đã xảy ra + phản hồi/khắc phục của công ty, không suy diễn thêm, không dùng chi tiết tuyên bố đã bị rút lại (6 dự án/mật khẩu database).

## Định hướng dựng (style 5 — map & geo)
Ẩn dụ: dữ liệu từ máy lập trình viên (điểm nội bộ/local) bị đẩy sang máy chủ đám mây tại Trung Quốc (Alibaba Cloud). Dùng bản đồ/route line + ghim địa danh để trực quan hoá luồng dữ liệu, con số 564 lần thử tải làm data moment trong 1 map-pin phóng to.

## Ảnh
- Lấy qua `?image=927c5be35e24` (Article Image Card, có dẫn nguồn GenK).
- Không tái dựng "hiện trường" giả bằng AI — chỉ dùng ảnh bài báo + đồ hoạ ý niệm (icon cloud, ghim bản đồ, khoá/ổ đĩa CSS shape).
