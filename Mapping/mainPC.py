from ConnexionBluetooth import connexionBluetooth
#from GrilleSalle import grilleSalle
from matplotlib.animation import FuncAnimation
#from testTraitementDonnes import mainTraitementDonnees
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

#fonction 1
b = connexionBluetooth()
def fonction1():
    global b
    global _x
    global _y
    while True:
        b.dataExchange()
        #print("fin echange donnes")
        sensorData = b.separateData()
        #print(connexionBluetooth.getNumData(sensorData[0]), connexionBluetooth.getNumData(sensorData[1]))
        b.resetData()

        #ajout des points au tableau s'il sont différents du précédent:
        #if(connexionBluetooth.getNumData(sensorData[0]) != _x[len(_x)-1] and connexionBluetooth.getNumData(sensorData[1])!=_y[len(_y)-1]):
        _x[0] = connexionBluetooth.getNumData(sensorData[0])
        _y[0] = connexionBluetooth.getNumData(sensorData[1])

        
        #x.append(connexionBluetooth.getNumData(sensorData[]))
        #y.append(connexionBluetooth.getNumData(sensorData[]))
        #print("_x = " + str(_x[len(_x)-1]) + "_y = " + str(_y[len(_y)-1]))


t1 = threading.Thread(target=fonction1)
t1.start()

def animate(i):
    ax.clear()
    ax.scatter(_x, _y, color='blue')
    ax.scatter(_x[0], _y[0], color='red')
    #print("_x = " + str(_x[len(_x)-1]) + "_y = " + str(_y[len(_y)-1]))

ani = FuncAnimation(fig, animate, interval=33.3333)

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

