#!/usr/bin/env pybricks-micropython
import pybricks
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.robotics import DriveBase
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
#robot = DriveBase(d._kLeftMotor, d._kRightMotor, wheel_diameter=42.2, axle_track=145)
robot = DriveBase(d._kLeftMotor, d._kRightMotor, wheel_diameter=42.2, axle_track=163)


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

def printingAngle():
    while True:
        print(s.degrés())
        time.sleep(1)

#Avance la dist voulue en mm
def straight(dist : int):
    robot.straight(dist)

#tourneXDegres prend en paramètres`les degrés à effectuer(- pour tourner à gauche + pour la droite),
# la vitesse quelle doit effectuer ceci (la vitesse c'est 1/8 de tour par niv),
# et finalement l'indiceDeCorrection, ceci est une variable en dehors de la fonction qui enregistre l'angle que le bot voulais atteindre.
# Pour utiliser cette variable, le bot dois avoir utilisé cette fonction plus d'une fois. Sinon, utilisez la valeur 0.
def tourneXDegres(deg, speedLvl, indiceDeCorrection):
    baseSpeed = speedLvl * 45
    #angleVoulu = float(((s.degrés() + deg)%360))
    angleVoulu = float(((indiceDeCorrection + deg)%360))
    print("Voulu " + str(angleVoulu))
    turn = True 
    if s.degrés() > angleVoulu and deg > 0 and turn :
        if angleVoulu > speedLvl * 5: 
            while(s.degrés() > angleVoulu):
                d._kLeftMotor.run(-baseSpeed)
                d._kRightMotor.run(baseSpeed)
                print(str(s.degrés()) + " : 1-0")
            while(s.degrés() + 5 * speedLvl < angleVoulu):
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

#print("CURRENT : "+str(math.sin(math.radians(s.degrés()))) +" VOULU : "+ str(math.sin(math.radians(77))) +" diff : " + str(math.sin(math.radians(s.degrés())) - math.sin(math.radians(77)))+" deg: " +  str(s.degrés()))
#robot.turn(90)
#robot.turn(-90)


        
# while True :
#     d.avanceUntilObstacle(s)
#indiceDeCorrection = tourneXDegres(180,2,indiceDeCorrection)
#     d.avanceUntilObstacle(s)
#tourneXDegres(90,2,0)

#tourneXDegres(90,4,tourneXDegres(-90,3,tourneXDegres(90,2,tourneXDegres(-90,1,0))))































# def ligneDroite(speedLvl, distance):
#     baseAngle = s.degrés()
#     baseSpeed = -speedLvl * 90
#     while (True):
#         print(str(round(s.degrés() - baseAngle, 3)) + " Diff")
#         print(str(baseAngle) + "  Base Angle")
#         print(str(s.degrés()) + "  Current")
#         #baseAngle = baseAngle + 0.0007
#         if s.degrés() > baseAngle + 1: 
#             d._kLeftMotor.run(baseSpeed - 5)
#             d._kRightMotor.run(baseSpeed + 5)
#             print("GOING LEFT (too much right)")
#         elif s.degrés() < baseAngle - 1:
#             d._kLeftMotor.run(baseSpeed + 5)
#             d._kRightMotor.run(baseSpeed - 5)
#             print("GOING RIGHT (too much left)")
#         else:
#             d._kLeftMotor.run(baseSpeed)
#             d._kRightMotor.run(baseSpeed)
#             print("STRAIGHT")
#         #if d._kLeftMotor.angle() >= cmToAngleRot(30):
#             #d.stop()

# def ligneDroiteSans(speedLvl):
#     baseSpeed = -speedLvl * 90
#     while (True):
#         d.setSpeed(baseSpeed)
#         print(s.degrés())
        

        # def reCalibre(angleVoulu, speedLvl):
#     baseSpeed = speedLvl * 45
#     #TOURNE VERS GAUCHE

#     if(math.sin(math.radians(s.degrés())) - math.sin(math.radians(angleVoulu)) < -0.003):
#         # print("1")
#         while(math.sin(math.radians(s.degrés())) < math.sin(math.radians(angleVoulu))):
#                 #print("2")
#                 d._kLeftMotor.run(baseSpeed/(10*speedLvl))
#                 d._kRightMotor.run(-baseSpeed/(10*speedLvl))
#                 print("RE-CALIBRATING LEFT  diff : " + str(math.sin(math.radians(s.degrés())) - math.sin(math.radians(angleVoulu)))+" deg: " +  str(s.degrés()))
#     #Tourne vers droit
#     elif (math.sin(math.radians(s.degrés())) - math.sin(math.radians(angleVoulu)) > 0.0025):
#         #print("3")
#         while(math.sin(math.radians(s.degrés())) > math.sin(math.radians(angleVoulu))):
#                 #print("4")
#                 d._kLeftMotor.run(-baseSpeed/(10*speedLvl))
#                 d._kRightMotor.run(baseSpeed/(10*speedLvl))
#                 print("RE-CALIBRATING DROIT diff : " + str(math.sin(math.radians(s.degrés())) - math.sin(math.radians(angleVoulu)))+" deg: " +  str(s.degrés()))
    


def turnRad(deg, spd):
    quadActuel = déterminerQuad(0)    
    quadVoulu = déterminerQuad(deg)
    while(quadActuel != quadVoulu):
        gaucheOuDroiteSpd(deg, spd)
        quadActuel = déterminerQuad(0)
    while(distToDeg(deg) > 5):
        gaucheOuDroiteSpd(deg, spd)
    while(distToDeg(deg) <= 5):
        gaucheOuDroiteSlw(deg)
    print(str(distToDeg(deg)))

def distToDeg(deg):
    return abs(deg - s.degrés())  
  
def déterminerQuad(deg):
    if (deg == 0): deg = s.degrés()
    if(math.sin(math.radians(s.degrés())) > 0): si = 1
    else:si = 2 
    if(math.cos(math.radians(s.degrés())) > 0): co = 1
    else: co = 2 
    match [si,co]:
        case [1,1]: quad = 1
        case [1,2]: quad = 2
        case [2,2]: quad = 3
        case [2,1]: quad = 4
    return quad

def gaucheOuDroiteSpd(deg, spd):
    baseSpeed = 45 * spd
    if(deg > 0):  
        d._kLeftMotor.run(-baseSpeed)
        d._kRightMotor.run(baseSpeed)
    if(deg < 0):
        d._kLeftMotor.run(baseSpeed)
        d._kRightMotor.run(-baseSpeed)

def gaucheOuDroiteSlw(deg):
    if(deg > 0):  
        d._kLeftMotor.run(-45/8)
        d._kRightMotor.run(45/8)
    if(deg < 0):
        d._kLeftMotor.run(45/8)
        d._kRightMotor.run(-45/8)
