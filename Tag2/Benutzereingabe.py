"""
Benutzereingabe mit Prüfung
Eingabe eines Monats im Bereich von 1 .. 12
Bei einem Fehler soll die Eingabe wiederholt werden
"""

monat = 0
# Schleife, solange wiederholen, bis die Eingabe richtig ist
while monat < 1 or monat > 12:
    # Benutzereingabe
    monat = int(input("Eingabe Monat (1..12): "))
    if monat < 1 or monat > 12:
        print(f"Falsche Eingabe, Monat: {monat} war außerhalb des Bereiches von 1..12")
else:
    print(f"Die Eingabe des Monats war: {monat}")     
    
# Nach der Schleife
# print(f"Die Eingabe des Monats war: {monat}")
