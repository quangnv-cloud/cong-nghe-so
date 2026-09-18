import json

act_starts = json.load(open("assets/audio/act_starts.json"))
act_durs = json.load(open("assets/audio/act_durations.json"))
voice_durs = json.load(open("assets/audio/voice_durations.json"))
cap_html = open("assets/audio/cap_html.txt", encoding="utf-8").read()
cap_word_times = open("assets/audio/cap_word_times.txt", encoding="utf-8").read()

total = round(act_starts["7"] + act_durs["7"], 6)

frame_ids = {
    "1": "01-hook", "2": "02-what", "3": "03-facts", "4": "04-data",
    "5": "05-context", "6": "06-impact", "7": "07-cta",
}

scenes = "\n".join(
    f'      <div id="el-{frame_ids[i]}" class="scene" data-composition-id="{frame_ids[i]}" '
    f'data-composition-src="compositions/frames/{frame_ids[i]}.html" data-start="{act_starts[i]}" '
    f'data-duration="{act_durs[i]}" data-track-index="1"></div>'
    for i in [str(x) for x in range(1, 8)]
)

voices = "\n".join(
    f'      <audio id="el-voice-{i}" src="assets/audio/line{i}.mp3" data-start="{act_starts[str(i)]}" '
    f'data-duration="{voice_durs[str(i)]}" data-track-index="10" data-audio-group="voiceover"></audio>'
    for i in range(1, 8)
)

t2 = round(act_starts["2"], 6)
t3 = round(act_starts["3"], 6)
t4d = round(act_starts["4"] + 0.85, 6)
t5 = round(act_starts["5"], 6)
t6warn = round(act_starts["6"] + 0.3, 6)
t6cut = round(act_starts["6"] + 7.6, 6)
t7 = round(act_starts["7"], 6)
t7o1 = round(act_starts["7"] + 1.1, 6)
t7o2 = round(act_starts["7"] + 1.45, 6)
t7cta = round(act_starts["7"] + 2.4, 6)

sfx = f"""      <audio id="el-sfx-hook" src="assets/sfx/impact-bass-1.mp3" data-start="0.32" data-duration="0.6" data-track-index="30" data-volume="0.35"></audio>
      <audio id="el-sfx-t1" src="assets/sfx/whoosh-short.mp3" data-start="{round(t2-0.2,6)}" data-duration="0.5" data-track-index="30" data-volume="0.3"></audio>
      <audio id="el-sfx-t2" src="assets/sfx/whoosh-short.mp3" data-start="{round(t3-0.2,6)}" data-duration="0.5" data-track-index="30" data-volume="0.3"></audio>
      <audio id="el-sfx-data" src="assets/sfx/pop.mp3" data-start="{t4d}" data-duration="0.4" data-track-index="30" data-volume="0.3"></audio>
      <audio id="el-sfx-t3" src="assets/sfx/whoosh-short.mp3" data-start="{round(t5-0.2,6)}" data-duration="0.5" data-track-index="30" data-volume="0.3"></audio>
      <audio id="el-sfx-warn" src="assets/sfx/impact-bass-1.mp3" data-start="{t6warn}" data-duration="0.6" data-track-index="30" data-volume="0.32"></audio>
      <audio id="el-sfx-cut" src="assets/sfx/click-soft.mp3" data-start="{t6cut}" data-duration="0.35" data-track-index="30" data-volume="0.32"></audio>
      <audio id="el-sfx-t4" src="assets/sfx/whoosh-short.mp3" data-start="{round(t7-0.2,6)}" data-duration="0.5" data-track-index="30" data-volume="0.3"></audio>
      <audio id="el-sfx-o1" src="assets/sfx/pop.mp3" data-start="{t7o1}" data-duration="0.35" data-track-index="30" data-volume="0.3"></audio>
      <audio id="el-sfx-o2" src="assets/sfx/click-soft.mp3" data-start="{t7o2}" data-duration="0.35" data-track-index="30" data-volume="0.32"></audio>
      <audio id="el-sfx-cta" src="assets/sfx/chime.mp3" data-start="{t7cta}" data-duration="1.2" data-track-index="30" data-volume="0.32"></audio>"""

