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
    #-LA CONDITION POUR QUE LE ROBOT ARRÊTE
    #-LA PRÉCISION QUE LE ROBOT NE TOURNE PAS DANS LE MUR OU SON QUEST SE TROUVE, MAIS PLUS LOIN, OU MOIN, DÉPENDAMENT SUR QUELLE FONCT QU'ON CALL, (CASE 2/3) 
    #-FAIT LA FONCT AVANCE LONGEURE ROBOT TOURNE VERS QUEST ET LA METTRE DANS CASEfour
    #-quand le robot undo, fait que quand tu tourne vers le quest, c'est un step 2 de tourner du coté x, ensuite quql chs jai oublié
    #-
    #-
    #-


class AutonomousMoving :

    d = None
    s = None
    p = None
    _RANGE = math.sqrt(math.pow(90,2)+ math.pow(90,2))/2
    #position du robot
    placesTravelled = []
    pos = []
    steps = []
    #x,y,orientationActuel, orientation Du quest
    quests = []
    points = []
    tasks = []
    rightView = False
    leftView = False
    nbAppelé = 0
    end = 0

    def __init__(self, D : Drivebase, S : Sensors):
        self.d = D 
        self.s = S
        self.p = self.d._pos
    
    #Cette fonction calibre le robot d'une position face contre le mur
    def calibrate(self, x):
        while (x < 10000):
            self.d._kLeftMotor.run(45)
            self.d._kRightMotor.run(45)
            x = x + 1
            #print(s.degrés())
        self.d.turnRad(176, 2)

    #Un mur est devant
    #-tourne à gauche si possible, sinon droit, sinon recul? (scénario de tourne à droit?)
    def caseOne(self):
        #print(len(self.tasks))
        print("Entering case ONE")
        print(str(len(self.quests)) + " : Quests amount")

        if(not self.s.getIsObstacleLeft() and self.s.getIsObstacleRight()):
            #tourne a gauche
            self.d.turnRad(-88,2)
        elif(not self.s.getIsObstacleRight() and self.s.getIsObstacleLeft()):
            #tourne a droite
            self.d.turnRad(90)
        elif(self.s.getIsObstacleFront()):
            print("need to do undo function")

        
        self.steps.append([self.p.getX(), self.p.getY(), 1])
        print("End case ONE")
        #print("One")

    #Wall has appeared in sights left/right
    #-note le quest et continue ton trajet
    def caseTwo(self, direction):
        #print(self.s.getFrontValue())
        print("Wall has appeared in sights " + str(direction))
        #if(not self.comparerPosAuVisites(direction, 1)):
        self.d.updatePos() 
        self.tasks.append([self.p.getX(), self.p.getY(), self.s.degrés(), direction, len(self.steps), self.getPointVue(direction), 2])
        #print("Two")
        

    #Wall has DISSAPPEARED in sights left/right
    #-note le quest et continue ton trajet
    def caseThree(self, direction):
        print("Wall has DISSAPPEARED in sights " + str(direction))
        #if(not self.comparerPosAuVisites(direction, 1)):    
        self.d.updatePos()
        #print(str(self.p.getX()))
        self.tasks.append([self.p.getX(), self.p.getY(), self.s.degrés(), direction, len(self.steps), self.getPointVue(direction),3])
        #self.d.stopMotors()
        #print("Three")
        
    
    #You've hit a wall youve been to before
    #-visit the most recently active created quest
    def caseFour(self):
        (x, y, deg, direction, stepNb, case) = self.quests[-1]
        nbAUndo = len(self.steps) - stepNb
        self.undo(nbAUndo)
        if(case == 2):
            self.d.turnRad(180,2)
            self.d.avanceDistance(150)
            self.d.turnRad(180,2)
        if(case == 3):
            self.d.avanceDistance(150)
            self.d.turnRad(180,2)
        if(direction > 0): self.d.turnRad(88, 2)
        else: self.d.turnRad(-88, 2)
        self.quests.remove[self.quests[-1]]
        print("Four")

    #définie si event est true ou false, so si tes pas capable de trouver de events
    def caseFourOFour(self):
        self.calibrate(10000)
        self.d.avanceDistance(30 + 2* self.nbAppelé)
        self.d.turnRad(88, 2)
        self.nbAppelé = self.nbAppelé + 1
        self.d.updatePos()

    def addNewPlaceTravelled(self):
        self.d.updatePos()
        self.placesTravelled.append(self.getCurrentPos())
        #print("[ " + str(round(self.p.getX())) + ", " + str(round(self.p.getY())) + " ]")

    #cette fonct retourne vrai si le robot était passé par cette position autrefois, pour trigger case 4
    def comparerPosAuVisites(self, posX, posY, pointVue, case):
        i = 0
        response = False
        a,b = pointVue
        while(i < len(self.points)):
            c,d = self.points[i]
            if(self.estEntreVals(c, d, posX, posY, self._RANGE) and case == 0):
                response = True
                #print("[ " + str(round(c)) + ", " + str(round(d)) + " ] compared to : [ " + str(round(posX)) + ", " + str(round(posY)) + " ] within range : "  + str(round(self._RANGE,0)))
            if(self.estEntreVals(c, d, a, b, self._RANGE) and case == 1):
                response = True
                #print("[ " + str(c) + ", " + str(d) + " ] compared to : [ " + str(a) + ", " + str(b) + " ] within range : " + str(self._RANGE)  )
            i = i + 1
        return response

    def main(self):
        #première action
        self.calibrate(0)
        self.addNewPlaceTravelled()


        while (True):#CONDITION QUI FAIT QUE LE ROBOT DÉCIDE D'AVOIR FINI
            self.avanceUntilObstacle()
            self.transposeTasks()
            if(len(self.quests) == 0):
                if(not self.endIsNear()):
                    print("no quests right now")
                    self.caseOne()
                else:
                #CASE FOUR O FOUR
                    print("4040404040404040400404040404")
                    self.caseFourOFour()
            elif(self.comparerPosAuVisites(self.p.getX(), self.p.getY(), [0,0] , 0)):
                print("UNDO")
                self.caseFour()
            else:
                self.caseOne()
            #     self.caseFourOFour()
    
    def undo(self, nombreAUndo):
        i = 0
        self.d.turnRad(180,2)
        print("Undo")
        print(nombreAUndo)
        while(i < nombreAUndo):
            (a,b,c) = self.steps[-1]
            if(c == 0):
                self.d.avanceDistance(math.sqrt(math.pow(self.p.getX() - a,2) + math.pow(self.p.getY() - b,2)))
            elif(c == 1):
                self.d.turnRad(88,2)
            i = i + 1
            self.steps.remove(self.steps[-1])
        self.d.turnRad(180, 2)

    def estEntreVals(self, pointUnX, pointUnY, pointDeuxX, pointDeuxY, range):
        response = False
        if(pointUnX > pointDeuxX - self._RANGE and pointUnX < pointDeuxX + range):
            if(pointUnY > pointDeuxY - self._RANGE and pointUnY < pointDeuxY + range):
                response = True
        return response
        
    def getCurrentPos(self):
        return [self.p.getX(), self.p.getY()]
    
    #si gauche case = -1 si droit case = +1
    def getPointVue(self, case):
        if(case == 1):
            rightDistance = self.s.getRightDistance()
            tab = [self.p.getX() + (math.cos(self.s.degrés() + 90) * rightDistance), 
                    self.p.getY() + (math.sin(self.s.degrés() + 90) * rightDistance)]
            return tab
        elif(case == -1):
            leftDistance = self.s.getLeftDistance()
            return [self.p.getX() + (math.cos(self.s.degrés() - 90) * leftDistance),
                    self.p.getY() + (math.sin(self.s.degrés() - 90) * leftDistance)]
        
    def endIsNear(self):
        self.end = 1 + self.end
        if(self.end > 10):
            return True
        else:
            return False


    def transposeTasks(self):
        i = 0
        p = 0
        if(len(self.tasks) > 0):
            for [x,y,c,direction,e,pointVue, case] in self.tasks:
                if(not self.comparerPosAuVisites(x, y, pointVue, 1)):
                    p = p + 1
                    print("New quest added : " + str(p))
                    self.quests.append([x, y, c, direction, e, case])
                i = i + 1 
                #print("task number : " + str(i))  
            self.tasks.clear()
        

    def avanceUntilObstacle(self):
        self._hasFinishedAction = False
        self.d.setSpeed(-400)
        while self._hasFinishedAction == False:
            #print(self.s.getFrontValue())
            r = self.s.getRightDistance()
            l = self.s.getLeftDistance()
            self.addNewPlaceTravelled()
            if( l < 1000):
                if(self.leftView == False): self.caseTwo(-1)
                self.leftView = True
                self.points.append(self.getPointVue(-1))
            else:
            #elif(not l == 2550.0): 
                if(self.leftView == True): self.caseThree(-1)
                self.leftView = False
            if( r < 1000):
                if(self.rightView == False): self.caseTwo(1)
                self.rightView = True
                self.points.append(self.getPointVue(1))
            else:
                #if(not r == 2550.0):
                if(self.rightView == True): self.caseThree(1)
                self.rightView = False
            if(self.s.getFrontValue() < self.d.VALUE_FROM_OBSTACLE):
                print("OBSTACLE SEEN IN FRONT")
                self._hasFinishedAction = True
                #print(str(self.p.getX()) + " : " + str(self.p.getY()))
                self.d.stopMotors()
                self.d.updatePos()
                #print(str(self.p.getX()) + " : " + str(self.p.getY()))
                self.steps.append([self.p.getX(), self.p.getY(), 0])