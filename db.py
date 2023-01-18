import sqlite3
from datetime import date, datetime


# Getting connection to the database
def get_db(name="main.db"):
    db = sqlite3.connect(name)
    create_tables(db)
    return db


# Creating a table if it not already exists
def create_tables(db):
    cur = db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS habitz (
    name TEXT, description TEXT, interval INT, creation_date TEXT, date_of_completion TEXT, 
    count_streak_loss INT, count_longest_streak INT)""")

    db.commit()


# Adding a habit to the database
def add_habit(db, name, description, interval, creation_date, date_of_completion, count_streak_loss,
              count_longest_streak):
    cur = db.cursor()
    cur.execute("INSERT INTO habitz VALUES (?, ?, ?, ?, ?, ?, ?)", (name, description, interval, creation_date,
                date_of_completion, count_streak_loss, count_longest_streak))
    db.commit()


# Checking off a habit after having done it
def check_off_habit(db, name):
    cur = db.cursor()
    cur.execute("SELECT * FROM habitz WHERE name = ?", (name,))
    habit_list = cur.fetchall()
    # Take the last tuple and convert it into a list
    completed_habit = habit_list.pop()
    completed_habit = list(completed_habit)
    # Checking off the habit for the first time
    if completed_habit[4] is None:
        completed_habit[4] = str(date.today())
        completed_habit[6] += 1
        cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", completed_habit)
        db.commit()
        print("Your habit has been successfully checked off for the first time! What a great start!")
        return

    # Checking off a daily habit
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
    # Checking off a weekly habit
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
    # Checking off a monthly habit
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
    # Checking off a yearly habit
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


# Function for incrementing the streak-count and inserting the date of completion
def insert_date_of_completion(db, completed_habit, cur):
    completed_habit[4] = str(date.today())
    completed_habit[6] += 1
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", completed_habit)
    db.commit()
    print("Your habit has been successfully checked off. Congratulations, you're doing great!")


# Function for getting the names out of the database
def get_habit_names(db):
    cur = db.cursor()
    cur.execute("SELECT DISTINCT name FROM habitz")
    names = cur.fetchall()
    # Creating a list of the first part of all tuples
    names = [x[0] for x in names]
    return names


# Function for getting the periodicity out of the database
def get_habit_periodicity(db):
    cur = db.cursor()
    cur.execute("SELECT DISTINCT interval FROM habitz")
    periodicity = cur.fetchall()
    # Creating a list of the first part of all tuples
    periodicity = [x[0] for x in periodicity]
    return periodicity


# Function for getting all habit data
def get_habit_data(db, name):
    cur = db.cursor()
    cur.execute("SELECT * FROM habitz WHERE name =?", (name,))
    return cur.fetchall()


# Function for deleting a habit
def delete_habit(db, name):
    cur = db.cursor()
    cur.execute("DELETE from habitz WHERE name = ?", (name,))
    db.commit()
