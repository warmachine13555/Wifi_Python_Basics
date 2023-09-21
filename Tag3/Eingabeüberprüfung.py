# Benutzer gibt eine Zahl ein
# Dann erfolgt eine Abfrage (j/n), ob er weitermachen will

while True:
    # Eingabe
    zahl = int(input("Eingabe Zahl:"))
    print(zahl)

    # Weitermachen ja/nein
    weiter = input("Weitermachen (ja/nein): ")
    # Herkömmlich
    # if weiter == "j" or weiter == "J" or weiter == "ja" or weiter == "Ja":
    # if weiter.lower() == "j" or weiter.lower() == "ja":
    # if weiter.lower().startswith("j"):
    if weiter.lstrip().lower().startswith("j"):
        continue
    else:
        break