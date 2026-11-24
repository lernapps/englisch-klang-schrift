---
name: app-content
description: Use for any content work in this app - researching, writing, extending, correcting or reviewing its competencies, chapters, pages, rounds, questions, exercises, figures, terms or sources. This app's own content decisions; they take precedence over the generic lernapps content skills. Load it before you change any content.
---

# Content guide of this app

„Klang und Schrift: Aussprache und Rechtschreibung“: Explainer (Strang-App `englisch/aussprache`, Format 2, Sprache Deutsch, englische Beispiele, britisch) über englische Laute, Lautschrift, Endungen, Kurzformen und Satzmelodie. Auftrag: Issue lernapps/apps#482 (Epic lernapps/apps#489, Konventionen dort). Die erste Version baut Stufe 5-6 (Kapitel 1 bis 3, 9 Bausteine, 11 Seiten, veröffentlicht). Inkrement 02 (Branch `increment/02-richtig-schreiben-betonung`) baut Stufe 7-8: Kapitel 4 „Richtig schreiben“ (`laut-buchstabe`, `kommasetzung`) und Kapitel 5 „Betonung, Rhythmus und Melodie“ (`wortbetonung`, `bindungen`, `schwache-formen`, `satzbetonung`, `intonation-question-tags`), zusammen 7 Bausteine und 11 Seiten (davon 2 Wiederholungsseiten). Noch offen (Stufe 9-10, spätere Inkremente): `intonation-haltung`, amerikanisches Englisch (#484).

## Curriculum

