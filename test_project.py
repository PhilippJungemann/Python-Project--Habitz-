import os
import sqlite3
from db import get_habit_data
from analyse import analyse_habit_names, analyse_longest_streak_overall, analyse_most_struggle, \
    analyse_longest_streaks_per_habit, analyse_same_periodicity
from tracker import track_all_habitz, reset_streak


def teardown_method():
    os.remove("test.db")


teardown_method()


def get_test_db(name="test.db"):
    db = sqlite3.connect(name)
    create_method(db)
    return db


def create_method(db):
    cur = db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS habitz (
    name TEXT, description TEXT, interval INT, creation_date TEXT, date_of_completion TEXT, 
    count_streak_loss INT, count_longest_streak INT)""")


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
                                                             "2023-01-25", 1, 1,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-26", 1, 2,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-27", 1, 3,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-28", 1, 4,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-29", 1, 5,))
    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Jogging", "Jogging everyday", "daily", "2023-01-01",
                                                             "2023-01-30", 1, 6,))
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


def test_analyse_module(name="Jogging",  db=get_test_db()):
    generate_test_data(db)
    # testing if the generating of the test data was done correctly
    data = get_habit_data(db, name)
    assert len(data) == 29
    data = get_habit_data(db, name="Swimming")
    assert len(data) == 5
    # testing if the function analyse_habit_names is working correctly
    habit_names = analyse_habit_names(db)
    assert habit_names == "Jogging, Swimming"
    # testing if the function analyse_same_periodicity is working correctly
    daily_habits = analyse_same_periodicity(db, period="daily")
    assert daily_habits == ['Jogging']
    # testing if the function analyse_longest_streak_overall is working correctly
    habit_with_longest_streak = analyse_longest_streak_overall(db)
    assert habit_with_longest_streak == "The longest streak of all time is 23 for the habit 'Jogging'"
    longest_streak_per_habit = analyse_longest_streaks_per_habit(db, name)
    # testing if the function analyse_most_struggle is working correctly
    assert longest_streak_per_habit == "The longest streak for 'Jogging' is 23"
    habit_with_most_struggle = analyse_most_struggle(db)
    assert habit_with_most_struggle == "The habit you struggled the most with 1 missed check-offs is: 'Jogging'"


def test_tracker_module(name="Jogging",  db=get_test_db()):
    track_check = track_all_habitz(db, name)
    assert track_check == "Wurd"
