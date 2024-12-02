#Erste Schritte

print('Hallo wie heißen Sie')
name= input()
print('Hallo' ,name)

print("dies ist ein einfacher Addierer")
print("geben sie die erste Zahl ein")
Zahl1 = input()
print("geben sie die zweite Zahl ein")
Zahl2 = input()

print("Das sind ihre Eingaben:" ,Zahl1,Zahl2,)

res1 = (int(Zahl1) + int(Zahl2))
print(res1)

#Mathematische Formeln

val1 = 13
val2 = 5
resAdd = val1 + val2
resub = val1 - val2
resMult= val1 * val2
resDiv = val1 / val2

print("Die Addition beträgt:",resAdd)
print("Die Subtraktion beträgt:",resub)
print("Die Multiplikation beträgt:",resMult)
print("Die Division beträgt:",resDiv)

print(f"die Subtraktion der Zahlen: {val1} und {val2} ergibt {resub}")

print (f"Die geschweifte Klammer {{")

# Mit Definition und Rückgabewert

def summe (var1, var2):
    ergebnis = var1 + var2
    return ergebnis
z= int(input('Geben Sie die Zahl ein: '))
u= int(input('Geben Sie die Zahl ein: '))
r= summe(z,u)
print(r)

# While-Schleife geben Sie es so oft aus wie alt Sie sind

name = input('Geben Sie ihren Namen ein: ')
age = int(input('Geben Sie ihr Alter ein: '))

i= 0

while i < age:
    i=i+1
    print(f'Hallo, {name}')

#geben Sie an wie viel KM Sie gegangen sind, beim Gehen beträgt ein Schritt 74cm. Das Programm gibt dann die Schritte aus

km= int(input('geben Sie die gegangene KM anzahl in meter an'))
schritt = float(0.74)

resDiv =round( km / schritt)
print(resDiv)


#IF-Bedingung
# User wird nach Alter gefragt, Anhand daran merkt man ob der User Volljährig ist
print("geben Sie ihr alter ein")
alter= input()
alter = int(alter)
if alter >= 18:
    print("der User ist volljährig")

#Wenn der Benutzer jünger als 10 ist. Ist er ein Kind
elif alter <= 10:
    print("der User ist minderjährig")
    print("du bist ja noch ein Kind")
else:
    print("der User ist minderjährig")


#User soll eine positive Zahl eingeben, es wird geprüft ob die Zahl gerade ist oder ungerade
print('geben Sie eine positive Zahl ein ')
zahl1= input()
zahl1=int(zahl1)

if zahl1>0:
    print('Ihre Zahl ist positiv')
else:
    print('Ihre Zahl ist negativ')

if zahl1 %2:
    print('Ihre Zahl ist ungerade')
else:
    print('Ihre Zahl ist gerade')

#Es wird überprüft ob das Jahr ein Schaltjahr ist
print('geben Sie ein Jahr ein ')
jahr= input()
jahr=int(jahr)

if jahr % 400 ==0:
    print('Das Jahr ist ein Schaltjahr')
elif jahr % 100 ==0:
    print('Das Jahr ist kein Schaltjahr')
elif jahr % 4 == 0:
    print('Das Jahr ist ein Schaltjahr')
else:
    print('Das Jahr ist kein Schaltjahr')

#FOR SCHLEIFE UND LISTEN

# User gibt eine Zahl ein und es werden alle Zahlen ausgegeben zusätzlich das Quadrat.

zahl=input("geben Sie eine Zahl ein: ")
zahl=int (zahl)
for zahl in range (zahl):
    print(zahl*zahl)

#Funktionen

#Funktion ohne Rückgabe und Übergabeparameter

def myfunc_1():
    print('Hallo Welt')
myfunc_1()

#Funktion mit Übergabewert
def myfunc_2(param1):
    print('Hallo Welt', param1)
myfunc_2('und Ahmet')

#Funktion mit Übergabe und Rückgabewert

def myfunc_3(param1,param2):
    ret= param1+param2
    return ret

r= myfunc_3(5,32)
print(r)

#Die Geradengleichung y = ax +b. User gibt die Parameter ein und bekommt das ergebnis geliefert
#Erstellen Sie eine eigene Funktion

a = input('geben Sie eine Zahl für a ein ')
b= input('geben Sie eine Zahl für b ein ')
x= input('geben Sie eine Zahl für x ein ')

a= int(a)
b= int(b)
x= int(x)

def myfunc_4 (a,b,x):
    ret= a*x +b
    return ret
r= myfunc_4(a,b,x)
print('y=' ,r)

# Listen Übung

# 1. Speichern Sie den Vornamen, Nachnamen und Alter einer Person in der Liste person_1.

person_1 = ['Ahmet, Toplar, 23']
print(person_1)

#	2. Definieren Sie die Funktion printPerson, welche Vorname, Nachname und Alter
#	einer Person als Übergabeparameter bekommt und diese ausgibt.

def printPerson (vorname, nachname, alter):
    print(f'mein Name ist {vorname}, {nachname}, {alter}')

printPerson('Ahmet', 'Toplar', 23)

#	3. Definieren Sie die Funktion getPersonAsString, welche Vorname, Nachname und Alter
#	einer Person als Übergabeparameter bekommt und einen String zurückgibt, z.B. "Vorname: Hans; Nachname: Meier; Alter: 23"


person_1 = ['Ahmet', 'Toplar', '23']
def getPersonAssString (person_1):
    ret= (f'Vorname: {person_1 [0]}, Nachname: {person_1[1]}, Alter: {person_1[2]}')
    return ret

r=getPersonAssString(person_1)
print(r)

#Tupel

#Dictionary

coffee_maker = dict()
coffee_maker["brand"] = "Silver Crest"
coffee_maker["volume"] = 0.750
coffee_maker["heater"] = True

#Hier wird der Datentyp leicht lesbar festgelegt und die Paare klar mittels key und value eingefügt.

#Über die dritte Schreibweise können Sie auch weitere key-value Paare schnell und einfach hinzufügen:
coffee_maker["decaf"] = False

#Jeder key muss in einem Dictionary eindeutig sein. Wird zwei mal der gleiche key verwendet,
#wird der Value zu dem key überschrieben.#
coffee_maker["brand"] = "WMF"

#Den value zu einem Key können Sie leicht auslesen:
value= coffee_maker["brand"]

#... oder:
value = coffee_maker.get("brand")

#Mit dem Befehl pop können leicht keys gelöscht werden

coffee_maker.pop("brand")

#Oft ist es hilfreich alle keys einen Dictionary zu kennen, dafür nutzt man folgenden Befehl:
keys_of_coffee_maker = coffee_maker.keys()

#... gleiches gilt für die values

values_of_coffee_maker = coffee_maker.values()


#Erstellen sie ein Wörterbuch person, das die folgenden Informationen erhält.

person = dict()
person['Vorname'] = 'Anna'
person['Müller'] = 'Müller'
person['Alter'] = '23'

#Das Alter zu verändern

person['Alter'] = '24'

print(person)


