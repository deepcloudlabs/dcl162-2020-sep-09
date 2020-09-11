import xml.sax

from world.domain import Country


class CountryHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.countries = []
        self.country = Country()
        self.opening_tag = ""
        self.property_tag_names = {
            "Code": "code",
            "Name": "name",
            "Population": "population",
            "Continent": "continent"
        }

    def startElement(self, tag, attributes):
        self.opening_tag = tag

    def characters(self, content):
        if self.opening_tag in self.property_tag_names.keys():
            prop = self.property_tag_names[self.opening_tag]
            setattr(self.country, prop, content)

    def endElement(self, tag):
        self.opening_tag = ""
        if tag == "country":
            if self.country.continent == "Asia":
                self.countries.append(self.country)
            self.country = Country()


if __name__ == '__main__':
    parser = xml.sax.make_parser()
    handler = CountryHandler()
    parser.setContentHandler(handler)
    parser.parse("resources/countries.xml")
    sorted_countries = sorted(handler.countries, key=lambda ctry : int(ctry.population), reverse=True)
    for country in sorted_countries:
        print(country)
