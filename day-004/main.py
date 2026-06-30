import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Define the Players
player_one = 0
player_two = 0

# Define the controls
game_options = ["rock", "paper", "scissors"]

# Test Controls
print(game_options[0])
print(game_options[1])
print(game_options[2])
print("")

# Define Player One Selection
player_one_selects = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
print("")
print(f"Player One Selected : {game_options[player_one_selects]}\n")

# Define Player Two Selection (Randomly Generated)
player_two_select = random.randint(0, 2)
print(f"Player Two Selected Option : {game_options[player_two_select]}\n")

# Define Rules of Engagement: # RR - RP - RS - PP - PR - PS - SS - SR - SP
if game_options[player_one_selects] == game_options[player_two_select]:
    print("Draw")
elif game_options[player_one_selects] == "rock" and game_options[player_two_select] == "paper":
    print("Player Two Wins")
elif game_options[player_one_selects] == "rock" and game_options[player_two_select] == "scissors":
    print("Player One Wins")
elif game_options[player_one_selects] == "paper" and game_options[player_two_select] == "rock":
    print("Player One Wins")
elif game_options[player_one_selects] == "paper" and game_options[player_two_select] == "scissors":
    print("Player Two Wins")
elif game_options[player_one_selects] == "scissors" and game_options[player_two_select] == "rock":
    print("Player Two Wins")
elif game_options[player_one_selects] == "scissors" and game_options[player_two_select] == "paper":
    print("Player One Wins")



