def parse_countries(countries):
    rows = []
    print('previo al for')
    print(type(countries))
    for country in countries:
        print('estamos en el array')
        print(type(country))
        name = country["name"]["common"]
        #It has a array, use "get" to save even it doesnt have this key
        capital = country.get("capital", ['It doesn´t have a known capital'])[0]
        region = country.get("region", "nn")
        population = country.get("population", 0)

        rows.append((name, capital, region, population))

    return rows