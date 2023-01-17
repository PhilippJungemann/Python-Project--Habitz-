from db import add_habit, create_tables
from datetime import date


class Habit:

    def __init__(self, name: str, desc: str, inter: str):
        """Counter class, to count events
        :param name: the name of the counter
        :param desc: the description of the counter
        :param inter: the interval that must not be broken in order not to lose a streak
        """
        self.name = name
        self.description = desc
        self.interval = inter
        self.creation_date = date.today()
        self.date_of_completion = None
        self.count_missed_check_off = 0
        self.count_longest_streak = 0

    def store(self, db):
        create_tables(db)
        add_habit(db, self.name, self.description, self.interval, self.creation_date, self.date_of_completion,
                  self.count_missed_check_off, self.count_longest_streak)
