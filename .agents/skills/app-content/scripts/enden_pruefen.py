#!/usr/bin/env python3
"""Hüllkurve der MP3-Dateien in src/audio/: meldet Dateien, deren letzter lauter Abschnitt sehr kurz ist (Verdacht auf einen
Fehllaut am Ende nach einer Senke). Aufruf im App-Ordner:
~/.cache/lernapps/audio/venv/bin/python .agents/skills/app-content/scripts/enden_pruefen.py [Schwelle] [Frames]
Schwelle: Anteil des Maximums (Vorgabe 0,15); Frames: höchstens so viele 10-ms-Frames (Vorgabe 8) für den letzten Abschnitt.
Das Ergebnis ist nur ein Hinweis: ein Mensch hört die gemeldeten Dateien an (Hörliste, Spalte Prüfstand)."""
import glob, os, subprocess, sys, tempfile
import numpy as np
import soundfile

TH = float(sys.argv[1]) if len(sys.argv) > 1 else 0.15
MAXRUN = int(sys.argv[2]) if len(sys.argv) > 2 else 8
W = 240  # 10 ms bei 24 kHz

rows = []
for f in sorted(glob.glob("src/audio/*.mp3")):
    with tempfile.TemporaryDirectory() as d:
        wav = os.path.join(d, "a.wav")
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", f, "-ar", "24000", "-ac", "1", wav], check=True)
        a, sr = soundfile.read(wav)
    a = a.astype(np.float32)
    env = np.array([np.sqrt(np.mean(a[i:i + W] ** 2)) for i in range(0, len(a) - W + 1, W)])
    n = env / env.max()
    hi = n >= TH
    last = int(np.where(hi)[0][-1])
    s = last
    while s > 0 and hi[s - 1]:
        s -= 1
    run = last - s + 1
    dip = 0
    e = s - 1
    while e >= 0 and not hi[e]:
        dip += 1
        e -= 1
    rows.append((f, run, dip, float(n[s:last + 1].max())))

flagged = [r for r in rows if r[1] <= MAXRUN]
for f, run, dip, peak in flagged:
    print("GEMELDET %s: letzter Abschnitt %d ms nach %d ms Pause, Spitze %.2f" % (f, run * 10, dip * 10, peak))
print("%d Dateien, %d gemeldet" % (len(rows), len(flagged)))
