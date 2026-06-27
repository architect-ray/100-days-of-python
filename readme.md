# blueprint-100

Building from the ground up — 100 days of Python, one commit at
a time. The daily build log of Architect Ray.

**Progress:** Day 0 — starting the build
**Language:** Python
**Approach:** One project a day. One commit a day. No skipped foundations.

---

## About

Every structure starts with a blueprint and a foundation. This
repository is both — a 100-day commitment to writing Python
daily, beginning at Day 0 and building up one project at a time.

The aim isn't brilliance on any single day. It's consistency
across all of them. Each day is a small, self-contained build;
together they form a foundation. The commit history is the real
deliverable — proof of showing up, every day.

Every line here is my own work, written as I follow the course,
then transferred clean into this repository (see *How This Repo
Is Built* below).

---

## Progress Log

| Day | Project | Concepts |
|-----|---------|----------|
| 000 | Setup & first commit | environment, git, the plan |
| 001 | — | — |
| 002 | — | — |
| ... | ... | ... |

*Updated as the build rises.*

---

## Structure

```
blueprint-100/
├── README.md            ← this file
├── .gitignore
├── LICENSE
├── day-000/
│   ├── README.md        ← what was built + learned
│   └── main.py          ← my own code
├── day-001/
│   ├── README.md
│   └── main.py
└── day-0NN/
    ├── README.md
    └── main.py
```

Day folders are zero-padded (`day-000`, `day-001`, …) so they
sort correctly. Each folder holds my own code and a short note
on what I built and what I learned — nothing from the course's
own files.

---

## How This Repo Is Built

I follow the course in its own environment, then transfer my
own code into this repository deliberately — keeping the two
cleanly separate.

```
WORKSHOP  →  GALLERY

  Course project          This repository
  (where I learn)         (where I ship)
  ──────────────          ───────────────
  Work through the   →    Copy my own code into
  lesson, experiment,     a clean day-0NN/ folder,
  pass the checks.        write my own README,
                          commit, push.
```

**The principle:** the course project is my workshop — I learn
there. This repo is the gallery — I place only the finished,
clean piece here. Only my own code is transferred; course
scaffolding, instructions, and provided solutions stay in the
course project where they belong. That keeps this repository
original, uncluttered, and a genuine record of my own work.

---

## The Build Plan

```
Days 0–14    Foundations — Python fundamentals
Days 15–28   Framing — OOP, files, APIs
Days 29–45   Fit-out — GUIs, libraries
Days 46–59   Systems — scraping, automation
Days 60–80   Structure — web dev, databases
Days 81–100  Finishing — data science & capstones
```

*(Indicative — adjusted to the course as the build progresses.)*

---

## How to Run

Each day is self-contained:

```bash
cd day-0NN
python main.py
```

Later builds may carry their own dependencies — see each day's
README where applicable.

---

## The Principle

Consistency over intensity. Build it, document it, ship it.
A foundation is laid one day at a time — and the discipline of
laying it is the skill being built here, as much as the code.

— *Architect Ray*
