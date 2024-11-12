def summe_2d_liste(param1):
    summe=0
    for i in matrix:
        for element in i:
            summe += element
    return summe

matrix=[(1,2,3),(4,5,6),(7,8,9)]
erg=summe_2d_liste(matrix)


print(erg)