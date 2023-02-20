# Python-Project "Habitz"
## Habit Tracker App
 
 ## Table of content
 1. Introduction
 2. Communication from user to Habitz
 3. Communication from Habitz to user
 4. Interactiing of the individual modules
 5. Testing the modules
 6. Benefits for the user of Habitz
 7. Requirements
 
 
 ## 1. Introduction
 
This app helps the user to acquire positive habits. 
Therefor, the user can define habits that he or she has to "work through" within a certain period of time. 
The idea behind “Habitz” is to support the user as best as possible in achieving his or her goal of acquiring positive new habits. 
Extensive analysis options and a reminder function keep the user motivated.

## 2. Communication from user to Habitz: 

Communication is realized via a "command line interface" (cli). The cli is opened in Pycharm via the terminal by typing "python main.py". The input starts the While- Loop in the main module and opens the cli. The loop ends only when the user selects "Exit Habitz" via the input field and thus sets the condition for the While-Loop to "false". 
After opening the app, the user can choose whether to 
1. Create a new habit,
2. Mark a habit as completed,
3. Analyze his habits,
4. Delete a habit or 
5. Exit Habitz. 

When the choice is made to "create a new habit", the name of the habit, the description and the interval (daily, weekly, monthly or yearly) in which the habit must be done must be entered. The parameters for creating the habit, the date of completion, the counter of missed completions and the counter of successful completions in a row are created automatically. 

Once the choice is made to "mark a habit as completed", the user is prompted to select the appropriate name from a list of the current habit. After that, a function is executed that marks the habit as completed for the corresponding time period and increases the counter for the corresponding streak by 1.

If "analyse my habits" is selected, it is possible to display: 
1. All active habits, 
2. A list of habits with the corresponding streak, 
3. The longest streak of all times, 
4. The habit with the most missed completions, 
5. The longest streak for a particular habit, 
6. A list of all habits with the same periodicity

In addition to that the following options can be chosen:

7. Get back to main menu and
8. Exit Habitz. 

If the user selects "Delete a habit", the program will first ask for further confirmation of the operation, as the deletion of the property with all the associated data in the database will be final. 

Via "Exit Habitz" the While-Loop of the program is stopped and the cli is closed. 

## 3. Communication from Habitz to user: 

When the app is opened, the tracker function is executed first and checks which habits, if any, have not been completed in time. If this is the case, the counter for "Lost Streak" is increased by 1 and the counter for "Longest Streak" is set to 0. If a streak loss has occurred, the user is notified via the command line interface. 
After the tracker function has run through, the reminder function starts. This function checks in the database which tasks are pending at which time and informs the user about them via the cli.

## 4. Interactiing of the individual modules:

The starting point of Habitz is the module "main". Here the cli is opened for communication with the user. 
The other modules and their respective functions can be accessed via the "main" module. 
The "habit" module is used to create new habits. Via the class "Habit" and its function "store" a new habit is created in the module "db"(database). 
Analyses are performed using the "analyse" module. The functions in "analysis" use functions from the "db" module to communicate with the database.

## 5. Testing the modules:
Via the module "test_project" there is the possibility to test the individual modules and their respective functions on a clearly arranged data set by selecting "Run test_project" in Pycharm. After that, a possibly older test data set from a previous test is deleted first, in order to create a new data set ("test.db") afterwards. The content of this data set is directly visible for the user in the module in order to compare the test results with the present data set without detours. Afterwards, the functions of the individual modules are checked for the correct return values. 

In addition, the project has a much more extensive data set ("main.db"), which is controlled by the user in "live operation" via the cli. Extensive analyses can be carried out here via the cli using "analyze my habitz".   


## 6. Benefits for the user of Habitz:

The special benefit of the "Habitz" app lies in the bidirectional communication and the comprehensive analysis options. 
Both contribute to an increased motivation of the user and facilitate the achievement of personal goals. 
On the one hand, the user is thus proactively informed by the app about the current challenges and achievements in a motivating manner when opening it; 
On the other hand, the user can perform in-depth analyses of the stored data on his habits and is motivated to keep setting new personal records. 


## 7. Requirements: 

Python Modules that have to be installed and imported:
questionary; 

Python Modules that have to be imported but do not to be be installed, because they are already part of the python package:
sqlite3; datetime; os
