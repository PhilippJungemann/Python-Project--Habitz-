from db import add_habit, create_tables
from datetime import date


class Habit:

    def __init__(self, name: str, desc: str, inter: str):
        """Counter class, to count events
        :param self.name: the name of the habit
        :param self.description: the description of the habit
        :param self.interval: the interval that must not be broken in order not to lose a streak
        :param self.creation_date: the date of the habit creation
        :param self.date_of_completion: here the date of completion will be inserted
        :param self.count_streak_loss: this will be incremented if a check-off interval is missed
        :param self.count_longest_streak: this will be incremented if a check-off is done in time
        """
        self.name = name
        self.description = desc
        self.interval = inter
        self.creation_date = date.today()
        self.date_of_completion = None
        self.count_streak_loss = 0
        self.count_longest_streak = 0

    def store(self, db):
        """store function, to store parameters of the new habit in the database
        :param db: connection to the database
        """
        create_tables(db)
        add_habit(db, self.name, self.description, self.interval, self.creation_date, self.date_of_completion,
                  self.count_streak_loss, self.count_longest_streak)
