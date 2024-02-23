#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Sensors :
    _frontInfrared = InfraredSensor(Port.S4)
    _leftUltrasonic = UltrasonicSensor(Port.S1)
    _rightUltrasonic = UltrasonicSensor(Port.S3)
    _isObstacleRight = False
    _isObstacleLeft = False

    _DISTANCE_FROM_OBSTACLE = float(200.0)

    def update(self):
        if(self.getLeftDistance() < self._DISTANCE_FROM_OBSTACLE):
            self._isObstacleLeft  = True
        if(self.getRightDistance() < self._DISTANCE_FROM_OBSTACLE):
            self._isObstacleRight = True
        else:
            self._isObstacleLeft = False
            self._isObstacleRight = False

    def getLeftDistance(self):
        return float(self._leftUltrasonic.distance()) #mm  
    
    def getRightDistance(self):
        return float(self._rightUltrasonic.distance()) #mm
    
    def getFrontValue(self):
        return float(self._frontInfrared.distance()) #retourne une val entre 0 et 100 (faut multiplier par un scalaire)
    
    def getIsObstacleLeft(self):
        return bool(self._isObstacleLeft)
    
    def getIsObstacleRight(self):
        return bool(self._isObstacleRight)