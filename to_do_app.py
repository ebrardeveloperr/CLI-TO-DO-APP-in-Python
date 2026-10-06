## Cli TO DO APP

tasks = []

def show_menu():
    print("Welcome to the CLI To-Do App!")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")


# code for adding a task

def add_task():
    task=input("Enter your Task: ")
    tasks.append({"task" :task, "Done": False})
    print(f'Task \t "{task}" \t Added Successfully!')

#code for viewing tasks

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    print("Your Tasks: ")
    for index,task in enumerate(tasks ,start=1):
        status = "✅" if task["Done"] else "❌"
        print(f"{index}. {task['task']} - {status}")

#code for marking a task as completed

def mark_done():
    view_tasks()
    if not tasks:
        return
    try:
        index =int(input("Enter the task number to mark as completed: ")) -1
        if 0 <= index<len(tasks):
            tasks[index]["Done"] = True
            print(f'Task \t "{tasks[index]["task"]}" \t Marked as Completed!')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

#code for deleting a task

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            deleted_task = tasks.pop(index)
            print(f'Task \t "{deleted_task["task"]}" \t Deleted Successfully!')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

#code for main function
def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Thank you for using the CLI To-Do App!")
            break
        else:
            print("Invalid choice. Please try again.")

main()