# Funktion zur Ausgabe der Liste
# es erfolgt keine Kopie der Daten, sondern es wird eine Referenz übergeben
# Vorteil: wenige Speicherbedarf und Schnelligkeit
def ausgabe(liste):
    # end ist ein Zusatzparameter für Print und wird statt einer neuen Zeile ausgegeben
    print("Obst: ", end=" ")
    # Schleife über die Liste, Index-Zugriff
    # for i in range(len(liste)):
    #   print(f"{liste[i]}", end=" ")
    # Alternative für Schleifen, Iteration
    for frucht in liste:
        print(f"{frucht}", end=" ")
    # Nach der Schleife, jetzt soll eine neue Zeile erzeugt werden
    print()

# Definition einer Liste
obst = ["Apfel", "Birne", "Kiwi"]
print(obst)
ausgabe(obst)

# Listen sind dynamisch => Elemente sind veränderbar
# Hinzufügen am Ende
obst.append("Banane")
ausgabe(obst)

# Beliebig in der Liste einfügen
obst.insert(1, "Kirsche")
ausgabe(obst)

# sortieren
# Texte werden alphabetisch sortiert ["eins","zwei","drei"] => ["drei","eins","zwei"]
# Zahlen werden numerisch sortiert [2,1,3] => [1,2,3]
obst.sort()
ausgabe(obst)
obst.reverse()
ausgabe(obst)

# Überprüfung
if "Banane" in obst:
    print("Banane vorhanden")
    # an welcher Stelle in der Liste komm die Banane vor
    print(obst.index("Banane"))

# Element löschen
obst.pop(1)
ausgabe(obst)
obst.remove("Apfel")
ausgabe(obst)

# Liste leeren
obst.clear()
ausgabe(obst)