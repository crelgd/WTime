from PyQt5 import QtWidgets, QtCore
from ui import *
from Core import Time
import sys

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_WTime()
        self.ui.setupUi(self)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.timer_finished)

        self.ui.pushButton.clicked.connect(self.start)

    def start(self):
        self.fieldMin = int(self.ui.lineEdit.text())
        min = Time(self.fieldMin, 0)
        self.timer.start(min.minToSec() * 1000)

    def timer_finished(self):
        self.timer.stop()
        self.message_window = QtWidgets.QMainWindow()
        self.message_ui = Ui_MainWindow()
        self.message_ui.setupUi(self.message_window)
        self.message_window.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.message_ui.label.setText(f"Ваш таймер на {str(self.fieldMin)}минут был завершен!")
        self.message_ui.pushButton.clicked.connect(self.message_window.close)
        self.message_window.show()

app = QtWidgets.QApplication([])
application = Main()
application.show()

sys.exit(app.exec())