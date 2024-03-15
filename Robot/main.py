#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import math
from drivebase import Drivebase
from sensors import Sensors

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
d = Drivebase()
s = Sensors()
#d._init_()
#x : float = 0
#y : float = 0
#dist est le rapport de déplacement sur le temps utilisé pour le faire
#dist : float = 0

#pos = [x,y]

# Write your program here.
#ev3.speaker.beep()

#d.setSpeed(200)
#20.6  2 rotations
#9.745 rotations = 102.616 cm   1 rotation
#40.4  10 rotations
#d.turn(90, 100)
#d.turn(-180, 100)

#cette fonction reçoit dist : le rapport de déplacement sur un temps déterminé, et reçoit angle : la valeur que le gyro retourne.
def newPos(dist : float, angle : float):
    x = x + math.cos(s.degrés()) * dist, 
    y = y + math.sin(s.degrés()) * dist
    
#Cette fonction reçoit la distance en centimètres et retourne le nombre de degrés que les moteurs doivent tourner
def cmToAngleRot(dist : float): 
    return ((dist * 0.0949) * 360)

#pour bouger vers la droite, utilisz un angle positif sinon négatif
# def tourneXDegres(deg, speedLvl):
#     baseSpeed = speedLvl * 90
#     angleVoulu = (s.degrés() + deg)%360 
#     if deg > 0:
#         while(s.degrés() <= angleVoulu):
#             d._kLeftMotor.run(-baseSpeed)
#             d._kRightMotor.run(baseSpeed)
#             print(s.degrés())
#     elif deg < 0:
#         while(s.degrés() <= angleVoulu ):
#             d._kLeftMotor.run(baseSpeed)
#             d._kRightMotor.run(-baseSpeed)
#             print(s.degrés())
#     d.stopMotors()

def tourneXDegres(deg, speedLvl):
    baseSpeed = speedLvl * 45
    #SIKE = str(s.degrés()) 
    angleVoulu = float(((s.degrés() + deg)%360))
    
    #print("cur : " + str(s.degrés()) + " ; Voulu " + str(angleVoulu) + " :deg " + str(deg))
    turn = True 
    if angleVoulu < s.degrés() and deg > 0 and turn :
        print("i tried")
        if angleVoulu > speedLvl * 10: 
            while(angleVoulu < s.degrés()):
                d._kLeftMotor.run(-baseSpeed)
                d._kRightMotor.run(baseSpeed)
                print(str(s.degrés()) + " : 1-0")
            while(angleVoulu > s.degrés() + 10*speedLvl):
                d._kLeftMotor.run(-baseSpeed)
                d._kRightMotor.run(baseSpeed)
                print(str(s.degrés()) + " : 1-1")
            while angleVoulu > s.degrés() + 1*speedLvl:
                d._kLeftMotor.run(-baseSpeed/8*speedLvl)
                d._kRightMotor.run(baseSpeed/8*speedLvl)
                print("derniers 1: " + str(s.degrés()))
            print(str(s.degrés()- angleVoulu))
        if angleVoulu <= speedLvl * 10:
            while(s.degrés() <= 360 - speedLvl* 10 + angleVoulu):
                d._kLeftMotor.run(-baseSpeed)
                d._kRightMotor.run(baseSpeed)
                print(str(s.degrés()) + " : 1-2")
            while(s.degrés() >= 360 - speedLvl* 10 + angleVoulu):
                d._kLeftMotor.run(-baseSpeed/8*speedLvl)
                d._kRightMotor.run(baseSpeed/8*speedLvl)
                print(str(s.degrés()) + " : 1-3")
            while angleVoulu > s.degrés() + 1*speedLvl:
                d._kLeftMotor.run(-baseSpeed/8*speedLvl)
                d._kRightMotor.run(baseSpeed/8*speedLvl)
                print("derniers 1: " + str(s.degrés()))
            print(str(s.degrés()- angleVoulu))
        turn = False
    if angleVoulu < s.degrés() and deg < 0 and turn:
        while(angleVoulu < s.degrés() - 10*speedLvl):
            d._kLeftMotor.run(baseSpeed)
            d._kRightMotor.run(-baseSpeed)
            print(str(s.degrés()) + " : 2")
        while angleVoulu < s.degrés() - 1*speedLvl:
            d._kLeftMotor.run(baseSpeed/8*speedLvl)
            d._kRightMotor.run(-baseSpeed/8*speedLvl)
            print("derniers 2: " + str(s.degrés()))
        print(str(s.degrés()- angleVoulu))
        turn = False



    if angleVoulu > s.degrés()  and deg > 0 and turn:
        print("degrés voulu : " + str(angleVoulu))
        while(angleVoulu > s.degrés() + 10*speedLvl):
            d._kLeftMotor.run(-baseSpeed)
            d._kRightMotor.run(baseSpeed)
            print(str(s.degrés()) + " : 3")
        while angleVoulu > s.degrés() + 1*speedLvl:
            d._kLeftMotor.run(-baseSpeed/8*speedLvl)
            d._kRightMotor.run(baseSpeed/8*speedLvl)
            print("derniers 3: " + str(s.degrés()))
        print(str(s.degrés()- angleVoulu))
        turn = False
        
    if angleVoulu > s.degrés() and deg < 0 and turn :
        if angleVoulu < 360 - speedLvl * 10: 
            while(angleVoulu > s.degrés()):
                d._kLeftMotor.run(baseSpeed)
                d._kRightMotor.run(-baseSpeed)
                print(str(s.degrés()) + " : 4-0")
            while(angleVoulu < s.degrés() - 10*speedLvl):
                d._kLeftMotor.run(baseSpeed)
                d._kRightMotor.run(-baseSpeed)
                print(str(s.degrés()) + " : 4-1")
            while angleVoulu < s.degrés() - 1*speedLvl:
                d._kLeftMotor.run(baseSpeed/8*speedLvl)
                d._kRightMotor.run(-baseSpeed/8*speedLvl)
                print("derniers 1: " + str(s.degrés()))
            print(str(s.degrés()- angleVoulu))
        if angleVoulu > 360 - speedLvl * 10:
            while(s.degrés() >= speedLvl* 10 + angleVoulu - 360):
                d._kLeftMotor.run(baseSpeed)
                d._kRightMotor.run(-baseSpeed)
                print(str(s.degrés()) + " : 4-2")
            while(s.degrés() <= speedLvl* 10 + angleVoulu - 360):
                d._kLeftMotor.run(baseSpeed/8*speedLvl)
                d._kRightMotor.run(-baseSpeed/8*speedLvl)
                print(str(s.degrés()) + " : 4-3")
            while angleVoulu < s.degrés() + 1*speedLvl:
                d._kLeftMotor.run(baseSpeed/8*speedLvl)
                d._kRightMotor.run(-baseSpeed/8*speedLvl)
                print("derniers 1: " + str(s.degrés()))
            print(str(s.degrés()- angleVoulu))
        turn = False


    # if angleVoulu > s.degrés()  and deg < 0 and turn:
    #     while(angleVoulu > s.degrés() - 10*speedLvl):
    #         d._kLeftMotor.run(baseSpeed)
    #         d._kRightMotor.run(-baseSpeed)
    #         print(str(s.degrés()) + " : 4")
    #     while angleVoulu > s.degrés() - 1*speedLvl:
    #         d._kLeftMotor.run(baseSpeed/8*speedLvl)
    #         d._kRightMotor.run(-baseSpeed/8*speedLvl)
    #         print(str(angleVoulu) + "derniers 4: " + str(s.degrés()))
    #         print(str(s.degrés()- angleVoulu))
    #     turn = False
    print("stop : " + str(s.degrés()) + " voici l'angle de fin " + "voici angle voulu : " + str(angleVoulu))
    print(str(s.degrés()- angleVoulu))
    d.stopMotors()



