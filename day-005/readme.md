# Day 005 — PyPassword Generator

```
 /\   architectray · 
/__\  100 Days of Python · 2026-07-01
```

**Concepts:** control flow (`for` loops), lists, strings, `random.choice()`, `random.shuffle()`, string vs. list accumulation
**The lesson:** building the same result two different ways side by side — an
easy-mode string and a hard-mode shuffled list — and learning why "get one
step working first" matters more than writing the whole thing at once.

---

## The Project

A password generator that asks the user how many letters, symbols, and
numbers they want, then builds a password two ways: an **easy-mode**
password (characters added in the order they're requested — all
letters, then all symbols, then all numbers) and a **hard-mode**
password (the same characters collected into a list, then shuffled
into random order before being joined into a string).

**The two modes**
```
Easy Mode  →  letters + symbols + numbers   (predictable order)
Hard Mode  →  same pool, shuffled           (random order)
```

**Python concepts**
- three separate character-pool lists (`letters`, `numbers`, `symbols`)
- `int(input())` to capture how many of each type are wanted
- **string accumulation** (`+=`) for the easy-mode password
- **list accumulation** (`.append()`) for the hard-mode password
- `random.choice()` to pick one random item from a list
- `random.shuffle()` to reorder a list in place
- `"".join(list)` to turn a shuffled list of characters back into a string

---

## The Code (as written)

```python
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
    # Update User Password Variable with Random Selection of Symbold
    user_password += random.choice(symbols)
    user_password_hard.append(random.choice(numbers))

# Loop Iteration Defined by User Input
for number in range(nr_numbers):
    # Update User Password Variable with Random Selection of Symbold
    user_password += random.choice(numbers)
    user_password_hard.append(random.choice(symbols))

print(f"Your New Password (Easy-Mode): {user_password}")
random.shuffle(user_password_hard)
shuffled_password = "".join(user_password_hard)
print(f"Your New Password (Hard-Mode): {shuffled_password}")
```

Each `for` loop does double duty: it builds the easy-mode string with
`+=` and pushes to the hard-mode list with `.append()` in the same
pass, so both passwords are constructed from a single set of loops
rather than looping over the pools twice.

---

## What I Learned

- **Strings and lists accumulate differently.** `user_password += random.choice(letters)`
  builds a new string each time (strings are immutable), while
  `user_password_hard.append(...)` grows the same list in place.
  Both reach the same kind of end result — a sequence of characters —
  but get there by different mechanisms.
- **`random.shuffle()` mutates in place and returns `None`.** It
  reorders `user_password_hard` directly rather than returning a new
  shuffled list, which is why the shuffle call sits on its own line
  *before* the `.join()`, not chained onto it.
- **`"".join(list)` turns a list of single characters back into a
  string.** The empty string (`""`) before `.join` is the separator —
  here it means "no separator," so the characters sit right next to
  each other, which is what a password needs.
- **One loop, two jobs.** Building both password variables inside the
  same `for` loop (rather than looping over each pool twice — once
  for easy-mode, once for hard-mode) means each random character pull
  happens once, which is closer to how the real logic should scaffold
  reuse when possible.

---

## Improvements I Recognised

Reviewing my own code, these are the changes I'd make — all within
the concepts taught so far:

- **Easy-mode isn't shuffled.** Building it block-by-block (all
  letters, then all symbols, then all numbers) means the *type* of
  each character is fully predictable from its position — a
  meaningfully weaker password than hard-mode's shuffled version,
  even before the category-swap bug above is considered.
- **No validation on the three counts.** If a user enters `0` for
  all three, both password variables print as empty strings with no
  explanation. A short check — e.g. confirming at least one count is
  greater than zero — would make the "no password possible" case
  visible instead of silent.

---

## Notes From Today

Today's notes were less about syntax and more about process:

- **Solve one step at a time.** Get a single piece working (e.g. just
  the easy-mode letters loop) before layering in the next piece
  (symbols, then numbers, then the hard-mode list, then the shuffle).
  Trying to write the whole generator in one pass is exactly how a
  bug like the crossed categories above slips in unnoticed — each
  loop looks locally correct at a glance, and the swap only becomes
  obvious if each loop is checked in isolation.
- **Scaffold the simplest version first.** A working password
  generator that just does letters is a real milestone — build up
  from there rather than trying to reach the finished version
  directly.
- **Be deliberate about IDE auto-fill.** Sometimes it hands you the
  answer before you've worked through the logic yourself, which
  skips the learning. Other times it's confidently wrong — auto-fill
  is a guess based on pattern, not a check against what the code
  should actually do, and either way it's worth turning off while
  a concept is still being learned properly.

---

## Run

```bash
python main.py
```
Enter the number of letters, symbols, and numbers you want when
prompted. Note: hard-mode's category-swap bug (see above) means the
counts of symbols vs. numbers in the *hard-mode* output currently
don't match what was typed in — this will be fixed once `.lower()`-style
targeted debugging is introduced, or simply by swapping `numbers` and
`symbols` back in the two `.append()` calls.

---

## What I'm Taking Forward

Two ways of building the same thing, side by side, is a good way to
see a bug that a single approach would have hidden — easy-mode's
correct category logic made the hard-mode swap visible by contrast.
The bigger habit, though, is the one from today's notes: build in the
smallest possible working steps, and don't let the IDE's guess stand
in for actually working through the logic.

```
─ Be joyful in hope, patient in affliction, faithful in prayer. ──
```
