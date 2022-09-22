import time
from networktables import NetworkTables

import logging

logging.basicConfig(level=logging.DEBUG)

NetworkTables.startClientTeam(4829)
sd = NetworkTables.getTable("climbZerosTable")

while True:
    value = sd.getNumber("leftClimbHookHeight", -1)
    print(value)
    time.sleep(1)

# i = 0
# while True:
#     robotTime = sd.getNumber("dsTime", -1)
#     print("dsTime:", robotTime)
#
#     sd.putNumber("robotTime", i)
#     time.sleep(1)
#     i += 1

