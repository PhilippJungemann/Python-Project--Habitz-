from db import get_habit_data
from datetime import date, datetime
#

# reminder
def reminder(db, name):
    all_data = get_habit_data(db, name)
    last = all_data.pop()
    new = list(last)
    if new[4] is None:
        print("Your habit " + name + " is waiting for the first check off!")
        return
    last_check_off = datetime.strptime(new[4], '%Y-%m-%d').date()
    today = date.today()
    diff = today - last_check_off
    diff = int(diff.days)
    if new[2] == "daily":
        if diff > 0:
            print("Your habit '" + name + "' has to be done today!")
        else:
            print("Great - your habit '" + name + "' doesn't need to be done until tomorrow!")
            return
    if new[2] == "weekly":
        last_check_off = datetime.strptime(new[4], '%Y-%m-%d').date()
        last_check_off = datetime.strftime(last_check_off, '%W')
        current_week = date.today().strftime("%W")
        diff = int(current_week) - int(str(last_check_off))
        if abs(diff) > 0:
            print("Your habit '" + name + "' has to be done this week!")
        else:
            print("Great - your habit '" + name + "' doesn't need to be done until next week!")
            return
    if new[2] == "monthly":
        last_check_off = datetime.strptime(new[4], '%Y-%m-%d').date()
        last_check_off = datetime.strftime(last_check_off, '%m')
        current_month = date.today().strftime("%m")
        diff = int(current_month) - int(str(last_check_off))
        if abs(diff) > 0:
            print("Your habit '" + name + "' has to be done this month!")
        else:
            print("Great - your habit '" + name + "' doesn't need to be done until next month!")
            return
    if new[2] == "yearly":
        last_check_off = datetime.strptime(new[4], '%Y-%m-%d').date()
        last_check_off = datetime.strftime(last_check_off, '%Y')
        current_year = date.today().strftime("%Y")
        diff = int(current_year) - int(str(last_check_off))
        if diff > 0:
            print("Your habit '" + name + "' has to be done this year!")
        else:
            print("Great - your habit '" + name + "' doesn't need to be done until next year!")
            return
