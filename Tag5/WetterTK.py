from tkinter import *
from tkinter import messagebox
import requests
# Wir benötigen ein weiteres Paket, das mit tikinter zusammenarbeiten kann
# pip install pillow
from PIL import ImageTk, Image

def queryAPI():
    # Wir verwenden Exception Handling
    try:
        # Abfrage aus dem Internet
        response = requests.get("http://api.openweathermap.org/data/2.5/weather?q="  + eingabe_ort.get() + "&units=metric&APPID=5e82f2874c6adf74d2c48ce1ebde23e2")
        # Umwandlung des Textes in ein Dictionary
        wetter = eval(response.text)
        main = wetter["main"]

        # 2) Schritt Zugriff mittels z.B. temp => Zahl
        label_tempout.config(text=main['temp'])
        label_luftdruckout.config(text=main['pressure'])
        label_luftfeuchtigkeitout.config(text=main['humidity'])

        icon = wetter['weather'][0]['icon']
        image = Image.open(requests.get("http://openweathermap.org/img/wn/"+icon+"@2x.png",stream=True).raw)
        # Umwandlung in ein Tkinter Image
        photo = ImageTk.PhotoImage(image)
        # Bild in das Label einfügen
        (label_icon.config(image=photo))
        label_icon.image = photo
    except:
        # Messagebox
        messagebox.showerror("Fehler", "Ort nicht gefunden", icon="error")
        return

# Hauptprogramm
# Fenster erstellen
fenster = Tk()
# Größe des Fensters
fenster.geometry("300x500")
# Titel des Fensters
fenster.title("Mein Wetter")

# Elemente
# Eingabefeld für Stadt
eingabe_ort = Entry(fenster)
# Labels
label_ort = Label(fenster, text="Ort:")
label_temp = Label(fenster, text="Temperatur:")
label_tempout = Label(fenster, text="0")
label_luftdruck = Label(fenster, text="Luftdruck:")
label_luftdruckout = Label(fenster, text="0")
label_luftfeuchtigkeit = Label(fenster, text="Luftfeuchtigkeit:")
label_luftfeuchtigkeitout = Label(fenster, text="0")
label_icon = Label(fenster)
# Button
query_button = Button(fenster, text="Abfrage", command=queryAPI)

# Platzierung
label_ort.grid(row=0, column=0, padx=20, pady=20)
eingabe_ort.grid(row=0, column=1, padx=20, pady=20)
query_button.grid(row=1, column=1, padx=20, pady=20)
label_temp.grid(row=2, column=0, padx=20, pady=20)
label_tempout.grid(row=2, column=1, padx=20, pady=20)
label_luftdruck.grid(row=3, column=0, padx=20, pady=20)
label_luftdruckout.grid(row=3, column=1, padx=20, pady=20)
label_luftfeuchtigkeit.grid(row=4, column=0, padx=20, pady=20)
label_luftfeuchtigkeitout.grid(row=4, column=1, padx=20, pady=20)
label_icon.grid(row=5, column=1, padx=20, pady=20)

fenster.mainloop()