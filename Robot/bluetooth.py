#!/usr/bin/env pybricks-micropython
from pybricks.messaging import BluetoothMailboxServer, Mailbox
from pybricks import tools
from sensors import Sensors
from Drivebase import Drivebase
from autonomousMoving import AutonomousMoving
from Point2D import Point2D

class Bluetooth :
    #Initialisation des objets pour le fonctionnement de la classe bluetooth
    server = BluetoothMailboxServer()
    mbox = Mailbox('greeting', server)
    
    dernierMurEnvoye = 0

    def __init__(self):
        #Le serveur (ev3) doit attendre la connexion de l'ordi
        #Code exemple prit de la documentation microPython ev3
        print('waiting for connection...')
        self.server.wait_for_connection()
        print('connected!')

        # Le ev3 attends un message de l'ordinateur et renvoie un message de confirmation
        self.mbox.wait()
        print(self.mbox.read())
        self.mbox.send('Message recu')

    def sendPositionAndSensor(self, s:Sensors, d:Drivebase):
        """
        Méthode qui envoie la position du robot (x, y, angle) et la distance mesurée par les ultrasons
        """
        data = d._pos.__str__()
        data += ";UL:" + str(s.getLeftDistance())
        data += ";UR:" + str(s.getRightDistance())
        self.mbox.send(data)
        self.mbox.wait()
        #print(data)

    def sendPositionAndWalls(self, d:Drivebase, a:AutonomousMoving):
        """
        Envoie les nouvelles positions de murs (celles qui n'ont pas été envoyées) contenues dans AutonomousMoving
        """
        data = d._pos.__str__()
        #Regarde pour savoir si de nouveaux murs ont étés vus 
        if(len(a.points)>self.dernierMurEnvoye):
            #Ajoute tous les nouveaux dans le string qui va être envoyée
            for i in range(len(a.points) - self.dernierMurEnvoye):
                pointTemp = a.points[self.dernierMurEnvoye + i]
                print(pointTemp)
                temp = Point2D(pointTemp[0], pointTemp[1])
                data += ";"+ temp.__str__()
        #Enregistre la dernière position de mur envoyée
        self.dernierMurEnvoye = len(a.points)
        self.mbox.send(data)
        print(data)
        self.mbox.wait_new()
        print(self.mbox.read())
    
    def sendOtherData(self, text:str):
        """
        Méthode de débug
        Permet d'envoyer des strings à l'ordinateur
        """
        self.mbox.send(text)
        self.mbox.wait()
