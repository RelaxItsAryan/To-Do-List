import os

FILE_NAME = "tasks.txt"

def load_tasks():
    """Load tasks from file and return as list of dictionaries."""
    tasks = []
    if not os.path.exists(FILE_NAME):
        open(FILE_NAME, 'w').close()

    with open(FILE_NAME, "r") as f:
        for line in f:
            if "|" in line:
                task, status = line.strip().split(" | ")
                tasks.append({"task": task, "status": status})
    return tasks
def save_tasks(tasks):
    """Save task list back to file."""
    with open(FILE_NAME, "w") as f:
        for t in tasks:
            f.write(f"{t['task']} | {t['status']}\n")

def add_task():
    task = input("Enter new task: ").strip()
    tasks = load_tasks()
    tasks.append({"task": task, "status": "pending"})
    save_tasks(tasks)
    print("Task added successfully!")


def view_pending_tasks():
    tasks = load_tasks()
    print("\n--- Pending Tasks ---")
    count = 0
    for i, t in enumerate(tasks):
        if t["status"] == "pending":
            print(f"{i + 1}. {t['task']}")
            count += 1
    if count == 0:
        print("No pending tasks!")
    print()


def mark_task_completed():
    tasks = load_tasks()
    view_pending_tasks()

    index = int(input("Enter task number to mark completed: ")) - 1

    if 0 <= index < len(tasks) and tasks[index]["status"] == "pending":
        tasks[index]["status"] = "done"
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task number!")


def delete_task():
    tasks = load_tasks()
    print("\n--- All Tasks ---")
    for i, t in enumerate(tasks):
        print(f"{i + 1}. {t['task']} ({t['status']})")

    index = int(input("Enter task number to delete: ")) - 1

    if 0 <= index < len(tasks):
        deleted = tasks.pop(index)
        save_tasks(tasks)
        print(f"Task '{deleted['task']}' deleted!")
    else:
        print("Invalid task number!")
def main():
    while True:
        print("\n====== TO-DO LIST MENU ======")
        print("1. Add Task")
        print("2. View Pending Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_pending_tasks()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()