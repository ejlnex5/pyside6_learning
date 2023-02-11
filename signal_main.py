#Version 1
"""
from PySide6.QtWidgets import QApplication, QPushButton

def button_clicked():
    print("You clicked the button, didn't you!")

app = QApplication()
button = QPushButton("Press ME")

button.clicked.connect(button_clicked)

button.show()
app.exec()
"""

#Version 2: Signals Sending Values, Capture Values
"""from PySide6.QtWidgets import QApplication, QPushButton

def button_clicked(data):
    print("You clicked the button, didn't you! checked : ", data)

app = QApplication()
button = QPushButton("Press ME")
button.setCheckable(True) #Makes button checkable. Clicks toggle between TRUE/FALSE

button.clicked.connect(button_clicked)

button.show()
app.exec()
"""
#VERSION 3
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider

def respond_to_slider(data):
    print("Slider moved to : ", data)

app = QApplication()
slider = QSlider(Qt.Orientation.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

#Create the connection
slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()
