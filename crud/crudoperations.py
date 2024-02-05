def add():
    todo = input("insert toDo item:") + "\n"
    with open(f"./file/" + "todos.txt", 'r') as file:
        todo_list = file.readlines()
    

    #We append the new "todo" item to the "todo_list"
    todo_list.append(todo)
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