cars = 100
# If you change 4.0 to 4 the multiplication with cars_driven (for carpool capacity)changes to an integer, rest there is no effect
# reason for that is that float 4.0 was changing the result to a float
space_in_a_car = 4
drivers = 30
passengers = 90
# Since there can be only cars with a driver can be driven so
cars_not_driven = cars - drivers
cars_driven = drivers
# the car pool capacity available will be the amount of cars that can be driven plus 
# the seat availble in cars
carpool_capacity = cars_driven * space_in_a_car
# To know how many passenger will in each car if they are equally divided
# But to save fuel we can increase the amount of person per car to reduce cars driven
average_passengers_per_car = passengers / cars_driven
# below are just the output statements to report what we did
# It seems we dont need to add space after each "" python adds it on its own accord
print("There are",cars,"cars available.")
print("There are only", drivers,"drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity,"people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, 
      "in each car.")