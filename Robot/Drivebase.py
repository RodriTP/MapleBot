#!/usr/bin/env pybricks-micropython
from sensors import Sensors
import sys
sys.path.append('/home/robot/MapleBot/Util')
from RobotPose import RobotPose
import math
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
import time


class Drivebase :
    """
    Classe représentant la base mobile du robot.\n
    Cette classe permet de controler les moteurs et gère l'odometrie du robot
    """
    #motors
    _kLeftMotor = Motor(Port.D)
    _kRightMotor = Motor(Port.A)
    #encoders
    rightOldEncoderVal = float(0)
    leftOldEncoderVal = float(0)
    rightEncoderMemory = 0
    leftEncoderMemory = 0
    #constants
    _kWheelCirconference = float(math.pi*43) #en mm
    VALUE_FROM_OBSTACLE = 300.0
    #Odometrie
    _s = Sensors()
    _pos = None
    #autre
    _hasFinishedAction = False

    
    
    def __init__(self):
        """Constructeur de Drivebase"""
        self.setEncoders(0)
        self.rightEncoderVal = self._kRightMotor.angle()
        self.leftEncoderVal =  self._kLeftMotor.angle()
        self._pos = RobotPose(0,0,0)

    def __str__(self):
        """affiche les valeur des encodeurs des moteurs"""
        return "leftMotorAngle : " + str(self._kLeftMotor.angle()) + "; righMotorAngle : " + str(self._kRightMotor.angle())
    
    def periodic(self):
        """
        Mettre ici les fonctions de Drivebase qui doivent être loop infiniment.\n
        Cette fonction va être appelé dans une boucle infinie dans le main (while True)
        """
        self.updatePos()

    def setEncoders(self, angle):
        """
        Override la valeur des encodeurs à un angle donné\n
        Param
            angle (float) : angle auquel on veut mettre les encodeurs
        """
        self._kLeftMotor.reset_angle(angle)
        self._kRightMotor.reset_angle(angle)
    
    def stopMotors(self):
        """Arrête et stall les moteurs"""
        self._kLeftMotor.hold()
        self._kRightMotor.hold()
    
    def setSpeed(self, speed):
        """
        Fait fonctionner les moteurs à la vitesse voulue\n
        Param
            speed (number) : vitesse voulue (positif = avancer, négatif = reculer)
        """
        self._kLeftMotor.run(-speed)
        self._kRightMotor.run(-speed)
    
    def getSpeed(self):
        """Return : la vitesse des moteurs"""
        return self._kLeftMotor.speed()
    
    def getDistance(self): #en mm
        """
        Return: (float) (mm) distance parcourue depuis la dernière fois que la méthode à été appelé
        """
        diffRightEncodervalue = self._kRightMotor.angle() - self.rightEncoderMemory
        diffLeftEncodervalue = self._kLeftMotor.angle() - self.leftEncoderMemory
        d = float((diffRightEncodervalue+diffLeftEncodervalue)/2 * self._kWheelCirconference / float(360))
        self.rightEncoderMemory = self._kRightMotor.angle()
        self.leftEncoderMemory = self._kLeftMotor.angle()
        return d #if d > 0.0 else d*-1.0
    
    
    def getDistanceWithoutReset(self):
        """
        Return: (float) (mm) distance parcourue depuis la dernière fois que les encodeurs on été reset (.setEncoder(0))
        """
        return self._kLeftMotor.angle()+self._kRightMotor.angle()/2 * self._kWheelCirconference/ float(360)
    
    def turn(self, angle, speed, sensors : Sensors):
        """
        Permet de touner le robot d'un certain angle\n
        Param
            angle : angle qu'on veut tourner
            speed : vitesse pour tourner
            sensors (Sensors) : objet de type sensors
        """
        self._hasFinishedAction = False
        targetAngle = sensors.degrés()+angle
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
            if(int(sensors.degrés()) == int(targetAngle)): 
                self.stopMotors()
                self._hasFinishedAction = True
                break

    def avanceDistance(self, distance : float): #distance en mm
        """
        Permet d'avancer une distance exacte
        Param
            distance (float) : distance en mm qu'on veut avancer
        """
        self._hasFinishedAction = False
        self.setEncoders(0)
        self.setSpeed(-200)
        
        

        distance = -3.22 * distance
        while self._hasFinishedAction == False:
            
            self._hasFinishedAction = (self.getDistanceWithoutReset() <= distance)
        
        print("J'AI AVANCÉ : "+str(self.getDistanceWithoutReset()))
        self.stopMotors()
    
    def equalsWithTolerance(self, value1 : float, value2 : float, tolerance : float):
        """
        Compare deux valeurs en tenant compte de la tolérance spécifié\n
        Param
            value1 (float) : valeur qu'on veut comparer
            value2 (float) : valeur avec la quelle on compare
            tolerance (float) : tolérance de la valeur2
        """
        if(float(value1) <= float(value2) + float(tolerance) 
           and float(value1) >= float(value2)+float(tolerance)):
            return True
        else:
            return False
    
    def updatePos(self):
        """
        Update la position du robot (x,y,yaw) (en mm et deg)
        """
        deg = self._s.degrés()
        dis = self.getDistance()
        x = self._pos.getX() + (math.cos(math.radians(deg)) *dis)
        y = self._pos.getY() + (math.sin(math.radians(deg)) *dis)*-1
        self._pos.set(
            x,
            y,
            deg
        )
    
    def cmToAngleRot(dist : float): 
        """
        Permet de transformer une distance en centimètre en valeur d'encodeur (angles)\n
        Param
            dist (float) : distance en cm à convertir en angles
        """
        return ((dist * 0.0949) * 360)
    
    def turnRad(self, deg : float, spd : int):
        """
        Permet de tourner le nombre de degrés voulus à la vitesse voulue.\n
        Param
            deg (float) : nombre de degrés qu'on veux tourner (+ troune a droite, - tourne a gauche)
                ex : angle actuel = 20, deg = 10, angle final = 30
            spd (int) : facteur de vitesse (spd va etre multiplié par 5 pour définir la vraie vitesse)
                ex : spd = 2, vitesse angulaire = 10
        """
        currDeg = self._s.degrés()
        quadActuel = self.déterminerQuad(0)    
        quadVoulu = self.déterminerQuad(deg)
        used = False
        works = True
        
        while(quadActuel != quadVoulu and works):
            print("angle : "+str(self._s.degrés()))
            self.gaucheOuDroiteSpd(deg, spd)
            quadActuel = self.déterminerQuad(0)
            if(abs(self.distToDeg(deg,currDeg)) > 5*spd):
                works = False
        if(abs(self.distToDeg(deg,currDeg)) >= 0.5):
            while(abs(self.distToDeg(deg,currDeg)) > 5*spd):
                self.gaucheOuDroiteSpd(deg, spd)
            if(self.distToDeg(deg,currDeg) >= 0.5):  
                while(self.distToDeg(deg,currDeg) >= 0.5):
                    self.gaucheOuDroiteSlw(deg)        
                used = True
            if(used  != True):
                while(self.distToDeg(deg,currDeg) <= -0.5):
                    self.gaucheOuDroiteSlw(deg)
        self.stopMotors()      

    def distToDeg(self, deg, currDeg):
        answer = self._s.degrés() - deg - currDeg
        if(answer < -360):
            answer = answer + 360
        if(answer > 360):
            answer = answer + -360
        return answer 
    
    def déterminerQuad(self, deg):
        """Détermine le quadrant dans lequelque l'angle voulu se trouve"""
        if (deg == 0): deg = self._s.degrés()
        if(math.sin(math.radians(deg)) > 0): si = 1
        else: si = 2 
        if(math.cos(math.radians(deg)) > 0): co = 1
        else: co = 2 
        if (si == 1): 
            if(co==1): quad = 1 
            elif(co==2): quad = 2
        elif(si==2): 
            if(co==2): quad = 3 
            elif(co==1): quad = 4
        return quad

    def gaucheOuDroiteSpd(self, deg, spd):
        """Détermine la direction qui faut tourner"""
        baseSpeed = 45 * spd
        #droite
        if(deg > 0):  
            self._kLeftMotor.run(-baseSpeed)
            self._kRightMotor.run(baseSpeed)
        #gauche
        if(deg < 0):
            self._kLeftMotor.run(baseSpeed)
            self._kRightMotor.run(-baseSpeed)

    def gaucheOuDroiteSlw(self, deg):
        """Détermine la direction qui faut tourner à vitesse réduite afin de garder de la précision"""
        #droite
        if(deg > 0):  
            self._kLeftMotor.run(-45/8)
            self._kRightMotor.run(45/8)
        #gauche
        if(deg < 0):
            self._kLeftMotor.run(45/8)
            self._kRightMotor.run(-45/8)
    
    def getPosition(self) -> RobotPose:
        """
        Retourne la position du robot
        """
        return self._pos

    def turnTime(self, code):
        """
        tourner droite = 90 gauche = -90 et 180dgr = 180
        """
        if(code == 180):
            self._kLeftMotor.run(-45)
            self._kRightMotor.run(+45)
            start = time.time()
            stopp = False
            while(not stopp):
                if(time.time() - start > 15.6):
                    stopp = True
                    self.stopMotors()
        if(code == 90):
            self._kLeftMotor.run(-45)
            self._kRightMotor.run(+45)
            start = time.time()
            stopp = False
            while(not stopp):
                if(time.time() - start > 8):
                    stopp = True
                    self.stopMotors()
        if(code == -90):
            self._kLeftMotor.run(+45)
            self._kRightMotor.run(-45)
            start = time.time()
            stopp = False
            while(not stopp):
                if(time.time() - start > 8):
                    stopp = True
                    self.stopMotors()