# Tupel
# (1,2)

# Funktion zum Dividieren
# Parameter: zwei Zahlen
# Returnwert: Tupel
# - Division ist gutgegangen (c, True)
# - division ist fehlgeschlagen (None, False)

def division(a,b):
    # Exception fangen
    try:
        c = a/b
        # Division ist gutgegangen
        return (c, True)
    except:
        # Division ist nicht gutgegangen
        return (None, False)
    
# der Benutzer gibt die Zeit im Format HH:MM:SS ein
# return ist ein tupel mit stunden, minuten und sekunden
def zeiteingabe():
    while True:
        # Benutzereingabe
        text = input("Eingabe Uhrzeit(HH:MM:SS): ")
        # split
        # ergebnis ist eine Liste: index0 => stunden, index1 => minuten, index2 => sekunden
        teile = text.split(":")
        # Prüfung sind es drei Teile
        if len(teile) != 3:
            print("Fehler: Uhrzeit(HH:MM:SS) eingeben")
            # eingabe soll wiederholt werden, in schleife bleiben => continue
            continue
        # umwandlung in zahlen
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
        # hier ist die Zeit korrekt => Ausgabe
        # print(f"Zeit: {stunden:02d}:{minuten:02d}:{sekunden:02d}")
        # Rückgabe Tupel
        return stunden, minuten, sekunden

# Hauptprogramm
print(division(2, 3))
print(division(2, 0))
# zeittupel = zeiteingabe()
# stunden = zeittupel[0]
# minuten = zeittupel[1]
# sekunden = zeittupel[2]
# Bessere Möglichkeit => direktes Anlegen und Zuweisung von Variablen
stunden, minuten, sekunden = zeiteingabe()
print(f"Zeit: {stunden:02d}:{minuten:02d}:{sekunden:02d}")