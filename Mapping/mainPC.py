from ConnexionBluetooth import connexionBluetooth
from multiprocessing import Process
from GrilleSalle import grilleSalle
from matplotlib.animation import FuncAnimation
from testTraitementDonnes import mainTraitementDonnees
import testTraitementDonnes
import sys
import matplotlib.pyplot as plt
import threading
#sys.path.append('Util')
#from Point2D import Point2D
_x = [1]
_y = [1]
fig, ax = plt.subplots()


sensorData = []

map = mainTraitementDonnees()

#fonction 1
def fonction1():
    b = connexionBluetooth()
    while True:
        b.dataExchange()
        #print("fin echange donnes")
        sensorData = b.separateData()
        #print(connexionBluetooth.getNumData(sensorData[0]), connexionBluetooth.getNumData(sensorData[1]))
        b.resetData()

        #ajout des points au graph
        _x.append(connexionBluetooth.getNumData(sensorData[0]))
        _y.append(connexionBluetooth.getNumData(sensorData[1]))
        print("_x = " + str(_x[len(_x)-1]) + "_y = " + str(_y[len(_y)-1]))

t1 = threading.Thread(target=fonction1)
t1.start()

while True:
    print(len(_x))


"""
def ajouterPoint(x:float, y:float):
        global _x
        global _y
        _x.append(x)
        _y.append(y)
"""

"""
    #print("_x = " + str(_x[len(_x)-1]) + "_y = " + str(_y[len(_y)-1]))
def update(frame):
    global _x
    global _y
    #print("debut du update")
    ax.clear()  # clearing the axes
    ax.scatter(_x, _y)  # creating new scatter chart with updated data
    fig.canvas.draw()  # forcing the artist to redraw itself

anim = FuncAnimation(fig, update)
plt.show()

"""

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
