#!/usr/bin/env python3
"""Generate karaoke caption chunk HTML + GSAP timeline JS for a script line.
Usage: python3 gen_captions.py <act_num> <duration_seconds> <text...>
Prints two blocks separated by '===JS===': HTML chunks, then JS tween lines.
Chunking: greedy groups of up to 5 words; if the final group would have <3 words
(and there is a previous group), merge it into the previous group.
"""
import sys

def chunk_words(words, size=5, min_last=3):
    chunks = []
    i = 0
    while i < len(words):
        chunks.append(words[i:i+size])
        i += size
    if len(chunks) >= 2 and len(chunks[-1]) < min_last:
        last = chunks.pop()
        chunks[-1] = chunks[-1] + last
    return chunks

def main():
    act = sys.argv[1]
    dur = float(sys.argv[2])
    text = " ".join(sys.argv[3:])
    words = text.split()
    chunks = chunk_words(words)
    total_words = len(words)
    per_word = dur / total_words

    html_lines = []
    js_lines = []
    cum_word_idx = 0
    cum_time = 0.0
    prev_chunk_start = None
    chunk_starts = []
    # First pass: compute chunk_start time (time of first word of each chunk)
    word_times = []
    t = 0.0
    for w in words:
        word_times.append(t)
        t += per_word

    idx = 0
    for ci, chunk in enumerate(chunks):
        cid = f"cap-l{act}-{ci}"
        spans = " ".join(f'<span data-hf-id="hf-cap{act}-{ci}-{wi}" class="w">{w}</span>' for wi, w in enumerate(chunk))
        html_lines.append(f'<div data-hf-id="hf-capd{act}-{ci}" class="cap-chunk" id="{cid}">{spans}</div>')
        chunk_start = max(0.05, word_times[idx] - 0.0)
        # chunk end = start of next chunk's first word, or dur if last chunk
        if ci < len(chunks) - 1:
            next_idx = idx + len(chunk)
            chunk_end = word_times[next_idx]
        else:
            chunk_end = dur
        js_lines.append(f"tl.fromTo('#{cid}', {{autoAlpha:0, y:8}}, {{autoAlpha:1, y:0, duration:0.1}}, {chunk_start:.3f});")
        js_lines.append(f"tl.to('#{cid}', {{autoAlpha:0, duration:0.1}}, {chunk_end:.3f});")
        for wi, w in enumerate(chunk):
            wt = word_times[idx + wi]
            js_lines.append(f"tl.fromTo('#{cid} .w:nth-child({wi+1})', {{color:'rgba(255,255,255,0.5)'}}, {{color:'#4C8DFF', duration:0.1, ease:'none'}}, {wt:.3f});")
        idx += len(chunk)

    print("\n      ".join(html_lines))
    print("===JS===")
    print("\n".join(js_lines))

if __name__ == "__main__":
    main()
