#!/usr/bin/env pybricks-micropython
import pybricks
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.robotics import DriveBase
from pybricks.messaging import BluetoothMailboxServer, TextMailbox
from pybricks.tools import StopWatch, DataLog
import math
from Drivebase import Drivebase
from sensors import Sensors
from Point2D import Point2D
from autonomousMoving import AutonomousMoving
import time
import _thread
from bluetooth import Bluetooth
from autonomousMovingEnhanced import AutonomousMovingEnhaced
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

ev3 = EV3Brick()
sensors = Sensors()
drivebase = Drivebase()
autonomousMoving = AutonomousMoving(drivebase,sensors)
bluetooth = Bluetooth()
autonomousMovingEnhaced = AutonomousMovingEnhaced(drivebase, sensors)

def periodicMain():
    """
    Fonction qui permet de loop les fonctions periodic à l'infini.\n
    Seule fonction periodic qui contient un "while True"
    """
    while True:
        sensors.periodic()
        drivebase.periodic()

def bluetoothMain():
    """
    Fonction qui permet d'envoyer les informations voulue vers l'ordinateur périodiquement.
    """
    global bluetooth
    while True:
        bluetooth.sendPositionAndWalls(drivebase, autonomousMoving)
        bluetooth.sendPositionAndSensor(sensors, drivebase)

#Création de threads pour faire fonctionner le code qui doit etre fait périodiquement sans affecter le reste du code
periodicThread = _thread.start_new_thread(periodicMain, ())
bluetoothThread = _thread.start_new_thread(bluetoothMain, ())

autonomousMovingEnhaced.start()