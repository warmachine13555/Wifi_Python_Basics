# Man schreibe ein Programm, das Schillingbeträge in Euro umrechnet und umgekehrt. Ein Euro entsrpricht
# 13,7603 Schilling.


# Eingabe
calc = int(input("Wollen Sie von (1) Schilling nach Euro oder (2) Euro nach Schilling rechnen? (1, 2): "))
zahl = float(input("Geben Sie den Betrag ein: "))

# Konstanten
SCHILLING_TO_EURO = 1 / 13.7603  # Euro pro Schilling
EURO_TO_SCHILLING = 13.7603  # Schilling pro Euro

# Funktionen
def schilling_to_euro(zahl):
    """Berechnung von Schilling in Euro"""
    return zahl * SCHILLING_TO_EURO

def euro_to_schilling(zahl):
    """Berechnung von Euro in Schilling"""
    return zahl * EURO_TO_SCHILLING

# Berechnungen und Ausgabe
if calc == 1:
    erg = schilling_to_euro(zahl)
    print(f"{zahl} Schilling entsprechen {erg:.2f} Euro")
elif calc == 2:
    erg = euro_to_schilling(zahl)
    print(f"{zahl} Euro entsprechen {erg:.2f} Schilling")
else:
    print("Ungültige Auswahl. Bitte wählen Sie 1 für Schilling nach Euro oder 2 für Euro nach Schilling.")
