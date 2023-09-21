# Lottozahlen generieren (6 aus 45)
# - Zahlen sind Zufallszahlen im Bereich von 1 bis 45
# - keine Zahl darf doppelt vorkommen

import random

# for i in range(6):
#     zahl = random.randint(1, 45)
#     list.append(zahl)
#     print(zahl)

# Anlegen einer leere Liste
lotto = []
# 6 Lottozaheln generieren
while len(lotto) < 6:
    # Zufallszahl
    zahl = random.randint(1, 45)
    print(zahl)
    # Doppelte zahlen vermeiden
    if zahl in lotto:
        print("Doppelt")
    else:
        # Zufallszahl zur Liste hinzufügen
        lotto.append(zahl)

# sortieren
lotto.sort()

# Ausgabe
print(lotto)