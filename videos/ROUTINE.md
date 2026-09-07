# ROUTINE — trình tự bắt buộc cho cloud routine "Công Nghệ Số"

File này là checklist thao tác mà routine cloud (chạy 3 khung giờ/ngày) phải làm ĐÚNG THỨ TỰ.
Quy tắc brand/style đầy đủ ở `BRAND-SYSTEM.md` / `PRODUCTION-WORKFLOW.md` / `CONSTRUCTION-STYLES.md`
(đọc 3 file đó TRƯỚC). Video mẫu tham chiếu: `videos/astra-openai/`.

---

Bạn đang tự động sản xuất 1 video tin tức công nghệ / AI cho kênh "Công Nghệ Số", chạy không giám sát theo lịch. Đọc kỹ 3 file sau TRƯỚC KHI làm bất cứ điều gì — đây là toàn bộ quy tắc bắt buộc, không được bỏ qua hay tự suy đoán thay thế:
  - videos/BRAND-SYSTEM.md
  - videos/PRODUCTION-WORKFLOW.md
  - videos/CONSTRUCTION-STYLES.md

`<EXEC>` = https://script.google.com/macros/s/AKfycbyjZ02o6kzCnDNHEstgQV2wixqYZY6zSub9JGidKLudLT4sOlR3A5Un2TDP5d7xOsic/exec
`<REPO>` = quangnv-cloud/cong-nghe-so (nhánh master)

Thực hiện đúng trình tự trong videos/PRODUCTION-WORKFLOW.md, cụ thể:

0. (1 lần, đầu run) Sandbox cloud KHÔNG có sẵn `lyria-recipe.py` (BGM) và `carve.mjs` (audio ducking) — chạy `cd /tmp && npx --yes hyperframes@0.8.30 skills` để cài bộ skill chính chủ chứa 2 script này (`~/.claude/skills/media-use/audio/scripts/lyria-recipe.py` và `~/.claude/skills/hyperframes-audio/scripts/carve.mjs`). Cũng `pip install --quiet google-genai` cho lyria-recipe.py. KHÔNG tự viết script thay thế, KHÔNG bỏ bước BGM/carve.

1. Lấy tin ứng viên: GET <EXEC>?category=vn và GET <EXEC>?category=intl. Chọn 1 tin công nghệ / AI đáng chú ý nhất trong cửa sổ thời gian gần nhất — ưu tiên: ra mắt sản phẩm / mô hình lớn, số liệu cụ thể (vốn đầu tư, benchmark, thị phần, giá), tác động tới người dùng / doanh nghiệp VN, VÀ có góc tranh luận rõ (được / mất, bước tiến / mối lo) để nuôi act CTA cuối. Mỗi item có `hasImage` — CHỈ chọn tin `hasImage: true`. Sau khi chọn, POST <EXEC> với {"id":"<id>","video":"<slug sẽ tạo>"} để đánh dấu đã dùng.

2. Đọc nội dung tin: GET <EXEC>?article=<id đã chọn> → trả JSON {"ok":true,"source":"...","title":"...","text":"<văn bản bài báo>"}. TUYỆT ĐỐI KHÔNG WebFetch / curl thẳng trang báo (domain tin không nằm trong egress allowlist của sandbox — Apps Script tải hộ từ IP Google). Nếu trả {"ok":false} (trang JS-render không parse được text), dùng `title` + phần tóm tắt có sẵn; nếu quá mỏng để dựng đủ 7 act thì quay lại bước 1 chọn tin khác (POST đánh dấu used tin cũ trước).
   - Nếu tin từ nguồn `intl` (tiếng Anh): VIẾT LẠI bằng tiếng Việt cho khán giả VN — KHÔNG dịch máy word-by-word. Giữ tên riêng (OpenAI, Nvidia, Gemini, ChatGPT, iPhone...) và thuật ngữ phổ biến. Đóng khung "điều này nghĩa là gì với người dùng / doanh nghiệp VN" nếu có góc đó. TUYỆT ĐỐI không bịa số liệu ngoài bài gốc.
   - Nếu tin từ nguồn `vn`: viết lại gọn theo văn phong bản tin, giữ nguyên số liệu.

3. Nhận "cách dựng" (construction style): POST <EXEC> với {"action":"claim_style","video":"<slug>"} → trả {"ok":true,"index":N,"style":"N-tên"}. Dùng ĐÚNG style đó (chi tiết ở videos/CONSTRUCTION-STYLES.md). KHÔNG đọc videos/style-rotation-state.json để lấy chỉ số. Gọi claim_style NGAY SAU bước 1 (đã POST đánh dấu used), trước khi dựng.

