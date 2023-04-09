def get_todos(file_path = "todo.txt"):
    """ Read a text file and return a
    list of tp-do items.
    """
    with open(file_path, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_arg, file_path = "todo.txt"):
    """ Write the to-do items list in the text
    file.
    """
    with open(file_path, 'w') as file:
        file.writelines(todos_arg)

def count(phrase):
    return phrase.count('.')

if __name__ == "__main__":
    print(get_todos())