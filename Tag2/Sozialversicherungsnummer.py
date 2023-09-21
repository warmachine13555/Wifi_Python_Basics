"""
Eingabe: Sozialversicherungsnummer (z.B 3285171076)
Ausgabe: gültig/nicht gültig
http://www.pruefziffernberechnung.de/V/VSNR-AT.shtml
"""

# Eingabe
num = int(input("Sozialversicherungsnummer: "))

# Variablen für die Prüfung
summe = 0
pruefziffer = 0
counter = 0

# Schleife, Verarbeitung der einzelnen Zeichen
while num != 0:
    # abspalten der letzten Ziffer
    ziffer = num % 10
    # print(ziffer)
    # Num durch 10 teilen, damit ist die letzte Ziffer weg
    num = int(num/10)
    # counter erhöhen
    counter += 1
    
    # Berücksichtigung der Gewichtung
    # 3, 7, 9, 5, 8, 4, 2, 1, 6
    match counter:
        case 1:
            summe += ziffer * 6
        case 2:
            summe += ziffer * 1
        case 3:
            summe += ziffer * 2
        case 4:
            summe += ziffer * 4
        case 5:
            summe += ziffer * 8
        case 6:
            summe += ziffer * 5
        case 7:
            # Prüfziffer merken
            pruefziffer = ziffer
        case 8:
            summe += ziffer * 9
        case 9:
            summe += ziffer * 7
        case 10:
            summe += ziffer * 3
        case _:
            print("Eingabe ist zu lange!")
            break

# nach der Schleife            
print(f"Summe: {summe} Prüfziffer: {pruefziffer}")

# Prüfung
if summe % 11 == pruefziffer:
    print("Nummer ist gültig")
else:
    print("Nummer ist ungültig")
