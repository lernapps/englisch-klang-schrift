---
# Read by the hooks, the review, the evals. Schema: @lernapps/tooling/guidance/plan-front-matter.v1.schema.json
# Written by `lernapps plan` and the hooks. Never change a key or a value by hand.
# Archetype, as in the app's first plan. Allowed values: explainer, interactive, quiz.
archetype: explainer
# Current phase. Allowed values: explore, plan, code, commit.
phase: commit
# prePushFailures: failed pre-push runs of this increment, written by the hook.
prePushFailures: 0
# failedChecks: failed rules and runs, written by lernapps check and the hooks.
failedChecks: { checks-pass: 3 }
---

# Increment: increment-02-richtig-schreiben-betonung

<!--
For you, the assistant. One increment of a published app: new competencies, chapters, pages, rounds, questions, or a
correction. The process is in AGENTS.md; this plan holds the method.
- `npx --no -- lernapps plan next` prints the task to do now, `plan done` ticks it and prints the next one.
- You write only below Goal, Key decisions, Notes, Answers, Content method and Retrospective, in the creator's
  language. Delete the comment of a section once the section is filled.
- The first version's decisions stand: archetype, content method, content guide. Never change an earlier plan.
- Work on the branch `increment/<NN>-<short name>`. Until Commit everything is local: push nothing.
-->

*Started 2026-11-22. Explore, Plan, Code, Commit.*

## Goal

<!-- 1–2 sentences: what learners can do after this increment. -->

