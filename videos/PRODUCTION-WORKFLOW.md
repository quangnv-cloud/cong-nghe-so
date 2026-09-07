# Quy trình sản xuất — CÔNG NGHỆ SỐ

Runbook thao tác cho MỌI video tin công nghệ / AI. Toàn bộ quy tắc brand/style ở `BRAND-SYSTEM.md`,
10 cách dựng ở `CONSTRUCTION-STYLES.md` — đọc song song, không lặp lại ở đây.

`<EXEC>` = exec URL của Apps Script "CNS News Fetch":
`https://script.google.com/macros/s/AKfycbyjZ02o6kzCnDNHEstgQV2wixqYZY6zSub9JGidKLudLT4sOlR3A5Un2TDP5d7xOsic/exec`
`<REPO>` = `quangnv-cloud/cong-nghe-so` (nhánh `master`)

## 0. Trước khi bắt đầu

- Đọc `BRAND-SYSTEM.md` toàn bộ, đặc biệt mục "GSAP / kỹ thuật" (lỗi đã tái diễn nhiều lần).
- KHÔNG copy state file (`index.html`, `meta.json`, `compositions/`) từ project cũ — luôn
  `hyperframes init` qua workflow `/hyperframes` rồi build lại nội dung riêng cho tin mới.

## 1. Chọn tin & lên kịch bản

1. Lấy tin ứng viên: `GET <EXEC>?category=vn` và `GET <EXEC>?category=intl`. Mỗi item có `id`,
   `title`, `link`, `source`, `category`, `pubDate`, `hasImage`.
2. Chọn **1 tin công nghệ / AI đáng chú ý nhất** trong cửa sổ gần nhất — ưu tiên: ra mắt sản phẩm /
   mô hình lớn, số liệu cụ thể (vốn đầu tư, benchmark, thị phần, giá), tác động tới người dùng /
   doanh nghiệp VN, và **có góc tranh luận** (được/mất, bước tiến/mối lo) để nuôi act CTA. Chỉ chọn
   tin `hasImage: true`.
3. Đánh dấu đã dùng: `POST <EXEC>` với `{"id":"<id>","video":"<slug sẽ tạo>"}`.
4. **Đọc nội dung tin**: `GET <EXEC>?article=<id>` → `{"ok":true,"source":"...","title":"...","text":"<văn bản>"}`.
   KHÔNG `WebFetch` / `curl` thẳng trang báo (domain tin không nằm trong egress allowlist của
   sandbox — Apps Script tải hộ từ IP Google). Nếu `ok:false` (trang JS-render, không parse được),
   dùng `title` + phần mô tả có sẵn; nếu quá mỏng để dựng đủ 7 act, chọn tin khác.
5. **Nếu `category` là `intl` (tiếng Anh)**: VIẾT LẠI bằng tiếng Việt cho khán giả VN — KHÔNG dịch
   máy word-by-word. Giữ tên riêng (OpenAI, Nvidia, Gemini...) và thuật ngữ phổ biến. Đóng khung
   "điều này nghĩa là gì với người dùng / doanh nghiệp VN" nếu có góc đó. TUYỆT ĐỐI không bịa số
   liệu ngoài bài gốc.
   **Nếu `category` là `vn`**: viết lại gọn theo văn phong bản tin, giữ nguyên số liệu.
6. Nhận cách dựng: `POST <EXEC> {"action":"claim_style","video":"<slug>"}` → `{"ok":true,"index":N,"style":"N-tên"}`.
   Dùng ĐÚNG style đó (`CONSTRUCTION-STYLES.md`). KHÔNG đọc `style-rotation-state.json` để lấy chỉ
   số. Gọi `claim_style` NGAY SAU bước 3, trước khi dựng.
7. Viết `BRIEF.md` + `SCRIPT.md` + `CAPTION.md` trong `videos/<slug>/`.
   - `SCRIPT.md`: MỘT dòng = MỘT act (7 dòng), văn phong tin tức, **KHÔNG viết tắt** (bảng quy đổi
     ở mục "Voiceover" của `BRAND-SYSTEM.md`), act 6 là sự thật đã xảy ra, act 7 là câu hỏi CTA
     kêu gọi bình luận (KHÔNG nhắc tên kênh trong lời đọc).
   - `CAPTION.md`: theo mẫu ở `videos/astra-openai/CAPTION.md` — dòng đầu 1 emoji + tiêu đề IN HOA;
     2–3 đoạn ngắn (mỗi đoạn mở 1 emoji 📊 ⚠️ 💬); 1 câu hỏi tranh luận; `📌 Nguồn: <tên>, <ngày>`
     (thêm "· dịch" nếu intl); hashtag `#CongNgheSo #TinCongNghe` + 4–6 hashtag chủ đề. Kèm bản
     Threads ≤500 ký tự (để dành, tuyến này chưa đăng Threads).
