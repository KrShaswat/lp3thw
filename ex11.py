# printing what input we want, end = ' ' is so that input is shown in the same line
print("How old are you?", end=' ')
# saving the user input in age
age = input()
# asking user stuff
print("How tall are you?", end=' ')
# same as line 4
height = input()
print("How much do you weigh?", end = ' ')
weight = input()
# printing the user input inside strings usng f (format)
print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# Most of what software does is the followinf:
## Takes some kind of input from a person
## Changes it
## Prints out something to show how it changed.
