# This one is like your acripts with argv
# Here def tells python we are making a function
# print_two is the name of the function
# *args is similar to argv parameter for this function ?
# 
def print_two(*argvs):
    # this unpacks the arguments
    arg1, arg2 = argvs
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
# we dont need to unpack argv
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just rakes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")
    
# the functions wokr same as the print() and other commands
print_two('Zed', 'Shaw')
print_two_again('Zed', 'Shaw')
print_one("First!")
print_none()