'''
cels = input("Wie viel grad wollen Sie in Fahrenheit umrechnen?: ")
cels = float(cels)
'''
from zoneinfo import reset_tzpath

w1=1.8
w2=32
w3=5/9
'''
def myFunc(cel):
    ret = cel * w1 + w2
    return ret

r=myFunc(cels)
print(f"{cels} Grad sind exakt {r} Fahrenheit")

fahr = input("Wie viel Fahrenheit wollen Sie in Grad umrechnen?: ")
fahr = float(fahr)

def myFunc2(fahrenheit):
    ret = (fahrenheit-w2) * w3
    return ret

r=myFunc2(fahr)
print(f"{fahr} Fahrenheit sind in Grad umgerechnet {r}")
'''
from gzip import write32u

erg=float(input("Wenn Sie Grad zu Fahrenheit umrechnen wollen geben Sie die 1 ein und wenn Sie von Fahrenheit zu Grad umrechnen wollen geben sie die 2 ein: " ))

if erg==1:
    grad = float(input("Geben Sie ihre Grad angabe an: "))
    erge = grad * w1 + w2
    print(f"Grad umgerechnet ergiebt {erge}")
elif erg==2:
    fagr = float(input("Geben Sie ihre Fahrenheit angabe ein: "))
    ergeb = (fagr-w2) * w3
    print(f"Fahrenheit umgerechnet ergibt {ergeb} Grad")