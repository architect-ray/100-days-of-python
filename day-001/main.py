# ============================================================
#  100 Days of Python  ·  Day 001 — Band Name Generator
# ------------------------------------------------------------
#  Author   : architectray
#  Created  : 2026-06-27
#  Project  : 100 Days of Python
#  Concepts : [variables, input, string concatenation]
# ============================================================

"""Band Name Generator — suggests a band name from a user's
hometown and a pet's name."""

# ── BEGIN ───────────────────────────────────────────────────

# Create a Greeting for the User
greeting = "Hello, "

# Assign the Users' Name
user_name = input("What is your name? ")

# Greet the User
print(greeting + user_name + "!")

# Ask the user for the city that they grew up in and store it in a variable.
city_name_input = input("Enter City Name: ")

# Ask the user for the name of a pet and store it in a variable.
pet_name_input = input("Enter Pet Name: ")

# Combine the name of their city and pet and show them their band name.
cat_band_name = city_name_input + " " + pet_name_input
print("Your Band Name is... ", cat_band_name)


# ── END ───────────────────────────────────────────────────────────────────
# On any given day, you can massively change the direction of your life
# ───────────────────────────────────────────────────────────────────────────


