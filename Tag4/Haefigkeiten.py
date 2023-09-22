# Eingabe: string
# Ausgabe: Buchstabenhäufigkeiten
# Dictionary
# - key: Buchstabe
# - value: Anzahl

def haeufigkeit(text):
    # leeres Dictionary anlegen
    dict = {}
    
    # schleife über den text
    for zeichen in text:
        # ist das zeichen schon im Dictionary enthalten
        if zeichen in dict:
            # vorhanden => Zähler um eins hochzählen
            dict[zeichen] += 1
        else:
            # nicht vorhanden => wir müssen einen Eintrag machen
            dict[zeichen] = 1
    return dict
        

# Hauptprogramm
text = input("Bitte einen Text eingeben: ")
print(haeufigkeit(text.lower()))