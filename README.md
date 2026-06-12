# Streakly 
A command-line habit tracker built with Python. Track your daily habits, monitor streaks, and view weekly progress — all from the terminal.

## Project Structure
```
Final_Project/
├── Classes/
│   ├── user.py       # User class - manages habits
│   ├── habit.py      # Habit class - tracks completion
│   └── entry.py      # Entry class - stores daily logs
├── cli.py            # CLI commands via Click
├── storage.py        # JSON save/load
├── streak.py         # Streak and weekly progress logic
└── data/habits.json  # Auto-generated data file
```
## Run Commands
_ `Add habit` -python3 CLI.py add "Jogging" "Jog around talanta stadium" 2026-12-16 <br>
_`Find habit` - python3 CLI.py find "Jogging"<br>
_`Day streak`python3 CLI.py daystreak "Exercise"<br>
_`Week streak`python3 CLI.py weekstreak "Exercise"<br>
_`delete habit`python3 CLI.py delete 1
## Tech Stack
- `click` — CLI commands
- `rich` — terminal output formatting
- `pytest` — some unit testing
