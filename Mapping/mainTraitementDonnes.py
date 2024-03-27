import matplotlib.pyplot as plt
from scipy import stats
from  GrilleSalle import grilleSalle
from Data import Data
################## Début classe mainTraitementDonnees (sert de main) #######################
#### creer une grille la remplis avec les données et affiche la grille
class mainTraitementDonnees :

    def creationGrille(grille, data): #métode pour creer un grillage et séparer les données

        # --- DÉFINITION DES LIMITES X ET Y POUR CHAQUE CASE ---

        #initialisation des pointeurs
        pointeurLimSuppX = Data.trouverMinX(data) 
        pointeurLimInfX = Data.trouverMinX(data)
        
        for i in range(len(grille)): # on parcours les colonnes |
            #on met les pointeurs Y à leur position initiales
            pointeurLimSuppY = Data.trouverMaxY(data) 
            pointeurLimInfY = Data.trouverMaxY(data)

            pointeurLimInfX= pointeurLimSuppX #la limite inférieure de la nouvelle case est égale à la limite supérieure de l'acienne case

            #Si il reste moins que l'espacement prévu, alors la valeur maximale en X correspond à la limite de la dernière colonne
            if (Data.trouverMaxX(data) - pointeurLimSuppX) < Data.espacement: 
                pointeurLimSuppX = Data.trouverMaxX(data)
            else: #Sinon la limite de la prochaine case est à une distance donnée de celle d'avant
                pointeurLimSuppX += Data.espacement

            for j in range (len(grille[0])): # on parcours les lignes -
                pointeurLimSuppY = pointeurLimInfY #la limite suppérieure de la nouvelle case est égale à la limite inférieure de l'acienne case
                
                #Si il reste moins que l'espacement prévu, alors la valeur maximale en X correspond à la limite de la dernière colonne
                if (pointeurLimInfY - Data.trouverMinY(data)) < Data.espacement:
                    pointeurLimInfY = Data.trouverMinY(data)
                else:  #Sinon la limite de la prochaine case est à une distance donnée de celle d'avant
                    pointeurLimInfY -= Data.espacement   

                grille[i][j].limiteSuppX = pointeurLimSuppX
                grille[i][j].limiteInfX = pointeurLimInfX
                grille[i][j].limiteSuppY = pointeurLimSuppY
                grille[i][j].limiteInfY = pointeurLimInfY
           #print("Point (", i, ", ", j, ") : LimiteSuppX = ", grille[i][j].limiteSuppX, "; LimiteInfX = ", grille[i][j].limiteInfX, "; LimiteSuppY = ", grille[i][j].limiteSuppY, "; LimiteInfY = ",grille[i][j].limiteInfY)
        
            
        
        # --- INSERTION DES DONNÉES DANS LA GRILLE EN FONCTION DES LIMITES QUI ONT ÉTÉ DEFINIS ---
                     
        for point in range(len(data)): # on parcours les points des données originales
            for i in range(len(grille)): # on parcours les colonnes |
                for j in range (len(grille[0])): # on parcours les lignes -
                    #print("Point (", i, ", ", j, ") : LimiteSuppX = ", grille[i][j].limiteSuppX, "; LimiteInfX = ", grille[i][j].limiteInfX, "; LimiteSuppY = ", grille[i][j].limiteSuppY, "; LimiteInfY = ",grille[i][j].limiteInfY)
                    if (data[point][0] > grille[i][j].limiteInfX and data[point][0] < grille[i][j].limiteSuppX) and (data[point][1] > grille[i][j].limiteInfY and data[point][1] < grille[i][j].limiteSuppY):
                        grille[i][j].dataGrille.append(data[point]) 
                        print("in!")
        
        for i in range(len(grille)): # on parcours les colonnes |
            for j in range (len(grille[0])): # on parcours les lignes -
                grille[i][j].quantite = len(grille[i][j].dataGrille)
                #print(grille[i][j].quantite)

        return grille 

    
    #création de la grille
    grille = [[grilleSalle() for i in range(int((Data.trouverMaxY(Data.data)-Data.trouverMinY(Data.data))/Data.espacement)+1)] for j in range(int((Data.trouverMaxX(Data.data)-Data.trouverMinX(Data.data))/Data.espacement)+1)]
    # for i in range(len(grille)): # on parcours les colonnes |
    #     for j in range (len(grille[0])): # on parcours les lignes -
    #         print("Point (", i, ", ", j, ") : LimiteSuppX = ", grille[i][j].limiteSuppX, "; LimiteInfX = ", grille[i][j].limiteInfX, "; LimiteSuppY = ", grille[i][j].limiteSuppY, "; LimiteInfY = ",grille[i][j].limiteInfY)
    
    grille = creationGrille(grille, Data.data)
    
    # for i in range(len(grille)): # on parcours les colonnes |
    #     for j in range (len(grille[0])): # on parcours les lignes -
    #          print("Point (", i, ", ", j, ") : LimiteSuppX = ", grille[i][j].limiteSuppX, "; LimiteInfX = ", grille[i][j].limiteInfX, "; LimiteSuppY = ", grille[i][j].limiteSuppY, "; LimiteInfY = ",grille[i][j].limiteInfY)


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

    reg = stats.linregress(Data.data[:][0], Data.data[:][1]) # Régression linéaire

    #plt.xlim([0, 25])
    #plt.ylim([10, 15])

    plt.show() # afficher le tout
######################################################################