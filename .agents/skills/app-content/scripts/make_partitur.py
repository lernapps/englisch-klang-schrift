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


PARTITUREN["partitur-vokale"] = (
    "Klangpartitur mit einer Zeile Laute: zwei blaue Karten, ʃɪp unter dem Wort ship und ʃiːp unter dem Wort sheep",
    [("ʃɪp", "ship", None), ("ʃiːp", "sheep", None)], "legende", "legende")
PARTITUREN["partitur-auslaute"] = (
    "Klangpartitur mit einer Zeile Laute: zwei blaue Karten, bɛd unter dem Wort bed und bɛt unter dem Wort bet",
    [("bɛd", "bed", None), ("bɛt", "bet", None)], "legende", "legende")
PARTITUREN["partitur-endungen"] = (
    "Klangpartitur mit einer Zeile Laute: zwei blaue Karten, kæts unter dem Wort cats und bæɡz unter dem Wort bags",
    [("kæts", "cats", None), ("bæɡz", "bags", None)], "legende", "legende")
PARTITUREN["partitur-melodie-frage"] = (
    "Klangpartitur mit Melodie und Lauten: über dem Satz Is it big steigt ein roter Pfeil am Ende nach oben; unten drei blaue Karten",
    [("ɪz", "Is", None), ("ɪt", "it", None), ("bɪɡ", "big?", None)], [None, None, "up"], "legende")
PARTITUREN["partitur-melodie-aussage"] = (
    "Klangpartitur mit Melodie und Lauten: über dem Satz It is big fällt ein grüner Pfeil am Ende nach unten; unten drei blaue Karten",
    [("ɪt", "It", None), ("ɪz", "is", None), ("bɪɡ", "big.", None)], [None, None, "down"], "legende")


def zunge(title):
    def panel(x0, label, sub, tip):
        p = []
        p.append(f'<path d="M{x0+10} 230 C{x0+30} 170 {x0+80} 170 {x0+tip} 135 L{x0+tip} 145 C{x0+80} 195 {x0+50} 215 {x0+10} 240 Z" fill="#e58a8a" stroke="#333" stroke-width="2"/>')
        p.append(f'<rect x="{x0+120}" y="50" width="50" height="70" rx="10" fill="#fff" stroke="#333" stroke-width="2"/>')
        p.append(f'<rect x="{x0+120}" y="150" width="50" height="70" rx="10" fill="#fff" stroke="#333" stroke-width="2"/>')
        p.append(f'<text x="{x0+155}" y="262" text-anchor="middle" {F} font-size="22" fill="{INK}">{e(label)}</text>')
        p.append(f'<text x="{x0+155}" y="290" text-anchor="middle" {F} font-size="20" fill="{GREY}">{e(sub)}</text>')
        return "\n".join("  " + l for l in p)
    body = panel(0, "th /θ/", "Zunge zwischen den Zähnen", 165) + "\n" + panel(320, "s /s/", "Zunge hinter den Zähnen", 110) + "\n"
    return svg(640, 310, title, body)



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


def umgekehrt(title, groups):
    """Vom Laut zur Schrift: je Gruppe eine blaue Laut-Karte oben und darunter grüne Karten mit den Schreibungen und je einem Beispielwort."""
    n = len(groups)
    h = 70 + 3 * 54 + 30
    body = []
    body.append(f'<text x="6" y="42" {F} font-size="22" fill="{INK}">Laute</text>')
    body.append(f'<text x="6" y="130" {F} font-size="22" fill="{INK}">Schrift</text>')
    colw = (480 - 100) / n
    lines, cards = [], []
    for gi, (ipa, spell) in enumerate(groups):
        cx = 100 + colw * gi + colw / 2
        cards.append(f'<rect x="{cx - 50:.0f}" y="14" width="100" height="48" rx="8" fill="{BLUE}"/>'
                     f'<text x="{cx:.0f}" y="46" text-anchor="middle" {F} font-size="26" fill="#fff">{e(ipa)}</text>')
        lines.append(f'<path d="M{cx:.0f} 62 L{cx:.0f} {82 + (len(spell) - 1) * 54 + 22}" stroke="{GREY}" stroke-width="2" fill="none"/>')
        for k, (letters, word) in enumerate(spell):
            y = 82 + k * 54
            cards.append(f'<rect x="{cx - 80:.0f}" y="{y}" width="160" height="44" rx="8" fill="{GREEN}"/>'
                         f'<text x="{cx:.0f}" y="{y + 29}" text-anchor="middle" {F} font-size="22" fill="#fff">{e(letters)} · {e(word)}</text>')
    body.extend(lines)
    body.extend(cards)
    return svg(480, h, title, "\n".join("  " + l for l in body) + "\n")


UMGEKEHRT = {
    "partitur-laut-buchstabe": ("Ein Laut, mehrere Schreibungen: Die blaue Karte iː hat drei grüne Karten ee (see), ea (sea) und e-e (these). Die blaue Karte aɪ hat drei grüne Karten igh (night), i-e (time) und y (my)",
                                [("iː", [("ee", "see"), ("ea", "sea"), ("e-e", "these")]), ("aɪ", [("igh", "night"), ("i-e", "time"), ("y", "my")])]),
}


