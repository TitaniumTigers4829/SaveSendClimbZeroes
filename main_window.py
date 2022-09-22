from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import QMainWindow, QPushButton

from read_write_climb_zeroes import *
from save_send_network_tables import *

class MainWindow(QMainWindow):

    sending_climb_zeroes = False

    def __init__(self):
        super().__init__()
        self.button1 = QPushButton(self)
        self.button2 = QPushButton(self)
        self.set_up_window()

    def set_up_window(self):
        width = 700
        height = 300
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        self.setWindowTitle("Climb Zeroes Manager")
        self.setWindowIcon(QIcon("4829logo.png"))
        self.button1.setText("Save")
        self.button1.setFont(QFont("Ariel", 20))
        self.button1.setGeometry(100, 100, 200, 100)
        self.button1.clicked.connect(self.save_climb_zeroes)
        self.button2.setText("Send")
        self.button2.setFont(QFont("Ariel", 20))
        self.button2.setGeometry(400, 100, 200, 100)
        self.button2.clicked.connect(self.send_button_clicked)

    def save_climb_zeroes(self):
        # TODO: Code for getting them from network tables
        receive_climb_values()
        successful = True
        if successful:
            self.button1.setStyleSheet("background-color: green")
        write_climb_values("1", "2342")
        
    def send_button_clicked(self):
        self.sending_climb_zeroes = not self.sending_climb_zeroes
        if self.sending_climb_zeroes:
            self.button2.setText("Stop Sending")
            self.button1.setStyleSheet("")
            self.button1.setDisabled(True)
            # TODO: code for setting values through network tables
            left_hook_zero, right_hook_zero = read_climb_values()
            print(left_hook_zero)
            print(right_hook_zero)

        else:
            self.button2.setText("Send")
            self.button1.setEnabled(True)
