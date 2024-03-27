from ConnexionBluetooth import connexionBluetooth
from GrilleSalle import grilleSalle
from Data import Data
from testTraitementDonnes import mainTraitementDonnees
import sys
#sys.path.append('Util')
#from Point2D import Point2D


b = connexionBluetooth()
sensorData = []
d = Data()
d.ajoutDonnee(0.0, 0.0)

b.dataExchange()

repetition =0
while repetition<100:
    b.dataExchange()
    sensorData = b.separateData()
    b.resetData()
    d.ajoutDonnee(connexionBluetooth.getNumData(sensorData[0]), connexionBluetooth.getNumData(sensorData[1]))
    print(connexionBluetooth.getNumData(sensorData[0]), connexionBluetooth.getNumData(sensorData[1]))
    print(100-repetition)
    repetition+=1

#g = grilleSalle()
#g.creerGrille(d)
a = mainTraitementDonnees(d)
a.afficherGrille()