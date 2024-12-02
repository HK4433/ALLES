import random
import copy
import time
import os

COUNT = 100  #Wieviel Prozent vom Bildschirm benutzt wird
DEAD = ' '   #Wieviele Tot sind
ALIVE = 'X'  #Was Angezeigt wird

lst = [ [0]*COUNT for i in range(COUNT)]  #Das Feld indem das Game of life Statt finded

#Die Felder auf denen Die X leben und Sterben
def init():
    for i in range(0, len(lst)):
        for j in range(0, len(lst[0])):
            if random.random() < 0.5:
                lst[i][j]=ALIVE
            else:
                lst[i][j]=DEAD

#Dead and Alive wird ausgegben
def output():
    for i in range(0, len(lst)):
        for j in range(0, len(lst[0])):
            print(lst[i][j], end=" ")
        print('\n')

#Das Feld indem das Game of life Statt finded kopie
def newGen():
    global lst
    lst_tmp = [[0] * COUNT for i in range(COUNT)]

    for i in range(len(lst)):
        for j in range(len(lst[0])):
            counter = 0

            # to be optimized
            # horizonzal + vertical check and count
            if i > 0:
                if lst[i - 1][j] == ALIVE:
                    counter = counter + 1
            if i < COUNT - 1:
                if lst[i + 1][j] == ALIVE:
                    counter = counter + 1
            if j > 0:
                if lst[i][j - 1] == ALIVE:
                    counter = counter + 1
            if j < COUNT - 1:
                if lst[i][j + 1] == ALIVE:
                    counter = counter + 1

            # diagonal check and count
            if i > 0 and j > 0:
                if lst[i - 1][j - 1] == ALIVE:
                    counter = counter + 1
            if i > 0 and j < COUNT - 1:
                if lst[i - 1][j + 1] == ALIVE:
                    counter = counter + 1
            if i < COUNT - 1 and j > 0:
                if lst[i + 1][j - 1] == ALIVE:
                    counter = counter + 1
            if i < COUNT - 1 and j < COUNT - 1:
                if lst[i + 1][j + 1] == ALIVE:
                    counter = counter + 1

            # check for life
            if lst[i][j] == ALIVE:
                if counter == 2 or counter == 3:
                    lst_tmp[i][j] = ALIVE
                else:
                    lst_tmp[i][j] = DEAD
            else:
                if counter == 3:
                    lst_tmp[i][j] = ALIVE
                else:
                    lst_tmp[i][j] = DEAD

    lst = copy.deepcopy(lst_tmp)


init()
output()
while True:     #Das Programm laufen lassen
    os.system('cls')
    newGen()
    output()
    time.sleep(0.1)
