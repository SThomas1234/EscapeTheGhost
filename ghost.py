import sys, random


def check_options(options, inp):
    # This function checks to see if the user's input can be found in the list of potential options per situation
    # The list of options is represented by the options variable found before each while True loop.
    # If the input is found in the list, the function returns True and False otherwise.

    val = True
    if inp not in options:
        val = False
    else:
        val = True
    return val


def is_str(inp):
    # This function checks an input's validity by checking to see if it's a string or not
    # If the input is not a string, the function returns True and False otherwise.

    val = True
    inp.strip()
    if inp.isdigit():
        val = False
    else:
        val = True
    return val


def repeated_inputs(option_number):
    # This function checks to see if the user has entered an option multiple times
    # The global variables represent the amount of times each input has been entered
    # Every time the user enters an input, this function is called to increment the respective count variable.

    global option1_frequency,  option2_frequency,  option3_frequency,  option4_frequency
    if option_number == 1: 
        option1_frequency += 1 
        return option1_frequency # Represents frequency of the first option

    elif option_number == 2: 
        option2_frequency+=1 
        return option2_frequency # Represents frequency of the second option

    elif option_number == 3: 
        option3_frequency +=1 
        return option3_frequency # Represents frequency of the third option

    elif option_number == 4: 
        option4_frequency+=1 
        return option4_frequency # Represents frequency of the fourth option


def get_user_response():  # Written with assistance from Professor Boady
    # The purpose of this function is to ensure that the input the user provided is valid in all respects (in the options list, a string, not repeated)
    # If these conditions are met, the function keeps executing, and if not it jumps to the last else statement.
    # The function first asks the user for input, and uses the check_options and is_str functions to check for initial validity (in the list of potential options, a string)
    # Then the function uses the for loop to find the value of i (represents the option_number described in the repeated_inputs() function)
    # The function then passes the value of i into the repeated_inputs to check if has already been used. If so, it tells the user the input was repeated. If not, it returns the option number.

    while True:
        response = input()
        if check_options(options,response) and is_str(response):
            for i in range(len(options)):
                if options[i] == response:
                    option_num=i+1
            val = repeated_inputs(option_num)
            if val==1:
                return option_num
            else:
                print("You already selected this option. Please choose another.")
        else:
            print("Invalid Input. Please try again.")


def random_event(outcomes):
    # This function creates the possibility of additional lose conditions in addition to the one presented in the game's second situation.
    # It chooses a random element from the passed in list, outcomes, which list potential lose scenarios
    # If the value of "val," determined by the random.randint() function is <=5, the original outcome for the response will still occur
    # If val >5, however, the new condition will exectute and the player will lose the game.

    val = random.randint(0,10)
    element = random.choice(outcomes) # Chooses a random element from the outcomes list.
    if val <= 5:
        pass
    else:
        print(element)
        print("GAME OVER")
        sys.exit()


print("""You wake up and realize that you have been captured by the infamous Ghost Killer, a serial killer that has 
evaded capture for years. He has left you in a room in an abandoned house. You have a short amount of time to escape 
before he returns to kill you. In the room, there are two doors, a radiator, and a window.
What will you do?
   a.) Check out the window
   b.) Check out the first door
   c.) Check out the second door
""")

counter = 0
options = ["Check out the window", "Check out the first door", "Check out the second door"] # Establishes options for scenario 1
option1_frequency,  option2_frequency,  option3_frequency,  option4_frequency = 0, 0, 0, 0
response = get_user_response() # Gets user response and checks for its validity

while counter < 3:
    # This while loop is responsible for dealing with user responses to the first scenario: exploring the room they are trapped in
    # The point of this while True loop is for the user to explore all given possibilities before advancing to the next scenario.
    # To break out of the loop, the while loop operates off a counter variable which is incremented after every unique option choice.

    if response == 1: # Conditional checks if the user selected the first option in the "options" list
        print("The window is sealed")

    elif response == 2 or response == 3: # Conditional checks if the user selected the second or third options in the "options" list
        print("The door is sealed")

    counter +=1 # Increments count after each valid user response

    if counter ==3: # Exits the while True loop
        break
    print("What will you do?")
    response = get_user_response() #  Gets user response and checks for its validity

