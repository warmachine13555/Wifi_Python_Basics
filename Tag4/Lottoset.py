# Lottozahlen 6 aus 45 
# Verwendung von Set, weil hier nur eindeutige Elemente drinnen sind

import random

# Leeres Set
lotto = set()

# Schleife bis 6 Zahlen gefunden
while len(lotto) < 6:
    # Zufallszahl
    zahl = random.randint(1, 45)
    # Set sorgt bei add dafür, dass keine Zahlen doppelt vorkommen
    lotto.add(zahl)
    
# Sortierung leider nicht möglich
print(lotto)