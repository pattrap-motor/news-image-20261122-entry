#!/usr/bin/env python3
"""Draw 'The World in One Day - 22 November 2026' (1024x1024, Pillow).

Original vector newspaper front page for make.fun news-image-20261122.
Deterministic: fixed geometry, no randomness, no timestamps, no network.
Run: python3 draw.py  ->  writes entry.png beside this file.
"""
import math

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (247, 241, 227)      # cream paper
INK = (26, 26, 26)
RED = (176, 30, 40)
TEAL = (13, 92, 102)
GOLD = (224, 168, 44)
GREY = (96, 96, 96)
SKY = (216, 232, 245)
SEA1 = (31, 122, 140)
SEA2 = (21, 94, 107)
SEA3 = (15, 76, 92)
NAVY = (31, 58, 95)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap by pixel width."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, max_w, leading, fill=INK):
    """Draw wrapped text; return the y after the last line."""
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def centred(draw, y, text, fnt, fill=INK):
    w = draw.textlength(text, font=fnt)
    draw.text(((W - w) / 2, y), text, font=fnt, fill=fill)


def draw_lead_art(draw):
    """COP31 illustration: sun rising over the sea at Antalya, flags of
    the negotiating nations along the horizon."""
    x0, y0, x1, y1 = 27, 155, 468, 493
    draw.rectangle([x0, y0, x1, y1], fill=SKY)
    # Sun with rays, upper right of the panel.
    cx, cy, r = 372, 232, 48
    for k in range(12):
        ang = k * math.pi / 6
        x_a = cx + int((r + 10) * math.cos(ang))
        y_a = cy + int((r + 10) * math.sin(ang))
        x_b = cx + int((r + 26) * math.cos(ang))
        y_b = cy + int((r + 26) * math.sin(ang))
        draw.line([x_a, y_a, x_b, y_b], fill=GOLD, width=4)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GOLD)
    # Layered sea: three sine-topped bands.
    for base, colour in ((392, SEA1), (424, SEA2), (456, SEA3)):
        pts = [(x0, y1)]
        for x in range(x0, x1 + 1, 8):
            pts.append((x, base + int(9 * math.sin(x / 42.0))))
        pts.append((x1, y1))
        draw.polygon(pts, fill=colour)
    # Row of small national flags on poles along the horizon.
    flag_colours = [RED, (34, 139, 34), (29, 78, 216),
                    GOLD, (107, 70, 193), (230, 126, 34)]
    for i, colour in enumerate(flag_colours):
        px = 52 + i * 56
        draw.line([px, 348, px, 392], fill=INK, width=2)
        draw.polygon([(px, 348), (px + 30, 354), (px, 362)], fill=colour)
    # Caption strip.
    draw.rectangle([x0, 463, x1, y1], fill=INK)
    draw.text((37, 470), "ANTALYA · TODAY", font=font(SANS_B, 16),
              fill=(255, 255, 255))


def draw_quake_art(draw):
    """Peru illustration: the Andes with a seismograph trace."""
    x0, y0, x1, y1 = 26, 538, 196, 774
    draw.rectangle([x0, y0, x1, y1], fill=(222, 228, 235))
    draw.polygon([(x0, y1), (108, 648), (x1, y1)], fill=NAVY)
    draw.polygon([(x0, y1), (150, 676), (x1, y1)], fill=(52, 84, 138))
    # Seismograph zigzag across the mountains.
    pts = []
    x = x0 + 4
    step = 0
    while x <= x1 - 4:
        amp = 26 if step % 7 == 3 else (10 if step % 3 == 0 else 4)
        pts.append((x, 712 + (amp if step % 2 else -amp)))
        x += 11
        step += 1
    draw.line(pts, fill=RED, width=3)
    draw.line([x0, 742, x1, 742], fill=INK, width=2)
    draw.rectangle([x0, 744, x1, y1], fill=INK)
    label = "00:09 GMT"
    w = draw.textlength(label, font=font(SANS_B, 14))
    draw.text((x0 + (x1 - x0 - w) / 2, 750), label,
              font=font(SANS_B, 14), fill=(255, 255, 255))


def draw_clock(draw, x, y, r):
    draw.ellipse([x, y, x + 2 * r, y + 2 * r], outline=INK, width=3)
    cx, cy = x + r, y + r
    draw.line([cx, cy, cx, cy - r + 6], fill=INK, width=3)
    draw.line([cx, cy, cx + r - 8, cy + 5], fill=INK, width=3)


def draw_ball(draw, x, y, r):
    draw.ellipse([x, y, x + 2 * r, y + 2 * r], outline=INK, width=2,
                 fill=(255, 255, 255))
    cx, cy = x + r, y + r
    pent = []
    for k in range(5):
        ang = -math.pi / 2 + k * 2 * math.pi / 5
        pent.append((cx + int(7 * math.cos(ang)),
                     cy + int(7 * math.sin(ang))))
    draw.polygon(pent, fill=INK)
    for px, py in pent:
        draw.line([px, py, cx + int((r - 2) * (px - cx) / 7),
                   cy + int((r - 2) * (py - cy) / 7)], fill=INK, width=1)


