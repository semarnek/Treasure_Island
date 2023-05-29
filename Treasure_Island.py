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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

answer = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n")
if answer.lower() == "left":
    answer = input("You come to a lake. There is an island in the middle of the lake. "
                   "Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
    if answer.lower() == "wait":
        answer = input("You arrive at the island unharamed. There is a house with 3 doors. "
                       "One red, one yellow and one blue. Which color do you choose?\n")
        if answer.lower() == "yellow":
            print("Well done! You found the treasure! You win!\n")
        elif answer.lower() == "red":
            print("You burned by fire. Game over :(\n")
        elif answer.lower() == "blue":
            print("You eaten by beasts. Game over :(\n")
        else:
            print("Game over :(\n")


    else:
        print("You attacked by a trout. Game over :(\n")

else:
    print("You fall into a hole. Game over :(\n")


