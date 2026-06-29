# Day 003 — Treasure Island

```
 /\   architectray · 
/__\  100 Days of Python · 2026-06-29
```

**Concepts:** control flow, `if` / `elif`, nested conditionals, branching logic
**The lesson:** mapping a flowchart faithfully into nested conditional logic — and knowing when `elif` beats multiple `if`s.

---

## The Project

A text-based "Treasure Island" adventure. The player makes a
series of choices — a direction, an action, then a door — and
each path leads either to a game-over or, by the one correct
route (Left → Wait → Yellow), to victory. The program is a direct
translation of the course flowchart into branching conditional
logic.

**The winning path**
```
Left  →  Wait  →  Yellow   →  "You Win!"
```
Every other combination ends the game.

**Python concepts**
- `input()` to capture each choice
- `if` / `elif` for branching on the choice
- **nested** conditionals — each correct choice opens the next
  decision, mirroring the flowchart's depth
- single-path logic: only one route through the tree wins

---

## The Code (as written)

```python
# User Options - Left, Right
first_option = str(input("First Option. Pick one: Left, or Right..."))
if first_option == "Right":
    print("Fall into a hole.\nGame Over")
elif first_option == "Left":
    second_option = str(input("Second Option. Pick one: Swim, or Wait..."))
    if second_option == "Swim":
        print("Attacked by trout.\nGame Over.")
    elif second_option == "Wait":
        third_option = str(input("Third Option. Pick a Door: Red, Blue, or Yellow..."))
        if third_option == "Blue":
            print("Eaten by beasts.\nGame Over.")
        elif third_option == "Red":
            print("Burned by Fire.\nGame Over.")
        elif third_option == "Yellow":
            print("You Win!")
```

The nesting is the point: each `elif` that continues the story
opens a fresh decision inside it, so the structure of the code
mirrors the structure of the flowchart — depth for depth.

---

## What I Learned

- **Nested conditionals map a flowchart directly.** Each branch
  that continues the adventure contains the next decision. The
  code's shape follows the flowchart's shape — which makes it
  readable and easy to verify against the spec.
- **`elif` is right when only one option can be true.** Only one
  door can be chosen, so `if` / `elif` is correct here. Separate
  `if` statements would also "work" but would wrongly imply the
  conditions are independent. Structure should reflect intent:
  mutually exclusive choices → `elif`.
- **`input()` already returns a string.** Wrapping it in `str()`
  is redundant — `input()` is always a string, so `str(input())`
  does no work. Cleaner: `first_option = input(...)`.
- **The happy path is one route through a tree.** Mapping a
  branching narrative made the single winning path (Left → Wait
  → Yellow) concrete — every other branch is a dead end by design.

---

## Improvements I Recognised

Reviewing my own code, these are the changes I'd make — all
within the concepts taught so far:

- **Remove the redundant `str()`.** `input()` returns a string
  already; `str(input(...))` → `input(...)`.
- **Handle invalid input with `else`.** As written, an
  unexpected entry (e.g. "Banana") ends the program silently with
  no feedback. An `else` on each branch — "That door doesn't
  exist." — tells the player they entered something unexpected
  and makes the program feel complete.
- **More descriptive variable names.** `first_option` /
  `second_option` / `third_option` → `direction` / `action` /
  `door`. The code then almost reads like English:
  `if direction == "Left":`.
- **Readability of output.** `print("Fall into a hole.\nGame
  Over")` could be two `print()` lines — either is fine; the
  split reads slightly cleaner.

**On `else`:** not every `if` needs one — `else` is only required
when something should happen if all conditions fail. Here it isn't
strictly necessary, but it *improves the experience* by catching
invalid input. A deliberate choice, not a rule.

**On multiple `if`s vs `elif`:** the lecture covered multiple
`if`s. They'd run here, but they're the wrong tool — only one
door can be chosen, so the conditions are mutually exclusive, and
`elif` expresses that correctly. Multiple `if`s suit cases where
several conditions might all be true at once. Choosing the right
structure is itself part of the logic.

---

## Run

```bash
python main.py
```
Enter the options exactly (e.g. `Left`, `Wait`, `Yellow`).
Note: input is currently case-sensitive — `left` won't match
`Left` until string methods like `.lower()` are introduced.

---

## What I'm Taking Forward

Control flow is where logic becomes structure. The real skill
wasn't writing the `if`s — it was choosing the *right* structure
for the intent: nesting to mirror the flowchart, `elif` for
mutually exclusive choices, and recognising where an `else` adds
robustness without being mandatory. Making the code's shape match
the problem's shape is the lesson.

```
─ Faith is confidence in what we hope for, and assurance about what we do not see. ──
```
