countries = [
    {"code": "tur", "name": "turkey", "continent": "asia", "population": 80000000},
    {"code": "fra", "name": "france", "continent": "europe", "population": 67000000},
    {"code": "ita", "name": "italy", "continent": "europe", "population": 60000000}
]
order_by_population = lambda ctry: ctry["population"]
european_countries = []
for country in countries:
    if country["continent"] == "europe":
        european_countries.append(country)
european_countries = sorted(european_countries, key=order_by_population, reverse=True)
print(european_countries)
if_european = lambda ctry: ctry['continent'] == "europe"
order_by_name = lambda ctry: ctry["name"]

print(sorted(list(filter(if_european, countries)), key=order_by_name, reverse=True))

print(all(map(if_european, countries)))
