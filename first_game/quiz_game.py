import random

TITLE = r"""
   ____        _       _____              _
  / __ \      (_)     / ____|            (_)
 | |  | |_   _ _ ____| |  __  __ _ _ __ ___  ___  ___
 | |  | | | | | |_  / | |_ \ / _` | '_ ` _ \ / _ \
 | |__| | |_| | |/ / |__) | (_| | | | | | | |  __/
  \___\_/ \__,_|_|\_\_____/ \__,_|_| |_| |_|\___|
"""

RULES = """
===============================  RULES  ===============================
1. You must answer 5 questions from THREE difficulty levels.
2. Difficulty points: Easy = 1 | Medium = 3 | Hard = 5.
3. Easy: "Easy question" | Medium: "Medium question" | Hard: "Hard question"
4. You start with 3 lives. Every wrong answer costs 1 life.
5. Hard questions only: you get ONE hint per whole game.
6. Answer by typing the NUMBER of your choice (1-4).
7. Type "hint" to use your hint (only works on Hard questions).
8. Type "quit" to leave at any time.
9. Win condition: score >= 10 points AND at least 1 life remaining.
========================================================================
"""

QUESTIONS = {
    "easy": [
        {
            "question": "What does CPU stand for?",
            "options": ["Central Processing Unit", "Computer Personal Unit",
                        "Core Processing Unit", "Central Program Utility"],
            "answer": 1,
        },
        {
            "question": "What is 2^10 (2 to the power of 10)?",
            "options": ["512", "1024", "2048", "1000"],
            "answer": 2,
        },
        {
            "question": "Which of these is a programming language?",
            "options": ["HTML", "CSS", "Python", "HTTP"],
            "answer": 3,
        },
        {
            "question": "What does RAM stand for?",
            "options": ["Random Access Memory", "Read All Memory", "Right Access Module", "Rapid Application Memory"],
            "answer": 1,
        },
    ],
    "medium": [
        {
            "question": "What does 'if __name__ == \"__main__\":' in Python control?",
            "options": ["Loop speed", "Code that runs only when the file is run directly (not imported)",
                        "Memory allocation", "Module imports"],
            "answer": 2,
        },
        {
            "question": "What is the output of: print(type(42))?",
            "options": ["<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'bool'>"],
            "answer": 1,
        },
        {
            "question": "Which built-in function converts text like '42' into a number?",
            "options": ["int()", "str()", "len()", "list()"],
            "answer": 1,
        },
    ],
    "hard": [
        {
            "question": "Where should you store secrets (API keys, passwords) in a Python project?",
            "options": ["Directly in your .py file", "In a .env file", "In code comments",
                        "In the database table"],
            "answer": 2,
            "hint": "Files whose name starts with a dot are usually hidden."
        },
        {
            "question": "What is the time complexity of binary search on a sorted list?",
            "options": ["O(n)", "O(log n)", "O(n log n)", "O(1)"],
            "answer": 2,
            "hint": "With each step you cut the search area roughly in half."
        },
        {
            "question": "Which function keeps only the elements of a list that satisfy a condition?",
            "options": ["sum()", "filter()", "sorted()", "map()"],
            "answer": 2,
            "hint": "It 'filters out' what doesn't pass your test."
        },
    ],
}

DIFFICULTY_ORDER = ["easy", "medium", "hard", "easy", "medium"]
POINTS = {"easy": 1, "medium": 3, "hard": 5}


def choose_question(difficulty, used_ids):
    pool = [q for i, q in enumerate(QUESTIONS[difficulty]) if i not in used_ids[difficulty]]
    q = random.choice(pool)
    used_ids[difficulty].add(QUESTIONS[difficulty].index(q))
    return q


def show_question(q, difficulty):
    print(f"\n[{difficulty.upper()}] {q['question']}")
    for num, option in enumerate(q["options"], start=1):
        print(f"  {num}. {option}")


def get_valid_input(q, difficulty, hint_used):
    while True:
        raw = input("Your answer> ").strip().lower()
        if raw == "quit":
            return "quit"
        if raw == "hint":
            if difficulty == "hard" and not hint_used:
                return "hint"
            print("You can only use a hint on Hard questions, ONCE per game.")
            continue
        try:
            choice = int(raw)
            if 1 <= choice <= 4:
                return choice
        except ValueError:
            pass
        print("Please enter a number (1-4), 'hint', or 'quit'.")


def play():
    score = 0
    lives = 3
    hint_used = False
    quit_game = False
    used = {"easy": set(), "medium": set(), "hard": set()}

    print(TITLE)
    print(RULES)

    start = input("Type 'start' to begin or 'quit' to leave> ").strip().lower()
    if start == "quit":
        print("See you next time!")
        return

    for round_num, difficulty in enumerate(DIFFICULTY_ORDER, start=1):
        if quit_game or lives <= 0:
            break

        question = choose_question(difficulty, used)
        print(f"\n--- QUESTION {round_num}/5 ---")
        show_question(question, difficulty)

        answer = get_valid_input(question, difficulty, hint_used)

        if answer == "quit":
            quit_game = True
            break
        if answer == "hint":
            print(f"[HINT]: {question['hint']}")
            hint_used = True
            answer = get_valid_input(question, difficulty, hint_used)
            if answer == "quit":
                quit_game = True
                break

        if answer == question["answer"]:
            score += POINTS[difficulty]
            print(f"[OK] Correct! +{POINTS[difficulty]} point(s) -> total {score}")
        else:
            lives -= 1
            print(f"[X] Incorrect! The answer was {question['answer']}. Lives left: {lives}")

    print("\n===================== RESULT =====================")
    if quit_game:
        print("You quit early. Final score:", score)
        return
    print(f"Score: {score} | Lives: {lives}")
    if score >= 10 and lives >= 1:
        print("[WIN] CONGRATULATIONS! You WIN")
    elif score >= 10 and lives == 0:
        print("Great points, but you lost all your lives!")
    else:
        print("Keep practicing — the quiz awaits!")
    print("Thanks for playing, Sreehas!")


if __name__ == "__main__":
play()
#hello
