import os, sys, json, urllib.request

API_KEY = os.environ["ELEVENLABS_API_KEY"]
VOICE_ID = "RCmOaM1iiIH5xX3QXjIF"
MODEL_ID = "eleven_v3"

lines = [l.strip() for l in open(sys.argv[1], encoding="utf-8") if l.strip()]
outdir = sys.argv[2]
os.makedirs(outdir, exist_ok=True)

for i, line in enumerate(lines, start=1):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    payload = {
        "text": line,
        "model_id": MODEL_ID,
        "voice_settings": {"speed": 1.09, "stability": 0.5, "similarity_boost": 0.75}
    }
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, method="POST", headers={
        "xi-api-key": API_KEY,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg"
    })
    with urllib.request.urlopen(req, timeout=120) as resp:
        audio = resp.read()
    outpath = os.path.join(outdir, f"line{i}.mp3")
    with open(outpath, "wb") as f:
        f.write(audio)
    print(f"wrote {outpath} ({len(audio)} bytes)")
