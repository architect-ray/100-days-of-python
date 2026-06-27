# Day 001 — Band Name Generator

```
 /\   architectray
/__\  100 Days of Python · 2026-06-27
```

**Concepts:** printing, input, variables, string manipulation
**The real lesson:** setting up Git, SSH, and a clean dual-identity workflow from the ground up.

---

## The Project

A simple program that asks the user for the city they grew up
in and the name of a pet, then suggests a band name from the
two. The Python itself is straightforward — the foundations laid
*around* it were the substance of Day 1.

**What the code does**
- Prints a welcome message (`print`)
- Captures two inputs from the user (`input`)
- Stores them in variables
- Combines them with an f-string and returns the band name

**Python concepts**
- `print()` for output
- `input()` for capturing user input
- Variables for storing values
- String concatenation / f-strings for combining text

---

## The Real Day 1 — Foundations

The Band Name Generator took minutes. Building the *system* it
lives in took the day — and that work is as much a part of "100
Days of Python" as the code, because the goal isn't just to
write Python, it's to ship it professionally. Day 1 was where
the whole publishing pipeline got built.

### Git identity — local vs global

- Git carries two separate concepts: **identity** (the
  name/email stamped into each commit) and **authentication**
  (the credential that proves you can push). They are
  independent.
- Identity is set at **global** (`~/.gitconfig`, all repos) or
  **local** (`.git/config`, one repo) level. The `--global`
  flag is the *only* difference. **No flag means local** — Git
  defaults to the narrowest scope, not the broadest.
- Running two identities cleanly means **clearing the global
  identity entirely** and setting identity **locally per repo**.
  With no global fallback, Git forces a conscious identity
  choice in every repo — a safety net against committing as the
  wrong person.

### The first real mistake — and the fix

- Committed the README **before** setting a local identity.
  With global cleared and no local set, Git **auto-generated**
  an identity from the system username and hostname and stamped
  it on the commit (with a warning).
- Fixed with:
  `git config user.email "<correct>"` then
  `git commit --amend --reset-author --no-edit` to re-stamp the
  commit with the correct author.
- **Lesson:** my Git guesses an identity rather than refusing,
  so "set local identity before the first commit" is not
  optional — it's the habit that prevents contamination. Caught
  it on commit one. Best possible time.

### Authentication vs Authorisation

- **Authentication** = proving *who* you are (the SSH key / PAT).
- **Authorisation** = what you're *allowed to do* once
  authenticated (write access to a specific repo).
- A credential can authenticate successfully yet fail
  authorisation — e.g. a valid token for the wrong account being
  refused write access to this repo.

### Clone vs init

- `git init` turns existing **local** code into a repo, then
  needs the remote wired up manually.
- `git clone` pulls down a repo that **already exists** —
  creating `.git`, setting the `origin` remote, and configuring
  branch tracking **in one step**.
- Since the GitHub repo was created first, **clone** was the
  correct, cleaner path — no manual remote setup, no README
  collision.

### SSH — keys, location, and why

- Generated an SSH key pair: `ssh-keygen -t ed25519 -C "<label>"`.
- A key pair is two files in `~/.ssh/`:
  - **Private** (`id_ed25519`) — stays on the machine, secret,
    never shared or committed. Proves identity.
  - **Public** (`id_ed25519.pub`) — given to GitHub. Safe to
    share.
- Keys live in `~/.ssh/` because it's the standard location SSH
  checks automatically, protected by user permissions — and
  **outside any repo**, so a private key can never be
  accidentally committed.
- `ssh-keygen` ignores the current directory; the key always
  saves to `~/.ssh/` regardless of where it's run.
- The `-C` flag is just a **label**, not functional. Used a
  non-identifying tag rather than a real email, to keep the
  separated identity clean.
- A passphrase encrypts the private key — a stolen key file is
  useless without it.

### Verifying the SSH connection

- `ssh -T git@github.com` →
  `Hi architect-ray! You've successfully authenticated, but
  GitHub does not provide shell access.`
- **"Permanently added to known hosts"** — normal first-connection
  behaviour; SSH records GitHub's identity to verify future
  connections. A security feature, not a warning.
- **"Does not provide shell access"** — expected; GitHub's SSH is
  for Git operations only, never terminal access.
- The greeting naming **architect-ray** is the confirmation the
  *right* identity authenticated — a quick check to run before
  any push.
- The key **fingerprint** and **randomart** don't need saving —
  the fingerprint is derivable from the key any time
  (`ssh-keygen -lf`), and randomart is a rarely-used visual aid.
  What matters is protecting the **private key** and remembering
  the **passphrase**.

### Pushing — explicit vs shorthand

- `git push origin main` is the explicit form (names remote and
  branch); `git push` is the shorthand that works once **upstream
  tracking** is set.
- **Cloning sets tracking automatically**, so plain `git push`
  works immediately — no `-u` needed.

### Privacy — the commit email

- A commit's email is **public** in history. Using GitHub's
  **noreply address**
  (`ID+username@users.noreply.github.com`, found in
  Settings → Emails) attributes commits to the account and fills
  the contribution graph **without** exposing a real address.

---

## Commit Convention

```
feat(day-001): add band name generator
```
Conventional Commits, imperative mood, ~50 chars — a clean,
scannable public history that is itself part of the portfolio.

---

## Run

```bash
python main.py
```

---

## What I'm Taking Forward

The code is the easy part. Day 1's real work was building a
clean, repeatable, identity-conscious workflow — local identity
per repo, SSH keys per machine, clone over init, the noreply
address, a consistent commit convention, and a place for
everything. The foundation is laid; the next 99 days build on it.

```
── On any given day, you can massively change the direction of your life ──
```
