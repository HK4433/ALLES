import csv
file1=open('Class.csv','r+')
writer=csv.writer(file1,delimiter=';')
writer.writerow()

print('Done')