Stufe 7-8 der Strang-App `englisch/aussprache` (Auftrag lernapps/apps#482): Kapitel 4 „Richtig schreiben“ und Kapitel 5 „Betonung, Rhythmus und Melodie“ mit 7 Bausteinen. Jede Seite hat ein kurzes Lesestück (Chat, Blog, Dialog von Sophie, 13 bis 14, in England) zum Lesen und Hören, dazu Übungen in drei Stufen (verstehen, belegen, Meinung oder Anwendung).


## Key decisions

<!-- One line each: decision and reason. Your own choice without the creator: mark "(guess)". -->

- Archetyp und Inhaltsmethode der ersten Version gelten (`explainer`, Format 2, Strang `englisch/aussprache`, britisch, `[de]`, `scope`, keine Komponente); das Inkrement ändert sie nicht.
- Neue Seitenform nach `konventionen.md` Abschnitt 8: **Lesestück als Kern** (Stufe 7-8: etwa 150 bis 300 Wörter, hier eher 120 bis 200: Pronunciation-Seiten, Lesestück zählt nicht zu den 350 Wörtern Erklärtext), Aufgaben in drei Stufen (verstehen, belegen mit Zeile, Meinung/Anwendung), Randglossar als `definition`-Blöcke. Chat und Blog als Text ohne Bild (ein Bild nur, wo es etwas zeigt: die Klangpartitur). (guess: Lesestück kürzer als 150 Wörter nur, wenn die Seite sonst zu lang wird)
- Die mittlere Zeile der Klangpartitur (Betonung) wird in Kapitel 5 gefüllt: große Punkte auf betonten, kleine auf unbetonten Silben und Wörtern; `make_partitur.py` bekommt dafür eine Funktion.
- Eigene Texte nach Fakten (Wikipedia-Fakten, keine Sätze), keine Texte von VOA, Wikinews, African Storybook (nicht nötig). Figuren: Sophie 13 bis 14, Ellie, Peter, Amir, Mr Hill; Mrs Parker nur im Text (Zeichnung nach `konventionen.md`, falls je gezeichnet).
- Audio nur, was die Stimme richtig spricht: Vor dem Bau der Seiten eine **Hörprobe** zur Betonung (present Nomen/Verb, record, desert), zu Bindungen (far away) und schwachen Formen; die Satzmelodie bei question tags wird **nicht** aufgenommen (die Stimme steigt bei Fragen nicht). Messung der Tonhöhe und Lautstärke je Silbe als Hinweis, kein Ersatz für das Ohr eines Menschen.
- Wiederholungsseiten: Kapitel 4 vor `kommasetzung` für `relativsaetze-nicht-notwendig` (#481), Kapitel 5 vor `intonation-question-tags` für `question-tags` (#473).
- `intonation-haltung` (Stufe 9-10) bleibt außerhalb.


## Notes

<!-- New competencies by chapter (ids of the strand), didactic approach, scope, sources and licences, open questions. -->

Neue Bausteine (Karte, Band 7-8) und `requires`:
- Kapitel 4 `richtig-schreiben`: `laut-buchstabe` (Schritt 1; requires vokale, silent-letters: beide in Kapitel 1) · `kommasetzung` (Schritt 2; requires `relativsaetze-nicht-notwendig` aus #481: Wiederholungsseite)
- Kapitel 5 `betonung-rhythmus-melodie`: `wortbetonung` (1; lautschrift) · `bindungen` (1) · `schwache-formen` (2; wortbetonung) · `satzbetonung` (3; schwache-formen, bindungen) · `intonation-question-tags` (1; `question-tags` aus #473: Wiederholungsseite; intonation-fragen: Kapitel 3)
Neun Dateien: 7 Fachseiten und 2 Wiederholungsseiten. Reihenfolge nach `requires`, im Kapitel 5 steht `satzbetonung` nach `schwache-formen` und `bindungen`, die question-tags-Seite zuletzt (sie baut auf der Melodie aus Kapitel 3 auf).

Didaktik je Baustein (ableiten statt ablesen, Fehlvorstellung in Klammern):
- `laut-buchstabe`: Richtung der Partitur umdrehen (vom Laut zur Schrift): ein Laut /iː/ hat mehrere Schreibungen (ee, ea, e-e), und gleich klingende Wörter (see – sea, meet – meat) unterscheidet nur die Schrift; /aɪ/ in night, light (igh); Lesestück: Sophies Chat mit einer Rechtschreibprüfung. (Rechtschreibprüfung findet see/sea nicht; „Wie ich es höre, schreibe ich es.“)
- `kommasetzung`: Kommas zeigen Pausen, die man auch hört; nach einleitendem Adverbial (Last summer, we …), vor/nach nicht notwendigem Relativsatz (My brother, who lives in London, …), Aufzählung; Lesestück: Sophies Blogeintrag. (Komma wie im Deutschen: vor jedem Nebensatz; dass-Satz hat im Englischen kein Komma)
- `wortbetonung`: große und kleine Punkte; Paare present (Nomen: erste Silbe) – present (Verb: zweite Silbe), record, desert; Lesestück: Chat über ein Geschenk. (jede Silbe gleich lang; Betonung wie im Deutschen)
- `bindungen`: Wörter verbinden: Konsonant → Vokal (turn off), linking r (far away); Lesestück: Peter nimmt Sophies Vorlesung auf. (jedes Wort einzeln sprechen)
- `schwache-formen`: and, to, of, for, can als /ən/, /tə/, /əv/ nur unbetont; am Satzende stark; Schwa /ə/; Lesestück: Dialog beim Backen mit Mrs Parker (Rezept vorlesen). (alle Wörter voll sprechen)
- `satzbetonung`: Inhaltswörter (Nomen, Verben, Adjektive) tragen Betonung, Funktionswörter nicht; Rhythmus: Betonungen in gleichen Abständen; Lesestück: Sophies Nachricht. (jedes Wort betonen)
- `intonation-question-tags`: Tag steigt (echte Frage) oder fällt (erwartet Zustimmung), ohne Aufnahme (die Stimme zeigt es nicht); Pfeil in der oberen Zeile; Lesestück: Chat zwischen Sophie und Ellie. (jeder Tag steigt)

Scope: drin sind Betonung im Wort und im Satz, Bindungen, schwache Formen, Rhythmus, Melodie bei question tags, Komma bei Einleitung, nicht notwendigem Relativsatz und Aufzählung, Schreibungen von /iː/ (ee, ea), /aɪ/ (igh), Homophone. Nicht drin: Haltung und Gefühl in der Satzmelodie (9-10), amerikanische Betonung (#484), Zeichensetzung außer Komma, weitere Schreibregeln (Kapitel 1 und 2).

Quellen (am 2026-11-22 geöffnet, nur Fakten): en.wikipedia.org „Initial-stress-derived noun“ (Betonungsverschiebung present, record), „Linking and intrusive R“ (linking r bei non-rhotic Akzenten), „Stress and vowel reduction in English“ (schwache und starke Formen, Wörterliste), „Tag question“ (Hilfsverb, balancierte und unbalancierte Tags), „Comma“ (nicht notwendige Relativsätze, einleitende Phrasen). Nicht geprüft: Oxford- und Cambridge-Wörterbuch, deutsche Wikipedia. Keine Texte übernommen.


## Explore

<!--
- All content questions belong here; Plan maps the answers onto the app. Ask; write no code.
- Skip what earlier answers or the app already tell. At most 2 questions per message, one topic each.
-->

### Tasks

- [x] Read the README of the archetype's template (its path is in skill `lernapps-app`): what the app can do now.
      Tell the creator what is new, if it matters for this increment.
- [x] Load the content guide `.agents/skills/app-content/SKILL.md` and read the earlier plans in `.vibe/plans/`: what
      the app teaches, how its content is made, what is open.
- [x] Interview, one topic per question, the creator's words under "Answers": which competencies, chapters or rounds,
      for which school years; hurdles and examples; the amount; any change of look and feel or of terms. No answer:
      ask once more, then write your assumption with "(guess)".
- [x] Load skill `lernapps-content-research`. Research what the content guide does not cover. Write under "Notes":
      the new competencies by chapter with their ids, the sources you opened.
- [x] Write under "Notes" the didactic approach per competency and the scope (in, out, data range).
- [x] The increment needs a kind of content the guide does not cover (a new page structure, screen, component or kind
      of exercise): load skills `lernapps-explainer-design` and `lernapps-exercise-patterns`. Else skip this task.
- [x] **Checkpoint:** research. Show in plain words: the new competencies by chapter, the didactic approach, the
      scope, every "(guess)", the sources and what is unchecked. Stop and wait. Changes: change them, then ask again.
      Creator: Ja: kürzere Lesestücke (120 bis 200 Wörter) für Aussprache-Seiten ok. Zuerst K4 (laut-buchstabe, kommasetzung); wortbetonung, bindungen, schwache-formen, satzbetonung erst nach dem Hörurteil zur Hörprobe 2. Nichts weiter pushen, bis die Ersteller:in es erlaubt.

### Answers

<!-- The creator's answers, in their words, one bullet each. -->

- Competencies: laut-buchstabe, kommasetzung (Kapitel 4); wortbetonung, bindungen, schwache-formen, satzbetonung, intonation-question-tags (Kapitel 5); Stufe 7-8 (Quelle: Auftrag der Orchestrator-Session und `issues/482.md`).
- Form: Lesestücke nach Abschnitt 8 der `konventionen.md`; Sophie 13 bis 14 in England, Chats und kurze Dialoge, ein Bild nur wo es etwas zeigt.
- Audio: nur aufnehmen, was die Stimme richtig spricht; Satzmelodie nicht aufnehmen (Quelle: Auftrag).
- Amount: 7 Fachseiten, 2 Wiederholungsseiten; Kapitel 9-10 (`intonation-haltung`) später.
- Look and feel, Terms: wie die erste Version (Klangpartitur, Lautkarte, Karte, stimmhaft/stimmlos); neu: Betonung, betont/unbetont, Silbe, Schwa, Bindung.


## Plan

<!--
- Map the new content onto the app with the guide's patterns. The creator confirms the plan in one read.
- After the yes you work on your own.
-->

### Tasks

- [x] Load skill `lernapps-content-growth`. Add the tasks of Code as slices, one per competency, in the guide's
      order, one call each: `npx --no -- lernapps plan add --at slices "<task>"`. Say in each which sub-agent may
      write it in parallel, if any.
- [x] Write "Content method": the guide's patterns, figures and components per slice. Anything new: map it as skill
      `lernapps-explainer-design` says, and say why the guide's patterns do not fit.
- [x] Draw a sketch of each new component or interactive exercise, in `.vibe/sketches/`.
- [x] Show the creator, short: goal, new competencies by chapter, slices; in plain words what learners see and do and
      what is new. At most 2 questions.
- [x] **Checkpoint:** confirm the plan and the content method. Stop and wait for an explicit yes. Changes: change
      them, then ask again.
      Creator: Plan ok. Lesestück nur gelesen, nicht vorgelesen. Musterseite laut-buchstabe fertig bauen, Lerner-Check, Checkpoint Musterseite, danach der Rest; Seiten 3-7 erst nach dem Hörurteil; gepusht wird erst nach Erlaubnis.

### Content method

<!-- One line each: the guide's patterns, figures and components used, and where; anything new, what it does and
cannot. Something new goes into the guide in the slice that adds it. -->
<!-- An explainer: per figure, model and component its learning action in two to four sentences
(`explainer-representation-explained`); per page its prerequisites the app does not practise, and which get a recap
page, which a link. -->

Die Muster der ersten Version gelten (Inhaltsführer `.agents/skills/app-content/SKILL.md`): Abschnitte `einstieg`, `neu`, `uebung`, `anwenden`, `weiter`; Übungen `matching`, `single-choice`, `multiple-choice`, `language-task` (gap, write mit `mistakes`), `speaking-task`, `open-task`; Bildfamilie mit `make_partitur.py`; Hörliste; `pruefen.py` und `enden_pruefen.py`. **Neu in diesem Inkrement** (kommt in der Scheibe, die es einführt, in den Inhaltsführer):
- **Seitenform mit Lesestück** (Abschnitt `lesestueck` zwischen `einstieg` und `neu`): Vorwissen-Frage im `einstieg`, Lesestück 120 bis 200 Wörter als Chat, Blog oder Dialog der Figuren (Sophie 13 bis 14, Ellie, Peter, Amir, Mr Hill; Mrs Parker nur im Text), geschrieben als `text`-Blöcke (eine Zeile je Nachricht, Absender fett), Randglossar als `definition`-Blöcke für schwere Wörter, dann Aufgaben in drei Stufen: (1) Verstehen: `single-choice` zum Inhalt, (2) Belegen: `single-choice` oder `language-task`, welche Zeile etwas zeigt (Lesestück steht dann im Text der Aufgabe als `material`), (3) Meinung oder Anwendung: `open-task`. Das Lesestück trägt das Thema der Seite, die Erklärung folgt (`neu`); die Aufgaben fragen aber nicht dieselben Sätze ab wie das Lesestück.
- **Klangpartitur mit mittlerer Zeile** (`partitur-<seite>.svg`): große Punkte (betont) und kleine Punkte (unbetont) über den Silben; Lerninhalt: Punkte zeigen, welche Silbe oder welches Wort lauter, länger und klarer gesprochen wird. Die Legende nennt die Punkte; in Aufgaben zeigt die Partitur nur die Legende. Karten tragen jetzt Silben (zwei Karten für ein Wort, wenn die Silben eigene Laute haben).
- **Umgekehrte Partitur** (Kapitel 4, `laut-buchstabe`): ein Laut (Karte) mit mehreren Schreibungen (Buchstabenkarten darunter).
- Keine Komponente (`prefer-built-in-block`).

Seiten und Figuren (Lernzweck in zwei bis vier Sätzen):
- `richtig-schreiben/laut-buchstabe`: Einstieg: Sophie schreibt „sea“, die Rechtschreibprüfung meldet nichts. Lesestück: Chat Sophie – Ellie über eine Postkarte (see/sea, meet/meat, night). Figur `partitur-laut-buchstabe`: Laute-Karte /iː/ mit den Schreibungen ee, ea, e-e darunter, /aɪ/ mit igh, i-e: zeigt, dass der Laut gleich bleibt und die Schrift wechselt (Richtung Laut → Schrift). Voraussetzungen aus der App: vokale, silent-letters (Link im Text). Übungen: Verstehen, Belegen, Zuordnung Laut ↔ Schreibung, Homophone wählen (single-choice mit Satzzusammenhang), Schreiben aus Lautschrift (`language-task`), Diktat (Hörtext, Kontext entscheidet), Anwenden: `open-task` (eigene Postkarte mit drei Homophon-Paaren).
- `richtig-schreiben/das-brauchst-du` (Recap `englisch/relativsaetze-nicht-notwendig`): Tabelle „Klassenzimmer-Poster · Nicht notwendige Relativsätze“.
- `richtig-schreiben/kommasetzung`: Lesestück: Sophies Blogeintrag „My first term in Millbrook“. Figur: Partitur-Zeile mit einer Pause (Komma) in der Satzmitte; Lernzweck: Ein Komma markiert eine Pause, die man auch hört. Regeln: nach einleitender Zeit-/Ortsangabe, vor und nach nicht notwendigem Relativsatz, in Aufzählungen; kein Komma vor that-Sätzen. Übungen: Kommas setzen (`language-task` write), notwendig oder nicht (single-choice), Satzbau nach Hören (Diktat).
- `betonung-rhythmus-melodie/wortbetonung`: Lesestück: Chat über ein Geschenk (present). Figur: Partitur mit Punkten über Silben (present Nomen: ● ·, Verb: · ●). Übungen: Betonung setzen (single-choice zum Wort), Paare zuordnen (matching Wortart ↔ Betonung), Betonung nach der Lautschrift mit ˈ (Lautkarte: ˈ vor der betonten Silbe) lesen; Hören: nur nach Hörurteil.
- `…/bindungen`: Lesestück: Peter nimmt Sophie auf; Figur: Partitur mit Bogen zwischen zwei Wörtern (turn off → turn‿off), linking r (far‿away). Übungen: Bindestellen finden (multiple-choice), Bogen zuordnen, Sprechen mit eigener Aufnahme.
- `…/schwache-formen`: Lesestück: Backen mit Mrs Parker (Rezept); Figur: Karten mit starker und schwacher Form (and /ænd/ – /ən/); Tabelle „Starke und schwache Formen“; Übungen: wann stark, wann schwach (single-choice), Schwa erkennen, Diktat nur mit Wörtern, die der Kontext festlegt.
- `…/satzbetonung`: Lesestück: Sophies Nachricht; Figur: Partitur mit Punkten über Wörtern, Rhythmus als gleiche Abstände; Übungen: betonte Wörter markieren (multiple-choice), Rhythmus zählen (number), Sprechen.
- `…/das-brauchst-du` (Recap `englisch/question-tags`) und `…/intonation-question-tags`: Lesestück: Chat Sophie – Ellie („Cold today, isn’t it?“); Figur: Partitur oben: Pfeil steigt (echte Frage) oder fällt (Zustimmung erwartet); keine Aufnahme (die Stimme zeigt es nicht), Diktat mit Satzzeichen; Übungen: Situation ↔ Pfeil zuordnen, wählen, Anwenden `open-task`.

Hörtexte: ganze Sätze mit `bf_emma`, mit dem neuen `regen_audio.py` (Fehllaut-Schnitt); Betonungspaare, Bindungen und schwache Formen nur mit Hörurteil der Ersteller:in (Hörprobe 2); Lesestücke nur in kurzen Abschnitten und nur, wenn nichts an Betonung oder Melodie hängt. Kein Hörsatz steht fast wörtlich in Lesestück, Tabelle, Merke oder anderer Übung derselben Seite (`pruefen.py`). Hörliste im Inhaltsführer.

Selbsteinschätzung: je neues Kapitel 1 bis 2 Übungen je Seite ohne Audio (Commit-Phase).


## Code

<!--
- Build locally on the branch, on your own. After each task: `plan done`, then one commit with the work and this
  plan. The hooks check each commit; a failing check is fixed from its message, as skill `lernapps-cli` says.
- What you cannot decide: choose, write it under "Key decisions" with "(guess)", go on.
- The creator asks for a change: say your reading in one sentence first.
-->

### Tasks

- [x] `git switch -c increment/<NN>-<short name>` from `main`. Commit this plan on it.
- [x] Load skill `lernapps-cli`. Update the app as its section "Update" says. Commit the update alone and fix its
      findings before any content. The update replaces the `lernapps-*` skills: read again those you use.
- [x] Load skill `lernapps-explainer` and the content guide.
- [x] Load skill `lernapps-content-questions`. Read whole, with your file tool:
      `.agents/skills/lernapps-explainer/references/blocks.md` and
      `.agents/skills/lernapps-explainer/references/exercises.md`. A foreign language: also
      `references/language-tasks.md` in the same folder. A component in the plan: also `references/components.md`.
- [x] Decide whether the app needs `scope`, as "`scope`" in
      `.agents/skills/lernapps-explainer/references/structure.md` says. Write the choice under "Key decisions".
- [x] Kapitel 4 anlegen (chapter.yaml, app.yaml) und Seite : Lesestück (Sophies Chat mit der Rechtschreibprüfung), Klangpartitur umgekehrt (Laut → Schreibungen), Homophone see – sea; neue Seitenform (Lesestück, Randglossar, drei Aufgabenstufen) im Inhaltsführer beschreiben. Alleine, kein Sub-Agent.
- [x] Wiederholungsseite (#481) und Seite : Lesestück (Sophies Blogeintrag), Kommas als hörbare Pausen, nach einleitendem Adverbial, vor und nach nicht notwendigem Relativsatz. Alleine.
- [x] Kapitel 5 anlegen, Funktion für die mittlere Zeile (Betonungspunkte) in , Seite (nach dem Hörurteil zur Hörprobe 2): Lesestück (Chat über ein Geschenk), present/record, große und kleine Punkte. Alleine.
- [x] Seite (nach dem Hörurteil): Lesestück (Peter nimmt Sophie auf), Konsonant-Vokal-Bindung und linking r (far away). Alleine.
- [x] Seite (nach dem Hörurteil): Lesestück (Backen mit Mrs Parker), and, to, of, for als Schwa-Formen, am Satzende stark. Alleine.
- [x] Seite (nach dem Hörurteil): Lesestück (Sophies Nachricht), Inhaltswörter und Rhythmus. Alleine.
- [x] Wiederholungsseite (#473) und Seite : Lesestück (Chat Sophie und Ellie), Pfeil steigt oder fällt, keine Aufnahme der Melodie. Kapitel 4 und 5 mit Rückblick, der neuen Kapitel (kommt in Commit). Alleine.
<!-- tasks: slices (7 added): one per competency, as written in Plan -->
- [x] **Checkpoint:** the pattern page, after the first slice. A slice in a pattern the app already has: show it to
      the creator and go on. A new pattern: load skill `lernapps-learner-check`, do its learner check, fix what it
      finds, then ask the creator whether the others may follow it, and wait.
      Creator: Ja, mach nach dem Muster weiter mit Gesamtprüfung (Lernenden-Check Kapitel 4 und 5, Sprachprüfung), Inhaltsführer, Selbsteinschätzung und dem Veröffentlichungs-Checkpoint. Push erst nach Erlaubnis der Ersteller:in. (Orchestrator-Session in der Rolle der Ersteller:in)
- [x] Update the content guide so that it describes the app as it is now (`app-content-matches`).
- [x] Run `npx --no -- lernapps check` until it passes.
- [x] Look at every changed screen, at 360 px and on a desktop, as "Look at the app" of skill `lernapps-cli` says.

## Commit

<!--
- Publish with the creator's yes. A push to `main` publishes.
- Open the pull requests (to `main`, to the catalog) without asking: they publish nothing.
-->

### Tasks

- [x] If pages or exercises changed, load skill `lernapps-explainer-self-assessment` and update the self-assessment
      as it says. Commit.
- [x] Load skill `lernapps-github`. Push the branch, open the preview pull request and see its checks to green, as it
      says.
- [x] **Checkpoint:** publish. Show what the increment adds and the preview link. Ask whether it may go online. Stop
      and wait for the yes.
      Creator: Die Ersteller:in hat die Pull Request #2 selbst gemergt (Inkrement 02 ist online); Auftrag danach: Einführungen der Figuren kürzen (Branch increment/03-einfuehrungen-kuerzen).
- [x] Load skill `lernapps-commit`. Publish as skill `lernapps-github` says: the pull request squash-merged into
      `main`, the run of `Pages` watched to its end.
- [x] Open the address the job `deploy` printed and confirm the new content. Never use a derived address.
- [x] (skipped: Die App ist nicht im Katalog gelistet, und der Auftrag der Orchestrator-Session verbietet einen Katalogeintrag.) The app is listed and its entry changes (school years, summary): load skill `lernapps-listing` and write the
      changed entry. Else skip this task.
- [x] Fill the retrospective.
- [x] (skipped: Kein Push auf main ohne Erlaubnis; der Plan-Stand wird mit dem Branch increment/03-einfuehrungen-kuerzen und seiner Pull Request in main gebracht.) Commit this plan on `main` and push it. A push of only `.vibe/` publishes nothing.
- [ ] **Checkpoint:** list. The entry changed: open the pull request to the catalog as skill `lernapps-listing`
      says, without asking first, see it to "bestanden", then show the creator the pull request and its result. The
      entry did not change: tell the creator that the catalog updates the app by itself.
- [ ] If the plan changed since its last push, commit it on `main` and push again.

## Retrospective

<!-- At the end of Commit. Facts, short, no names. Read by review and evals. -->

### Phases reached

<!-- Last phase completed, checkpoints passed. E.g. "commit; confirmed, published". -->

Commit erreicht und abgeschlossen. Bestanden: Recherche, Plan und Inhaltsmethode, Musterseite `laut-buchstabe`, Hörurteil zur Hörprobe 2, Muster für Kapitel 5, Veröffentlichen (die Ersteller:in hat die Pull Request #2 selbst gemergt; der Pages-Lauf auf main war erfolgreich, die Seiten sind unter der Adresse der App erreichbar). Kein Katalogeintrag (Auftrag).

### Creator turns after the plan

<!-- Number of creator messages after the confirmation, topic of each. Target: at most 3. -->

Ein Mensch schrieb nach der Bestätigung zweimal: „Versuch es noch einmal“ (nach einem Ausfall eines Unter-Agenten) und „gehört: passt“ (Hörurteil zur Hörprobe 2). Dazu leitete die Orchestrator-Session (in der Rolle der Ersteller:in) Antworten und Aufträge der Ersteller:in weiter: Muster für Kapitel 5 bestätigt, Vokabelblock statt Wörter-Tabellen, Erlaubnis zum Push („Ja, alle pushen“). Das sind keine eigenen Nachrichten eines Menschen an diese Sitzung.

### Where I had to guess

<!-- Each gap in plan, skills, content guide, messages or answers, and your choice. "None" if none. -->

- Plan: Der Musterseiten-Checkpoint stand nach den Kapitel-5-Seiten noch einmal offen (Aufgaben wurden früher abgehakt); `plan skip` ist bei Checkpoints nicht erlaubt, ich habe die Orchestrator-Session gefragt.
- Lesestück-Glossar: Plan sagte `definition`-Blöcke; später kam der Vokabelblock (Templates 0.14.0); alle Randglossare wurden umgestellt.
- Satzrhythmus („betonte Wörter im gleichen Abstand“): nicht in den geöffneten Quellen, vereinfachte Aussage nach üblicher Lehrbuchlage (im Inhaltsführer vermerkt).
- Komma nach kurzer Einleitung: erst als Pflicht geschrieben, von der Sprachprüfung als freiwillig erkannt; Regel „meist“, längere Einleitungen in den Übungen.
- Tag-Melodie: keine Aufnahme, weil die Stimme sie nicht zeigt; Seite sagt das offen (guess: Text statt Aufnahme).
- Neue Audiodateien aus Kapitel 4 und das Komma-Diktat sind nicht angehört (Prüfstand „offen“); die sieben Sätze der Hörprobe 2 wurden von der Ersteller:in gehört.

## Funde der Prüfungen (Code, Inkrement 02)

Sprachprüfung (Unter-Agent) und Lernenden-Check Kapitel 4 und 5 (Unter-Agent, 360 px und 1280 px) fanden und behoben:
- Komma nach sehr kurzen Einleitungen ist im britischen Englisch freiwillig: Aufgaben mit längeren Einleitungen, Regel „meist“, neues Diktat (After the long lesson, …), Musterlösungen angepasst.
- Altersangaben: Kapitel 4 und 5 nennen die Figuren 13 Jahre alt; die App-Einleitung sagt das jetzt. Peter und die Parkers werden auf den Seiten mit Rolle genannt.
- Begriffe: „stark“ (Form) und „betont“ (Wort) getrennt; /ə/ auf wortbetonung vorab erklärt; Anhängsel „am question tag“ statt „am Tag“.
- Aufgaben: Belegen-Frage auf kommasetzung gegen die Einstiegsfrage getauscht; Tag-Schreibaufgabe nimmt It's und It is an; „Wann will Sophie wirklich eine Antwort?“ ohne strittige Option.
- Bilder: obere Zeile in Kapitel 5 leer statt „kommt später“, Betonungspunkte auch bei den Tag-Bildern.
- Nicht behoben (Vorlagenpunkte): Meldung „Achte auf die Satzzeichen“ bei fehlenden Kommas, Meldung bei Text in einer Zahlaufgabe.
