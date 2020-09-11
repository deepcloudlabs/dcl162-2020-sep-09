import csv

with open("people.csv", "rt") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(dict(row))
