# ============================================================
#  100 Days of Python  ·  Day 002 — Bill Tip Calculator
# ------------------------------------------------------------
#  Author   : architectray
#  Created  : 2026-06-28
#  Project  : 100 Days of Python
#  Concepts : [data types, operations, type conversations]
# ============================================================

"""Bill Tip Calculator — calculates how much each person should pay
when splitting a restaurant bill. """

# ── BEGIN ───────────────────────────────────────────────────

# Welcome Message Greeting
print("Welcome to the tip calculator!")

# User Input Total Bill Amount
bill = float(input("What was the total bill? $"))

# User Input Total Tip Percent (Expressed in Whole Number)
tip = int(input("What percentage tip would you like to give? 10 12 15 "))

# How do you express the "tip" variable, as a percentage?
# A percentage is a fraction of 100. 100% represents the whole. (e.g. 100 / 100 = 1.0.)
# To add a tip, increase the whole (100%) by the tip percentage.
# The final value is a multiplier that can be applied to the bill.
tip_percent = (100 + tip) / 100

# User Input Number of Person(s)
people = int(input("How many people to split the bill? "))

# Calculate Price per Person
price_per_person = (bill * tip_percent) / people

# Convert to 2 Decimal Places
rounded_price_per_person = round(price_per_person, 2)

# Print Final Result
print("\nRECEIPT\n----")
print(f"The Total Bill is: ${bill} \nEach Person(s) is required to pay: ${rounded_price_per_person}\n\nThank You!")


# ── END ──────────────────────────────────────────────────────────────
# Change is a function of Focus, Clarity, and Desire
# ─────────────────────────────────────────────────────────────────────