8. Ảnh minh hoạ: `GET <EXEC>?image=<id>` → `{"ok":true,"data":"<base64>"}`. Giải mã:
   `curl -s "<EXEC>?image=<id>" | jq -r .data | base64 -d > assets/img/article-hero.jpg`.
   KHÔNG curl thẳng CDN báo. `ok:false` → chọn tin khác `hasImage:true`.

## 2. Giọng đọc (ElevenLabs)

Chi tiết ở mục "Voiceover" của `BRAND-SYSTEM.md`. Tóm tắt: từng dòng script → 1 file mp3
(`line1.mp3`…`line7.mp3`), `model_id: eleven_v3`, `voice_id: RCmOaM1iiIH5xX3QXjIF`, speed ~1.09,
key `ELEVENLABS_API_KEY`. Đo `ffprobe` từng file (input cho timing). Verify phiên âm ngược, soát
riêng lỗi đọc lắp do viết tắt.

## 3. Dựng composition

1. `hyperframes init` qua `/hyperframes` (không copy state cũ).
2. Dựng **7 act** (bảng trong `BRAND-SYSTEM.md`). Hook + Brand Anchor cố định (không thuộc style).
   5 act giữa (What happened / Key facts / Data moment / Context / Impact) dựng theo ẩn dụ hình ảnh
   của style đã claim ở §1.6 — tự thiết kế HTML/CSS/GSAP thật, mô tả style chỉ là định hướng.
   Act 7 CTA theo mẫu `videos/astra-openai/compositions/frames/07-cta.html`.
3. `data-duration` mỗi frame = độ dài voice thật + đệm ~0.3–0.5s. Rà lại mốc animation nội bộ.
4. Tổng thời lượng **dưới 75s**.
5. Ảnh Hook / Article Image Card dùng file đã tải ở §1.8. Logo dùng `public/logo.png`.

## 4. Nhạc nền & SFX

Chi tiết ở mục "Nhạc nền" của `BRAND-SYSTEM.md` + `videos/astra-openai/AUDIO-NOTES.md`. Tóm tắt:
Lyria calm (`--density 0.25 --brightness 0.4`, ambient, `--negative-prompt` bắt buộc), retrim +
fade-out, `data-volume` 0.30. Gắn `data-audio-group="voiceover"`, chạy
`node <hyperframes-audio skill dir>/scripts/carve.mjs --comp index.html --strength 0.4`.
**Chạy lại carve sau MỌI thay đổi timing/audio.**

## 5. Lint & QA

```bash
npm run check
```
Fix hết **error** trước khi render. Dùng Studio thumbnail (`preview --background` + endpoint
`.../thumbnail/index.html?t=<giây>&...&v=<cachebust>`) soát từng frame ít nhất 1 mốc, đặc biệt
frame có số liệu dài / nền ảnh + text (contrast WCAG AA).

## 6. Render

```bash
npx hyperframes preview --stop
npm run render
```
`ffmpeg` chưa có trên sandbox → `sudo apt-get update && sudo apt-get install -y ffmpeg` (có root).

## 7. Verify file render THẬT (bắt buộc đủ 4 bước)

```bash
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1 <mp4>   # 1) thời lượng
ffmpeg -i <mp4> -af silencedetect=noise=-35dB:d=0.6 -f null -                          # 2) không có lặng chết giữa video
ffmpeg -y -ss <t> -i <mp4> -frames:v 1 -q:v 2 out.png                                  # 3) trích frame, xem bằng Read
ffmpeg -y -i <mp4> -vn -ac 1 -ar 16000 audio.wav                                       # 4) transcript
python -m whisper audio.wav --model base --language Vietnamese --output_format txt
```
Whisper model host (`openaipublic.azureedge.net`) có thể bị chặn ở sandbox → thay bằng Gemini
multimodal: `POST generativelanguage.googleapis.com/.../models/<model>:generateContent` với
`inline_data` audio/wav. Gọi `GET /v1beta/models` trước để lấy tên model còn dùng được (vd.
`gemini-flash-latest` — tên có timestamp như `gemini-2.5-flash` dễ bị "no longer available").

Chỉ coi "xong" khi cả 4 bước sạch — không báo hoàn thành chỉ dựa `npm run check` / thumbnail.

## 7.5. Thumbnail

