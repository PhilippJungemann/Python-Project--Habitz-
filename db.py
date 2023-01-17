import sqlite3
from datetime import date, datetime


def get_db(name="main.db"):
    db = sqlite3.connect(name)
    create_tables(db)
    return db


def create_tables(db):
    cur = db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS habitz (
    name TEXT, description TEXT, interval INT, creation_date TEXT, date_of_completion TEXT, 
    count_streak_loss INT, count_longest_streak INT)""")

    db.commit()


def add_habit(db, name, description, interval, creation_date, date_of_completion, count_streak_loss,
              count_longest_streak):
    cur = db.cursor()
    cur.execute("INSERT INTO habitz VALUES (?, ?, ?, ?, ?, ?, ?)", (name, description, interval, creation_date,
                date_of_completion, count_streak_loss, count_longest_streak))
    db.commit()


def check_off_habit(db, name):
    cur = db.cursor()
    cur.execute("SELECT * FROM habitz WHERE name = ?", (name,))
    habit_list = cur.fetchall()
    # Take the last tuple and convert it into a list
    completed_habit = habit_list.pop()
    completed_habit = list(completed_habit)
    if completed_habit[4] is None:
        completed_habit[4] = str(date.today())
        completed_habit[6] += 1
        cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", completed_habit)
        db.commit()
        print("Your habit has been successfully checked off for the first time! What a great start!")
        return

    if completed_habit[2] == "daily":
        last_check_off = datetime.strptime(completed_habit[4], '%Y-%m-%d').date()
        today = date.today()
        diff = today - last_check_off
        diff = int(diff.days)
        if diff == 0:
            print("You have already done the habit in the defined period. Great, you are very motivated!")
        else:
            # Insert the current date as the date of completion of the habit and increment streak
            insert_date_of_completion(db, completed_habit, cur)
    if completed_habit[2] == "weekly":
        last_check_off = datetime.strptime(completed_habit[4], '%Y-%m-%d').date()
        last_check_off = datetime.strftime(last_check_off, '%W')
        current_week = date.today().strftime("%W")
        diff = int(current_week) - int(str(last_check_off))
        if diff == 0:
            print("You have already done the habit in the desired period. Great, you are very motivated!")
        else:
            # Insert the current date as the date of completion of the habit and increment streak
            insert_date_of_completion(db, completed_habit, cur)
    if completed_habit[2] == "monthly":
        last_check_off = datetime.strptime(completed_habit[4], '%Y-%m-%d').date()
        last_check_off = datetime.strftime(last_check_off, '%m')
        current_month = date.today().strftime("%m")
        diff = int(current_month) - int(str(last_check_off))
        if diff == 0:
            print("You have already done the habit in the desired period. Great, you are very motivated!")
        else:
            # Insert the current date as the date of completion of the habit and increment streak
            insert_date_of_completion(db, completed_habit, cur)
    if completed_habit[2] == "yearly":
        last_check_off = datetime.strptime(completed_habit[4], '%Y-%m-%d').date()
        last_check_off = datetime.strftime(last_check_off, '%Y')
        current_year = date.today().strftime("%Y")
        diff = int(current_year) - int(str(last_check_off))
        if diff == 0:
            print("You have already done the habit in the desired period. Great, you are very motivated!")
        else:
            # Insert the current date as the date of completion of the habit and increment streak
            insert_date_of_completion(db, completed_habit, cur)


def insert_date_of_completion(db, completed_habit, cur):
    completed_habit[4] = str(date.today())
    completed_habit[6] += 1
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", completed_habit)
    db.commit()
    print("Your habit has been successfully checked off. Congratulations, you're doing great!")


def get_habit_names(db):
    cur = db.cursor()
    cur.execute("SELECT DISTINCT name FROM habitz")
    names = cur.fetchall()
    names = [x[0] for x in names]
    return names


def get_habit_periodicity(db):
    cur = db.cursor()
    cur.execute("SELECT DISTINCT interval FROM habitz")
    periodicity = cur.fetchall()
    periodicity = [x[0] for x in periodicity]
    return periodicity


def get_habit_data(db, name):
    cur = db.cursor()
    cur.execute("SELECT * FROM habitz WHERE name =?", (name,))
    return cur.fetchall()


def delete_habit(db, name):
    cur = db.cursor()
    cur.execute("DELETE from habitz WHERE name = ?", (name,))
    db.commit()
