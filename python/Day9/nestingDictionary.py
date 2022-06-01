capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
}

travel_log = [ 
    {
        "country" : "France",
         "Cities_visited" : ["paris", "Lille", "Dijon"],
          "total_visit": 12
    },
    {
        "country" :"Germany", 
        "Cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visit": 5
    }
]

def add_new_country(country, visit, cities):
    new_country = {}
    new_country["country"] = country
    new_country["Cities_visited"] = cities
    new_country["total_visit"] = visit
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)