4. Viết BRIEF.md + SCRIPT.md + CAPTION.md trong videos/<slug>/. Khởi tạo project qua hyperframes CLI (KHÔNG copy state file từ project cũ).
   - SCRIPT.md: MỘT dòng = MỘT act (7 dòng, act 7 là CTA), văn phong tin tức. TUYỆT ĐỐI KHÔNG viết tắt — viết đầy đủ đúng cách đọc thành tiếng vì ElevenLabs đọc verbatim: "AI" → "trí tuệ nhân tạo" (hoặc "ây-ai" nếu ngữ cảnh cần, nhất quán trong 1 video), "AGI" → "trí tuệ nhân tạo tổng quát", "API" → "ây-pi-ai", "CEO" → "giám đốc điều hành", "USD" → "đô la Mỹ", "GB"/"TB" → "gi-ga-bai"/"tê-ra-bai" (bảng đầy đủ ở mục "Voiceover" của videos/BRAND-SYSTEM.md). Tên riêng đọc nguyên được thì giữ. Số lớn viết theo cách người Việt đọc ("4.000 tỷ" → "4 nghìn tỷ").
   - QUAN TRỌNG: lời voice act 7 (CTA) kêu gọi để lại bình luận / nêu quan điểm nhưng KHÔNG được nhắc tên kênh ("Công Nghệ Số") — TTS đọc "Công" thành "Cổng". Tên kênh chỉ xuất hiện bằng hình.
   - BRIEF.md và text hiển thị trên video vẫn được viết tắt bình thường — ràng buộc không-viết-tắt CHỈ áp cho SCRIPT.md.
   - CAPTION.md: theo đúng mẫu videos/astra-openai/CAPTION.md — dòng đầu 1 emoji + tiêu đề IN HOA nêu sự kiện/số liệu chính; 1 dòng trống; 2-3 đoạn ngắn nêu số liệu / bối cảnh / tranh cãi (mỗi đoạn mở 1 emoji như 📊 ⚠️ 💬); 1 câu hỏi tranh luận mời bình luận; 1 dòng trống; "📌 Nguồn: <tên nguồn>, <ngày>" (thêm " · dịch" nếu là nguồn intl); 1 dòng trống; hashtag gồm #CongNgheSo #TinCongNghe + 4-6 hashtag liên quan chủ đề. Kèm 1 bản rút gọn ≤500 ký tự (mục "Bản rút gọn cho Threads") để dành — tuyến này CHƯA đăng Threads. TUYỆT ĐỐI không bịa số liệu ngoài BRIEF.md/SCRIPT.md.

5. Ảnh minh hoạ bài báo (bắt buộc theo brand — Hook + Article Image Card + thumbnail): GET <EXEC>?image=<id tin> → trả JSON {"ok":true,"mime":"image/jpeg","filename":"...","data":"<base64>"}. Giải mã ra file: curl -s "<EXEC>?image=<id>" | jq -r .data | base64 -d > assets/img/article-hero.jpg. KHÔNG curl thẳng CDN báo. Nếu {"ok":false} → quay lại bước 1 chọn tin khác có hasImage:true.

6. Sinh giọng đọc ElevenLabs — model_id eleven_v3 (KHÔNG eleven_multilingual_v2 — không hỗ trợ tiếng Việt), voice_id RCmOaM1iiIH5xX3QXjIF ("Khánh Lâm - tin tức, thời sự"), voice_settings.speed ~1.09, key từ biến môi trường ELEVENLABS_API_KEY. Tạo TỪNG DÒNG script 1 file mp3 riêng (line1.mp3 … line7.mp3), không gộp. Đo ffprobe từng file (input cho timing frame).

