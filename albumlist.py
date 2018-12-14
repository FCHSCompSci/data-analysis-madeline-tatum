import csv

filename = 'albumlist.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    numbers = []
    for row in reader:
        numbers.append(row[0])
    print(numbers)

    years = []
    for row in reader:
        years.append(row[1])
    print(years)

    albums = []
    for row in reader:
        albums.append(row[2])
    print(albums)

    artists = []
    for row in reader:
        artists.append(row[3])
    print(artists)

    genres = []
    for row in reader:
        genres.append(row[4])
    print(genres)

    subgenres = []
    for row in reader:
        subgenres.append(row[5])
    print(subgenres)

