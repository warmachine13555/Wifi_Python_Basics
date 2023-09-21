# Rechner: 4 Grundrechnungsarten

# Eingabe

zahl1 = float(input("Eingabe Zahl1: "))
zahl2 = float(input("Eingabe Zahl2: "))
operator = input("Operator (+-*/): ")


# Rechnung
ergebnis = None
# Verwendung von match/case weil übersichtlicher
match operator:
    case "+":
        ergebnis = zahl1 + zahl2
    case "-":
        ergebnis = zahl1 - zahl2
    case "*":
        ergebnis = zahl1 * zahl2
    case "/":
        if zahl2 == 0:
            print("Division durch null nicht erlaubt!")
        else:
            ergebnis = zahl1 / zahl2
    case _:
        print("Ungültiger Operator")


# Ausgabe
if ergebnis != None:
    print(f"Das Ergebnis ist {ergebnis:.2f}.")