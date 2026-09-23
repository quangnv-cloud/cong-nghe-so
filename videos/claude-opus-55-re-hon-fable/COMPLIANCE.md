# COMPLIANCE — claude-opus-55-re-hon-fable

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-23T02:05:00Z
platforms: [facebook_reel, youtube_shorts]

GATE A (news pick): GREEN
GATE B (content):   GREEN
GATE C (final):     PASS

decision: APPROVE
risk_level: GREEN
ai_disclosure_required: false
copyright_notes: "Hero image = official Anthropic 'Claude Opus 5.5' announcement banner, fetched via ?image= from the GenK article (og:image), used once as sourced editorial illustration with visible 'Nguồn: GenK' attribution on every frame; no watermark removed, no re-hosting of third-party video. BGM generated fresh via Google Lyria (lyria-realtime-exp, calm/ambient/instrumental recipe, negative-prompt excludes vocals) — project-owned, no external track reused. SFX from repo's shared library (chime/click-soft/impact-bass-1/pop/whoosh-short), same set used across the channel's videos. Fonts: self-hosted Montserrat (Google Fonts, OFL license) latin+vietnamese subsets, same files copied from videos/astra-openai/assets/fonts/."
claims_verified:
  - "Claude Opus 5.5 launched 22/9/2026, Anthropic calls it strongest model tested — BRIEF.md line 1"
  - "Fable 5.1 (Anthropic's other flagship) launched 'đầu tháng 9/2026' per BRIEF.md — no exact date is given in the source, so SCRIPT.md/on-screen text say only 'chỉ vài tuần sau khi' (a few weeks after), not a precise week-count; the on-screen timeline badges show only the two real dates that ARE sourced ('Đầu 9/2026' and '22/9/2026'), never a derived duration"
  - "'Opus 5.5 làm ngang Fable 5.1 ở hầu hết công việc' is Anthropic's own claim, not independently verified — both SCRIPT.md line 3 and the 03-facts.html on-screen sub-line now carry the 'theo Anthropic' attribution"
  - "Available on Claude app, API, AWS/Google Cloud/Azure — BRIEF.md (voice line omits cloud-platform list for pacing; shown as fact only in BRIEF, not fabricated in video)"
  - "~40% cheaper to run than Opus 5, ~30%+ faster than Opus 5 — BRIEF.md"
  - "API price: Opus 5.5 = $4/$20 per million tokens (in/out); Opus 5 = $5/$25; Fable 5.1 = $10/$50 — BRIEF.md"
  - "Opus 5.5 ~60% cheaper base token price than Fable 5.1 (per VentureBeat, cited in BRIEF) — BRIEF.md"
  - "Terminal-Bench 4.0: Opus 5.5 66.4% vs Fable 5.1 55.8% vs Opus 5 52.3% — BRIEF.md"
  - "Sonar independent audit, 544 coding tasks: Opus 5.5 pass rate 87.68% (~Opus 5's 88.6%), writes fewer lines/tokens, total issues found down 42%, critical security vulnerabilities down 53% — BRIEF.md"
  - "Sonar audit: overall bug density +12% (644 bugs/million LOC), concurrency-handling bugs +44% (largest bug category) — BRIEF.md"
  - "Debate framing (bước tiến / mối lo) — directly reflects BRIEF.md 'Góc tranh luận' section, not invented"
claims_not_in_video_but_in_brief: ["GDPval-AA Elo scores", "GPT-6 Astra comparison", "C-to-Rust migration example", "sensitive-request routing to Opus 4.8", "paid-tier usage-limit relief"] # left out only for runtime budget, none contradicted
sensitive_flags: []
vietnam_legal_flags: []
notes: "Two corrections made after an independent coordinator review of the first render, before this build was approved:
(1) GATE B1 fix — SCRIPT.md line 2 originally said 'chỉ ba tuần sau khi' (exactly 3 weeks), a precise figure not traceable to BRIEF.md (which only says Fable 5.1 launched 'đầu tháng 9/2026'). Changed to 'chỉ vài tuần sau khi' (voice + the matching subtitle/caption in 02-what.html) — accurate without inventing precision.
(2) GATE B1 fix — SCRIPT.md line 3 had dropped the 'Theo Anthropic,' attribution on the 'ngang Fable 5.1' capability-parity claim, which is Anthropic's own claim rather than an independently verified fact. Restored 'Theo Anthropic,' at the start of the voice line and added ', theo Anthropic' to the matching on-screen sub-line in 03-facts.html.
(3) Thumbnail/render fix — the first render's Hook scene (data-duration 6.31s) left no clean window after the last karaoke caption chunk cleared (~6.26s) before the scene cut, so a 3.0s thumbnail extraction caught a mid-sentence caption fragment ('5.5, mô hình mà hãng gọi'). Extended Hook's data-duration to 6.70s (a ~0.44s clean settled tail with logo/badge/name/tags only, no caption), cascaded the +0.39s shift through every later scene's data-start, all SFX cue times, and the BGM/total duration (67.98s → 68.13s), then re-extracted the thumbnail at t=6.5s and confirmed by reading the image: no caption text visible, logo + channel name + source badge + title + both contrast tags all sharp and uncropped.
Regenerating lines 2 and 3 also required retiming 03-facts.html's node-reveal animations and both frames' karaoke captions against fresh ElevenLabs STT word timestamps (the 'Theo Anthropic,' prefix pushes all later words ~1.5s later in that line); line 3's new audio happened to measure the same total duration as the old file (11.389388s) by mp3-frame-quantization coincidence — verified genuine (not stale/cached) by re-running STT on the new file and confirming it actually contains 'Theo Anthropic, ... rẻ hơn khoảng sáu mươi phần trăm'.
Full re-render + full 5-step verify + 4b vertical-balance re-check completed after both fixes; see session report for all details. Video final duration 68.13-68.2s (ffprobe/AAC rounding), still well under the 75s cap.
(4) Orchestrator final audio QC — independent loudnorm re-measurement of the delivered mp4 found Input Integrated -14.06 LUFS (within spec) but Input True Peak -0.93 dBTP, 0.07dB over the '≤ -1.0 dBTP' ceiling. Applied a corrective 2-pass loudnorm (video stream copied unchanged, audio re-encoded AAC 192kbps) targeting I=-14/TP=-1.5/LRA=7 with the measured stats fed in; re-measured the corrected file independently: Integrated -14.0 LUFS, True Peak -1.1 dBTP, no silence introduced, duration unchanged (68.26s). This is the file that was committed/published."
```