def satzband(title, rows):
    """Sätze als Karten: ein Satzteil je grüne Karte; ein rotes Komma in der Lücke ist eine hörbare Pause.
    rows: Liste von (Titel, [Teile]); ein Teil ist Text oder "," für eine Pause (Komma)."""
    h = 40 + len(rows) * 96
    body = []
    for ri, (label, parts) in enumerate(rows):
        y = 12 + ri * 96
        body.append(f'<text x="8" y="{y + 18}" {F} font-size="18" fill="{GREY}">{e(label)}</text>')
        x = 8
        for part in parts:
            if part == ",":
                body.append(f'<text x="{x + 2}" y="{y + 66}" {F} font-size="40" font-weight="bold" fill="{RED}">,</text>')
                x += 22
            else:
                w = max(40, 8.5 * len(part) + 18)
                body.append(f'<rect x="{x}" y="{y + 30}" width="{w}" height="46" rx="8" fill="{GREEN}"/>'
                            f'<text x="{x + w / 2:.0f}" y="{y + 60}" text-anchor="middle" {F} font-size="18" fill="#fff">{e(part)}</text>')
                x += w + 6
    return svg(480, h, title, "\n".join("  " + l for l in body) + "\n")


SATZBAND = {
    "satzband-komma": ("Drei Sätze als Karten. Erste Reihe: Last summer, rotes Komma, we went to Wales. Zweite Reihe: My brother, rotes Komma, who lives in London, rotes Komma, is a pilot. Dritte Reihe ohne Komma: The boy who lives next door is my friend",
                       [("Einleitung, dann Komma", ["Last summer", ",", "we went to Wales"]),
                        ("Nicht notwendiger Relativsatz: zwei Kommas", ["My brother", ",", "who lives in London", ",", "is a pilot"]),
                        ("Notwendiger Relativsatz: kein Komma", ["The boy who lives next door", "is my friend"])]),
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

SZENEN["szene-vokale"] = (
    "Peter zeigt ein Foto, Mr Hill fragt nach dem Tier; Ellie schaut zu",
    {"peter": (60, 135, 0.8), "ellie": (190, 125, 0.85), "hill": (400, 125, 0.85)},
    bubble(10, 8, 190, "A sheep!", 70) + bubble(380, 8, 250, "Sheep or ship?", 430))
SZENEN["szene-konsonanten-th-w"] = (
    "Sophie sagt Sank you, Ellie wundert sich; Mr Hill zeigt auf die Klangpartitur",
    {"sophie": (60, 135, 0.8), "ellie": (190, 125, 0.85), "hill": (400, 125, 0.85)},
    bubble(10, 8, 220, "Sank you!", 70) + bubble(260, 8, 140, "Eh?", 300))
SZENEN["szene-stimmhafte-auslaute"] = (
    "Amir hält die Hand an den Hals und spricht; Peter und Mr Hill hören zu",
    {"amir": (60, 125, 0.85), "peter": (190, 135, 0.8), "hill": (400, 125, 0.85)},
    bubble(10, 8, 270, "bed . . . bet", 70))
SZENEN["szene-endungen-s-ed"] = (
    "Sophie liest ein Wort mit Endung langsam in zwei Teilen, Ellie schüttelt den Kopf; Mr Hill hört zu",
    {"sophie": (60, 135, 0.8), "ellie": (190, 125, 0.85), "hill": (400, 125, 0.85)},
    bubble(10, 8, 250, "walk-ed?", 70) + bubble(280, 8, 170, "Nope!", 320))
SZENEN["szene-intonation-fragen"] = (
    "Peter fragt Amir etwas; Amir antwortet; Ellie und Mr Hill hören zu",
    {"peter": (60, 135, 0.8), "amir": (190, 125, 0.85), "hill": (400, 125, 0.85)},
    bubble(10, 8, 230, "Is it big?", 70) + bubble(270, 8, 230, "It is big.", 330))


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, (title, cols, top, mid) in PARTITUREN.items():
        open(os.path.join(OUT, name + ".svg"), "w").write(partitur(title, cols, top, mid))
    open(os.path.join(OUT, "zunge-th.svg"), "w").write(zunge("Zwei Zeichnungen der Zunge: links liegt die Zungenspitze zwischen den oberen und unteren Zähnen (th), rechts hinter den oberen Zähnen (s)"))
    for name, (title, a, b, c) in VERSCHMELZEN.items():
        open(os.path.join(OUT, name + ".svg"), "w").write(verschmelzen(title, a, b, c))
    for name, (title, rows) in SATZBAND.items():
        open(os.path.join(OUT, name + ".svg"), "w").write(satzband(title, rows))
    for name, (title, groups) in UMGEKEHRT.items():
        open(os.path.join(OUT, name + ".svg"), "w").write(umgekehrt(title, groups))
    for name, (title, rows) in WERKSTAETTEN.items():
        open(os.path.join(OUT, name + ".svg"), "w").write(werkstatt(title, rows))
    for name, (title, figs, extra) in SZENEN.items():
        open(os.path.join(OUT, name + ".svg"), "w").write(szene(title, figs, extra))
    print("ok")
