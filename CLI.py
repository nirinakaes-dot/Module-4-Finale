from storage import save_habits , load_habits
from streak import streak_days, streak_week
from  Classes.entry import Entry
from Classes.habit import Habit
from Classes.user import User
import click
from rich.table import Table
from rich.console import Console


@click.group()
def cli ():
    pass

##Delete Habit command
@cli.command()
@click.argument('title')
def delete(title):
    user = User("username")
    user.delete_habit(title)

##Add Habit command

@cli.command()
@click.argument('title')
@click.argument('description')
@click.argument('due_date')


def add(title,description,due_date):
    user = User("username")
    user.add_habit(title,description,due_date)

## Find Habit command
@cli.command()
@click.argument('title')
def find(title):
    user = User("username")
    user.find_habit(title)

##Find day streak command
@cli.command()
@click.argument('title')
def daystreak(title):
    user = User('username')
    habit = user.find_habit(title)
    streak_days(habit)

##Find week streak command
@cli.command()
@click.argument('title')
def weekstreak(title):
    user = User("username")
    habit = user.find_habit(title)
    streak_week(habit)

    
if __name__ == "__main__":
    cli()



    





   