print(""" 
You notice something shine in the corner of the room. Upon closer inspection, you find out that it's a toolbox. What
will you do?
    a.) Use the screwdriver to try and dismantle the first door
    b.) Use the screwdriver to try and dismantle the second door
    c.) Use the screwdriver and hammer to try and unseal the window
    """)

options = ["Use the screwdriver to try and dismantle the first door",
           "Use the screwdriver to try and dismantle the second door",
           "Use the screwdriver and hammer to try and unseal the window"]  # Updates Options for scenario 2

option1_frequency,  option2_frequency,  option3_frequency,  option4_frequency = 0, 0, 0, 0 # Resets count variables for the new responses
response = get_user_response() #  Gets user response and checks for its validity
outcomes = ["You took too long trying to unscrew the door. The Ghost Killer has found and killed you.",
            "You made too much noise trying to unscrew the door. The Ghost Killer has found and killed you."] # Updates lose scenarios for scenario 2
while True:
    # This while True loop is responsible for handling the user responses to the second scenario in the game: the player's intial escape attempt.
    # The point of the loop is to introduce a lose condition and demonstrate to the user that they are sealed in (supposedly).
    # To break out of the loop, the player must select the third option: using tools to try and unseal the window.

    if response == 1: # Conditional checks if the user selected the first option in the "options" list
        random_event(outcomes) # Checks to see if the normal outcome or the lose condition executes.
        print("The screwdriver head does not match the screws found on this door")
        print("What will you do?")

    elif response == 2: # Conditional checks if the user selected the second option in the "options" list
        print("""The screwdriver head is a match, but, in your weakened state, it is taking awhile to undo the door’s hinges.
              When you finally get to the last screw, the Ghost Killer reappears and stabs you in the heart. Soon after, 
              you bleed to death.""")
        print("GAME OVER") # Player has lost the game
        sys.exit() # Exits the program

    elif response == 3: # Conditional checks if the user selected the third option in the "options" list
        break # Breaks out of the while True loop, progresses onto the next scenario

    response = get_user_response() # Gets user responses and checks for its validity

print("""You successfully manage to squeeze the screwdriver between the window’s gap and begin to use the hammer to 
try and pry open the window. However, a few hits in, the screwdriver breaks off. You quickly grab a piece of the 
screwdriver and use it to keep the window open. However, you don’t have much time because the window is extremely
heavy. What will you do now?
    a.) Try to push the window up
    b.) Run and get an item from the toolbox to keep the window open
    c.) Try to smash the window with the hammer """)

options = ["Try to push the window up", "Try to smash the window with the hammer", # Updates options for scenario 3
           "Run and get an item from the toolbox to keep the window open"]

outcomes = ["You took too long. The Ghost Killer has found and killed you.",
            "You made too much noise. The Ghost Killer has found and killed you."] # Updates extra lose scenarios for scenario 3

option1_frequency,  option2_frequency,  option3_frequency,  option4_frequency = 0, 0, 0, 0 # Resets count variables for the new responses
response = get_user_response() # Gets user response and checks for its validity.

while True:
    # This while True loop is responsible for handling the game's third scenario: trying to get the window to budge
    # The loop breaks when the user enters the third option: getting an item from the toolbox to get the window open.

    if response == 1: # Conditional checks if the user selected the first option in the "options" list
        random_event(outcomes) # Checks to see if the normal outcome or the lose condition executes.
        print("You try to lift up the window, but you don’t have the strength to. What will you do?")

    elif response == 2: # Conditional checks if the user selected the second option in the "options" list
        random_event(outcomes) # Checks to see if the normal outcome or the lose condition executes.
        print("The window does not budge to your attacks. What will you do?")

    elif response == 3: # Conditional checks if the user selected the third option in the "options" list
        break

    response = get_user_response() # Gets user response and checks for its validity.


print("""Which item will you pick?
    a.) Nails
    b.) Flashlight
    c.) Metal Wedge
    d.) Rope""")

options = ["Nails", "Flashlight", "Metal Wedge", "Rope"] # Updates options for fourth scenario
option1_frequency,  option2_frequency,  option3_frequency,  option4_frequency = 0, 0, 0, 0 # Resets count variables for new responses
response = get_user_response() # Gets user response and checks for its validity.

