# Eingabe: Gahlt und Anzahl Kinder
# Ausgabe: Gehalt, Zulage und Auszahlungsbetrag
# 1 Kind: Zulage = 125
# 2 Kinder: Zulage je 110
# bei mehr als 2 Kindern pro Kind 100 (3,4,5 Kinder)
# ab dem 6. Kind keine weiteren Zulagen

# Eingabe

gehalt = float(input("Gehalt: "))
kinder = float(input("Anzahl Kinder: "))
zulage = 0

# Berechnung auf der Basis von if, elif und else

if kinder == 1:
    zulage = 125
elif kinder == 2:
    zulage = kinder * 110
elif kinder >= 3 and kinder <= 5:
    zulage = kinder * 100
elif kinder >= 6:
    # Kinder 6,7,8,...
    zulage = 500

# Ausgabe
print(f"Grundgehalt: {gehalt:.2f} Zulage: {zulage:.2f} Gesamtgehalt: {gehalt+zulage:.2f}")