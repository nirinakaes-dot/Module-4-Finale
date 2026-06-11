import json
import os
Habit_file = "habits.json"

def save_habits(habits):
 with open (Habit_file,'w')as file:
  json.dump(habits,file)

def load_habits():
 if not os.path.exists(Habit_file):
  return []
 try:
  with open(Habit_file, 'r')  as file:
   return json.load(file)
 except json.JSONDecodeError:
  return [] 
   
 
