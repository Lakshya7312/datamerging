import csv
import pandas as pd

file1 = 'result.csv'
file2 = 'unit_converted_stars.csv'

df1 = []
df2 = []

with open(file1,'r', encoding='utf8') as f:
    reader = csv.reader(f)

    for i in reader:
        df1.append(i)

with open(file1,'r', encoding='utf8') as g:
    reader = csv.reader(g)

    for a in reader:
        df2.append(a)

h1 = df1[0]
p1 = df1[1:]

h2 = df2[0]
p2 = df2[1:]

headers = h1 + h2

planet_data = []

for i in p1:
    planet_data.append(i)
for j in p2:
    planet_data.append(j)   

with open("final_stars.csv", 'w', encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)