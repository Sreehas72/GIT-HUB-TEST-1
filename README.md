# The Quiz with Rules

Sreehas's first Python game. A quiz to beat, with a twist of rules and lives.

## How to Run

Requires **Python 3** (installed).
```bash
py first_game/quiz_game.py
```

## How to Play

On start, you must type `start` to begin.

- **5 questions** are drawn from 3 difficulty levels:
  - `EASY` - 1 point
  - `MEDIUM` - 3 points
  - `HARD` - 5 points
- You start with **3 lives**. Every wrong answer costs 1 life.
- On **HARD** questions only, you may type `hint` to get a clue, **ONCE per game**.
- Answer by typing the number of the option (1-4).
- Type `quit` at any time to leave.

## Win Condition

Finish with **10 or more points** AND at least **1 life remaining**.

## Rules for Visitors

- You may fork this repo and submit a Pull Request with new questions or fixes.
- Keep question content clean: school-friendly, no personal or hateful content.
- Changes to gameplay (points, rules) must stay backward-compatible with the win condition above.
- Emojis break on the Windows console in Python, please use ASCII-only text in `print()` output.
- Fun and helpful code comments are welcome; no slick shortcuts in scoring.