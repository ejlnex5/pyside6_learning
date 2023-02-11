from PySide6.QtWidgets import QRadioButton, QButtonGroup, QCheckBox, QGroupBox, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QSizePolicy, QGridLayout

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QCheckbox and QRadioButton")

        #checkboxes : OS
        os = QGroupBox("Choose Operating System")
        windows = QCheckBox("Windows")
        windows.toggled.connect(self.windows_box_toggled)

        linux = QCheckBox("Linux")
        linux.toggled.connect(self.linux_box_toggled)

        mac = QCheckBox("Mac")
        mac.toggled.connect(self.mac_box_toggled)
        os_layout = QVBoxLayout()
        os_layout.addWidget(windows)
        os_layout.addWidget(linux)
        os_layout.addWidget(mac)
        os.setLayout(os_layout)

        drinks = QGroupBox("Drink Selection")
        beer = QCheckBox("Beer")
        juice = QCheckBox("Juice")
        coffee = QCheckBox("Coffee")

        #Make the checkboxes exclusive
        exclusive_button_group = QButtonGroup(self)#A parent parameter is required
        exclusive_button_group.addButton(beer)
        exclusive_button_group.addButton(juice)
        exclusive_button_group.addButton(coffee)
        exclusive_button_group.setExclusive(True)

        drink_layout = QVBoxLayout()
        drink_layout.addWidget(beer)
        drink_layout.addWidget(juice)
        drink_layout.addWidget(coffee)
        drinks.setLayout(drink_layout)

        answers = QGroupBox("Choose Answer")
        answer_a = QRadioButton("A")
        answer_b = QRadioButton("B")
        answer_c = QRadioButton("C")
        answer_a.setChecked(True)

        answers_layout = QVBoxLayout()
        answers_layout.addWidget(answer_a)
        answers_layout.addWidget(answer_b)
        answers_layout.addWidget(answer_c)
        answers.setLayout(answers_layout)

        h_layout = QHBoxLayout()
        h_layout.addWidget(os)
        h_layout.addWidget(drinks)
  
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(answers)

        self.setLayout(v_layout)

    def windows_box_toggled(self, checked):
        if (checked):
            print("Windows checked")
        else:
            print("Windows box unchecked")

    def linux_box_toggled(self, checked):
        if (checked):
            print("Mac checked")
        else:
            print("Mac box unchecked")

    def mac_box_toggled(self, checked):
        if (checked):
            print("Windows checked")
        else:
            print("Windows box unchecked")


        """button_1 = QPushButton("One")
        button_2 = QPushButton("Two")
        button_3 = QPushButton("Three")
        button_3.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        button_4 = QPushButton("Four")
        button_5 = QPushButton("Five")
        button_6 = QPushButton("Six")
        button_7 = QPushButton("Seven")

        grid_layout = QGridLayout()
        grid_layout.addWidget(button_1,0,0)
        grid_layout.addWidget(button_2,0,1,1,2)#Take up 1 row and 2 columns
        grid_layout.addWidget(button_3,1,0,2,1)#Take up 2 rows and 1 column
        grid_layout.addWidget(button_4,1,1,)
        grid_layout.addWidget(button_5,1,2)
        grid_layout.addWidget(button_6,2,1)
        grid_layout.addWidget(button_7,2,2)


        self.setLayout(grid_layout)"""