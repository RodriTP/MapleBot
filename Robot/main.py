#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
<<<<<<< HEAD
from pybricks.messaging import BluetoothMailboxServer, TextMailbox
=======
import math
>>>>>>> d69961f4cad1b70f3e1785e91f9e9d92ff1989fc
from drivebase import Drivebase
from sensors import Sensors
#from bluetooth import Bluetooth

ev3 = EV3Brick()
<<<<<<< HEAD
s = Sensors()

#b = Bluetooth()

d = Drivebase()
d._init_()

#TODO : TESTER GYRO
#       BLUETOOTH CONNECTION
#       ligne droite
#       Infrarouge code rodrigo
      
=======
d = Drivebase()
s = Sensors()
#d._init_()
#x : float = 0
#y : float = 0
#dist est le rapport de déplacement sur le temps utilisé pour le faire
#dist : float = 0

#pos = [x,y]

>>>>>>> d69961f4cad1b70f3e1785e91f9e9d92ff1989fc
# Write your program here.
#ev3.speaker.beep()

#d.setSpeed(200)
#20.6  2 rotations
#9.745 rotations = 102.616 cm   1 rotation
#40.4  10 rotations
#d.turn(90, 100)
#d.turn(-180, 100)
<<<<<<< HEAD
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
=======

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
>>>>>>> d69961f4cad1b70f3e1785e91f9e9d92ff1989fc
