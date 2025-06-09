import json
import os

task = []


try :
    with open("task.json",'r') as f:
        task = json.load(f)
except FileNotFoundError:
    task = []        

def save_tasks():
    with open('task.json','w') as f:
        json.dump(task, f)

while True:
    print("\nTo-Do List Menu")
    print("1 Add task")
    print("2 Show tasks")
    print("3 Mark task as done")
    print("4 Delet a task.")
    print("5 Show done tasks.")
    print("6 Show not-done tasks.")
    print("7 Edit a task")
    print("8 Exit")
    choice = input("Choose an option (1-5): ")
 
    #add new task

    if choice == '1':
        title = input("Enter task title: ")
        task.append({"title":title, "done": False})
        save_tasks()
        print("Task added successfuly!")

    #show tasks 

    elif choice == '2':
        if not task:
            print("No tasks yet.")
        else:
            print("\nYour Task.")
            for i , t in enumerate(task, 1):
                status = "✅" if t["done"] else "❌"
                print(f"{i} {t['title']} {status}")
    
    #mark task as done
    
    elif choice == '3':
        if not task:
            print("No tasks to mark.")      
        else:
            print("\nYour Task")
            for i, t in enumerate(task, 1):
                status = "✅" if t["done"] else "❌"
                print(f"{i},{t['title']},{status}")

            try:
                index = int(input("Enter task number to mark as done: "))
                if  1 <= index <= len(task):
                    task[index -1]["done"] = True
                    save_tasks()
                    print("task marked as done ✅")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("please enter a valid number.")

    #delet a task

    elif choice == '4':
        if not task:
            print("No tasks to delete.")
        else:
             print("\nYour Tasks:")
             for i, t in enumerate(task, 1):
                 status = "✅" if t["done"] else "❌"
                 save_tasks()
                 print(f"{i}. {t['title']} {status}")

        try:
            index = int(input("Enter task number to delete: "))
            if 1 <= index <= len(task):
                removed = task.pop(index - 1)
                print(f"Task '{removed['title']}' deleted.🗑️")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

     #show done tasks

    elif choice == '5':
        print("\n✅Done Tasks: ")
        has_done = False
        for i , t in enumerate(task,1):
            if t["done"]:
                print(f"{i}.{t['title']}✅")
                has_done = True
        if not has_done:
            print("No done Tasks yet.")
    #show not done tasks
    elif choice == "6":
        print("\n❌ Not-Done Tasks:")
        has_not_done = False
        for i , t in enumerate(task, 1 ):
            if not t["done"]:
                print(f"{i}. {t['title']}❌")
                has_not_done = True
        
        if not has_not_done:
            print("All tasks are done!")

    #edit task

    elif choice == "7":
        if not task:
            print("No task to edit")
        else:
             print("\nYour tasks: ")
             for i , t in enumerate(task, 1):
                 status = "✅" if t["done"] else "❌"
                 print(f"{i},{t['title']},{status}")
             try:
              index = int(input("Enter task number to edit: "))
              if 1<= index <= len(task):
                  new_title = input("Enter new title: ")
                  old_title = task[index - 1]['title']
                  task[index - 1]['title'] = new_title
                  save_tasks()
                  print(f"Task '{old_title}' changed to '{new_title}' ✏️")
              else:
                  print("Invalid task number")
             except ValueError:
                 print("Please enter a valid number.")       

    #exit from app

    elif choice == '8':
        print("Goodby!")
        break

    else:
        print("Invalid Choice!.")     




  