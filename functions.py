def get_todos(Filepath = "todos.txt"):
    """ Read the text file and return a list of the todos """
    with open(Filepath, "r") as file:
        todos = file.readlines()
    return todos

def write_todos(todos_arg , Filepath = "todos.txt"):
    """ Write the todos """
    with open(Filepath, "w") as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello World")
    print(get_todos())
