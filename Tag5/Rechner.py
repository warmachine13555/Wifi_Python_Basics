# tkinter ist ein Modul für Grafische Programmierung
# * => alle Elemente werden importiert und sind direkt ohne Modulname verwendbar
from tkinter import *
from tkinter import messagebox

# Definition der Funktionen

def plus():
    berechnung("+")

def sub():
    berechnung("-")

def mul():
    berechnung("*")

def div():
    berechnung("/")

def berechnung(operator):
    # Eingabe auslesen
    zahl1 = eingabe_zahl1.get()
    zahl2 = eingabe_zahl2.get()
    # Prüfung ob Eingabe leer
    if zahl1 == "" or zahl2 == "":
        # Fehlermeldung
        label_ergebnis_ausgabe.config(text="Fehler")
        return
    # Umwandlung in Zahlen
    zahl1 = int(zahl1)
    zahl2 = int(zahl2)
    # Berechnung
    match operator:
        case "+":
            ergebnis = zahl1 + zahl2
        case "-":
            ergebnis = zahl1 - zahl2
        case "*":
            ergebnis = zahl1 * zahl2
        case "/":
            if zahl2 == 0:
                # label_ergebnis_ausgabe.config(text="Division durch 0 nicht erlaubt")
                messagebox.showerror("Fehler", "Division durch 0 nicht erlaubt", icon="error")
                return
            ergebnis = zahl1 / zahl2
    # Ausgabe
    label_ergebnis_ausgabe.config(text=ergebnis)


# Hauptprogramm
# Fenster erstellen
fenster = Tk()
# Größe des Fensters
fenster.geometry("300x300")
# Titel des Fensters
fenster.title("Mein Rechner")

# Definition der Elemente am Bildschirm
# Definition der Labels
label_zahl1 = Label(fenster, text="Zahl 1:")
label_zahl2 = Label(fenster, text="Zahl 2:")
label_ergebnis = Label(fenster, text="Ergebnis:")
label_ergebnis_ausgabe = Label(fenster, text="0")
# Definition Eingabefelder
eingabe_zahl1 = Entry(fenster)
eingabe_zahl2 = Entry(fenster)
# Definition Buttons
plus_button = Button(fenster, text="  +  ", command=plus)
sub_button = Button(fenster, text="  -  ", command=sub)
mul_button = Button(fenster, text="  *  ", command=mul)
div_button = Button(fenster, text="  /  ", command=div)

# Platzierung der Elemente
label_zahl1.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
label_zahl2.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
eingabe_zahl1.grid(row=0, column=2, columnspan=2, padx=20, pady=20)
eingabe_zahl2.grid(row=1, column=2, columnspan=2, padx=20, pady=20)
plus_button.grid(row=2, column=0, padx=20, pady=20)
sub_button.grid(row=2, column=1, padx=20, pady=20)
mul_button.grid(row=2, column=2, padx=20, pady=20)
div_button.grid(row=2, column=3, padx=20, pady=20)
label_ergebnis.grid(row=3, column=0, columnspan=2, padx=20, pady=20)
label_ergebnis_ausgabe.grid(row=3, column=2, columnspan=2, padx=20, pady=20)

# Am Bildschirm anzeigen, zusätzlich werden Ereignisse verarbeitet (z.B. Button-Klick)
fenster.mainloop()