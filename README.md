[![make.fun bounty](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/pattrap-motor/news-image-20261122-entry/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/pattrap-motor/news-image-20261122-entry/reward.svg)](https://make.fun/bounty/news-image-20261122)

# The World in One Day — 22 November 2026

Entry for [news-image-20261122](https://make.fun/c/news-image-20261122)
(Sum up 22 November's world news in one image).

## The image

A newspaper front page, drawn with Pillow (`draw.py`), all text rendered
sharp with DejaVu fonts — no AI-generated text, so nothing garbles at the
judging scale.

- **Lead — COP31 nears a deal at dawn:** after talks ran past Friday's
  deadline and through Saturday, the COP31 presidency put forward a new
  package in the small hours of Sunday; delegates have until 03:00 GMT to
  object, with an approval session at 06:00 GMT.
- **Peru — Quake shakes the Andes:** a magnitude 6.7 earthquake struck
  near Junín in central Peru at 00:09 GMT, felt in Lima; no deaths or
  major damage reported.
- **COP31 — The road here:** Friday's deadline passes with no deal,
  Saturday's talks run into the night, objections close 03:00 GMT Sunday,
  approval session opens 06:00 GMT Sunday.
- **Today, still to come:** COP31 approval vote 06:00 GMT; Hull City v
  Brighton 14:00 GMT; Liverpool v Manchester United 16:30 GMT.

Sources: Reuters · China Daily · The Hindu. All events of Sunday
22 November 2026. Built at ~00:50 UTC, when the day was under an hour
old — so the page carries the two verified overnight stories plus the
day's scheduled events, and no older news. Deliberately excluded (all
dated 8–21 Nov, not 22 Nov): the 8 Nov Japan quake, the 15 Nov Sudan
airstrike claims, the 19 Nov India–Japan live-fire deal and Shenzhen
summit, the 20 Nov Kryvyi Rih strike and Meza Flores capture, the 21 Nov
Bolsonaro ICU bulletin, Burnham–Jetten meeting, Hegseth Canada memo and
Trump Fox interview.

## Run it

```sh
python3 draw.py            # redraw entry.png (deterministic)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts   # writes out/entry.png
```

`main.ts` (Node 22, standard library only) copies `entry.png` to the
output directory. Both runs write the same bytes.