def fwofe(deg, speedLvl):
 angleVoulu = 2
 baseSpeed = 2
 if angleVoulu > s.degrés() and deg < 0 and turn :
        if angleVoulu < 360 - speedLvl * 10: 
            while(angleVoulu > s.degrés()):
                d._kLeftMotor.run(baseSpeed)
                d._kRightMotor.run(-baseSpeed)
                print(str(s.degrés()) + " : 4-0")
            while(angleVoulu < s.degrés() - 10*speedLvl):
                d._kLeftMotor.run(baseSpeed)
                d._kRightMotor.run(-baseSpeed)
                print(str(s.degrés()) + " : 4-1")
            while angleVoulu < s.degrés() - 1*speedLvl:
                d._kLeftMotor.run(baseSpeed/8*speedLvl)
                d._kRightMotor.run(-baseSpeed/8*speedLvl)
                print("derniers 1: " + str(s.degrés()))
            print(str(s.degrés()- angleVoulu))
        if angleVoulu > 360 - speedLvl * 10:
            while(s.degrés() >= speedLvl* 10 + angleVoulu - 360):
                d._kLeftMotor.run(baseSpeed)
                d._kRightMotor.run(-baseSpeed)
                print(str(s.degrés()) + " : 4-2")
            while(s.degrés() <= speedLvl* 10 + angleVoulu - 360):
                d._kLeftMotor.run(baseSpeed/8*speedLvl)
                d._kRightMotor.run(-baseSpeed/8*speedLvl)
                print(str(s.degrés()) + " : 4-3")
            while angleVoulu < s.degrés() + 1*speedLvl:
                d._kLeftMotor.run(baseSpeed/8*speedLvl)
                d._kRightMotor.run(-baseSpeed/8*speedLvl)
                print("derniers 1: " + str(s.degrés()))
            print(str(s.degrés()- angleVoulu))
        turn = False
 


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
    baseAngle = s.degrés()
    baseSpeed = -speedLvl * 90
    while (True):
        print(str(round(s.degrés() - baseAngle, 3)) + " Diff")
        print(str(baseAngle) + "  Base Angle")
        print(str(s.degrés()) + "  Current")
        #baseAngle = baseAngle + 0.0007
        if s.degrés() > baseAngle + 1: 
            d._kLeftMotor.run(baseSpeed - 5)
            d._kRightMotor.run(baseSpeed + 5)
            print("GOING LEFT (too much right)")
        elif s.degrés() < baseAngle - 1:
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
        d._kRightMotor.run(-baseSpeed)
        print(s.degrés())
        

def testerGyro(x, y , z):
    #baseAngle = s.degrés()
    while (True):
        print(s.degrés())
    #     print(baseAngle)
        #print(x)
        # if s.degrés() > baseAngle: 
        #     d._kLeftMotor.run(- 10 )
        #     d._kRightMotor.run(+ 10)
        # elif s.degrés() < baseAngle:
        #     d._kLeftMotor.run(+ 10)
        #     d._kRightMotor.run(- 10)
        # x = x + 1
    # while (y < 50000):
    #     print(s.degrés())
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
#     degGyro = s.degrés()
#     print(degGyro)


#testerGyro(0,0,0)
#ligneDroite(3,0)
#ligneDroiteSans(3,0)
tourneXDegres(190,2)
tourneXDegres(190,1)

