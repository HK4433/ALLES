
#Schreiben Sie eine Funktion greetWorld() ohne Rückgabewert, die "Guten Tag, Welt!" auf dem Bildschirm ausgibt
#Rufen Sie die Funktion auf.

def greetWorld ():
    print("Guten Tag, Welt")

greetWorld()


#Schreiben Sie eine Funktion greetPerson1(Name) ohne Rückgabewert, die einen Namen als Parameter übergibt
#und dann "Guten Tag, [NAME]!" auf dem Bildschirm ausgibt. Verwenden Sie die Funktion mit dem Namen "Anna"

def greetPerson1 (name):
   print(f"Guten Tag, {name}")

greetPerson1("Anna")


#Schreiben Sie eine Funktion greetPerson2(NAME) mit Rückgabewert, die eiinen Namen als Parameter übergibt
#und dann "Guten Tag, [Name]!" auf dem Bildschirm ausgibt. Verwenden Sie die Funktion mit dem Namen "Anna"

def greetPerson2 (name):
   ret=(f"Guten Tag, {name}")
   return ret

r=greetPerson2("Anna")
print(r)

#Schreiben Sie eine Funktion printPerson(vorname,nachname,alter), die den Vor- und Nachnamen sowie das Alter
#einer Person ausgibt

def printPerson(vorname, nachname, alter):
    ret1=print(f"Sie heißen {r} {p} und sind {g} Jahre alt")
    return ret1

r=input("Vorname?: ")
p=input("Nachname?: ")
g=input("Alter?: ")
t=printPerson(r,p,g)
print(t)

#Schreiben Sie eine Funktion, die alle Elemente in einer Liste verdoppelt. Verwenden Sie die Liste zahlen
#=[2,5,8,1,6]

zahlen=[2,5,8,1,6]
def myfunc1
for element in zahlen:
    o=element*2
    print(o)


#Schreiben Sie eine Funktion, die alle Elemente einer Liste rückwerts ausgibt. Verwenden Sie die Liste früchte
#=["Apfel","Banane","Orange","Mango"]

fruchte=["Apfel","Banane","Orange","Mango"]
fruchte.reverse()
print(fruchte)


#Schreiben Sie eine Funktion, die das größte Element in einer Liste von Zahlen zurückgibt. Verwenden Sie die
#Liste zahlen = [15,22,3,47,9,5]

zahlen1=[15,22,3,47,9,5]
temp=0
for eins in zahlen1:
    if temp<=eins:
        temp=eins
print(temp)


#Schreiben Sie eine Funktion, die alle geraden Zahlen aus einer Liste zurückgibt. Verwenden Sie die Liste
#=[12,7,9,16,18,21,30]
