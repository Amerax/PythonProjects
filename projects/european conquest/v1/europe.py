import pygal_maps_world.maps
import countries
from random import randrange
import pygal_maps_world

country_dict = {name: countries.country(name, randrange(0, 100), False, False, None) for name in countries.country_codes.keys()}

def start():
    for country, bordering in countries.borders.items():
        for bordering_country in bordering:
            if country_dict[country].power > country_dict[bordering_country].power:
                country_dict[bordering_country].attacked = True
                country_dict[bordering_country].occupied = True
                country_dict[bordering_country].occupier = country
                country_dict[country].power += country_dict[bordering_country].power
            else:
                pass
start()

for value in country_dict.values():
    print(value.occupier)

worldmap_chart = pygal_maps_world.maps.World()
worldmap_chart.title = 'Some countries'

for classes in country_dict.values():

    countries_conquered = []
    for country in country_dict.values():
        if country.occupier == classes.name:
            countries_conquered.append(countries.country_codes[country.name])
            countries_conquered.append(countries.country_codes[classes.name])


    worldmap_chart.add(countries.country_codes[classes.name], countries_conquered)
worldmap_chart.render_in_browser()
