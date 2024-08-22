import csv
import pygal

def artist_percentages(*args):
    artist_dict = {artist: 0 for artist in args}
    with open('table1.csv', newline='', encoding='UTF-8') as csv_file:
        dict_reader = csv.DictReader(csv_file, delimiter=',', quotechar='"')

        for dictionary in dict_reader:
            for artist in args:
                if artist in dictionary['Artist']:
                    artist_dict[artist] += 1

    return artist_dict

artist_dict = artist_percentages('Khalid', 'Ed Sheeran', 'Post Malone', 'Wiz Khalifa', 'Marshmello')

bar_chart = pygal.HorizontalBar()
bar_chart = pygal.HorizontalBar(explicit_size=True, width=1500, height=720)
bar_chart.title = 'How Many Times Artist Appear'

for artist_name, value in artist_dict.items():
    bar_chart.add(artist_name, value)

bar_chart.render_in_browser()
