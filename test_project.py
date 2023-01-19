import pytest
import habit
from db import get_db, check_off_habit, delete_habit, get_habit_data


db = get_db("test.db")
name = "Jogging"
cur = db.cursor()


def create_method():

    cur.execute("""CREATE TABLE IF NOT EXISTS habitz (
    name TEXT, description TEXT, interval INT, creation_date TEXT, date_of_completion TEXT, 
    count_streak_loss INT, count_longest_streak INT)""")


def generate_test_data():
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

#        increment_counter(db, "test_counter", "2021-12-06")
#        increment_counter(db, "test_counter", "2021-12-07")
#
#        increment_counter(db, "test_counter", "2021-12-09")
#        increment_counter(db, "test_counter", "2021-12-10")


def test_db_counter(self):
    generate_test_data()
    habit.Habit.store(self, db)
    check_off_habit(db, name)
    check_off_habit(db, name)
    delete_habit(db, name)


def test_length_counter():
    data = get_habit_data(db, "Jogging")
    assert len(data) == 29

    data = get_habit_data(db, "Swimming")
    assert len(data) == 5


def teardown_method():
    import os
    os.remove("test.db")




