print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
Welcome to the Treasure Island.
Your mission is find the treasure.
''')

# Stage 1
path_choice= input("You find yourself in an ancient forest."
                    " Two narrow paths stretch out before you."
                    " Do you go 'left' into the dark woods, or 'right' toward the misty hills?\n").lower()
# Stage 2
if path_choice == "right":
    bridge_choice = input("After walking for hours, you reach a sparkling river blocking your way."
                          " A broken bridge lies nearby."
                          " Will you 'wait' to fix the bridge,"
                          " or 'swim' across the rushing water?\n").lower()
    # Stage 3
    if bridge_choice == "wait":
        choose_door = input("Crossing safely, you find an ancient tower with three heavy doors:"
                            " one golden, one silver, and one obsidian black."
                            " Which one do you open?\n").lower()

        if choose_door == "golden":
            print("You open the golden door and find a chamber glittering with treasures. You Win!")
        elif choose_door == "silver":
            print("You step into the silver door and trigger a deadly trap. Game Over.")
        elif choose_door == "obsidian black":
            print("A shadow engulfs you as you enter the black door. You are never seen again. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")

    else:
        print("The current is too strong! You are swept away downstream. Game Over.")

else:
    print("You wander into the mist and lose your way forever. Game Over.")
