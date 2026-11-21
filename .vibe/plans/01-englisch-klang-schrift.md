---
# Read by the hooks, the review, the evals. Schema: @lernapps/tooling/guidance/plan-front-matter.v1.schema.json
# Written by `lernapps plan` and the hooks. Never change a key or a value by hand.
# Archetype, null until chosen in Explore. Allowed values: explainer, interactive, quiz.
archetype: explainer
# Current phase. Allowed values: explore, plan, code, commit.
phase: explore
# prePushFailures: failed pre-push runs, written by the hook.
prePushFailures: 0
# failedChecks: failed rules and runs, written by lernapps check and the hooks.
failedChecks: {}
---

# Plan: englisch-klang-schrift, first version

<!--
For you, the assistant. The process is in AGENTS.md; this plan holds the method.
- `npx --no -- lernapps plan next` prints the task to do now, `plan done` ticks it and prints the next one.
- You write only below Goal, Key decisions, Notes, Answers, Entry draft, Content method and Retrospective, in the
  creator's language. Delete the comment of a section once the section is filled.
- Work on the branch `work`, locally: push nothing before Commit.
-->

*Started 2026-11-21. Explore, Plan, Code, Commit.*

## Goal

<!-- 1–2 sentences: what learners do, what they learn. -->

Ich kann englische Laute, Wörter und Sätze verständlich sprechen, die Lautschrift lesen und typische Schreibungen richtig schreiben (Auftrag lernapps/apps#482). Diese erste Version baut nur Stufe 5-6: die Kapitel 1 bis 3 mit 9 Bausteinen. Kinder hören Minimalpaare, sprechen nach, lesen Lautschrift und vergleichen ihre Aufnahme mit dem Original.


## Key decisions

<!-- One line each: decision and reason. Archetype first. Your own choice without the creator: mark "(guess)". -->

- Archetyp `explainer`: Seiten mit Text, Klangpartitur als Bild, Übungen, Diktat und Nachsprechen (Hörtexte und `speaking-task` gibt es nur im Explainer). Quiz und interactive passen nicht. Dazu: Orchestrator-Session (Ersteller:in) im Auftrag 482.
- Strang-App `englisch/aussprache`, Format 2, Sprache Deutsch (`[de]`), britisches Englisch, Anrede „du“.
- Lautschrift: britische Schreibung (/əʊ/, /ɒ/, /ɜː/), Zeichen und Beispielwörter nach Wikipedia „Help:IPA/English“ (nur Fakten); ein Zeichen steht immer auch mit Beispielwort und Ton. (guess)
- Keine Vue-Komponente: Lautkarten sind Tabelle plus `speaking-task` mit je einem Satz je Karte (Anhören ohne Aufnahme-Pflicht), Minimalpaare als Sätze mit `audio`-Aufgaben. „Antippen und Hören“ geht damit nur über den Player des Blocks. (guess, siehe Fragen)
- Minimalwörter stehen nie am Satzende, immer in der Satzmitte vor einem zweisilbigen Schluss („Look, a sheep again.“), damit die Stimme sie nicht abschneidet. (guess)
- Recap-Seiten nur in Kapitel 2 und 3; Kapitel 1 braucht von außen nichts.
- Figuren und Orte wie in `konventionen.md`; kein neuer Ort: die Lautkarten hängen als „Klangpartitur“ im Klassenzimmer neben Zeitstrahl und Satzleiste, Mr Hill bringt sie mit. (guess)


## Notes

<!-- Strand or subject, competencies by chapter (ids), didactic approach, scope, sources and licences, open questions. -->

Strang `englisch/aussprache` (Karte `https://lernapps.net/apps/map/englisch.json`, Fokus `competency`, Strang-App). Neun Lücken, alle Band 5-6, alle `practisedBy` leer.

Kapitel und Karten-Ids:
1. `klaenge` „Englische Laute und Lautschrift“: `lautschrift` (Schritt 1) · `vokale` (2) · `konsonanten-th-w` (2) · `stimmhafte-auslaute` (3) · `silent-letters` (1, steht bewusst zuletzt: Buchstabe und Laut sind dann geklärt, kein `ahead` nötig, die Karte verlangt nichts)
2. `endungen`: Recap [`englisch/plural`, `englisch/simple-past`, `englisch/present-progressive`] aus #475 und #472 · `endungen-s-ed` (4) · `rechtschreibung-endungen` (4)
3. `gespraech`: Recap [`englisch/to-be`, `englisch/simple-present-fragen`, `englisch/fragewoerter`] aus #472 und #473 · `kurzformen` (4) · `intonation-fragen` (5)
Elf Seiten: neun Bausteine, zwei Wiederholungsseiten. Kapitel 4 und 5 sind Stufe 7-8 (Inkremente, nicht jetzt).

Didaktik: Die Klangpartitur trägt den Explainer: ein Bild je Seite mit drei Zeilen (unten Laute, Mitte Betonung, oben Melodie). Kapitel 1 und 2 füllen die untere Zeile, Kapitel 3 führt die obere ein (Pfeil steigt oder fällt), die mittlere bleibt in den Kapiteln 1 bis 3 als leere Legende (Betonung kommt in Stufe 7-8). Kurzformen verschmelzen zwei Lautkarten zu einer. Hello, Millbrook! (`begruessung`) hat eine Lesehilfe (gud-BAI, aim, fenk ju): Kapitel 1 greift sie auf und ersetzt sie durch die Lautschrift (/ɡʊd ˈbaɪ/, /aɪm/, /θæŋk juː/).

Wie lernen die Kinder (je Baustein, ableiten statt ablesen) und welche Fehlvorstellung die Rückmeldung fängt:
- `lautschrift`: Sie lesen Beispielwörter vor dem Zeichen (Ton hören, dann Zeichen zuordnen) und leiten ab: ein Zeichen = ein Laut, die Schreibung sagt es nicht (ʃ in „shoe“ und „nation“). Fehler: Lautschrift mit Buchstaben gleichsetzen (/ʃ/ als „sh“-Buchstaben), :-Länge übersehen, Betonung/Wortlänge verwechseln.
- `vokale`: Minimalpaare hören (ship – sheep, cat – cut), Länge-Zeichen ː ableiten. Fehler: lange und kurze Vokale vertauschen („Schiff“ und „Schaf“), /æ/ wie deutsches ä, /ʌ/ wie a.
- `konsonanten-th-w`: Zungenstellung beschreiben, Minimalpaare (thank – sank, west – vest). Fehler: th als s/f/d, w als v (und umgekehrt), deutsches r.
- `stimmhafte-auslaute`: bed – bet, dog – dock (Auslautverhärtung im Deutschen: „Rad“ = „Rat“); sie erkennen, dass die Länge des Vokals davor mit entscheidet. Fehler: stimmloses Ende wie im Deutschen.
- `silent-letters`: Sie streichen die stummen Buchstaben (grau) in Wörtern und schreiben nach Diktat. Fehler: knife als „k-nife“ sprechen, Schreibung ohne k/w/b.
- `endungen-s-ed`: Regel selbst finden an Gruppen (letzter Laut stimmlos, stimmhaft, Zischlaut/t,d); vorher hören, dann eintragen. Fehler: alle -ed wie „ed“, alle -s wie /s/.
- `rechtschreibung-endungen`: Werkstatt: Wort vor und nach der Endung vergleichen; Regel ableiten (Doppeln bei kurzem Vokal, y→ie, e fällt vor -ing). Fehler: stoped, cryes, makeing.
- `kurzformen`: zwei Lautkarten werden eine, Apostroph steht für das ausgelassene Stück. Fehler: Apostroph an falscher Stelle (do’nt), its/it’s, I’m als „im“.
- `intonation-fragen`: Pfeil steigt bei Ja/Nein-Fragen, fällt bei Aussagen, Aufforderungen und Fragewort-Fragen (Grundregel; Ausnahmen sind Stufe 7-8). Fehler: deutsche Gewohnheit (Frage steigt immer).

Üben: Hören und Schreiben (Diktat mit neuen ganzen Sätzen), Zuordnen Laut ↔ Beispiel, Auswahl mit echten Lernerfehlern, Lücken, Nachsprechen mit `speaking-task` und Selbstbewertung (nichts beurteilt die Aussprache). Nur ganze Sätze als Audio; Einzelwörter nur mit Rückfrage (siehe Audio-Vorbehalt).

Audio-Vorbehalt (an die Ersteller:in): Ich kann die Dateien nicht anhören. Ob `bf_emma` ship/sheep, bed/bet, thank/sank sauber trennt, kann nur ein Mensch mit Englisch prüfen. Plan: jedes Minimalpaar als zwei Sätze mit gleichem Rahmen, Wort in der Satzmitte, Schluss zweisilbig; nach dem Erzeugen mit `regen_audio.py` bearbeitet; die Dateien liste ich mit Text, damit sie jemand anhört, bevor die App veröffentlicht wird. Zwei Dinge sind schon vorher bekannt: Kokoro folgt der Schreibung, nicht der Lautschrift, und spricht /θ/ gelegentlich schwach; und ein Wort wie „thank“ ohne Satz ist unsicher.

Scope: drin sind Laute, Lautschrift (britisch), Endungen -s/-ed (Klang und Schreibung), Kurzformen, Satzmelodie (Grundregel). Nicht drin: Betonung, Bindungen, schwache Formen (Stufe 7-8, #482 Kapitel 5), amerikanische Aussprache und Dialekte (#484), Formen von -s und -ed selbst (#472, #475), Großschreibung (#470), Komma (Kapitel 4 später). Laut-Auswahl: die wichtigsten Zeichen, nicht das ganze IPA: Vokale /iː ɪ e æ ɑː ɒ ɔː ʊ uː ʌ ɜː ə/, Doppellaute /eɪ aɪ ɔɪ əʊ aʊ/, Konsonanten /θ ð ʃ ʒ tʃ dʒ ŋ w v r j/ nur soweit die Beispielwörter sie brauchen. Datenbereich der Wörter: A1/A2-Grundwortschatz; Wörter außerhalb nur wo erklärt.

Quellen (geöffnet am 2026-11-21): en.wikipedia.org „Help:IPA/English“ (Zeichen und Beispielwörter, Hinweis auf britische Schreibung /əʊ/ statt /oʊ/ und auf das nicht gesprochene r nach Vokal), „English plurals“, „Intonation (linguistics)“ und „English orthography“ (Fakten zu Schreibung und Melodie). Nur Fakten, keine Sätze. Nicht geprüft: Oxford- oder Cambridge-Wörterbuch (kein Zugriff), deutsche Wikipedia.

Anschluss an die Vorgänger (gelesen: #473 englisch-saetze-bauen; Struktur gleich übernommen): Seitenabschnitte `einstieg`, `neu`, `uebung`, `anwenden`, `weiter`; Wiederholungsseite `das-brauchst-du` mit Tabelle ohne Übung; Figuren aus `millbrook-klassenzimmer.svg` (#470); Bildfamilie (dort Satzleiste, hier Klangpartitur) mit Skript erzeugt.


## Explore

<!--
- Find out what the app teaches, for whom, how much and how it looks. Ask; write no code, run no `create`.
- An answer counts only in the creator's words under "Answers". At most 2 questions per message, one topic each.
-->

### Tasks

- [x] Check the start: the folder `.agents/skills/lernapps-app` exists (else stop and tell the creator that the folder
      was not started with `init`), and `git branch --show-current` prints `work` (else `git switch -c work`).
- [x] Load skill `lernapps-app`. Tell the creator in two sentences what a lernapps app is and where it will live: at
      their own address, free and public, and once listed as a copy on lernapps.net. Say that the technical part
      (GitHub) comes at the end and that you do it.
- [x] Interview: ask the topics "Goal" and "Learners" of "Answers".
- [x] Load skill `lernapps-map-assignment` and read the learning map of the subject as it says. The creator brings
      the content themselves (material, a word list, the pages): note under "Notes" which competencies of the map it
      covers. Else write the skill's assignment, with its story; the creator's yes answers the topics Content and
      Amount. A subject without a map: skip this task and say so.
- [x] Load skill `lernapps-exercise-patterns` and read its reference for the subject. Note under "Notes" how learners
      will practise what the goal names.
- [x] Choose the archetype as skill `lernapps-app` says: read the README of each archetype in question, then tell the
      creator in plain words what the chosen one can and cannot do. Write the archetype and its reason under "Key
      decisions".
- [x] Run `npx --no -- lernapps skills --archetype <name>` with the chosen archetype. It installs the archetype's
      skills and adds the archetype's tasks to this plan.
- [x] Load skill `lernapps-explainer-design`. An explainer has the look of the runtime: write "fixed by the
      archetype" under the topic "Look and feel" of "Answers".
- [x] Interview: ask every other topic of "Answers", in order. Leave out only a topic that an answer of the creator
      already covers, and note which answer. A topic nobody answered is asked once before you write an assumption
      with "(guess)".
- [x] Load skill `lernapps-content-research` and research as it says. Write under "Notes": the strand or subject, the
      competencies by chapter with their ids, the sources you opened.
- [x] Write under "Notes" which competency goes on which page and which pages form a chapter, as "Map the content" of
      skill `lernapps-explainer-design` says. Per page, name the prerequisites the app does not practise.
- [x] Write under "Notes", one line per competency: how learners get there (they derive it, they do not only read it
      off), and which misconception the feedback catches.
- [x] Write under "Notes" the scope: what is in, what is out and why, the data range (for example "all main-group
      elements", never a silent "1–20"), the languages.
- [ ] **Checkpoint:** research. Show in plain words: the strand or why none, the competencies by chapter, the didactic
      approach, the scope, every "(guess)", the sources and what is unchecked, the archetype and its reason. Stop and
      wait. Changes: change them, then ask again.

### Answers

<!-- The interview: per topic the creator's answer, in their words. Keep the topics. -->

- Goal: what learners do in the app, what they learn.
- Learners: subject, school year, prior knowledge.
- Model and focus: an app of the catalog (https://lernapps.net/apps/llms.txt) as model; what matters most (exercises,
  visualisations, game feel).
- Hurdles: misconceptions and mistakes of the learners; the creator's examples and experiments.
- Content: who writes it (creator, you, from sources); own material (worksheets, tests).
- Amount: how much content in the first version; what comes later.
- Languages: German only, or German and English. Never English only.
- Look and feel: calm like a worksheet, or like a game (colours, praise, effects); dark mode.
- Terms: the creator's words for the main things in the app, used everywhere.
- Finding the app: what teachers and parents would search for.

- Goal: „Ich kann englische Laute, Wörter und Sätze verständlich sprechen, die Lautschrift lesen und typische Schreibungen richtig schreiben.“ (Issue #482, Leitidee)
- Learners: Englisch als erste Fremdsprache, Stufe 5-6 (erstes und zweites Lernjahr, Sophie 11 bis 12 in Millbrook). Vorwissen: Hello, Millbrook! (Lesehilfe), Zeiten (#472), Pronomen (#471), Dinge und Mengen (#475), Sätze bauen (#473). Quelle: Startnachricht der Orchestrator-Session und Issue.
- Model and focus: Hello, Millbrook! und die fertigen Vorgänger (#472, #475, #473, #476) als Muster; wichtig ist die Audio-Qualität („Ohne Ton geht dieser Explainer nicht“).
- Hurdles: Minimalpaare ship – sheep, bed – bet; th, w, v, r; stimmhafte Auslaute; stumme Buchstaben (knife, listen); typische Fehler siehe Notes.
- Content: aus dem Issue und Quellen (Fakten); Beispielsätze eigene, aus dem Alltag der Figuren. Kein eigenes Material.
- Amount: Kapitel 1 bis 3, 9 Bausteine, 11 Seiten (2 Wiederholungsseiten); Kapitel 4 und 5 später als Inkremente.
- Languages: Deutsch (`[de]`), englische Beispiele, britisch.
- Look and feel: fixed by the archetype.
- Terms: Klangpartitur (drei Zeilen), Lautkarte, Lautschrift, Minimalpaar, stummer Buchstabe (grau), „Ausdruck“, Fachbegriffe noun, verb, sentence, tense wie in #470.
- Finding the app: Aussprache Englisch, Lautschrift lesen, Minimalpaare, th aussprechen, Endungen -s -ed aussprechen, Kurzformen, Satzmelodie Frage; Klasse 5 bis 6.


## Plan

<!--
- Map the confirmed content onto the archetype. No new content questions: a gap in the content goes back to Explore.
- The creator confirms the plan in one read. After the yes you work on your own.
-->

### Tasks

- [ ] Map the content as "Map the content" of skill `lernapps-explainer-design` says, and write the result under
      "Content method".
- [ ] Choose a pattern per competency as skill `lernapps-exercise-patterns` says, and add it to "Content method".
- [ ] Add to "Content method" one line per page, as "Engagement" of skill `lernapps-explainer-design` says: the
      opening task, the change of activity, the reward, the story.
- [ ] Add the tasks of Code, each one a piece of work that ends in a commit. First the pattern: one complete page or
      screen, `npx --no -- lernapps plan add --at pattern "<task>"`. Then the others, one call each:
      `npx --no -- lernapps plan add --at pages "<task>"`. Each task says what it builds and what it shows.
- [ ] Draw a sketch of each screen, component or interactive exercise: a static SVG or image, or the steps with what
      learners see after each. Keep the files in `.vibe/sketches/`.
- [ ] Show the creator, short: goal, competencies by chapter, the Code tasks, the sketches, and the content method in
      plain words (what learners see and do, what the app cannot do). At most 2 questions.
- [ ] **Checkpoint:** confirm the plan and the content method. Stop and wait for an explicit yes. Changes: change
      them, then ask again.

### Content method

<!-- One line each: the patterns and where; the figures and how they are made; the data files; each component, what it
checks and what it cannot; how a later agent adds a chapter. It becomes the content guide in Code. -->
<!-- An explainer: per figure, model and component its learning action in two to four sentences
(`explainer-representation-explained`); per page its prerequisites the app does not practise, and which get a recap
page, which a link. -->

## Code

<!--
- Build the app, locally on `work`, on your own. After each task: `plan done`, then one commit with the work and this
  plan. The hooks check each commit; a failing check is fixed from its message, as skill `lernapps-cli` says.
- What you cannot decide: choose, write it under "Key decisions" with "(guess)", go on.
- The creator asks for a change: say your reading in one sentence first, then change every place it holds for
  (`feedback-applied-everywhere`).
-->

### Tasks

- [ ] Load skill `lernapps-cli`. Create the app as its section "Create" says:
      `npx --no -- lernapps create --archetype explainer`.
- [ ] Fill the content guide `.agents/skills/app-content/SKILL.md` from "Notes" and "Content method": every heading,
      no "FILL IN" left. Commit it before any content.
- [ ] Load skill `lernapps-explainer`.
- [ ] Load skill `lernapps-content-questions`. Read whole, with your file tool:
      `.agents/skills/lernapps-explainer/references/blocks.md` and
      `.agents/skills/lernapps-explainer/references/exercises.md`. A foreign language: also
      `references/language-tasks.md` in the same folder. A component in the plan: also `references/components.md`.
- [ ] Decide whether the app needs `scope`, as "`scope`" in
      `.agents/skills/lernapps-explainer/references/structure.md` says. Write the choice under "Key decisions".
<!-- tasks: pattern: the one page or screen that is the pattern for the others -->
- [ ] **Checkpoint:** the pattern page. Load skill `lernapps-learner-check` and do its learner check on the page. Fix
      what it finds. Then show the creator the page and ask whether the others may follow it. Stop and wait. A
      change: change the pattern first.
<!-- tasks: pages: the other pages or screens, after the pattern -->
- [ ] Update the content guide so that it describes the app as built (`app-content-matches`).
- [ ] Run `npx --no -- lernapps check` until it passes.
- [ ] Look at every screen and state, at 360 px and on a desktop, as "Look at the app" of skill `lernapps-cli` says.
      Compare each with its sketch.
- [ ] Do the whole-app check of skill `lernapps-learner-check`. Fix what it finds and write under "Notes" what you
      fixed.

## Commit

<!--
- Put the app on GitHub, publish it with the creator's yes, then list it. A push to `main` publishes.
- Open the pull requests (to `main`, to the catalog) without asking: they publish nothing.
- The creator asked to stop before publishing (a trial): stop here and say so.
-->

### Tasks

- [ ] Load skill `lernapps-explainer-self-assessment`. Add the self-assessment as it says, or write under "Key
      decisions" why the app has none. Commit.
- [ ] Load skill `lernapps-github`. Set up the repository and Pages as it says. Ask for the repository's name and
      every click only the creator can make, in one message.
- [ ] Push `work`, open the preview pull request and see its checks to green, as skill `lernapps-github` says.
- [ ] **Checkpoint:** publish. Show what the app does and the preview link from the comment "Vorschau der App". Ask
      whether it may go online. Stop and wait for the yes.
- [ ] Load skill `lernapps-commit`. Publish as skill `lernapps-github` says: `work` into `main` as one squash commit,
      the run of `Pages` watched to its end.
- [ ] Open the address the job `deploy` printed and confirm that the app shows. Never use a derived address.
- [ ] Load skill `lernapps-listing`. Write the entry under "Entry draft" as it says, with the creator's answer to
      "Finding the app".
- [ ] Fill the retrospective.
- [ ] Commit this plan on `main` and push it: the listing check and the review read it there.
- [ ] **Checkpoint:** list. Open the listing pull request as skill `lernapps-listing` says, without asking first: the
      pull request is the review. See it to "bestanden", then show the creator the pull request and its result.
- [ ] If the plan changed since its last push, commit it on `main` and push again.

### Entry draft

<!-- YAML valid against the entry schema the listing skill names. Only known values, never invented. -->

```yaml
```

## Retrospective

<!-- At the end of Commit, before the listing pull request. Facts, short, no names. Read by review and evals. -->

### Phases reached

<!-- Last phase completed, checkpoints passed. E.g. "commit; confirmed, published". -->

### Creator turns after the plan

<!-- Number of creator messages after the confirmation, topic of each. Target: at most 3. -->

### Where I had to guess

<!-- Each gap in plan, skills, messages or answers, and your choice. "None" if none. -->
