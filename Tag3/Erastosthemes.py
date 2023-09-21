# Sieb des Erasthostenes
# Steichen von Vielfachen


# Funktion
def sieb(limit):
    # 1) Erzeugen einer Python-Liste
    #    die Liste is mit den Zahlen von 2 bis limit gefüllt
    # ergebnis = []
    # for i in range(2,limit+1):
    #     ergebnis.append(i)
    ergebnis = list(range(2, limit+1))

    # 2) Steichen der Vielfachen
    for i in range(2, limit+1):
        # nur wenn i noch nicht gestrichen ist, machen wir weiter
        if i in ergebnis:
            # Vielfachen von i streichen
            for vielfache in range(i*2, limit+1, i):
                if vielfache in ergebnis:
                    ergebnis.remove(vielfache)


    # 3) Rückgabe des Ergebnisses
    return ergebnis

# Hauptprogramm
print(sieb(1000))