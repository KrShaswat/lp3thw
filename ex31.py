print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    print("3. Challenge the bear to a fist fight")
    print("4. Hide like bitch.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print ("The bear eats your legs off. Good job!")
    elif bear == "3":
        print("The bear bitch slaps you dead and go back to eating cake. Good job!")
    elif bear == "4":
        print("You survived, you dignity not so much")
        print("You sulk while hiding in the laterine to mask your smell")
    else:
        print(f"Well, doing {bear} is probably will get you killed too.")
        print("Bear eats you and saves cake for desert")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries")
    print("2. Yellow jacket clothespin.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")