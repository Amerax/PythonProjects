import csv

song_list = []
artist_name_list = []

with open('Memorable_Songs.csv', 'r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file, quotechar='"', delimiter=',')
    idx = 0
    for row in reader:
        song_list.append(row[1])
        artist_name_list.append(row[2])

with open('table1.csv', 'w', encoding='UTF-8', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', quotechar='"')
    for value, artist in zip(song_list, artist_name_list):
        writer.writerow([value, artist])
