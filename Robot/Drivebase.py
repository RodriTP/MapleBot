#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Drivebase :
    #_kLeftMotor = Motor(Port.)
    #_kRightMotor = Motor(Port.)
    _kWheelDiameter = int(0)
    
    
    def _init_():
        resetEncoders()

    def _str_():
        pass

    def resetEncoders():
        _kLeftMotor.reset_angle(0)
        _kRightMotor.reset_angle(0)
    
    def stop():
        _kLeftMotor.brake()
        _kRightMotor.brake()
    
    def setSpeed(speed):
        _kLeftMotor.run(float(speed))
        _kRightMotor.run(float(speed))