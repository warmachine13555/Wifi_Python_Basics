"""
Firma:
- Mitarbeiter (Basisklasse)
- Praktikanten (abgeleitet von der Basisklasse)
- Manager (abgeleitet von der Basisklasse)

Klasse Mitarbeiter:

Attribute:
- Name
- Geburtsdatum
- Monatsgehalt

Methoden/Funktionen
- Konstruktor
- ausgabe
- jahresgehalt()

Klasse Praktikant:

Attribute:
- gleich wie Mitarbeiter
- zusätzlich Monate gearbeitet

Methoden:
- gleich wie Mitarbeiter

Klasse Manager:

Attribute:
- gleich wie Mitarbeiter
- zusätzlich Bonus

Methoden:
- gleich wie Mitarbeiter

"""

# Basisklasse
class Mitarbeiter:
    # Konstruktor
    def __init__(self, name, gebdat, mgehalt):
       # Attribute
       self.name = name
       self.gebdat = gebdat
       self.mgehalt = mgehalt 
       
    # Ausgabe
    def __str__(self):
        return f"Mitarbeiter Name: {self.name} Geburtsdatum: {self.gebdat} Monatsgehalt: {self.mgehalt} Jahresgehalt: {self.jahresgehalt()}"
    
    def jahresgehalt(self):
        return 14 * self.mgehalt

# Klasse Praktikant
class Praktikant(Mitarbeiter):
    # Konstruktor
    def __init__(self, name, gebdat, mgehalt, monate):
        # 1) Aufruf des Konstruktors der Basisklasse
        super().__init__(name, gebdat, mgehalt)
        # 2) Init von zusätzlichen Attributen
        self.monate = monate
        
    # Ausgabe
    def __str__(self):
        return f"Praktikant Name: {self.name} Geburtsdatum: {self.gebdat} Monatsgehalt: {self.mgehalt} Monate: {self.monate} Jahresgehalt: {self.jahresgehalt()}"
    
    # Jahresgehalt
    # Wenn eine funktion gleich wie in der Basisklasse heist, 
    # so überschreiben (ersetzen) wir die Funktion der Basisklasse
    def jahresgehalt(self):
        return self.monate * self.mgehalt
    
# Manager
class Manager(Mitarbeiter):
    # Konstruktor
    def __init__(self, name, gebdat, mgehalt, bonus):
        # 1) Aufruf des Konstruktors der Basisklasse
        super().__init__(name, gebdat, mgehalt)
        # 2) Init von zusätzlichen Attributen
        self.bonus = bonus
    
    # Ausgabe
    def __str__(self):
        return f"Manager Name: {self.name} Geburtsdatum: {self.gebdat} Monatsgehalt: {self.mgehalt} Bonus: {self.bonus} Jahresgehalt: {self.jahresgehalt()}"
    
    # Jahresgehalt
    def jahresgehalt(self):
        # wir können Methoden der Basisklasse mit super() aufrufen
        # Vorteil => Änderungsfreundlichkeit, es gibt nur eine Stelle für Änderungen
        return super().jahresgehalt() + self.bonus
    
# Manager
    
# Hauptprogramm
peter = Mitarbeiter("Peter","2000-01-01", 2500)
print(peter)
fritz = Praktikant("Fritz", "2005-02-02", 1000, 3)
print(fritz)
franz = Manager("Franz", "1990-03-03", 5000, 3000)
print(franz)

# Objekte in Listen speichern
mitarbeiter = [peter, fritz, franz]
for einmitarbeiter in mitarbeiter:
    # es wird die zum Typ des Objektes passende Methode aufgerufen
    print(einmitarbeiter)