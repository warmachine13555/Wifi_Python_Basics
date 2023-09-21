# writeFile() ... der Benutzer gibt Text ein, der wird in einem File abgespeichert
# readFile() ... Auslesen und Ausgaben des Fileinhaltes
# Hauptprogramm: ruft die beiden Funktionen auf


def writeFile(path):
    # File zum Schreiben öffnen
    file = open(path, "w", encoding="UTF8")

    # Schleife mit Benutzereingaben
    while True:
        text = input("Eingabe (Ende mittels <return>): ")
        if len(text) > 0:
            # in das File schreiben
            # \n => New Line
            file.write(text + "\n")
        else:
            break
    file.close()

def readFile(path):
    file = open(path, "r", encoding="UTF8")

    #Schleife zum Lesen des Fileinhaltes
    text = None
    while text != "":
        # Zeile aus dem File lesen
        text = file.readline()
        # Wegfiltern von New Line => slicing
        text = text[:-1]
        # Ausgabe
        print(text)
    # Files sollten immer geschlossen werden
    file.close()

# Hauptprogramm
# Exeptionhandling empfehlenswert:
# - Fehler wegen fehlende Berechtigungen
# - Fehler wegen falschen Dateinamen (Directory oder File existiert nicht)

try:
    # relativer Pfad => im gleichen Verzeichnis ist das file zu finden
    path = "Text.txt"
    # Alternativ sind absolute Pfade
    # C:\Users\tp\Documents\Python\PythonBasis2309\Tag3
    writeFile(path)
    readFile(path)

except Exception as e:
    print(f"Fehler: {e}")