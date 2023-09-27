# Verwaltung einer Personen-Datenbank
# Pro Person:
# - Name
# - Adresse
# - Telefonnummer
# wir verwenden SQLite3 => Standard, keine Installation mit pip notwendig
import sqlite3

def neuerEintrag(cur, con):
    # Benutzereingaben
    name = input("Name: ")
    adresse = input("Adresse: ")
    telefonnummer = input("Telefonnummer: ")
    # Einfügen der Daten in die Tabelle Personen
    # INSERT INTO Personen => Einfügen in die Tabelle Personen
    # (name, adresse, telefonnummer) => Spaltennamen
    # VALUES (?, ?, ?) => Platzhalter für die Werte
    # Die Werte werden in einem Tupel übergeben
    # Die Reihenfolge der Werte muss mit der Reihenfolge der Platzhalter übereinstimmen

    # Änderungen in der DB speichern
    cur.execute("INSERT INTO personen (name, adresse, telefonnummer) VALUES (?, ?, ?)", (name, adresse, telefonnummer))
    # Endgültig in der DB speichern
    con.commit()

def löschenEintrag(cur, con):
    # Name eingeben zum löschen
    name = input("Name zum Löschen: ")
    res = cur.execute("SELECT * FROM personen WHERE name = :name", {"name": name})
    # nur einen einzelnen Datensatz holen
    person = cur.fetchone()
    # Wenn es den Datensatz gibt
    if person:
        # Löschen des Datensatzes
        cur.execute("DELETE FROM personen WHERE personenID = :id", {"id": person[0]})
        # Änderungen in der DB speichern
        con.commit()
    else:
        print("Name nicht gefunden")

def ausgabeEintrag(cur):
    # Lesen von allen Datensätzen in der Tabelle Personen
    res = cur.execute("SELECT * FROM personen;")
    # Holen der Daten und Speichern in einer Liste
    personenListe = res.fetchall()
    # Schleife über die Liste
    for person in personenListe:
        # in der Liste steht ein Tupel pro Personeneintrag
        print(f"Name: {person[1]} Adresse: {person[2]} Telefonnummer: {person[3]}")

try:
    # Verbindung zur Datenbank herstellen
    # Wenn es die DB nocht nicht gibt, wird eine leere DB angeleg
    # Wenn es die DB gibt, wird einfach eine Verbindung geöffnet
    con = sqlite3.connect("personen.db")
    # Cursor => Arbeiten mit der DB
    cur = con.cursor()
    # Tabelle anlegen
    # CREATE TABLE Personen => Erzeugen der Tabelle
    # IF NOT EXISTS => Tabelle wird nur erzeugt, wenn sie noch nicht existiert
    # PRIMARY KEY => die DB erzeugt automatisch einen eindeutigen Wert für jeden Datensatz
    cur.execute("""
                CREATE TABLE IF NOT EXISTS personen 
                (
                    personenID INTEGER NOT NULL,
                    name VARCHAR(100),
                    adresse VARCHAR(200),
                    telefonnummer VARCHAR(20),
                    PRIMARY KEY (personenID)
                )
                """)
    # Bedienung des Users
    while True:
        eingabe = input("(n)eu (l)öschen (a)usgeben (e)nde: ").lower()
        match eingabe:
            case "n":
                # Eingabe der Daten
                neuerEintrag(cur, con)
            case "l":
                # Löschen der Daten
                löschenEintrag(cur, con)
            case "a":
                # Ausgabe der Daten
                ausgabeEintrag(cur)
            case "e":
                # Beenden
                break
            case _:
                print("Falsche Eingabe")



    # Schließen der Verbindung
    con.close()

except Exception as e:
    print(e)