# Eingabe: Abfahrts- und Ankunftszeiten einer Zugfahrt
# Ausgabe: Länge der Zugfahrt (Gesamt Minuten, Stunden:Minuten)

# verwendung Utilmodul.checkInput
import Utilmodul 
# Alias U.checkInput
import Utilmodul as U
# Direkte Import, verwendung checkInput
from Utilmodul import checkInput, STUNDEN, MINUTEN

# Eingabe
shour = checkInput("Start-Zeit Stunden: ", STUNDEN)
smin = checkInput("Start-Zeit Minuten: ", MINUTEN)
ehour = checkInput("Ende-Zeit Stunden: ", STUNDEN)
emin = checkInput("Ende-Zeit Minuten: ", MINUTEN)


# Berechnung

sgesmin = shour * MINUTEN + smin
egesmin = ehour * MINUTEN + emin
if egesmin > sgesmin:
    diffmin = egesmin - sgesmin
else:
    # Korrektur wenn wir über Mitternacht gehen
    diffmin = STUNDEN * MINUTEN - sgesmin + egesmin

# Ausgabe
print(f"Dauer der Zugfahrt in Minuten: {diffmin}")

# Rückrechnung von diffmin in Stunden und Minuten
stunden = int(diffmin/MINUTEN)
# minuten = diffmin - stunden * MINUTEN
# % Modulo Operator => liefert den rest bei einer Division, wenn mit ganzen zahlen gearbeitet wird.
minuten = diffmin % MINUTEN

print(f"Länge der Zugfahrt: {stunden:02d}:{minuten:02d}")