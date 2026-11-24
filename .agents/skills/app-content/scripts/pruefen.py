#!/usr/bin/env python3
"""Skriptprüfung der Seiten (konventionen.md, Abschnitt 7). Aufruf im App-Ordner:
python3 .agents/skills/app-content/scripts/pruefen.py [--map /pfad/englisch.json]
Prüft je Seite:
1. Kein Hörsatz (audio in language-task und speaking-task) steht wörtlich oder fast wörtlich (Ähnlichkeit >= 0,8)
   in einem anderen Text derselben Seite oder in einer anderen Hörübung der Seite.
2. Jede Audiodatei ist in audio-texte.json, jeder Eintrag hat eine Datei und wird benutzt; der Satz der Datei
   stimmt mit dem Text der Übung überein.
3. Englische Wörter der Hörsätze und Antworten stehen im Grundwortschatz (A1/A2, aus der Karte), sonst Meldung.
Beendet mit Exit-Code 1, wenn eine Meldung der Gruppen 1 und 2 vorliegt (Gruppe 3 ist eine Liste zum Prüfen)."""
import difflib, glob, json, os, re, sys, urllib.request
import yaml

ROOT = os.getcwd()
MAPURL = "https://lernapps.net/apps/map/englisch.json"
IRREG = {"children", "made", "wrote", "bought", "is", "are", "am", "has", "does", "did", "was", "were", "aren't", "isn't", "doesn't", "don't", "didn't", "can't", "i'm", "you're", "it's", "they're", "we're", "he's", "she's", "that's", "what's", "where's", "who's"}
NAMES = {"sophie", "ellie", "peter", "amir", "hill", "parker", "mr", "mrs", "millbrook"}


def norm(s):
    return re.sub(r"[^a-z' ]+", " ", s.lower().replace("’", "'")).split()


def strings(o, skip_keys=("audio", "id", "image", "source", "licence", "url", "type", "answer")):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for k, v in o.items():
            if k in skip_keys:
                continue
            yield from strings(v, skip_keys)
    elif isinstance(o, list):
        for v in o:
            yield from strings(v, skip_keys)


def audio_items(o, out):
    if isinstance(o, dict):
        if "audio" in o and isinstance(o["audio"], str):
            out.append(o)
        for v in o.values():
            audio_items(v, out)
    elif isinstance(o, list):
        for v in o:
            audio_items(v, out)


def sentence_parts(s):
    return [p for p in re.split(r"(?<=[.!?])\s+|\n", re.sub(r"[*_`]", "", s)) if p.strip()]


def similar(a, b):
    na, nb = norm(a), norm(b)
    if not na or not nb:
        return 0
    return difflib.SequenceMatcher(None, na, nb).ratio()


def load_words():
    path = None
    if "--map" in sys.argv:
        path = sys.argv[sys.argv.index("--map") + 1]
    try:
        data = json.load(open(path)) if path else json.load(urllib.request.urlopen(MAPURL, timeout=30))
    except Exception as ex:  # noqa: BLE001
        print("Hinweis: Grundwortschatz nicht geladen:", ex)
        return None
    return {w["word"].lower() for w in data["vocabulary"]["words"]}


def known(w, W):
    if w in W or w in NAMES or w in IRREG:
        return True
    for suf, rep in (("s", ""), ("es", ""), ("ies", "y"), ("ed", ""), ("ed", "e"), ("ing", ""), ("ing", "e"), ("ied", "y"), ("n't", ""), ("'s", ""), ("'re", ""), ("'m", ""), ("er", ""), ("est", "")):
        if w.endswith(suf) and (w[: -len(suf)] + rep) in W:
            return True
    if len(w) > 2 and w[-1] == w[-2] and w[:-1] in W:
        return True
    for suf in ("ing", "ed"):
        if w.endswith(suf) and len(w) > len(suf) + 2 and w[-len(suf) - 1] == w[-len(suf) - 2] and w[: -len(suf) - 1] in W:
            return True
    return False


def main():
    texts = json.load(open(os.path.join(ROOT, ".agents/skills/app-content/scripts/audio-texte.json")))
    by_file = {os.path.basename(k): v for k, v in texts.items()}
    used = set()
    errors = []
    outside = {}
    W = load_words()
    for page in sorted(glob.glob(os.path.join(ROOT, "src", "*", "*.yaml"))):
        if page.endswith("chapter.yaml"):
            continue
        rel = os.path.relpath(page, os.path.join(ROOT, "src"))
        doc = yaml.safe_load(open(page))
        items = []
        audio_items(doc.get("blocks", []), items)
        hear = []
        for it in items:
            f = it["audio"]
            used.add(f)
            if f not in by_file:
                errors.append(f"{rel}: {f} steht nicht in audio-texte.json")
                continue
            if not os.path.exists(os.path.join(ROOT, "src", "audio", f)):
                errors.append(f"{rel}: Datei src/audio/{f} fehlt")
            spoken = by_file[f]
            expect = it.get("text") or re.sub(r"\(([^|)]*)\|[^)]*\)", r"\1", it.get("target", spoken))
            if norm(expect) != norm(spoken):
                errors.append(f"{rel}: {f}: Satz der Datei ({spoken!r}) und Text der Übung ({expect!r}) unterscheiden sich")
            hear.append((f, spoken))
        # Dubletten: Hörsatz gegen alle anderen Texte der Seite und gegen andere Hörsätze
        others = []
        for s in strings(doc.get("blocks", [])):
            others.extend(sentence_parts(s))
        for f, sp in hear:
            n_same = 0
            for o in others:
                r = similar(sp, o)
                if r >= 0.8:
                    n_same += 1
                    if n_same > 1:  # ein Treffer ist der Hörsatz selbst (target oder text)
                        errors.append(f"{rel}: Hörsatz {sp!r} kommt in einem anderen Text der Seite vor: {o!r} ({r:.2f})")
            for g, sp2 in hear:
                if g != f and similar(sp, sp2) >= 0.8:
                    errors.append(f"{rel}: Hörsätze {f} und {g} sind fast gleich")
        if W:
            for f, sp in hear:
                for w in norm(sp):
                    if not known(w.strip("'"), W):
                        outside.setdefault(rel, set()).add(w)
    for k in texts:
        if os.path.basename(k) not in used:
            errors.append(f"audio-texte.json: {k} wird in keiner Seite benutzt")
    for e in errors:
        print("FEHLER", e)
    for rel, ws in sorted(outside.items()):
        print(f"WÖRTER außerhalb von A1/A2 in Hörsätzen von {rel}: {', '.join(sorted(ws))}")
    print("ok" if not errors else f"{len(errors)} Meldungen")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
