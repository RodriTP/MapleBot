#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import BluetoothMailboxServer, TextMailbox
import math
from Drivebase import Drivebase
from sensors import Sensors
from bluetooth import Bluetooth

ev3 = EV3Brick()
s = Sensors()


d = Drivebase()
      
b = Bluetooth()
# Write your program here.
#ev3.speaker.beep()
while True:
    b.sendPositionAndSensor(s, d)
    print("send")
#d.setSpeed(200)
#20.6  2 rotations
#9.745 rotations = 102.616 cm   1 rotation
#40.4  10 rotations
#d.turn(90, 100)
#d.turn(-180, 100)

#cette fonction reçoit dist : le rapport de déplacement sur un temps déterminé, et reçoit angle : la valeur que le gyro retourne.
def newPos(dist : float, angle : float):
    x = x + math.cos(Sensors.degrés() % 360) * dist, 
    y = y + math.sin(Sensors.degrés() % 360) * dist
    
#Cette fonction reçoit la distance en centimètres et retourne le nombre de degrés que les moteurs doivent tourner
def cmToAngleRot(dist : float): 
    return ((dist * 0.0949) * 360)

#def updateDist():
    

#x : float = obstacle_sensor.distance()

#while (True):
    #print(float(x))
    #print(d._kGyro.angle())
    #d._kLeftMotor.run(360)
    #d._kRightMotor.run(360)
    #if d._kLeftMotor.angle() >= cmToAngleRot(127):
        #d.stop()

def ligneDroite(speedLvl, distance):
    baseAngle = Sensors.degrés()
    baseSpeed = -speedLvl * 90
    while (True):
        print(str(round(Sensors.degrés() - baseAngle, 3)) + " Diff")
        print(str(baseAngle) + "  Base Angle")
        print(str(Sensors.degrés()) + "  Current")
        #baseAngle = baseAngle + 0.0007
        if Sensors.degrés() > baseAngle + 1: 
            d._kLeftMotor.run(baseSpeed - 5)
            d._kRightMotor.run(baseSpeed + 5)
            print("GOING LEFT (too much right)")
        elif Sensors.degrés() < baseAngle - 1:
            d._kLeftMotor.run(baseSpeed + 5)
            d._kRightMotor.run(baseSpeed - 5)
            print("GOING RIGHT (too much left)")
        else:
            d._kLeftMotor.run(baseSpeed)
            d._kRightMotor.run(baseSpeed)
            print("STRAIGHT")
        #if d._kLeftMotor.angle() >= cmToAngleRot(30):
            #d.stop()

def ligneDroiteSans(speedLvl, distance):
    baseSpeed = -speedLvl * 90
    while (True):
        d._kLeftMotor.run(baseSpeed)
        d._kRightMotor.run(baseSpeed)
        print

def testerGyro(x, y , z):
    #baseAngle = Sensors.degrés()
    while (True):
        print(Sensors.degrés())
    #     print(baseAngle)
        #print(x)
        # if Sensors.degrés() > baseAngle: 
        #     d._kLeftMotor.run(- 10 )
        #     d._kRightMotor.run(+ 10)
        # elif Sensors.degrés() < baseAngle:
        #     d._kLeftMotor.run(+ 10)
        #     d._kRightMotor.run(- 10)
        # x = x + 1
    # while (y < 50000):
    #     print(Sensors.degrés())
        #print(baseAngle)
        #print(y)
        # if y%10000 < 5000: 
        #     d._kLeftMotor.run(- 60 )
        #     d._kRightMotor.run(+ 60)
        # elif y%10000 > 5000:
        #     d._kLeftMotor.run(+ 60)
        #     d._kRightMotor.run(- 60)
        # y = y + 1
    

# while True:
#     degGyro = Sensors.degrés()
#     print(degGyro)


testerGyro(0,0,0)
#ligneDroite(3,0)
#ligneDroiteSans(3,0)
