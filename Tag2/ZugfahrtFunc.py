# Eingabe: Abfahrts- und Ankunftszeiten einer Zugfahrt
# Ausgabe: Länge der Zugfahrt (Gesamt Minuten, Stunden:Minuten)

# Funktion
def checkInput(text, limit):
    """
    checkInput: Eingabe durch den Benutzer und Überprüfung der Werte

    Args:
        text (str): Text für den Benutzer, damit er weis, was er eingeben soll
        limit (int): mit limit wird die Grenze für die Eingabe definiert

    Returns:
        int: Geprüfte Eingabe des Benutzers
    """
    zahl = limit
    # Kontrolle des Zahlenbereiches
    while zahl < 0 or zahl >= limit:
        try: 
            # Eingabe des Benutzers
            zahl = int(input(text))
            if zahl < 0 or zahl >= limit:
                print(f"Ungültige Eingabe, Bereich geht von 0 bis {limit-1}")
        except:
            #ValueException
            print("Ungültige Eingabe, nur Zahlen und keine Buchstaben sind erlaubt!")
    #Rückgabe der geprüften Benutzereingabe
    return zahl

# Konstante
MINUTEN = 60
STUNDEN = 24

# Eingabe
shour = checkInput("Start-Zeit Stunden: ", STUNDEN)
smin = checkInput("Start-Zeit Minuten: ", MINUTEN)
ehour = checkInput("Ende-Zeit Stunden: ", STUNDEN)
emin = checkInput("Ende-Zeit Minuten: ", MINUTEN)


# Berechnung

sgesmin = shour * MINUTEN + smin
egesmin = ehour * MINUTEN + emin
if egesmin > sgesmin:
    diffmin = egesmin - sgesmin
else:
    # Korrektur wenn wir über Mitternacht gehen
    diffmin = STUNDEN * MINUTEN - sgesmin + egesmin

# Ausgabe
print(f"Dauer der Zugfahrt in Minuten: {diffmin}")

# Rückrechnung von diffmin in Stunden und Minuten
stunden = int(diffmin/MINUTEN)
# minuten = diffmin - stunden * MINUTEN
# % Modulo Operator => liefert den rest bei einer Division, wenn mit ganzen zahlen gearbeitet wird.
minuten = diffmin % MINUTEN

print(f"Länge der Zugfahrt: {stunden:02d}:{minuten:02d}") 