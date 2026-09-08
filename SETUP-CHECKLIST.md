# Checklist setup — tuyến tin công nghệ / AI

Cấu hình đã chốt: tiếng Việt (khán giả VN), chỉ nguồn báo công nghệ VN,
đăng FB + IG + YT + Threads, tự dựng + tự đăng theo lịch. Cùng máy hiện tại (bỏ qua phần cài phần mềm).

Ký hiệu: **[A]** = anh làm · **[C]** = Claude làm · **[A+C]** = làm cùng

---

## 1. Nền tảng & repo

- [ ] **[A]** Tạo Gmail cá nhân mới (vd. `bottincongnghe@gmail.com`) — KHÔNG dùng `@botbanhang.vn`. Đăng nhập trên Chrome máy này.
- [ ] **[A]** Chốt **tên kênh** + tông màu (xem `BRAND-PROPOSAL.md`).
- [ ] **[A]** Tạo GitHub repo mới (vd. `bot-tin-cong-nghe`), private cũng được (public khi cần routine đọc — flip ở GitHub Settings như tuyến cũ).
- [ ] **[A]** Tạo 4 kênh mạng xã hội mới cho tuyến này:
  - Fanpage Facebook mới
  - Instagram → chuyển sang Business/Creator, liên kết vào Page mới qua Business Manager (không phải link cá nhân)
  - Kênh YouTube mới
  - Tài khoản Threads mới

## 2. Apps Script + Sheet (**[A+C]**)

- [ ] **[A]** `script.google.com` (Gmail mới) → Dự án mới.
- [ ] **[C]** Dán `Code.gs` (đã sửa `FEEDS` sang nguồn công nghệ + fallback og:image), đổi tiền tố `TECHNEWS` → tên kênh thật ở 3 chỗ (`NEWS_IMAGE_FOLDER_NAME`, 4× `SpreadsheetApp.create(...)`).
- [ ] **[A+C]** Chạy `fetchAndStore` 1 lần → cấp quyền (Sheets + Drive + UrlFetch) → xác nhận log "added N new item(s)".
- [ ] **[A+C]** Chạy `installHourlyTrigger` 1 lần.
- [ ] **[A+C]** Deploy → New deployment → Web app, Execute as: **Me**, Who has access: **Anyone** → copy **exec URL mới**.
- [ ] **[C]** Verify: `?category=vn` trả JSON có `items` + `hasImage`; `?image=<id>` trả base64.

## 3. Token 4 nền tảng (**[A]**, theo `automation/news-fetch-gas/SETUP.md`)

Mỗi nền tảng cần app/token RIÊNG cho kênh mới — không dùng lại token kênh "Kinh Tế Số".

- [ ] **Facebook**: Meta app (mới hoặc dùng lại app cũ, nhưng Page token phải của Page mới) → Page Access Token dạng System User, quyền `pages_manage_posts` + `pages_read_engagement` + `pages_show_list`.
- [ ] **Instagram**: thêm quyền `instagram_basic` + `instagram_content_publish` + `instagram_manage_insights` vào token trên; IG account phải Business + link đúng Page mới.
- [ ] **YouTube**: Google Cloud Console → OAuth Client mới → OAuth Playground lấy refresh token với scope `youtube.upload` + `youtube.readonly`.
- [ ] **Threads**: thêm sản phẩm Threads API vào app Meta, mời tài khoản Threads mới làm Tester (chấp nhận tại `threads.com/settings/website_permissions` → tab "Lời mời"), tạo token qua "Công cụ tạo mã người dùng".
- [ ] **[A]** Điền tất cả token/ID vào **Script Properties** của Apps Script project MỚI (Cài đặt dự án → Thuộc tính của tập lệnh). Tên property giống hệt tuyến cũ (xem `SETUP.md`).

## 4. Brand + video mẫu (**[C]**)

- [ ] **[C]** Scaffold repo mới: `automation/` + `BRAND-SYSTEM.md` + `PRODUCTION-WORKFLOW.md` + `CONSTRUCTION-STYLES.md` + `style-rotation-state.json`.
- [ ] **[C]** Dựng 1-2 video mẫu (local) → **[A]** duyệt phong cách.
- [ ] **[C]** Điều chỉnh brand theo phản hồi.

## 5. Cloud routine (**[A+C]**)

- [ ] **[A]** Tạo environment cloud riêng cho tuyến này tại claude.ai/code (hoặc dùng lại env cũ nhưng khác trigger). Network access "Custom": `script.google.com`, `script.googleusercontent.com`, `api.elevenlabs.io`, `generativelanguage.googleapis.com`, `github.com`, `raw.githubusercontent.com`, `objects.githubusercontent.com` + registry npm/pip. (KHÔNG cần domain CDN báo — ảnh đi qua `?image=`.)
- [ ] **[A]** Điền `ELEVENLABS_API_KEY` + `GEMINI_API_KEY` vào Environment variables của env đó.
- [ ] **[A]** Cài Claude GitHub App cho repo mới (quyền ghi) — như tuyến cũ.
- [ ] **[C]** Tạo trigger (tắt sẵn) mỗi khung giờ, prompt từ `ROUTINE-PROMPT.md` đã điền `<EXEC_URL>`/`<REPO>`/`<KENH>`.
- [ ] **[A+C]** Chạy thử 1 trigger có giám sát → **[A]** ưng → **[A]** bật lịch.

---

## Việc KHÔNG cần làm lại
Code đăng 4 nền tảng, chống đăng trùng, dedupe, tracker engagement/audience_growth, cơ chế `?image=`, khoá style — có sẵn trong `Code.gs`, chỉ deploy là chạy.
