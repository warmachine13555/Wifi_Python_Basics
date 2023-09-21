# Den Inhalt eines Directories auslesen
# Für jedes File im Directory Information darstellen

import os


# Funktion zum Zeilenzählen, da es keine fertige Funktion gibt
def lineCounter(filename):
    # file öffnen
    file = open(filename, "r")

    # Zeilenzählen
    lines = file.readlines()

    # file schließen
    file.close()

    # rückgabe der Anzahl von Zeilen
    return len(lines)


try:
    # Inhalt des aktuellen directories wird ausgelesen
    # . ist das aktuelle Directory
    # listdir(".") => relativer Pfad
    for file in os.listdir("."):
        # Ausgabe filename
        print(file)
        # wor wollen nur Informationen von Pythonfiles
        if file.endswith(".py"):
            # Ausgabe von mehr Information
            print(f"Filegröße: {os.path.getsize(file)} Anzahl Zeilen: {lineCounter(file)}")
            # os.stat liefert viele Informationen wie Zeitstempel, Rechte, ...
            print(os.stat(file))

except Exception as e:
    print(f"Fehler: {e}")