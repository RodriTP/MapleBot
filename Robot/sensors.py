#!/usr/bin/env pybricks-micropython
import utime
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
#import adafruit_bno055, board
from pybricks.hubs import EV3Brick
from pybricks.iodevices import I2CDevice
from bno055 import *

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
c='a'
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

  
class Sensors :
    _leftUltrasonic = UltrasonicSensor(Port.S1)
    _frontInfrared = InfraredSensor(Port.S3)
    _rightUltrasonic = UltrasonicSensor(Port.S4)
    _isObstacleRight = False
    _isObstacleLeft = False
    _gyroOffset = None
    #sys, gyro,accel, mag
    def degrés(self):
        line = []
        gay = True
        while gay == True: 
            for c in ser.read(1):
                if (chr(c) != '\n') and (chr(c) != '\r'):
                    line.append(chr(c))
                if chr(c) == '\n':
                    strline=''.join(str(v) for v in line) 
                    #print(float(strline))
                    line = []
                    gay = False
                    if self._gyroOffset == None:
                        self._gyroOffset = float(strline)
                        return self._gyroOffset
                    else :
                        return (float(strline)-self._gyroOffset)%float(360)
    
    _DISTANCE_FROM_OBSTACLE = float(200.0)

    def update(self):
        if(self.getLeftDistance() < self._DISTANCE_FROM_OBSTACLE):
            self._isObstacleLeft  = True
        if(self.getRightDistance() < self._DISTANCE_FROM_OBSTACLE):
            self._isObstacleRight = True
        else:
            self._isObstacleLeft = False
            self._isObstacleRight = False

    def getLeftDistance(self):
        return float(self._leftUltrasonic.distance()) #mm  
    
    def getRightDistance(self):
        return float(self._rightUltrasonic.distance()) #mm
    
    def getFrontValue(self):
        return float(self._frontInfrared.distance()) #retourne une val entre 0 et 100 (faut multiplier par un scalaire)
    
    def getIsObstacleLeft(self):
        return bool(self._isObstacleLeft)
    
    def getIsObstacleRight(self):
        return bool(self._isObstacleRight)
    #self.device.read(reg = 0x0F, length=1)