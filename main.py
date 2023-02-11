#VERSION 1
"""
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton

import sys
app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("App Name")

button = QPushButton()
button.setText("Press Me")

window.setCentralWidget(button)

window.show()
app.exec()
"""

#VERSION 2 : Separate Class
"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button App")
        button = QPushButton("Press Me")

        #Set up the button as our central widget
        self.setCentralWidget(button)

app = QApplication(sys.argv)

window = ButtonHolder()
window.show()
app.exec
"""

#Version 3
import sys
from PySide6.QtWidgets import QApplication
from button_holder import ButtonHolder
app = QApplication(sys.argv)

window = ButtonHolder()
window.show()
app.exec()