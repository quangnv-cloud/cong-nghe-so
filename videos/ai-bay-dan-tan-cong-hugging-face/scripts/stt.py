import os, sys, json, urllib.request, uuid

API_KEY = os.environ["ELEVENLABS_API_KEY"]
outdir = sys.argv[1]

def post_stt(filepath):
    boundary = uuid.uuid4().hex
    with open(filepath, "rb") as f:
        filedata = f.read()
    parts = []
    def field(name, value):
        parts.append(f"--{boundary}\r\nContent-Disposition: form-data; name=\"{name}\"\r\n\r\n{value}\r\n".encode())
    field("model_id", "scribe_v1")
    field("timestamps_granularity", "word")
    parts.append(
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"audio.mp3\"\r\nContent-Type: audio/mpeg\r\n\r\n".encode()
        + filedata + b"\r\n"
    )
    parts.append(f"--{boundary}--\r\n".encode())
    body = b"".join(parts)
    req = urllib.request.Request(
        "https://api.elevenlabs.io/v1/speech-to-text",
        data=body, method="POST",
        headers={
            "xi-api-key": API_KEY,
            "Content-Type": f"multipart/form-data; boundary={boundary}",
        }
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode())

results = {}
for i in range(1, 8):
    p = os.path.join(outdir, f"line{i}.mp3")
    r = post_stt(p)
    results[i] = r
    print(f"line{i}: {len(r.get('words', []))} words/tokens")

json.dump(results, open(os.path.join(outdir, "stt_raw.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("done")
