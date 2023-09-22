#import Uhrzeit
from Uhrzeit import Uhrzeit, ANZMIN

# Hauptprogramm: Verwendung der Klasse

# Anlegen eines Objektes
beginZeit = Uhrzeit(10,20)
beginZeit.ausgeben()
# Zugriff auf ein Attribut
print(beginZeit.stunden)
# Bessere Methode für Ausgabe
print(beginZeit)
beginZeit.addierenMin(70)
print(beginZeit)
beginZeit.addierenMin(14*ANZMIN)
print(beginZeit)

zeit = Uhrzeit(5,20)
beginZeit.addierenUhrzeit(zeit)
print(beginZeit)