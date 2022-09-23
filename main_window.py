from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel
import threading
import logging

from save_send_network_tables import *


class MainWindow(QMainWindow):

    connected_to_network_table = False
    sending_climb_zeroes = False
    nt = None

    def __init__(self):
        super().__init__()
        self.button1 = QPushButton(self)
        self.button2 = QPushButton(self)
        self.label = QLabel(self)
        self.set_up_window()
        t1 = threading.Thread(target=self.establish_network_table_connection)
        t1.start()

    def set_up_window(self):
        width = 700
        height = 350
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
        self.label.setText("Awaiting Input")
        self.label.setFont(QFont("Ariel", 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setGeometry(150, 200, 400, 100)

    # TODO: Check that this works first
    def establish_network_table_connection(self):
        cond = threading.Condition()
        notified = [False]

        def connectionListener(connected, info):
            print(info, '; Connected=%s' % connected)
            with cond:
                notified[0] = True
                cond.notify()

        logging.basicConfig(level=logging.DEBUG)
        NetworkTables.startClientTeam(4829)
        NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

        with cond:
            print("Waiting")
            if not notified[0]:
                cond.wait()
                self.connected_to_network_table = False

        # This is reached once it is connected to the network table
        self.connected_to_network_table = True
        nt = NetworkTables.getTable("climbZerosTable")
        self.nt = nt
        print("Connected")

    def save_climb_zeroes(self):
        if self.nt is not None:
            self.label.setText("Connected")
            # This starts a thread that will run until climb values are saved
            t2 = threading.Thread(target=receive_climb_values, args=[self.nt])
            t2.start()
            self.button1.setStyleSheet("background-color: green")
        else:
            self.label.setText("Cannot establish connection")

    def send_button_clicked(self):
        if self.nt is not None:
            self.label.setText("Connected")
            self.sending_climb_zeroes = not self.sending_climb_zeroes
            if self.sending_climb_zeroes:
                self.button2.setText("Stop Sending")
                self.button1.setStyleSheet("")
                self.button1.setDisabled(True)
                t3 = threading.Thread(target=send_climb_values, args=[self.nt])
                t3.start()
            else:
                self.button2.setText("Send")
                self.button1.setEnabled(True)
        else:
            self.label.setText("Cannot establish connection")
