# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    # Get input from use and strip space characters from it
    user_action = input("Enter add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        # new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = functions.get_todos()

            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Your command is invalid.")
            continue

    elif user_action.startswith("complete"):
        try:
            completed_number = int(user_action[9:])
            index = (completed_number - 1)

            todos = functions.get_todos()

            removed = todos[index].strip("\n")
            new_list = todos.pop(completed_number - 1)

            functions.write_todos(todos)
            print(f"Todo '{removed}' is completed and removed")
        except IndexError:
            print("There is item with that number.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("The command is invalid")

print("BYE!")
