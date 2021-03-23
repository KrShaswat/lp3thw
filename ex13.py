from sys import argv
# script is to give script name a variable so actually we need 4 argv's for 3 variables 1 is for script
script,  first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("your third variable is:", third)

#'python ex13.py first 2nd 3rd' to run first 2nd 3rd are the arguments taken from the user