# Eingabe: E-Mail Adresse
# Ausgabe: E-Mail gültig/nicht gültig
# Prüfungen:
# - Länge > 4 (a.b@c)
# - Es muss das @ Zeichen vorhanden sein
# - Es muss der . vorhanden sein
# - die Endung sollte ".at" sein (endswith)
# - Umwandlung in Kleinbuchstaben


while True:
    email = input("Geben Sie ihre E-Mail Adresse ein (Format Max.Mustermann@mail.at): ").lower()
    emailsplit = email.split(".")
    if len(email) < 4:
        print("Keine gültige E-Mail (Mail unter 4 zeichen lang)")
        continue
    if "@" not in email:
        print("Keine gültige E-Mail (@ fehlt)")
        continue
    if not email.endswith(".at"):
        print("Keine gültige E-Mail (.at fehlt)")
        continue
    if len(emailsplit) != 3:
        print("Keine gültige E-Mail (. fehlt)")
        continue
    print(f"Gültige Email: {email}")