```bash
ffmpeg -y -ss 3.5 -i output/<slug>.mp4 -frames:v 1 -q:v 2 output/thumbnail.jpg
```
`t` trong cửa sổ Hook (3–5s), SAU khi toàn bộ animation Hook vào ổn định (đọc timeline
`compositions/frames/01-hook.html`: mốc `tl.fromTo` trễ nhất + `duration` của nó + ~0.3s). Xem lại
bằng Read — xác nhận logo + tên kênh + badge nguồn + tiêu đề + 2 tag đều hiện đủ, rõ, không mờ.

## 8. Commit + push

Commit toàn bộ `videos/<slug>/` (kèm `output/*.mp4` + `output/thumbnail.jpg` — KHÔNG bị
`.gitignore`; `node_modules/` thì bị) lên `<REPO>` nhánh `master`. Thêm 1 dòng vào mảng `log` của
`videos/style-rotation-state.json` (index + style + slug + ngày) cho người đọc theo dõi — con trỏ
thật do `claim_style` quản lý.

## 9. Đăng Facebook + YouTube

Chỉ gọi SAU KHI §8 push xong (FB/YT tải video từ `raw.githubusercontent.com`). Endpoint đã cấu hình
sẵn token — KHÔNG tự tìm / nhập token.

`<mp4>` = `https://raw.githubusercontent.com/quangnv-cloud/cong-nghe-so/master/videos/<slug>/output/<slug>.mp4`
`<jpg>` = `https://raw.githubusercontent.com/quangnv-cloud/cong-nghe-so/master/videos/<slug>/output/thumbnail.jpg`

a. **Facebook Reel**:
   `POST <EXEC> {"action":"publish_facebook","video_url":"<mp4>","thumbnail_url":"<jpg>","caption":"<CAPTION.md phần trên dấu --->","video":"<slug>","title":"<tiêu đề tin>"}`
   `thumbnail_url` BẮT BUỘC (nếu không FB tự chọn khung ngẫu nhiên).

b. **YouTube**:
   `POST <EXEC> {"action":"publish_youtube","video_url":"<mp4>","thumbnail_url":"<jpg>","title":"<tiêu đề tin> #Shorts","description":"<CAPTION.md phần trên dấu --->","privacy":"public","video":"<slug>"}`
   Hệ thống tự viết hoa tiêu đề — không tự viết hoa.

Gọi POST bằng client theo được redirect 302 giữ POST (vd `python urllib`) — `curl -L` làm mất
Content-Length (411) hoặc đổi POST→GET. 1 lệnh lỗi → KHÔNG coi cả routine thất bại, ghi rõ.

**IG / Threads**: code có sẵn (`publish_instagram` / `publish_threads`) nhưng tuyến này CHƯA link
tài khoản IG Business / tạo Threads token → **KHÔNG gọi** cho tới khi có chỉ đạo mới.

## 9.5. Chốt thumbnail YouTube

Xem `result.thumbnail` / `result.thumbnail_attempts` trong phản hồi `publish_youtube`. Nếu
`code != 200` (hoặc để chắc), sau khi đăng xong đợi ~90s rồi:
`POST <EXEC> {"action":"yt_set_thumbnail","video_id":"<id YouTube>","thumbnail_url":"<jpg>"}` → `code:200` là xong.
**Lưu ý**: kênh còn mới, quyền custom thumbnail chỉ mở sau ~24h kể từ khi xác minh SĐT. Nếu 403
`youtube.thumbnail`, ghi vào tóm tắt "video đã đăng, thumbnail chưa dính do quyền kênh" — KHÔNG coi
là routine thất bại.

## 10. Tóm tắt cuối

Tin + nguồn (+ "đã dịch từ <nguồn>" nếu intl), style + index, thời lượng, kết quả verify 4 bước,
đường dẫn repo, kết quả đăng FB (Reel — post id), YouTube (video id/link + trạng thái thumbnail).
Nếu BẤT KỲ bước 1–8 thất bại → DỪNG ở đó, KHÔNG làm 9–9.5, báo lỗi rõ ràng thay vì giao video lỗi
hoặc đăng nhầm nội dung.

## 11. Khi có phản hồi sửa (phiên tương tác)

- Chỉ thị rõ ràng dứt khoát ("bỏ đi", "sửa thành X", "áp dụng cho video sau") → làm luôn.
- Ý kiến chung / câu hỏi mở ("nhịp chậm không?") → trình bày phân tích + đề xuất, chờ xác nhận.
- Phản hồi thường trực cho video sau → ghi ngay vào `BRAND-SYSTEM.md` (brand) hoặc file này (quy
  trình), không chỉ sửa video hiện tại rồi quên.
