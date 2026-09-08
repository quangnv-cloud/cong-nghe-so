# Prompt routine cloud — tuyến tin công nghệ / AI (BẢN MẪU CŨ — ĐÃ THAY BẰNG videos/ROUTINE.md)

> SUPERSEDED: routine thật đọc `videos/ROUTINE.md` (có GATE A/B/C + chỉ nguồn VN). File này giữ lại tham khảo lịch sử.

Thay các `<...>` bằng giá trị thật sau khi setup xong, rồi dán vào `RemoteTrigger create`
(1 trigger / khung giờ). Giống cấu trúc tuyến "BOT BÁN HÀNG · KINH DOANH" nhưng đã đổi:
lấy ảnh qua `?image=`, lấy style qua `claim_style`, thêm bước chốt lại thumbnail YouTube.

- `<EXEC_URL>` = exec URL của Apps Script project MỚI
- `<REPO>` = `quangnv-cloud/<tên-repo-mới>` (vd. `quangnv-cloud/bot-tin-cong-nghe`)
- `<KENH>` = tên kênh (vd. "Bản Tin Công Nghệ")

---

Bạn đang tự động sản xuất 1 video tin tức công nghệ / AI cho kênh "<KENH>", chạy không giám sát theo lịch. Đọc kỹ 3 file sau TRƯỚC KHI làm bất cứ điều gì — đây là toàn bộ quy tắc bắt buộc:
  - BRAND-SYSTEM.md
  - PRODUCTION-WORKFLOW.md
  - CONSTRUCTION-STYLES.md

Thực hiện đúng trình tự:

1. Lấy tin ứng viên: GET `<EXEC_URL>?category=vn` (chỉ nguồn báo VN). Chọn 1 tin công nghệ/AI đáng chú ý nhất trong cửa sổ thời gian gần nhất — ưu tiên: ra mắt sản phẩm/mô hình lớn, số liệu cụ thể (vốn đầu tư, hiệu năng, thị phần...), tác động tới người dùng/doanh nghiệp VN. Mỗi item có `hasImage` — chỉ chọn tin `hasImage: true`. Sau khi chọn, POST `<EXEC_URL>` với `{"id":"<id>","video":"<slug>"}` để đánh dấu đã dùng.
   - VIẾT LẠI gọn theo văn phong bản tin, giữ nguyên số liệu, thêm góc phân tích riêng. TUYỆT ĐỐI không bịa số liệu ngoài bài gốc.

2. Nhận style: POST `<EXEC_URL>` `{"action":"claim_style","video":"<slug>"}` → trả `{"index":N,"style":"N-tên"}`. KHÔNG đọc file rotation nào. Dựng theo đúng định hướng style đó (chi tiết ở CONSTRUCTION-STYLES.md).

3. Viết BRIEF.md + SCRIPT.md trong `videos/<slug>/`. Khởi tạo project qua hyperframes CLI (KHÔNG copy state file từ project cũ). SCRIPT.md: MỘT dòng = MỘT act, văn phong tin tức, act cuối là sự thật/số liệu đã có (không suy đoán tương lai). KHÔNG viết tắt (TTS đọc verbatim — "AI" viết "trí tuệ nhân tạo" hoặc "ây-ai" tùy ngữ cảnh brand quy định).

4. Ảnh minh hoạ: GET `<EXEC_URL>?image=<id tin>` → JSON `{"ok":true,"data":"<base64>"}`. Giải mã: `... | jq -r .data | base64 -d > assets/img/article-hero.jpg`. KHÔNG curl thẳng CDN báo. Nếu trả `ok:false` → chọn tin khác có `hasImage:true`.

5. Sinh giọng đọc ElevenLabs (model + voice_id theo BRAND-SYSTEM.md, key `ELEVENLABS_API_KEY`). Từng dòng 1 file.

6. Dựng composition theo cấu trúc act của brand + định hướng style bước 2. Hook + Brand Anchor cố định.

7. BGM (Lyria, key `GEMINI_API_KEY`, LUÔN `--negative-prompt "vocals, lyrics, singing, choir, rap, spoken word, humming"`) + SFX + carve.mjs.

8. `npm run check` — fix hết error. Cài ffmpeg/whisper nếu thiếu (`sudo apt-get install -y ffmpeg`; `pip3 install openai-whisper`). Render `npm run render`. Verify đủ 4 bước (ffprobe duration, silencedetect, frame extraction xem qua Read, transcript spot-check). Thất bại hoàn toàn dù đã thử cài → DỪNG, ghi lý do.

9. Thumbnail: `ffmpeg -y -ss 3.5 -i output/<slug>.mp4 -frames:v 1 -q:v 2 output/thumbnail.jpg` (điều chỉnh t trong cửa sổ Hook nếu cần). Verify qua Read.

10. Cập nhật log trong `style-rotation-state.json` (chỉ để người đọc — nguồn thật đã ở Apps Script).

11. Commit + push toàn bộ `videos/<slug>/` (kèm output/*.mp4 + thumbnail.jpg) lên `<REPO>` nhánh master.

12. Viết caption theo phong cách brand (xem PRODUCTION-WORKFLOW.md), kèm bản Threads ≤500 ký tự. Không bịa số liệu.

13-16. Đăng Facebook (Reel + Story ảnh), YouTube, Instagram (Reel), Threads — gọi POST tới `<EXEC_URL>` với các action `publish_facebook` / `publish_facebook_photo` / `publish_youtube` / `publish_instagram` / `publish_threads` (giống hệt tuyến cũ — endpoint đã cấu hình sẵn token, KHÔNG tự tìm/nhập token). `video_url`/`thumbnail_url` dùng `https://raw.githubusercontent.com/<REPO>/master/videos/<slug>/output/...`. Chỉ gọi SAU khi bước 11 push xong. 1 lệnh lỗi → KHÔNG coi cả routine thất bại, ghi rõ.

17. Chốt thumbnail YouTube: xem `result.thumbnail.code` trong phản hồi `publish_youtube`. Nếu != 200 (hoặc để chắc chắn), SAU khi đăng xong hết, đợi ~90s rồi gọi lại `POST <EXEC_URL> {"action":"yt_set_thumbnail","video_id":"<id YouTube>","thumbnail_url":"https://raw.githubusercontent.com/<REPO>/master/videos/<slug>/output/thumbnail.jpg"}` để chốt ảnh bìa thương hiệu.

18. Tóm tắt ngắn: tin + nguồn, style, thời lượng, kết quả verify, đường dẫn repo, kết quả đăng từng kênh (+ post id/permalink), trạng thái thumbnail YouTube. Nếu bất kỳ bước 1-11 thất bại → DỪNG ở đó, KHÔNG thực hiện 12-17, báo lỗi rõ ràng.
