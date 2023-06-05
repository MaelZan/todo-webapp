import os

if not os.path.exists('To-Do.txt'):
    with open("To-Do.txt", 'w') as file:
        pass


FILEPATH = "To-Do.txt"


def get_todos(filepath=FILEPATH):  # Declares a function
    """Returns the items in the To-Do.txt file as a list"""
    with open(filepath) as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath=FILEPATH):
    """Writes the to-do items in the To-Do.txt file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_local)
