# CCTV Knowledge Guide — Starter Template

A starter learning guide to CCTV (closed-circuit television) systems
for an IT generalist: the parts of a system, the common camera and
recorder types, how storage is estimated, and what to check when
reviewing a system. It is a knowledge guide — it records what a
CCTV system is made of and how the pieces fit together. It is NOT
a record of CCTV installation or operation experience, and it does
not claim any production use. Sample content only — no real company
data, no real sites or camera locations, no invented metrics.

## What it is

- `docs/cctv-guide.md` — the guide: system parts, camera types,
  recorders (NVR/DVR), storage basics, placement principles, and
  the privacy and upkeep points to know about.
- `cctv-knowledge-checklist.csv` — a checklist in CSV form of the
  things to learn and check when reviewing a CCTV system, so you
  can track your own learning against it.
- `scripts/storage-estimate.py` — a starter Python script that
  estimates storage needs from camera count, bitrate, hours per
  day, and retention days. Labelled a starter learning template;
  it is not a production tool.

## How to use

1. Read `docs/cctv-guide.md` first — it explains the parts of a
   system and the words used in the checklist.
2. Work through `cctv-knowledge-checklist.csv` one section at a
   time, marking each item learned, reviewing, or not applicable.
3. Try the storage estimator with sample numbers to build a feel
   for how camera count, bitrate, and retention days change the
   storage needed:

```bash
python3 scripts/storage-estimate.py --cameras 8 --bitrate 4 --hours 24 --days 30
python3 scripts/storage-estimate.py --cameras 4 --bitrate 2 --hours 12 --days 14
```

4. Use the checklist to review a system you are learning about —
   note what you do not know yet and what to ask the person who
   runs the system.

## CCTV system at a glance (starter definitions)

| Part | What it does | Example |
|------|--------------|---------|
| Camera | Captures video | Fixed dome, bullet, PTZ |
| Recorder (NVR/DVR) | Stores and plays back video | Network video recorder, digital video recorder |
| Storage | Holds the recordings | Hard drive sized by retention need |
| Network / cabling | Carries video to the recorder | Ethernet (PoE), coaxial |
| Monitor / viewing | Lets someone watch live or playback | Control-room screen, app |
| Power | Keeps cameras and recorder running | PoE switch, mains + UPS |

Definitions above are starter explanations for learning, not a
standard for any real organisation or installation.

## Knowledge only — read this

CCTV is listed here as **knowledge only**. This repo documents
general knowledge about CCTV systems. It does not claim hands-on
CCTV installation, configuration, or operation experience, and it
does not describe any real site, real camera, or real recording.
Local laws on cameras, signage, retention, and access vary —
always check the rules that apply where a system operates.

## Sample / Demo notice

All sites, cameras, systems, and numbers in this repo are fictional
samples for learning. The diagram in `docs/diagram.png` is a
locally generated illustration labelled "Sample / Demo" — it is
not a screenshot of a real system, and this template does not
claim any production use.

## License

MIT — see `LICENSE`.
