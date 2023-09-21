"""
Der Computer bestimmt sich eine Zufallszahl zwischen 1 und 100
Der menschliche Spieler gibt eine Zahl ein und erhält die Information
zu groß, zu klein oder richtig
Die Anzahl der Rateversuche wird auf 7 beschränkt
"""

# Modul für Zufallszahlen
import random

# Generieren einer Zufallszahl
zufall = random.randint(1, 100)
# print(zufall)

# Variable Benutzereingabe
rateZahl = 0
# Variable für die Anzahl der Versuche
versuche = 7

# while Schleife => die Anzahl der Durchläufe ist nicht bestimmt
while rateZahl != zufall and versuche > 0:
    # Benutzereingabe
    rateZahl = int(input("Errate Zahl zwischen 1 und 100: "))
    # Anzahl der Versuche runterzählen
    versuche -= 1
    
    # Vergleiche
    if rateZahl > zufall:
        print(f"Die gesuchte Zahl ist kleiner, Übrige Versuche: {versuche}")
    elif rateZahl < zufall:
        print(f"Die gesuchte Zahl ist größer, Übrige Versuche: {versuche}")
    # else:
        # Zahlen sind gleich
        # print("Zahl erraten")
        
# Schleife ist beendet, Ausgabe gewonnen oder verloren
if rateZahl == zufall:
    print("Gewonnen: Zahl erraten, übrige Anzahl Versuche {versuche}")
else:
    print("Verloren, die Zahl wurde mit 7 Versuchen nicht erraten")