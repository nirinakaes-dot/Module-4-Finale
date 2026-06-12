from datetime import date


class Habit:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = False
        self.entries = []

    def to_dict(self):
      return {
        "title": self.title,
        "description": self.description,
        "due_date": str(self.due_date),
        "status": self.status
    }
    @classmethod
    def from_dict(cls, data):
     habit = cls(data['title'], data['description'], data['due_date'])
     habit.status = data.get('status', False)
     habit.entries = data.get('entries', [])
     return habit

    def check_pending_habits(self):
        if self.status == False:
            return True
        return False

    def check_completed_habits(self):
        if self.status == True:
            return True
        return False
    
    #Changes the status from False to True
    def mark_complete(self):
        if self.status == True:
          print(f'{self.title} was complete')   
          #changes the state 
        else:
            self.status = True 
            print(f'{self.title} is being marked as complete')
