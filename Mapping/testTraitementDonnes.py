import matplotlib.pyplot as plt
from  GrilleSalle import grilleSalle
from Data import Data
##################Début classe mainTraitementDonnees (sert de main) #######################
#### creer une grille la remplis avec la date et affiche la grille (modifier ce commentaire si mauvaise description)
class mainTraitementDonnees :
    grilleSalle.creerGrille(Data.data)

    x = []
    y = []

    for point in range(len(Data.data)-1):
        x.append(Data.data[point][0])
        y.append(Data.data[point][1])

    plt.scatter(x,y) # Ajoute le nuage de point, c-à-d les données que le robot à collecter, au plot 

    print("max X: ", Data.trouverMaxX(Data.data))
    print("min X: ", Data.trouverMinX(Data.data))
    print("max Y: ", Data.trouverMaxY(Data.data))
    print("min Y: ", Data.trouverMinY(Data.data))

    #stats = linregress(data[:][0], data[:][1]) # Régression linéaire

    #plt.xlim([0, 25])
    #plt.ylim([10, 15])

    plt.show() # afficher le tout
######################################################################