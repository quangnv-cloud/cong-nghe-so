import json, os, sys, time, urllib.request, urllib.error

APP_ID = os.environ["VBEE_APP_ID"]
TOKEN = os.environ["VBEE_TOKEN"]
VOICE_CODE = "hn_female_ngochuyen_full_48k-fhg"
SPEED_RATE = "1.09"
BASE = "https://vbee.vn/api/v1/tts"

def post_json(url, payload, headers):
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.loads(r.read().decode("utf-8"))

def get_json(url, headers):
    req = urllib.request.Request(url, headers=headers, method="GET")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))

def main():
    n = int(sys.argv[1])
    line_path = f"assets/voice/line{n}.json"
    with open(line_path, encoding="utf-8") as f:
        text = json.load(f)["input_text"]

    headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
    payload = {
        "app_id": APP_ID,
        "input_text": text,
        "voice_code": VOICE_CODE,
        "speed_rate": SPEED_RATE,
        "audio_type": "mp3",
        "bitrate": 128,
        "callback_url": "https://example.com/vbee-callback",
    }
    resp = post_json(BASE, payload, headers)
    if resp.get("status") != 1:
        print("SUBMIT_FAIL", json.dumps(resp, ensure_ascii=False))
        sys.exit(1)
    request_id = resp["result"]["request_id"]
    print(f"line{n} request_id={request_id}")

    status_url = f"{BASE}/{request_id}"
    for attempt in range(30):
        time.sleep(2)
        status_resp = get_json(status_url, headers)
        result = status_resp.get("result", {})
        st = result.get("status")
        if st == "SUCCESS":
            audio_link = result["audio_link"]
            out_path = f"assets/voice/line{n}.mp3"
            req = urllib.request.Request(audio_link, method="GET")
            with urllib.request.urlopen(req, timeout=60) as r, open(out_path, "wb") as out:
                out.write(r.read())
            print(f"line{n} OK -> {out_path}")
            return
        if st == "FAILURE" or status_resp.get("status") == 0:
            print("TTS_FAIL", json.dumps(status_resp, ensure_ascii=False))
            sys.exit(1)
    print("TIMEOUT waiting for TTS")
    sys.exit(1)

if __name__ == "__main__":
    main()
