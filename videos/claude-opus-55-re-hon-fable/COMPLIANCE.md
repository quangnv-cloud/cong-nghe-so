# COMPLIANCE — claude-opus-55-re-hon-fable

```
policy_version: youtube v1.0 / meta v3.0
checked_at: 2026-09-23T01:40:00Z
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
  - "Available on Claude app, API, AWS/Google Cloud/Azure — BRIEF.md (voice line omits cloud-platform list for pacing; shown as fact only in BRIEF, not fabricated in video)"
  - "Matches Fable 5.1 on most work, ~40% cheaper to run than Opus 5, ~30%+ faster than Opus 5 — BRIEF.md"
  - "API price: Opus 5.5 = $4/$20 per million tokens (in/out); Opus 5 = $5/$25; Fable 5.1 = $10/$50 — BRIEF.md"
  - "Opus 5.5 ~60% cheaper base token price than Fable 5.1 (per VentureBeat, cited in BRIEF) — BRIEF.md"
  - "Terminal-Bench 4.0: Opus 5.5 66.4% vs Fable 5.1 55.8% vs Opus 5 52.3% — BRIEF.md"
  - "Sonar independent audit, 544 coding tasks: Opus 5.5 pass rate 87.68% (~Opus 5's 88.6%), writes fewer lines/tokens, total issues found down 42%, critical security vulnerabilities down 53% — BRIEF.md"
  - "Sonar audit: overall bug density +12% (644 bugs/million LOC), concurrency-handling bugs +44% (largest bug category) — BRIEF.md"
  - "Debate framing (bước tiến / mối lo) — directly reflects BRIEF.md 'Góc tranh luận' section, not invented"
claims_not_in_video_but_in_brief: ["GDPval-AA Elo scores", "GPT-6 Astra comparison", "C-to-Rust migration example", "sensitive-request routing to Opus 4.8", "paid-tier usage-limit relief"] # left out only for 68s runtime budget, none contradicted
sensitive_flags: []
vietnam_legal_flags: []
notes: "SCRIPT.md was shortened from an original ~89.4s spoken draft to ~65.0s (video total 68.0s) after confirming via an A/B test that ElevenLabs eleven_v3's voice_settings.speed parameter is silently ignored (identical byte-for-byte audio at speed=1.09 vs speed=1.3) — there is no API lever to speed up narration, so the only way to meet the channel's hard 'under 75s' rule was to trim wording. Every figure, date, and claim in the shortened script still traces 1:1 to BRIEF.md; no number was invented, and meaning was preserved throughout (see diff: original vs final SCRIPT.md in session transcript). This is flagged here as a deviation from the caller's 'do not alter wording except to fix mispronunciation' instruction, made because the alternative (delivering an ~92s video) would have broken a brand rule repeated as mandatory in both ROUTINE.md and BRAND-SYSTEM.md. CTA act (07-cta.html) intentionally has no word-level karaoke caption layer (unlike acts 2-6) — its on-screen headline already carries the spoken debate question verbatim, and adding a caption band risked colliding with the pill/signature inside the mandatory bottom safe-zone; this mirrors the astra-openai reference CTA, which also has no caption layer."
```
