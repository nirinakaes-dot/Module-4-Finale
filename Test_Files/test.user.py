import pytest
from datetime import date
import sys
sys.path.insert(0, '.')

from Classes.habit import Habit
from Classes.user import User


# ── User tests ──

def test_add_habit():
    user = User("testuser")
    user.add_habit("Exercise", "Run every day", date(2026, 12, 31))
    assert len(user.habits) == 1
    assert user.habits[0].title == "Exercise"

def test_delete_habit():
    user = User("testuser")
    user.add_habit("Exercise", "Run every day", date(2026, 12, 31))
    user.delete_habit(1)
    assert len(user.habits) == 0

def test_find_habit():
    user = User("testuser")
    user.add_habit("Exercise", "Run every day", date(2026, 12, 31))
    habit = user.find_habit("Exercise")
    assert habit.title == "Exercise"
