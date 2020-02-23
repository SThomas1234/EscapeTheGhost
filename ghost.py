#TODO: Define function to handle exceptions like user entering the wrong things
#TODO: Define function that can handle random events
#TODO: Define function that can manage different paths
#TODO: Create an outline of the story
    # Ghost Killer has captured the player after they got out of school late
    # The player is locked in a room in an abandoned house when they come to
    # The player is trapped in a bare room, fitted with scuff marks
    # As the player comes to their senses, they hear a gravelly voice over what appears to be an intercom. He tells you that ...
import random, sys
def check_options(options, inp):
    while inp not in options:
        print("That is not a valid selection. Please try again")
        inp = input()

# def function that checks if user does the same option more than once
print("""You wake up and realize that you have been captured by the infamous Ghost Killer, a serial killer that has 
evaded capture for years. He has left you in a room in an abandoned house. You have a short amount of time to escape 
before he returns to kill you. In the room, there are two doors, a radiator, and a window.
What will you do?
   a.) Check out the window.
   b.) Check out the first door.
   c.) Check out the second door.
""")
counter = 0
options = ["Check out the window.", "Check out the first door.", "Check out the second door."]
response = input()
check_options(options,response)
# first correct condition entered does print what its supposed to
while counter < 3:
    if response == "Check out the window.":
        print("The window is sealed.")
        #response = input()
    elif response == "Check out the first door." or response == "Check out the second door.":
        print("The door is sealed.")
        #response = input()
    counter +=1
    if counter ==3:
        break
    print("What will you do?")
    response = input()
print(""" 
You notice something shine in the corner of the room. Upon closer inspection, you find out that it's a toolbox. What
will you do?
    a.) Use the screwdriver to try and dismantle the first door.
    b.) Use the screwdriver to try and dismantle the second door.
    c.) Use the screwdriver and hammer to try and unseal the window.
    """)
        #response = input()
response = input()
while True:
    if response == "Use the screwdriver to try and dismantle the first door.":
        print("The screwdriver head does not match the screws found on this door.")
        print("What will you do?")
        response = input()
    elif response == "Use the screwdriver to try and dismantle the second door.":
        print("""The screwdriver head is a match, but, in your weakened state, it is taking awhile to undo the door’s hinges.
              When you finally get to the last screw, the Ghost Killer reappears and stabs you in the heart. Soon after, 
              you bleed to death.""")
        print("GAME OVER") # Player has lost the game
        sys.exit() # Exits the program
    elif response == "Use the screwdriver and hammer to try and unseal the window.":
        break
print("""You successfully manage to squeeze the screwdriver between the window’s gap and begin to use the hammer to 
try and pry open the window. However, a few hits in, the screwdriver breaks off. You quickly grab a piece of the 
screwdriver and use it to keep the window open. However, you don’t have much time because the window is extremely
heavy. What will you do now?
    a.) Try to push the window up.
    b.) Run and get an item from the toolbox to keep the window open.
    c.) Try to smash the window with the hammer. """)
response = input()
# Implement loop for options relating to freeing the window
while True:
    if response == "Try to push the window up.":
        print("You try to lift up the window, but you don’t have the strength to. What will you do?")
        #response = input()
    # Only works correctly for first case, other two options brick program.
    if response == "Try to smash the window with the hammer.":
        print("The window does not budge to your attacks. What will you do?")
        #response = input()
    if response == "Run and get an item from the toolbox to keep the window open.":
        break
    response = input()

print("""Which item will you pick?
    a.) Nails
    b.) Flashlight
    c.) Metal Wedge
    d.) Rope""")
response = input()

# Implement loop for options of what tool to use
while True:
    if response == "Nails" or response == "Rope":
        print("That seems ineffective. Select another item.")

    elif response == "Flashlight":
        print("That doesn't seem sturdy enough to support the weight of the window. Select another item.")
    elif response == "Metal Wedge":
        print("Good choice. This item is sturdy enough to keep the window open.")
        break
    response = input()
# Implement loop for escaping out of the window
print("""After placing the wedge under the window, you manage to keep the window open. From there, you hammer away at 
the wedge, causing the window to slowly lift up. Eventually, you manage to lift up the window to a point where you can 
narrowly squeeze through. To secure this point, vertically place the hammer between the window and the wedge. 
Now, how will you get out of the window?
    a.) Jump out
    b.) Use the rope to descend down""")
response = input()

while True:
    if response == "Jump out":
        print("The window is too high from the ground for you to successfully land without injuring yourself. What will you do?")
    elif response == "Use the rope to descend down":
        break
    response = input()

print("""The rope is long enough to reach the ground, but where will you tie it to?
   a.) First Door’s Door Knob
   b.) Second Door’s Door Knob 
   c.) Radiator""")
response = input()

# Implement options for escaping

while True:
    if response == "First Door's Door Knob":
        print("The rope is not long enough to extend all the way from the first door (which is in the far corner of the room) to the ground outside. Pick another point to tie the rope from.")
    elif response == "Second Door's Door Knob":
        print("The second door is close enough to the window to attach the rope, but the doorknob itself is rusting. It is likely that it would break due to the pressure of your weight hanging on the rope. Pick another point to tie the rope from.")
    elif response == "Radiator":
        break
    response = input()
print("""Good choice. The radiator is right below the window, constructed out of metal, and is firmly attached to the floor.
It can definitely support your weight hanging on the rope.\n""")

print("""You hear footsteps approaching. The Ghost Killer is coming, so you don’t have a lot of time. You quickly tie the 
rope around the radiator and descend downwards to the grass below. The footsteps get louder and louder, but you rejoice 
as you get closer and closer to the ground below. As soon as your feet touch the ground, you run for it, as the Ghost Killer 
screams in anger that you escaped his clutches.\n""")

print("YOU WON")
