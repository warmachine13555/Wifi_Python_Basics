# Der Benutzer gibt nacheinander Namen ein
# Die Namen werden in einer Liste gespeichert
# Beendigung mittels Eingabe von <Return>
# if len(name) == 0: => Eingabe von <RETURN>
# Ausgabe: sortierte Liste der Namen

nameInput = None
nameListe = []

while True:
    nameInput = input("Geben Sie einen Namen ein (<RETURN> beendet die Eingabe)")
    if nameInput == "":
        break
    nameListe.append(nameInput)

nameListe.sort()
print("Namen: ", end=" ")
for nameInput in nameListe:
    print(nameInput, end=" ")