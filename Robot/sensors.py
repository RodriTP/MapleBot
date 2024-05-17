#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import UltrasonicSensor
from pybricks.nxtdevices import UltrasonicSensor as UltrasonicSensor_Nxt
from pybricks.parameters import Port
from pybricks.parameters import Port
from gyro import Gyro
  
class Sensors :
    """
    Classe qui permet d'obtenir les valeurs de tous les senseurs présent sur le robot.\n
    Sensors est un singleton pour eviter de faire clash le code en créant multiples \n
    instances d'un même senseur physique
    """
    _leftUltrasonic = UltrasonicSensor(Port.S1)
    _frontUltrasonic = UltrasonicSensor_Nxt(Port.S3)
    _rightUltrasonic = UltrasonicSensor(Port.S4)
    _isObstacleRight = False
    _isObstacleLeft = False
    isObstacleLeftTab = []
    isObstacleRightTab = []
    _gyro = Gyro()
    

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Sensors, cls).__new__(cls)
        return cls.instance
    
    #sys, gyro,accel, mag
    def __init__(self) -> None:
        """Créer une instance de Sensors"""
        pass

    def periodic(self):
        """
        Mettre ici les fonctions de Sensors qui doivent être loop infiniment.
        Cette fonction va être appelé dans une boucle infinie dans le main
        """
        self.updateObastaclePresence()
        self.updateTabs()
        self._gyro.periodic()
    
    _SIDE_DISTANCE_FROM_OBSTACLE = float(300.0) #mm avant était 2000.0
    _FRONT_DISTANCE_FROM_OBSTACLE = float(175.0) #mm avant était 300.0

    def updateObastaclePresence(self):
        """Update périodiquement les booleans permettant savoir s'il y a un obstacle ou pas"""
        if(self.getLeftDistance() < self._SIDE_DISTANCE_FROM_OBSTACLE):
            self._isObstacleLeft  = True
        else:
            self._isObstacleLeft = False
        if(self.getRightDistance() < self._SIDE_DISTANCE_FROM_OBSTACLE):
            self._isObstacleRight = True
        else:
            self._isObstacleRight = False

    def updateTabs(self):
        Sensors.isObstacleLeftTab.append(self._isObstacleLeft)
        Sensors.isObstacleRightTab.append(self._isObstacleRight)

    def getLeftDistance(self):
        """
        Return : 
            distance entre la gauche du robot et l'objet le plus proche (en mm)
        """
        return float(self._leftUltrasonic.distance()) #mm  
    
    def getRightDistance(self):
        """
        Return : 
            distance entre la droite du robot et l'objet le plus proche (en mm)
        """
        return float(self._rightUltrasonic.distance()) #mm
    
    def isObstacleLeft(self):
        """
        Return
            True: un obstacle est detecté
            False: aucun obstacle n'est detecté
        """
        return self.isObstacleReal(Sensors.isObstacleLeftTab)
    
    def isObstacleRight(self):
        """
        Return
            True: un obstacle est detecté
            False: aucun obstacle n'est detecté
        """
        return self.isObstacleReal(Sensors.isObstacleRightTab)

    def isObstacleReal(self, tab):
        """
        Vérifie si il y réelement un obstacle en regardant la constance des 10\n
        dernières valeurs lues.
        """
        nbTrue = 0
        nbFalse = 0
        length = len(tab)
        if(length < 10):
            return False
        else:
            rtab = list(reversed(tab))
            for i in range(10):
                if(rtab[i]):
                    nbTrue +=1                        
                else:
                    nbFalse+=1
            return nbTrue>=7
        
    def degrés(self):
        """Return: (float) [0,360[ degré(s) en sens horaire"""
        return Sensors._gyro._angle
    
    def getFrontValue(self):
        """
        Return : 
                distance entre l'avant du robot et l'objet le plus proche (en mm)
        """
        return float(self._frontUltrasonic.distance()) #mm
    
    def isObstacleInFront(self):
        """
        Return
            True: un obstacle est detecté
            False: aucun obstacle n'est detecté
        """
        return bool(self.getFrontValue() < self._FRONT_DISTANCE_FROM_OBSTACLE)