print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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


# User Options - Left, Right,
first_option = str(input("First Option. Pick one: Left, or Right..."))
if first_option == "Right":
    # Right - Game Over
    print("Fall into a hole.\nGame Over")
elif first_option == "Left":
    # Left - Swim, or Wait
    second_option = str(input("Second Option. Pick one: Swim, or Wait..."))
    # Swim - Game Over
    if second_option == "Swim":
        print("Attacked by trout.\nGame Over.")
    elif second_option == "Wait":
        # Wait - Pick a Door
        third_option = str(input("Third Option. Pick a Door: Red, Blue, or Yellow..."))
        if third_option == "Blue":
            # Blue - Game Over
            print("Eaten by beasts.\nGame Over.")
        elif third_option == "Red":
            # Red - Game Over
            print("Burned by Fire.\nGame Over.")
        elif third_option == "Yellow":
            # Yellow - You Win!
            print("You Win!")