def draw():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # Masthead + date banner.
    centred(d, 16, "THE WORLD IN ONE DAY", font(SERIF_B, 62))
    d.rectangle([24, 94, 1000, 97], fill=INK)
    centred(d, 106, "SUNDAY · 22 NOVEMBER 2026", font(SANS_B, 29), fill=RED)
    d.rectangle([24, 142, 1000, 143], fill=INK)

    # ---- LEAD: COP31 ----
    d.rectangle([24, 152, 1000, 520], outline=INK, width=3)
    draw_lead_art(d)
    tx = 488
    d.text((tx, 172), "LEAD · CLIMATE · ANTALYA", font=font(SANS_B, 19),
           fill=RED)
    d.text((tx, 198), "COP31 NEARS", font=font(SERIF_B, 48), fill=INK)
    d.text((tx, 252), "A DEAL AT DAWN", font=font(SERIF_B, 48), fill=INK)
    y = text_block(
        d, tx, 318,
        "Talks ran past Friday's deadline and through Saturday. In the "
        "small hours of Sunday, the COP31 presidency put forward a new "
        "package — a text, it says, that all sides can agree.",
        font(SANS, 19), 488, 26)
    y = text_block(
        d, tx, y + 10,
        "Delegates have until 03:00 GMT to object. An approval session "
        "opens at 06:00 GMT.",
        font(SANS, 19), 488, 26)
    d.text((tx, 484), "Nearly 200 nations must agree as one.",
           font=font(SANS_B, 19), fill=TEAL)

    # ---- Row 2: Peru quake + COP31 timeline ----
    d.rectangle([24, 536, 500, 776], outline=INK, width=2)
    draw_quake_art(d)
    d.text((210, 552), "PERU · 00:09 GMT", font=font(SANS_B, 16), fill=RED)
    d.text((210, 576), "Quake shakes", font=font(SERIF_B, 29), fill=INK)
    d.text((210, 608), "the Andes", font=font(SERIF_B, 29), fill=INK)
    text_block(
        d, 210, 650,
        "A magnitude 6.7 earthquake struck near Junín in central Peru in "
        "the first minutes of Sunday, felt in Lima. No deaths or major "
        "damage reported.",
        font(SANS, 17), 278, 23)

    d.rectangle([524, 536, 1000, 776], outline=INK, width=2)
    d.text((544, 552), "COP31 · THE ROAD HERE", font=font(SANS_B, 16),
           fill=RED)
    d.text((544, 576), "From deadlock to a text", font=font(SERIF_B, 29),
           fill=INK)
    d.line([545, 633, 545, 737], fill=(190, 190, 190), width=2)
    rows = [
        ("FRI", "Deadline passes with no deal"),
        ("SAT", "Talks run on into the night"),
        ("SUN 03:00", "Objections to the text close"),
        ("SUN 06:00", "Approval session opens"),
    ]
    ry = 624
    for label, text in rows:
        d.ellipse([540, ry + 4, 550, ry + 14], fill=GOLD, outline=INK)
        d.text((562, ry), label, font=font(SANS_B, 17), fill=INK)
        d.text((668, ry), text, font=font(SANS, 17), fill=INK)
        ry += 34
    d.text((544, 754), "All times GMT.", font=font(SANS, 14), fill=GREY)

    # ---- Row 3: later today ----
    d.rectangle([24, 792, 1000, 944], outline=INK, width=2)
    d.text((40, 806), "TODAY · STILL TO COME", font=font(SANS_B, 17),
           fill=RED)
    d.line([350, 836, 350, 928], fill=(190, 190, 190), width=1)
    d.line([670, 836, 670, 928], fill=(190, 190, 190), width=1)
    cols = [
        (40, draw_clock, "COP31 approval vote", "06:00 GMT · Antalya"),
        (370, draw_ball, "Hull City v Brighton", "14:00 GMT · Premier League"),
        (690, draw_ball, "Liverpool v Man Utd", "16:30 GMT · Premier League"),
    ]
    for x, icon, label, sub in cols:
        icon(d, x, 842, 18)
        d.text((x + 50, 844), label, font=font(SANS_B, 18), fill=INK)
        d.text((x + 50, 872), sub, font=font(SANS, 16), fill=GREY)

    # Footer.
    centred(d, 960,
            "Sources: Reuters · China Daily · The Hindu — "
            "All events of Sunday 22 November 2026",
            font(SANS, 16), fill=GREY)
    return img


if __name__ == "__main__":
    draw().save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png")
