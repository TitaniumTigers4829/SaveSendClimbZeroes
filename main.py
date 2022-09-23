import sys

from PyQt6.QtWidgets import QApplication

from main_window import MainWindow
from networktables import NetworkTables

from save_send_network_tables import *

import logging

def main():
    logging.basicConfig(level=logging.DEBUG)
    NetworkTables.startClientTeam(4829)
    nt = NetworkTables.getTable("climbZerosTable")

    sleep(1)

    # app = QApplication(sys.argv)
    #
    # window = MainWindow()
    # window.show()
    #
    # app.exec()
    send_climb_values(nt)

    # receive_climb_values(nt)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
