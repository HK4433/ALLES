from itertools import count
'''
zahlen=[5,3,8,2,10]
temp=0
for einz in zahlen:
    temp+=einz
print(temp)

temp=0
zahlen=[15, 22, 3, 47, 9, 5]

for einz in zahlen:
    if temp <= einz:
        temp=einz
print(temp)

zahlen=[4, 2, 4, 6, 4, 7, 8, 4, 1]
for element in range(9):
    r= zahlen.count(element)
    if r >= 0:
        print(f"Die Zahl {element} kommt {r} mal vor")

zahlen=[2,5,8,1,6]
for element in zahlen:
    var=element * 2
    print(var)

fruchte=["Apfel","Banane","Orange","Mango"]
fruchte.reverse()
print(fruchte)

zahlen = [12,7,9,16,18,21,30]
for element in zahlen:
    if element % 2 == 0:
        print(element,end=";")

zahlen=[1,4,7,10]
for element in zahlen:
    element=int(element)
    var1= element*3
    print(var1)

lst = list(range(1,101))
lst1 = [x*x+x for x in lst]
print(lst1)
'''
def quadrad (trt1):
    return trt1*trt1+trt1

trt1= list(range(1,101))

ergebnis= list(map(quadrad,trt1))
print (ergebnis)

