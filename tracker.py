from db import get_habit_data
from datetime import date, datetime


def track_all_habitz(db, name):
    """track_all_habitz function, to track the current habits and, if necessary,
    set the streak to zero if the habit has not been done in time
    :param db: connection to the database
    :param name: the name of the habit
     """
    all_data = get_habit_data(db, name)
    last = all_data.pop()
    new = list(last)
    if new[4] is None:
        return
    last_check_off = datetime.strptime(new[4], '%Y-%m-%d').date()
    today = date.today()
    diff = today - last_check_off
    diff = int(diff.days)
    if new[2] == "daily":
        reset_streak(db, diff, new, name)
        # the returning of new is only done for the test_project_module
        return new

    if new[2] == "weekly":
        last_check_off = datetime.strptime(new[4], '%Y-%m-%d').date()
        last_check_off = datetime.strftime(last_check_off, '%W')
        current_week = date.today().strftime("%W")
        diff = int(current_week) - int(str(last_check_off))
        reset_streak(db, diff, new, name)

    if new[2] == "monthly":
        last_check_off = datetime.strptime(new[4], '%Y-%m-%d').date()
        last_check_off = datetime.strftime(last_check_off, '%m')
        current_month = date.today().strftime("%m")
        diff = int(current_month) - int(str(last_check_off))
        reset_streak(db, diff, new, name)

    if new[2] == "yearly":
        last_check_off = datetime.strptime(new[4], '%Y-%m-%d').date()
        last_check_off = datetime.strftime(last_check_off, '%Y')
        current_year = date.today().strftime("%Y")
        diff = int(current_year) - int(str(last_check_off))
        reset_streak(db, diff, new, name)


def reset_streak(db, diff, new, name):
    """track_all_habitz function, to track the current habits and, if necessary,
    set the streak to zero if the habit has not been done in time
    :param db: connection to the database
    :param diff: the calculated difference between the current date and the date of last check-off
    :param new: this is the list of the latest habit with its respective parameters
    :param name: the name of the habit
     """
    if abs(diff) > 1:
        new[5] += 1
        new[6] = 0
        cur = db.cursor()
        cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", new)
        db.commit()
        print("So sorry to say, but you lost your streak in " + name + ". Don't worry and keep up!")
    else:
        return
