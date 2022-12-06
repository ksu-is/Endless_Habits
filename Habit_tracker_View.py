from datetime import datetime


def habit_break(habit_name, start_date):

    # personal details
    goal = 60

    # Time passed
    time_passed = (datetime.now() - start_date).total_seconds()

   # hours and days converted
    hours = round(time_passed / 60 / 60, 1)
    days = round(hours / 24, 2)
 
    # goal date countdown
    days_to_go = round(goal - days)

    if hours > 72:
        hours = str(days) + 'days'
    else:
        hours = str(hours) + 'hours'

    return {'habit' : habit_name, 'time since' : hours, 'days remaining' : days_to_go}

print(habit_break('coffee', datetime(2021, 7, 23, 10, 45)))