import matplotlib.pyplot as plt
from scipy import stats
from  GrilleSalle import grilleSalle
from Data2 import Data

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
           
        return grille
    

            
    def insertionDonnees(grille, data):
        # --- INSERTION DES DONNÉES DANS LA GRILLE EN FONCTION DES LIMITES QUI ONT ÉTÉ DEFINIS ---
                     
        for point in range(len(data)): # on parcours les points des données originales
            for i in range(len(grille)): # on parcours les colonnes |
                for j in range (len(grille[0])): # on parcours les lignes -
                    # on vérifie si le point entre dans la case
                    if (data[point][0] >= grille[i][j].limiteInfX and data[point][0] <= grille[i][j].limiteSuppX) and (data[point][1] >= grille[i][j].limiteInfY and data[point][1] <= grille[i][j].limiteSuppY):
                        grille[i][j].dataGrille.append(data[point]) #on ajoute le point à la case
        
        for i in range(len(grille)): # on parcours les colonnes |
            for j in range (len(grille[0])): # on parcours les lignes -
                grille[i][j].quantite = len(grille[i][j].dataGrille)
                

        print("espacement:",Data.espacement)

        return grille 

    
    #création du array 2D grille
    grille = [[grilleSalle() for i in range(int((Data.trouverMaxY(Data.data)-Data.trouverMinY(Data.data))/Data.espacement)+1)] for j in range(int((Data.trouverMaxX(Data.data)-Data.trouverMinX(Data.data))/Data.espacement)+1)]
   
    grille = creationGrille(grille, Data.data)
    grille = insertionDonnees(grille, Data.data)
    



    x = []
    y = []

    for point in range(len(Data.data)-1):
        x.append(Data.data[point][0])
        y.append(Data.data[point][1])
    fig, (ax1, ax2) = plt.subplots(1, 2)
    
    #Dessiner les données
    ax1.scatter(x,y) # Ajoute le nuage de point, c-à-d les données que le robot à collecter, au plot 
    
    #Dessiner les données avec les limites qui ont été calculée
    ax2.scatter(x,y)
    ax2.axvline(x = grille[0][0].limiteInfX, color = 'r')
    ax2.axhline(y = grille[0][0].limiteSuppY, color = 'r')

    for i in range(len(grille)): # on parcours les colonnes |
        for j in range (len(grille[0])): # on parcours les lignes -
            ax2.axvline(x = grille[i][j].limiteSuppX, color = 'r')
            ax2.axhline(y = grille[i][j].limiteInfY, color = 'r')
            

    reg = stats.linregress(Data.data[:][0], Data.data[:][1]) # Régression linéaire

    #plt.xlim([0, 25])
    #plt.ylim([10, 15])

    plt.show() # afficher le tout
######################################################################