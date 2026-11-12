# CCTV Knowledge Guide

A starter guide to CCTV systems for an IT generalist. This is a
learning template — all sites, cameras, systems, and numbers below
are fictional. CCTV is covered here as **knowledge only**: this
guide explains what the parts of a system are and how they fit
together. It does not claim hands-on CCTV installation,
configuration, or operation experience, and it does not describe
any real site or real recording.

## The parts of a CCTV system

- **Camera** — captures video. The common types are fixed dome
  (indoor, discreet), bullet (outdoor, visible deterrent), and
  PTZ — pan, tilt, zoom — (a camera an operator can move and zoom
  remotely).
- **Recorder** — stores video and plays it back. An NVR (network
  video recorder) works with IP cameras over a network; a DVR
  (digital video recorder) works with analogue cameras over
  coaxial cable. A hybrid recorder can take both.
- **Storage** — hard drives inside or attached to the recorder.
  Size is set by how many cameras, how much detail (bitrate),
  how many hours a day are recorded, and how many days of video
  must be kept (retention).
- **Network / cabling** — carries video from camera to recorder.
  IP cameras commonly use Ethernet, often with PoE (Power over
  Ethernet), so one cable carries power and data. Older analogue
  cameras use coaxial cable with separate power.
- **Monitor / viewing** — a screen or app for live viewing and
  playback, usually in a control room or on a duty manager's
  computer.
- **Power** — cameras and the recorder need power, and a UPS
  (uninterruptible power supply) keeps the system running through
  a short power cut.

## Camera types (starter definitions)

| Type | Best for | Watch out for |
|------|----------|---------------|
| Fixed dome | Indoor areas, corridors, reception | Limited field of view; fixed aim |
| Bullet | Outdoor walls, entrances, car parks | Visible, so needs a sensible mounting height |
| PTZ | Large open areas, yards | One camera can only look one way at a time |
| Fisheye / 360 | Open rooms, lobbies | Image needs dewarping to read detail |

## NVR vs DVR (starter comparison)

| | NVR (IP cameras) | DVR (analogue cameras) |
|---|---|---|
| Camera connection | Ethernet network | Coaxial cable |
| Power | Often PoE from a switch | Separate power per camera |
| Image quality | Usually higher resolution | Limited by analogue signal |
| Adding a camera | Plug into the network | Needs a free DVR channel |
| Typical use | Newer installs | Existing older installs |

## Storage basics

Storage need grows with four things: number of cameras, bitrate
(how much data each second of video takes), hours recorded per
day, and retention days. Recording only on motion, or only during
certain hours, cuts storage a lot — but it also means there is no
video for the times nothing moved. The script in
`scripts/storage-estimate.py` shows how the numbers interact.

Rough sense of scale (starter examples, not a specification):
recording 8 cameras at 4 Mbps, 24 hours a day, for 30 days needs
roughly 10 TB before overhead. Doubling the cameras doubles the
storage; halving the hours halves it. Always check the recorder's
own calculator or the vendor's guidance for a real system.

## Placement principles (general knowledge)

- Cover entrances and exits first — they are where people pass.
- Aim cameras so faces and movement are visible, not just the
  top of heads.
- Avoid pointing a camera straight into bright light or a window;
  backlight washes the picture out.
- Keep cameras out of easy reach where tampering is a risk.
- Do not point cameras at places where people expect privacy,
  such as toilets or changing areas.
- Check the picture at night, not only in daylight — infrared
  range and glare behave differently after dark.

## Privacy and legal points to know

- Cameras record people. In many places that makes the video
  personal data, with rules on signage, who can watch it, how
  long it is kept, and who it can be shared with.
- Put up clear signs where cameras operate, and keep a simple
  record of why each camera is there.
- Limit who can view and export footage, and log who does.
- Delete recordings when the retention period ends; do not keep
  them "just in case".
- Laws and rules differ by country and by sector. Always check
  the rules that apply where a system operates — this guide is
  not legal advice.

## Upkeep checklist (what to know how to check)

- Are all cameras actually recording? A dead camera with a live
  picture is a common failure.
- Is the recorder's clock right? Wrong timestamps make playback
  useless.
- Is there free storage, or is the oldest video being overwritten
  sooner than the retention policy allows?
- Are camera lenses clean, and is night vision still working?
- Is the firmware of cameras and recorder up to date?
- Who has the admin password, and is it stored securely — never
  in a shared document or a repo?
- Is there a backup of the recorder's settings, so a failed
  recorder can be replaced without starting from scratch?

## Common mistakes (starter notes)

- Buying cameras without checking the recorder has enough
  channels and storage for them.
- Recording 24 hours a day when motion-only recording would do,
  then running out of storage.
- Forgetting the clock: recordings with the wrong time are hard
  to use.
- Putting a camera where it watches a private area by mistake.
- Keeping footage longer than the policy allows.
- Treating CCTV knowledge as CCTV experience — knowing how a
  system works is not the same as having installed or run one.

## Adding your own learning items

Add a row to `cctv-knowledge-checklist.csv` with: item, section,
status, and notes. Keep every entry fictional in samples — never
commit real site names, camera locations, IP addresses, or
credentials.

## Sample / Demo notice

All sites, cameras, systems, and numbers here are fictional
samples for learning, labelled "Sample / Demo" in the diagram.
This template does not claim any production use.
