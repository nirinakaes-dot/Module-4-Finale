from storage import save_habits, load_habits
from streak import streak_days, streak_week
from Classes.entry import Entry
from Classes.habit import Habit
from Classes.user import User
import click
from rich.table import Table
from rich.console import Console
from datetime import datetime

console = Console()

@click.group()
def cli():
    pass

##Delete Habit command
@cli.command()
@click.argument('title')
def delete(title):
    """Delete habit by index."""
    habits = load_habits()
    user = User("username")
    user.habits = habits
    user.delete_habit(int(title))
    save_habits(user.habits)
    console.print(f'[red]{title} deleted successfully![/red]')

##Add Habit command
@cli.command()
@click.argument('title')
@click.argument('description')
@click.argument('due_date')
def add(title, description, due_date):
    """Add a new habit. DATE format: YYYY-MM-DD"""
    habits = load_habits()
    user = User("username")
    user.habits = habits
    due_date = datetime.strptime(due_date, "%Y-%m-%d").date()

    user.add_habit(title, description, due_date)
    save_habits(user.habits)
    console.print(f'[green]{title} added successfully![/green]')

## Find Habit command
@cli.command()

@click.argument('title')
def find(title):
    """Find a habit using  title."""
    habits = load_habits()
    user = User("username")
    user.habits = habits
    habit = user.find_habit(title)
    console.print(f'[blue]Found: {habit.title} - {habit.description}[/blue]')

##Find day streak command
@cli.command()
@click.argument('title')
def daystreak(title):
    """Show the current day streak for a habit."""
    habits = load_habits()
    user = User("username")
    user.habits = habits
    habit = user.find_habit(title)
    streak = streak_days(habit)
    console.print(f'[yellow]{title} streak: {streak} days![/yellow]')

##Find week streak command
@cli.command()
@click.argument('title')
def weekstreak(title):
    """Show the current week streak for a habit."""
    habits = load_habits()
    user = User("username")
    user.habits = habits
    habit = user.find_habit(title)
    weekly = streak_week(habit)
    table = Table(title=f"{title} - Weekly Progress")
    table.add_column("Day")
    table.add_column("Status")
    for i, completed in enumerate(weekly):
        day = f"Day {7 - i}"
        status = "[green]✅ Done[/green]" if completed else "[red]❌ Missed[/red]"
        table.add_row(day, status)
    console.print(table)

@cli.command()
@click.argument('title')
def complete(title):
    """Mark a habit as complete for today."""
    habits = load_habits()
    user = User("username")
    user.habits = habits
    habit = user.find_habit(title)
    habit.mark_complete()
    save_habits(user.habits)
    console.print(f'[green]{title} marked as complete! ✅[/green]')

if __name__ == "__main__":
    cli()