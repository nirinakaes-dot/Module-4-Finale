import json
import os
from Classes.habit import Habit
Habit_file = "habits.json"

def save_habits(habits):
    with open(Habit_file, 'w') as file:
        json.dump([h.to_dict() for h in habits], file)  

def load_habits():
 if not os.path.exists(Habit_file):
  return []
 try:
     with open(Habit_file, 'r') as file:
            data = json.load(file)
            return [Habit.from_dict(h) for h in data]  
 except json.JSONDecodeError:
      return []
   
 
