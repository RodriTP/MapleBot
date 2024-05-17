#!/usr/bin/env pybricks-micropython
import sys
sys.path.append('/home/robot/MapleBot/Robot')
from Drivebase import Drivebase
from sensors import Sensors
import math






class AutonomousMoving :

    d = None
    s = None
    p = None
    _RANGE = math.sqrt(math.pow(90,2)+ math.pow(90,2))/2
    #position du robot
    pos = []
    steps = []
    #x,y,orientationActuel, orientation Du quest
    quests = []
    points = []
    tasks = []
    rightView = False
    leftView = False
    nbAppelé = 0
    end = 0

    def __init__(self, D : Drivebase, S : Sensors):
        self.d = D 
        self.s = S
        self.p = self.d._pos
    
    
    def calibrate(self, x):
        """
        Cette fonction calibre le robot d'une position face contre le mur, le recul et
        lui fait tourner
        """
        while (x < 10000):
            self.d._kLeftMotor.run(45)
            self.d._kRightMotor.run(45)
            x = x + 1
        self.d.turnRad(176, 2)

    
    def caseOne(self):
        """
        Un mur est devant
        tourne à gauche
        """
        self.d.turnRad(-88,2)
        self.steps.append([self.p.getX(), self.p.getY(), 1])

    
    def caseWallAppeared(self, direction):
        """
        Wall has APPEARED in sights left/right
        note le quest et continue ton trajet
        """
        self.d.updatePos() 
        self.tasks.append([self.p.getX(), self.p.getY(), self.s.degrés(), direction, len(self.steps), self.getPointVue(direction), 2])
        

    
    def caseWallDissapeared(self, direction):
        """
        Wall has DISSAPPEARED in sights left/right
        note le quest et continue ton trajet
        """
        self.d.updatePos()
        self.tasks.append([self.p.getX(), self.p.getY(), self.s.degrés(), direction, len(self.steps), self.getPointVue(direction),3])
        
    
    def caseFour(self):
        """
        You've hit a wall youve been to before (tu sais ça en utilisant la ligne 153 ou tu compare tes valeurs) So:
        visit the most recently active created quest
        """
        (x, y, deg, direction, stepNb, case) = self.quests[-1]
        nbAUndo = len(self.steps) - stepNb
        self.undo(nbAUndo)
        if(case == 2):
            self.d.turnRad(180,2)
            self.d.avanceDistance(150)
            self.d.turnRad(180,2)
        if(case == 3):
            self.d.avanceDistance(150)
            self.d.turnRad(180,2)
        if(direction > 0): self.d.turnRad(88, 2)
        else: self.d.turnRad(-88, 2)
        self.quests.remove[self.quests[-1]]

    
    def caseFourOFour(self):
        """définie si event est true ou false, so si tes pas capable de trouver de events"""
        self.calibrate(10000)
        self.d.avanceDistance(30 + 2* self.nbAppelé)
        self.d.turnRad(88, 2)
        self.nbAppelé = self.nbAppelé + 1
        self.d.updatePos()

    def placesTravelled(self):
        self.d.updatePos()
        self.pos.append(self.getCurrentPos())

    
    def comparerPosAuVisites(self, posX, posY, pointVue, case):
        """
        Cette fonct retourne vrai si le robot avait passé par cette position autrefois, pour trigger case 4
        """
        i = 0
        response = False
        a,b = pointVue
        while(i < len(self.points)):
            c,d = self.points[i]
            if(self.estEntreVals(c, d, posX, posY, self._RANGE) and case == 0):
                response = True
            if(self.estEntreVals(c, d, a, b, self._RANGE) and case == 1):
                response = True
            i = i + 1
        return response

    def main(self):
        self.calibrate(0)
        self.placesTravelled()
        while (True):
            self.avanceUntilObstacle()
            self.transposeTasks()
            if(len(self.quests) == 0):
                if(not self.endIsNear()):
                    print("no quests right now")
                    self.caseOne()
                else:
                #CASE FOUR O FOUR
                    print("404")
                    self.caseFourOFour()
            elif(self.comparerPosAuVisites(self.p.getX(), self.p.getY(), [0,0] , 0)):
                print("UNDO")
                self.caseFour()
            else:
                self.caseOne()
    
    def undo(self, nombreAUndo):
        """
        Défait ses mouvements jusqu'à ce qu'il arrive à sont quest le plus récent
        """
        i = 0
        self.d.turnRad(180,2)
        print("Undo")
        print(nombreAUndo)
        while(i < nombreAUndo):
            (a,b,c) = self.steps[-1]
            if(c == 0):
                self.d.avanceDistance(math.sqrt(math.pow(self.p.getX() - a,2) + math.pow(self.p.getY() - b,2)))
            elif(c == 1):
                self.d.turnRad(88,2)
            i = i + 1
            self.steps.remove(self.steps[-1])
        self.d.turnRad(180, 2)

    def estEntreVals(self, pointUnX, pointUnY, pointDeuxX, pointDeuxY, range):
        """
        Est entre intervales == True else False
        """
        response = False
        if(pointUnX > pointDeuxX - self._RANGE and pointUnX < pointDeuxX + range):
            if(pointUnY > pointDeuxY - self._RANGE and pointUnY < pointDeuxY + range):
                response = True
        return response
        
    def getCurrentPos(self):
        return [self.p.getX(), self.p.getY()]
    
    
    def getPointVue(self, case):
        """
        Obtien la position calculé des sensors soit à gauche ou droite du robot
        """
        if(case == 1):
            rightDistance = self.s.getRightDistance()
            tab = [self.p.getX() + (math.cos(self.s.degrés() + 90) * rightDistance), 
                    self.p.getY() + (math.sin(self.s.degrés() + 90) * rightDistance)]
            return tab
        elif(case == -1):
            leftDistance = self.s.getLeftDistance()
            return [self.p.getX() + (math.cos(self.s.degrés() - 90) * leftDistance),
                    self.p.getY() + (math.sin(self.s.degrés() - 90) * leftDistance)]
        

    def endIsNear(self):
        """
        Calcul si le robot à fini sont parcours
        """
        self.end = 1 + self.end
        if(self.end > 10):
            return True
        else:
            return False


    def transposeTasks(self):
        """
        Pour éviter les ralentissements qui causeront des problèmes 
        ceci sécance afin de gèrer les calculs lorsqu'il est immobile
        """
        i = 0
        p = 0
        if(len(self.tasks) > 0):
            for [x,y,c,direction,e,pointVue, case] in self.tasks:
                if(not self.comparerPosAuVisites(x, y, pointVue, 1)):
                    p = p + 1
                    print("New quest added : " + str(p))
                    self.quests.append([x, y, c, direction, e, case])
                i = i + 1  
            self.tasks.clear()
        

    def avanceUntilObstacle(self):
        """
        Avancer until obstacle is X devant le robot, pendant ce temps, scan les alentours et prend en note les Quests 
        """
        self._hasFinishedAction = False
        self.d.setSpeed(-400)
        while self._hasFinishedAction == False:
            r = self.s.getRightDistance()
            l = self.s.getLeftDistance()
            self.placesTravelled()
            if( l < 1000):
                if(self.leftView == False): self.caseWallAppeared(-1)
                self.leftView = True
                self.points.append(self.getPointVue(-1))
            else:
                if(self.leftView == True): self.caseWallDissapeared(-1)
                self.leftView = False
            if( r < 1000):
                if(self.rightView == False): self.caseWallAppeared(1)
                self.rightView = True
                self.points.append(self.getPointVue(1))
            else:
                if(self.rightView == True): self.caseWallDissapeared(1)
                self.rightView = False
            if(self.s.getFrontValue() < self.d.VALUE_FROM_OBSTACLE):
                print("OBSTACLE SEEN IN FRONT")
                self._hasFinishedAction = True
                self.d.stopMotors()
                self.d.updatePos()
                self.steps.append([self.p.getX(), self.p.getY(), 0])