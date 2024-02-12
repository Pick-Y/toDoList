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