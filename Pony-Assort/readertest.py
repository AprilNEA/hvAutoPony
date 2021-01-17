# coding:utf-8
import csv
f = csv.reader(open('answers.csv','r'))
for i in f:
    print(i)