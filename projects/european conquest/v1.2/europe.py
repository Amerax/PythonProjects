import pygal_maps_world.maps
import countries
from random import randrange
import pygal_maps_world

country_dict = {name: countries.country(name, randrange(0, 100), False, name, name) for name in countries.country_codes.keys()}

for country, bordering in countries.borders.items():
        if not country_dict[country].occupied:
            for bordering_country in bordering:
                if country_dict[country].power > country_dict[country_dict[bordering_country].occupier].power:
                    country_dict[country].power += country_dict[bordering_country].power
                    country_dict[bordering_country].occupier = country
                    country_dict[bordering_country].occupied = True
                    country_dict[country].occupying.append(bordering_country)


worldmap_chart = pygal_maps_world.maps.World()
worldmap_chart.title = 'World Map'
for country in country_dict.values():
       
        worldmap_chart.add(country.name, [countries.country_codes[occupying_country] for occupying_country in country.occupying])
worldmap_chart.render_in_browser()


