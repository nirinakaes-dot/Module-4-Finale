from datetime import timedelta, date
def streak_days(habit):
    streak = 0
    check = date.today()
    while check in[entry.date for entry in habit.entries]:
        check = check - timedelta(days=1)
        streak += 1
    return streak   

def streak_week(habit):
    weekly = []
    for i in range(7):
       check = date.today()-timedelta(days=i) 
       weekly.append(check in [entry.date for entry in habit.entries])
    return weekly    