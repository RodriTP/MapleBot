#!/usr/bin/env pybricks-micropython
from sensors import Sensors

from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
#from pybricks.media.ev3dev import SoundFile, ImageFile


class Drivebase :
    _kLeftMotor = Motor(Port.D)
    _kRightMotor = Motor(Port.A)
    #_kGyro = GyroSensor(Port.S2, Direction.COUNTERCLOCKWISE)
    _kWheelCirconference = float(3.14159*1.5*2)
    VALUE_FROM_OBSTACLE = 50.0
    _hasFinishedAction = False
    
    def _init_(self):
        self.setEncoders(0)
        self.setGyro(0)

    def _str_(self):
        self._kLeftMotor.angle()
        self._kRightMotor.angle()

    #def periodic():
    

    def setEncoders(self, angle):
        self._kLeftMotor.reset_angle(float(angle))
        self._kRightMotor.reset_angle(float(angle))

    def setGyro(self, angle):
        self._kGyro.reset_angle(float(angle))
    
    def stopMotors(self):
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
    
    #droite = angle positif, gauche = angle négatif
    def turn(self, angle, speed):
        self._hasFinishedAction = False
        targetAngle = self.getAngle()+angle
        print(float(targetAngle))
        if(angle > 0): #tourne vers la droite
            rightSpeed = float(speed)*-1
            leftSpeed = float(speed)
        else: #tourne vers la gauche
            rightSpeed = float(speed)
            leftSpeed = float(speed)*-1
        
        self._kRightMotor.run(rightSpeed)
        self._kLeftMotor.run(leftSpeed)
        
        while True:
            #peux faire mieux pour plus de précision mais flemme/condition 
            #bcp plus complexe faut vérifier sens de rotation
            if(int(self.getAngle()) == int(targetAngle)): 
                self.stopMotors()
                self._hasFinishedAction = True
                break

        #while self.getAngle() != targetAngle:

    def avanceUntilObstacle(self, sensor):
        self._hasFinishedAction = False
        self.setSpeed(200)
        while True:
            if(sensor.getFrontValue()<self.VALUE_FROM_OBSTACLE):
                self.stopMotors()
                self._hasFinishedAction = True

    def avanceDistance(self, distance):
        self._hasFinishedAction = False
        self.setEncoders(0)
        self.setSpeed(200)
        while True:
            if self._kLeftMotor.angle() >= (float(distance)*360.0)/float(9.745):#9.745 en cm
                self.stopMotors()
                self._hasFinishedAction = True

    def moveAuto(self, sensor):
        hasObstacleInFront = False
        while True:#à determiner la condition de fin du movement autonome
            #commence a avancer
            if(not hasObstacleInFront and self.getSpeed() == 0 and self._hasFinishedAction):
                self.setSpeed(200)
            #s'arrette quand il a un obstacle devant lui
            elif(sensor.getFrontValue() <= self.VALUE_FROM_OBSTACLE and self._hasFinishedAction):
                print("obstacle found")
                self.stopMotors()
                hasObstacleInFront = True

            if(hasObstacleInFront):
                print("avoiding obstacle")
                #tourne a droite
                if(not sensor.getIsObstacleRight()):
                    self._kRightMotor.run(-100)
                    self._kLeftMotor.run(100)
                    if(sensor.getFrontValue() > self.VALUE_FROM_OBSTACLE and self._hasFinishedAction):
                        self.turn(30, 100)

                #tourne a gauche
                if(not sensor.getIsObstacleLeft()):
                    self._kRightMotor.run(100)
                    self._kLeftMotor.run(-100)
                    if(sensor.getFrontValue() > self.VALUE_FROM_OBSTACLE and self._hasFinishedAction):
                        self.turn(-30, 100)
                
                hasObstacleInFront = not self._hasFinishedAction
                print("obstacle avoided")
            
    
    
    def equalsWithTolerance(self, value, tolerance):
        if(float(value) <= float(value) + float(tolerance) 
           and float(value) >= float(value)+float(tolerance)):
            return True
        else:
            return False
    


        