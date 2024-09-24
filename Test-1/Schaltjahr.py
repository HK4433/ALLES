jahr = input("Geben Sie mir eine Jahresangabe: ")
jahr = int(jahr)

if (jahr % 400==0) or (jahr % 4==0):
    print("Es ist ein Schaltjahr")
elif (jahr / 100==0):
    print("Es ist kein Schaltjahr")
else:
    print("Es ist kein Schaltjahr")


#CHAT GPT LÖSUNG
jahr = input("Geben Sie mir eine Jahresangabe: ")
jahr = int(jahr)

# Überprüfen, ob es ein Schaltjahr ist
if (jahr % 400 == 0) or (jahr % 4 == 0 and jahr % 100 != 0):
    print("Es ist ein Schaltjahr")
else:
    print("Es ist kein Schaltjahr")

