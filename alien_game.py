from sys import exit
print("""
    Aliens have invaded earth. Our Governments have united and are collectively fighting
    a losing battle. In this hopeless chaos a technical Genius Pappu came through
    and invented a subsonic divice to kill all aliens in one go. Yup Sharmaji ka
    launda Pappu. But Pappu ko bna diya ullu and aliens stole the circuit 
    and are carrying it back to their ship.
""")
name = input("Sergent Ramniwas: What is your name Private: \n")

print(f"Sergent Ramniwas: Private {name}, its your responsibilty to retrieve the circuit lost by Mr. Pappu")

input("Sergent Ramniwas: Do you accept this mission? ")
accept_mission = input("Sergent Ramniwas: Private say it loud and clear SIR YES SIR\n")

if accept_mission == "SIR YES SIR":
    print("Good soldier get going")

elif accept_mission != "SIR YES SIR":
    print("Sargent: You are a disgrace. Put your weapon down and leave.")
    exit()

print(f"""Sergent Ramniwas: Listen carefully, I will not repeat this.
    Private {name} your mission is to go in the chintamani jungle and 
    ambush the aliens in their route. You cannot fight them so use smoke to 
    confuse them and steal the circuit and run. Run faster then you ever have
""")

print("Following orders you move towards the jungle.")
path = input("You reach a crossroads, turn left to Jack Daniels jungle, right for chintmani jungle. \n")

if path == 'left':
    print("Hmm, something is wrong you dont see anything everything is quite too quite")
    print("You feel sharp pain in the head and your vision fades away")
    exit()

elif path == 'right':
    print(""" You enter the chintamani jungle 
    you come accross trail of wierdly shaped footprints.
    when you follow them you see two aliens ahead.
    """)

else:
    print("There were simple instructions to follow . . . TCH TCH TCH")
    exit()

smoke_em = input("What do you do? use smoke bomb or go rambo? \n")
if smoke_em == 'smoke bomb' or smoke_em == 'bomb':
    print("""You move very carefully to a higher ground position yourself
        out of sight and throw the smoke bomb right in between the 
        aliens, they panic and start weezing.
    """)
    steal_circuit = ("You can wait for smoke to fade and then attack them or go ninja")

    if steal_circuit == 'wait':
        print("""Smoke fades away, you position your rifle aim for the 
            head an alien and BANG!!. One alien down, you move your crosshairs
            to other alien and you see it aiming at at your way
            then you see sparks and your vision fades away.
        """)
        exit()
    elif steal_circuit == 'ninja':
        print("""
            You slide down the slope and pull your knife and glock out.
            you move swiftly and reach the first alien and stab it in the face, 
            it plops to the ground. You aim the glock at the other and empty
            the clip. As the smoke fades you emerge victorious covered in green
            goo.             
        """)
elif smoke_em == 'rambo':
    print("""You scream HAIYAAAA and jump in the open and start firing your M4
        None of your bullets hit, rambo is a movie Private.
        As you realize the aliens can teleport to your location you try to run.
        Well you try to run atleast. You are caught and eaten by the aliens""")
    exit()

else:
    print("Well my 2 month old puppy that can understand and follow orders. Shame")

print(""" You have successfully stolen the Pappu device time to go back.""")
print("As you reach the base Sergent Ramniwas looks at you and smiles")
print(f"""Sargent Ramniwas: Well done Private {name}. I will recommend you to galantry
    Award.

    As the days goes by Pappu is now a Hero. you? well another soldier lost in sands
    of time. Though Army remembers you and are treated as the alien slayer {name}.
""")

