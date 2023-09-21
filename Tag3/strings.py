# String = Folge von Unicode Zeichen
# Zugriff ist so wie bei Listen

s1 = "Hello World"

# Zugriff auf die Einzel-Zeichen
# Index Zugriff: von 0 bis len(str)-1
for i in range(len(s1)):
    # \t ... Tabulator
    print(f"{s1[i]}", end="\t")
print()

# Iteration
for zeichen in s1:
    # \t .. Tabulator
    print(f"{zeichen}", end="\t")
print()

# slicing von Index 3 bis 6
print(s1[3:6])

# slicing vom Index bis zum Ende
print(s1[6:])

# slicing vom Beginn bis zum Index
print(s1[:6])

name = "Benjamin Lettner"
index = name.index(" ")
print(name[index+1:])

# suchen
if "World" in s1:
    print("World ist vorhanden")
    # Bestimmung der Stelle
    print(s1.index("World"))

# Umwandlung
print(s1.lower())
print(s1.upper())
print(s1.capitalize())

# Ersetzen
print(s1.replace("World", "Österreich"))

# split
teile = s1.split(" ")
print(teile)
# join
print("-".join(teile))