states = {
    'Haryana': 'HR',
    'Uttar Pradesh': 'UP',
    'Delhi': 'DL',
    'Arunachal Pradesh': 'AP',
    'Himachal Pradesh': 'HP'
    }

cities = { 
    'HR': 'Faridabad',
    'AP': 'Itanagar',
    'HP': 'Simla',
    'UP': 'Varanasi',
    'DL': 'New Delhi'
}

# printing Abbreviaitions
for state, abbrev in list(states.items()):
    print(f"{state} is in short called {abbrev}")

# printing Cities with abbrev 

for abbrev, city in list(cities.items()):
    print(f"{abbrev} state has {city} city.")

# printing both cities and abbreviations

for state, abbrev in list(states.items()):
    print(f"{state} in short is called {abbrev} has city {cities[abbrev]}")