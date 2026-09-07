# DTO Master — DATA TRAFFIC ORGANIC (nguồn Looker Studio đa kênh)

Một Google Sheet duy nhất gom số liệu organic của mọi tuyến nội dung → Looker Studio hiển thị
tách theo `brand` + tổng `all channels`.

- **File master**: "Bản sao của BBH News Queue"
  `1isvFaqM9g6F8hFb3Fu5pvMg2Jgj017Nsh6R0OgHsof0` — sở hữu bởi `minhanhh1108`.
- Cả 2 Apps Script kênh (Kinh Tế Số + Công Nghệ Số) đều chạy dưới `minhanhh1108` → ghi thẳng được,
  không cần share.

## Cấu trúc

| Tab | Grain | Cột |
|---|---|---|
| `brands` | 1 dòng / tuyến | `brand · label · emoji · order · active` |
| `post_metrics` | 1 dòng / (brand, post_id) — GHI ĐÈ | `brand · platform · video_project · post_type · post_id · permalink · title · posted_at · posted_date · views · likes · reactions · comments · shares · last_checked` |
| `traffic_daily` ⭐ | 1 dòng / (brand, platform, ngày) — THÊM/upsert | `brand · platform · date · posts_published · views_total · views_delta · engagement_total · engagement_delta · followers · followers_delta` |

`brand` = tuyến nội dung (`kinh_te_so`, `cong_nghe_so`, …). `platform` = nền tảng (`facebook`,
`instagram`, `youtube`, `threads`). `*_delta` = chênh so với ngày trước = **traffic organic trong ngày**.

Tab cũ (`engagement_metrics` / `audience_growth` / `posts_log` / `news_queue`) **giữ nguyên** làm
bản chụp lịch sử — `setupMaster()` di trú dữ liệu KTS từ 2 tab đầu sang tab mới.

## Bước 1 — chạy `setupMaster()` (1 lần)

1. Mở file master → **Tiện ích mở rộng → Apps Script**
2. Dán toàn bộ `automation/analytics-master/Code.gs` → **Lưu**
3. Dropdown hàm → `setupMaster` → **Chạy** → cấp quyền
4. Log: tạo 3 tab, seed `brands`, di trú `post_metrics` + `traffic_daily` (KTS)

## Bước 2 — nối từng Apps Script kênh

Với **mỗi** Apps Script kênh (Kinh Tế Số, Công Nghệ Số): **⚙ Cài đặt dự án → Thuộc tính của tập
lệnh**, thêm 2 dòng:

| Tên | Giá trị |
|---|---|
| `MASTER_SHEET_ID` | `1isvFaqM9g6F8hFb3Fu5pvMg2Jgj017Nsh6R0OgHsof0` |
| `BRAND_SLUG` | `cong_nghe_so` (hoặc `kinh_te_so`) |

Code.gs đã có `mirrorAnalyticsToMaster_()` (gọi tự động ở cuối `refreshEngagementMetrics`, chạy 6h
sáng cùng trigger metrics). Không có 2 property này → hàm tự bỏ qua, không lỗi.

**Kinh Tế Số**: `mirrorAnalyticsToMaster_()` + 2 hằng `MASTER_*_HEADERS` cần được copy vào Code.gs
của repo `bot-ban-hang-kinh-doanh` (lấy nguyên khối từ cuối `automation/news-fetch-gas/Code.gs`
tuyến này), rồi thêm dòng `try { mirrorAnalyticsToMaster_(); } catch (e) {...}` sau
`refreshAudienceGrowth_()` trong `refreshEngagementMetrics`, deploy lại. (Phiên khác làm vì đó là
production tuyến cũ.)

## Bước 3 — chạy thử

Ở Apps Script kênh: dropdown → `refreshEngagementMetrics` → **Chạy**. Kiểm tra master:
`post_metrics` có dòng `brand = <slug>`, `traffic_daily` có dòng hôm nay (delta trống ở lần đầu,
có giá trị từ ngày thứ 2).

## Bước 4 — Looker Studio

1. **Tạo báo cáo mới** → nguồn dữ liệu **Google Sheets** → chọn file master → thêm 3 nguồn:
   `traffic_daily`, `post_metrics`, `brands`.
2. `traffic_daily`: đặt `date` kiểu Date, các cột `*_total`/`*_delta`/`followers*` kiểu Number.
3. **Blend** `traffic_daily` + `brands` theo key `brand` để lấy `label` (kèm emoji) + `order`.
4. **Trang "All channels"**:
   - Scorecard: `SUM(views_delta)`, `SUM(engagement_delta)`, `SUM(followers_delta)` — kỳ 7/28 ngày
   - Biểu đồ đường: dimension thời gian `date`, metric `views_delta`, **breakdown dimension =
     `label`** → mỗi tuyến 1 màu (đây là cả cây, xem 1 lần)
   - Bảng: dimension `label`, metric `views_delta` / `engagement_delta` / `followers` — sort `order`
5. **Filter control** trên `brand` (hoặc `label`) → người xem chọn 1 tuyến; để trống = tổng
   `all_channels`.
6. Muốn giống hệt sơ đồ cây (mỗi tuyến 1 trang riêng): nhân bản trang, đặt **page-level filter**
   `brand = cong_nghe_so`…
7. "Top bài": nguồn `post_metrics`, dimension `title` + `label`, metric `views`, sort giảm dần.

## Lưu ý

- **`traffic_daily` chỉ có xu hướng TỪ NGÀY BẮT ĐẦU CHẠY** — không backfill được engagement theo
  ngày (không có snapshot cũ). Follower history của KTS thì có (di trú từ `audience_growth`).
- `views_delta` có thể âm nếu nền tảng điều chỉnh số, hoặc bài bị xoá → ở Looker lọc `views_delta >= 0`
  nếu muốn "traffic dương" sạch.
- Khi thêm kênh mới: thêm dòng vào `brands` (active TRUE) + set `MASTER_SHEET_ID`/`BRAND_SLUG` ở
  Apps Script kênh đó. Không cần đụng master.
