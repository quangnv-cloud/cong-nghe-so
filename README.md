# Công Nghệ Số

Kênh tin tức công nghệ / AI tự động — tiếng Việt, khán giả VN. Nguồn: **chỉ báo công nghệ
Việt Nam** (VnExpress Số hóa, GenK, Dân Trí, Thanh Niên, Znews, VietnamNet — bỏ nguồn quốc tế
08/09/2026). Tự dựng video (HyperFrames) + tự đăng theo lịch lên Facebook Fanpage và YouTube
(Instagram / Threads bổ sung sau).

Tuyến nội dung độc lập hoàn toàn với "Kinh Tế Số / BOT BÁN HÀNG · KINH DOANH" — Gmail riêng,
Apps Script riêng, token riêng, repo riêng.

## Cấu trúc

| Thư mục | Nội dung |
|---|---|
| `automation/news-fetch-gas/` | `Code.gs` — Apps Script proxy: kéo RSS, chống trùng, phục vụ ảnh (`?image=`), và các endpoint đăng bài (`publish_facebook`, `publish_youtube`, …). `SETUP.md` + `SETUP-FB-YT.md` — hướng dẫn deploy + lấy token. |
| `videos/astra-openai/` | Video mẫu validate pipeline: "OpenAI ra mắt Astra" (dịch từ TechCrunch), 62s dọc 1080×1920. `output/openai-astra.mp4` + `thumbnail.jpg`. |
| `docs/` | Trang chủ + Chính sách quyền riêng tư (GitHub Pages) — dùng cho màn hình xác nhận OAuth của app YouTube. |
| `BRAND-PROPOSAL.md` | Định hướng thương hiệu (màu, typo, cấu trúc 7 act có CTA). |
| `ROUTINE-PROMPT.md` | Prompt mẫu cho cloud routine dựng + đăng video. |
| `SETUP-CHECKLIST.md` | Ai làm gì trong quá trình dựng tuyến. |

## Bảo mật

Token / API key **không bao giờ** nằm trong repo này. Tất cả đọc từ **Script Properties**
của dự án Apps Script (`FB_PAGE_ACCESS_TOKEN`, `FB_PAGE_ID`, `YOUTUBE_CLIENT_ID`,
`YOUTUBE_CLIENT_SECRET`, `YOUTUBE_REFRESH_TOKEN`, `SPREADSHEET_ID`, …).
