# Day 002 — Bill Tip Calculator

```
 /\   architectray
/__\  100 Days of Python · 2026-06-28
```
**Concepts:** data types, operations, type conversion.
**The real lesson:** understanding how types interact, why conversion matters, and how a simple percentage becomes a clean multiplier.

---

## The Project

A command-line tip calculator that takes a restaurant bill, a tip percentage, and a number of people — and returns how much each person owes. The Python is straightforward. The thinking behind it is not.

---

## What the Code Does

1. Prompts the user for the total bill amount
2. Asks for a tip percentage (10, 12, or 15)
3. Asks how many people are splitting the bill
4. Calculates the total including tip
5. Divides by the number of people
6. Rounds to 2 decimal places
7. Prints a formatted receipt

---

## Python Concepts

**Data types**
Three types in play: `float` for the bill (money needs decimals), `int` for tip percentage and number of people (whole numbers only), and the implicit `float` that results from the calculation.

**Type conversion**
`input()` always returns a string. Wrapping it in `float()` or `int()` converts it immediately at capture — so the variable is already the right type before it's used anywhere. No conversion needed later.

**Operations**
Standard arithmetic: multiplication, division. The order matters — bill × multiplier first, then divide by people.

**`round()`**
`round(value, 2)` constrains the result to 2 decimal places. Essential for money — floating point arithmetic produces results like `14.999999999` without it.

---

## The Real Lesson — The Tip as a Multiplier

The non-obvious part of this project is the tip calculation itself.

A tip percentage is a fraction of 100. To add a tip to a bill without calculating the tip separately and adding it, you can express the whole thing as a single multiplier:

```
tip_percent = (100 + tip) / 100
```

A 10% tip becomes `110 / 100 = 1.1`. Multiply the bill by 1.1 and you get the bill plus 10% in one step. No intermediate variable needed. One operation, correct result.

This is a pattern worth internalising — percentage increases as multipliers appear constantly in financial calculations.

---

## Type Interaction — Where It Gets Interesting

```python
bill = float(input(...))   # float
tip  = int(input(...))     # int
people = int(input(...))   # int

tip_percent = (100 + tip) / 100   # int + int / int → float
                                   # Python 3 division always returns float

price_per_person = (bill * tip_percent) / people  # float * float / int → float
```

Python 3 promotes types upward through operations — an `int` divided by an `int` returns a `float`. Once a `float` enters a calculation, the result is `float`. Understanding this chain means you know what type you're working with at every step without guessing.

---

## Run

```bash
python main.py
```

**Example session:**
```
Welcome to the tip calculator!
What was the total bill? $124.50
What percentage tip would you like to give? 10 12 15 15
How many people to split the bill? 4

RECEIPT
----
The Total Bill is: $124.5
Each Person(s) is required to pay: $35.79

Thank You!
```

---

## What I'm Taking Forward

Day 2 was about types — not just knowing they exist, but understanding why they matter at the point of capture, how they interact through operations, and what Python does silently when types mix. The tip-as-multiplier pattern is the kind of thinking that separates someone who can write a calculator from someone who understands what the calculator is actually doing.

---

*── Change is a function of Focus, Clarity, and Desire ──*
