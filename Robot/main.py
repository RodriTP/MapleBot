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
import time
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

from bluetooth import Bluetooth

ev3 = EV3Brick()
s = Sensors()


d = Drivebase()
s = Sensors()
indiceDeCorrection = 0
x = 0
y = 0
pos = [x,y]
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

b = Bluetooth()
s.degrés()

while True:
    d.computePos()
    print(d._pos.__str__())
    b.sendPositionAndSensor(s, d)
    print("send")
    



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
    


def turnRad(deg, spd):
    currDeg = s.degrés()
    quadActuel = déterminerQuad(0)    
    quadVoulu = déterminerQuad(deg)
    print(quadActuel)
    print(quadVoulu)
    used = False
    works = True
    #prob = quee il stop le quad après le but alors y arrête pas
    while(quadActuel != quadVoulu and works):
        #print(str(tooBig(distToDeg(deg,currDeg))) + " quadFonct")
        #print("QuadActuel : " + str(quadActuel) + "---QuadVoulu : " + str(quadVoulu))
        gaucheOuDroiteSpd(deg, spd)
        quadActuel = déterminerQuad(0)
        print(s.degrés())
        if(abs(tooBig(distToDeg(deg,currDeg))) > 10*spd):
            works = False
    if(abs(tooBig(distToDeg(deg,currDeg))) >= 0.5):
        while(abs(tooBig(distToDeg(deg,currDeg))) > 10*spd):
            print(s.degrés())
            #print(str(tooBig(abs(distToDeg(deg,currDeg)))) + " : more than 10")
            gaucheOuDroiteSpd(deg, spd)
        if(tooBig(distToDeg(deg,currDeg)) >= 0.5):  
            while(tooBig(distToDeg(deg,currDeg)) >= 0.5):
                print(s.degrés())
                #print(str(tooBig(distToDeg(deg,currDeg))) + " : less than 10-1")
                gaucheOuDroiteSlw(deg)        
            used = True
        if(used  != True):
            while(tooBig(distToDeg(deg,currDeg)) <= -0.5):
                print(s.degrés())
                #print(str(tooBig(distToDeg(deg,currDeg))) + " : less than 10-2 ")
                gaucheOuDroiteSlw(deg)
            
    print(str(distToDeg(deg,currDeg)) + " supposed to be done")
    #recal(deg)


def distToDeg(deg, currDeg):
    #print(str(s.degrés()) + " " + str(deg))
    answer = s.degrés() - deg - currDeg
    if(answer < -360):
        answer = answer + 360
    if(answer > 360):
        answer = answer + -360
    return answer #

def tooBig(distDiff):
    # if(distDiff > 180):
    #     return distDiff - 180
    # if(distDiff < -180): 
    #     return distDiff + 180
    return distDiff
  
def déterminerQuad(deg):
    if (deg == 0): deg = s.degrés()
    if(math.sin(math.radians(deg)) > 0): si = 1
    else: si = 2 
    if(math.cos(math.radians(deg)) > 0): co = 1
    else: co = 2 
    if (si == 1): 
        if(co==1): quad = 1 
        elif(co==2): quad = 2
    elif(si==2): 
        if(co==2): quad = 3 
        elif(co==1): quad = 4
    return quad

def gaucheOuDroiteSpd(deg, spd):
    baseSpeed = 45 * spd
    #droite
    if(deg > 0):  
        #print("right")
        d._kLeftMotor.run(-baseSpeed)
        d._kRightMotor.run(baseSpeed)
    #gauche
    if(deg < 0):
        #print("left")
        d._kLeftMotor.run(baseSpeed)
        d._kRightMotor.run(-baseSpeed)

def gaucheOuDroiteSlw(deg):
    #droite
    if(deg > 0):  
        #print("right")
        d._kLeftMotor.run(-45/8)
        d._kRightMotor.run(45/8)
    #gauche
    if(deg < 0):
        #print("left")
        d._kLeftMotor.run(45/8)
        d._kRightMotor.run(-45/8)



def recal(deg):
    #while(abs(distToDeg(deg)) > 0.5):
        while(s.degrés() - deg > 0.5 and deg > 0):#gauche
            print("RE-CALIBRATING GAUCHE diff : " + str(s.degrés() - deg)+" deg: " +  str(s.degrés()))
            d._kLeftMotor.run(45/10)
            d._kRightMotor.run(-45/10)
        while(s.degrés() - deg < -0.5 and deg < 0):#droite
            print("RE-CALIBRATING DROIT diff : " + str(s.degrés() - deg)+" deg: " +  str(s.degrés()))
            d._kLeftMotor.run(-45/10)
            d._kRightMotor.run(45/10)
            


def calibrer():
    x = 0
    while (x < 10000):
        d._kLeftMotor.run(45)
        d._kRightMotor.run(45)
        x = x+ 1
        #print(s.degrés())
    turnRad(176, 2)

#turnRad(-90,2)
calibrer()
while(True):
    d.avanceUntilObstacle(s)
    turnRad(-176, 2)
    d.avanceUntilObstacle(s)
    turnRad(176, 2)
# turnRad(100, 2)
# turnRad(-80, 2)
# turnRad(-45, 2)
# turnRad(-64, 2)
#robot.turn(113)