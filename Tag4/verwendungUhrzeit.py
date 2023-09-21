# import Uhrzeit
from Uhrzeit import Uhrzeit, ANZMIN

# Hauptprogramm: verwenden der Klasse Uhrzeit

# Anlegen eines Objektes
beginZeit = Uhrzeit(10, 20)
beginZeit.ausgeben()
# Zugriff auf die Attribute
print(beginZeit.stunden)
# Bessere Methode für Ausgabe
print(beginZeit)
beginZeit.addiereMin(70)
print(beginZeit)
beginZeit.addiereMin(14*ANZMIN)
print(beginZeit)

zeit = Uhrzeit(5, 20)
beginZeit.addierenUhrzeit(zeit)
print(beginZeit)