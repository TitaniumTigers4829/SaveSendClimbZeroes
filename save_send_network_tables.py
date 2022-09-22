from networktables import NetworkTables
import time


def receive_climb_values(nt):
    left_climb_zero = nt.getNumber("leftClimbHookHeight", -1)
    right_climb_zero = nt.getNumber("rightClimbHookHeight", -1)
    print(f"left {left_climb_zero}")
    print(f"right {right_climb_zero}")
    time.sleep(3)


def send_climb_values(nt):
    nt.putNumber("leftClimbHookZero", 3686)
    time.sleep(3)

