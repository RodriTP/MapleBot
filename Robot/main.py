#!/usr/bin/env pybricks-micropython
import pybricks
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
# from pybricks.parameters import Port, Stop, Direction, Button, Color
# from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
# from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.tools import StopWatch, DataLog
import math
from Drivebase import Drivebase
from sensors import Sensors
import time

from threading import Thread
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
d = Drivebase()
s = Sensors()
indiceDeCorrection = 0
x = 0
y = 0
pos = [x,y]
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
def newPos(dist, angle, x, y):
    X = x + math.cos(angle) * dist 
    Y = y + math.sin(angle) * dist
    return [X,Y]
    
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

# def tournerXDegres(deg, speedLvl, indiceDeCorrection):
#     baseSpeed = speedLvl * 45
#     #angleVoulu = float(((s.degrés() + deg)%360))
#     angleVoulu = float(((indiceDeCorrection + deg)%360))
#     #print("cur : " + str(s.degrés()) + " ; Voulu " + str(angleVoulu) + " :deg " + str(deg))
#     turn = True 

#     if angleVoulu < s.degrés() and deg > 0 and turn :
#         print("i tried")
#         if angleVoulu > speedLvl * 10: 
#             while(angleVoulu < s.degrés()):
#                 d._kLeftMotor.run(-baseSpeed)
#                 d._kRightMotor.run(baseSpeed)
#                 print(str(s.degrés()) + " : 1-0")
#             while(angleVoulu > s.degrés() + 10*speedLvl):
#                 d._kLeftMotor.run(-baseSpeed)
#                 d._kRightMotor.run(baseSpeed)
#                 print(str(s.degrés()) + " : 1-1")
#             while angleVoulu > s.degrés() + 1*speedLvl:
#                 d._kLeftMotor.run(-baseSpeed/(8*speedLvl))
#                 d._kRightMotor.run(baseSpeed/(8*speedLvl))
#                 print("derniers 1: " + str(s.degrés()))
#             print(str(s.degrés()- angleVoulu))
#         if angleVoulu <= speedLvl * 10:
#             while(s.degrés() <= 360 - speedLvl* 10 + angleVoulu):
#                 d._kLeftMotor.run(-baseSpeed)
#                 d._kRightMotor.run(baseSpeed)
#                 print(str(s.degrés()) + " : 1-2")
#             while(s.degrés() >= 360 - speedLvl* 10 + angleVoulu):
#                 d._kLeftMotor.run(-baseSpeed/(8*speedLvl))
#                 d._kRightMotor.run(baseSpeed/(8*speedLvl))
#                 print(str(s.degrés()) + " : 1-3")
#             while angleVoulu > s.degrés() + 1*speedLvl:
#                 d._kLeftMotor.run(-baseSpeed/(8*speedLvl))
#                 d._kRightMotor.run(baseSpeed/(8*speedLvl))
#                 print("derniers 1: " + str(s.degrés()))
#             print(str(s.degrés()- angleVoulu))
#         turn = False
#     if angleVoulu < s.degrés() and deg < 0 and turn:
#         while(angleVoulu < s.degrés() - 10*speedLvl):
#             d._kLeftMotor.run(baseSpeed)
#             d._kRightMotor.run(-baseSpeed)
#             print(str(s.degrés()) + " : 2")
#         while angleVoulu < s.degrés() - 1*speedLvl:
#             d._kLeftMotor.run(baseSpeed/(8))
#             d._kRightMotor.run(-baseSpeed/(8))
#             print("derniers 2: " + str(s.degrés()))
#         print(str(s.degrés()- angleVoulu))
#         turn = False
#     if angleVoulu > s.degrés() and deg > 0 and turn:
#         print("degrés voulu : " + str(angleVoulu))
#         while(angleVoulu > s.degrés() + 10 * speedLvl):
#             d._kLeftMotor.run(-baseSpeed)
#             d._kRightMotor.run(baseSpeed)
#             print(str(s.degrés()) + " : 3")
#         while angleVoulu > s.degrés() + 1 * speedLvl:
#             d._kLeftMotor.run(-baseSpeed/8)
#             d._kRightMotor.run(baseSpeed/8)
#             print("derniers 3: " + str(s.degrés()))
#         print(str(s.degrés()- angleVoulu))
#         turn = False
#     if angleVoulu > s.degrés() and deg < 0 and turn :
#         if angleVoulu < 360 - speedLvl * 10: 
#             while(angleVoulu > s.degrés()):
#                 d._kLeftMotor.run(baseSpeed)
#                 d._kRightMotor.run(-baseSpeed)
#                 print(str(round(s.degrés(),3)) + " : 4-0")
#             while(angleVoulu < s.degrés() - 10*speedLvl):
#                 d._kLeftMotor.run(baseSpeed)
#                 d._kRightMotor.run(-baseSpeed)
#                 print(str(round(s.degrés(),3)) + " : 4-1")
#             while angleVoulu < s.degrés() - 1*speedLvl:
#                 d._kLeftMotor.run(baseSpeed/(8))
#                 d._kRightMotor.run(-baseSpeed/(8))
#                 print("derniers 4: " + str(round(s.degrés(),3)))
#             print(str(s.degrés()- angleVoulu))
#         if angleVoulu > 360 - speedLvl * 10:
#             while(s.degrés() >= speedLvl* 10 + angleVoulu - 360):
#                 d._kLeftMotor.run(baseSpeed)
#                 d._kRightMotor.run(-baseSpeed)
#                 print(str(round(s.degrés(),3)) + " : 4-2")
#             while(s.degrés() < speedLvl * 10 + angleVoulu - 360):
#                 d._kLeftMotor.run(baseSpeed/(8*speedLvl))
#                 d._kRightMotor.run(-baseSpeed/(8*speedLvl))
#                 print("derniers 4: " + str(round(s.degrés(),3)))
#             print(str(s.degrés()- angleVoulu))
#         turn = False


