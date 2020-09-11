import csv

with open("people.csv", "rt") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
