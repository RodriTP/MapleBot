#!/usr/bin/env pybricks-micropython
#import utime
from pybricks.ev3devices import UltrasonicSensor
from pybricks.nxtdevices import UltrasonicSensor as UltrasonicSensor_Nxt
#from pybricks import nxtdevices.UltrasonicSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
#import adafruit_bno055, board
from pybricks.iodevices import I2CDevice
#from bno055 import *

#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Port, Color, Button, Direction, Stop
from pybricks.iodevices import DCMotor, UARTDevice, LUMPDevice, I2CDevice


from pybricks.parameters import Port
from pybricks.media.ev3dev import SoundFile

from gyro import Gyro
import _thread
  
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
        self._gyro.periodic()
    
    _DISTANCE_FROM_OBSTACLE = float(2000.0)

    def updateObastaclePresence(self):
        """Update périodiquement les booleans permettant savoir s'il y a un obstacle ou pas"""
        if(self.getLeftDistance() < self._DISTANCE_FROM_OBSTACLE):
            self._isObstacleLeft  = True
        else:
            self._isObstacleLeft = False
        if(self.getRightDistance() < self._DISTANCE_FROM_OBSTACLE):
            self._isObstacleRight = True
        else:
            self._isObstacleRight = False

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
    
    def getFrontValue(self):
        """Return : valeur arbitraire (varie en fonction de T°, distance, et autre) à un obstacle"""
        return float(self._frontUltrasonic.distance()) #retourne une val entre 0 et 100 (faut multiplier par un scalaire)
    
    def getIsObstacleLeft(self):
        """
        Return
            True: un objet est detecté
            False: aucun objet n'est detecté
        """
        return bool(self._isObstacleLeft)
    
    def getIsObstacleRight(self):
        """
        Return
            True: un objet est detecté
            False: aucun objet n'est detecté
        """
        return bool(self._isObstacleRight)
    #self.device.read(reg = 0x0F, length=1)

    def degrés(self):
        """Return: (float) la lecture du gyro en degré"""
        return Sensors._gyro._angle