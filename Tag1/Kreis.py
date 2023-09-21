# Berechnung der Fläche eines Kreises

# Importieren des Mathematik-Modules
import math

# Definition Konstanten
PI = 3.14159

# Eingabe

radius = float(input("Eingabe des Radius: "))

# Berechnung flaeche = radius * radius * PI

# normal berechnen
# flaeche = radius * radius * 3.14159

# Konstanten Definiert
# flaeche = radius * radius * PI

# Potentieren  
# flaeche = radius ** 2 * PI

# math modul importiert
flaeche = radius * radius * math.pi


# Ausgabe

print(f"Die Fläche des Kreises ist: {flaeche:.2f}")