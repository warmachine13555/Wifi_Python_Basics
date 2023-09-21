# der Benutzer gibt eine Zeit im Format HH:MM:SS ein
# Eingabeschleife, solange, bis der Benutzer eine gültige Uhrzeit eingegeben hat.

while True:
    # Benutzereingabe String
    text = input("Eingabe Uhrzeit (HH:MM:SS): ")
    # Split in einzelteile
    teile = text.split(":")
    #Prüfung auf drei Teile
    if len(teile) != 3:
        print("Fehler: Uhrzeit (HH:MM:SS) eingeben")
        # wir wollen in der Schleife bleiben,
        # aber ein sprung zum Beginn der Schleife ist notwendig
        continue

    # Umwandlung in Zahlen
    stunden = int(teile[0])
    minuten = int(teile[1])
    sekunden = int(teile[2])

    # Prüfung
    if stunden > 23:
        print("Stunden zu groß")
        continue
    if minuten > 59:
        print("Minuten zu groß")
        continue
    if sekunden > 59:
        print("Sekunden zu groß")
        continue

    # Zeit ist korrekt
    print(f"Zeit: {stunden:02d}:{minuten:02d}:{sekunden:02d}")
    # Schleife verlassen
    break

print("nach der Schleife")