Englisch als erste Fremdsprache, Klasse 5-6 (erstes und zweites Lernjahr, Stufe 5-6 der Karte). Kein Lehrplan: Reihenfolge und Bausteine kommen aus der Lernlandkarte `https://lernapps.net/apps/map/englisch.json` (Fokus `competency`; Strang-App des Strangs `aussprache`). Vorwissen von außen: Zeiten (#472: `to-be`, `simple-past`, `present-progressive`), Dinge und Mengen (#475: `plural`), Sätze bauen (#473: `simple-present-fragen`, `fragewoerter`), und die kleine Lesehilfe aus Hello, Millbrook! (#470: gud-BAI, aim, fenk ju). Nicht hier: Haltung und Gefühl in der Satzmelodie (Stufe 9-10), amerikanisches Englisch (#484), die Formen mit -s und -ed selbst (#472, #475), Großschreibung (#470). Betonung, Bindungen, schwache Formen, Rhythmus und Kommas stehen seit Inkrement 02 in den Kapiteln 4 und 5.

## Competencies

Alle neun sind Lücken der Karte, Band 5-6. Eine Seite je Baustein, Ordnung nach `requires`. Von außen braucht die Karte `plural`, `simple-past`, `present-progressive` (dazu wiederholt Kapitel 2 `simple-present` wegen -s), `to-be`, `simple-present-fragen`, `fragewoerter`: sie stehen als Sammel-Wiederholung (`recap`) am Anfang der Kapitel 2 und 3. Die „Ich kann“-Sätze der Karte stehen auf den Wiederholungsseiten wörtlich; die Fachseiten nennen ihr Ziel unter „Das kannst du danach“ (aus dem „Ich kann“-Satz abgeleitet, nur was die App prüft). `competencies:` einer Seite sind Karten-Ids; Wiederholungsseiten haben keine.

1. Kapitel `klaenge` („Englische Laute und Lautschrift“)
   - `lautschrift` → `klaenge/lautschrift` (Musterseite)
   - `vokale` → `klaenge/vokale`
   - `konsonanten-th-w` → `klaenge/konsonanten-th-w`
   - `stimmhafte-auslaute` → `klaenge/stimmhafte-auslaute`
   - `silent-letters` → `klaenge/silent-letters` (zuletzt: Buchstabe und Laut sind dann geklärt)
2. Kapitel `endungen` („Endungen hören und schreiben“)
   - Wiederholung `recap: [englisch/plural, englisch/simple-past, englisch/present-progressive, englisch/simple-present]` → `endungen/das-brauchst-du`
   - `endungen-s-ed` → `endungen/endungen-s-ed`
   - `rechtschreibung-endungen` → `endungen/rechtschreibung-endungen`
3. Kapitel `gespraech` („Sprechen wie im Gespräch“)
   - Wiederholung `recap: [englisch/to-be, englisch/simple-present-fragen, englisch/fragewoerter]` → `gespraech/das-brauchst-du`
   - `kurzformen` → `gespraech/kurzformen`
   - `intonation-fragen` → `gespraech/intonation-fragen`
4. Kapitel `richtig-schreiben` („Richtig schreiben“, Stufe 7-8, Inkrement 02)
   - `laut-buchstabe` → `richtig-schreiben/laut-buchstabe` (Musterseite der Stufe; Chat Sophie–Ellie; /iː/ ee, ea, e-e und /aɪ/ igh, i-e, y; Homophone week/weak)
   - Wiederholung `recap: englisch/relativsaetze-nicht-notwendig` → `richtig-schreiben/das-brauchst-du`
   - `kommasetzung` → `richtig-schreiben/kommasetzung` (Blog; Komma nach Einleitung, um nicht notwendige Relativsätze, in Aufzählungen ohne Komma vor and)
5. Kapitel `betonung-rhythmus-melodie` („Betonung, Rhythmus und Melodie“, Stufe 7-8, Inkrement 02)
   - `wortbetonung` (Chat Sophie–Amir; present/record Nomen und Verb; Punkte in der mittleren Zeile; ˈ in der Lautschrift)
   - `bindungen` (Dialog Peter–Sophie; Konsonant plus Vokal, linking r)
   - `schwache-formen` (Dialog beim Backen; Schwa; Tabelle „Klassenzimmer-Poster · Starke und schwache Formen“)
   - `satzbetonung` (Sprachnachricht; starke und schwache Wörter, Rhythmus)
   - Wiederholung `recap: englisch/question-tags` → `betonung-rhythmus-melodie/das-brauchst-du`
   - `intonation-question-tags` (Chat Sophie–Ellie; Pfeil steigt = wirklich fragen, fällt = Zustimmung erwartet; **keine Aufnahme**, weil `bf_emma` die Melodie nicht hören lässt; die Seite sagt das offen)

Übungs-IDs: Präfix = Seite (`vokale-…`), Diktat `<seite>-hoeren`, Nachsprechen `<seite>-nachsprechen`.

## Content structure

- Pfad: `src/<kapitel>/chapter.yaml`, Seiten `src/<kapitel>/<seite>.yaml`.
- Jede Seite hat dieselben Abschnitts-IDs in dieser Reihenfolge: `einstieg` (Szene der Figuren, erste leichte Aufgabe, „Das kannst du danach“), `neu` (Klangpartitur, Lautkarten, Merke), `uebung` (mindestens vier Übungen, leicht → schwer), `anwenden` (`speaking-task` oder `open-task`), `weiter` (nächster Schritt an der Wand; am Kapitelende ein Rückblick). Die Wiederholungsseite hat nur Text und Tabellen.
- Länge: höchstens 350 Wörter Text, höchstens 4 Textblöcke hintereinander, Bild oder Übung in den ersten vier Blöcken, höchstens eine kurze Tabelle je Seite. Jede Seite bringt einen neuen Schritt.
- Geschichte: Mr Hill hängt neben den Zeitstrahl und die Satzleiste der Klasse die **Klangpartitur** auf und füllt eine Wand mit **Lautkarten**. Sophie, Ellie, Peter und Amir sprechen nach, hören einander und sammeln Karten. Figuren und Orte wie in #470 (nicht ändern): Sophie (blond, Zöpfe, grüne Jacke, aus Deutschland, wohnt bei den Parkers, 11 bis 12), Ellie Parker (11, roter Pferdeschwanz, rote Jacke), Peter Parker (9, kurze braune Haare, gelbe Jacke), Amir (11, schwarze Locken, Brille, blaue Jacke), Mr Hill (graue Haare, braune Jacke), Mrs Parker. Millbrook School, Schultag ab 8:45. Kein neuer Ort. Tabellen heißen „Klassenzimmer-Poster · …“ und „Schulkalender · …“ und die Lautkarten „Lautkarten · …“.
- Anrede „du“. Hörsätze bleiben natürlich: kein Name nur wegen des Klangs am Satzende; endet ein Satz auf ein einsilbiges Wort, kommt er in die Hörliste.

### Inkrement 02: Stufe 7-8 (Kapitel 4 und 5)

- Neue Seitenform: `einstieg` (Vorwissen-Frage mit mindestens drei Optionen, „Das kannst du danach“) → `lesestueck` → `neu` → `uebung` → `anwenden` → `weiter`. Das **Lesestück** (120 bis 200 Wörter, Chat, Blog oder Dialog der Figuren, Sophie 13 bis 14; zählt nicht zu den 350 Wörtern Erklärtext) steht in `text`-Blöcken (eine Zeile je Nachricht, Absender fett, höchstens drei Blöcke), davor der Block `vocabulary` „Am Rand · Wörter aus dem …“ (Randglossar; die einzige Tabelle einer Seite bleibt eine Datentabelle) und zwei Aufgaben: Verstehen (`single-choice`) und Belegen (`single-choice` mit Zeilen des Lesestücks als Optionen). Die Übungen fragen nicht dieselben Wörter und Sätze wie das Lesestück. Die dritte Stufe ist die Anwendung in `uebung` und `anwenden` (`open-task` mit Meinung oder eigenem Text). Das Lesestück wird nur gelesen, nicht vorgelesen; Hören über Sätze der Übungen.
- Kapitel 4 `richtig-schreiben` („Richtig schreiben“): `laut-buchstabe` (Musterseite der Stufe), Wiederholung `das-brauchst-du` (`relativsaetze-nicht-notwendig`, #481), `kommasetzung`. Kapitel 5 `betonung-rhythmus-melodie`: `wortbetonung`, `bindungen`, `schwache-formen`, `satzbetonung`, Wiederholung `das-brauchst-du` (`question-tags`, #473), `intonation-question-tags`.
- Kapitel 5 nutzt die mittlere Zeile der Klangpartitur: großer roter Punkt = betonte Silbe oder starkes Wort, kleiner dunkler Punkt = unbetont (`mid` als Liste „big“/„small“/None in `partitur()`); ein roter Bogen unter den Karten zeigt eine Bindung (`bogen`); `compact=True` für Bilder mit vier oder mehr Karten. Die obere Zeile (Pfeil) erscheint wieder auf `intonation-question-tags`.
- Bild `partitur-<seite>` mit `umgekehrt()` (Kapitel 4, vom Laut zur Schrift): blaue Laut-Karte oben, grüne Karten mit Schreibung und Beispielwort darunter; die Beispielwörter stehen nicht in den Übungen.

## Terminology

- „Ausdruck“ (fester Ausdruck), nie „Wendung“. Fachbegriffe noun, verb, adjective, sentence, tense (aus #470); Begriffe aus #472, #473 und #475 (simple present, simple past, Zeitstrahl, Helfer, Satzleiste, Plural) wie dort.
- Kapitel 5: **Silbe** (Sprechtakt), **betont/unbetont** (großer/kleiner Punkt), **Betonung** (nicht „Akzent“), **Schwa** (/ə/), **starke und schwache Form**, **Bindung** (ein Laut rutscht zum nächsten Wort), **linking r**, **Rhythmus**, **question tag** („Tag“), **Pfeil** (Melodie).
- Begriffe dieser App, immer dieselben Wörter: **Klangpartitur** (drei Zeilen: unten Laute, Mitte Betonung, oben Melodie), **Lautkarte** (eine Zeile der Tabelle „Lautkarten · …“: Zeichen, Beispielwort, Klang; die blauen Karten der Partitur heißen nur „Karten“), **Lautschrift** (das Zeichensystem; die Zeichen stehen zwischen Schrägstrichen: /ʃ/), **Minimalpaar** (zwei Wörter, die sich in einem Laut unterscheiden), **stummer Buchstabe** (grau), **Lesehilfe** (die deutsche Annäherung aus Hello, Millbrook!), **Kurzform**.
- Britisches Englisch (favourite, colour, football). Englische Aufgaben enthalten kein deutsches Wort.
- Lautschrift britisch: /əʊ/ (nicht /oʊ/), /ɒ/, /ɜː/, kein r nach Vokal am Wortende. Betonungszeichen (ˈ) stehen ab Kapitel 5 vor der betonten Silbe (/ˈprez.ənt/); in den Kapiteln 1 bis 3 nicht.

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

- **Klangpartitur** (SVG-Familie `src/images/partitur-<seite>.svg`, eigene Zeichnung, `CC-BY-4.0`, erzeugt mit `.agents/skills/app-content/scripts/make_partitur.py`; Hintergrund #f4efe2, Schrift mindestens 16 im 480er viewBox): drei Zeilen, links beschriftet: oben Melodie, Mitte Betonung, unten Laute. Laute: Karten in Blau (#2c6fd8) mit Lautschrift, darunter die Schreibung. Betonung: in den Kapiteln 1 bis 4 nur ein gestrichelter Rahmen „kommt später“, ab Kapitel 5 Punkte. Melodie: ab Kapitel 3 Pfeil, der steigt (Rot #c0392b) oder fällt (Grün #138d75); davor gestrichelter Rahmen „kommt später“. Stumme Buchstaben grau (#8a8577). In Aufgaben zeigt die Partitur nur die Legende, nie das Ergebnis.
- **Werkstatt** (`werkstatt-endungen.svg`): Wortkarte links (Grün), Handgriff in der Mitte (Gelb, dunkle Schrift: doppeln, y → ie, e fällt weg), Endung rechts (Blau).
- **Zungenbild** (`zunge-th.svg`): eigene Zeichnung der Zungenstellung bei /θ/ und /ð/.
- **Szenen** (`szene-<seite>.svg`): die Figuren als `<g id>` aus `millbrook-klassenzimmer.svg` von #470 (hello-millbrook), unverändert; keine Fotos, keine Figuren aus Büchern, Filmen oder Marken. Quelle „eigene Zeichnung“, Lizenz `CC-BY-4.0`. `alt` sagt, was die Szene zeigt, nie die Lösung; die Bildunterschrift nennt, wer wer ist.
- Jede Figur funktioniert bei 360 px (viewBox, Beschriftung innerhalb). Poster sind `table`-Blöcke.
- Gebaut (Inkrement 02, neu): `partitur-laut-buchstabe` (umgekehrt), `satzband-komma` (Sätze als Karten, rote Kommas), `partitur-wortbetonung-nomen`, `partitur-wortbetonung-verb`, `partitur-bindung-konsonant`, `partitur-bindung-r`, `partitur-schwache-formen`, `partitur-satzbetonung`, `partitur-tag-steigt`, `partitur-tag-faellt`. Gebaut (Version 1): Bilder `partitur-lautschrift`, `partitur-silent-letters`, `partitur-vokale`, `partitur-auslaute`, `partitur-endungen`, `partitur-kurzformen`, `partitur-melodie-frage` und `partitur-melodie-aussage` (Pfeil in der oberen Zeile: rot steigt, grün fällt), `werkstatt-endungen`, `zunge-th` (Zunge zwischen den Zähnen gegen dahinter) und je Seite eine Szene `szene-<seite>`. Alle erzeugt mit dem Skript `make_partitur.py` (ein Bild ist ein Eintrag in `PARTITUREN`, `VERSCHMELZEN`, `WERKSTAETTEN` oder `SZENEN`); Audio: `~/.cache/lernapps/audio/venv/bin/python .agents/skills/app-content/scripts/regen_audio.py <json>` (Datei → Satz, wie `audio-texte.json`).

## Sources

Karte `https://lernapps.net/apps/map/englisch.json`; Grundwortschatz `https://lernapps.net/apps/map/englisch/grundwortschatz/` (A1/A2; Wörter der Übungen stammen daraus; andere stehen unten in „Wörter außerhalb von A1/A2“). Fakten aus Wikipedia (nur Fakten, keine Sätze, CC BY-SA), geöffnet am 2026-11-21 und (Inkrement 02) am 2026-11-22: „Initial-stress-derived noun“ (present, record), „Linking and intrusive R“, „Stress and vowel reduction in English“ (schwache Formen), „Tag question“, „Comma“; `https://en.wikipedia.org/wiki/Help:IPA/English` (Zeichen und Beispielwörter, britische Schreibung /əʊ/ statt /oʊ/, kein r nach Vokal in nicht-rhotischen Akzenten), `English plurals`, `Intonation (linguistics)`, `English orthography`. Nicht geprüft: Oxford- oder Cambridge-Wörterbuch (kein Zugriff), deutsche Wikipedia, Klexikon. Beispielsätze sind eigene aus dem Alltag der Figuren. Audio: KI-Stimme `bf_emma` (britisch, weiblich), mit Skill `lernapps-audio` erzeugt und als KI-generiert markiert. Material der Ersteller:in: keines.

Wörter außerhalb von A1/A2 (auf der Seite erklärt): Inkrement 02: Hörsätze nur mit Grundwortschatz; `butter` (A1, Essen) steht im Randglossar der Seite `schwache-formen`; `bought` ist eine unregelmäßige Form von buy (in `pruefen.py` freigegeben). Die Aussage zum Satzrhythmus („starke Wörter ungefähr im gleichen Abstand“) ist vereinfacht und steht nicht in den geöffneten Quellen; sie ist nicht geprüft. `klaenge/lautschrift`: keine (alle englischen Wörter der Seite gegen die Liste geprüft, 2026-11-21; Namen ausgenommen). Pig und chips stehen nicht in der Liste und werden nicht mehr abgefragt. Weitere Seiten: `silent-letters`, `rechtschreibung-endungen`, `kurzformen` und die Wiederholungsseiten: keine; `hop` ist erklärt („hüpfen“, auf `rechtschreibung-endungen`); alle Hörsätze wurden mit `scripts/pruefen.py` gegen die Liste geprüft. Neue Seiten: `python3 .agents/skills/app-content/scripts/pruefen.py` ausführen (prüft auch Dubletten und audio-texte.json).

## Hörliste (vor dem Veröffentlichen von einem Menschen anzuhören)

Hörprobe 2 (`.vibe/hoerprobe2/`: present/record Nomen und Verb, far away, bread and butter, Sophie wants to go to the shop, Tag-Frage): die Ersteller:in hat gehört, dass alles passt; die sieben Sätze stehen unten als „gehört, in Ordnung“. Die Tag-Frage wurde nicht übernommen (die Melodie steigt nicht; keine Aufnahme der Melodie). Die Stimme `bf_emma` wurde hier nicht angehört (die Entwicklung läuft ohne Ohr). Die Ersteller:in hat die Hörprobe (`.vibe/hoerprobe/`: sheep, ship, bed, bet, thank, sank in der Satzmitte) angehört: die kritischen Paare sind gut zu unterscheiden. Alle anderen Dateien bleiben offen. Alle Dateien wurden mit der Regel `valley_cut` (aus `regen_audio.py`, Fehllaut nach der letzten Senke, siehe README-schnitt der Orchestrator-Session) erzeugt; fünf Sätze wurden dabei am Ende gekürzt (Spalte Prüfstand). Als Gegenprobe zeigt `scripts/enden_pruefen.py` sechs Dateien mit sehr kurzem letzten Abschnitt („Ende prüfen“): die Ersteller:in hört sie gezielt an, vor allem Wörter mit zweiter Silbe am Satzende (upstairs, village). Alle Sätze enden auf ein zwei- oder mehrsilbiges Wort. Jede Datei aus `src/audio/` muss ein Mensch mit Englisch hören, besonders die Minimalpaare. Tabelle: Datei, Satz, erwartetes Minimalwort, Prüfstand (offen / gehört, in Ordnung / ändern). Hörprobe: `.vibe/hoerprobe/` (sheep, ship, bed, bet, thank, sank in der Satzmitte, noch nicht angehört).

| Datei (src/audio/) | Seite | Satz | erwartetes Wort/Laut | Prüfstand |
|---|---|---|---|---|
| `amir-jumped-over-the-boxes-yesterday.mp3` | endungen/endungen-s-ed | Amir jumped over the boxes yesterday. | Endung -s oder -ed (/s/, /z/, /ɪz/, /t/, /d/, /ɪd/) | offen |
| `amir-painted-a-picture-yesterday.mp3` | endungen/endungen-s-ed | Amir painted a picture yesterday. | painted /ɪd/ | offen |
| `amir-played-football-with-peter-yesterday.mp3` | endungen/endungen-s-ed | Amir played football with Peter yesterday. | played /d/ | offen |
| `ellie-has-two-cats-and-a-dog-today.mp3` | endungen/endungen-s-ed | Ellie has two cats and a dog today. | cats /s/ | offen |
| `mrs-parker-opens-the-window-every-morning.mp3` | endungen/endungen-s-ed | Mrs Parker opens the window every morning. | Endung -s oder -ed (/s/, /z/, /ɪz/, /t/, /d/, /ɪd/) | offen |
| `peter-cleaned-his-room-yesterday.mp3` | endungen/endungen-s-ed | Peter cleaned his room yesterday. | cleaned /d/ | offen |
| `peter-needed-some-help-yesterday.mp3` | endungen/endungen-s-ed | Peter needed some help yesterday. | needed /ɪd/ | offen |
| `peter-plays-with-two-dogs-in-the-garden.mp3` | endungen/endungen-s-ed | Peter plays with two dogs in the garden. | Endung -s oder -ed (/s/, /z/, /ɪz/, /t/, /d/, /ɪd/) | offen |
| `sophie-waited-for-the-bus-yesterday.mp3` | endungen/endungen-s-ed | Sophie waited for the bus yesterday. | Endung -s oder -ed (/s/, /z/, /ɪz/, /t/, /d/, /ɪd/) | offen |
| `the-children-walked-to-school-together.mp3` | endungen/endungen-s-ed | The children walked to school together. | walked /t/ | offen |
| `amir-carries-two-bags-upstairs.mp3` | endungen/rechtschreibung-endungen | Amir carries two bags upstairs. | Wort mit Endung -ing, -s oder -ed | offen · Fehllaut-Schnitt (−85 ms) |
| `amir-studies-english-in-the-evening.mp3` | endungen/rechtschreibung-endungen | Amir studies English in the evening. | Wort mit Endung -ing, -s oder -ed | offen |
| `ellie-is-running-to-the-station.mp3` | endungen/rechtschreibung-endungen | Ellie is running to the station. | Wort mit Endung -ing, -s oder -ed | offen |
| `peter-is-getting-a-new-bag-today.mp3` | endungen/rechtschreibung-endungen | Peter is getting a new bag today. | Wort mit Endung -ing, -s oder -ed | offen |
| `peter-stayed-at-home-yesterday.mp3` | endungen/rechtschreibung-endungen | Peter stayed at home yesterday. | Wort mit Endung -ing, -s oder -ed | offen |
| `sophie-is-shopping-with-mrs-parker.mp3` | endungen/rechtschreibung-endungen | Sophie is shopping with Mrs Parker. | Wort mit Endung -ing, -s oder -ed | offen |
| `is-peter-at-home-this-afternoon.mp3` | gespraech/intonation-fragen | Is Peter at home this afternoon? | Frage (Dateien der Fragen steigen nicht) | offen |
| `please-carry-the-bag-for-amir.mp3` | gespraech/intonation-fragen | Please carry the bag for Amir. | Aufforderung | offen |
| `where-does-mrs-parker-work-today.mp3` | gespraech/intonation-fragen | Where does Mrs Parker work today? | Frage mit Fragewort | offen |
| `ellie-doesnt-like-coffee-today.mp3` | gespraech/kurzformen | Ellie doesn't like coffee today. | doesn't | offen |
| `hows-mrs-parker-today.mp3` | gespraech/kurzformen | How's Mrs Parker today? | how's | offen |
| `we-arent-hungry-this-morning.mp3` | gespraech/kurzformen | We aren't hungry this morning. | aren't | offen |
| `whats-in-your-bag-today.mp3` | gespraech/kurzformen | What's in your bag today? | what's | offen |
| `wheres-peter-this-morning.mp3` | gespraech/kurzformen | Where's Peter this morning? | where's | offen |
| `youre-early-and-im-late-again.mp3` | gespraech/kurzformen | You're early, and I'm late again. | you're, I'm | offen |
| `amir-lives-in-the-west-of-the-village.mp3` | klaenge/konsonanten-th-w | Amir lives in the west of the village. | west /w/, village /v/ | offen · Ende prüfen (Wächter schnitt nicht) |
| `amir-visits-his-uncle-every-sunday.mp3` | klaenge/konsonanten-th-w | Amir visits his uncle every Sunday. | visits /v/ | offen |
| `amir-waits-for-the-bus-every-morning.mp3` | klaenge/konsonanten-th-w | Amir waits for the bus every morning. | th, w, v oder r | offen |
| `ellie-drives-the-van-slowly.mp3` | klaenge/konsonanten-th-w | Ellie drives the van slowly. | van /v/ | offen |
| `mother-thinks-the-weather-is-lovely-today.mp3` | klaenge/konsonanten-th-w | Mother thinks the weather is lovely today. | th, w, v oder r | offen |
| `peter-has-a-red-ball-upstairs.mp3` | klaenge/konsonanten-th-w | Peter has a red ball upstairs. | red /r/ | offen · Fehllaut-Schnitt (−85 ms) · Ende prüfen (nach dem Schnitt) |
| `sophie-looks-at-the-blue-sky-again.mp3` | klaenge/konsonanten-th-w | Sophie looks at the blue sky again. | the /ð/ | offen |
| `sophie-thinks-about-the-party-tomorrow.mp3` | klaenge/konsonanten-th-w | Sophie thinks about the party tomorrow. | th, w, v oder r | offen |
| `they-thank-the-teacher-today.mp3` | klaenge/konsonanten-th-w | They thank the teacher today. | thank /θ/ | offen |
| `three-brothers-wait-at-the-window.mp3` | klaenge/konsonanten-th-w | Three brothers wait at the window. | three /θ/, window /w/ | offen |
| `amir-buys-a-new-watch-today.mp3` | klaenge/lautschrift | Amir buys a new watch today. | watch /tʃ/ | offen |
| `amir-has-a-chair-in-the-kitchen.mp3` | klaenge/lautschrift | Amir has a chair in the kitchen. | chair /tʃ/, kitchen /tʃ/ | offen |
| `ellie-has-a-fish-and-a-green-apple.mp3` | klaenge/lautschrift | Ellie has a fish and a green apple. | fish /ʃ/, green /iː/ | offen |
| `ellie-has-a-red-chair-again.mp3` | klaenge/lautschrift | Ellie has a red chair again. | chair /tʃ/ | offen |
| `peter-has-a-black-cat-upstairs.mp3` | klaenge/lautschrift | Peter has a black cat upstairs. | cat /æ/ | offen · Fehllaut-Schnitt (−95 ms) · Ende prüfen (nach dem Schnitt) |
| `peter-likes-to-sing-together.mp3` | klaenge/lautschrift | Peter likes to sing together. | sing /ŋ/ | offen |
| `peter-takes-a-long-walk-this-morning.mp3` | klaenge/lautschrift | Peter takes a long walk this morning. | long /ŋ/ | offen |
| `sophie-and-peter-eat-cheese-together.mp3` | klaenge/lautschrift | Sophie and Peter eat cheese together. | cheese /tʃ/, /iː/ | offen |
| `sophie-has-a-new-shoe-today.mp3` | klaenge/lautschrift | Sophie has a new shoe today. | shoe /ʃ/ | offen |
| `sophie-washes-the-dishes-this-evening.mp3` | klaenge/lautschrift | Sophie washes the dishes this evening. | washes /ʃ/, -es | offen |
| `amir-listens-to-mrs-parker.mp3` | klaenge/silent-letters | Amir listens to Mrs Parker. | listens: t stumm | offen |
| `amir-wrote-a-letter-yesterday.mp3` | klaenge/silent-letters | Amir wrote a letter yesterday. | wrote: w stumm | offen |
| `ellie-fastens-her-bag-in-the-kitchen.mp3` | klaenge/silent-letters | Ellie fastens her bag in the kitchen. | fastens: t stumm | offen |
| `mr-hill-writes-a-long-text-today.mp3` | klaenge/silent-letters | Mr Hill writes a long text today. | writes: w stumm | offen |
| `peter-talks-to-mrs-parker-every-morning.mp3` | klaenge/silent-letters | Peter talks to Mrs Parker every morning. | talks: l stumm | offen |
| `sophie-climbs-the-big-tree-with-ellie.mp3` | klaenge/silent-letters | Sophie climbs the big tree with Ellie. | climbs: b stumm | offen |
| `amir-puts-the-bag-on-the-table.mp3` | klaenge/stimmhafte-auslaute | Amir puts the bag on the table. | stimmhaftes oder stimmloses Wortende | offen |
| `ellie-has-a-bad-cold-this-morning.mp3` | klaenge/stimmhafte-auslaute | Ellie has a bad cold this morning. | stimmhaftes oder stimmloses Wortende | offen |
| `i-like-this-bed-very-much-today.mp3` | klaenge/stimmhafte-auslaute | I like this bed very much today. | bed: d summt | offen |
| `i-made-a-bet-yesterday.mp3` | klaenge/stimmhafte-auslaute | I made a bet yesterday. | bet: t summt nicht | offen |
| `mr-hill-carries-a-heavy-bag-every-morning.mp3` | klaenge/stimmhafte-auslaute | Mr Hill carries a heavy bag every morning. | bag: g summt | offen |
| `mr-hill-writes-a-long-word-on-the-board-today.mp3` | klaenge/stimmhafte-auslaute | Mr Hill writes a long word on the board today. | stimmhaftes oder stimmloses Wortende | offen |
| `peter-has-a-big-cat-and-a-small-dog-today.mp3` | klaenge/stimmhafte-auslaute | Peter has a big cat and a small dog today. | stimmhaftes oder stimmloses Wortende | offen |
| `the-boat-is-at-the-dock-today.mp3` | klaenge/stimmhafte-auslaute | The boat is at the dock today. | dock: k summt nicht | offen |
| `the-dog-is-very-big-and-friendly.mp3` | klaenge/stimmhafte-auslaute | The dog is very big and friendly. | dog: g summt | offen |
| `the-kid-hides-under-the-table-today.mp3` | klaenge/stimmhafte-auslaute | The kid hides under the table today. | kid: d summt | offen |
| `ellie-wants-to-sit-on-the-seat-again.mp3` | klaenge/vokale | Ellie wants to sit on the seat again. | kurzer oder langer Vokal, /æ/ oder /ʌ/ (Minimalwort in der Satzmitte) | offen |
| `look-a-sheep-again.mp3` | klaenge/vokale | Look, a sheep again. | sheep /ʃiːp/ (lang) | offen |
| `look-a-ship-again.mp3` | klaenge/vokale | Look, a ship again. | ship /ʃɪp/ (kurz) | offen |
| `my-cat-is-sleeping-again.mp3` | klaenge/vokale | My cat is sleeping again. | cat /æ/ | offen |
| `peter-cut-the-apple-in-the-kitchen.mp3` | klaenge/vokale | Peter cut the apple in the kitchen. | kurzer oder langer Vokal, /æ/ oder /ʌ/ (Minimalwort in der Satzmitte) | offen |
| `please-cut-the-bread-today.mp3` | klaenge/vokale | Please cut the bread today. | cut /ʌ/ | offen |
| `please-leave-the-bag-in-the-kitchen.mp3` | klaenge/vokale | Please leave the bag in the kitchen. | kurzer oder langer Vokal, /æ/ oder /ʌ/ (Minimalwort in der Satzmitte) | offen |
| `sophie-and-ellie-live-in-a-small-village.mp3` | klaenge/vokale | Sophie and Ellie live in a small village. | kurzer oder langer Vokal, /æ/ oder /ʌ/ (Minimalwort in der Satzmitte) | offen · Fehllaut-Schnitt (−55 ms) · Ende prüfen (nach dem Schnitt) |
| `sophie-sees-a-sheep-and-a-ship-today.mp3` | klaenge/vokale | Sophie sees a sheep and a ship today. | kurzer oder langer Vokal, /æ/ oder /ʌ/ (Minimalwort in der Satzmitte) | offen |
| `the-bag-is-full-of-apples-today.mp3` | klaenge/vokale | The bag is full of apples today. | full /ʊ/ | offen |
| `we-can-hear-the-band-outside.mp3` | richtig-schreiben/laut-buchstabe | We can hear the band outside. | hear / here | offen · Ende prüfen |
| `please-write-the-right-word-today.mp3` | richtig-schreiben/laut-buchstabe | Please write the right word today. | write / right | offen |
| `after-the-long-lesson-peter-plays-football-in-the-garden.mp3` | richtig-schreiben/kommasetzung | After the long lesson, Peter plays football in the garden. | Pause nach der Einleitung | offen · Fehllaut-Schnitt (−93 ms) |
| `my-teacher-who-is-very-kind-helps-us-today.mp3` | richtig-schreiben/kommasetzung | My teacher, who is very kind, helps us today. | Pause um den Relativsatz | offen |
| `i-bought-a-present-for-sophie.mp3` | betonung-rhythmus-melodie/wortbetonung | I bought a present for Sophie. | present (Nomen): erste Silbe betont | gehört, in Ordnung (Hörprobe 2, Ersteller:in) |
| `we-present-the-show-tomorrow.mp3` | betonung-rhythmus-melodie/wortbetonung | We present the show tomorrow. | present (Verb): zweite Silbe betont | gehört, in Ordnung (Hörprobe 2, Ersteller:in) |
| `this-is-a-record-of-the-game-today.mp3` | betonung-rhythmus-melodie/wortbetonung | This is a record of the game today. | record (Nomen): erste Silbe betont | gehört, in Ordnung (Hörprobe 2, Ersteller:in) · Ende prüfen (Schlusswort today gehört) |
| `we-record-the-song-tomorrow.mp3` | betonung-rhythmus-melodie/wortbetonung | We record the song tomorrow. | record (Verb): zweite Silbe betont | gehört, in Ordnung (Hörprobe 2, Ersteller:in) |
| `my-father-is-far-away-today.mp3` | betonung-rhythmus-melodie/bindungen | My father is far away today. | linking r: far away | gehört, in Ordnung (Hörprobe 2, Ersteller:in) |
| `bread-and-butter-for-peter-and-amir.mp3` | betonung-rhythmus-melodie/schwache-formen | Bread and butter for Peter and Amir. | schwaches and, for | gehört, in Ordnung (Hörprobe 2, Ersteller:in) |
| `sophie-wants-to-go-to-the-shop-today.mp3` | betonung-rhythmus-melodie/satzbetonung | Sophie wants to go to the shop today. | betonte Wörter Sophie, wants, go, shop, today | gehört, in Ordnung (Hörprobe 2, Ersteller:in) |

## Adding a chapter or round

1. Baustein auf der Karte wählen (Kapitel 4 und 5: siehe oben; Stufe 7-8: kein Zeichen der Lautschrift setzen, das nicht auf einer Lautkarte steht); die Voraussetzungen müssen auf früheren Seiten stehen oder eine Wiederholungsseite bekommen.
2. Seite `src/<kapitel>/<seite>.yaml` mit den Abschnitten `einstieg`, `neu`, `uebung`, `anwenden`, `weiter` anlegen, in `chapter.yaml` eintragen, Competency-ID setzen.
3. Partitur-Bild: neue Zeile in `make_partitur.py`; die mittlere Zeile füllt Kapitel 5 (große und kleine Punkte).
4. Übungen aus den Mustern oben, je mit `mistakes` und `hint`; 1 bis 2 ihrer Übungen (ohne Audio) in `selfAssessment` des Kapitels.
5. Hörtexte: Datei `src/audio/<satz>.mp3` und Eintrag in `.agents/skills/app-content/scripts/audio-texte.json` (Datei → Satz), erzeugt mit `regen_audio.py` (aus hello-millbrook, schneidet das Ausklingen ab); Sätze nicht zwischen Seiten wiederholen, Minimalwörter nie am Satzende, Sätze natürlich lassen (kein Name nur wegen des Klangs), einsilbige Enden in die Hörliste; Eintrag in die Hörliste.
6. Wörter gegen den Grundwortschatz prüfen; `npx --no -- lernapps check`; committen.

## Rules learned from mistakes

Aus #470, #472, #473 und `konventionen.md` Abschnitt 7 übernommen:
- Jede Übung fragt nur Wörter ab, die vorher auf der Seite stehen; Wörter außerhalb von A1/A2 werden auf der Seite erklärt.
- Eine Tabelle, die eine Übung beantwortet, steht nicht direkt über ihr; Einstieg, Poster, Merke und Bild nennen andere Beispiele als die Übungen.
- Diktat und Nachsprechen bringen neue Sätze: kein Hörsatz steht wörtlich oder fast wörtlich in Einstieg, Poster, Merke, Bildtext oder in einer anderen Übung derselben Seite (Skriptprüfung).
- Distraktoren nur echte Lernerfehler, jeder mit eigener Meldung; ein Einstiegs-`single-choice` hat mindestens drei Optionen.
- Mit `(a|b)` gleichwertige richtige Antworten zulassen; Kurzformen zulassen; `case: wrong` nur dort, wo die Seite Großschreibung unterrichtet.
- Audio: das Ausklingen der Stimme am Satzende abschneiden (`regen_audio.py`), kein Name nur wegen des Klangs am Satzende (das Ausklingen schneidet `regen_audio.py` ab; Sätze mit einsilbigem Ende in die Hörliste), keine Einzelwörter, Minimalwort nie am Satzende.
- Bilder: Beschriftungen innerhalb des `viewBox`; die Bildunterschrift nennt, wer wer ist; das `alt` verrät nie die Lösung.
- Hinweise und Meldungen nennen weder „Spalte“ noch „Poster“ noch „oben“.
- Ein Begriff steht auf der Seite, bevor eine Übung ihn braucht; höchstens drei neue Begriffe je Absatz; ein Merke-Kasten hat zwei bis drei Aussagen.
- Bei `accepted` mit `?` in der Flow-Liste den Eintrag in Anführungszeichen setzen.
Aus dieser App (Lerner-Check der Musterseite, Sprachprüfung, Orchestrator-Prüfung):
- Bildschrift mindestens 22 im 480er viewBox (Partitur) und 27 in Sprechblasen der Szene, sonst ist sie bei 360 px nicht lesbar; ein Zeichen wie ː muss innerhalb der Karte liegen (Kartenbreite 17 je Zeichen plus 44).
- Der Einstieg einer Seite stellt keine Frage, die erst die Erklärung beantwortet: die Szene und die Antwort-`explanation` tragen den Grund.
- Antworten einer Auswahl sind gleich lang; die richtige ist nicht die längste und nicht die einzige vorsichtige.
- Ein Distraktor ist ein echter Lernerfehler mit eigener `info`; `matching` hat keine Meldung je Eintrag und keine Distraktoren, `multiple-choice` oder `single-choice` mit `info` benutzen, wenn der Fehler eine Meldung braucht.
- Eine Übungsfrage mit einem Wort, das in der Zuordnung davor steht, verrät sich: andere Wörter abfragen. Bild, Tabelle, Zuordnung, Schreiben und Diktat nehmen je andere Wörter.
- Ein Wort, das ein zweites Zeichen derselben Aufgabe enthält (cheese: /tʃ/ und /iː/), macht die Frage mehrdeutig.
- Das Wort „Lautkarte“ nur für eine Zeile der Lautkarten-Tabelle; die blauen Karten der Partitur heißen „Karten“.
- Schreibaufgaben mit `case: ok`, sonst meldet die App „richtig“ und im gleichen Satz „Achte auf Groß- und Kleinschreibung“; Diktate: ganze Sätze, `punctuation: ok`, mit `mistakes` je Satz.
- Nach der Eingabe „drei“ in einem `number`-Feld meldet die App nur „Antworte zuerst“: die Aufgabe sagt „mit Ziffern“.
- Höchstens vier Sätze je `speaking-task` zum Anhören; mehr wirkt wie viele Aufnahmeknöpfe.
- Pig und chips stehen nicht im Grundwortschatz: nicht abfragen.
- Wörter einer Aufgabe zu einem Muster folgen genau den Mustern der Tabelle darüber (stumme Buchstaben: kn, wr, mb, st, lk, gh), und die Wörter der Tabelle werden nicht abgefragt; ein Wort ohne Muster (answer, castle, two, hour) ist für Kinder nur zu raten.
- Regeln der Schreibung (Verdoppeln, y → ie, e fällt weg) mit „meist“ oder „bei kurzen Wörtern“ formulieren: visit – visited, open – opened, show – showed, fix – fixed, see – seeing sind Ausnahmen.
- Eine Aussage zur Silbenzahl (Kurzform = eine Silbe) stimmt nicht für isn't und doesn't; sagen: „als ein Wort, ohne Pause“.
- Übungen zu einer Kurzform fragen nicht dieselben Paare wie die Zuordnung darüber; Diktate mit Kurzformen nehmen Formen, die nicht im Poster oder in anderen Übungen stehen.
- Hinweise im Diktat verraten nicht, dass ein Apostroph fehlt („Das erste Wort ist eine Kurzform“).
- Die Seite sagt nur, was die App prüft: „Du verstehst/schreibst …“, nicht „Du sprichst richtig“, weil nichts die Aussprache beurteilt.
- Der Dev-Server (`npm run dev`) wird als Hintergrundaufgabe des Werkzeugs gestartet, sonst endet er mit der Shell.
- Entscheidung: `gespraech/intonation-fragen` hat keine Aufnahmen zum Nachsprechen, nur Diktate (Satzzeichen, keine Melodie): die Stimme steigt bei Ja-Nein-Fragen am Satzende nicht; lieber keine Aufnahme als eine, die falsch belehrt.
- Aus dem Gesamtcheck: Die KI-Stimme `bf_emma` steigt bei Ja-Nein-Fragen am Satzende nicht (Tonhöhe gemessen): Seiten zur Satzmelodie haben keine Aufnahmen zum Nachsprechen, die Pfeile und die Tabelle tragen die Regel (Schreib- und Sprechaufgabe als `open-task`). Ein Hörsatz mit einem Namen am Ende (Anrede) taugt nicht für eine steigende Frage.
- Eine Szene, die ein Rätsel stellt (aim, Sank you, walk-ed, k-nee), wird auf derselben Seite aufgelöst (in `explanation`: /aɪm/ gegen /eɪm/).
- Ein Begriff, den eine spätere Seite erklärt (summt, stimmhaft), steht nicht vorher auf einer Seite; vorher sagt man „weich“, „hauchig“.
- Jeder Apostroph und jeder Doppelbuchstabe lässt sich nicht hören: Diktate dazu sind Schreibaufgaben, und der Hinweis sagt das („Den Apostroph hörst du nicht“).
- Am Seitenende steht ein Schritt, den die nächste Seite aufnimmt: gleiche Figuren, gleicher Ort (p1 → p2: Peter und das Foto).
- Wiederholungsseiten erinnern auch an Begriffe aus früheren Kapiteln dieser App (Klangpartitur, Karte, stimmhaft/stimmlos) mit Link auf die Seite, die sie einführt; eine Seite nennt nie eine „Karte“, die nicht auf Seite 1 oder in der Wiederholung steht.
- Zeichen, die ein Bild zeigt, sind vorher im Text oder in der Tabelle eingeführt (ɛ in bɛd steht im Text der Seite zu den Wortenden).
- Wörter am Rand (Glossar vor dem Lesestück) stehen im Block `vocabulary` (`languages: { source: de, target: en }`, `entries` mit `target` und `source`), nicht in einer Tabelle (lernapps-explainer, `references/language-tasks.md`). Die einzige Tabelle einer Seite bleibt für Daten wie „Starke und schwache Formen“ (seit Templates 0.14.0).
- Melodie wird nie aufgenommen: `bf_emma` steigt bei Ja-Nein-Fragen nicht; Seiten zur Melodie (`intonation-fragen`, `intonation-question-tags`) haben keine Hörübung dazu, sagen das offen und verweisen auf echte Sprecher.
- Hörsätze der Betonung sind nur die von der Ersteller:in abgehörten Sätze (Hörprobe 2); neue Betonungspaare brauchen wieder eine Hörprobe und ein Hörurteil.
- Übungen zu Betonung und Schwachformen nehmen andere Wörter als Lesestück und Merke (increase, insult, from, at, was, them statt present, record, and, to).
- Ein Wort einer Tabelle oder Merke steht nie als Lösung direkt über der Übung dazu; Aufgaben mit Zahlen (`number`) haben für den typischen Fehler eine eigene Meldung.
- Selbsteinschätzung: jedes Kapitel hat eine in `chapter.yaml`; neue Seiten: 1 bis 3 ihrer Übungen in `selfAssessment` aufnehmen, wie Skill `lernapps-explainer-self-assessment` sagt. Ohne Ton und ohne Bezug zur Seite („oben“); Hörübungen, Sprechaufgaben und offene Aufgaben stehen nie darin. Kapitel 4: 5 Übungen in 2 Schritten, Kapitel 5: 10 Übungen in 3 Schritten (die Wiederholungsseiten sind nie dabei).
- Keine Vorstellung der Figuren im Verlauf: kein Alter, keine Verwandtschaft, kein Datum und keine Herkunft im Fließtext, in Bildunterschriften und in Szenen-Texten; wer die Figuren sind, steht einmal in der Einleitung der App (`src/app.yaml`). Eine Figur wird nur dort kurz benannt, wo die Aufgabe sie braucht (wer spricht in der Chatzeile). Einstieg und `weiter` sagen in ein bis zwei Sätzen, was geschieht und was als Nächstes kommt, ohne Rückblick auf frühere Seiten und ohne Zitat von Mr Hill, das nichts zur Aufgabe beiträgt (Auftrag der Ersteller:in, Inkrement 03).
