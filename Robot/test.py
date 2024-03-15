#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Port, Color, Button, Direction, Stop
from pybricks.iodevices import DCMotor, UARTDevice, LUMPDevice, I2CDevice

from pybricks.hubs import EV3Brick
from pybricks.iodevices import UARTDevice
from pybricks.parameters import Port
from pybricks.media.ev3dev import SoundFile
import time

# Initialize the EV3
ev3 = EV3Brick()

# Initialize sensor port 2 as a uart device
# https://pybricks.com/ev3-micropython/iodevices.html#uart-device
#  class UARTDevice(port, baudrate, timeout=None(ms))
ser = UARTDevice(Port.S2, baudrate=9600, timeout=None)
line = []
# Write some data
#ser.write(b'\r\nHello, world!\r\n')

# Play a sound while we wait for some data
# for i in range(3):
# #    ev3.speaker.play_file(SoundFile.HELLO)
# #    ev3.speaker.play_file(SoundFile.GOOD)
# #    ev3.speaker.play_file(SoundFile.MORNING)
#     print("Bytes waiting to be read:", ser.waiting())

# Read all data received while the sound was playing
# while True:
#     # data = ser.read_all()

# # read until we see the "newLine" character and print the line
#     for c in ser.read(1):
#         if (chr(c) != '\n') and (chr(c) != '\r'):
#             line.append(chr(c))
#         if chr(c) == '\n':
#             strline=''.join(str(v) for v in line)
#             # print(''.join(str(v) for v in line))
#             # print(line)
            
#             heading = float(strline)
#             print(heading)
#             # print(heading + 400)
#             line = []
#             break    
#     # print(c)        

def degrés():
    line = []
    gay = True
    while gay == True: 
        for c in ser.read(1):
            if (chr(c) != '\n') and (chr(c) != '\r'):
                line.append(chr(c))
            if chr(c) == '\n':
                strline=''.join(str(v) for v in line)
                # print(''.join(str(v) for v in line))
                #print(line)
                rep = float(strline) 
                print(rep)
                line = []
                gay = False
                return rep

              

degrés()