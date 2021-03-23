# keyword
# and is true if all values are true otherwise false
print(1 and 0)
print(0 and 1)
print(1 and 1)
print(0 and 0)

# as 
from sys import argv as arguments
with open ('languages.txt') as file:
    fileContent = file.read()

print("Text file contents:")
print(fileContent)

# assert
# throws an assertion error if the statement is not true

#assert False

# break
# break stop the loop iteration when called

while True:
    print("This runs this will not run")
    break
    print("this wont run")

# class
# defines a class

class Myclass:
    x= 5

p1 = Myclass()
print(p1.x)

# Continue
# skips the code after the continue call but the loop runs hte rest iterations

for i in range(10):
    
    if i == 5:
        continue
    print(i)

# def 
# to define a function

def a_function():
    print("This a function that returns 0")
    return 0

# elif is short for else if 

# generally present after the if statement as second condition to check
# more like that not true check for this too
# else 
# else is like if none of the if or elif work them this is all we are left with


for i in range(10):
    print(i)
    if i < 5:
        print("too small")
    elif i > 5:
        print("too big")
    else:
        print("just right")


# except
# in exception handling goes with try and finally

try:
    print(z)
except:
    print("An exception occurred")

# exec
# to run a string as python code

exec ('print("running String as code")')

# finally 
# in exception handling will run no matter what happens

try:
    print(z)
except Exception as e:
    print(e)
finally:
    print("I will always be here")

# for 
# for is to run a loop check line 62

# from 
# from is to get something from inside a library like argv from sys

from sys import argv

# global 
# global to declare a global variable
# i dont think this is recognized any more

# global (z) 

# if 
# if a statement is true then run the coded under neatly indented with 4 spaces

#import
# import to import a library of functions or another python file in the code

# is like test of equality
True is True
False is True

# lambda
# is another way write functions
def fucntion(x):
    return x
# same thing in lambda function but more like a function constructed with an expression
lambda x: x
# Here 
# keyword  = lambda
# a bound variable: x
# a body : x

lambda x: x+1

# Here 
# keyword = lambda
# bound variable = x
# body  = x+1

# we can apply the above function to an argument 
(lambda x: x+1)(2)
# to name a lmbda fucntion (since its an expression it can be named)

add_one  = lambda x: x+1
add_one(4)

# not is logical not

not True

# logical or 
True or False 
# will be True

# pass is statement that tells python to pass this entirely
# used to make empty function classes etc.


# raise key wrord is used to raise an exception

x = " Hello"

if not type(x) is int: 
    raise TypeError("Only integers are allowed")

# return
# return is used to exit function while returning a value

# with  and as

# yield
# yield stops the function from running from then on but returns a value.
# next time you call functions it runs the code after the previsous yield



