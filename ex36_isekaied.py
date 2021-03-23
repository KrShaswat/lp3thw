#print("Play Isekai'ed? (Y/n): ")
# need a exit and run function
name = input("What should I call you?: ")
feed = {'name': name,
        'symbol': '> ', 
        'angel_love': 5, 
        'devil_love': 5}

# -------------------------------SCENE - 1:  The Crossroads--------------------------
# fed all variable for function to dictionary feed.
# scene with same outcome you die
# print(feed)
def crossroads(feed):
    """First scene: Encounter with truck kun"""
    print(""" 
    It's a cold morning, you are walking to the bus stop.
    Through fog of your breathe you see two people arguing. You don't pay much attention
    and go and sit on the bench to wait for the bus.
    Then you hear someone weeping, you see a lady behind visibly scared cowering backwards.
    What do you do?
    1. Interfere
    2. Ignore 
    """
    )
    no_fighting = input(feed['symbol'])
    if no_fighting == 'interfere':
        print("Fight all you want motherfuckers, but nobody is scaring a lady!")
        print(f"""
        You step up and walk straight towards the lady. Right through the men arguing
        and ask her 
        \n{feed['name']}: Are you ok?\n 
        lady doesn't say anything but is looking through you and is even more scared.
        You look back and all you see is a fist flying right at your face.
        damn bitch, mama told you not to interfere in anyone's business
        \n{feed['name']}: awwwhh fuck, it hurts motherfucker it hurts, oooh i am gonna kill you now.\n 
        as you stand up you realise you are on the road and those three are running back.
        *splat* A truck runs you over.
        You dead, like literally dead dead.
        At least you tried to do some good.
        Angel Dumas is pleased
        """)
        feed['angel_love'] += 1
    elif no_fighting == 'ignore':
        feed['devil_love'] += 1
        print("Ignore, someone is always fighting and someone is always scared! \nDevil Karen is pleased\n")
        print(""" 
        Still its interesting to see insects fight among themselves. 
        You are not at all concerned about the lady who is scared and is stepping back towards the road 
        and a truck is coming surprisingly fast.
        But, do you save her?
        1. yes
        2. no        
        """)
        save_the_bitch = input(feed['symbol'])
        if save_the_bitch == 'yes':
            print(""" 
            Awwww,  can't see an insect die?
            Well whatever, you try to push her off the truck's path.
            She grabs your sleave while falling back and pulls you directly in front of the truck.
            Well, you always knew the good you do is just for your satisfaction but, 
            what in the actual fuck happened?
            Dead, trying to save a women. This bitch better name her first born after you.
            Angel Dumas seems to be intersted
            """)
            feed['angel_love'] += 1
        elif save_the_bitch == 'no':
            feed['devil_love'] += 1
            print("oooh, it got interesting let's see which one of the insects saves the bitch. \nDevil Karen is very pleased\n")
            print(""" 
            As you watch the scene with a pink blush and satisfied smile on your face. 
            The truck takes a sudden turn saves the bitch and looses control going over the bus stop with you in it.
            You are dead, not the insects What the fuck?
            and died with that embarassing expression on your face. tch tch tch       
            """)
        else:
            print("May I suggest to learn alphabets?")
    else: 
        print("Typing a skill a few can learn, yeah like 99% people can type")

crossroads(feed)
print(feed)

#-------------------------SCENE 2: The Limbo ----------------------------------------
# This scene is more of a introduction writing need more work
# Need explanations for what happened and what is to be done
if feed['devil_love'] < feed['angel_love']:
    feed['guide'] = 'Dumas'
    feed['guide_type'] = 'Angel'
elif feed['devil_love'] > feed['angel_love']:
    feed['guide'] = 'Karen'
    feed['guide_type'] = 'Devil'
elif feed['devil_love'] == feed['angel_love']:
    feed['guide'] = 'Mirror'
    feed['guide_type'] = ''
else:
    print("Error in guide selection check line: 94")
print(f"""
As your ears stop ringing, you regain conscious in a pure white place.
There is nothing beneath yet you are not falling.
You have no clothes on either, just an advice but you should cover it up.
As you look around you see three shapes before you
One of them comes into focus.
Let me help you out.
This is {feed['guide']} and is {feed['guide_type']} of your own creation
The guide for your journey is decided on your actions
in your last moments.
""")
if feed['guide'] == 'Karen':
    print("""
    Karen looks at you and smiles. 
    \nKaren: Such a promising Overlord, Let's go somewhere you can trample on some hopes and aspirations.\n
    she just flicks her finger and you are with her in a warp.
    """)
if feed['guide'] == 'Dumas':
    print(f"""
    Dumas greets you.
    \nDumas: Hello, {feed['name']}. A village is waiting for a hero a savior.\n
    Dumas touches your back and takes you through a warp
    """)
print(feed)
#--------------------------Scene 3: Rebirth -----------------------------------------
# the scene 