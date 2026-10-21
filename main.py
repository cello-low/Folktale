#variables to track where you are
room = "start"
keys = 0
game_running = True
start_room_counter = 0
shed_counter = True
has_treat = False

def start_room():
    global start_room_counter
    print("You are at the enterance of a garden.")
    if start_room_counter == 0:
        start_room_counter +=1
        start_first_enter()
    elif start_room_counter == 1:
        start_room_counter +=1
        start_second_enter()
    print("You can see the main house's door, which has a small keyhole, to the east. There is a shed to the north.")
    print("\n")
    print("If you would like to go north, type 'n'. If you would like to go east, type 'e'.")
    direction = input("Which direction would you like to go? ")
    print("\n")
    if direction == "n":
        shed_room()
    elif direction == "q":
        end_game()
    elif direction == "e":
        door_room()
    else:
        print("Uh Oh, you can't go that way.")
        start_room()
#not room
def start_first_enter():
    print("Beautiful flowers line the path, but you're too nervous to appreciate them.")
    print("That's because today's the big day, and you're tasked with arranging the flowers.")
    print("But in order to get into the house to arrange the flowers, you need your keys.")
    print("But.\nYou've lost them.")

def start_second_enter():
    print("Wait...\n Is that a can of the Deluxe Kitty Treats?!?!")
    print("Someone must have left it here.")
    print("It's Sir Purrington's favorite treat.")
    global has_treat
    has_treat = True
    print("You now have a treat.\n")

def door_room():
    global keys
    if keys > 0:
        print("You use a key to unlock the door and enter the room.")
        print("Inside, you hear the maids busy at work, preparing breakfast.")
        print("Thank goodness you found your key in time, you would have gotten such a scolding from the Butler if you haden't.")
        print("Congratulations, you have won the game!")
        end_game()
        exit()
    else:
        print("The door is locked. You need a key to open it.\n")
        start_room()

def shed_room():
    global shed_counter
    global has_treat

    if shed_counter:
        shed_counter = False
        shed_first_enter()
        direction = input("Press any key and 'enter' to continue.")
        print("\n")
        start_room()

    if has_treat:
        global keys
        keys += 1
        print("You hear Sir Purrington land on the floor of the shed, and you see the door swing open.")
        print("Sir Purrington steps out of the shed, and starts feasting upon the treat.")
        print("Upon entering the shed, you see a small key on the back shelf.")
        print(f"You now have {keys} small key.")
        direction = input("Press any key and 'enter' to continue.")
        print("\n")
        if direction != "":
            start_room()

#not room
def shed_first_enter():
    print("Unfortunantly, the door is shut from the other side. But, you can hear a faint meowing.")
    print("There's only one kitty on these grounds: Sir Purrington the Perfect.")
    print("He's a brilliant kitty, and he is known for opening doors with ease.")
    print("Perhaps you could bribe him out with... I don't know, a treat?")
    print("\n")

def end_game():
    global game_running
    game_running = False
    print("Thank you for playing!")

#main gameplay loop
while game_running:
    start_room()


