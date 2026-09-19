# 🐍 Python Mini Projects

**A collection of beginner-friendly Python mini projects, built while learning Python programming fundamentals.**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Learning-brightgreen)
![License](https://img.shields.io/badge/License-Open--Source-lightgrey)

Each script in this repo is a small, self-contained project that explores a different core Python concept — loops, conditionals, functions, dictionaries, string parsing, and more. Clone it, run any file, and tinker with the code to make it your own.

---

## 📂 Projects Included

| # | Project | File | Concepts Used |
|---|---------|------|----------------|
| 1 | 🧮 Calculator | [`calculator.py`](./calculator.py) | Loops, conditionals, f-strings |
| 2 | 🏧 ATM Simulator | [`atm.py`](./atm.py) | `match`/`case`, state management |
| 3 | 🎯 Number Guessing Game | [`number_guess.py`](./number_guess.py) | Randomization, user input, comparisons |
| 4 | 🐍🪜 Snake and Ladders | [`snake&ladders.py`](./snake&ladders.py) | Game loops, position tracking |
| 5 | 💰 Expense Tracker | [`expence_tracker.py`](./expence_tracker.py) | Lists, dictionaries, menus |
| 6 | 🔤 Word Guessing Game | [`guess_game.py`](./guess_game.py) | `random.choice()`, string checks |
| 7 | 📅 Habit Tracker (NLP-style parser) | [`habit_tracker.py`](./habit_tracker.py) | Regex, `datetime`, type hints |
| 8 | 🔢 Number Sorter & Counter | [`number_sorter.py`](./number_sorter.py) | Sorting, dictionaries, formatted tables |
| 9 | 🔐 Password Generator | [`password_generator.py`](./password_generator.py) | `random`, `string` module |
| 10 | ❓ Quiz Game | [`quiz_game.py`](./quiz_game.py) | Dictionaries, functions, scoring logic |
| 11 | ✅ To-Do List Parser (NLP-style) | [`to_do.py`](./to_do.py) | Regex, intent detection, date parsing |

---

## 🔍 Project Details

### 1. 🧮 Calculator — `calculator.py`
A simple command-line calculator that performs the four basic arithmetic operations: addition, subtraction, multiplication, and division. Runs in a loop so you can do multiple calculations until you type `exit`.

```bash
python calculator.py
```

### 2. 🏧 ATM Simulator — `atm.py`
A menu-driven ATM simulation using Python's `match`/`case` statement (Python 3.10+). Lets you check your balance, deposit money, and withdraw money, with basic validation to stop you from overdrawing.

```bash
python atm.py
```

### 3. 🎯 Number Guessing Game — `number_guess.py`
A two-player guessing game — Player 1 secretly picks a target number, and Player 2 tries to guess it, getting "too high" / "too low" hints along the way.

```bash
python number_guess.py
```

### 4. 🐍🪜 Snake and Ladders — `snake&ladders.py`
A console-based two-player version of the classic board game. Players take turns "rolling" a dice (entering a number 1–6), climb ladders, slide down snakes, and race to reach square 100 first.

```bash
python "snake&ladders.py"
```

### 5. 💰 Expense Tracker — `expence_tracker.py`
A terminal-based expense tracker. Log an expense with its date, category, description, and amount; view every expense you've logged; and get a running total of how much you've spent — all stored in a list of dictionaries for the session.

```bash
python expence_tracker.py
```

### 6. 🔤 Word Guessing Game — `guess_game.py`
A hangman-style word guessing game. A random word is picked from a built-in list, and you guess it one letter at a time within 12 turns.

```bash
python guess_game.py
```

### 7. 📅 Habit Tracker — `habit_tracker.py`
A more advanced mini-project that parses natural-language sentences like *"did 30 min yoga today"* into structured data (habit name, status, duration in minutes, and date) using regular expressions and simple rule-based NLP.

```python
extract_habit_log("did 30 min yoga today")
# -> {'habit': 'yoga', 'status': 'done', 'duration_minutes': 30, 'date': '2026-09-19'}
```

```bash
python habit_tracker.py
```

### 8. 🔢 Number Sorter & Counter — `number_sorter.py`
Takes a series of numbers from the user, then sorts them from least to greatest and prints a frequency table showing how many times each unique number was entered.

```bash
python number_sorter.py
```

### 9. 🔐 Password Generator — `password_generator.py`
Generates a random, secure password of a user-specified length using a mix of letters, digits, and punctuation from Python's `string` module.

```bash
python password_generator.py
```

### 10. ❓ Quiz Game — `quiz_game.py`
A multiple-choice quiz on general programming knowledge. Tracks your score across all questions and gives you a performance message at the end (Perfect / Well done / Keep practicing).

```bash
python quiz_game.py
```

### 11. ✅ To-Do List Parser — `to_do.py`
Another rule-based NLP mini-project — it reads a natural sentence like *"remind me to buy milk tomorrow, it's urgent"* and extracts the intent (add/done/delete), priority, due date, and task title.

```bash
python to_do.py
```

---

## 🛠️ Python Concepts Practiced

- Python 3 fundamentals
- Functions & modular code
- Loops (`while`, `for`)
- Conditional statements (`if`/`elif`/`else`, `match`/`case`)
- Lists & dictionaries
- The `random` module
- The `re` (regex) module for lightweight NLP parsing
- The `datetime` module for date handling
- Basic input validation and error handling

---

## ▶️ How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/AnubhavSinghZ/mini_projects.git
   ```

2. **Move into the project folder**
   ```bash
   cd mini_projects
   ```

3. **Run any project** (requires Python 3 installed)
   ```bash
   python calculator.py
   ```

---

## 🎯 Purpose

This repository was created to practice Python fundamentals and improve problem-solving skills through hands-on, beginner-friendly mini projects — ranging from simple calculators and games to lightweight rule-based NLP parsers.

---

## 👤 Author

**Anubhav Singh**

Learning Python and building projects to strengthen programming skills.
Currently exploring AI & ML. 🚀

---

⭐ If you find this repo helpful or interesting, consider giving it a star!
