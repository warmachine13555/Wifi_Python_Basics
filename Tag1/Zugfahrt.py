# Eingabe: Abfahrts- und Ankunftszeiten einer Zugfahrt
# Ausgabe: Länge der Zugfahrt (Gesamt Minuten, Stunden:Minuten)

# Konstante
MINUTEN = 60
STUNDEN = 24

# Eingabe
shour = int(input("Start-Zeit Stunden: "))
if shour < 0 or shour >= STUNDEN:
    print("Fehler!")
    exit()
smin = int(input("Start-Zeit Minuten: "))
if smin < 0 or smin >= MINUTEN:
    print("Fehler")
    exit()
ehour = int(input("Ende-Zeit Stunden: "))
if ehour < 0 or ehour >= STUNDEN:
    print("Fehler!")
    exit()
emin = int(input("Ende-Zeit Minuten: "))
if emin < 0 or emin >= MINUTEN:
    print("Fehler!")
    exit()

# Berechnung

sgesmin = shour * MINUTEN + smin
egesmin = ehour * MINUTEN + emin
diffmin = egesmin - sgesmin

# Ausgabe
print(f"Dauer der Zugfahrt in Minuten: {diffmin}")

# Rückrechnung von diffmin in Stunden und Minuten
stunden = int(diffmin/MINUTEN)
# minuten = diffmin - stunden * MINUTEN
# % Modulo Operator => liefert den rest bei einer Division, wenn mit ganzen zahlen gearbeitet wird.
minuten = diffmin % MINUTEN

print(f"Länge der Zugfahrt: {stunden:02d}:{minuten:02d}") 