"""
Eingabe: Anfangskapital, Zinssatz und Veranlagungsdauer
Ausgabe: Endkapital und die gutgeschriebenen Zinsen
"""

# Eingabe
anfangsKapital = float(input("Anfangskapital: "))
zinsen = float(input("Zinssatz: "))
dauer = int(input("Veranlagungsdauer: "))

# dauer = float(input("Veranlagungsdauer: "))
# if dauer - int(dauer) > 0:
#     print("Fehler, kommastellen eingeben")

# Berechnung
endKapital = anfangsKapital
# For-Schleife nach der Anzahl der Jahre Veranlagungsdauer
for jahr in range(1,dauer+1):
    # Berechnung
    gewinn = endKapital * zinsen / 100
    endKapital += gewinn
    # Ausgabe
    print(f"Jahr: {jahr} gutgeschriebene Zinsen: {gewinn:.2f} Endkapital: {endKapital:.2f}")
    
# Kontrolle mit einer Formel: Verwendung der Potenz
print(f"Endkapital: {anfangsKapital * ((100+zinsen)/100) ** dauer:.2f}")
    