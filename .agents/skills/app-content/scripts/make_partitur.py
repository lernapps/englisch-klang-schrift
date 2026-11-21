#!/usr/bin/env python3
"""Erzeugt die Bilder der Klangpartitur und die Szenen (src/images). Aufruf aus dem App-Ordner:
python3 .agents/skills/app-content/scripts/make_partitur.py
Ein neues Bild ist ein neuer Eintrag in PARTITUREN oder SZENEN. Figuren kommen aus figuren.svgfrag (aus #470)."""
import os, html
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "..", "..", "src", "images")
BG, BLUE, GREY, RED, GREEN, INK = "#f4efe2", "#2c6fd8", "#8a8577", "#c0392b", "#138d75", "#222"
F = 'font-family="sans-serif"'
e = html.escape

def svg(w, h, title, body, defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img">\n  <title>{e(title)}</title>\n'
            f'  {defs}\n  <rect width="{w}" height="{h}" fill="{BG}"/>\n{body}</svg>\n')

def partitur(title, cols, top="legende", mid="legende", note=None):
    """cols: Liste von (Lautschrift, Schreibung, stumm). stumm: Zeichen der Schreibung, die grau gesetzt werden (Position als Index-Liste).
    top: "legende" (gestrichelter Rahmen, kommt später) oder Liste "up"/"down"/None je Spalte.
    mid: "legende" (gestrichelter Rahmen, kommt später)."""
    h = 230
    b = []
    b.append(f'<text x="6" y="42" {F} font-size="22" fill="{GREY}">Melodie</text>')
    b.append(f'<text x="6" y="104" {F} font-size="22" fill="{GREY}">Betonung</text>')
    b.append(f'<text x="6" y="164" {F} font-size="22" fill="{INK}">Laute</text>')
    if top == "legende":
        b.append(f'<rect x="130" y="14" width="342" height="44" rx="8" fill="none" stroke="{GREY}" stroke-dasharray="6 4"/>'
                 f'<text x="301" y="42" text-anchor="middle" {F} font-size="20" fill="{GREY}">kommt später</text>')
    if mid == "legende":
        b.append(f'<rect x="130" y="78" width="342" height="34" rx="8" fill="none" stroke="{GREY}" stroke-dasharray="6 4"/>'
                 f'<text x="301" y="101" text-anchor="middle" {F} font-size="20" fill="{GREY}">kommt später</text>')
    widths = [max(76, 17 * len(c[0] or "–") + 44) for c in cols]
    gap = 10
    x = 130 + max(0, (342 - sum(widths) - gap * (len(cols) - 1)) / 2)
    xs = []
    for (ipa, text, silent), w in zip(cols, widths):
        xs.append(x + w / 2)
        if ipa is None:
            b.append(f'<rect x="{x:.0f}" y="132" width="{w}" height="48" rx="8" fill="none" stroke="{GREY}" stroke-dasharray="6 4"/>'
                     f'<text x="{x + w / 2:.0f}" y="164" text-anchor="middle" {F} font-size="26" fill="{GREY}">–</text>')
        else:
            b.append(f'<rect x="{x:.0f}" y="132" width="{w}" height="48" rx="8" fill="{BLUE}"/>'
                     f'<text x="{x + w / 2:.0f}" y="164" text-anchor="middle" {F} font-size="26" fill="#fff">{e(ipa)}</text>')
        spans = "".join(f'<tspan fill="{GREY}">{e(ch)}</tspan>' if i in (silent or []) else e(ch) for i, ch in enumerate(text))
        b.append(f'<text x="{x + w / 2:.0f}" y="208" text-anchor="middle" {F} font-size="22" fill="{INK}">{spans}</text>')
        x += w + gap
    if isinstance(top, list):
        for cx, d in zip(xs, top):
            if d == "up":
                b.append(f'<path d="M{cx-30:.0f} 50 L{cx+26:.0f} 22" stroke="{RED}" stroke-width="5" fill="none" stroke-linecap="round"/><polygon points="{cx+34:.0f},18 {cx+16:.0f},20 {cx+24:.0f},34" fill="{RED}"/>')
            elif d == "down":
                b.append(f'<path d="M{cx-30:.0f} 22 L{cx+26:.0f} 50" stroke="{GREEN}" stroke-width="5" fill="none" stroke-linecap="round"/><polygon points="{cx+34:.0f},54 {cx+16:.0f},52 {cx+24:.0f},38" fill="{GREEN}"/>')
    return svg(480, h, title, "\n".join("  " + l for l in b) + "\n")