7. Dựng composition 7 act (Hook → What happened → Key facts → Data moment → Context → Impact → CTA) theo đúng định hướng ẩn dụ hình ảnh của style đã claim ở bước 3. Hook + Brand Anchor (logo + tên kênh "Công Nghệ Số" góc trên-phải, "Nguồn:" góc trên-trái) + act 7 CTA giữ cố định theo brand, không thuộc style. Act 6 (Impact) nội dung là sự thật/số liệu đã xảy ra — KHÔNG suy đoán tương lai. Act 7 CTA: câu hỏi tranh luận của tin + 2 lựa chọn đối lập (icon bằng CSS shape, KHÔNG emoji) + pill "Bình luận quan điểm của bạn" + chữ ký logo (tham chiếu videos/astra-openai/compositions/frames/07-cta.html). Ảnh Hook/Article Image Card dùng file đã tải ở bước 5. Logo dùng videos/<slug>/public/logo.png (copy từ videos/astra-openai/public/logo.png). data-duration mỗi frame = độ dài voice thật (bước 6) + đệm ~0.3-0.5s. Tổng thời lượng dưới 75 giây. VENDOR GSAP LOCAL (assets/vendor/gsap.min.js từ npm i gsap) — KHÔNG dùng <script src="cdn.jsdelivr.net/...">, CDN đó bị chặn ở sandbox. KHÔNG emoji trong composition (thiếu font khi render).
   ⚠️ CÂN BẰNG DỌC (bắt buộc — lỗi đã tái phát 2 lần): nội dung MỖI frame phải LẤP ĐẦY khung 1080×1920, KHÔNG dồn hết lên 55-65% trên rồi để trống đen nửa dưới. Phần tử cuối của frame kết thúc quanh top: 1400-1680px, không dừng ở ~1000px. Frame ít nội dung → căn giữa dọc HOẶC phóng to element. Bám dải phân bố dọc của videos/astra-openai/compositions/frames/ (top ~220 → ~1290px+). Xem mục "Cân bằng dọc" trong BRAND-SYSTEM.md. Khi soát thumbnail/frame ở bước 10, với MỖI frame tự hỏi "nửa dưới có trống đen không?" — có thì sửa trước khi render.

8. BGM: Google Lyria (lyria-recipe.py, key GEMINI_API_KEY) — recipe CALM: --density 0.25 --brightness 0.4, prompt kiểu "calm ambient tech-news underscore, soft synth pads, sparse, minimal pulse, no drums, instrumental only", LUÔN kèm --negative-prompt "vocals, lyrics, singing, choir, rap, spoken word, humming". BGM ambient NHẸ, ít nhịp — KHÔNG dùng prompt "driving/fast-paced". Retrim khớp tổng thời lượng + fade-out 2-3s cuối. data-volume track BGM = 0.30. SFX mật độ vừa phải. Gắn data-audio-group="voiceover" cho mọi <audio> giọng, rồi chạy node <hyperframes-audio skill dir>/scripts/carve.mjs --comp index.html --strength 0.4. Chạy lại carve sau MỌI thay đổi timing/audio.

9. npm run check — fix hết error trước khi render.

10. Trước khi render: kiểm tra ffmpeg -version, nếu chưa có thì sudo apt-get update && sudo apt-get install -y ffmpeg (sandbox có quyền root). Render bằng npm run render. Verify đầy đủ 4 bước theo mục 7 của videos/PRODUCTION-WORKFLOW.md: (1) ffprobe duration đúng thiết kế; (2) ffmpeg silencedetect — không có khoảng lặng chết giữa video; (3) trích frame tại các mốc quan trọng, xem bằng Read; (4) transcript so với SCRIPT.md — nếu Whisper model host bị chặn thì dùng Gemini multimodal (generativelanguage.googleapis.com, gọi GET /v1beta/models trước để lấy tên model còn dùng được, vd gemini-flash-latest). Soát riêng lỗi đọc lắp / đánh vần do viết tắt lọt vào SCRIPT.md — nếu có, sửa dòng đó thành dạng viết đầy đủ rồi sinh lại đúng file voice đó. Nếu render/verify thất bại hoàn toàn dù đã thử cài đặt, DỪNG LẠI, ghi rõ lý do.

11. Xuất thumbnail: ffmpeg -y -ss 3.5 -i output/<slug>.mp4 -frames:v 1 -q:v 2 output/thumbnail.jpg (t trong cửa sổ Hook 3-5s, sau khi toàn bộ animation Hook vào ổn định — đọc timeline compositions/frames/01-hook.html để tính chính xác). Xem lại bằng Read — xác nhận logo + tên kênh + badge nguồn + tiêu đề + 2 tag tương phản đều hiện đủ, rõ, không mờ/cắt.

12. Thêm 1 dòng vào mảng "log" của videos/style-rotation-state.json (index + style + slug + ngày) cho người đọc theo dõi — KHÔNG cần sửa last_used_index (con trỏ thật do claim_style / Apps Script quản lý).