#     print("stop : " + str(s.degrés()) + " voici l'angle de fin " + "voici angle voulu : " + str(angleVoulu))
#     print(str(s.degrés()- angleVoulu))
#     d.stopMotors()
#     return angleVoulu

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

def ligneDroiteSans(speedLvl):
    baseSpeed = -speedLvl * 90
    while (True):
        d.setSpeed(baseSpeed)
        print(s.degrés())
        

#ligneDroite(3,0)

def tourneXDegres(deg, speedLvl, indiceDeCorrection):
    baseSpeed = speedLvl * 45
    angleVoulu = float(((indiceDeCorrection + deg)%360))
    print("Voulu " + str(angleVoulu))
    turn = True 
    if angleVoulu < s.degrés() and deg > 0 and turn :
        if angleVoulu > speedLvl * 5: 
            while(angleVoulu < s.degrés()):
                d._kLeftMotor.run(-baseSpeed)
                d._kRightMotor.run(baseSpeed)
                print(str(s.degrés()) + " : 1-0")
            while(angleVoulu > s.degrés() + 5 * speedLvl):
                d._kLeftMotor.run(-baseSpeed)
                d._kRightMotor.run(baseSpeed)
                print(str(s.degrés()) + " : 1-1")
            while angleVoulu > s.degrés() + 1*speedLvl:
                d._kLeftMotor.run(-baseSpeed/(8*speedLvl))
                d._kRightMotor.run(baseSpeed/(8*speedLvl))
                print("derniers 1-1: " + str(s.degrés()))
            print(str(s.degrés()- angleVoulu))
        if angleVoulu <= speedLvl * 5:
            while(s.degrés() <= 360 - speedLvl* 5 + angleVoulu):
                d._kLeftMotor.run(-baseSpeed)
                d._kRightMotor.run(baseSpeed)
                print(str(s.degrés()) + " : 1-2")
            while(s.degrés() >= 360 - speedLvl * 5 + angleVoulu):
                d._kLeftMotor.run(-baseSpeed/(8*speedLvl))
                d._kRightMotor.run(baseSpeed/(8*speedLvl))
                print("derniers 1-2: " + str(s.degrés()))
            print(str(s.degrés()- angleVoulu))
        turn = False
    if angleVoulu < s.degrés() and deg < 0 and turn:
        while(angleVoulu < s.degrés() - 5*speedLvl):
            d._kLeftMotor.run(baseSpeed)
            d._kRightMotor.run(-baseSpeed)
            print(str(s.degrés()) + " : 2")
        while angleVoulu < s.degrés() - 1*speedLvl:
            d._kLeftMotor.run(baseSpeed/(8))
            d._kRightMotor.run(-baseSpeed/(8))
            print("derniers 2: " + str(s.degrés()))
        print(str(s.degrés()- angleVoulu))
        turn = False
    if angleVoulu > s.degrés() and deg > 0 and turn:
        print("degrés voulu : " + str(angleVoulu))
        while(angleVoulu > s.degrés() + 5 * speedLvl):
            d._kLeftMotor.run(-baseSpeed)
            d._kRightMotor.run(baseSpeed)
            print(str(s.degrés()) + " : 3")
        while angleVoulu > s.degrés() + 1 * speedLvl:
            d._kLeftMotor.run(-baseSpeed/8)
            d._kRightMotor.run(baseSpeed/8)
            print("derniers 3: " + str(s.degrés()))
        print(str(s.degrés()- angleVoulu))
        turn = False
    if angleVoulu > s.degrés() and deg < 0 and turn :
        if angleVoulu < 360 - speedLvl * 5: 
            while(angleVoulu > s.degrés()):
                d._kLeftMotor.run(baseSpeed)
                d._kRightMotor.run(-baseSpeed)
                print(str(round(s.degrés(),3)) + " : 4-0")
            while(angleVoulu < s.degrés() - 5*speedLvl):
                d._kLeftMotor.run(baseSpeed)
                d._kRightMotor.run(-baseSpeed)
                print(str(round(s.degrés(),3)) + " : 4-1")
            while angleVoulu < s.degrés() - 1*speedLvl:
                d._kLeftMotor.run(baseSpeed/(8))
                d._kRightMotor.run(-baseSpeed/(8))
                print("derniers 4-1: " + str(round(s.degrés(),3)))
            print(str(s.degrés()- angleVoulu))
        if angleVoulu > 360 - speedLvl * 5:
            while(s.degrés() >= speedLvl* 5 + angleVoulu - 360):
                d._kLeftMotor.run(baseSpeed)
                d._kRightMotor.run(-baseSpeed)
                print(str(round(s.degrés(),3)) + " : 4-2")
            while(s.degrés() < speedLvl * 5 + angleVoulu - 360):
                d._kLeftMotor.run(baseSpeed/(8*speedLvl))
                d._kRightMotor.run(-baseSpeed/(8*speedLvl))
                print("derniers 4-2: " + str(round(s.degrés(),3)))
            print(str(s.degrés()- angleVoulu))
        turn = False
    print("stop : " + str(s.degrés()) + " voici l'angle de fin " + "voici angle voulu : " + str(angleVoulu))
    print(str(s.degrés()- angleVoulu))
    print(str(s.degrés()- angleVoulu))
    print(str(s.degrés()- angleVoulu))
    print("stop : " + str(s.degrés()) + " voici l'angle de fin " + "voici angle voulu : " + str(angleVoulu))
    #reCalibre(angleVoulu, baseSpeed)
    d.stopMotors()
    return angleVoulu