PARTITUREN = {
    "partitur-lautschrift": ("Klangpartitur mit einer Zeile Laute: zwei blaue Karten mit Lautschrift unter den Wörtern big und book",
                             [("bɪɡ", "big", None), ("bʊk", "book", None)], "legende", "legende"),
}

PARTITUREN["partitur-silent-letters"] = (
    "Klangpartitur mit einer Zeile Laute: das Wort knee hat eine graue gestrichelte Karte für das k und blaue Karten für n und iː",
    [(None, "k", [0]), ("n", "n", None), ("iː", "ee", None)], "legende", "legende")


def verschmelzen(title, a, b, c):
    """Zwei Karten (Lautschrift, Schreibung) werden zu einer: a + b = c."""
    body = []
    body.append(f'<text x="6" y="42" {F} font-size="22" fill="{GREY}">Melodie</text>')
    body.append(f'<text x="6" y="104" {F} font-size="22" fill="{GREY}">Betonung</text>')
    body.append(f'<text x="6" y="164" {F} font-size="22" fill="{INK}">Laute</text>')
    for yy, hh in ((14, 44), (78, 34)):
        body.append(f'<rect x="130" y="{yy}" width="342" height="{hh}" rx="8" fill="none" stroke="{GREY}" stroke-dasharray="6 4"/>'
                    f'<text x="301" y="{yy + (28 if hh == 44 else 23)}" text-anchor="middle" {F} font-size="20" fill="{GREY}">kommt später</text>')
    def card(x, w, ipa, text):
        return (f'<rect x="{x}" y="132" width="{w}" height="48" rx="8" fill="{BLUE}"/>'
                f'<text x="{x + w / 2}" y="164" text-anchor="middle" {F} font-size="26" fill="#fff">{e(ipa)}</text>'
                f'<text x="{x + w / 2}" y="208" text-anchor="middle" {F} font-size="22" fill="{INK}">{e(text)}</text>')
    body.append(card(124, 82, *a))
    body.append(f'<text x="222" y="164" text-anchor="middle" {F} font-size="26" fill="{INK}">+</text>')
    body.append(card(238, 82, *b))
    body.append(f'<text x="340" y="164" text-anchor="middle" {F} font-size="26" fill="{INK}">=</text>')
    body.append(card(360, 106, *c))
    return svg(480, 230, title, "\n".join("  " + l for l in body) + "\n")


VERSCHMELZEN = {
    "partitur-kurzformen": ("Klangpartitur mit einer Zeile Laute: die Karte ʃiː für she und die Karte ɪz für is werden zu einer Karte ʃiːz für she's",
                            ("ʃiː", "she"), ("ɪz", "is"), ("ʃiːz", "she's")),
}


def werkstatt(title, rows):
    h = 48 + 56 * len(rows)
    body = [f'<text x="240" y="30" text-anchor="middle" {F} font-size="22" fill="{INK}">Werkstatt: Was passiert vor der Endung?</text>']
    for i, (word, griff, endung, ergebnis) in enumerate(rows):
        y = 48 + i * 56
        body.append(f'<rect x="6" y="{y}" width="92" height="46" rx="8" fill="{GREEN}"/><text x="52" y="{y + 31}" text-anchor="middle" {F} font-size="22" fill="#fff">{e(word)}</text>')
        body.append(f'<rect x="100" y="{y}" width="190" height="46" rx="8" fill="#e6b800"/><text x="195" y="{y + 31}" text-anchor="middle" {F} font-size="20" fill="#222">{e(griff)}</text>')
        body.append(f'<rect x="300" y="{y}" width="58" height="46" rx="8" fill="{BLUE}"/><text x="329" y="{y + 31}" text-anchor="middle" {F} font-size="22" fill="#fff">{e(endung)}</text>')
        body.append(f'<text x="368" y="{y + 31}" {F} font-size="22" fill="{INK}">= {e(ergebnis)}</text>')
    return svg(480, h, title, "\n".join("  " + l for l in body) + "\n")


WERKSTAETTEN = {
    "werkstatt-endungen": ("Die Werkstatt zeigt drei Handgriffe vor einer Endung: stop plus ed wird stopped durch Verdoppeln, cry plus s wird cries durch y zu ie, make plus ing wird making, weil das e wegfällt",
                           [("stop", "Konsonant doppeln", "ed", "stopped"), ("cry", "y wird ie", "s", "cries"), ("make", "e fällt weg", "ing", "making")]),
}


