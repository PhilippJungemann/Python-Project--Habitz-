from db import get_habit_data, get_habit_names


# Getting habit names and convert them to a nice string
def analyse_habit_names(db):
    all_habits = str(get_habit_names(db))
    all_habits = all_habits.replace("[", "")
    all_habits = all_habits.replace("'", "")
    all_habits = all_habits.replace("]", "")
    return all_habits


# Creating a list of habits with the same periodicity
def analyse_same_periodicity(db, period):
    cur = db.cursor()
    cur.execute("SELECT DISTINCT name FROM habitz WHERE interval=?", (period,))
    names = cur.fetchall()
    # Creating a list of the first part of all tuples
    names = [x[0] for x in names]
    return names


# Getting the longest streak per habit
def analyse_longest_streaks_per_habit(db, name):
    data = get_habit_data(db, name)
    longest_streak = 0
    for habit in data:
        if int(habit[6]) > longest_streak:
            longest_streak = int(habit[6])
    print("The longest streak for '" + name + "' is " + str(longest_streak))


# Getting the longest streak overall
def analyse_longest_streak_overall(db):
    names = get_habit_names(db)
    longest_streak = 0
    winner = None
    # First looping through the names
    for name in names:
        data = get_habit_data(db, name)
        # For every name looping through the habit data to find the highest number in count_longest_streak
        for habit in data:
            if int(habit[6]) > longest_streak:
                longest_streak = int(habit[6])
                winner = habit[0]
    print("The longest streak of all times is " + str(longest_streak) + " for the habit '" + winner + "'")


# Getting the habit with the biggest number of missed check-offs
def analyse_most_struggle(db):
    names = get_habit_names(db)
    most_struggle = 0
    loser = None
    # First looping through the names
    for name in names:
        data = get_habit_data(db, name)
        # For every name looping through the habit data to find the highest number in count_missed_check_off
        for habit in data:
            if int(habit[5]) > most_struggle:
                most_struggle = int(habit[5])
                loser = habit[0]
    print("The habit you struggled the most with " + str(most_struggle) + " missed check-offs is: '" + loser + "'")
