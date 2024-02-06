import sys
sys.path.append('crud')
from crudoperations import add,show,edit, complete





while True:
    user_selection = input("Choose an option from the list:\n 1) add(to addan item)\n 2) show(to show todo_items in list)\n 4) edit (to edit item in the list)\n 5) complete (to remove an item from the list)\n 6) end (to exit program)\n")
    user_selection = user_selection.strip()

    if  user_selection.startswith("add"):
        add(user_selection[4:])
    elif user_selection.startswith("show"):
        show()
    elif user_selection.startswith("edit"):
        edit()
    elif user_selection.startswith("complete"):
        complete()
    elif user_selection.startswith("end"):
        break
    else:
        print("Invalid command")

# - add a new items to a list
# - show the content of a list
# - edit the content of a list
# - remove an item from the list when the task has been completed
