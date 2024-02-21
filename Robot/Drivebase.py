#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Drivebase :
    _kLeftMotor = Motor(Port.D)
    _kRightMotor = Motor(Port.A)
    _kGyro = GyroSensor(Port.S2, Direction.COUNTERCLOCKWISE)
    _kWheelCirconference = float(3.14159*1.5*2)
    
    def _init_(self):
        self.setEncoders(0)
        self.setGyro(0)

    def _str_(self):
        self._kLeftMotor.angle()
        self._kRightMotor.angle()

    def setEncoders(self, angle):
        self._kLeftMotor.reset_angle(float(angle))
        self._kRightMotor.reset_angle(float(angle))

    def setGyro(self, angle):
        self._kGyro.reset_angle(float(angle))
    
    def stop(self):
        self._kLeftMotor.run(0)
        self._kRightMotor.run(0)
    
    def setSpeed(self, speed):
        self._kLeftMotor.run(speed)
        self._kRightMotor.run(speed)
    
    def getSpeed(self):
        return self._kLeftMotor.speed()
    
    def getDistance(self):
        return float(self._kLeftMotor.angle()*self._kWheelCirconference)
    
    def getAngle(self):
        angle = self._kGyro.angle()
        return angle

    def turn(self, angle, speed):
        targetAngle = self.getAngle()+angle     #
        print(float(targetAngle))
        if(angle > 0):
            rightSpeed = float(speed)*-1
            leftSpeed = float(speed)
        else:
            rightSpeed = float(speed)
            leftSpeed = float(speed)*-1

        self._kLeftMotor.run(leftSpeed)
        self._kRightMotor.run(rightSpeed)
        
        while True:
            #peux faire mieux pour plus de précision mais flemme/condition 
            #bcp plus complexe faut vérifier sens de rotation
            if(int(self.getAngle()) == int(targetAngle)): 
                self.stop()
                break

        #while self.getAngle() != targetAngle:

        