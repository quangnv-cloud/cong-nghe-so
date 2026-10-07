# COMPLIANCE — nvidia-von-hoa-6000-ty

policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-10-07T01:30:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): GREEN
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "Ảnh hero từ ?image=f5f528c0c726 (stock photo biên tập, logo Nvidia trên điện thoại đặt trên tiền đô la Mỹ), dùng trong Article Image Card có dẫn nguồn Znews, không chỉnh sửa nội dung ảnh; nhạc nền tự sinh qua Google Lyria (instrumental, không lời, có negative-prompt loại vocal); SFX từ bộ SFX repo (astra-openai/assets/sfx, dùng chung toàn kênh); video 100% tự dựng bằng HyperFrames, không reup."
claims_verified:
  - "Vốn hóa Nvidia tiến sát 6.000 tỷ USD (sát mốc 5.800 tỷ USD) — đối chiếu ?article=f5f528c0c726"
  - "Giá cổ phiếu tăng 28% từ đầu năm 2026 — đối chiếu ?article="
  - "Vốn hóa tăng thêm 1.200 tỷ USD — đối chiếu ?article="
  - "Đóng góp 14% mức tăng S&P 500 — đối chiếu ?article="
  - "Bỏ xa Apple gần 1.000 tỷ USD (vốn hóa #1 thế giới) — đối chiếu ?article="
  - "Cổ phiếu giảm 11% cuối tháng 3/2026 vì hoài nghi chi tiêu AI — đối chiếu ?article="
  - "Phê duyệt mua lại cổ phiếu 150 tỷ USD, lớn nhất lịch sử doanh nghiệp — đối chiếu ?article="
  - "Dự báo (không phải sự thật đã xảy ra) doanh thu FY2028 tăng 70% — đối chiếu ?article=, gắn nhãn 'dự báo' trong script"
  - "Trích dẫn Jensen Huang và nhận định Mizuho Securities — đối chiếu ?article="
sensitive_flags: []
vietnam_legal_flags: []
notes: "Tin tài chính nhưng là báo cáo số liệu vốn hóa/thị trường công khai, không phải lời mời đầu tư hay cam kết lợi nhuận từ kênh — không thuộc danh mục loại bỏ GATE A (financial scam/insider/cam kết lãi). Act 6 (Impact) chỉ dùng sự thật đã xảy ra (mua lại cổ phiếu đã phê duyệt, vị thế vốn hóa #1 đã đạt); dự báo doanh thu FY2028 được đặt ở Act 5 (Context) với ngôn từ 'dự báo' rõ ràng, không lẫn vào phần sự thật. Góc nhìn riêng (B7): trực quan hóa 'tiến trình tới mốc 6.000 tỷ USD' bằng ring-progress + đối chiếu cú giảm tháng 3 để tạo góc tranh luận tăng trưởng thật vs bong bóng định giá, không chỉ đọc lại tiêu đề báo. Hạn chế đã biết: bỏ qua caption karaoke đồng bộ giọng đọc (kỹ thuật BRAND-SYSTEM #3) vì ElevenLabs STT hết quota (0 credits) tại thời điểm sản xuất — không phải lỗi GATE, ghi nhận để video sau bổ sung khi quota khôi phục."
