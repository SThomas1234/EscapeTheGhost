import sys, random

def check_options(options, inp):
    val = True
    if inp not in options:
        val = False
    else:
        val = True
    return val


def is_str(inp):
    val = True
    inp.strip()
    if inp.isdigit():
        val = False
    else:
        val = True
    return val


def repeated_inputs(option_number):
    global count1, count2, count3, count4
    if option_number == 1:
        count1 += 1
        return count1

    elif option_number == 2:
        count2+=1
        return count2

    elif option_number == 3:
        count3 +=1
        return count3

    elif option_number == 4:
        count4+=1
        return count4

def get_user_response():
    while True:
        response = input()
        if check_options(options,response) and is_str(response):
            for i in range(len(options)):
                if options[i]==response:
                    option_num=i+1
            val = repeated_inputs(option_num)
            if val==1:
                return option_num
            else:
                print("You already selected this option. Please choose another.")
        else:
            print("Invalid Input. Please try again.")


def dictionary_to_options():
    pass


# def function that checks if user does the same option more than once
print("""You wake up and realize that you have been captured by the infamous Ghost Killer, a serial killer that has 
evaded capture for years. He has left you in a room in an abandoned house. You have a short amount of time to escape 
before he returns to kill you. In the room, there are two doors, a radiator, and a window.
What will you do?
   a.) Check out the window
   b.) Check out the first door
   c.) Check out the second door
""")
counter = 0
options = ["Check out the window", "Check out the first door", "Check out the second door"]
count1, count2, count3, count4 = 0, 0, 0, 0
response = get_user_response()

while counter < 3:
    if response == 1:
        print("The window is sealed")

    elif response == 2 or response == 3:
        print("The door is sealed")

    counter +=1

    if counter ==3:
        break
    print("What will you do?")
    response = get_user_response()


print(""" 
You notice something shine in the corner of the room. Upon closer inspection, you find out that it's a toolbox. What
will you do?
    a.) Use the screwdriver to try and dismantle the first door
    b.) Use the screwdriver to try and dismantle the second door
    c.) Use the screwdriver and hammer to try and unseal the window
    """)

options = ["Use the screwdriver to try and dismantle the first door", "Use the screwdriver to try and dismantle the second door", "Use the screwdriver and hammer to try and unseal the window"]
count1, count2, count3, count4 = 0, 0, 0, 0
response = get_user_response()


while True:
    if response == 1:
        print("The screwdriver head does not match the screws found on this door")
        print("What will you do?")

    elif response == 2:
        print("""The screwdriver head is a match, but, in your weakened state, it is taking awhile to undo the door’s hinges.
              When you finally get to the last screw, the Ghost Killer reappears and stabs you in the heart. Soon after, 
              you bleed to death.""")
        print("GAME OVER") # Player has lost the game
        sys.exit() # Exits the program

    elif response == 3:
        break

    response = get_user_response()

print("""You successfully manage to squeeze the screwdriver between the window’s gap and begin to use the hammer to 
try and pry open the window. However, a few hits in, the screwdriver breaks off. You quickly grab a piece of the 
screwdriver and use it to keep the window open. However, you don’t have much time because the window is extremely
heavy. What will you do now?
    a.) Try to push the window up
    b.) Run and get an item from the toolbox to keep the window open
    c.) Try to smash the window with the hammer """)

options = ["Try to push the window up", "Try to smash the window with the hammer", "Run and get an item from the toolbox to keep the window open"]
count1, count2, count3, count4 = 0, 0, 0, 0
response = get_user_response()

while True:
    if response == 1:
        print("You try to lift up the window, but you don’t have the strength to. What will you do?")

    elif response == 2:
        print("The window does not budge to your attacks. What will you do?")

    elif response == 3:
        break

    response = get_user_response()


print("""Which item will you pick?
    a.) Nails
    b.) Flashlight
    c.) Metal Wedge
    d.) Rope""")

options = ["Nails", "Flashlight", "Metal Wedge", "Rope"]
count1, count2, count3, count4 = 0, 0, 0, 0
response = get_user_response()

while True:
    if response == 1 or response == 4:
        print("That seems ineffective. Select another item.")

    elif response == 2:
        print("That doesn't seem sturdy enough to support the weight of the window. Select another item.")
    elif response == 3:
        print("Good choice. This item is sturdy enough to keep the window open.")
        break
    response = get_user_response()

print("""After placing the wedge under the window, you manage to keep the window open. From there, you hammer away at 
the wedge, causing the window to slowly lift up. Eventually, you manage to lift up the window to a point where you can 
narrowly squeeze through. To secure this point, vertically place the hammer between the window and the wedge. 
Now, how will you get out of the window?
    a.) Jump out
    b.) Use the rope to descend down""")

options = ["Jump out", "Use the rope to descend down"]
count1, count2, count3, count4 = 0, 0, 0, 0
response = get_user_response()


while True:
    if response == 1:
        print("The window is too high from the ground for you to successfully land without injuring yourself. What will you do?")

    elif response == 2:
        break
    response = get_user_response()

print("""The rope is long enough to reach the ground, but where will you tie it to?
   a.) First Door’s Door Knob
   b.) Second Door’s Door Knob 
   c.) Radiator""")

options = ["First Door's Door Knob", "Second Door's Door Knob", "Radiator"]
count1, count2, count3, count4 = 0, 0, 0, 0
response = get_user_response()

while True:
    if response == 1:
        print("The rope is not long enough to extend all the way from the first door (which is in the far corner of the room) to the ground outside. Pick another point to tie the rope from.")

    elif response == 2:
        print("The second door is close enough to the window to attach the rope, but the doorknob itself is rusting. It is likely that it would break due to the pressure of your weight hanging on the rope. Pick another point to tie the rope from.")

    elif response == 3:
        break
    response = get_user_response()

print("""Good choice. The radiator is right below the window, constructed out of metal, and is firmly attached to the floor.
It can definitely support your weight hanging on the rope.\n""")

print("""You hear footsteps approaching. The Ghost Killer is coming, so you don’t have a lot of time. You quickly tie the 
rope around the radiator and descend downwards to the grass below. The footsteps get louder and louder, but you rejoice 
as you get closer and closer to the ground below. As soon as your feet touch the ground, you run for it, as the Ghost Killer 
screams in anger that you escaped his clutches.\n""")

print("YOU WON")
