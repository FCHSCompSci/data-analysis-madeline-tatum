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

mc_artists = collections.Counter(artists).most_common(10)
print(mc_artists)

x = ['The Beatles','Bob Dylan','The Rolling Stones','Bruce Springsteen','The Who','U2','Led Zeppelin','David Bowie','Radiohead','Elton John']
y = [10,10,10,8,7,5,5,5,5,5]
plt.plot(x,y)
plt.title("Most Common Artists", fontsize=24)
plt.xlabel("Artist", fontsize=14)
plt.ylabel("Frequency of artist", fontsize=14)
plt.show()

fig = plt.figure(dpi=126, figsize=(10, 6))
