#variables to track where you are
room = "enterance"
keys = 0
game_running = True

def start_room():
    print("You are at the enterance of a garden. There is a path leading north to a fountain.")
    print("Beautiful flowers line the path, but you're too nervous to appreciate them.")
    print("You can also see a solid wall with a door and a keyhole to the east.")
    print("\n")
    print("If you would like to go north, type 'n'. If you would like to go east, type 'e'.")
    direction = input("Which direction would you like to go? ")
    print("\n")
    if direction == "n":
        fountain_room()
    elif direction == "q":
        end_game()
    elif direction == "e":
        door_room()
    else:
        print("Uh Oh, you can't go that way.")
        start_room()

def door_room():
    global keys
    if keys > 0:
        print("You use a key to unlock the door and enter the room.")
        print("Inside, you hear the maids busy at work, preparing breakfast.")
        print("Thank goodness you found your key in time, you would have gotten such a scolding from the Butler if you haden't.")
        print("Congratulations, you have won the game!")
        end_game()
    else:
        print("The door is locked. You need a key to open it.")
        start_room()

def fountain_room():
    print("You are at a beautiful marble fountain. The water gushes from a statue of a mermaid.")
    print("You can see the enterace to the south, and to the west is a small shed.")
    print("\n")
    print("If you would like to go south, type 's'. If you would like to go west, type 'w'.")
    direction = input("Which direction would you like to go? ")
    print("\n")
    if direction == "s":
        start_room()
    elif direction == "q":
        end_game()
    elif direction == "w":
        shed_room()
    else:
        print("Uh Oh, you can't go that way.")
        start_room()

def shed_room():
    print("You see a small shed. The door is slightly ajar, and you can hear some scratching in the background.")
    print("As you push open the door, a small tabby cat jumps out and runs away.")
    print("In your haste to dodge the cat, you bump into the wall and hear a clink as a small key falls from the shelf.")
    global keys
    keys += 1
    print("You now have", keys, "key(s).")
    direction = input("Press any key and 'enter' to continue.")
    print("\n")
    if direction != "":
        fountain_room()

#future expansion: add a puzzle where you have to lure the cat out
#setup the fact that you're the gardener
#and you need to get into the shed for your key, and also tools for flowers
#because you're setting up the flowers for the day

def end_game():
    global game_running
    game_running = False
    print("Thank you for playing!")


#main gameplay loop
while game_running:
    start_room()


