"""
Man schreibe ein Programm, das Stunden, Minuten, und Sekunden einliest und dann die Zeit in Sekunden umrechnet
umrechnet und ausgibt.
"""


# Eingabe

eS = int(input("Geben Sie die Sekunden an: "))
eMin = int(input("Geben Sie die Minuten an: "))
eH = int(input("Geben Sie die Stunden an: "))


# Konstanten

STUNDEN = 24
MINUTEN = 60
SEKUNDEN = 60

# Berechnung

sErgebnis = eS + (eMin * SEKUNDEN) + (eH * MINUTEN * SEKUNDEN)

# Ausgabe

print(f"Das Ergebnis sind {sErgebnis}s.")