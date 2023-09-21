# Eingabe: Gehalt und Anzahl Kinder
# Ausgabe: Gehalt, Zulage und Auszahlungsbetrag
# 1 Kind: Zulage = 125
# 2 Kinder: Zulage je 110
# bei mehr als 2 Kindern pro Kind 100 (3,4,5 Kinder)
# ab dem 6. Kind keine weiteren Zulagen


# Eingabe

gehalt = float(input("Gehalt: "))
kinder = float(input("Anzahl Kinder: "))
zulage = None

# Berechnung auf der Basis von if, elif und else
# Zusammengesetzte Bedingung: 3 oder 4 oder 5
# case 3 | 4 | 5

match kinder:
    case 0:
        zulage = 0
    case 1:
        zulage = 125
    case 2:
        zulage = kinder * 110
    case 3 | 4 | 5:
        zulage = kinder * 100
    case _:
        zulage = 500


# Ausgabe
print(f"Grundgehalt: {gehalt:.2f} Zulage: {zulage:.2f} Gesamtgehalt: {gehalt+zulage:.2f}")