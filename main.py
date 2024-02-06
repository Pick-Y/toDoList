import sys
sys.path.append('crud')
from crudoperations import add,show,edit, complete





while True:
    user_selection = input("Choose an option from the list:\n 1) add(to addan item)\n 2) show(to show todo_items in list)\n 4) edit (to edit item in the list)\n 5) complete (to remove an item from the list)\n 6) end (to exit program)\n")
    user_selection = user_selection.strip()
    if "add" in user_selection:
        add(user_selection[4:])
    elif "show" in user_selection.strip():
        show()
    elif "edit" in user_selection.strip():
        edit()
    elif "complete" in user_selection.strip():
        complete()
    else:
        break

# - add a new items to a list
# - show the content of a list
# - edit the content of a list
# - remove an item from the list when the task has been completed
