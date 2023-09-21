# Konto-Klasse
#
# Attribute:
# - Name
# - Kontonummer
# - Wert
#
# Methoden/Funktionen
# - Initialisierung(Konstruktor __init__())
# - ausgabe
# - einzahlen(betrag) => Betrag wird zum Wert des Kontos hinzugezählt
# - auszahlen(betrag) => Betrag wird vom Konto abgezogen
# wenn das Konto positiv bleibt => Returnwert True
# Wenn das Konto überzogen wird, so bleibt das Konto unverändert => Returnwert False

# Klasse Konto
class Konto:
    # Konstruktor
    def __init__(self, name, kontonummer, wert=0):
        self.name = name
        self.kontonummer = kontonummer
        self.wert = wert

    # Ausgabe
    def ausgabe(self):
        print(f"Konto: {self.name}, Kontonummer: {self.kontonummer}, Wert: {self.wert}")

    # einzahlen
    def einzahlen(self, betrag):
        self.wert += betrag

    # auszahlen
    def auszahlen(self, betrag):
        if self.wert >= betrag:
            self.wert -= betrag
            return True
        else:
            return False


# Hauptprogramm
# Anlegen eines Objektes
konto1 = Konto("Ben", 12345, 1000)
konto1.ausgabe()
konto1.einzahlen(100)
konto1.ausgabe()
konto1.auszahlen(200000)
konto1.ausgabe()
konto1.einzahlen(2000)
konto1.ausgabe()
konto1.auszahlen(2000)
konto1.ausgabe()
