#!/usr/bin/env pybricks-micropython
import pybricks
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.robotics import DriveBase
from pybricks.messaging import BluetoothMailboxServer, TextMailbox
from pybricks.tools import StopWatch, DataLog
import math
from Drivebase import Drivebase
from sensors import Sensors
from Point2D import Point2D
from autonomousMoving import AutonomousMoving
import time
import _thread
#from bluetooth import Bluetooth
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

indiceDeCorrection = 0
x = 0
y = 0
pos = [x,y]
ev3 = EV3Brick()
s = Sensors()
d = Drivebase()
s = Sensors()

#p = Point2D(x,y)
a = AutonomousMoving(d,s)


#robot = DriveBase(d._kLeftMotor, d._kRightMotor, wheel_diameter=42.2, axle_track=145)
#robot = DriveBase(d._kLeftMotor, d._kRightMotor, wheel_diameter=42.2, axle_track=163)

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
    #reCalibre(angleVoulu, baseSpeed)
    d.stopMotors()
    return angleVoulu

#print("CURRENT : "+str(math.sin(math.radians(s.degrés()))) +" VOULU : "+ str(math.sin(math.radians(77))) +" diff : " + str(math.sin(math.radians(s.degrés())) - math.sin(math.radians(77)))+" deg: " +  str(s.degrés()))
#robot.turn(90)
#robot.turn(-90)

""" Section pour run du code"""
        
# while True :
#     d.avanceUntilObstacle(s)
# indiceDeCorrection = tourneXDegres(90,2,0)
# indiceDeCorrection = tourneXDegres(-90,2,indiceDeCorrection)
#     d.avanceUntilObstacle(s)
#tourneXDegres(90,2,0)

#tourneXDegres(90,4,tourneXDegres(-90,3,tourneXDegres(90,2,tourneXDegres(-90,1,0))))

"""
d.avanceDistance(50)
d.computePos()
print('pos 1 :'+ str(d._pos))
tourneXDegres(90, 5,0)
d.computePos()
print('pos 2 :'+ str(d._pos))
d.avanceDistance(50)
d.computePos()
print('pos 3 :'+ str(d._pos))
"""



# s.degrés()
    



""" Fin Section pour run code"""























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

# def calibrer():
#     x = 0
#     while (x < 10000):
#         d._kLeftMotor.run(45)
#         d._kRightMotor.run(45)
#         x = x+ 1
#         #print(s.degrés())
#     turnRad(176, 2)







# b = Bluetooth()

# def sendData():
#     """
#     Update la position et envoie continuellement la position et valeur des sensors distance à l'ordinateur
#     """
#     while True :
#         d.updatePos()
#         b.sendPositionAndSensor(s,d)


# t1 = _thread.start_new_thread(sendData, ())


a.main()


# while True:
#     print(s.getFrontValue())
#     if(s.getFrontValue() < d.VALUE_FROM_OBSTACLE):
#         print("AAAAA")