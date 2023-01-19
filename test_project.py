import habit
from db import check_off_habit, delete_habit, get_habit_data
import sqlite3
from datetime import date
from analyse import analyse_habit_names


def teardown_method():
    import os
    os.remove("test.db")


teardown_method()


def create_method(db):
    cur = db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS habitz (
    name TEXT, description TEXT, interval INT, creation_date TEXT, date_of_completion TEXT, 
    count_streak_loss INT, count_longest_streak INT)""")


def get_test_db(name="test.db"):
    db = sqlite3.connect(name)
    create_method(db)
    return db


# data = get_test_db()
# cur = data.cursor()


def generate_test_data(db):
    cur = db.cursor()
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-01", 0, 1,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-02", 0, 2,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-03", 0, 3,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-04", 0, 4,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-05", 0, 5,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-06", 0, 6,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-07", 0, 7,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-08", 0, 8,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-09", 0, 9,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-10", 0, 10,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-11", 0, 11,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-12", 0, 12,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-13", 0, 13,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-14", 0, 14,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-15", 0, 15,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-16", 0, 16,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-17", 0, 17,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-18", 0, 18,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-19", 0, 19,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-20", 0, 20,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-21", 0, 21,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-22", 0, 22,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-23", 0, 23,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-24", 0, 24,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-25", 0, 25,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-26", 0, 26,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-27", 0, 27,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-28", 0, 28,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-29", 0, 29,))
    db.commit()

    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Swimming", "Swimming every week", "weekly", "2023-01-01",
                                                             "2023-01-01", 0, 1,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Swimming", "Swimming every week", "weekly", "2023-01-01",
                                                             "2023-01-08", 0, 2,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Swimming", "Swimming every week", "weekly", "2023-01-01",
                                                             "2023-01-15", 0, 3,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Swimming", "Swimming every week", "weekly", "2023-01-01",
                                                             "2023-01-21", 0, 4,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Swimming", "Swimming every week", "weekly", "2023-01-01",
                                                             "2023-01-28", 0, 5,))
    db.commit()


def test_length_counter(name="Jogging",  db=get_test_db()):
    generate_test_data(db)
    data = get_habit_data(db, name="Jogging")
    assert len(data) == 29

    data = get_habit_data(db, name="Swimming")
    assert len(data) == 5


class Habit:

    def __init__(self, name: str, desc: str, inter: str):
        """Counter class, to count events
        :param self.name: the name of the counter
        :param self.description: the description of the counter
        :param self.interval: the interval that must not be broken in order not to lose a streak
        :param self.creation_date: the date of the habit creation
        :param self.date_of_completion: here the date of completion will be inserted
        :param self.count_missed_check_off: this will be incremented if a check-off interval is missed
        :param self.count_missed_check_off: this will be incremented if a check-off is done in time
        """
        self.name = name
        self.description = desc
        self.interval = inter
        self.creation_date = date.today()
        self.date_of_completion = None
        self.count_missed_check_off = 0
        self.count_longest_streak = 0

    def test_db_counter(self, name="Jogging", db=get_test_db()):
        generate_test_data(db)
        habit.Habit.store(self, db)
        check_off_habit(db, name)
        analyse_habit_names(db)
        delete_habit(db, name)
