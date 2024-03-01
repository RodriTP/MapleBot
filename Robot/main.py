#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import BluetoothMailboxServer, TextMailbox
from drivebase import Drivebase
from sensors import Sensors
#from bluetooth import Bluetooth

ev3 = EV3Brick()
s = Sensors()

#b = Bluetooth()

d = Drivebase()
d._init_()

#TODO : TESTER GYRO
#       BLUETOOTH CONNECTION
#       ligne droite
#       Infrarouge code rodrigo
      
# Write your program here.
#ev3.speaker.beep()

#d.setSpeed(200)
#20.6  2 rotations
#9.745    1 rotation
#40.4  10 rotations
#d.turn(90, 100)
#d.turn(-180, 100)
d._kLeftMotor.run(-400)
d._kRightMotor.run(-400)
#d._kLeftMotor.runAngle(-200)
#d._kRightMotor.run(-200)

#self.setSpeed(-200)
while True:
    print(s.getFrontDistance())
    if(s.getFrontDistance()<35):
        d.stopMotors()
#while True:
#    d.turn(90, 100)
#    d.turn(-90, 100)
    #b.sendSensorData()
    #print(d._kGyro.angle())
    #d._kLeftMotor.run(200)
    #d._kRightMotor.run(-200)
    #if d._kLeftMotor.angle() >= 360*float(9.745):
    #d.stop()