import csv
from collections import defaultdict

columnsOne = defaultdict(list)
with open('/Users/Dustin/Downloads/report1523280837168.csv', 'r') as one:
    reader = csv.DictReader(one)  # read rows into a dictionary format
    for row in reader:  # read a row as {column1: value1, column2: value2,...}
        for (k, v) in row.items():  # go over each column name and value
            columnsOne[k].append(v)  # append the value into the appropriate list
            # based on column name k

columnsTwo = defaultdict(list)
with open('/Users/Dustin/Downloads/report1523280856494.csv', 'r') as two:
    reader = csv.DictReader(two)  # read rows into a dictionary format
    for row in reader:  # read a row as {column1: value1, column2: value2,...}
        for (k, v) in row.items():  # go over each column name and value
            columnsTwo[k].append(v)  # append the value into the appropriate list
            # based on column name k

dups = []
for row in columnsOne['Report Name']:
    for rw in columnsTwo['Name']:
        if rw in row:
            dups.append(rw)
dups = set(dups)
for item in dups:
    print(item)

with open('/Users/Dustin/Downloads/indashboards.txt', 'w+', encoding='utf8') as f:
    for item in dups:
        f.write(item + "\n")
