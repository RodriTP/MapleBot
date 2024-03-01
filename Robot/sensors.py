#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Sensors :
    _frontInfrared = InfraredSensor(Port.S3)        #Left infrared, à changer de place, maybe??
    _leftUltrasonic = UltrasonicSensor(Port.S1)     #Front ultrasonic, à changer de place, maybe??
    _rightUltrasonic = UltrasonicSensor(Port.S4)    #Right ultrasonic

    def getLeftDistance(self):
        return self._leftUltrasonic.distance(True) #mm      
    def getRightDistance(self):
        return self._rightUltrasonic.distance(True) #mm
    def getFrontDistance(self):
        return self._frontInfrared.distance() #retourne une val entre 0 et 100
    
