# pip install requests
import requests
# Pretty Print => Standard Modul
import pprint

# Abfrage aus dem Internet
response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Wien&units=metric&APPID=5e82f2874c6adf74d2c48ce1ebde23e2")
# print(response.text)
wetter = eval(response.text)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(wetter)

# Zugriff auf die Daten
# 1) Schritt Zugriff mit Key = Main => Dictionary
main = wetter["main"]
print(main)

# 2) Schritt Zugriff mittels z.B. temp => Zahl
print(f"Temperatur: {main['temp']}")
print(f"Luftdruck: {main['pressure']}")
print(f"Luftfeuchtigkeit: {main['humidity']}")
print(f"Icon: {wetter['weather'][0]['icon']}")
