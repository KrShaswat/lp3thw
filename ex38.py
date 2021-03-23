# a sting 
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")
# here we split the string ten_things into a list of strings based on space
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"] # list of eight stuff

while len(stuff) != 10: # the loop runs till len(stuff) is not equal to 10
    next_one = more_stuff.pop() # pops out the last element of more_stuff (it removes that string from the list)
    print("Adding: ", next_one) # prints the popped out word from more_stuff
    stuff.append(next_one) # adds the word in the bound varible of the function i.e stuff
    print(f"There are {len(more_stuff)} items now.") # 

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy # This just prints the last word using negative indexing
print(stuff.pop()) # this will pop out the last # pop out last word i.e. Corn
print(' '.join(stuff)) # what? cool! # joins the stuff dict with space as a string
print('#'.join(stuff[3:5])) # super stellar! # joins 4th  to 6th words in stuff i.e. Telephone 4th word and light which is before 6th word
