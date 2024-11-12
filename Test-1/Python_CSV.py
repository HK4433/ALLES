import csv
file1=open('Class.csv','w')
writer=csv.writer(file1,delimiter=';')
writer.writerow(['Class','Forename','Lastname'])
class1=input('Enter Class Name: ')
forename=input('Add Forname: ')
lastname=input('Add Lastname: ')
writer.writerow([class1,forename,lastname])
file1.close()

a=input('Do you want to update the list? Type yes or no: ')

while a=='yes':
    file1=open('Class.csv','a')
    writer=csv.writer(file1,delimiter=';')
    class1=input('Enter Class Name: ')
    forename=input('Add Forname: ')
    lastname=input('Add Lastname: ')
    writer.writerow([class1,forename,lastname])
    a=input('Do you want to update the list?: ')
    file1.close()

file1=open('Class.csv','r')
reader=csv.reader(file1,delimiter=';')
for row in reader:
    print(row)
print('Done')
file1.close()