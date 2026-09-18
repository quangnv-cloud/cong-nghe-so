import json

stt = json.load(open("assets/audio/stt_raw.json", encoding="utf-8"))
act_starts = json.load(open("assets/audio/act_starts.json"))

global_word_id = 0
chunks = []  # list of {start, duration, words: [{id, text}]}
word_time_pairs = []  # [id, absolute_time]

for act in range(1, 8):
    words = [w for w in stt[str(act)]["words"] if w["type"] == "word"]
    base = act_starts[str(act)]
    cur = []
    for w in words:
        cur.append(w)
        ends_clause = w["text"].endswith((",", ";", ":", ".", "?", "!"))
        if len(cur) >= 6 or (len(cur) >= 3 and ends_clause):
            chunks.append((base, cur))
            cur = []
    if cur:
        chunks.append((base, cur))

cap_html_lines = []
for ci, (base, words) in enumerate(chunks):
    c_start = round(base + words[0]["start"], 6)
    c_end = round(base + words[-1]["end"], 6)
    c_dur = round(c_end - c_start, 6)
    spans = []
    for w in words:
        wid = f"cw{global_word_id}"
        abs_t = round(base + w["start"], 6)
        word_time_pairs.append((wid, abs_t))
        text = w["text"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        spans.append(f'<span class="w" id="{wid}">{text}</span>')
        global_word_id += 1
    inner = " ".join(spans)
    cap_html_lines.append(
        f'<div class="clip cap-chunk" data-start="{c_start}" data-duration="{c_dur}" data-track-index="40">'
        f'<div class="cap-inner">{inner}</div></div>'
    )

open("assets/audio/cap_html.txt", "w", encoding="utf-8").write("\n      ".join(cap_html_lines))

js_pairs = ",".join(f'["{wid}",{t}]' for wid, t in word_time_pairs)
open("assets/audio/cap_word_times.txt", "w", encoding="utf-8").write(f"[{js_pairs}]")

print("chunks:", len(chunks), "words:", global_word_id)
