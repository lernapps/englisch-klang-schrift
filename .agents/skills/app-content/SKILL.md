---
name: app-content
description: Use for any content work in this app - researching, writing, extending, correcting or reviewing its competencies, chapters, pages, rounds, questions, exercises, figures, terms or sources. This app's own content decisions; they take precedence over the generic lernapps content skills. Load it before you change any content.
---

# Content guide of this app

„Klang und Schrift: Aussprache und Rechtschreibung“: Explainer (Strang-App `englisch/aussprache`, Format 2, Sprache Deutsch, englische Beispiele, britisch) über englische Laute, Lautschrift, Endungen, Kurzformen und Satzmelodie. Auftrag: Issue lernapps/apps#482 (Epic lernapps/apps#489, Konventionen dort). Die erste Version baut nur Stufe 5-6 (Kapitel 1 bis 3, 9 Bausteine, 11 Seiten). Die Kapitel 4 „Richtig schreiben“ (`laut-buchstabe`, `kommasetzung`) und 5 „Betonung, Rhythmus und Melodie“ (`wortbetonung`, `bindungen`, `schwache-formen`, `satzbetonung`, `intonation-question-tags`, `intonation-haltung`) sind Stufe 7-8 bis 9-10 und kommen als Inkremente `increment/<NN>-<name>`.

## Curriculum

