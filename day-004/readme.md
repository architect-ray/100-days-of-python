# Day 004 — Rock, Paper, Scissors

```
 /\   architectray · 
/__\  100 Days of Python · 2026-06-30
```

**Concepts:** control flow, `if` / `elif`, comparison logic, `random`, ASCII art, list indexing
**The lesson:** translating a set of pairwise rules (RR, RP, RS, PP, PR, PS, SS, SR, SP) into
compound conditionals — and discovering how easy it is for one branch to slip through
the cracks.

---

## The Project

A two-player Rock, Paper, Scissors game. Player One picks by typing a
number (0, 1, or 2); Player Two is the computer, picking at random.
The two choices are compared against every possible pairing to decide
a winner, a loser, or a draw.

**The matchups**
```
Rock     beats  Scissors
Paper    beats  Rock
Scissors beats  Paper
```
Same choice on both sides is a draw. Every other pairing has exactly
one winner.

**Python concepts**
- `random.randint(0, 2)` to generate Player Two's choice
- multi-line strings (`'''...'''`) for the ASCII art of each option
- `int(input())` to capture a numeric choice and use it as a list index
- a list (`game_options`) used to map a number to a name
- **compound conditionals** — `and` to combine two comparisons into a
  single rule (`if a == "rock" and b == "paper":`)
- `elif` chains to check each of the nine possible pairings in turn

---

## The Code (as written)

```python
import random

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
    print("Player Two Wins")
```

The `# RR - RP - RS - PP - PR - PS - SS - SR - SP` comment is the spec:
nine pairings, each one its own `elif`. The draw check up front means
the three "same vs same" cases (RR, PP, SS) are handled in a single
line, leaving six asymmetric pairings to enumerate by hand.

---

## What I Learned

- **`and` combines two conditions into one rule.** Each matchup needs
  *both* players' choices to match a specific pattern, so
  `if a == "rock" and b == "paper":` is the natural compound condition
  — not two separate `if`s, which would each fire independently.
- **Enumerating pairings by hand is error-prone.** Nine outcomes (one
  draw type × three, plus six win/loss combinations) is small enough to
  write out individually, but every pairing has to be entered *and*
  checked against the real rules — there's no structural safety net
  that catches a wrong outcome.
- **A list doubles as a lookup table.** `game_options[player_one_selects]`
  turns a typed number into a name, so the comparison logic can work
  in readable strings ("rock", "paper") instead of bare integers.
- **`random.randint(0, 2)` gives the computer a fair, independent
  choice** — drawn from the same index range the player chooses from,
  so both sides map onto `game_options` the same way.

---

## Improvements I Recognised

Reviewing my own code, these are the changes I'd make — all within
the concepts taught so far:

- **No bounds checking on input.** Typing anything other than `0`, `1`,
  or `2` raises an `IndexError` when it's used to index
  `game_options`. An `else` after the input prompt — "Please enter 0,
  1, or 2." — would catch this instead of crashing.
- **The ASCII art (`rock`, `paper`, `scissors`) is defined but never
  used.** Printing `rock`, `paper`, or `scissors` alongside each
  player's selection — e.g. `print(eval(game_options[player_one_selects]))`,
  or better, a small dictionary mapping name → art — would put the
  artwork to work instead of leaving it dead code.
- **Repeated indexing could be stored once.** `game_options[player_one_selects]`
  and `game_options[player_two_select]` are each evaluated multiple
  times across the `if`/`elif` chain. Assigning them to `player_one_choice`
  and `player_two_choice` up front would shorten every condition and
  remove the repetition.

**On compound conditionals vs nesting:** Day 003's flowchart problem
called for *nested* `if`s, because each choice opened a new decision.
This problem has no such hierarchy — both choices are made up front,
and only the comparison between them decides the outcome. That's why
the structure here is a flat `elif` chain of `and`-conditions rather
than nested blocks: nesting mirrors sequential decisions, compound
conditions mirror simultaneous ones. Choosing between them is still
the same skill from Day 003 — match the code's shape to the problem's
shape.

---

## Run

```bash
python main.py
```
Enter `0` for Rock, `1` for Paper, or `2` for Scissors when prompted.
Note: input must currently be a valid integer in range — entering
text or a number outside `0`–`2` will crash the program until input
validation is added.

---

## What I'm Taking Forward

Comparison logic doesn't reward writing fast — it rewards writing
carefully. Nesting conditionals (Day 003) and combining them with `and`
(today) are two different shapes for two different kinds of problems,
but both fall apart the same way: one quietly wrong line, indistinguishable
from a correct one until it's tested against every case it claims to
cover.

```
─ What are you going to do today that will make a difference? ──
```
