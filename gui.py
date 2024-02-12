import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLineEdit, QPushButton, QMessageBox,QLabel,QDialog



class TodoListApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.path = "todos.txt"
        self.list_of_items = self.read_file()
    
    def initUI(self):
        self.setWindowTitle('Todo List')
        self.setGeometry(100, 100, 400, 300)
        
        # Create main layout
        main_layout = QVBoxLayout()

        # Create input layout
        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        add_button = QPushButton('Add')
        add_button.clicked.connect(self.add_item)
        input_layout.addWidget(self.input_field)
        input_layout.addWidget(add_button)

        # Create buttons layout
        buttons_layout = QHBoxLayout()
        show_button = QPushButton('Show All')
        show_button.clicked.connect(self.show_all_items)
        edit_button = QPushButton('Edit')
        edit_button.clicked.connect(self.edit_item)
        delete_button = QPushButton('Delete')
        delete_button.clicked.connect(self.delete_item)
        buttons_layout.addWidget(show_button)
        buttons_layout.addWidget(edit_button)
        buttons_layout.addWidget(delete_button)

        # Create list widget
        self.list_widget = QListWidget()

        # Add layouts to the main layout
        main_layout.addLayout(input_layout)
        main_layout.addLayout(buttons_layout)
        main_layout.addWidget(self.list_widget)

        self.setLayout(main_layout)
    
    #reads file from text file
    def read_file(self):
     
     with open(self.path, 'r') as file:
        list_of_item = file.readlines()
     
     return list_of_item
    
    #write into the  text file
    def write_file(self,alist):
     
      with open(self.path, 'w') as file:
        #we write the "todo_list" line by line into the new file
        file.writelines(alist)
    
    def add_item(self):
        text = self.input_field.text()

        if text:
            self.list_of_items.append(text + "\n")
            self.write_file(self.list_of_items)

            self.list_widget.addItem(text)
            self.input_field.clear()
    
    def show_all_items(self):

        new_item_list = [item.strip("\n") for item in self.list_of_items]
        for item in new_item_list:
            self.list_widget.addItem(item)

        count = self.list_widget.count()
        if count == 0:
           
            QMessageBox.information(self, 'Todo List', 'No items in the list.')
        else:
            items = [self.list_widget.item(i).text() for i in range(count)]
            #QMessageBox.information(self, 'Todo List', '\n'.join(items))