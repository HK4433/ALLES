
#Aufgabe: Schreibe eine Funktion filter_odd_numbers(lst), die alle ungeraden Zahlen aus einer gegebenen Liste entfernt
# und die verbleibenden geraden Zahlen als neue Liste zurückgibt.
'''def filter_odd_numbers(lst):
    return [num for num in lst if num % 2 == 0]

# Testfälle
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(filter_odd_numbers(numbers))  # Sollte [2, 4, 6, 8] zurückgeben'''

#Schreibe eine Funktion calculate_average(lst), die den Durchschnitt (Mittelwert) der Zahlen in einer Liste berechnet.
# Wenn die Liste leer ist, soll die Funktion None zurückgeben.
'''def calculate_average(lst):
    if not lst:
        return None
    return sum(lst) / len(lst)

# Testfälle
numbers = [10, 20, 30, 40, 50]
print(calculate_average(numbers))  # Sollte 30 zurückgeben

empty_list = []
print(calculate_average(empty_list))  # Sollte None zurückgeben'''

#Aufgabe: Schreibe eine Funktion find_min(lst), die das kleinste Element in einer Liste von Zahlen findet und zurückgibt
# Verwende dazu keine eingebauten Funktionen wie min().

'''def find_min(lst):
    if not lst:
        return None
    min_value = lst[0]
    for num in lst:
        if num < min_value:
            min_value = num
    return min_value

# Testfälle
numbers = [23, 45, 12, 67, 34]
print(find_min(numbers))  # Sollte 12 zurückgeben'''

#Aufgabe: Schreibe eine Funktion create_sequence(n), die eine Liste von n aufeinander folgenden Zahlen beginnt mit der Zahl 1 erstellt.
# Wenn n = 5 ist, soll die Liste [1, 2, 3, 4, 5] zurückgegeben werden.

'''def create_sequence(n):
    return [i for i in range(1, n + 1)]

# Testfälle
print(create_sequence(5))  # Sollte [1, 2, 3, 4, 5] zurückgeben
print(create_sequence(3))  # Sollte [1, 2, 3] zurückgeben'''

#Aufgabe: Schreibe eine Funktion remove_negative(lst), die alle negativen Zahlen aus einer Liste entfernt
# und eine neue Liste mit den verbleibenden positiven Zahlen zurückgibt.
'''def remove_negative(lst):
    return [num for num in lst if num >= 0]

# Testfälle
numbers = [-1, 2, -3, 4, 5, -6]
print(remove_negative(numbers))  # Sollte [2, 4, 5] zurückgeben'''

#Aufgabe: Schreibe eine Funktion count_frequency(lst), die ein Dictionary zurückgibt,
# das die Häufigkeit jeder Zahl in der Liste enthält.
'''from collections import Counter

def count_frequency(lst):
    return dict(Counter(lst))

# Testfälle
numbers = [1, 2, 2, 3, 3, 3, 4]
print(count_frequency(numbers))  # Sollte {1: 1, 2: 2, 3: 3, 4: 1} zurückgeben
'''
#Aufgabe: Schreibe eine Funktion is_palindrome(s), die überprüft, ob ein gegebener String ein Palindrom ist (d. h. der String liest sich von vorne und hinten gleich).
# Du sollst den String als Liste von Zeichen behandeln.

'''def is_palindrome(s):
    return s == s[::-1]

# Testfälle
print(is_palindrome("radar"))  # Sollte True zurückgeben
print(is_palindrome("python"))  # Sollte False zurückgeben
'''

#Aufgabe: Schreibe eine Funktion second_largest(lst), die das zweitgrößte Element in einer Liste von Zahlen zurückgibt.
# Wenn es kein zweitgrößtes Element gibt (z. B. bei nur einem Element oder allen gleichen Zahlen), soll None zurückgegeben werden.

'''def second_largest(lst):
    unique_lst = list(set(lst))  # Entfernt Duplikate
    if len(unique_lst) < 2:
        return None
    unique_lst.sort()
    return unique_lst[-2]

# Testfälle
numbers = [10, 20, 30, 40, 50]
print(second_largest(numbers))  # Sollte 40 zurückgeben

numbers2 = [1, 1, 1, 1]
print(second_largest(numbers2))  # Sollte None zurückgeben
'''

#Schreibe eine Funktion generate_pyramid(n), die eine Zahlenpyramide mit n Zeilen erstellt.
# In der ersten Zeile steht die Zahl 1, in der zweiten Zeile die Zahlen 1 2, in der dritten Zeile 1 2 3 usw.

def generate_pyramid(n):
    for i in range(1, n + 1):
        print(" ".join(str(x) for x in range(1, i + 1)))

# Testfälle
generate_pyramid(3)
# Ausgabe:
# 1
# 1 2
# 1 2 3

generate_pyramid(5)
# Ausgabe:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5




