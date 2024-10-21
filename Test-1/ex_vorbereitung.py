'''
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




#Übung 1
def greetWorld ():
    print("Guten Tag, Welt!")

greetWorld ()


#Übung 2

def greetPerson1(name):
    print(f"Guten Tag, {name}!")  # Ausgabe der Begrüßung

# Verwende die Funktion mit dem Namen "Anna"
greetPerson1("Anna")  # Ausgabe: Guten Tag, Anna!


#Übung 3

def greetPerson2(name):
    return f"Guten Tag, {name}!"

ergebnis = greetPerson2 ("Anna")
print (ergebnis)

def greetPerson2(name):
    return f"Guten Tag, {name}!"  # Formatierte Zeichenkette mit dem Namen

# Verwende die Funktion mit dem Namen "Anna"
ergebnis = greetPerson2("Anna")
print(ergebnis)  # Ausgabe: Guten Tag, Anna!


#Übung 4

def printPerson(vorname, nachname, alter):
    return f"Guten Tag, {vorname}, {nachname}, {alter}!"

ergebnis = printPerson ("Ana", "Eckstein", "24")
print(ergebnis)

#Schreiben Sie eine Funktion, die alle Elemente in einer Liste verdoppelt. Verwenden Sie die Liste zahlen
#=[2,5,8,1,6]

zahlen=[2,5,8,1,6]

def myfunc1(zahlen):
    for element in zahlen:
        x = element * 2
        print(f"{element} mal 2 ergiebt {x}")

myfunc1(zahlen)


#Schreiben Sie eine Funktion, die alle Elemente einer Liste rückwerts ausgibt. Verwenden Sie die Liste früchte
#=["Apfel","Banane","Orange","Mango"]

fruchte=["Apfel","Banane","Orange","Mango"]
def myfunc2(fruchte):
    fruchte.reverse()
    print(fruchte)
myfunc2(fruchte)


#Schreiben Sie eine Funktion, die das größte Element in einer Liste von Zahlen zurückgibt. Verwenden Sie die
#Liste zahlen = [15,22,3,47,9,5]

zahlen1=[15,22,3,47,9,5]
def myfunc3(zahlen1):
    print(max(zahlen1))

myfunc3(zahlen1)

#Schreiben Sie eine Funktion, die alle geraden Zahlen aus einer Liste zurückgibt. Verwenden Sie die Liste
#=[12,7,9,16,18,21,30]

zahlen2=[12,7,9,16,18,21,30]
def myfunc4(zahlen2):
    for x in zahlen2:
        if x % 2 == 0:
           print(x)

myfunc4(zahlen2)



def zahlen(zahlen_1):
    return [x*2 for x in zahlen_1]

zahlen_1= [1,2,3,4,5]
r=zahlen_1
print(r)


#Definieren Sie eine Funktion die einen String und eine Int funktion bekommt und es 5 mal aufgerufen wird

name = "Harun"
i=2
def myfunc(lol, i):
    for x in range(i):
        print(f"{lol}")

myfunc(name, i)
'''
#Definieren Sie eine Liste von 1-100 und dann überprüfen ob sie durch 3 Teilbar sind und wenn die durch 3 Teilbar sind sollen sie ausgegeben werden

list=list(range(1,101))
for i in list:
    if (i % 3 == 0):
        print(f"{i} ist Teilbar durch 3")

