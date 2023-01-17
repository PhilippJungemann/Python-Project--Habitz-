from db import get_habit_data, get_habit_names


def analyse_habit_names(db):
    all_habits = str(get_habit_names(db))
    all_habits = all_habits.replace("[", "")
    all_habits = all_habits.replace("'", "")
    all_habits = all_habits.replace("]", "")
    return all_habits


def analyse_same_periodicity(db, period):
    cur = db.cursor()
    cur.execute("SELECT DISTINCT name FROM habitz WHERE interval=?", (period,))
    names = cur.fetchall()
    names = [x[0] for x in names]
    return names


def analyse_longest_streaks(db, name):
    data = get_habit_data(db, name)
    longest_streak = 0
    for habit in data:
        if int(habit[6]) > longest_streak:
            longest_streak = int(habit[6])
    print("The longest streak for '" + name + "' is " + str(longest_streak))
