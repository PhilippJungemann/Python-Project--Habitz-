from db import get_habit_data
from datetime import date, datetime


# tracker
def track_all_habitz(db, name):
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

    if new[2] == "weekly":
        last_check_off = datetime.strptime(new[4], '%Y-%m-%d').date()
        last_check_off = datetime.strftime(last_check_off, '%W')
        current_week = date.today().strftime("%W")
        # year change
        diff = int(current_week) - int(str(last_check_off))
        reset_streak(db, diff, new, name)

    if new[2] == "monthly":
        last_check_off = datetime.strptime(new[4], '%Y-%m-%d').date()
        last_check_off = datetime.strftime(last_check_off, '%m')
        current_month = date.today().strftime("%m")
        # year change
        diff = int(current_month) - int(str(last_check_off))
        reset_streak(db, diff, new, name)

    if new[2] == "yearly":
        last_check_off = datetime.strptime(new[4], '%Y-%m-%d').date()
        last_check_off = datetime.strftime(last_check_off, '%Y')
        current_year = date.today().strftime("%Y")
        diff = int(current_year) - int(str(last_check_off))
        reset_streak(db, diff, new, name)


def reset_streak(db, diff, new, name):
    if abs(diff) > 1:
        new[5] += 1
        new[6] = 0
        cur = db.cursor()
        cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", new)
        db.commit()
        print("So sorry to say, but you lost your streak in " + name + ". Don't worry keep up!")
    else:
        print("this works!")
        return
