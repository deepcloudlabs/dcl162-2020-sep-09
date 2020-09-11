from xml.dom import minidom

from world.domain import Country

"""
Parsing ic completed
"""
dom_tree = minidom.parse("resources/countries.xml")

"""
Processing starts here
"""
root_countries = dom_tree.documentElement


countries = root_countries.getElementsByTagName("country")
asian_countries = []

for country in countries:
    continent = country.getElementsByTagName("Continent")[0].childNodes[0].data
    if continent == "Asia":
       ctry = Country()
       ctry.continent = continent
       ctry.code = country.getElementsByTagName("Code")[0].childNodes[0].data
       ctry.name = country.getElementsByTagName("Name")[0].childNodes[0].data
       ctry.population = int(country.getElementsByTagName("Population")[0].childNodes[0].data)
       asian_countries.append(ctry)

sorted_countries = sorted(asian_countries, key=lambda ctry : int(ctry.population), reverse=True)
for country in sorted_countries:
    print(country)