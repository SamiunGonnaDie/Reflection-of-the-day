# from functions import
import functions
import time
date = (time.strftime("%b %d, %Y %H:%M:%S"))
print("Today is", date)
while True:
    work = input("Type add, show, edit or exit:")
    work = work.strip()
    if work.startswith("add"):
        todo = work[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")
        functions.write_todos(todos)

    elif work.startswith("show"):

        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1} - {item}"
            print(row)


    elif work.startswith("edit"):
        try:
            number= int(work [5:])
            number = number - 1
            todos = functions.get_todos()
            new_one= input("Enter a new one:")
            todos[number] = new_one + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Invalid input")
            continue
    elif work.startswith("complete"):
        try:
             number = int(work [9:])
             todos = functions.get_todos()
             index = number - 1
             todo_to_remove = todos[index].strip("\n")
             todos.pop(index)
             functions.write_todos(todos)

             message = f'todo {todo_to_remove} is removed'
             print(message)
        except  IndexError:
            print("no todo exists with that number")
            continue

    elif "exit" in work:
        break
    else:
        print("Invalid input")
print("BYE")

