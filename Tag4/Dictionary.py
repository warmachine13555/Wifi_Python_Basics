def ausgabeDict(dict):
    print("Dictionary: ")
    # schleife
    for key in dict.keys():
        print(f"Key: {key} Value: {dict[key]}")

# Anlegen eines Dictionaries
# eine Sammlung von Key-Value Paaren
woerter = {
    "Raum": "room",
    "Tisch": "table",
    "Tür": "door"
}

print(woerter)
ausgabeDict(woerter)

# Hinzufügen
# einneuer eintrag wird erstellt
# falls der eintrag schon existiert, wird der value überschrieben
woerter["Fenster"] = "window"
ausgabeDict(woerter)

# löschen
woerter.pop("Fenster")
ausgabeDict(woerter)

# abfragen
if "Raum" in woerter:
    print(f"Raum ist vorhanden, Übersetzung: {woerter['Raum']}")