import os
import sqlite3
from habit import Habit
from db import get_habit_data, get_habit_names
from analyse import analyse_habit_names, analyse_longest_streak_overall, analyse_most_struggle, \
    analyse_longest_streaks_per_habit, analyse_same_periodicity
from tracker import track_all_habitz
from reminder import reminder


def teardown_method():
    """teardown_method function, to remove the last test database to be able to run a new test
     """
    os.remove("test.db")


teardown_method()


def get_test_db(name="test.db"):
    """get_test_db function, to create a new test database
    :param name: the name of test database
     """
    db = sqlite3.connect(name)
    create_method(db)
    return db


def create_method(db):
    """create_method function, to create a new table in the test database
    :param db: connection to the database
     """
    cur = db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS habitz (
    name TEXT, description TEXT, interval INT, creation_date TEXT, date_of_completion TEXT, 
    count_streak_loss INT, count_longest_streak INT)""")


def generate_test_data(db):
    """generate_test_data function, to create a test data set
    :param db: connection to the database
     """
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

    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Hiking", "Hiking every month", "monthly", "2023-01-01",
                                                             "2023-01-28", 0, 1,))
    db.commit()

    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Visit the dentist", "Visiting the dentist every year",
                                                             "yearly", "2023-01-01", "2023-01-28", 0, 1,))
    db.commit()

    cur.execute("INSERT INTO habitz VALUES(?,?,?,?,?,?,?)", ("Health checkup", "Doing health checkup every year",
                                                             "yearly", "2023-01-01", "2023-01-30", 0, 1,))
    db.commit()


def test_analyse_module(name="Jogging",  db=get_test_db()):
    """test_analyse_module function, to test the functions of the "analyse" module
    :param name: name of the habit used by default
    :param db: connection to the database
     """
    generate_test_data(db)
    # testing if the generating of the test data was done correctly
    data = get_habit_data(db, name)
    assert len(data) == 29
    data = get_habit_data(db, name="Swimming")
    assert len(data) == 5
    # testing if the function analyse_habit_names is working correctly
    habit_names = analyse_habit_names(db)
    assert habit_names == "Jogging, Swimming, Hiking, Visit the dentist, Health checkup"
    # testing if the function analyse_same_periodicity is working correctly
    daily_habits = analyse_same_periodicity(db, period="daily")
    assert daily_habits == ['Jogging']
    # testing if the function analyse_longest_streak_overall is working correctly
    habit_with_longest_streak = analyse_longest_streak_overall(db)
    assert habit_with_longest_streak == "The longest streak of all time is 23 for the habit 'Jogging'"
    longest_streak_per_habit = analyse_longest_streaks_per_habit(db, name)
    # testing if the function analyse_longest_streaks_per_habit is working correctly
    assert longest_streak_per_habit == "The longest streak for 'Jogging' is 23"
    habit_with_most_struggle = analyse_most_struggle(db)
    # testing if the function analyse_most_struggle is working correctly
    assert habit_with_most_struggle == "The habit you struggled the most with 1 missed check-offs is: 'Jogging'"


def test_tracker_module(name="Jogging",  db=get_test_db()):
    """test_tracker_module function, to test the functions of the "tracker" module
    :param name: name of the habit used by default
    :param db: connection to the database
     """
    track_check = track_all_habitz(db, name)
    # testing if the tracker module is working correctly. (The streak set to 0 ([6]) and the loss_of_streak increased
    # by 1 to 2 ([5]) show that the program is working correctly)
    assert track_check == ['Jogging', 'Jogging everyday', 'daily', '2023-01-01', '2023-01-30', 2, 0]


def test_reminder_module(name="Jogging",  db=get_test_db()):
    """test_reminder_module function, to test the functions of the "reminder" module
    :param name: name of the habit used by default
    :param db: connection to the database
     """
    reminding = reminder(db, name)
    # testing if the reminder module is working correctly
    assert reminding == "Your habit 'Jogging' has to be done today!"


def test_habit_module(db=get_test_db(), name="Biking", desc="I want to bike every week", inter="weekly"):
    """test_habit_module function, to test the functions of the "habit" module
    :param db: connection to the database
    :param name: name of the habit that is to be created
    :param desc: description of the habit to be created on a test basis
    :param inter: period of the habit to be created on a test basis
     """
    habit = Habit(name, desc, inter)
    habit.store(db)
    names = get_habit_names(db)
    # testing if the habit module is working correctly
    assert names[5] == 'Biking'