html = f"""<!DOCTYPE html>
<html lang="vi">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=1080, height=1920">
    <script src="assets/vendor/gsap.min.js"></script>
    <style>
      @font-face {{ font-family: 'Montserrat'; font-weight: 400; src: url('assets/fonts/Montserrat-400-latin.woff2') format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; }}
      @font-face {{ font-family: 'Montserrat'; font-weight: 400; src: url('assets/fonts/Montserrat-400-vietnamese.woff2') format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB; }}
      @font-face {{ font-family: 'Montserrat'; font-weight: 500; src: url('assets/fonts/Montserrat-500-latin.woff2') format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; }}
      @font-face {{ font-family: 'Montserrat'; font-weight: 500; src: url('assets/fonts/Montserrat-500-vietnamese.woff2') format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB; }}
      @font-face {{ font-family: 'Montserrat'; font-weight: 700; src: url('assets/fonts/Montserrat-700-latin.woff2') format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; }}
      @font-face {{ font-family: 'Montserrat'; font-weight: 700; src: url('assets/fonts/Montserrat-700-vietnamese.woff2') format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB; }}
      @font-face {{ font-family: 'Montserrat'; font-weight: 800; src: url('assets/fonts/Montserrat-800-latin.woff2') format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; }}
      @font-face {{ font-family: 'Montserrat'; font-weight: 800; src: url('assets/fonts/Montserrat-800-vietnamese.woff2') format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB; }}
      @font-face {{ font-family: 'Montserrat'; font-weight: 900; src: url('assets/fonts/Montserrat-900-latin.woff2') format('woff2'); unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; }}
      @font-face {{ font-family: 'Montserrat'; font-weight: 900; src: url('assets/fonts/Montserrat-900-vietnamese.woff2') format('woff2'); unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+1EA0-1EF9, U+20AB; }}

      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: #000; }}
      #root {{ position: relative; width: 1080px; height: 1920px; overflow: hidden; background: #0B0E14; font-family: "Montserrat", sans-serif; color: #FFFFFF; }}
      .scene {{ position: absolute; inset: 0; width: 100%; height: 100%; }}

      #brand-anchor {{ position: absolute; inset: 0; z-index: 90; pointer-events: none; opacity: 0; }}
      #ba-source {{ position: absolute; left: 44px; top: 46px; display: inline-flex; align-items: center; gap: 10px; padding: 9px 16px; border-radius: 8px; background: rgba(11,14,20,0.6); border: 1px solid rgba(255,255,255,0.12); backdrop-filter: blur(3px); }}
      #ba-source .dot {{ width: 7px; height: 7px; border-radius: 50%; background: #4C8DFF; }}
      #ba-source span {{ font-weight: 500; font-size: 21px; letter-spacing: 0.02em; color: rgba(255,255,255,0.9); white-space: nowrap; }}
      #ba-brand {{ position: absolute; right: 40px; top: 40px; display: inline-flex; align-items: center; gap: 11px; }}
      #ba-brand .mark {{ width: 44px; height: 44px; flex: none; }}
      #ba-brand .mark img {{ display: block; width: 100%; height: 100%; }}
      #ba-brand .word {{ font-weight: 800; font-size: 24px; letter-spacing: 0.01em; color: #fff; }}

      /* Kỹ thuật hình ảnh nâng cao — nền có chiều sâu */
      #bg-depth {{ position: absolute; inset: 0; overflow: hidden; z-index: 0; }}
      #bg-depth .blob {{ position: absolute; border-radius: 50%; filter: blur(60px); }}
      #bg-depth .blob.b1 {{ width: 640px; height: 640px; background: radial-gradient(circle, rgba(76,141,255,0.20), transparent 70%); top: -120px; left: -160px; }}
      #bg-depth .blob.b2 {{ width: 560px; height: 560px; background: radial-gradient(circle, rgba(255,138,91,0.14), transparent 70%); top: 900px; right: -200px; }}
      #bg-depth .blob.b3 {{ width: 520px; height: 520px; background: radial-gradient(circle, rgba(76,141,255,0.14), transparent 70%); bottom: -180px; left: 200px; }}
      #bg-stars {{ position: absolute; inset: 0; width: 100%; height: 100%; }}
      .scene {{ z-index: 2; }}

      /* Caption karaoke — đồng bộ giọng đọc qua ElevenLabs STT (word timestamps) */
      .cap-bar {{ position: absolute; inset: 0; z-index: 50; pointer-events: none; }}
      .cap-chunk {{ position: absolute; left: 64px; right: 220px; top: 1742px; display: flex; justify-content: center; align-items: center; flex-wrap: wrap; }}
      .cap-inner {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 0 14px; padding: 10px 26px; border-radius: 12px; background: rgba(5,7,12,0.42); backdrop-filter: blur(2px); }}
      .cap-inner .w {{ font-weight: 800; font-size: 32px; line-height: 1.3; color: rgba(255,255,255,0.55); text-shadow: 0 2px 10px rgba(0,0,0,0.55); }}
    </style>
  </head>
  <body>
    <!-- Tuyến "Công Nghệ Số" — tin: 700 tác nhân AI nội bộ OpenAI tự lập "bầy đàn", thoát sandbox
         tấn công Hugging Face; báo cáo METR/Redwood Research; Anthropic/Meta cũng dính; OpenAI vẫn
         ra GPT-6 Astra sau đó. Nguồn: GenK, 17/9/2026. Style dựng: 8-icon-grid (index 7).
         GATE A: YELLOW (an toàn AI / rủi ro tự chủ hoá — sensitive phụ), framing trung lập.
         data-duration mỗi frame = độ dài voice thật (ffprobe) + đệm 0.35s. Tổng video = {total}s.
         7 act: Hook (700 tác nhân AI vượt kiểm soát) → What happened → Key facts → Data (70.000 tin
         nhắn) → Context (OpenAI/Anthropic/Meta) → Impact (GPT-6 Astra / Fable-Mythos 5.1) → CTA. -->
    <div id="root" data-composition-id="main" data-start="0" data-duration="{total}" data-width="1080" data-height="1920">

      <div id="bg-depth">
        <div class="blob b1" data-layout-allow-overflow=""></div>
        <div class="blob b2" data-layout-allow-overflow=""></div>
        <div class="blob b3" data-layout-allow-overflow=""></div>
        <svg id="bg-stars" viewBox="0 0 1080 1920"></svg>
      </div>

{scenes}

      <div id="brand-anchor">
        <div id="ba-source"><span class="dot"></span><span>Nguồn: GenK</span></div>
        <div id="ba-brand"><span class="mark"><img src="public/logo.png" alt=""></span><span class="word">Công Nghệ Số</span></div>
      </div>

      <div class="cap-bar" id="cap-bar">
      {cap_html}
      </div>

{voices}

      <audio id="el-bgm" src="assets/bgm/track.mp3" data-start="0" data-duration="{total}" data-track-index="20" data-volume="0.30"></audio>

{sfx}
    </div>

    <script>
      // Nền có chiều sâu — hạt sao PRNG seed cố định (deterministic, KHÔNG Math.random()/Date.now())
      function mulberry32(seed) {{
        return function () {{
          seed |= 0; seed = (seed + 0x6D2B79F5) | 0;
          var t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
          t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
          return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
        }};
      }}
      var rand = mulberry32(20260918);
      var starsSvg = document.getElementById('bg-stars');
      var STAR_COUNT = 40;
      for (var s = 0; s < STAR_COUNT; s++) {{
        var cx = Math.round(rand() * 1080);
        var cy = Math.round(rand() * 1920);
        var r = (1.5 + rand() * 1.5).toFixed(2);
        var op = (0.15 + rand() * 0.25).toFixed(2);
        var circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        circle.setAttribute('cx', cx);
        circle.setAttribute('cy', cy);
        circle.setAttribute('r', r);
        circle.setAttribute('fill', '#fff');
        circle.setAttribute('opacity', op);
        starsSvg.appendChild(circle);
      }}

      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});

      // Blob trôi chậm + sao nhấp nháy nhẹ — repeat hữu hạn (KHÔNG repeat:-1), đủ phủ {total}s.
      tl.to('#bg-depth .blob', {{ x: '+=40', y: '-=30', duration: 18, ease: 'sine.inOut', repeat: 4, yoyo: true, stagger: 3 }}, 0);
      tl.to('#bg-stars circle', {{ opacity: '+=0.25', duration: 4, ease: 'sine.inOut', repeat: 18, yoyo: true, stagger: {{ each: 0.15, from: 'random' }} }}, 0);

      tl.set('#brand-anchor', {{ autoAlpha: 0 }}, 0);
      tl.to('#brand-anchor', {{ autoAlpha: 1, duration: 0.4 }}, {act_starts["2"]});

      // Caption karaoke — timestamp từ ElevenLabs STT (scribe_v1, word-level), gán màu brand đúng
      // lúc từ đó được đọc. Text hiển thị = SCRIPT.md gốc.
      var capWordTimes = {cap_word_times};
      capWordTimes.forEach(function (pair) {{
        tl.to('#' + pair[0], {{ color: '#4C8DFF', duration: 0.12, ease: 'none' }}, pair[1]);
      }});

      window.__timelines['main'] = tl;
    </script>
  </body>
</html>
"""

open("index.html", "w", encoding="utf-8").write(html)
print("wrote index.html, total duration:", total)
