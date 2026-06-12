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

## Tech Stack
- `click` — CLI commands
- `rich` — terminal output formatting
- `pytest` — some unit testing