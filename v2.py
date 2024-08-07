#install using pip install pygal_maps_world
import csv
import pygal
import worldmap 


countries = {}
countries_as_abbrevations = []
countries_with_ratings = {}

with open('Lists_of_earthquakes_5.csv', 'r', newline='', encoding='UTF-8') as csv_file:
    reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    for row in reader:
        countries[row[0]] = float(row[1])

for country in countries:
    data = worldmap.county2code(country)[0]
    countries_with_ratings[(str(data[0]))] = countries[country]

print(countries_with_ratings)
worldmap_chart = pygal.maps.world.World()

worldmap_chart.title = 'Countries that had eqarthquakes'

# Add data for different groups of countries
worldmap_chart.add('Scale Rating', countries_with_ratings   )


# Render the map in the browser
worldmap_chart.render_in_browser()
