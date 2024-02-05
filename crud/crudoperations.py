def add():
    todo = input("insert toDo item:") + "\n"
    file = open(f"./file/" + "todos.txt", 'r')

    todo_list = file.readlines()
    

    #We append the new "todo" item to the "todo_list"
    todo_list.append(todo)
    #We close the file
    
    #We re-open the file in 'w' mode (writing mode)
    with open(f"./file/" + "todos.txt", 'w') as file:
        #we write the "todo_list" line by line into the new file
        file.writelines(todo_list)