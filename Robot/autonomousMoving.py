#!/usr/bin/env pybricks-micropython


import sys
import time
sys.path.append('/home/robot/MapleBot/Robot')
from Drivebase import Drivebase
from sensors import Sensors
#from RobotPose import RobotPose
import math
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
#import drivebase
from Point2D import Point2D
#from pybricks.media.ev3dev import SoundFile, ImageFile


#IL RESTE :
    #-LA FONCT SLOPE
    #-LA CONDITION POUR QUE LE ROBOT ARRÊTE
    #-LA PRÉCISION QUE LE ROBOT NE TOURNE PAS DANS LE MUR OU SON QUEST SE TROUVE, MAIS PLUS LOIN, OU MOIN, DÉPENDAMENT SUR QUELLE FONCT QU'ON CALL, (CASE 2/3) 
    #-FAIT LA FONCT AVANCE LONGEURE ROBOT TOURNE VERS QUEST ET LA METTRE DANS CASEfour
    #-
    #-
    #-
    #-


class AutonomousMoving :

    d = None
    s = None
    p = None
    _RANGE = math.sqrt(math.pow(180,2)+ math.pow(180,2))/2
    #position
    pos = [0,0]
    steps = [0,0,0]
    #x,y,orientationActuel, orientation Du quest
    quests = [0,0,0,0]
    event = [False, 0]
    points = [0,0]
    rightView = False
    leftView = False
    nbAppelé = 0

    def __init__(self, D : Drivebase, S : Sensors):
        self.d = D 
        self.s = S
        self.p = self.d._pos
    
    #Cette fonction calibre le robot d'une position face contre le mur
    def calibrate(self, x):
        while (x < 10000):
            self.d._kLeftMotor.run(45)
            self.d._kRightMotor.run(45)
            x = x+ 1
            #print(s.degrés())
        self.d.turnRad(176, 2)

    #Un mur est devant
    #-tourne à gauche si possible, sinon droit, sinon recul? (scénario de tourne à droit?)
    def caseOne(self):
        self.d.turnRad(-88,2)
        self.s.update()
        self.steps.append([self.p.getX, self.p.getY, 1])

    #Wall has appeared in sights left/right
    #-note le quest et continue ton trajet
    def caseTwo(self, direction):
        if(not self.comparerPosAuVisites(direction, 1)):
            if(direction == 1): 
                self.d.updatePos() 
                self.quests.append([self.p.getX, self.p.getY, self.s.degrés(), direction, len(self.steps)])
            else: 
                self.d.updatePos()
                self.quests.append([self.p.getX, self.p.getY, self.s.degrés(), direction, len(self.steps)])
        print("Wall has appeared in sights " + str(direction))

    #Wall has DISSAPPEARED in sights left/right
    #-note le quest et continue ton trajet
    def caseThree(self, direction):
        if(not self.comparerPosAuVisites(direction, 1)):
            if(direction == 1):     
                self.d.updatePos()
                self.quests.append([self.p.getX, self.p.getY, self.s.degrés(), direction, len(self.steps)])
            else: 
                self.d.updatePos()
                self.quests.append([self.p.getX, self.p.getY, self.s.degrés(), direction, len(self.steps)])
        print("Wall has DISSAPPEARED in sights " + str(direction))
    
    #You've hit a wall youve been to before
    #-visit the most recently active created quest
    def caseFour(self):
        (x, y, deg, direction, stepNb) = self.quests[-1]
        nbAUndo = len(self.steps) - stepNb
        self.undo(nbAUndo)
        if(direction > 0): self.d.turnRad(88, 2)
        else: self.d.turnRad(-88, 2)
        self.quests.remove[self.quests[-1]]

    #définie si event est true ou false, so si tes pas capable de trouver de events
    def caseFourOFour(self):
        self.calibrate(10000)
        self.d.avanceDistance(30 + 2* self.nbAppelé)
        self.d.turnRad(88, 2)
        self.nbAppelé = self.nbAppelé + 1
        self.d.updatePos()

    def placesTravelled(self):
        self.d.updatePos()
        self.pos.append(self.getCurrentPos())
        print("[ " + str(round(self.p.getX())) + ", " + str(round(self.p.getY())) + " ]")

    #cette fonct retourne vrai si le robot était passé par cette position autrefois, pour trigger case 4
    def comparerPosAuVisites(self, direction, case):
        i = 0
        response = False
        while(i < len(self.points)):
            if(self.estEntreVals(self.points[i], self.getCurrentPos(), self._RANGE) and case == 0):
                response = True
            if(self.estEntreVals(self.points[i], self.getPointVue(direction), self._RANGE) and case == 1):
                response = True
            i = i + 1
        return response

    def main(self):
        self.calibrate(0)
        self.placesTravelled()
        while (True):#CONDITION QUI FAIT QUE LE ROBOT DÉCIDE D'AVOIR FINIDAWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
            self.avanceUntilObstacle()
            if(self.comparerPosAuVisites(1, 0)):
                self.caseFour()
            else:
                self.caseOne()
            if(len(self.quests) == 0):
                self.caseFourOFour()
    
    def undo(self, nombreAUndo):
        i = 0
        self.d.turnRad(176,2)
        while(i < nombreAUndo):
            (a,b,c) = self.steps[-1]
            if(c == 0):
                self.d.avanceDistance(math.sqrt(math.pow(self.p.getX() - a,2) + math.pow(self.p.getY() - b,2)))
            elif(c == 1):
                self.d.turnRad(88,2)
            i = i + 1
            self.steps.remove(self.steps[-1])
        self.d.turnRad(176, 2)

    def estEntreVals(self, pointUn, pointDeux, range):
        response = False
        if(pointUn[0] > pointDeux[0] - self._RANGE and pointUn[0] < pointDeux[0] + range):
            if(pointUn[1] > pointDeux[1] - self._RANGE and pointUn[1] < pointDeux[1] + range):
                response = True
        return response
        
    def getCurrentPos(self):
        return [self.p.getX(), self.p.getY()]
    
    #si gauche coef = -1 si droit coef = +1
    def getPointVue(self, case):
        if(case == 1):
            return [self.p.getX() + (math.cos(self.s.degrés() + 90) * self.s.getRightDistance()),
            self.p.getY() + (math.sin(self.s.degrés() + 90) * self.s.getRightDistance())]
        elif(case == -1):
            return [self.p.getX() + (math.cos(self.s.degrés() - 90) * self.s.getLeftDistance()),
            self.p.getY() + (math.sin(self.s.degrés() - 90) * self.s.getLeftDistance())]

    def avanceUntilObstacle(self):
        self._hasFinishedAction = False
        self.d.setSpeed(-400)
        while self._hasFinishedAction == False:
            #print("1")
            self.placesTravelled()
            if(self.s.getLeftDistance() < 100):
                if(self.leftView == False): self.caseTwo(-1, 90)
                self.leftView = True
                self.points.append(self.getPointVue(-1))
                #print("2")
            else : 
                if(self.leftView == True): self.caseThree(-1, 90)
                self.leftView = False
                #print("3")
            if(self.s.getRightDistance() < 100):
                if(self.rightView == False): self.caseTwo(1, 90)
                self.rightView = True
                self.points.append(self.getPointVue(1))
                #print("4")
            else : 
                if(self.rightView == True): self.caseThree(1, 90)
                self.rightView = False
                #print("5")
            if(self.s.getFrontValue() < self.d.VALUE_FROM_OBSTACLE):
                print("6")
                self._hasFinishedAction = True
                self.d.updatePos()
                print(str(self.p.getX()) + " : " + str(self.p.getY()))
                self.d.stopMotors()
                time.sleep(0.1)
                self.d.updatePos()
                print(str(self.p.getX()) + " : " + str(self.p.getY()))
                self.steps.append([self.p.getX, self.p.getY, 0])