Englisch als erste Fremdsprache, Klasse 5-6 (erstes und zweites Lernjahr, Stufe 5-6 der Karte). Kein Lehrplan: Reihenfolge und Bausteine kommen aus der Lernlandkarte `https://lernapps.net/apps/map/englisch.json` (Fokus `competency`; Strang-App des Strangs `aussprache`). Vorwissen von außen: Zeiten (#472: `to-be`, `simple-past`, `present-progressive`), Dinge und Mengen (#475: `plural`), Sätze bauen (#473: `simple-present-fragen`, `fragewoerter`), und die kleine Lesehilfe aus Hello, Millbrook! (#470: gud-BAI, aim, fenk ju). Nicht hier: Betonung, Bindungen, schwache Formen (Kapitel 5), amerikanisches Englisch (#484), die Formen mit -s und -ed selbst (#472, #475), Großschreibung (#470), Kommas (Kapitel 4).

## Competencies

Alle neun sind Lücken der Karte, Band 5-6. Eine Seite je Baustein, Ordnung nach `requires`. Von außen braucht die Karte `plural`, `simple-past`, `present-progressive`, `to-be`, `simple-present-fragen`, `fragewoerter`: sie stehen als Sammel-Wiederholung (`recap`) am Anfang der Kapitel 2 und 3. Die „Ich kann“-Sätze stehen in der Seite wie in der Karte (nicht umformulieren). `competencies:` einer Seite sind Karten-Ids; Wiederholungsseiten haben keine.

1. Kapitel `klaenge` („Englische Laute und Lautschrift“)
   - `lautschrift` → `klaenge/lautschrift` (Musterseite)
   - `vokale` → `klaenge/vokale`
   - `konsonanten-th-w` → `klaenge/konsonanten-th-w`
   - `stimmhafte-auslaute` → `klaenge/stimmhafte-auslaute`
   - `silent-letters` → `klaenge/silent-letters` (zuletzt: Buchstabe und Laut sind dann geklärt)
2. Kapitel `endungen` („Endungen hören und schreiben“)
   - Wiederholung `recap: [englisch/plural, englisch/simple-past, englisch/present-progressive]` → `endungen/das-brauchst-du`
   - `endungen-s-ed` → `endungen/endungen-s-ed`
   - `rechtschreibung-endungen` → `endungen/rechtschreibung-endungen`
3. Kapitel `gespraech` („Sprechen wie im Gespräch“)
   - Wiederholung `recap: [englisch/to-be, englisch/simple-present-fragen, englisch/fragewoerter]` → `gespraech/das-brauchst-du`
   - `kurzformen` → `gespraech/kurzformen`
   - `intonation-fragen` → `gespraech/intonation-fragen`

Übungs-IDs: Präfix = Seite (`vokale-…`), Diktat `<seite>-hoeren`, Nachsprechen `<seite>-nachsprechen`.

## Content structure

- Pfad: `src/<kapitel>/chapter.yaml`, Seiten `src/<kapitel>/<seite>.yaml`.
- Jede Seite hat dieselben Abschnitts-IDs in dieser Reihenfolge: `einstieg` (Szene der Figuren, erste leichte Aufgabe, „Das kannst du danach“), `neu` (Klangpartitur, Lautkarten, Merke), `uebung` (mindestens vier Übungen, leicht → schwer), `anwenden` (`speaking-task` oder `open-task`), `weiter` (nächster Schritt an der Wand; am Kapitelende ein Rückblick). Die Wiederholungsseite hat nur Text und Tabellen.
- Länge: höchstens 350 Wörter Text, höchstens 4 Textblöcke hintereinander, Bild oder Übung in den ersten vier Blöcken, höchstens eine kurze Tabelle je Seite. Jede Seite bringt einen neuen Schritt.
- Geschichte: Mr Hill hängt neben den Zeitstrahl und die Satzleiste der Klasse die **Klangpartitur** auf und füllt eine Wand mit **Lautkarten**. Sophie, Ellie, Peter und Amir sprechen nach, hören einander und sammeln Karten. Figuren und Orte wie in #470 (nicht ändern): Sophie (blond, Zöpfe, grüne Jacke, aus Deutschland, wohnt bei den Parkers, 11 bis 12), Ellie Parker (11, roter Pferdeschwanz, rote Jacke), Peter Parker (9, kurze braune Haare, gelbe Jacke), Amir (11, schwarze Locken, Brille, blaue Jacke), Mr Hill (graue Haare, braune Jacke), Mrs Parker. Millbrook School, Schultag ab 8:45. Kein neuer Ort. Tabellen heißen „Klassenzimmer-Poster · …“ und „Schulkalender · …“ und die Lautkarten „Lautkarten · …“.
- Anrede „du“. Namen am Satzende zweisilbig (Sophie, Peter, Ellie, Amir).

## Terminology

- „Ausdruck“ (fester Ausdruck), nie „Wendung“. Fachbegriffe noun, verb, adjective, sentence, tense (aus #470); Begriffe aus #472, #473 und #475 (simple present, simple past, Zeitstrahl, Helfer, Satzleiste, Plural) wie dort.
- Begriffe dieser App, immer dieselben Wörter: **Klangpartitur** (drei Zeilen: unten Laute, Mitte Betonung, oben Melodie), **Lautkarte** (Zeichen, Beispielwort, Ton), **Lautschrift** (das Zeichensystem; die Zeichen stehen zwischen Schrägstrichen: /ʃ/), **Minimalpaar** (zwei Wörter, die sich in einem Laut unterscheiden), **stummer Buchstabe** (grau), **Lesehilfe** (die deutsche Annäherung aus Hello, Millbrook!), **Kurzform**.
- Britisches Englisch (favourite, colour, football). Englische Aufgaben enthalten kein deutsches Wort.
- Lautschrift britisch: /əʊ/ (nicht /oʊ/), /ɒ/, /ɜː/, kein r nach Vokal am Wortende. Betonungszeichen (ˈ) kommen in Kapitel 5 (Stufe 7-8) und stehen in den Kapiteln 1 bis 3 nicht.

## Exercise patterns

Aufbau leicht → schwer: zuordnen/wählen → Lücke → schreiben mit Cue → Korrektur → hören, schreiben und sprechen. Je Übung `mistakes` mit eigener Meldung und `hint`; gleichwertige Antworten mit `(a|b)`; `punctuation: ok`.

- Zeichen ↔ Beispielwort: `matching` mit verschiedenen rechten Einträgen (andere Wörter als die Tabelle darüber).
- Aussprache lesen: `single-choice` aus der Lautschrift, mindestens drei Optionen, echte Lernerfehler (lang/kurz vertauscht, th als s, w als v, k in knife mitgesprochen).
- Schreibung: `language-task` mode `gap` oder `write` mit `cue`; Typische Fehler (je eigene Meldung): stoped, cryes, makeing, playes, do’nt, its statt it’s, im statt I’m, nife.
- Sortieren nach dem letzten Laut: `matching` oder `multiple-choice`.
- Hören und Schreiben: `language-task` mit `audio` (Diktat); Sätze, deren Zusammenhang das Minimalwort festlegt, damit eine unscharfe Aufnahme nicht falsch belehrt. Nachsprechen: `speaking-task` mit einem Satz je Lautkarte (Player als „Antippen und Hören“); Selbstbewertung: die App sagt ehrlich, dass nichts beurteilt, wie jemand spricht.
- Jede Seite, die Hören übt, hat die richtige Antwort auch ohne Ton im Text überprüfbar (Zeichen ↔ Beispielwort); die Rückmeldung belehrt nie nur aufgrund einer Aufnahme.
- Keine Komponente (`prefer-built-in-block`); Ziehen von Karten wäre ein Wunsch für ein Inkrement. Keine Datendateien.
- Bekannte Eigenheiten der Vorlage: `ordering` zeigt Auswahlfelder (nicht verwenden); `accepted` einer Sprach-Aufgabe wirkt nicht (Gruppen `(a|b)`); im Modus `choice` zeigt die App `mistakes` nicht; `punctuation: hint` meldet bei richtiger Antwort „Achte auf die Satzzeichen“ (setze `punctuation: ok`).

## Figures

- **Klangpartitur** (SVG-Familie `src/images/partitur-<seite>.svg`, eigene Zeichnung, `CC-BY-4.0`, erzeugt mit `.agents/skills/app-content/scripts/make_partitur.py`; Hintergrund #f4efe2, Schrift mindestens 16 im 480er viewBox): drei Zeilen, links beschriftet: oben Melodie, Mitte Betonung, unten Laute. Laute: Karten in Blau (#2c6fd8) mit Lautschrift, darunter die Schreibung. Betonung: in den Kapiteln 1 bis 3 nur ein gestrichelter Rahmen „kommt später“. Melodie: ab Kapitel 3 Pfeil, der steigt (Rot #c0392b) oder fällt (Grün #138d75); davor gestrichelter Rahmen „kommt in Kapitel 3“. Stumme Buchstaben grau (#8a8577). In Aufgaben zeigt die Partitur nur die Legende, nie das Ergebnis.
- **Werkstatt** (`werkstatt-endungen.svg`): Wortkarte links (Grün), Handgriff in der Mitte (Gelb, dunkle Schrift: doppeln, y → ie, e fällt weg), Endung rechts (Blau).
- **Zungenbild** (`zunge-th.svg`): eigene Zeichnung der Zungenstellung bei /θ/ und /ð/.
- **Szenen** (`szene-<seite>.svg`): die Figuren als `<g id>` aus `millbrook-klassenzimmer.svg` von #470 (hello-millbrook), unverändert; keine Fotos, keine Figuren aus Büchern, Filmen oder Marken. Quelle „eigene Zeichnung“, Lizenz `CC-BY-4.0`. `alt` sagt, was die Szene zeigt, nie die Lösung; die Bildunterschrift nennt, wer wer ist.
- Jede Figur funktioniert bei 360 px (viewBox, Beschriftung innerhalb). Poster sind `table`-Blöcke.
- Gebaut: (wird mit den Seiten ergänzt.)

## Sources

Karte `https://lernapps.net/apps/map/englisch.json`; Grundwortschatz `https://lernapps.net/apps/map/englisch/grundwortschatz/` (A1/A2; Wörter der Übungen stammen daraus; andere stehen unten in „Wörter außerhalb von A1/A2“). Fakten aus Wikipedia (nur Fakten, keine Sätze, CC BY-SA), geöffnet am 2026-11-21: `https://en.wikipedia.org/wiki/Help:IPA/English` (Zeichen und Beispielwörter, britische Schreibung /əʊ/ statt /oʊ/, kein r nach Vokal in nicht-rhotischen Akzenten), `English plurals`, `Intonation (linguistics)`, `English orthography`. Nicht geprüft: Oxford- oder Cambridge-Wörterbuch (kein Zugriff), deutsche Wikipedia, Klexikon. Beispielsätze sind eigene aus dem Alltag der Figuren. Audio: KI-Stimme `bf_emma` (britisch, weiblich), mit Skill `lernapps-audio` erzeugt und als KI-generiert markiert. Material der Ersteller:in: keines.

Wörter außerhalb von A1/A2 (auf der Seite erklärt): (wird mit den Seiten ergänzt.)

## Hörliste (vor dem Veröffentlichen von einem Menschen anzuhören)

Die Stimme `bf_emma` wurde hier nicht angehört (die Entwicklung läuft ohne Ohr). Jede Datei aus `src/audio/` muss ein Mensch mit Englisch hören, besonders die Minimalpaare. Tabelle: Datei, Satz, erwartetes Minimalwort, Prüfstand (offen / gehört, in Ordnung / ändern). (wird mit den Dateien ergänzt.)

## Adding a chapter or round

1. Baustein auf der Karte wählen (Kapitel 4 und 5: siehe oben; Stufe 7-8: kein Zeichen der Lautschrift setzen, das nicht auf einer Lautkarte steht); die Voraussetzungen müssen auf früheren Seiten stehen oder eine Wiederholungsseite bekommen.
2. Seite `src/<kapitel>/<seite>.yaml` mit den Abschnitten `einstieg`, `neu`, `uebung`, `anwenden`, `weiter` anlegen, in `chapter.yaml` eintragen, Competency-ID setzen.
3. Partitur-Bild: neue Zeile in `make_partitur.py`; die mittlere Zeile füllt Kapitel 5 (große und kleine Punkte).
4. Übungen aus den Mustern oben, je mit `mistakes` und `hint`; 1 bis 2 ihrer Übungen (ohne Audio) in `selfAssessment` des Kapitels.
5. Hörtexte: Datei `src/audio/<satz>.mp3` und Eintrag in `.agents/skills/app-content/scripts/audio-texte.json` (Datei → Satz), erzeugt mit `regen_audio.py` (aus hello-millbrook, schneidet das Ausklingen ab); Sätze nicht zwischen Seiten wiederholen, Minimalwörter nie am Satzende, Namen am Satzende zweisilbig; Eintrag in die Hörliste.
6. Wörter gegen den Grundwortschatz prüfen; `npx --no -- lernapps check`; committen.

## Rules learned from mistakes

Aus #470, #472, #473 und `konventionen.md` Abschnitt 7 übernommen:
- Jede Übung fragt nur Wörter ab, die vorher auf der Seite stehen; Wörter außerhalb von A1/A2 werden auf der Seite erklärt.
- Eine Tabelle, die eine Übung beantwortet, steht nicht direkt über ihr; Einstieg, Poster, Merke und Bild nennen andere Beispiele als die Übungen.
- Diktat und Nachsprechen bringen neue Sätze: kein Hörsatz steht wörtlich oder fast wörtlich in Einstieg, Poster, Merke, Bildtext oder in einer anderen Übung derselben Seite (Skriptprüfung).
- Distraktoren nur echte Lernerfehler, jeder mit eigener Meldung; ein Einstiegs-`single-choice` hat mindestens drei Optionen.
- Mit `(a|b)` gleichwertige richtige Antworten zulassen; Kurzformen zulassen; `case: wrong` nur dort, wo die Seite Großschreibung unterrichtet.
- Audio: das Ausklingen der Stimme am Satzende abschneiden (`regen_audio.py`), Namen am Satzende zweisilbig, keine Einzelwörter, Minimalwort nie am Satzende.
- Bilder: Beschriftungen innerhalb des `viewBox`; die Bildunterschrift nennt, wer wer ist; das `alt` verrät nie die Lösung.
- Hinweise und Meldungen nennen weder „Spalte“ noch „Poster“ noch „oben“.
- Ein Begriff steht auf der Seite, bevor eine Übung ihn braucht; höchstens drei neue Begriffe je Absatz; ein Merke-Kasten hat zwei bis drei Aussagen.
- Bei `accepted` mit `?` in der Flow-Liste den Eintrag in Anführungszeichen setzen.
Aus dieser App: (wird mit den Prüfungen ergänzt.)
