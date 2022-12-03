import csv

title  = input("title: ").strip().upper()

with open("favorite.csv", "r") as file:
    counter = 0
    reader = csv.DictReader(file) 
    for row in reader:
        if row["title"].strip().upper() == title:
            counter += 1


print(counter)
