"""
Schreiben Sie ein Programm, das Temperaturwerte einliest (beliebig viele; Ende der Eingabe durch 1000) und dann das Minimum, das Maximum und den Durchschnitt aller eingegebenen Temperaturwerte berechnet.
"""

# modules
from math import inf

# var
anzahl = 0
temp = 0
tempges = 0
tempmax = 0
tempmin = inf

# Eingabe/Berechnung
while temp != 1000:
    temp = float(input("Geben Sie die Temperaturwerte ein (mit Eingabe 1000 beenden Sie die Eingabe) : "))
    anzahl += 1
    tempges += temp
    tempmed = tempges / anzahl
    if temp > tempmax:
        tempmax = temp
    if temp < tempmin:
        tempmin = temp

# Ausgabe
print(f"Temperaturminimum : {tempmin}°, Temperaturmaximum : {tempmax}°, Temperaturdurchschnitt : {tempmed}°")