import sys
sys.path.append('crud')
from crudoperations import add,show,edit, complete





while True:
    user_selection = input("Choose an option from the list:\n 1) add(to addan item)\n 2) show(to show todo_items in list)\n 4) edit (to edit item in the list)\n 5) complete (to remove an item from the list)\n 6) end (to exit program)\n")

    match user_selection.strip():
        case "add":
            add()
        case "show":
            show()
        case "edit":
            edit()
        case "complete":
            complete()

# - add a new items to a list
# - show the content of a list
# - edit the content of a list
# - remove an item from the list when the task has been completed
