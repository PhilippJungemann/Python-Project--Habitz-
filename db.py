import sqlite3
from datetime import date, datetime


def get_db(name="main.db"):
    """get_db function, to get connection to the database
    :param name: name of the database
    """
    db = sqlite3.connect(name)
    create_tables(db)
    return db


def create_tables(db):
    """create_tables function, to create a table if it not already exists
    :param db: connection to the database
     """
    cur = db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS habitz (
    name TEXT, description TEXT, interval INT, creation_date TEXT, date_of_completion TEXT, 
    count_streak_loss INT, count_longest_streak INT)""")

    db.commit()


def add_habit(db, name, description, interval, creation_date, date_of_completion, count_streak_loss,
              count_longest_streak):
    """add_habit function, to add a habit to the database
    :param db: connection to the database
    :param name: the name of the habit
    :param description: the description of the habit
    :param interval: the interval that must not be broken in order not to lose a streak
    :param creation_date: the date of the habit creation
    :param date_of_completion: here the date of completion will be inserted
    :param count_streak_loss: this will be incremented if a check-off interval is missed
    :param count_longest_streak: this will be incremented if a check-off is done in time
     """
    cur = db.cursor()
    cur.execute("INSERT INTO habitz VALUES (?, ?, ?, ?, ?, ?, ?)", (name, description, interval, creation_date,
                date_of_completion, count_streak_loss, count_longest_streak))
    db.commit()


def check_off_habit(db, name):
    """check_off_habit function, to check off a habit after having it done
    :param db: connection to the database
    :param name: the name of the habit
     """
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


def insert_date_of_completion(db, completed_habit, cur):
    """insert_date_of_completion function, to increment the streak-count and inserting the date of completion
    :param db: connection to the database
    :param completed_habit: the name of the  completed habit
    :param cur: connection to the cursor in the database
     """
    completed_habit[4] = str(date.today())
    completed_habit[6] += 1
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", completed_habit)
    db.commit()
    print("Your habit has been successfully checked off. Congratulations, you're doing great!")


def get_habit_names(db):
    """get_habit_names function, to get the names out of the database
    :param db: connection to the database
     """
    cur = db.cursor()
    cur.execute("SELECT DISTINCT name FROM habitz")
    names = cur.fetchall()
    # Creating a list of the first part of all tuples
    names = [x[0] for x in names]
    return names


def get_habit_periodicity(db):
    """get_habit_periodicity function, to get the periodicity out of the database
    :param db: connection to the database
     """
    cur = db.cursor()
    cur.execute("SELECT DISTINCT interval FROM habitz")
    periodicity = cur.fetchall()
    # Creating a list of the first part of all tuples
    periodicity = [x[0] for x in periodicity]
    return periodicity


def get_habit_data(db, name):
    """get_habit_data function, to get all habit data
    :param db: connection to the database
    :param name: the name of the habit
     """
    cur = db.cursor()
    cur.execute("SELECT * FROM habitz WHERE name =?", (name,))
    return cur.fetchall()


def delete_habit(db, name):
    """delete_habit function, to delete a habit
    :param db: connection to the database
    :param name: the name of the habit
     """
    cur = db.cursor()
    cur.execute("DELETE from habitz WHERE name = ?", (name,))
    db.commit()
