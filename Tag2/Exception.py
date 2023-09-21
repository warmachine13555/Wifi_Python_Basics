# Beispiel zum Exception handling

try:
    # Produktivcode
    zahl1 = float(input("Zahl1: "))
    zahl2 = float(input("Zahl2: "))
    ergebnis = zahl1/zahl2
    print(f"Ergebnis: {ergebnis}")


except ValueError as e:
    # dieser Fehler tritt in einem der beiden float-Funktionen auf
    print("Falsche Eingabe, nur Zahlen sind zulässig")
    # die Variable e enthält Zusatzinformationen
    print(e)
except ZeroDivisionError as e:
    # dieser Fehler tritt bei der Division durch Null auf
    print("Fehler, division durch Null")
    # die Variable e enthält Zusatzinformationen
    print(e)
except:
    # Fehlercode
    print("Allgemeiner Fehler")

# Nach dem Fangen des Fehlers lauft das Programm hier weiter
print("Ende")