13. Commit + push toàn bộ videos/<slug>/ (kèm output/<slug>.mp4 + output/thumbnail.jpg — thư mục output KHÔNG bị .gitignore; node_modules/ thì bị) lên <REPO> nhánh master.

14. Đăng Facebook Fanpage — POST <EXEC> (endpoint đã cấu hình sẵn token Facebook — KHÔNG cần và KHÔNG được tự tìm/nhập token nào khác):
   {"action":"publish_facebook","video_url":"https://raw.githubusercontent.com/quangnv-cloud/cong-nghe-so/master/videos/<slug>/output/<slug>.mp4","thumbnail_url":"https://raw.githubusercontent.com/quangnv-cloud/cong-nghe-so/master/videos/<slug>/output/thumbnail.jpg","caption":"<CAPTION.md, phần TRÊN dấu --->","video":"<slug>","title":"<tiêu đề tin>"} — đăng video lên Reels của Trang. thumbnail_url BẮT BUỘC.
   Chỉ gọi SAU KHI bước 13 push xong (Facebook tải video/ảnh từ raw.githubusercontent.com). Gọi POST bằng client theo được redirect 302 giữ nguyên POST (vd python urllib) — curl -L làm mất Content-Length (lỗi 411) hoặc đổi POST→GET. Lệnh tự ghi log vào Google Sheet. Nếu thất bại, KHÔNG coi cả routine là thất bại — ghi rõ lỗi vào tóm tắt, phần sản xuất video vẫn hoàn tất nếu bước 10-13 ok.

15. Đăng kênh YouTube — POST <EXEC> (đã cấu hình sẵn OAuth2 refresh token YouTube — KHÔNG tự tìm/nhập credential):
   {"action":"publish_youtube","video_url":"https://raw.githubusercontent.com/quangnv-cloud/cong-nghe-so/master/videos/<slug>/output/<slug>.mp4","thumbnail_url":"https://raw.githubusercontent.com/quangnv-cloud/cong-nghe-so/master/videos/<slug>/output/thumbnail.jpg","title":"<tiêu đề tin> #Shorts","description":"<CAPTION.md, phần TRÊN dấu --->","privacy":"public","video":"<slug>"}
   Hệ thống tự viết hoa toàn bộ tiêu đề trước khi đăng — không cần tự viết hoa. Chỉ gọi SAU KHI bước 13 push xong. Nếu lệnh thất bại toàn bộ, hoặc chỉ phần thumbnail báo lỗi 403 youtube.thumbnail (quyền custom thumbnail của kênh mới chỉ mở sau ~24h kể từ khi xác minh SĐT), KHÔNG coi cả routine là thất bại — video vẫn đăng thành công dù thiếu thumbnail tùy chỉnh; ghi rõ trạng thái vào tóm tắt.
   TUYẾN NÀY CHƯA đăng Instagram / Threads — KHÔNG gọi publish_instagram / publish_threads.

16. Chốt thumbnail YouTube: xem result.thumbnail (và result.thumbnail_attempts) trong phản hồi publish_youtube. Nếu code != 200 (hoặc để chắc chắn), SAU khi đăng xong đợi ~90s rồi gọi POST <EXEC> {"action":"yt_set_thumbnail","video_id":"<id YouTube>","thumbnail_url":"https://raw.githubusercontent.com/quangnv-cloud/cong-nghe-so/master/videos/<slug>/output/thumbnail.jpg"}. code:200 là xong. Nếu vẫn 403 youtube.thumbnail → ghi "chưa dính do quyền kênh chưa mở", không coi là lỗi routine.

17. Kết thúc bằng 1 bản tóm tắt ngắn: tin đã chọn + nguồn (+ "đã dịch từ <nguồn>" nếu intl), style + index từ claim_style, thời lượng video, kết quả verify 4 bước, đường dẫn file trong repo, kết quả đăng Facebook (Reel — thành công/lỗi + post id), kết quả đăng YouTube (thành công/lỗi + video id/link + trạng thái thumbnail). Nếu BẤT KỲ bước 1-13 thất bại, DỪNG LẠI ở đó, KHÔNG thực hiện bước 14-16, không hạ thấp tiêu chuẩn brand hay bỏ bước verify — báo lỗi rõ ràng trong tóm tắt thay vì giao 1 video lỗi hoặc đăng nhầm nội dung.
