tasks = []
def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print("\n")
    print(f"Task '{task}' has been added to the list!.")

def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current tasks: ")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")


def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Choose the number of task you want to delete:  "))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task number {taskToDelete} successfuly deleted!.")
        else:
            print(f"Task #{taskToDelete} was not found.")

    except:
        print("Invalid Input.")

if __name__ == "__main__":
    #make the loop
    while True:
        
        print("\n")
        print("=-------------------------=")
        print("Welcome to Seemon's To do list program!")
        print("What would you like to do?")
        print("1. Add a new task.")
        print("2. Delete task.")
        print("3. List tasks")
        print("4. Quit.")
        print("=-------------------------=")

        #Input here
        choice = input("Select your option: ")

        if choice == "1":
            addTask = ()
        elif choice == "2":
            deleteTask = ()
        elif choice == "3":
            listTasks = ()
        elif choice == "4":
            break
        else: 
            print("Invalid input!, Please try again.")
    print("Goodbye!!, have a great day!.")