from db import get_habit_data, get_habit_names


def analyse_habit_names(db):
    all_habits = str(get_habit_names(db))
    all_habits = all_habits.replace("[", "")
    all_habits = all_habits.replace("'", "")
    all_habits = all_habits.replace("]", "")
    return all_habits
#

def analyse_same_periodicity(db, period):
    cur = db.cursor()
    cur.execute("SELECT DISTINCT name FROM habitz WHERE interval=?", (period,))
    names = cur.fetchall()
    names = str(names)
    names = names.replace("[", "")
    names = names.replace("'", "")
    names = names.replace("]", "")
    names = names.replace("(", "")
    names = names.replace(",)", "")
    return names


def analyse_longest_streaks(db, name):
    data = get_habit_data(db, name)
    longest_streak = 0
    for habit in data:
        if int(habit[6]) > longest_streak:
            longest_streak = int(habit[6])
    print("The longest streak for '" + name + "' is " + str(longest_streak))








def calculate_count(db, name):
    """
    Calculate the count of the counter.

    :param db: an initialized sqlite3 database connection
    :param counter: name of the counter present in the DB
    :return: length of the counter increment events
    it should be possible to analyse every param on its own
    """
    data = get_habit_data(db, name)

    return len(data)

