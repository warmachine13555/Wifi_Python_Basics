# Zusammengesetzte Bedingungen

zahl = 22

# Abfrage ob die Zahl im Bereich ist 10,...20
if zahl >= 10:
    if zahl <= 20:
        # todo im Bereich
        print("Im Bereich")
    else :
        # fehler außerhalb des Bereiches
        print("Außerhalb des Bereiches")

# Zusammengesetze Bedingungen
# besserer und übersichtlicherer Stil
# bei and müssen beide Bedingungen erfüllt sein
if zahl >= 10 and zahl <=20:
    print("Im Bereich")
else :
    # fehler außerhalb des Bereiches
    print("Außerhalb des Bereiches")
    
# außerhalb des Bereiches 10,...20
# bei or reicht es, dass eine Bedingung erfüllt ist.
if zahl < 10 or zahl > 20:
    print("Außerhalb")
else :
    print("Innerhalb")