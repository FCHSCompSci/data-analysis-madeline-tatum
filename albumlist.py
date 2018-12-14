import csv
from matplotlib import pyplot as plt

filename = 'albumlist.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    numbers = []
    for row in reader:
        numbers.append(row[0])

    years = []
    for row in reader:
        years.append(row[1])

    albums = []
    for row in reader:
        albums.append(row[2])

    artists = []
    for row in reader:
        artists.append(row[3])

    genres = []
    for row in reader:
        genres.append(row[4])

    subgenres = []
    for row in reader:
        subgenres.append(row[5])

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.bar(numbers, height=500)
plt.show()