def bubble(x, y, w, text, tail):
    return (f'  <rect x="{x}" y="{y}" width="{w}" height="56" rx="14" fill="#fff" stroke="#333" stroke-width="2"/>\n'
            f'  <path d="M{tail} {y+56} l12 20 l12 -20" fill="#fff" stroke="#333" stroke-width="2"/>\n'
            f'  <rect x="{tail+2}" y="{y+52}" width="20" height="6" fill="#fff"/>\n'
            f'  <text x="{x + w/2}" y="{y+38}" text-anchor="middle" {F} font-size="27" fill="#222">{e(text)}</text>\n')

def board(x, y):
    """Die aufgehängte Klangpartitur: Rahmen mit drei Zeilen."""
    s = f'  <rect x="{x}" y="{y}" width="200" height="130" rx="8" fill="#fff" stroke="#333" stroke-width="2"/>\n'
    for i, (t, c) in enumerate([("Melodie", GREY), ("Betonung", GREY), ("Laute", BLUE)]):
        yy = y + 14 + i * 38
        s += f'  <rect x="{x+10}" y="{yy}" width="180" height="32" rx="6" fill="{c if t=="Laute" else "none"}" stroke="{GREY}" stroke-dasharray="{"0" if t=="Laute" else "5 3"}"/>\n'
        s += f'  <text x="{x+100}" y="{yy+21}" text-anchor="middle" {F} font-size="22" fill="{"#fff" if t=="Laute" else GREY}">{t}</text>\n'
    return s

def szene(title, figs, extra):
    defs = open(os.path.join(HERE, "figuren.svgfrag")).read().strip()
    body = f'  <rect y="270" width="640" height="70" fill="#c9a77a"/>\n' + extra
    for name, (x, y, sc) in figs.items():
        body += f'  <use href="#{name}" transform="translate({x},{y}) scale({sc})"/>\n'
    return svg(640, 340, title, body, defs)

SZENEN = {
    "szene-lautschrift": ("Mr Hill hängt die Klangpartitur an die Wand; Sophie liest vor, Ellie schaut verwundert",
        {"hill": (400, 125, 0.85), "sophie": (60, 135, 0.8), "ellie": (190, 125, 0.85)},
        board(405, 2) + bubble(10, 8, 130, "aim", 70) + bubble(165, 8, 130, "Aim?", 214)),
}

SZENEN["szene-silent-letters"] = (
    "Sophie liest das Wort an der Tafel mit dem k vor, Amir lacht; Mr Hill zeigt auf die Klangpartitur",
    {"sophie": (60, 135, 0.8), "amir": (190, 125, 0.85), "hill": (400, 125, 0.85)},
    board(405, 2) + bubble(10, 8, 150, "k-nee?", 70) + bubble(190, 8, 130, "Ha ha!", 230))
SZENEN["szene-rechtschreibung-endungen"] = (
    "Peter überlegt an der Tafel, wie er eine Endung an ein Wort hängt; Mr Hill und Ellie schauen zu",
    {"peter": (60, 135, 0.8), "ellie": (190, 125, 0.85), "hill": (400, 125, 0.85)},
    bubble(10, 8, 280, "plan + ed = ?", 70))
SZENEN["szene-kurzformen"] = (
    "Ellie ruft etwas und zeigt auf eine Tasche; Amir und Mr Hill hören zu",
    {"amir": (60, 125, 0.85), "ellie": (190, 125, 0.85), "hill": (400, 125, 0.85)},
    bubble(150, 8, 300, "That's my bag!", 214))


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, (title, cols, top, mid) in PARTITUREN.items():
        open(os.path.join(OUT, name + ".svg"), "w").write(partitur(title, cols, top, mid))
    for name, (title, a, b, c) in VERSCHMELZEN.items():
        open(os.path.join(OUT, name + ".svg"), "w").write(verschmelzen(title, a, b, c))
    for name, (title, rows) in WERKSTAETTEN.items():
        open(os.path.join(OUT, name + ".svg"), "w").write(werkstatt(title, rows))
    for name, (title, figs, extra) in SZENEN.items():
        open(os.path.join(OUT, name + ".svg"), "w").write(szene(title, figs, extra))
    print("ok")
