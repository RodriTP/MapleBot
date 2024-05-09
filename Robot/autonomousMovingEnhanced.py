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
from RobotPose import RobotPose
#from pybricks.media.ev3dev import SoundFile, ImageFile
from enum import Enum


#IL RESTE :
    #-LA CONDITION POUR QUE LE ROBOT ARRÊTE
    #-LA PRÉCISION QUE LE ROBOT NE TOURNE PAS DANS LE MUR OU SON QUEST SE TROUVE, MAIS PLUS LOIN, OU MOIN, DÉPENDAMENT SUR QUELLE FONCT QU'ON CALL, (CASE 2/3) 
    #-FAIT LA FONCT AVANCE LONGEURE ROBOT TOURNE VERS QUEST ET LA METTRE DANS CASEfour
    #-quand le robot undo, fait que quand tu tourne vers le quest, c'est un step 2 de tourner du coté x, ensuite quql chs jai oublié
    #-
    #-
    #-
class States(Enum):
    CALIBRATING = 0
    ADVANCE_UNTIL_OBSTACLE = 1
    LOOKING_FOR_NEW_QUEST = 2
    UNDO = 3 #a changer de nom potentiellement pour un plus clair

class AutonomousMoving :
    drivebase = None
    sensors = None

    #variables de la state machine
    currentState = States.CALIBRATING #state par défaut
    previousState = None

    #variables nécessaire au fonctionnement de l'algorithme de déplacament autonome
    placesOfInterestTravelled = [] #la position 0 du tableau est la position de départ du robot
    quests = []

    def __init__(self, d : Drivebase, s : Sensors):
        self.drivebase = d
        self.sensors = s
    
    def consumeStateInput(self):
        #
        if self.currentState == States.CALIBRATING and self.previousState != States.CALIBRATING:
            print("Entering state CALIBRATING")
            self.calibrate(0)
            self.addNewPlaceTravelled()
            print("End of CALIBRATING")
            self.setState(States.ADVANCE_UNTIL_OBSTACLE)

        if self.currentState == States.ADVANCE_UNTIL_OBSTACLE and self.previousState != States.ADVANCE_UNTIL_OBSTACLE:
            print("Entering state ADVANCE_UNTIL_OBSTACLE")
            self.drivebase.setSpeed(400)

            wasObstacleLeft = self.sensors.isObstacleLeft()
            wasObstacleRight = self.sensors.isObstacleRight()

            while not self.sensors.isObstacleInFront():
                if not self.sensors.isObstacleLeft() and wasObstacleLeft == True:
                    self.quests.append(Point2D(self.drivebase.getPosition().getX(), self.drivebase.getPosition().getY(), self.drivebase.getPosition().getOrientation()-90.0))
                    wasObstacleLeft = False
                
                if not self.sensors.isObstacleRight() and wasObstacleRight == True:
                    self.quests.append(Point2D(self.drivebase.getPosition().getX(), self.drivebase.getPosition().getY(), self.drivebase.getPosition().getOrientation()+90.0))
                    wasObstacleRight = False

            self.drivebase.stopMotors()
            self.addNewPlaceTravelled()
            self.setState(States.LOOKING_FOR_NEW_QUEST)        

        if self.currentState == States.LOOKING_FOR_NEW_QUEST:
            print("Starting state LOOKING_FOR_NEW_QUEST")

        if self.currentState == States.UNDO :
            print("Starting state UNDO")
    
    previousState = currentState
    
    
    def calibrate(self, x):
        """
        Cette fonction calibre le robot d'une position face contre le mur.\n
        Params
            x : ?????????????
        """
        while (x < 10000):
            self.drivebase.setSpeed(45)
            x = x + 1
        self.drivebase.turnRad(176, 2)

    def addNewPlaceTravelled(self):
            """Ajoute une position (x,y,yaw) d'intéret au tableau de places déjà visité"""
            self.placesOfInterestTravelled.append(self.drivebase.getPosition())



    def setState(self, newState : States):
        self.previousState = self.currentState
        self.currentState = newState