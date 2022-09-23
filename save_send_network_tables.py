from time import sleep

from _pynetworktables import *

from read_write_climb_zeroes import *

# Constants for the names of network table entries
RECEIVE_LEFT_NAME = "leftClimbHookHeight"
RECEIVE_RIGHT_NAME = "rightClimbHookHeight"
SEND_LEFT_NAME = "leftClimbHookZero"
SEND_RIGHT_NAME = "rightClimbHookZero"
SEND_CONFIRMATION_NAME = "zeroesReceivedSuccessfully"


def receive_climb_values(nt: NetworkTable) -> bool:
    """
    Handles receiving the climb zeroes from the robot.
    :param nt: The network table created from the .getTable method.
    :return: True if the values were successfully received, False if not.
    """
    # Gets the climb zeroes from the network table
    left_climb_zero = nt.getNumber(RECEIVE_LEFT_NAME, -1)
    right_climb_zero = nt.getNumber(RECEIVE_RIGHT_NAME, -1)
    sleep(3)
    if left_climb_zero != -1 and right_climb_zero != -1:
        # Saves the climb zeroes in a text file
        write_climb_values(str(left_climb_zero), str(right_climb_zero))
        return True
    else:
        return False


def send_climb_values(nt: NetworkTable):
    """
    Handles sending the saved climb zeroes to the robot.
    :param nt: The network table created from the .getTable method.
    :return:
    """
    # Gets the saved zeroes from the text file
    left_hook_zero, right_hook_zero = read_climb_values()
    # Puts the saved zeroes in the network table
    nt.putNumber(SEND_LEFT_NAME, float(left_hook_zero))
    nt.putNumber(SEND_RIGHT_NAME, float(right_hook_zero))
    sleep(3)


def verify_values_were_sent(nt: NetworkTable) -> bool:
    """
    This function uses another network table entry to verify that the robot received the sent zeroes.
    :param nt: The network table created from the .getTable method.
    :return: True if the robot successfully received the zeroes, False if not.
    """
    # Gets the climb zeroes from the network table
    send_confirmation = nt.getBoolean(SEND_CONFIRMATION_NAME, False)
    sleep(3)
    return send_confirmation
