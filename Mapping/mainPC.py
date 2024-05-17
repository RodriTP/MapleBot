from ConnexionBluetooth import connexionBluetooth
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import threading
import math

_x = [0]
_y = [0]

#True : Recoie position du robot et distance des ultrason
#False : Recoie position du robot et position des murs
recoieDistanceMurs = True

#Création de deux graphiques
fig, (axHeatmap, axScatter) = plt.subplots(1, 2)


b = connexionBluetooth()

def bluetooth():
    """
    Fonction qui permet de gérer la connexion Bluetooth de l'ordi et d'ajouter les points reçus par le robot
    """
    global b
    global _x
    global _y
    while True:
        #Échange de données
        b.dataExchange()
        sensorData = b.separateData()
        print("sensorData : " + str(sensorData))

        b.resetData()

        #Mise à jour de la position du robot dans la map
        _x[0] = connexionBluetooth.getNumData(sensorData[0])
        _y[0] = connexionBluetooth.getNumData(sensorData[1])

        #S'assure que la bonne méthode est appelée pour l'analyse des données
        #Ici, c'est la méthode avec les distances des ultrasons
        if recoieDistanceMurs:
            #Si l'ordinateur a reçu plus de 3 données (x, y, a, ultrason1, ultrason2), ajouter ces points au graphique
            if(len(sensorData)>3):
                distanceGauche = connexionBluetooth.getNumData(sensorData[3])/1000 #transforme la distance vue par l'ultrason gauche de mm en m
                if(distanceGauche < 2.0):
                    _x.append(calculerPointX(_x[0], distanceGauche, (connexionBluetooth.getNumData(sensorData[2])-90)%360)) #La position x du point ultrason gauche
                    _y.append(calculerPointY(_y[0], distanceGauche, (connexionBluetooth.getNumData(sensorData[2])-90)%360)) #La position Y du point ultrason gauche

                distanceDroite = connexionBluetooth.getNumData(sensorData[4])/1000 #transforme la distance vue par l'ultrason droit de mm en m
                if(distanceDroite < 2.0):
                    _x.append(calculerPointX(_x[0], distanceDroite, (connexionBluetooth.getNumData(sensorData[2])+90)%360)) #La position x du point ultrason droit
                    _y.append(calculerPointY(_y[0], distanceDroite, (connexionBluetooth.getNumData(sensorData[2])+90)%360))#La position Y du point ultrason droit

        #Deuxième méthode pour l'ajout des points des murs reçus
        else :
            #Regarde s'il a reçue les points des murs
            if(len(sensorData)>3):
                #Prend pour chaque point représentant un mur pour l'ajouter au tableau avec les points des murs
                for i in range (len(sensorData)-3):
                    if i%2==0:
                        _x.append(connexionBluetooth.getNumData(sensorData[i+3]))
                    else :
                        _y.append(connexionBluetooth.getNumData(sensorData[i+3]))
        

#Calcule la position du point du mur en X à l'aide de la trigonométrie
def calculerPointX(posX:float, distance:float, angle:float):
    return posX + distance*math.cos(math.radians(angle))

#Calcule la position du point du mur en X à l'aide de la trigonométrie
def calculerPointY(posY:float, distance:float, angle:float):
    return posY + distance*math.sin(math.radians(angle))

#Création de la thread pour le bluetooth
threadBluetooth = threading.Thread(target=bluetooth)
threadBluetooth.start()


def update(frame):
    """
    Fonction qui s'appelle toutes les 200ms qui met à jour l'histogramme 2d et le nuage de point
    """
    #Grahique important
    axHeatmap.clear()
    axHeatmap.hist2d(_x, _y, density=True, cmin=1, cmax=7, cmap='OrRd')
    axScatter.clear()
    axScatter.scatter(_x, _y, color='blue')

    #Position actuelle du robot dans la map
    axHeatmap.scatter(_x[0], _y[0], color='blue')
    axScatter.scatter(_x[0], _y[0], color='red')

# Créer l'animation dans mathplotlib et afficher les graphiques
ani = FuncAnimation(fig, update, frames=100, interval=200)
plt.show()
