class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

def add_task(tasks):
    description = input("Enter task description: ")
    deadline = input("Enter task deadline: ")
    task = Task(description, deadline)
    tasks.append(task)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task.completed else "Not Completed"
            print(f"{i}. {task.description} (Deadline: {task.deadline}, Status: {status})")

def mark_task_completed(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index].completed = True
        print("Task marked as completed.")
    else:
        print("Invalid task index.")

def delete_task(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the index of the task to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        print("Task deleted successfully.")
    else:
        print("Invalid task index.")

def main():
    tasks = []
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()