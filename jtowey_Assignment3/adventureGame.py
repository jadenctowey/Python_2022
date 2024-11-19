''' 
create a game where the user is traveling through doors 
make a variety of doors to choose from and different ones from different spots 
add a chance of dying and finding the treasure as well as an exit 
make sure there are 3 dif ways to end the game
loop practice!
'''

import random 
death_die = random.randint(1,1000)       #this will generate a random number
room = 1

while room != 0:            #set room to 0 if the person dies and if not they keep going through the loop
    if room == 1:       #entrance to the castle options
        print("You are at the entrance of a castle, there is a latch door below you,\ndo you enter throught the 'latch door' or the 'front gate'?")
        print()
        choice = input("Which entrance do you choose?")     #user input for next room
        print()
        if choice == "latch door":          #PICK LATCH DOOR
            if death_die == 4:              #small chance of death on this first step 
                print("The dragon was there!! He ate you")
                room = 0
            else:           #if they don't die move to room
                room = 2
        elif choice == "front gate":        #PICK FRONT GATE
            if death_die == 130:            #small chance of death on this first step
                print("The guards caught you and you died!")
                room = 0
            else:          #if they don't die move to room 
                room = 3
        else:
            print(choice, "wasn't an option! Try again!")      #if there was a typo have them reset 
            print()
            
#they chose the latch door and lived... here is there next choice --> 
    elif room == 2:     #entrance to the latch door options
        print("You have made it alive through the latch door and into the basement,\ndo you take 'staircase 1', 'staircase 2', or go 'back' to the entrance")
        print()
        choice = input("Which way are you going?")      #user input for room after latch door
        print()
        if choice == "staircase 1":             #PICK STAIRCASE 1
            if death_die > 945:                 #chance of dying 
                print("A gaurd caught you at the top of the stairs! You died!")
                room = 0
            else:                               #if they do not die move to next room
                room = 4
        elif choice == "staircase 2":           #PICK STAIRCASE 2
            if death_die == 45:                 #chance of dying
                print("A gaurd caught you at the top of the stairs! You died!")
                room = 0
            else:                               #if they do not die move to next room
                room = 5
        elif choice == "back":                  #PICK BACK TO ENTRANCE
            room = 1
        else:
            print(choice, "wasn't an option! Try again!")      #if there was a typo have them reset
            print()

#they chose the front gate and lived... here is the next choice --> 
    elif room == 3:     #entrance to the front gate options
        print("You have made it alive through the front gate and are in the main hall,\ndo you enter the 'kitchen', the 'great hall', or go 'back' to the entrance")
        print()
        choice = input("Which way are you going?")      #user input for room after front gate
        print()
        if choice == "kitchen":             #PICK KITCHEN 
            if death_die > 750:                 #chance of dying 
                print("A knife fell and killed you!")
                room = 0
            else:                               #if they do not die move to next room
                room = 6
        elif choice == "great hall":           #PICK GREAT HALL
            if death_die > 345:                 #chance of dying
                print("The treasure was ahead of you but you triggered an alarm! They caught you!")
                room = 0
            else:                               #if they do not die they win
                print("YOU FOUND THE TREASURE AND TOOK THE CASTLE!!! YOU WIN")
                room = 0
        elif choice == "back":                  #PICK BACK TO ENTRANCE
            room = 1
        else:
            print(choice, "wasn't an option! Try again!")      #if there was a typo have them reset
            print()

#they made it up staircase 1 alive ... here is the next choice --> 
    elif room == 4:     #up staircase 1 options
        print("You have made it alive and up the first staircase,\ndo you enter the 'kitchen', go to the 'bedroom' or go 'back' to the basement")
        print()
        choice = input("Which way are you going?")      #user input for room after staircase 1
        print()
        if choice == "kitchen":             #PICK KITCHEN
            room = 6                       #go to room 6 (access from front hall too)
        elif choice == "bedroom":           #PICK BEDROOM
            print("The queen is asleep! Sneak back out")    #leave the room 
            room = 4   
        elif choice == "back":                  #PICK BACK TO BASEMENT
            room = 2
        else:
            print(choice, "wasn't an option! Try again!")      #if there was a typo have them reset
            print()

#they made it up staircase 2 alive ... here is the next choice --> 
    elif room == 5:     #staircase 2 options
        print("You made it up staircase 2 but got cornered. ,\nyou have to battle the guard to keep going!\n One weapon is the best but you may live with any choice,\n do you take the 'sword', the 'ax', or the 'bow and arrow'? OR GO 'back")
        print()
        choice = input("Which weapon will you take?")      #user input for room after staircase 2
        print()
        if choice == "sword":             #PICK SWORD 
            if death_die > 500:
                print("You were defeated! He is much more skilled than you")
                room = 0
            else:
                print("You beat him!")
                print()
                room = 7
        elif choice == "ax":           #PICK AX
            if death_die > 200:
                print("It was too heavy and the gaurd beat you!")
                room = 0
            else:
                print("You beat him!")
                print()
                room = 7
        elif choice == "bow and arrow":     #PICK BOW AND ARROW
            if death_die > 950:
                print("He had a sheild and made it to you first, so you died!")
                room = 0
            else:
                print("You beat him!")
                print()
                room = 7
        elif choice == "back":                  #PICK BACK TO BASEMENT
            room = 2
        else:
            print(choice, "wasn't an option! Try again!")      #if there was a typo have them reset

#staircase 1 or main hall made it through to the kitchen --> 
    elif room == 6:     #kitchen options
        print("You have made it to the kitchen and there is an old woman sitting alone, \n do you 'approach' her or run to the top of 'staircase 2'?")
        print()
        choice = input("What will you do?")      #user input for in the kitchen
        print()
        if choice == "approach":             #PICK TALK TO OLD WOMAN
            print("The old woman speaks to you...\n'good thing you came to me! if you had run by you would have had a battle! I will escort you to the magic room'")
            room = 7                       
        elif choice == "staircase 2":           #PICK STAIRCASE 2 
            room = 5 
        else:
            print(choice, "wasn't an option! Try again!")      #if there was a typo have them reset
            print()

#the magic room, either win the battle or talk to the old lady to get here... --> 
    elif room == 7:     #the magic room
        print("You have entered the magic room.\n you can either 'risk' a battle for all the treasure or 'leave' the castle alive")
        print()
        choice = input("What will you do?")      #leave or play game input
        print()
        if choice == "risk":             #PICK RISK
            print("You chose to fight for the treasure...\n there is a 'map' of the castle, a 'box', and a 'sword'")
            choice = input("What will you take?")
            if choice == "map":
                if death_die > 500:
                    print("You fought through the castle and found the treasure! YOU WIN")
                    room = 0
                else:
                    print("The map was empty and a witch found you before you could run! She took you away\n YOU LOSE")
            elif choice == "box":
                print("There was posion inside!!! YOU DIED")
                room = 0
            elif choice == "sword":
                if death_die > 600:
                    print("You battled your way through the castle, but they caught you and put you in jail!")
                    room = 0
                else:
                    print("You fought off the gaurds! Took the treasure! And ran out safely! YOU WIN!")
                    room = 0                     
        elif choice == "leave":           #PICK LEAVE
            print("You made it out safely with no treasure. Try again...")    #leave the game 
            print()
            room = 1
        else:
            print(choice, "wasn't an option! Try again!")      #if there was a typo have them reset
            print()
    else:
        print("Something went wrong... try again.")

