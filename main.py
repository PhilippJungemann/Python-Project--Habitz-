import questionary
from db import get_db, check_off_habit, get_habit_names, get_habit_periodicity, delete_habit
from habit import Habit
from analyse import analyse_habit_names, analyse_same_periodicity, analyse_longest_streaks
from tracker import track_all_habitz
from reminder import reminder


# Creating a cli for the user
def cli():
    # Getting connected to the database
    db = get_db()

    names_list = get_habit_names(db)
    for name in names_list:
        track_all_habitz(db, name)
    for name in names_list:
        reminder(db, name)

    # Starting the while-loop
    stop = False
    while not stop:
        # Giving the user access to the different options to act in the app
        choice = questionary.select(
            "What do you want to do?",
            choices=["Create a new habit", "Mark a habit as completed", "Analyse my habits",
                     "Delete a habit", "Exit Habitz"]
        ).ask()
        if choice != "Exit Habitz":
            print("Great stuff!")

        # Here the user gets the option to create a new habit
        # For this purpose the necessary parameters are requested
        if choice == "Create a new habit":
            name = questionary.text("What is the name of your new habit?").ask()
            names = get_habit_names(db)
            try:
                index = names.index(name)
                print("A habit with this name already exists in your list of habits at the place " + str(index) +
                      ". Please choose another name!")
                continue
            except ValueError:

                desc = questionary.text("What is the description of your new habit?").ask()
                inter = questionary.select(
                    "Within what time frame should the habit be completed? ",
                    choices=["daily", "weekly", "monthly",
                             "yearly"]
                ).ask()
#                inter = questionary.text("Every how many days the habit should be checked off at the latest?").ask()
                # The parameters are passed and the corresponding habit is stored in the database
                habit = Habit(name, desc, inter)
                habit.store(db)
                print("Your new habit has been created successfully!")
                continue

        # Here the user gets the option to mark a habit as done
        elif choice == "Mark a habit as completed":
            names = get_habit_names(db)
            name = questionary.select(
                "Which habit do you want to mark as completed for today?",
                choices=names
            ).ask()

            check_off_habit(db, name)

            continue

        elif choice == "Analyse my habits":
            selected = questionary.select(
                "What do you want to analyse?",
                choices=["What are my current habits?", "Create a list of all habits with the same periodicity!",
                         "Make a list of the longest streaks of all my habits!",
                         "Show the longest streak for a particular habit!",
                         "What is my longest streak of all times?", "Which habit do I struggle with the most?",
                         "Get back to the main menu", "Exit Habitz"]
            ).ask()
            if selected == "What are my current habits?":
                names = analyse_habit_names(db)
                print("Your current habits are: "+str(names))
                continue
            elif selected == "Create a list of all habits with the same periodicity!":
                periodicity = get_habit_periodicity(db)
                period = questionary.select(
                    "Please enter the desired periodicity in days!",
                    choices=periodicity
                ).ask()
                same_period = analyse_same_periodicity(db, period)
                print("Your habits with a periodicity of " + period + " days are: " + str(same_period))
                continue
            elif selected == "Make a list of the longest streaks of all my habits!":
                names_list = get_habit_names(db)
                for name in names_list:
                    analyse_longest_streaks(db, name)
                continue
            elif selected == "Show the longest streak for a particular habit!":
                names = get_habit_names(db)
                name = questionary.select(
                    "To which habit should the longest streak be displayed?",
                    choices=names
                ).ask()
                analyse_longest_streaks(db, name)
                continue
            elif selected == "What is my longest streak of all times?":
                print("stuff")
            elif selected == "Which habit do I struggle with the most?":
                print("stuff")
            elif selected == "Get back to the main menu":
                continue
            else:
                stop = True

        if choice == "Delete a habit":
            names = get_habit_names(db)
            name = questionary.select(
                "Which habit do you want to delete?",
                choices=names
            ).ask()

            confirmation = questionary.confirm("Are you sure that you want to delete '"+name+"' ?").ask()
            if confirmation:
                delete_habit(db, name)
                print("'" + name + "' has been deleted successfully!")
            else:
                continue

        # doublecheck here if the habit really should be deleted, because that will be permanent

        else:
            print("Bye Habbi!")
            stop = True


if __name__ == '__main__':
    cli()