def reCalibre(angleVoulu, speedLvl):
    baseSpeed = speedLvl * 45
    #TOURNE VERS GAUCHE

    if(math.sin(math.radians(s.degrés())) - math.sin(math.radians(angleVoulu)) < -0.003):
        # print("1")
        while(math.sin(math.radians(s.degrés())) < math.sin(math.radians(angleVoulu))):
                #print("2")
                d._kLeftMotor.run(baseSpeed/(10*speedLvl))
                d._kRightMotor.run(-baseSpeed/(10*speedLvl))
                print("RE-CALIBRATING LEFT  diff : " + str(math.sin(math.radians(s.degrés())) - math.sin(math.radians(angleVoulu)))+" deg: " +  str(s.degrés()))
    #Tourne vers droit
    elif (math.sin(math.radians(s.degrés())) - math.sin(math.radians(angleVoulu)) > 0.0025):
        #print("3")
        while(math.sin(math.radians(s.degrés())) > math.sin(math.radians(angleVoulu))):
                #print("4")
                d._kLeftMotor.run(-baseSpeed/(10*speedLvl))
                d._kRightMotor.run(baseSpeed/(10*speedLvl))
                print("RE-CALIBRATING DROIT diff : " + str(math.sin(math.radians(s.degrés())) - math.sin(math.radians(angleVoulu)))+" deg: " +  str(s.degrés()))
    


        
#DriveBase.distance
# while True :
#     d.avanceUntilObstacle(s)
#     indiceDeCorrection = tourneXDegres(180,2,indiceDeCorrection)
#     d.avanceUntilObstacle(s)
#     indiceDeCorrection = tourneXDegres(-180,2,indiceDeCorrection)
#indiceDeCorrection = tourneXDegres(-90,2,indiceDeCorrection)
#indiceDeCorrection = tourneXDegres(-90,2,indiceDeCorrection)
#d.avanceUntilObstacle(s)
#tourneXDegres(90,4,tourneXDegres(-90,3,tourneXDegres(90,2,tourneXDegres(-90,1,0))))
# while True: 
#      print("CURRENT : "+str(math.sin(math.radians(s.degrés()))) +" VOULU : "+ str(math.sin(math.radians(77))) +" diff : " + str(math.sin(math.radians(s.degrés())) - math.sin(math.radians(77)))+" deg: " +  str(s.degrés()))
#      #reCalibre(77, 2)
#ligneDroiteSans(3)
                


                #TOUTES LES CHOSES CI-DESSOUS SONT POUR CE QUE JE FAISAIT EN DERNIER, EN UTILISANT LES FONCTIONS DE DRIVEBASE, LA CLASSE ET NON ELLE QU'ON A FAIT,
                #

#robot = DriveBase(d._kLeftMotor, d._kRightMotor, wheel_diameter=42.2, axle_track=145)
robot = DriveBase(d._kLeftMotor, d._kRightMotor, wheel_diameter=42.2, axle_track=163)
#while True:


def printingAngle():
    while True:
        print(s.degrés())
        time.sleep(1)

#robot.turn(405)
#robot.turn(90)
t = Thread(target=printingAngle())
t2 = Thread(target=robot.turn(90))
robot.turn(90)
t2.start()
t.start() 
t.join()
t2.join()


