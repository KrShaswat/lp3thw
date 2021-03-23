import ex40_mystuff
ex40_mystuff.apples()

# tangerine is a varibale declared in ex40_mystuff.py
print(ex40_mystuff.tangerine)


class MyStuff(object):
    # here we declare a varible in class i.e tanferine

    def __init__(self):
        self.tangerine = "And now a thousand years between"
    # here it is a function apple()
    def apple (self):
        print("I AM CLASSY APPLES!")


# Objects are like Imports
# instantiate is just a fancy, obnoxious, overly smart waty to say "create"
# when we instantiate a class we get an object

# to instantiate a class

thing = MyStuff()
thing.apple()
print(thing.tangerine)


# STEPS PYTHON GOES THROUGH

# python looks for MyStuff() and sees it is a class
# python crafts an empty object woth all the functions you've specified in the class using def
# python then looks to see if you made a "magic" __init__ function, and if you have it calls that function to initialize your newly created empty object
# 
