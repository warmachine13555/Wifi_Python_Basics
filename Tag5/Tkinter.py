# Taschenrechner +, -, /, *
# Grafische Oberfläche mit Tkinter
#
# 1) Klasse Taschenrechner
# - Konstruktor
# - addieren
# - subtrahieren
# - dividieren
# - multiplizieren
# - Ausgabe
# - Löschen
#
# 2) Klasse TaschenrechnerGUI
# - Konstruktor
# - addieren
# - subtrahieren
# - dividieren
# - multiplizieren
# - Ausgabe
# - Löschen
# - GUI
#
# 3) Hauptprogramm
# - Objekt der Klasse TaschenrechnerGUI anlegen
# - GUI starten
# - GUI in Schleife laufen lassen
# - GUI beenden
#

from tkinter import *

# Klasse Taschenrechner
class Taschenrechner:
    # Konstruktor
    def __init__(self):
        # Attribute
        self.ergebnis = 0

    # addieren
    def addieren(self, zahl):
        self.ergebnis += zahl

    # subtrahieren
    def subtrahieren(self, zahl):
        self.ergebnis -= zahl

    # dividieren
    def dividieren(self, zahl):
        self.ergebnis /= zahl

    # multiplizieren
    def multiplizieren(self, zahl):
        self.ergebnis *= zahl

    # Ausgabe
    def __str__(self):
        return f"Ergebnis: {self.ergebnis}"

    # Löschen
    def loeschen(self):
        self.ergebnis = 0

# Klasse TaschenrechnerGUI
class TaschenrechnerGUI:
    # Konstruktor
    def __init__(self):
        # Attribute
        self.taschenrechner = Taschenrechner()
        self.gui()

    # addieren
    def addieren(self):
        zahl = float(self.eingabe.get())
        self.taschenrechner.addieren(zahl)
        self.ausgabe.config(text=self.taschenrechner)

    # subtrahieren
    def subtrahieren(self):
        zahl = float(self.eingabe.get())
        self.taschenrechner.subtrahieren(zahl)
        self.ausgabe.config(text=self.taschenrechner)

    # dividieren
    def dividieren(self):
        zahl = float(self.eingabe.get())
        self.taschenrechner.dividieren(zahl)
        self.ausgabe.config(text=self.taschenrechner)

    # multiplizieren
    def multiplizieren(self):
        zahl = float(self.eingabe.get())
        self.taschenrechner.multiplizieren(zahl)
        self.ausgabe.config(text=self.taschenrechner)

    # Ausgabe
    def ausgabe(self):
        self.ausgabe.config(text=self.taschenrechner)

    # Löschen
    def loeschen(self):
        self.taschenrechner.loeschen()
        self.ausgabe.config(text=self.taschenrechner)

    # GUI
    def gui(self):
        # Fenster
        self.fenster = Tk()
        self.fenster.title("Taschenrechner")
        self.fenster.geometry("300x300")
        # Eingabe
        self.eingabe = Entry(self.fenster, width=20)
        self.eingabe.pack()
        # Buttons
        self.buttonAddieren = Button(self.fenster, text="+", command=self.addieren)
        self.buttonAddieren.pack()
        self.buttonSubtrahieren = Button(self.fenster, text="-", command=self.subtrahieren)
        self.buttonSubtrahieren.pack()
        self.buttonDividieren = Button(self.fenster, text="/", command=self.dividieren)
        self.buttonDividieren.pack()
        self.buttonMultiplizieren = Button(self.fenster, text="*", command=self.multiplizieren)
        self.buttonMultiplizieren.pack()
        self.buttonAusgabe = Button(self.fenster, text="Ausgabe", command=self.ausgabe)
        self.buttonAusgabe.pack()
        self.buttonLoeschen = Button(self.fenster, text="Löschen", command=self.loeschen)
        self.buttonLoeschen.pack()
        # Ausgabe
        self.ausgabe = Label(self.fenster, text=self.taschenrechner)
        self.ausgabe.pack()

    # GUI starten
    def start(self):
        self.fenster.mainloop()

    # GUI beenden
    def beenden(self):
        self.fenster.destroy()

# Hauptprogramm
taschenrechnerGUI = TaschenrechnerGUI()
taschenrechnerGUI.start()
taschenrechnerGUI.beenden()