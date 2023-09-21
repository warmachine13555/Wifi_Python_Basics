"""
Eingabe: Zahlenfolge von ganzen Zahlen (Ende der Folge ist die Eingabe 0)
Ausgabe: Anzahl der gültigen Zahlen, Summe und der Durchschnitt
10,20,30,0
3,60,20
"""

zahl = None
anzahl = 0
summe = 0

# Eingabe
while zahl != 0:
    zahl = int(input(f"Geben Sie eine ganze Zahl ein (0 zum Beenden): "))
    if zahl != 0:    
        anzahl += 1 # Berechne Anzahl Zahlen eingegeben
        summe += zahl # Berechne Summe

# Berechne den Durchschnitt
if anzahl > 0:
    durchschnitt = summe / anzahl
else:
    durchschnitt = 0

# Ausgabe
print(f"Anzahl der gültigen Zahlen: {anzahl} Summe der Zahlen: {summe} Durchschnitt der Zahlen: {durchschnitt}")
