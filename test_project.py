import pytest
from habit import Habit
#from db import get_db, add_counter, increment_counter, get_counter_data
from analyse import calculate_count
import questionary
import time
from datetime import date, datetime, timedelta
from db import get_db
from analyse import calculate_count
from db import add_counter, increment_counter


def create_method():
    db = get_db("test.db")
    habit = Habit("Jogging", "I want to jog every day", "daily")
    habit.store(db)
    habit = Habit("Swimming", "I want to swim every week", "weekly")
    habit.store(db)
    habit = Habit("Hiking", "I want to hike every month", "monthly")
    habit.store(db)
    habit = Habit("Traveling", "I want to travel every year", "yearly")
    habit.store(db)


def generate_habit_data():
    name = "Jogging"
    db = get_db("test.db")
    cur = db.cursor()
    cur.execute("SELECT * FROM habitz WHERE name =?", (name,))
    data = cur.fetchall()

#        increment_counter(db, "test_counter", "2021-12-06")
#        increment_counter(db, "test_counter", "2021-12-07")
#
#        increment_counter(db, "test_counter", "2021-12-09")
#        increment_counter(db, "test_counter", "2021-12-10")


def test_db_counter():
    counter = Counter("test_counter_1", "test_description_1")
    counter.store(db)

    counter.increment()
    counter.add_event(db)
    counter.reset()
    counter.increment()


def test_db_counter():
    data = get_counter_data(db, "test_counter")
    assert len(data) == 4

    count = calculate_count(db, "test_counter")
    assert count == 4


def teardown_method():
    import os
    os.remove("test.db")




