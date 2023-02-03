# Python-Project "Habitz"
# Habit Tracker App
 
 ## Table of content
 1. Introduction
 2. Communication from user to Habitz
 3. Communication from Habitz to user
 4. Interactiing of the individual modules
 5. Benefits for the user of Habitz
 6. Requirements
 
 
 
 1. Introduction
 
This app helps the user to acquire positive habits. 
To do this, the user can define habits that he or she has to "work through" within a certain period of time. 
The idea behind “Habitz” is to support the user as best as possible in achieving his or her goal of acquiring positive new habits. 
Extensive analysis options and a reminder function keep the user motivated.

2. Communication from user to Habitz: 

Communication takes place via a "command line interface".
After opening the app, the user can choose whether to 
create a new habit, 
mark a habit as done, 
analyze his habits or 
leave the app again. 
When the choice is made to "create a new habit", the name of the habit, the description and the interval (daily, weekly, monthly or yearly) in which the habit must be done must be entered. The parameters for creating the habit, the date of completion, the counter of missed completions and the counter of successful completions in a row are created automatically. 

Once the choice is made to "mark a habit as completed", the user is prompted to select the appropriate name from a list of the current habit. After that, a function is executed that marks the habit as completed for the corresponding time period and increases the counter for the corresponding streak by 1. 
If "analyze my habits" is selected, it is possible to display all active habits, a list of habits with the corresponding streak, the longest streak of all times, habit with the most missed completions, the longest streak for a particular habit and a list of all habits with the same periodicity.

3. Communication from Habitz to user: 

When the app is opened, the tracker function is executed first and checks which habits, if any, have not been completed in time. If this is the case, the counter for "Lost Streak" is increased by 1 and the counter for "Longest Streak" is set to 0. If a streak loss has occurred, the user is notified via the command line interface. 
After the tracker function has run through, the reminder function starts. This function checks in the database which tasks are pending at which time and informs the user about them.

4. Interactiing of the individual modules:

The starting point of Habitz is the module "main". Here the "Command Line Interface" is opened for communication with the user. 
The other modules and their respective functions can be accessed via the "main" module. 
The "habit" module is used to create new habits. Via the class "Habit" and its function "store" a new habit is created in the module "db"(database). 
Analyses are performed using the "analyse" module. The functions in "analysis" use functions from the "db" module to communicate with the database.

5. Benefits for the user of Habitz:

The special benefit of the "Habitz" app lies in the bidirectional communication and the comprehensive analysis options. 
Both contribute to an increased motivation of the user and facilitate the achievement of personal goals. 
On the one hand, the user is thus proactively informed by the app about the current challenges and achievements in a motivating manner when opening it; 
On the other hand, the user can perform in-depth analyses of the stored data on his habits and is motivated to keep setting new personal records. 


6. Requirements: 

Python Modules that have to be installed and imported:
questionary; 

Python Modules that have to be imported but do not to be be installed, because they are already part of the python package:
sqlite3; datetime; os
