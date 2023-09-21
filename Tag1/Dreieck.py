# Berechnung der Hyptenuse (c) eines rechtwinkeligen Dreiecks

# Eingabe sind die beiden Seiten a und b

# c = Wurzel(a hoch 2 + b hoch 2) => a hoch 2 => a ** 2

# import math => Wurzel math.sqrt(...)

import math

# Eingabe

a = float(input("Eingabe a: "))
b = float(input("Eingabe b: "))

# Berechnung

c = math.sqrt(a ** 2 + b ** 2)

# Ausgabe

print(f"Hypotenuse des Dreiecks ist: {c:.2f}")