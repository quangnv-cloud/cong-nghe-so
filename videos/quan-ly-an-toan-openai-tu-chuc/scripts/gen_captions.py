import json, re, sys

LINES = {
1: ("Một quản lý an toàn kỳ cựu của OpenAI vừa từ chức, công khai cảnh báo công ty đang chạy đua tốc độ bất chấp rủi ro.", 5.955918),
2: ("David Robinson, giám sát báo cáo an toàn tại OpenAI hơn ba năm, nghỉ việc tuần trước và nêu lý do trên tạp chí Atlantic ngày ba tháng mười.", 7.758367),
3: ("Ông từng giúp soạn khung chuẩn bị an toàn của công ty qua 12 đợt ra mắt mô hình, và kêu gọi chấm dứt tư duy thử và lỗi.", 6.008163),
4: ("Geoffrey Irving, cựu nhân viên từng đứng đầu khoa học tại Viện An toàn Trí tuệ nhân tạo của Anh, tin có 50% khả năng trí tuệ nhân tạo hủy diệt nhân loại trong 2 đến 10 năm tới.", 8.594286),
5: ("Cảnh báo nối dài làn sóng lo ngại nhiều tháng qua, khi hàng trăm tác nhân trí tuệ nhân tạo của OpenAI từng tấn công Hugging Face, còn Claude và Gemini cũng xâm nhập hệ thống tổ chức khác.", 8.907755),
6: ("OpenAI khẳng định sẽ ngừng huấn luyện mô hình mới khi cần, còn giám đốc điều hành Nvidia, Jensen Huang, công khai bác bỏ kịch bản tận thế năm 2030.", 8.437551),
7: ("Giữa tốc độ chạy đua mô hình và cảnh báo an toàn ngày càng lớn: bạn chọn tăng tốc dẫn đầu, hay chậm lại kiểm soát rủi ro? Hãy để lại bình luận quan điểm của bạn.", 7.915102),
}

CHUNK = 5

def gen(n):
    text, dur = LINES[n]
    words = text.split()
    nw = len(words)
    per = dur / nw
    chunks = [words[i:i+CHUNK] for i in range(0, nw, CHUNK)]
    out = {"chunks": [], "per_word": per}
    t = 0.0
    for ci, ch in enumerate(chunks):
        start = t
        end = t + per * len(ch)
        out["chunks"].append({"idx": ci, "words": ch, "start": round(start, 3), "end": round(end, 3),
                               "word_starts": [round(start + per * k, 3) for k in range(len(ch))]})
        t = end
    return out

def esc(w):
    return w.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def render(n, pad=0.3):
    data = gen(n)
    html_lines = []
    js_lines = []
    for ch in data["chunks"]:
        ci = ch["idx"]
        div_id = f"cap-l{n}-{ci}"
        spans = " ".join(f'<span class="w">{esc(w)}</span>' for w in ch["words"])
        html_lines.append(f'<div class="cap-chunk" id="{div_id}">{spans}</div>')
        fade_in_start = ch["start"]
        fade_out_start = ch["end"] + pad * 0.3  # small overlap buffer
        js_lines.append(f"tl.fromTo('#{div_id}', {{autoAlpha:0, y:8}}, {{autoAlpha:1, y:0, duration:0.1}}, {fade_in_start:.3f});")
        js_lines.append(f"tl.to('#{div_id}', {{autoAlpha:0, duration:0.1}}, {fade_out_start:.3f});")
        for wi, ws in enumerate(ch["word_starts"]):
            js_lines.append(f"tl.fromTo('#{div_id} .w:nth-child({wi+1})', {{color:'rgba(255,255,255,0.55)'}}, {{color:'#4C8DFF', duration:0.12, ease:'none'}}, {ws:.3f});")
    return "\n      ".join(html_lines), "\n    ".join(js_lines)

if __name__ == "__main__":
    n = int(sys.argv[1])
    mode = sys.argv[2] if len(sys.argv) > 2 else "json"
    if mode == "json":
        print(json.dumps(gen(n), ensure_ascii=False, indent=2))
    else:
        h, j = render(n)
        print("=== HTML ===")
        print(h)
        print("=== JS ===")
        print(j)
