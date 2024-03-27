FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of todo items.
    """
    with open(filepath, mode="r", encoding="utf-8") as file_read:
        todos_local = file_read.readlines()
    return todos_local


def write_todos(todos_list, filepath=FILEPATH):
    """
    Write a todo list to a text file.
    """
    with open(filepath, mode="w", encoding="utf-8") as file_write:
        file_write.writelines(todos_list)
