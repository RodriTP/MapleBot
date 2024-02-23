#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Sensors :
    _frontInfrared = InfraredSensor(Port.S2)
    _leftUltrasonic = UltrasonicSensor(Port.S1)
    _rightUltrasonic = UltrasonicSensor(Port.S3)

    def getLeftDistance(self):
        return self._leftUltrasonic.distance() #mm  
    
    def getRightDistance(self):
        return self._rightUltrasonic.distance() #mm
    
    def getFrontDistance(self):
        return self._frontInfrared.distance() #retourne une val entre 0 et 100 (faut multiplier par un scalaire)
    
