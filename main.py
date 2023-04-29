from PySide6.QtWidgets import QApplication
from app import MainWindow
import sys

app = QApplication(sys.argv)

window = MainWindow(app)
window.setMinimumSize(400, 300)
window.setWindowTitle('Lewis County town info')

window.show()

app.exec()
