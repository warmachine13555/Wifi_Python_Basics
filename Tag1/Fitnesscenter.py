# Fitnesscenter: Berechnung der Jahresgebühr
# Basispreis = 300
# unter 5 Jahren Mitgliedschaft + 100
# ab 10 Jahren - 50
# rest - 10

# Eingabe
preis = 300
jahre = int(input("Jahre Mitglied: "))

# Bestimmung der Jahresgebühr
if jahre < 5:
    # Bereich 0,1,2,3,4
    # Langschreibweise
    # preis = preis + 100
    # Kurzschreibweise
    preis += 100
elif jahre >= 10:
    # Bereich 10,11,12,13,14,...
    preis -= 50
else:
    # Bereich 5,6,7,8,9
    preis -= 10

# Ausgabe der Jahresgebühr
print(f"Der Preis beträgt {preis}€.")