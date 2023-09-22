import datetime
import locale
import math
import os


def datumDifferenz():
    # Differenz zwischen zwei Daten
    # Berechnen Anzahl Tage bis Silvester
    silvester = datetime.date(2023, 12, 31)
    heute = datetime.date.today()
    date_format = heute.strftime('%x')  # Get the date format in the locale
    print(heute.strftime(date_format))

    # Rechnen, silvester heute sind date-Klassen
    # diff => ist eine Klasse vom Typ timedelta
    diff = silvester - heute
    print(f"Tage bis Silvester: {diff.days}")

def datumGesternHeuteMorgen( ):
    # Datum von gestern, heute, morgen
    heute = datetime.date.today()
    gestern = heute - datetime.timedelta(days=1)
    morgen = heute + datetime.timedelta(days=1)
    print(f"Heute: {heute}, Gestern: {gestern}, Morgen: {morgen}")
    print(f"Heute: {heute.strftime('%A %d-%B-%Y')}")

def zeitRechnung():
    jetzt = datetime.datetime.now()
    plustime = jetzt + datetime.timedelta(hours=20)
    print(f"Jetzt: {jetzt}, plustime: {plustime}")

def zeitDifferenz():
    time1 = datetime.datetime.now()
    # Zeitmessung für die folgende Schleife
    for i in range(1000000):
        ergebnis = math.sin(i)
    time2 = datetime.datetime.now()
    diff = time2 - time1
    print(diff)

def fileZeiten():
    for file in os.listdir("."):
        date = datetime.datetime.fromtimestamp(os.stat(file).st_ctime)
        print(f"File: {file} wurde erstellt am: {date}")


# Hauptprogramm
locale.setlocale(locale.LC_ALL, "de_DE.utf-8")
datumDifferenz()
datumGesternHeuteMorgen()
zeitRechnung()
zeitDifferenz()
fileZeiten()