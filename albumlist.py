import csv
from matplotlib import pyplot as plt
import collections

filename = 'albumlist.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    numbers = []
    years = []
    albums = []
    artists = []
    genres = []
    subgenres = []
    for row in reader:
        numbers.append(row[0])
        years.append(row[1])
        albums.append(row[2])
        artists.append(row[3])
        genres.append(row[4])
        subgenres.append(row[5])

filename_2 = 'mc_artists.csv'
with open(filename_2) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    them_artists = []
    frequency = []
    for row in reader:
        them_artists.append(row[0])
        frequency.append(row[1])

plt.plot(them_artists,sorted(frequency))
plt.title("Most Common Artists", fontsize=24)
plt.xlabel("Artist", fontsize=14)
plt.ylabel("Frequency of artist", fontsize=14)
plt.show()
