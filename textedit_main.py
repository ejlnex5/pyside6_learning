from PySide6.QtWidgets import QApplication
from text_edit import Widget

import sys
app = QApplication(sys.argv)

window = Widget()
window.show()

app.exec()