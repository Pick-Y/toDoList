import sys
#sys.path.append('crud')
#from crudoperations import add,show,edit, complete
from datetime import date, datetime
from PyQt6.QtWidgets import QApplication
from gui import TodoListApp

app = QApplication(sys.argv)
new_todo_list = TodoListApp()

if __name__ == '__main__':
    
    window = TodoListApp()
    window.show()
    sys.exit(app.exec())
