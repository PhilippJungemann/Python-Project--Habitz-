from db import get_habit_data
from datetime import date, datetime


def reminder(db, name):
    """reminder function, to remind the user about his current to-dos
    :param db: connection to the database
    :param name: the name of the habit
     """
    all_data = get_habit_data(db, name)
    # getting the last element of the data and convert it to a list
    last = all_data.pop()
    new = list(last)
    # if the habit was not checked off at all, reminding the user of it
    if new[4] is None:
        print("Your habit " + name + " is waiting for the first check off!")
        return
    last_check_off = datetime.strptime(new[4], '%Y-%m-%d').date()
    today = date.today()
    diff = today - last_check_off
    diff = int(diff.days)
    # if the habit is a daily one and was not checked off today, it has to be done
    if new[2] == "daily":
        if diff > 0:
            print("Your habit '" + name + "' has to be done today!")
            # the returning of "Your habit '" + name + "' has to be done today!"
            # is only done for the module 'test_project'
            return "Your habit '" + name + "' has to be done today!"
        # if it already was checked off, there is no action required
        else:
            print("Great - your habit '" + name + "' doesn't need to be done until tomorrow!")
            return
    # if the habit is a weekly one and was not checked off this week, it has to be done
    if new[2] == "weekly":
        last_check_off = datetime.strptime(new[4], '%Y-%m-%d').date()
        last_check_off = datetime.strftime(last_check_off, '%W')
        current_week = date.today().strftime("%W")
        diff = int(current_week) - int(str(last_check_off))
        # the absolute value must be taken so that no errors can occur at year changes
        if abs(diff) > 0:
            print("Your habit '" + name + "' has to be done this week!")
        # if it already was checked off, there is no action required
        else:
            print("Great - your habit '" + name + "' doesn't need to be done until next week!")
            return
    # if the habit is a monthly one and was not checked off this month, it has to be done
    if new[2] == "monthly":
        last_check_off = datetime.strptime(new[4], '%Y-%m-%d').date()
        last_check_off = datetime.strftime(last_check_off, '%m')
        current_month = date.today().strftime("%m")
        diff = int(current_month) - int(str(last_check_off))
        # the absolute value must be taken so that no errors can occur at year changes
        if abs(diff) > 0:
            print("Your habit '" + name + "' has to be done this month!")
        # if it already was checked off, there is no action required
        else:
            print("Great - your habit '" + name + "' doesn't need to be done until next month!")
            return
    # if the habit is a yearly one and was not checked off this year, it has to be done
    if new[2] == "yearly":
        last_check_off = datetime.strptime(new[4], '%Y-%m-%d').date()
        last_check_off = datetime.strftime(last_check_off, '%Y')
        current_year = date.today().strftime("%Y")
        diff = int(current_year) - int(str(last_check_off))
        if diff > 0:
            print("Your habit '" + name + "' has to be done this year!")
        # if it already was checked off, there is no action required
        else:
            print("Great - your habit '" + name + "' doesn't need to be done until next year!")
            return
