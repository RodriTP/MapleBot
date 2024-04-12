class traitementDonnees :

    def creationGrille(grille, data, Data): #métode pour creer un grillage et séparer les données
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
                

        return grille 
    

    def determinerMur(grille, data):
        # --- DÉTERMINE OÙ SONT LES MURS ---

        max = 0
        for i in range(len(grille)): # on parcours les colonnes |
            for j in range (len(grille[0])): # on parcours les lignes -
                if max < grille[i][j].quantite :
                    max = grille[i][j].quantite
        
        moyenne = len(data) / (len(grille)*len(grille[0]))
        # mediane = max / 2

        print ("moyenne : ", moyenne)
        print ("max : ", max)
        # print("médiane : ", mediane)

        limiteNiveau1 = moyenne
        limiteNiveau2 = max
        
        for i in range(len(grille)): # on parcours les colonnes |
            for j in range (len(grille[0])): # on parcours les lignes -
                if grille[i][j].quantite <= limiteNiveau2  and grille[i][j].quantite > limiteNiveau1:
                    grille[i][j].mur = 2
                else :
                    grille[i][j].mur = 1

        return grille

