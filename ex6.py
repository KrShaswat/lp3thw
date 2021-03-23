# variable with 10 input
types_of_people = 10
# string with types_of_people formatted into it using f
x = f"There are {types_of_people} types of people."
# more variables 
binary = "binary"
do_not = "don't"
# more varibles formatted into strings
y = f"Those who know {binary} and those who {do_not}"
# printing
print(x)
print(y)
# printing with formatting varibles into strings
print(f"I said:{x}")
print(f"I also said:'{y}'")
# boolean varible
hilarious = False
# empty {} is to denote that we will format varible here
joke_evaluation = "Isn't that joke so funny?!{}"
# format method used to format hilarious into the empty {} left in joke_evaluation string
print(joke_evaluation.format(hilarious))
# two variable with strings in them
w = "This is the left side of..."
e = "a string with a right side."
# it seems pyhton can add two string with just +
print(w + e)