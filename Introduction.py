# I will ask name?
# Then ask how old are you?
# do you like playing games?
# Which type of games do you like?
# Summarize

print("What is your name? ") # print statment to guide user
name = input() # inputs value enter by user and saves it in name variable

age = input("How old are you? ") # this asks user to enter his/her age and saves it in age variable

print("Do like playing games or sports? ") # print statement to guide user
like_game = input() # saves usr input in like_game variable

type_game = input("Which games or sports do you like? ") # asks user to enter if he/she likes playing games

print("So, your name is ", name) # prints a string with varible name
print("You are ", age,"years old") # prints two strings with variable age in between them
print(f"So you said {like_game} to liking games and you like playing {type_game}") # prints statement using f or format function to replace varible inputs--