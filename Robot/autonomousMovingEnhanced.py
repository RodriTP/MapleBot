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


#IL RESTE :
    #-LA CONDITION POUR QUE LE ROBOT ARRÊTE
    #-LA PRÉCISION QUE LE ROBOT NE TOURNE PAS DANS LE MUR OU SON QUEST SE TROUVE, MAIS PLUS LOIN, OU MOIN, DÉPENDAMENT SUR QUELLE FONCT QU'ON CALL, (CASE 2/3) 
    #-FAIT LA FONCT AVANCE LONGEURE ROBOT TOURNE VERS QUEST ET LA METTRE DANS CASEfour
    #-quand le robot undo, fait que quand tu tourne vers le quest, c'est un step 2 de tourner du coté x, ensuite quql chs jai oublié
    #-
    #-
    #-
class States:
    CALIBRATING = tuple(("CALIBRATING", 0))
    ADVANCE_UNTIL_OBSTACLE = tuple(("ADVANCE_UNTIL_OBSTACLE", 1))
    TURN = tuple(("TURN", 2))
    GO_TO_LAST_POINT_OF_INTEREST = tuple(("UNDO", 3)) #a changer de nom potentiellement pour un plus clair

class AutonomousMovingEnhaced :
    drivebase = None
    sensors = None

    #variables de la state machine
    currentState = tuple
    previousState = tuple

    #variables nécessaire au fonctionnement de l'algorithme de déplacament autonome
    _RANGE = math.sqrt(math.pow(90,2)+ math.pow(90,2))/2 /10 #avant était math.sqrt(math.pow(90,2)+ math.pow(90,2))/2
    pointsOfInterestTravelled = [] #la position 0 du tableau est la position de départ du robot
    quests = [] #places to explore aka quests available
    indexOfActiveQuest = int
    


    def __init__(self, d : Drivebase, s : Sensors):
        self.drivebase = d
        self.sensors = s

    def start(self):
        self.currentState = States.CALIBRATING
        print(self.currentState)
        while True:
            self.consumeStateInput()
    
    def consumeStateInput(self): # il faut faire boucler le consume state input jusqu'à ce que quests = 0
############### None ##########################
        if self.currentState == None:
            print("current state == Null")
            self.drivebase.stopMotors()

############### CALIBRATING ##########################
        if self.currentState == States.CALIBRATING and self.previousState != States.CALIBRATING:
            print("Entering state CALIBRATING")
            self.calibrate(0)
            self.addNewPlaceTravelled()
            print("End of CALIBRATING")
            self.setState(States.ADVANCE_UNTIL_OBSTACLE)

############### ADVANCE_UNTIL_OBSTACLE ##########################
        if self.currentState == States.ADVANCE_UNTIL_OBSTACLE and self.previousState != States.ADVANCE_UNTIL_OBSTACLE:
            print("Entering state ADVANCE_UNTIL_OBSTACLE")
            self.drivebase.setSpeed(400)

            wasObstacleLeft = self.sensors.isObstacleLeft()
            wasObstacleRight = self.sensors.isObstacleRight()

            while not self.sensors.isObstacleInFront(): #tant qu'il n'a pas de mur en face il vérifier les cotés pour créer des quests

                if wasObstacleLeft == True and self.sensors.isObstacleLeft() == False : #mur avant et pas mur actuellement
                    print("LEFT wall has DISAPPEARED")
                    self.pointsOfInterestTravelled.append(Point2D(self.drivebase.getPosition().getX(), self.drivebase.getPosition().getY(), self.drivebase.getPosition().getOrientation()-90.0)) #crée quest a gauche
                    self.quests.append(Point2D(self.drivebase.getPosition().getX(), self.drivebase.getPosition().getY(), self.drivebase.getPosition().getOrientation()-90.0))
                    wasObstacleLeft = False
                
                if wasObstacleLeft == False and self.sensors.isObstacleLeft() == True:
                    print("LEFT wall has APPEARED")
                    self.quests.append(Point2D(self.drivebase.getPosition().getX(), self.drivebase.getPosition().getY(), self.drivebase.getPosition().getOrientation()-90.0)) #crée quest a gauche
                    wasObstacleLeft = True
                
                if wasObstacleRight == True and self.sensors.isObstacleRight() == False:
                    print("RIGHT wall has DISAPPEARED")
                    self.pointsOfInterestTravelled.append(Point2D(self.drivebase.getPosition().getX(), self.drivebase.getPosition().getY(), self.drivebase.getPosition().getOrientation()+90.0)) #crée quest a droite
                    self.quests.append(Point2D(self.drivebase.getPosition().getX(), self.drivebase.getPosition().getY(), self.drivebase.getPosition().getOrientation()+90.0))
                    wasObstacleRight = False

                if wasObstacleRight == False and self.sensors.isObstacleRight == True:
                    print("RIGHT wall has DISAPPEARED")
                    self.quests.append(Point2D(self.drivebase.getPosition().getX(), self.drivebase.getPosition().getY(), self.drivebase.getPosition().getOrientation()+90.0)) #crée quest a droite
                    wasObstacleRight = True


            print("Wall in front")
            self.drivebase.stopMotors()
            
            if not self.isPositionAlreadyExplored(self.drivebase.getPosition()): #si la position ou il est rendu est nouvelle (pas encore exploré) il continue avec un TURN
                self.addNewPlaceTravelled()
                self.setState(States.TURN)
                print("Exiting ADVANCE_UNTIL_OBSTACLE")
            else : #la position ou il est rendu est déjà connues
                print("position déjà exporé")
                print("doit se rendre à la prochaine quest")
                      
          
