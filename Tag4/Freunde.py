# 2 Freunde, jeder von beiden hat eine Liste von Freunden(innen)
# Partyeinladung
# - wir nehmen alle Freunde(innen) => Vereinigung von Mengen
# - wir nehmen nur die gemeinsamen Freund(innen) => Durchschnitt von Mengen
# Sets sind Mengen und bieten genau die Funktionen an, die wir benötigen

# Zwei Sets anlegen
mary = { 'Peter', 'Fritz', 'Franz'}
peter = { 'Mary', 'Susi', 'Fritz'}

# - wir nehmen alle Freunde(innen) => Vereinigung von Mengen
# wir nehmen alle Elemente und Streichen doppelte
print(f"Mengen Vereinigung: {mary | peter}")

# - wir nehmen nur die gemeinsamen Freund(innen) => Durchschnitt von Mengen
# Die Elemente müssen in beiden Mengen vorkommen
print(f"Mengen Durschnitt: {mary & peter}")