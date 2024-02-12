import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLineEdit, QPushButton, QMessageBox,QLabel,QDialog



class TodoListApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.path = "todos.txt"
        self.list_of_items = self.read_file()