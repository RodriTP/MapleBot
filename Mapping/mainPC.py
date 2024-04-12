from ConnexionBluetooth import connexionBluetooth
#from GrilleSalle import grilleSalle
from matplotlib.animation import FuncAnimation
from testTraitementDonnes import mainTraitementDonnees
#import testTraitementDonnes
#import sys
import matplotlib.pyplot as plt
import threading
#sys.path.append('Util')
#from Point2D import Point2D

fig, ax = plt.subplots()
_x = [0]
_y = [0]

sensorData = []

map = mainTraitementDonnees()

#fonction 1
def fonction1():
    b = connexionBluetooth()
    global _x
    global _y
    while True:
        b.dataExchange()
        #print("fin echange donnes")
        sensorData = b.separateData()
        #print(connexionBluetooth.getNumData(sensorData[0]), connexionBluetooth.getNumData(sensorData[1]))
        b.resetData()

        #ajout des points au graph
        _x.append(connexionBluetooth.getNumData(sensorData[0]))
        _y.append(connexionBluetooth.getNumData(sensorData[1]))
        #print("_x = " + str(_x[len(_x)-1]) + "_y = " + str(_y[len(_y)-1]))


t1 = threading.Thread(target=fonction1)
t1.start()

def animate(i):
    ax.scatter(_x, _y)

ani = FuncAnimation(fig, animate, frames=20, interval=500, repeat=False)

plt.show()



"""
repetition =0
while repetition<100:
    b.dataExchange()
    sensorData = b.separateData()
    b.resetData()
    print(connexionBluetooth.getNumData(sensorData[0]), connexionBluetooth.getNumData(sensorData[1]))
    #ajouterPoint(connexionBluetooth.getNumData(sensorData[0]), connexionBluetooth.getNumData(sensorData[1]))
    print(100-repetition)
    repetition+=1
"""
#g = grilleSalle()
#g.creerGrille(d)

