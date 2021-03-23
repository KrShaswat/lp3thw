# made string of {} to farmat in strings
formatter = "{} {} {} {}"
# format method is used with formatter to insert  numbers, text, booleans, varibles
print(formatter.format(1,2,3,4))
print(formatter.format("one","two","thre","four"))
print(formatter.format(True,False,False,True))
print(formatter.format(formatter,formatter,formatter,formatter))

# this is clean man!

print(formatter.format(
    "What?",
     "I don't know poems",
     "instead i can give you an ackward look",
     "maybe you will like it"
))

# mistakes made 
## typo line 4
## didnt give spaces inbetween {} line 1
## in line 9, 10, 11 even if we add space after , and before" the space shows up in the output