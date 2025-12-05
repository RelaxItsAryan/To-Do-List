# To-Do-List
This is a simple command-line based To-Do List application built in Python. It allows users to add tasks, view pending tasks, mark tasks as completed, and delete tasks. All tasks are stored in a text file so the list persists even after the program closes.

# Features
1. Add New Tasks

Users can add tasks, which are automatically saved with a “pending” status.

2. View Pending Tasks

Displays only tasks that are still not completed, keeping the list clear and organized.

3. Mark Tasks as Completed

Updates the status of a task from “pending” to “done”.

4. Delete Tasks

Allows users to remove any task from the list entirely.

5. Persistent Storage

Tasks are stored in a text file (tasks.txt) so your list remains intact between sessions.

# How It Works

The application uses a simple menu-driven system:

# ====== TO-DO LIST MENU ======
1. Add Task
2. View Pending Tasks
3. Mark Task Completed
4. Delete Task
5. Exit


Users can select any option by entering the corresponding number.

# File Structure
ToDoList.py        # Main application script
tasks.txt          # Automatically created file to store tasks

# How to Run

Make sure Python is installed.

Place ToDoList.py in a folder.

Open a terminal in that folder and run:

python ToDoList.py


A new tasks.txt file will be created automatically if it does not exist.
