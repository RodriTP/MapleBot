#!/usr/bin/env pybricks-micropython


import sys
import time
sys.path.append('/home/robot/MapleBot')
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



class AutonomousMoving :
    d = None
    s = None
    p = None
    #position
    pos = [0,0]
    steps = [0,0,0]
    #x,y,orientationActuel, orientation Du quest
    quests = [0,0,0,0]
    event = [False, 0]
    rightView = False
    leftView = False

    def __init__(self, D : Drivebase, S : Sensors):
        self.d = D 
        self.s = S
        self.p = D._pos
    
    #Cette fonction calibre le robot de position face au mur
    def calibrate(self):
        x = 0
        while (x < 10000):
            self.d._kLeftMotor.run(45)
            self.d._kRightMotor.run(45)
            x = x+ 1
            #print(s.degrés())
        self.d.turnRad(176, 2)


    #Un mur est devant
    #-tourne à gauche si possible, sinon droit, sinon recul? (scénario de tourne à droit?)
    def caseOne(self):
        self.d.turnRad(-90,2)
        self.s.update()
        self.steps.append([self.p.getX, self.p.getY, 1])


    #Wall has appeared in sights left/right
    #-note le quest et continue ton trajet
    def caseTwo(self, direction, angle):
        #if(direction == 1): self.d.updatePos(), self.quests.append([self.p.getX, self.p.getY, self.s.degrés(),angle, len(self.steps)])
        #else: self.d.updatePos(), self.quests.append([self.p.getX, self.p.getY, self.s.degrés(),-angle, len(self.steps)])
        print("Wall has appeared in sights " + str(direction))

    #Wall has DISSAPPEARED in sights left/right
    #-note le quest et continue ton trajet
    def caseThree(self, direction,angle):
        #if(direction == 1): self.d.updatePos(), self.quests.append([self.p.getX, self.p.getY, self.s.degrés(),+angle, len(self.steps)])
        #else: self.d.updatePos(), self.quests.append([self.p.getX, self.p.getY, self.s.degrés(),-angle, len(self.steps)])
        print("Wall has DISSAPPEARED in sights " + str(direction))
    
    #You've hit a wall youve been to before
    #-visit the most recently active created quest
    def caseFour(self):
        (a,b,c,d,e) = self.quests[-1]
        self.undo(e)
    

    def placesTravelled(self):
        self.d.updatePos()
        self.pos.append([self.p.getX, self.p.getY])
        #print(self.p.__str__())
    

    def main(self):
        self.placesTravelled()

        while (self.event[0] == False):
            self.avanceUntilObstacle()
            #if(POSITION IS ONE I ALREADY HAV BEEN TOO, TRIGGER 4):
                #caseFour()


        return True
    
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

    
    def avanceUntilObstacle(self):
        self._hasFinishedAction = False
        self.d.setSpeed(-400)
        #print(str(self.s.degrés()) + " : Avance")
        #time.sleep(0.1)
        while self._hasFinishedAction == False:
            #print("1")
            self.placesTravelled()
            if(self.s.getLeftDistance() < 100):
                if(self.leftView == False): self.caseTwo(-1, 90)
                self.leftView = True
                #print("2")
            else : 
                if(self.leftView == True): self.caseThree(-1, 90)
                self.leftView = False
                #print("3")
            if(self.s.getRightDistance() < 500):
                if(self.rightView == False): self.caseTwo(1, 90)
                self.rightView = True
                #print("4")
            else : 
                if(self.rightView == True): self.caseThree(1, 90)
                self.rightView = False
                #print("5")
            if(self.s.getFrontValue() < self.d.VALUE_FROM_OBSTACLE):
                print("6")
                self._hasFinishedAction = True
                self.d.updatePos()
                #print(str(self.p.getX()) + "     :     " + str(self.p.getY()))
                self.d.stopMotors()
                time.sleep(0.1)
                #self.d.updatePos()
                print(str(self.p.getX()) + "     :     " + str(self.p.getY()))
                self.steps.append([self.p.getX, self.p.getY, 0])
