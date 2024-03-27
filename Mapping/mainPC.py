from ConnexionBluetooth import Bluetooth
from GrilleSalle import grilleSalle
from Data import Data
import sys
#sys.path.append('Util')
#from Point2D import Point2D


b = Bluetooth()
g = grilleSalle()
sensorData = []
d = Data()
d.ajoutDonnee(0.0, 0.0)
g.creerGrille(d)
b.dataExchange()

while True:
    b.dataExchange()
    sensorData = b.separateData()
    if(len(sensorData)!=1):
        d.ajoutDonnee(sensorData[0], sensorData[1])

    