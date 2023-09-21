# for-Schleifen

# Range mit einem Parameter: Obere Grenze
# Die Grenze ist nicht inkludiert
print("Range mit 1 Parameter")
for i in range(5):
    print(i)

# Range mit zwei Parameter: Unter- und Obergrenze
# Untergrenze inkludiert, Obergrenze nicht inkludiert
print("Range mit 2 Parameter")
for i in range(3,7):
    print(i)
    
# Range mit drei Parameter: Unter- und Obergrenze und Inkrement
print("Range mit 3 Parameter")
for i in range(3,10,2):
    print(i)

# Range mit drei Parameter: Unter- und Obergrenze und negativer Inkrement
print("Range mit 3 Parameter")
for i in range(10,3,-2):
    print(i)