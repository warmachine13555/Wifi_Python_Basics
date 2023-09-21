# Modul, das Funktionen und Konstanten enthält

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