"""
Firma:
- Mitarbeiter (Basisklasse)
- Praktikant (abgeleitet von der Basisklasse)
- Manager (abgeleitet von der Basisklasse)

Klasse Mitarbeiter:

Attribute:
- Name
- Geburtsdatum
- Monatsgehalt

Methoden/Funktionen:
- Konstruktor
- ausgabe
- jahresgehalt() => Monatsgehalt * 12

Klasse Praktikant:

Attribute:
- gleiche Attribute wie Mitarbeiter
- zusätzlich Monate gearbeitet

Methoden/Funktionen:
- gleiche Methoden wie Mitarbeiter

Klasse Manager:

Attribute:
- gleiche Attribute wie Mitarbeiter
- zusätzlich Bonus

Methoden/Funktionen:
- gleiche Methoden wie Mitarbeiter
"""


# Basis-Klasse Mitarbeiter
class Mitarbeiter:
    # Konstruktor
    def __init__(self, name, geburtsdatum, monatsgehalt):
        # Attribute
        self.name = name
        self.geburtsdatum = geburtsdatum
        self.monatsgehalt = monatsgehalt

    # Ausgabe
    def __str__(self):
        return f"Mitarbeiter Name: {self.name}, Geburtsdatum: {self.geburtsdatum}, Monatsgehalt: {self.monatsgehalt} jahresgehalt: {self.jahresgehalt()}"

    # Jahresgehalt
    def jahresgehalt(self):
        return self.monatsgehalt * 14


# Klasse Praktikant
class Praktikant(Mitarbeiter):
    # Konstruktor
    def __init__(self, name, geburtsdatum, monatsgehalt, monate):
        # Attribute
        # 1) Aufruf des Konstruktors der Basisklasse
        super().__init__(name, geburtsdatum, monatsgehalt)
        # 2) Initialisierung der eigenen Attribute
        self.monate = monate

    # Ausgabe
    def __str__(self):
        return f"Praktikant Name: {self.name}, Geburtsdatum: {self.geburtsdatum}, Monatsgehalt: {self.monatsgehalt}, Monate: {self.monate}, jahresgehalt: {self.jahresgehalt()}"

    # Jahresgehalt
    # Wenn eine Funktion gleich wie in der Basiklasse heist,
    # so wird die Funktion der Basisklasse überschrieben
    def jahresgehalt(self):
        return self.monatsgehalt * self.monate


# Klasse Manager
class Manager(Mitarbeiter):
    # Konstruktor
    def __init__(self, name, geburtsdatum, monatsgehalt, bonus):
        # Attribute
        # 1) Aufruf des Konstruktors der Basisklasse
        super().__init__(name, geburtsdatum, monatsgehalt)
        # 2) Initialisierung der eigenen Attribute
        self.bonus = bonus

    # Ausgabe
    def __str__(self):
        return f"Manager Name: {self.name}, Geburtsdatum: {self.geburtsdatum}, Monatsgehalt: {self.monatsgehalt}, Bonus: {self.bonus}, jahresgehalt: {self.jahresgehalt()}"

    # Jahresgehalt
    # Wenn eine Funktion gleich wie in der Basiklasse heist,
    # so wird die Funktion der Basisklasse überschrieben
    def jahresgehalt(self):
        # wir können Methoden der Basisklasse mit super() aufrufen
        # Vorteil: wenn sich die Methode in der Basisklasse ändert, so wird die Änderung automatisch übernommen.
        return super().jahresgehalt() + self.bonus


# Hauptprogramm
peter = Mitarbeiter("Peter", "01.01.2000", 2500)
print(peter)

fritz = Praktikant("Fritz", "01.01.2000", 1000, 3)
print(fritz)

franz = Manager("Hans", "01.01.1990", 5000, 3000)
print(fritz)

# Objekte in Listen speichern
mitarbeiter = [peter, fritz, franz]
for einmitarbeiter in mitarbeiter:
    # es wird die zum Typ des Objektes passende Methode aufgerufen
    print(einmitarbeiter)
