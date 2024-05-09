import matplotlib.pyplot as plt
import matplotlib.patches as patches
from  GrilleSalle import grilleSalle
from Data2 import Data
from TraitementDonnees import traitementDonnees
import numpy as np

################## Début classe mainTraitementDonnees (sert de main) #######################
#### creer une grille la remplis avec les données et affiche la grille
class main :
        traitement_instance = traitementDonnees

        #création du array 2D grille
        grille = [[grilleSalle() for i in range(int((Data.trouverMaxY(Data.data)-Data.trouverMinY(Data.data))/Data.espacement)+1)] for j in range(int((Data.trouverMaxX(Data.data)-Data.trouverMinX(Data.data))/Data.espacement)+1)]
    
        grille = traitement_instance.creationGrille(grille, Data.data, Data)
        grille = traitement_instance.insertionDonnees(grille, Data.data)
        grille = traitement_instance.determinerMur(grille)

        # Affichage
        x = []
        y = []

        for point in range(len(Data.data)-1):
            x.append(Data.data[point][0])
            y.append(Data.data[point][1])

        # Séparation de la fenêtre en trois graphiques
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(13, 7))

        #Dessiner les données
        ax1.scatter(x,y) # Ajoute le nuage de point, c-à-d les données que le robot à collecter, au plot 

        #Dessiner les données avec les limites qui ont été calculée
        ax2.scatter(x,y)
        ax2.axvline(x = grille[0][0].limiteInfX, color = 'r')
        ax2.axhline(y = grille[0][0].limiteSuppY, color = 'r')


        #Affichage du grillage et de la carte
        for i in range(len(grille)): # on parcours les colonnes |
            for j in range (len(grille[0])): # on parcours les lignes -
                ax2.axvline(x = grille[i][j].limiteSuppX, color = 'r')
                ax2.axhline(y = grille[i][j].limiteInfY, color = 'r')

                if grille[i][j].mur == True :
                    mur = patches.Rectangle((grille[i][j].limiteInfX, grille[i][j].limiteInfY), grille[i][j].limiteSuppX - grille[i][j].limiteInfX, grille[i][j].limiteSuppY- grille[i][j].limiteInfY, edgecolor='#FE2121', facecolor='#FE2121')
                else:
                    mur = patches.Rectangle((grille[i][j].limiteInfX, grille[i][j].limiteInfY), grille[i][j].limiteSuppX - grille[i][j].limiteInfX, grille[i][j].limiteSuppY- grille[i][j].limiteInfY, edgecolor='#C2F6F6', facecolor='#C2F6F6')
               
                ax3.add_patch(mur)

        plt.xlim(0, Data.trouverMaxX(Data.data) + 1)
        plt.ylim(0, Data.trouverMaxY(Data.data) + 1)
        plt.show() # afficher le tout
    ######################################################################
