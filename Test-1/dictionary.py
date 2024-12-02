person = {
    "first name": "Anna",
    "surname": "Müller",
    "age": 25,  # Der zweite "age" wurde entfernt, da er den ersten überschreiben würde
    "age": 23
}
print(person["first name"])

#def printPerson(person1):
#return print(person1)
#printPerson(person)

number1 = int(input("Please enter a number between 1 and 100: "))
if number1 > 100 or number1 < 0:
    print("Please enter a number between 1 and 100 and nothing else")
    number1 = int(input("Please enter a new number between 1 and 100: "))

number2 = int(input("Please enter a new number between 1 and 100: "))
if number2 > 100 or number2 < 0:
    print("Please enter a new number between 1 and 100 and nothing else")
    number1 = int(input("Please enter a new number between 1 and 100: "))


while number1 != number2:
    if number1 > number2 and number1 > 0 and number2 > 0:
        print("Your current number is lower than your last number")
        number2 = input("Please enter a new number between 1 and 100: ")
        number2 = int(number2)
        continue
    elif number2 > 100 or number2 < 0:
        print("Please enter a number between 1 and 100 and nothing else")
        number2 = int(input("Please enter a new number between 1 and 100: "))
        continue
    elif number1 < number2 and number2 > 0:
        print("Your current number is higher than your last number")
        number2 = input("Please enter a new number between 1 and 100: ")
        number2 = int(number2)
        continue
    elif number2 > 100 or number2 < 0:
        print("Please enter a number between 1 and 100 and nothing else")
        number2 = int(input("Please enter a new number between 1 and 100: "))
        continue
    elif number2 == 0:
        print("Program cancel")
        break
    else:
        print("You find the right number")

        while number1 == number2:
            if number1 == number2:
                print("Your current number is equal to your last number")
            if number1 > number2 and number1 > 0 and number2 > 0:
                print("Your current number is lower than your last number")
                number2 = input("Please enter a new number between 1 and 100: ")
                number2 = int(number2)
                continue
            elif number2 > 100 or number2 < 0:
                print("Please enter a number between 1 and 100 and nothing else")
                number2 = int(input("Please enter a new number between 1 and 100: "))
                continue
            elif number1 < number2 and number2 > 0:
                print("Your current number is higher than your last number")
                number2 = input("Please enter a new number between 1 and 100: ")
                number2 = int(number2)
                continue
            elif number2 > 100 or number2 < 0:
                print("Please enter a number between 1 and 100 and nothing else")
                number2 = int(input("Please enter a new number between 1 and 100: "))
                continue
            elif number2 == 0:
                print("Program cancel")
                break
            else:
                print("You find the right number")

