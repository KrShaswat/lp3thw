# importing argv from sys package
from sys import argv
# script is script name and input_file is the vaiable we will use and take when the program is run
script, input_file =argv
# function to make the input_file print so we take it in read mode
def print_all(f):
    print(f.read())
# 0 to seek start of the file, 1 to current position 2 to the end of file
def rewind(f):
    f.seek(0)
# ?
def print_a_line(line_count,f):
    print(line_count, f.readline())
#we open the file and save it in current_file vairble
current_file = open(input_file)

print("First let's print the whole file:\n")
# read the file with function
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
# go to strat of the file using function
rewind(current_file)

print("Let's print three lines:")
# printing three lines with tidious code meh!
current_line = 1
print_a_line (current_line, current_file)

current_line += current_line
print_a_line(current_line, current_file)

current_line += current_line
print_a_line(current_line, current_file)

# rewind(current_file)
# print_a_line(1, current_file)