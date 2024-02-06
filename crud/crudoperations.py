def add(option):
    #todo = input("insert toDo item:") + "\n"
    with open(f"./file/" + "todos.txt", 'r') as file:
        todo_list = file.readlines()
    

    #We append the new "todo" item to the "todo_list"
    todo_list.append(option + "\n")
    #We close the file
    
    #We re-open the file in 'w' mode (writing mode)
    with open(f"./file/" + "todos.txt", 'w') as file:
        #we write the "todo_list" line by line into the new file
        file.writelines(todo_list)

def show():
    with open(f"./file/" + "todos.txt", 'r') as file:
        list_of_item = file.readlines()
    
    new_item_list = [item.strip("\n") for item in list_of_item]
    
    for index, i in enumerate(new_item_list):
                #we want to enumerate list index starting from one and not 0
                #for a better UX
                numbered_item = f"{index + 1}:){i}"
                #Print the items present in the txt file
                print(numbered_item)
def edit():

    try:
        with open(f"./file/" + "todos.txt", 'r') as file:
                list_items = file.readlines()
                
        
        print("This is your current list:")
        show()
        number = int(input("Which item do you want to change?"))
        number = number - 1

        new_todo = input("Insert new to do item:\n ")
        list_items[number] = new_todo + "\n"
        print(list_items)

        with open(f"./file/" + "todos.txt", 'w') as file:
            file.writelines(list_items)
        
        print("This is your updated list:")
        show()
    except ValueError:
         print("Invalid value. Value must be an integer")
         
def complete():
    show()
    number = int(input("Which item do you want to remove?"))
    number = number - 1

    with open(f"./file/" + "todos.txt", 'r') as file:
        list_of_itmes = file.readlines()
    
    number_removed = list_of_itmes.pop(number)

    with open(f"./file/" + "todos.txt", 'w') as file:
        file.writelines(list_of_itmes)

    print("Removed " + str(number_removed))