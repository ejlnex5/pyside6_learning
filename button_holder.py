from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button App")
        button = QPushButton("Press Me")

        #Set up the button as our central widget
        self.setCentralWidget(button)