# Sample code for a command-line To-Do List application

tasks = []


def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)


def view_tasks():
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")


while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
