# Programm zum auslesen von config-Files

# 1) File einlesen
file = open("config.txt", "r")
# read liest mit einem Aufruf dem kompletten Fileinhalt
# Ergebnis ist ein String
inhalt = file.read()
file.close()
print(inhalt)

# 2) String wird in Dictionary umgewandelt
configdict = eval(inhalt)
print(configdict)

# 3) Verwendung
print(f"maxLength: {configdict['maxLength']}")