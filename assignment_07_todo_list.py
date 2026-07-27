# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
#
# TASK: Console-Based To-Do List Application
# =============================================================================


def print_menu():
    """Display the main menu."""
    print("============================")
    print("     TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


def add_task(tasks):
    """Prompt for a task description and add it to the list."""
    description = input("Enter task: ")
    tasks.append(description)
    print(f'Task added: "{description}"')


def view_tasks(tasks):
    """Display all tasks, numbered from 1. Show a message if empty."""
    if not tasks:
        print("Your to-do list is empty. Add a task to get started!")
        return

    print("Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def delete_task(tasks):
    """Show tasks, then remove the one the user picks by number."""
    if not tasks:
        print("Your to-do list is empty. Nothing to delete.")
        return

    view_tasks(tasks)

    try:
        choice = int(input("Enter task number to delete: "))
    except ValueError:
        print("Error: please enter a valid task number.")
        return

    if choice < 1 or choice > len(tasks):
        print("Error: that task number doesn't exist.")
        return

    removed = tasks.pop(choice - 1)
    print(f'Task "{removed}" has been removed.')


def main():
    tasks = []

    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: please enter a number from 1 to 4.")

        print()


if __name__ == "__main__":
    main()