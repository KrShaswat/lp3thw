# Importing argv from sys package
from sys import argv
# So to save the current script name and the text file to edit
script, filename = argv
# here CTRL+C i.e ^C inrupts the script and stops it immediately, so a hard exit?
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that. hit RETURN.")
# Here return or enter input is not saved and is just a gimmick
input('?')
# we open the file in 'w' i.e write mode
print("Opening the file...")
target = open(filename, 'w')
# truncating a file essentially empties it
# but since we are opening the file write mode it empties it
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")
# asking for lines to save in the filename.txt and saving them in a variable
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
#writing the input strings in file using write method. adding \n tells python to go to next line
# target.write(line1)
# target.write('\n')
# target.write(line2)
# target.write('\n')
# target.write(line3)
# target.write('\n')
# Study Drill 3
target.write(f'{line1}\n{line2}\n{line3}\n')

print("And finally, We close it.")
target.close()