while True:
    # This while True loop handles the user's responses to the game's fourth scenario: deciding what tool to use to keep the window open
    # The loop breaks when the user enters the third option: choosing the metal wedge to keep the window open.

    if response == 1 or response == 4: # Conditional checks if the user selected the first or fourth option in the "options" list
        print("That seems ineffective. Select another item.")

    elif response == 2: # Conditional checks if the user selected the second option in the "options" list
        print("That doesn't seem sturdy enough to support the weight of the window. Select another item.")

    elif response == 3: # Conditional checks if the user selected the third option in the "options" list
        print("Good choice. This item is sturdy enough to keep the window open.")
        break
    response = get_user_response() # Gets user response and checks for its validity.


print("""After placing the wedge under the window, you manage to keep the window open. From there, you hammer away at 
the wedge, causing the window to slowly lift up. Eventually, you manage to lift up the window to a point where you can 
narrowly squeeze through. To secure this point, vertically place the hammer between the window and the wedge. 
Now, how will you get out of the window?
    a.) Jump out
    b.) Use the rope to descend down""")

options = ["Jump out", "Use the rope to descend down"] # Resets options for the fifth scenario
option1_frequency,  option2_frequency,  option3_frequency,  option4_frequency = 0, 0, 0, 0  # Resets count variables for new response
response = get_user_response() # Gets user response and checks for its validity.


while True:
    # This while True loop is responsible for hanlding user responses to the game's fifth scenario: Deciding how the player will get out of the window
    # The loop breaks when the user enters the second option: Deciding to use the rope to descend down.

    if response == 1: # Conditional checks if the user selected the first option in the "options" list
        print("The window is too high from the ground for you to successfully land without injuring yourself. What will you do?")

    elif response == 2: # Conditional checks if the user selected the second option in the "options" list
        break
    response = get_user_response() # Gets user response and checks for its validity.

print("""The rope is long enough to reach the ground, but where will you tie it to?
   a.) First Door’s Door Knob
   b.) Second Door’s Door Knob 
   c.) Radiator""")

options = ["First Door's Door Knob", "Second Door's Door Knob", "Radiator"] # Resets options for game's final scenario.
option1_frequency,  option2_frequency,  option3_frequency,  option4_frequency = 0, 0, 0, 0  # Resets count variables for game's final scenario.
response = get_user_response() # Gets user response and checks for its validity.

outcomes = ["You took too long to find an anchor for the rope. The Ghost Killer has found and killed you.",
            "You made too much while dragging the rope. The Ghost Killer has found and killed you."] # Reset outcomes for game's final scenarios.
while True:
    # This while True loop manages user responses to the game's final scenario: where the player will anchor the rope to escape out the window
    # To break out of the loop, the user must pick the third option: tying the rope to the radiator next to the window.

    if response == 1: # Conditional checks if the user selected the first option in the "options" list
        random_event(outcomes) # Checks to see if the normal outcome or the lose condition executes.
        print("The rope is not long enough to extend all the way from the first door (which is in the far corner of the"
              " room) to the ground outside. Pick another point to tie the rope from.")

    elif response == 2: # Conditional checks if the user selected the second option in the "options" list
        random_event(outcomes) # Checks to see if the normal outcome or the lose condition executes.
        print("The second door is close enough to the window to attach the rope, but the doorknob itself is rusting. "
              "It is likely that it would break due to the pressure of your weight hanging on the rope. "
              "Pick another point to tie the rope from.")

    elif response == 3: # Conditional checks if the user selected the third option in the "options" list
        break
    response = get_user_response() # Gets user response and checks for its validity.

print("""Good choice. The radiator is right below the window, constructed out of metal, and is firmly attached to the floor.
It can definitely support your weight hanging on the rope.\n""")

print("""You hear footsteps approaching. The Ghost Killer is coming, so you don’t have a lot of time. You quickly tie the 
rope around the radiator and descend downwards to the grass below. The footsteps get louder and louder, but you rejoice 
as you get closer and closer to the ground below. As soon as your feet touch the ground, you run for it, as the Ghost Killer 
screams in anger that you escaped his clutches.\n""")  # Final Message

print("YOU WON")  # Player has completed and won the game.
