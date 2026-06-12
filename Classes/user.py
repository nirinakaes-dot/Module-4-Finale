from datetime import date
from Classes.habit import Habit

class User:

    def __init__(self,username,):
        self.username = username
        self.habits = []

    def validate_add_habit(self,title,description,due_date):
       
        ##Check if the variables exists

        if not title:
            raise ValueError('Title is empty')
        if not description:
            raise ValueError('Description is empty')  
        if not due_date:
            raise ValueError('Due date is empty')    

        ## Check if the length fits
        if len(title) < 3:
            raise ValueError('Title must be more than 3 characters')
        if len(description)< 3:
            raise ValueError('Description must be more than 3 characters')


        ## Check if its an instance
        if not isinstance( due_date, date):
            raise ValueError('Date must be a date object') 
        
        ##Ensures that validation passed
        return True
    
    def add_habit(self,title,description,due_date):

        ##Checks if validation passed
        self.validate_add_habit(title,description,due_date)

        ##Checks for duplicate titles
        for habits in self.habits:
            if habits.title == title:
                raise ValueError(f'{title} already exists')
            
        habit = Habit(title, description, due_date)

        #Appends task into the habit empty list

        self.habits.append(habit)
        print('Habit is succesfully added')


    def delete_habit(self,index):
## Check if the index is larger than the length of habit objects
        if index > len(self.habits) or index<1:
            raise ValueError('Enter a valid number')
        self.habits.pop(index-1)
        print('Deleted succesfully')


    def find_habit(self,find):

        ##Checks if the title is found in any of the saved habit titles
        for habits in self.habits:
            if habits.title == find:
                return habits
         ##raises an error t=if the title you typed is not matching any of the titles   
        raise ValueError(f'Sorry!! {find} does not exist')



        
    
        

    

            

