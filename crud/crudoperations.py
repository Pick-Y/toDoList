FILEPATH = f"./file/" + "todos.txt"
def read_file():
     
     with open(FILEPATH, 'r') as file:
        list_of_item = file.readlines()
     
     return list_of_item

def write_file(alist):
     
      with open(FILEPATH, 'w') as file:
        #we write the "todo_list" line by line into the new file
        file.writelines(alist)

def read_list_index(alist):
     for index, i in enumerate(alist):
        numbered_item = f"{index + 1}:){i}"
        print(numbered_item)

def add(option):
    #todo = input("insert toDo item:") + "\n"
    
    todo_list = read_file()
    

    #We append the new "todo" item to the "todo_list"
    todo_list.append(option + "\n")
    #We close the file
    
    #We re-open the file in 'w' mode (writing mode)
    write_file(todo_list)

def show():
  
    list_of_item = read_file()
    
    new_item_list = [item.strip("\n") for item in list_of_item]
    
    read_list_index(new_item_list)
def edit():

    try:
       
        list_items = read_file()
                
        
        print("This is your current list:")
        show()
        number = int(input("Which item do you want to change?"))
        number = number - 1

        new_todo = input("Insert new to do item:\n ")
        list_items[number] = new_todo + "\n"
        print(list_items)

        write_file(list_items)
        
        print("This is your updated list:")
        show()
    except ValueError:
         print("Invalid value. Value must be an integer")

def complete():

    try:
        show()
        number = int(input("Which item do you want to remove?"))
        number = number - 1

        
        list_of_itmes = read_file()
        
        number_removed = list_of_itmes.pop(number)

        write_file(list_of_itmes)

        print("Removed " + str(number_removed))
    except IndexError:
         print("The index you have inserted is not contained in the list")