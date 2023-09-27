# Pandas ist ein Modul zum einlesen, verarbeiten und speichern von Daten
# pip install pandas
# Mathplotlib dient zur Darstellung von charts
# pip install mathplotlib

import pandas as pd
import matplotlib.pyplot as plt


# Einlesen von Daten (Quellen: csv, Excel, Datenbanken, Json, Html, XML, ...)
# Tabellen ähnliche Datenstruktuer => DataFrame
daten = pd.read_csv("PandasInput.csv", delimiter=";", parse_dates=True)
print(daten)

# Rechnen mit Daten
print(daten['Preis'].sum())

# neue Spalte hinzufügen
gespreis = pd.DataFrame({'GesPreis': daten['Preis'] * daten['Menge']})
# Vereinigung von daten und gespreis
daten = daten.join(gespreis)
print(daten)
mwst = pd.DataFrame({'MwSt': daten['GesPreis'] * 0.20, 'EndPreis': daten['GesPreis'] * 1.20})
daten = daten.join(mwst)
print(daten)

daten.to_csv("PandasOutput.csv", sep=";")

# Ausgabe als Balkendiagramm
# x-Achse = Datum
# y-Achse = Endpreis
plot = daten.plot(kind='bar', x='Datum', y='EndPreis', title="Einnahmen September 2023")
plot.set_ylabel("Euro")
plt.savefig("Balken.jpg")

# Gruppierung => wir wollen Produkte der gleichen Art zusammenzählen
gruppiert = daten.groupby('Art').sum()
print(gruppiert)
# Tortendiagramm: Größe jedes Tortenstückes entspricht dem gruppierten Endpreis
zusammenfassung = gruppiert.plot(
    kind='pie',
    y='EndPreis',
    title="Gruppierung nach der Art",
    legend=False,
    autopct='%1.1f%%'
)
plt.savefig("Torte.jpg")

# anzeigen des Diagramms
# plt.show()
