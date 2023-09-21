"""
Schreiben Sie ein Programm, das Zahlen einliest und berechnet, ob die eingelesene Zahl eine Primzahl ist oder nicht.
"""


def ist_primzahl(zahl):
    if zahl <= 1:
        return False
    elif zahl <= 3:
        return True
    elif zahl % 2 == 0 or zahl % 3 == 0:
        return False
    i = 5
    while i * i <= zahl:
        if zahl % i == 0 or zahl % (i + 2) == 0:
            return False
        i += 6
    return True

try:
    eingabe = int(input("Geben Sie eine Zahl ein: "))
    if ist_primzahl(eingabe):
        print(f"{eingabe} ist eine Primzahl.")
    else:
        print(f"{eingabe} ist keine Primzahl.")
except ValueError:
    print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.")
