from datetime import date


class Habit:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = False

    def check_pending_habits(self):
        if self.status == False:
            return True
        return False

    def check_completed_habits(self):
        if self.status == True:
            return True
        return False
    
    def mark_complete(self):
        if self.status == True:
          print(f'{self.title} was complete')   
          #changes the state 
        else:
            self.status = True 
            print(f'{self.title} is being marked as complete')
