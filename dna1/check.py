import sys
import csv

dic = open(sys.argv[1])
reader = csv.DictReader(dic)

for row in reader:
    print(row['AATG'])
    