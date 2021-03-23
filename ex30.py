people = 50
cars = 50
trucks = 15

# if number of cars are greater than people then print " "
if cars > people:
    print("We should take the cars.")
# if, if statement is wrong then check for this and print " " if this is correct
elif cars < people: # elif run if the if statement doesnt run
    print("We should not take the cars.")
# if nothing works run this
else: # if none of the if or elif statement run then else statement runs
    print("We can't decide.")
# check for if trucks is greater than cars
if trucks > cars:
    print("That's too many trucks.")
# above condition doesn't work than check for elif condition
elif trucks < cars:
    print("Maybe we could take the trucks.")
# if none of the condition works run this
else:
    print("We still can't decide")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
