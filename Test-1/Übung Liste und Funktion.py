name=input("Geben Sie einen Namen ein: ")
lastname=input("Geben Sie einen Nachnamen ein: ")
age=input("Geben Sie ein Alter ein: ")

person1=[name, lastname, age]
def myFunc(getPersonAsString):
    ret=f"Mein Name ist: {getPersonAsString[0]}, mein Nachname: {getPersonAsString[1]}, mein alter ist: {getPersonAsString[2]}"
    return ret

r=myFunc(person1)
print(r)
