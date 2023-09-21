# Funktionen
# 1) bessere Strukturierung des Programmes
# 2) Wiederverdbarkeit, eine Funktion kann öfter aufgerufen werden
# 3) Variablen und Parameter in Funktionen sind nur innerhalb der Funktion gültig
# und könene nicht mit gleichlautenden Variablen im Hauptprogramm kollidieren

# Definition einer Funktion
def summe(a, b, c = 0):
    print(f"in der Funktion, a: {a} b: {b} c: {c} ")
    sum = a + b + c
    return sum

# Verwendung der Funktion
print(summe(2,3,4))
# Verwendung des Default-Parameters c
print(summe(2,3))
# Verwemdimg von Parameter-Namen
print(summe(c = 3, a = 1, b = 7))