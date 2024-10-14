
for i in range(10):
    print(i,end=" ")

for i in range(1,11):
    print(i,end=";" )

for i in range(0,11, 2):
    print(i,end=" ")

for i in range(10,-10, -2):
    print(i)

for i in range(11):
    for j in range(i):
        print(j)
    print('---')

num=input("Enter a number: ")
num=int(num)

for i in range(num):
    print(i,end=",")
    print(i*i,end=";")

def myFunc_1():
    print("Hallo Welt")

myFunc_1()

def myFunc_2(param1):
    print(f"Hallo {param1}!")

myFunc_2("World")

def my_Func3(param1,param2):
    ret = param1 + param2
    return ret

r = my_Func3(3,4)
print(r)

print("Geben Sie die Zahlen für die Geradengleichung: y=ax+b ein")
a =input("Geben Sie die Zahl a ein: ")
a = float(a)
x =input("Geben sie die Zahl x ein: ")
x = float(x)
b = input("Geben Sie die Zahl b ein: ")
b = float(b)

#Funktion Geradengleichung
def my_Func4(param1,param2,param3):
    ret = param1 * param2 + param3
    return ret

r = my_Func4(a,x,b)
print(f"Y= {r}")

def my_Func4(a,x,b):
    y = a * x + b
    return y

y = my_Func4(a,x,b)
print(y)