############### TURN ##########################
        if self.currentState == States.TURN and self.previousState != States.TURN:
            print("Entering state TURN")

            if(self.sensors.isObstacleLeft() and not self.sensors.isObstacleRight()):#peut tourner a droite
                print("Turning right")
                self.drivebase.turnRad(90,2)
                self.setState(States.ADVANCE_UNTIL_OBSTACLE)
            
            elif (self.sensors.isObstacleRight() and not self.sensors.isObstacleLeft()):#peut tourner a gauche
                print("Turning left")
                self.drivebase.turnRad(-88,2)
                self.setState(States.ADVANCE_UNTIL_OBSTACLE)
            
            elif (self.sensors.isObstacleLeft() == False and self.sensors.isObstacleRight() == False): #pas de mur ni a gauche ni a droite
                print("NO walls on the SIDES")
                self.pointsOfInterestTravelled.append(Point2D(self.drivebase.getPosition().getX(), self.drivebase.getPosition().getY(), self.drivebase.getPosition().getOrientation()-90.0)) #crée quest a gauche
                print("Turning right")
                self.drivebase.turnRad(90,2) #tourne a droite
                self.setState(States.ADVANCE_UNTIL_OBSTACLE)
            
            else : #mur des 2 cotés
                print("nowhere to turn, undoing last action")
                self.setState(States.UNDO)


############### UNDO ##########################
        if self.currentState == States.UNDO :
            print("Starting state UNDO")
    
    previousState = currentState
### fin du consumeStateInput()

    
    def calibrate(self, x):
        """
        Cette fonction calibre le robot d'une position face contre le mur.\n
        Params
            x : ?????????????
        """
        time.sleep(3)
        while (x < 5000):
            self.drivebase.setSpeed(-45)
            x = x + 1
        self.drivebase.turnRad(176, 2)

    def addNewPlaceTravelled(self):
            """Ajoute une position (x,y,yaw) d'intéret au tableau de places déjà visité"""
            self.pointsOfInterestTravelled.append(self.drivebase.getPosition())

    #cette fonct retourne vrai si le robot était passé par cette position autrefois
    def isPositionAlreadyExplored(self, currentPosition : Point2D):
        """
        Permet de savoir si le robot est déjà passé par la coordonée où il est.\n
        Param
            currentPosition (Point2D): position Actuelle du robot (x,y)
        Return
            True : si le robot est déjà passé par la coordonnée
            False : si le robot n'est jamais passé par la coordonnée
        """
        i = 0
        while (i< len(self.pointsOfInterestTravelled)):
            if(self.estEntreVals(currentPosition, self.pointsOfInterestTravelled[i], self._RANGE)):
                print("place already explored")
                return True
            else:
                i += 1
        return False
    
    def estEntreVals(self, point1 : Point2D, point2 : Point2D, range  : float):
        """
        Vérifie si deux points sont égaux selon une certaine marge d'erreur\n
        Params 
            point1 (Point2D) : premier point qu'on veut comparer\n
            point2 (Point2D) : deuxième point qu'on veux comparer\n
            range (float) : marge d'erreur accepté
        """

        if(point1.getX() > point2.getX() - self._RANGE and point1.getX() < point2.getX() + range
           and point1.getY() > point2.getY() - self._RANGE and point1.getY() < point2.getY() + range):
            return True
        else : 
            return False

    def setState(self, newState : States):
        self.previousState = self.currentState
        self.currentState = newState