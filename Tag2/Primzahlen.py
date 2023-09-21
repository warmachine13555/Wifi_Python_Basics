"""
    Eingabe: Start - und Endwert
    Ausgabe: Alle Primzahlen in diesem Bereich
    Primzahl: teilbar nur durch sich selbst und 1
"""


# Eibngabe
untergrenze = int(input("Untergrenze: "))
obergrenze = int(input("Obergrenze: "))

# Schleife von der Unter- zur Obergrenze
for zahl in range(untergrenze, obergrenze + 1):
    # print(zahl)
    # Untersuchung auf Primzahl
    istPrim = True
    for teiler in range(2, zahl):
        # auf teilbarkeit überprüfen
        if zahl % teiler == 0:
            # Teiler gefunden => keine Primzahl, Schleife verlassen
            istPrim = False
            break
    # Nach der Schleife Prüfung auf Teilbarkeit
    if istPrim == True:
        print(zahl)