def task():
    tasks = []
    totalTasks = int(input("Enter no. of Tasks you want to add: "))
    for i in range(1, totalTasks+1):
        add = input(f"Enter Task {i}: ")
        tasks.append(add)
    while True:
        option = int(input("----------------------------------\n1.ADD task\n2.Update task\n3.Delete task\n4.View task\n5.Exit Simulator\n-->Enter your Choice: "))
        if option == 1:
            addTask = input("Enter the task you want to add: ")
            tasks.append(addTask)
        elif option == 2:
            updateTask = input("Enter the task you want to update")
            if updateTask in tasks:
                indexValue = tasks.index(updateTask)

                newTask = input("Enter new task")
                tasks[indexValue] = newTask
            elif updateTask not in tasks:
                print("No matching task found..")
                addNewTask = input("Do you want to add this task(yes/no).")
                if addNewTask == "yes":
                    tasks.append(updateTask)
        elif option == 3:
            deleteTask = input("Enter the task you want to delete: ")
            found = False
            for t in tasks:
                if t.lower() == deleteTask.lower():
                    tasks.remove(t)   # remove the actual stored task
                    print(f"Task '{t}' deleted.")
                    found = True
                    break
                if not found:
                    print("No matching task found.")

        elif option == 4:
            print(tasks)
        elif option == 5:
            print("Exiting the TO_DO Simulator...\nThankyou for using TO_DO Simulator")
            return
task()