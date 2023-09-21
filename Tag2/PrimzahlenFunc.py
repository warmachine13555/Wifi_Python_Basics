"""
Eingabe: Start- und Endwert
Ausgabe: alle Primzahlen in diesem Bereich
Primzahl: teilbar nur durch sich selbst und 1
"""

# Funktion zur Prüfung einer Zahl auf Prim
def istPrim(zahl):
    # Untersuchung auf Primzahl
    for teiler in range(2, zahl):
        # auf teilbarkeit überprüfen
        if zahl % teiler == 0:
            # Teiler gefunden => keine Primzahl, Schleife verlassen
            return False
    # Nach der Schleifer Prüfung auf Teilbarkeit
    return True

# Eingabe
untergrenze = int(input("Untergrenze: "))
obergrenze = int(input("Obergrenze: "))

# Schleife von der Unter- zur Obergrenze
for zahl in range(untergrenze, obergrenze + 1):
    # print(zahl)
    
    # Funktionsaufruf
    if istPrim(zahl):
        print(zahl)