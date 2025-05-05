tasks = []

def show_menu():
    print("--- To-Do List ---\n")
    print("1. View Task")
    print("2. Add Task")
    print("3. Delete Task") 
    print("4. Exit")
    
while True :
    show_menu()
    choice = int(input("Enter choice between (1-4) : "))
    
    if choice == 1 :
        if not tasks :
            print("No tasks added yet. ")
        else:
            for i , task in enumerate(tasks , 1):
                print(f"{i}.{task}") 

    elif choice == 2 :
        task = input("Enter new task :")
        
        tasks.append(task)
        print("Task Added")
        
    elif choice == 3 :
        
        task_num = int(input("Enter the task number to delete : "))
        
        if 0 < task_num <= len(tasks):
            removed = tasks.pop(task_num-1)
            print(f"Removed task : {removed}")
        
        else:
            print("Invalid task number")
            
    elif choice == 4 :
        print("Exiting To-Do List . Goodbye!")
        break ; 
    
    else:
        print("Invalid Choice. Try Again.")
        
