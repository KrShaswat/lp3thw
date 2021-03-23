# create a mapping of state to abreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
} # dictionary of state name and abbreviations

# Create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
} # name of cities saved to keys same as state abbrevations

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland' # added two more cities

# print out some cities
print('_' * 10) # prints - 10 times acts visual aid
print("NY state has: ", cities['NY']) # printing cities using keys
print("OR State has: ", cities['OR']) 

# print some states
print('_'*10)
print("Michigan's abbreviation is: ", states['Michigan']) # printing the value using keys 
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']]) # since we have same abbreviations for the state values and cities keys
print("Florida has: ", cities[states['Florida']]) # we can use the abbreviation result as keys for cities

#print every state abbreviation
print('-'*10)
for state, abbrev in list(states.items()): # here two variable are attached with list states.items() it converts dictionary into list of dictionary key and value lists 
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-'* 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' *10)
for state, abbrev in list(states.items()):
    print(f"{states} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there 
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")



#-------------------------------------------------------------------------------------

# Stuff ran on commandline
# What a list can do
things = ['a', 'b', 'c', 'd']
print(things[1])
things[1] = 'z'
print(things[1])
print(things)

# What a Dictionary does
stuff = {'name': 'Zed', 'age':39, 'height': 6*12 +2}
print(stuff['name'])
print(stuff['age'])
print(stuff['height'])
stuff['city'] = "SF"
print(stuff['city'])
# we can also do this

stuff[1] = 'Wow'
stuff[2] = 'Neato'
print(stuff[1])
print(stuff[2])

# What if we have to delete stuff

del stuff['city']
del stuff[1]
del stuff[2]
print(stuff)