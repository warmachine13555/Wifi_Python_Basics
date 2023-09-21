# Obejektorientierung
# Klasse Uhrzeit
#
# Daten/Attribute
# - Stunden
# - Minuten
#
# Funktionen/Methoden
# - Initialisierung
# - Ausgabe
# - addierenMin
# - addierenUhrzeit

# Konstanten
ANZMIN = 60
ANZSTD = 24

# Klassen Uhrzeit
# Klasse ist der Bauplan, nachdem Objekte angelegt werden können
# wir definieren uns einen Python-Datentyp
class Uhrzeit:
    # Konstruktor => eine Funktion, die beim Anlegen des Obektes aufgerufen wird
    # self ist wichtig bei jeder Funktion, Referenz auf das eigene Objekt
    def __init__(self, std=0, min=0):
        # Setzen der Attribute/= Daten des Obekjektes
        self.stunden = std
        self.minuten = min
        # Hinzufügen eines weiteren Attributs
        self.gesmin = std * ANZMIN + min

    def ausgeben(self):
        print(f"Uhrzeit: {self.stunden:02d}:{self.minuten:02d}")

    # __str__ ist eine Funktion, die beim Print augferufen wird
    def __str__(self):
        # Rückgabe ist ein String, der das Objekt beschreibt
        return f"Uhrzeit: {self.stunden:02d}:{self.minuten:02d}"

    def addiereMin(self, min):
        # Addieren der Minuten zu den Gesamtminuten
        self.gesmin += min
        # Korrektur der Tagesgrenze
        self.gesmin %= ANZSTD * ANZMIN
        # Stunden korrigieren
        self.stunden = int(self.gesmin / ANZMIN)
        # Minuten korrigieren
        self.minuten = self.gesmin % ANZMIN

    # zeit ist ein Uhrzeit-Objekt
    def addierenUhrzeit(self, zeit):
        # wir addieren die Gesamtminuten des Zeitobjektes zu unserem Objekt
        self.gesmin += zeit.gesmin
        # Korrektur der Tagesgrenze
        self.gesmin %= ANZSTD * ANZMIN
        # Stunden korrigieren
        self.stunden = int(self.gesmin / ANZMIN)
        # Minuten korrigieren
        self.minuten = self.gesmin % ANZMIN

    # Ende Klasse Uhrzeit

