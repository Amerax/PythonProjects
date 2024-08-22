import csv
import pygal
import worldmap 


countries = []
countries_as_abbrevations = []

with open('Lists_of_earthquakes_5.csv', 'r', newline='', encoding='UTF-8') as csv_file:
    reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    for row in reader:
        countries.append(row[0])

for country in countries:
    data = worldmap.county2code(country)[0]
    countries_as_abbrevations.append(str(data[0]))


worldmap_chart = pygal.maps.world.World()

worldmap_chart.title = 'Countries that had eqarthquakes'

# Add data for different groups of countries
worldmap_chart.add('F countries', countries_as_abbrevations)


# Render the map in the browser
worldmap_chart.render_in_browser()
