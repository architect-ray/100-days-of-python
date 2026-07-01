import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Set Empty String Variable to Store User Password - Easy Mode
user_password = ""

# Set Empty List Variable to Store User Password - Hard Mode
user_password_hard = []

# Loop Iteration Defined by User Input
for letter in range(nr_letters):
    # Update User Password Variable with Random Selection of Letters
    user_password += random.choice(letters)
    user_password_hard.append(random.choice(letters))

# Loop Iteration Defined by User Input
for symbol in range(nr_symbols):
    # Update User Password Variable with Random Selection of Symbols
    user_password += random.choice(symbols)
    user_password_hard.append(random.choice(symbols))

# Loop Iteration Defined by User Input
for number in range(nr_numbers):
    # Update User Password Variable with Random Selection of Symbols
    user_password += random.choice(numbers)
    user_password_hard.append(random.choice(numbers))

print(f"Your New Password (Easy-Mode): {user_password}")
random.shuffle(user_password_hard)
shuffled_password = "".join(user_password_hard)
print(f"Your New Password (Hard-Mode): {shuffled_password}")

# Notes for today -
# Always think through the solution one step at time. Try and get one step working first.
# Always think through the simplest version and scaffold-as-you-go.
# Remove auto-fill from the IDE's sometimes you don't want to be given the answer immediately,
# or other time the auto-fill is vastly incorrect, it does actually know what you want, it's only guess-work.
