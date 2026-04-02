Lab 2 - Knowledge Representation and Propositional Logic


Overview

This lab explores propositional logic and model checking using a custom logic.py library. Each exercise builds a knowledge base using logical symbols and connectives, then uses model_check() to derive conclusions automatically.


Files

logic.py       Core library providing Symbol, And, Or, Not, Implication, and model_check()
harry.py       Harry Potter scenario using implication and disjunction
clue.py        Clue-style murder mystery with suspects, rooms, and weapons
mastermind.py  Mastermind colour-guessing puzzle encoded as logic constraints
puzzle.py      Harry Potter house assignment puzzle (Gilderoy, Pomona, Minerva, Horace)


Dependencies

pip install termcolor

logic.py must be present in the same directory as all other files.


How to Run

python harry.py
python clue.py
python mastermind.py
python puzzle.py


Exercises

Exercise 1 - harry.py (Base)
Models a scenario where Harry met exactly one of Hagrid or Dumbledore, and it is known that Dumbledore was met. Uses Implication, Or, Not, and And to derive whether it was raining.

Exercise 2 - harry.py (Extended with Snape)
Adds a fourth character, Snape, with three new rules:
- Harry met exactly one of Hagrid, Dumbledore, or Snape
- If it is raining, Snape did not come outside
- Snape was seen outdoors today (direct fact)

Conclusions proved:
- snape is True
- rain is False because Snape is outside so it cannot be raining
- hagrid and dumbledore are False because Snape was met exclusively

Exercise 3 - clue.py (New Scenario)
Replaces the original Clue characters with a new set.

Suspects: AliceSuspect, BobSuspect, CarolSuspect
Rooms: office, garage, basement
Weapons: poison, rope, candlestick

Clues encoded:
1. Cards in hand: Not(alice), Not(office), Not(poison)
2. Opponent showed: Or(Not(bob), Not(garage), Not(rope))
3. Separately learned: Not(candlestick), Not(basement)

Output: CarolSuspect is YES, the only suspect not eliminated by the clues.

Exercise 4 - mastermind.py (Third Clue Added)
Adds a third guess [blue0, green1, red2, yellow3] with 0 correct positions, eliminating blue0, green1, red2, and yellow3 from consideration.

Finding: The puzzle is not fully solved by three clues alone. Multiple valid arrangements remain consistent with all constraints, so model_check() cannot prove a unique solution for every position.

Exercise 5 - Scalability Analysis

puzzle.py uses 16 symbols (4 people x 4 houses), producing 65,536 truth-table rows.
mastermind.py uses 16 symbols (4 colors x 4 positions), also producing 65,536 rows.
A 6 color x 6 position version of mastermind.py would use 36 symbols, producing approximately 68.7 billion rows.

Algorithmic alternative: SAT solvers such as those using the DPLL algorithm use unit propagation and backtracking with pruning to avoid enumerating all 2^n models. This reduces practical complexity from exponential to tractable for large problems.
