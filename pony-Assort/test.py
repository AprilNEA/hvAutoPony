import csv
f = csv.reader(open('pony-Assort\pony1000.csv','r'))
for i in f:
    print(i[1])