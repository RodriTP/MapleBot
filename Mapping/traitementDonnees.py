from  CasesAutour import casesAutour

class traitementDonnees :
    # --- DÉFINITION DES LIMITES X ET Y POUR CHAQUE CASE ---
    def creationGrille(grille, data, Data): #métode pour creer un grillage et séparer les données

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
    

    # --- INSERTION DES DONNÉES DANS LA GRILLE EN FONCTION DES LIMITES QUI ONT ÉTÉ DEFINIS ---        
    def insertionDonnees(grille, data):
                     
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
    



    # --- MÉTHODES DÉDIÉS AUX MURS ---

   

    # def finMur(grille):
    #     nbMursAutour = 0
    #     for i in range(len(grille)): # on parcours les colonnes |
    #             for j in range (len(grille[0])): # on parcours les lignes -
    #                 if (grille[i][j].mur == True): # Si nous somme a une case ayant un mur
    #                     # on vérifie si au moins 2 des cases autour a un mur
    #                     if (grille[i-1][j-1].mur == True): #case en haut à gauche
    #                         nbMursAutour += 1
    #                     if (grille[i][j-1].mur == True): #case en haut
    #                         nbMursAutour += 1
    #                     if (grille[i+1][j-1].mur == True): #case en haut à droite
    #                         nbMursAutour += 1
    #                     if (grille[i-1][j].mur == True): #case à gauche
    #                         nbMursAutour += 1
    #                     if (grille[i+1][j].mur == True): #case à droite
    #                         nbMursAutour += 1
    #                     if (grille[i-1][j+1].mur == True): #case en bas à gauche
    #                         nbMursAutour += 1
    #                     if (grille[i][j+1].mur == True): #case en bas
    #                         nbMursAutour += 1
    #                     if (grille[i+1][j+1].mur == True): #case en bas à droite
    #                         nbMursAutour += 1
                        
    #                     if(nbMursAutour<2): #si chaque mur a moins d'un mur autour alors on retourne false
    #                         return False
                        
    #                     nbMursAutour = 0
    #     return True
                         

    # Détermine où sont les murs
    def determinerMur(grille):

        # Cette méthode sert à déterminer si chaque case ayant un mur a 2 case autour ayant un mur
        # Si ce n'est pas le cas alors il faudra continuer à chercher des murs
        # Return False -> tout les cases ayant un mur a 2 cases ayant un mur autour
        # Return True -> il y a au moins une case ayant un mur qui a moins de 2 cases ayant un mur autour
        def continuerMur(grille):
            for i in range(len(grille)): # on parcours les colonnes |
                    for j in range (len(grille[0])): # on parcours les lignes -
                        if (grille[i][j].mur == True): # Si nous somme a une case ayant un mur
                            if(nbMurs(grille, i, j)<2): #si chaque mur a moins d'un mur autour alors on retourne false
                                return True
                            
            return False
        
        def nbMurs(grille, i, j):
            nb = 0
            # on vérifie si au moins 2 des cases autour a un mur (tout en s'assurant de ne pas sortir de la grille)
            if (i-1>=0 and j-1>=0 and grille[i-1][j-1].mur == True): #case en haut à gauche
                nb += 1
            if ( j-1>=0 and grille[i][j-1].mur == True): #case en haut
                nb += 1
            if (i+1<len(grille) and j-1>=0 and grille[i+1][j-1].mur == True): #case en haut à droite
                nb += 1
            if (i-1>=0 and grille[i-1][j].mur == True): #case à gauche
                nb += 1
            if (i+1<len(grille) and grille[i+1][j].mur == True): #case à droite
                nb += 1
            if (i-1>=0 and j+1<len(grille[0]) and grille[i-1][j+1].mur == True): #case en bas à gauche
                nb += 1
            if (j+1 < len(grille[0]) and grille[i][j+1].mur == True): #case en bas
                nb += 1
            if (i+1<len(grille) and j+1<len(grille[0]) and grille[i+1][j+1].mur == True): #case en bas à droite
                nb += 1
            return nb
        
        maximum = 0
        posXPointeur = 0 #détermine la coordonée en X de la case sur laquelle on travaille
        posYPointeur = 0 #détermine la coordonée en Y de la case sur laquelle on travaille

        #On trouve d'abord la case qui a le plus de point et on commence de là
        for i in range(len(grille)): # on parcours les colonnes |
            for j in range (len(grille[0])): # on parcours les lignes -
                if maximum < grille[i][j].quantite :
                    maximum = grille[i][j].quantite
                    posXPointeur = i
                    posYPointeur = j
        

        grille[posXPointeur][posYPointeur].mur = True
        
        # on regarde les 2 case contenant le plus de données autour de la case de référence
        # ________________________________
        # | x-1, y-1 | x, y-1  | x+1, y-1 |
        # |__________|_________|__________|
        # | x-1, y   |  x, y   | x+1, y   |
        # |__________|_________|__________|
        # | x-1, y+1 | x, y+1  | x+1, y+1 |
        # |__________|_________|__________|
        # 
        # la case du milieu (x,y) sert de référence  


        #Liste avec toutes les cases autours de la case de référence
        casesAutourListe = [casesAutour() for i in range(8)]
        
        compteurFois = 0
        dernierPointeurX = 0
        dernierPointeurY = 0
        
        while continuerMur(grille) :
            #case en haut à gauche
            if (posXPointeur-1 >= 0 and posYPointeur-1 >= 0 and grille[posXPointeur-1][posYPointeur-1].mur == False):
                casesAutourListe[0].posX = posXPointeur-1
                casesAutourListe[0].posY = posYPointeur-1
                casesAutourListe[0].quantite = grille[posXPointeur-1][posYPointeur-1].quantite
            else :
                casesAutourListe[0].posX = 0
                casesAutourListe[0].posY = 0
                casesAutourListe[0].quantite = 0
            
                #case en haut
            if (posYPointeur-1 >= 0 and grille[posXPointeur][posYPointeur-1].mur == False):
                casesAutourListe[1].posX = posXPointeur
                casesAutourListe[1].posY = posYPointeur-1
                casesAutourListe[1].quantite = grille[posXPointeur][posYPointeur-1].quantite
            else :
                casesAutourListe[1].posX = 0
                casesAutourListe[1].posY = 0
                casesAutourListe[1].quantite = 0

                #case en haut à droite
            if (posXPointeur+1 < len(grille) and posYPointeur-1 >= 0 and grille[posXPointeur+1][posYPointeur-1].mur == False):
                casesAutourListe[2].posX = posXPointeur+1
                casesAutourListe[2].posY = posYPointeur-1
                casesAutourListe[2].quantite = grille[posXPointeur+1][posYPointeur-1].quantite
            else :
                casesAutourListe[2].posX = 0
                casesAutourListe[2].posY = 0
                casesAutourListe[2].quantite = 0

                #case à gauche
            if (posXPointeur-1 >= 0 and grille[posXPointeur-1][posYPointeur].mur == False):
                casesAutourListe[3].posX = posXPointeur-1
                casesAutourListe[3].posY = posYPointeur
                casesAutourListe[3].quantite = grille[posXPointeur-1][posYPointeur].quantite
            else :
                casesAutourListe[3].posX = 0
                casesAutourListe[3].posY = 0
                casesAutourListe[3].quantite = 0

                #case à droite
            if (posXPointeur+1 < len(grille) and grille[posXPointeur+1][posYPointeur].mur == False):
                casesAutourListe[4].posX = posXPointeur+1
                casesAutourListe[4].posY = posYPointeur
                casesAutourListe[4].quantite = grille[posXPointeur+1][posYPointeur].quantite
            else :
                casesAutourListe[4].posX = 0
                casesAutourListe[4].posY = 0
                casesAutourListe[4].quantite = 0

                #case en bas à gauche
            if (posXPointeur-1 >= 0 and posYPointeur+1 < len(grille[0]) and grille[posXPointeur-1][posYPointeur+1].mur == False):
                casesAutourListe[5].posX = posXPointeur-1
                casesAutourListe[5].posY = posYPointeur+1
                casesAutourListe[5].quantite = grille[posXPointeur-1][posYPointeur+1].quantite
            else :
                casesAutourListe[5].posX = 0
                casesAutourListe[5].posY = 0
                casesAutourListe[5].quantite = 0

                #case en bas
            if (posYPointeur+1 < len(grille[0]) and grille[posXPointeur][posYPointeur+1].mur == False):
                casesAutourListe[6].posX = posXPointeur
                casesAutourListe[6].posY = posYPointeur+1
                casesAutourListe[6].quantite = grille[posXPointeur][posYPointeur+1].quantite
            else :
                casesAutourListe[6].posX = 0
                casesAutourListe[6].posY = 0
                casesAutourListe[6].quantite = 0

                #case en bas à droite
            if (posXPointeur+1 < len(grille) and posYPointeur+1 < len(grille[0]) and grille[posXPointeur+1][posYPointeur+1].mur == False):
                casesAutourListe[7].posX = posXPointeur+1
                casesAutourListe[7].posY = posYPointeur+1
                casesAutourListe[7].quantite = grille[posXPointeur+1][posYPointeur+1].quantite
            else :
                casesAutourListe[7].posX = 0
                casesAutourListe[7].posY = 0
                casesAutourListe[7].quantite = 0

            mx = max(casesAutourListe[0].quantite, casesAutourListe[1].quantite, casesAutourListe[2].quantite, casesAutourListe[3].quantite, casesAutourListe[4].quantite, casesAutourListe[5].quantite, casesAutourListe[6].quantite, casesAutourListe[7].quantite) # case autour avec le max de données 
            
            for i in range(len(casesAutourListe)): #trouve la position de la case avec le max dans le tableau grille 
                if casesAutourListe[i].quantite == mx:
                    mx_pos = i

            #À ENLEVER
            #print("1: ",  casesAutourListe[0].quantite)
            # print("2: ",  casesAutourListe[1].quantite)
            # print("3: ",  casesAutourListe[2].quantite)
            # print("4: ",  casesAutourListe[3].quantite)
            # print("5: ",  casesAutourListe[4].quantite)
            # print("6: ",  casesAutourListe[5].quantite)
            # print("7: ",  casesAutourListe[6].quantite)
            # print("8: ",  casesAutourListe[7].quantite)

            grille[casesAutourListe[mx_pos].posX][casesAutourListe[mx_pos].posY].mur = True
        
            dernierPointeurX = posXPointeur
            dernierPointeurY = posYPointeur

            posXPointeur = casesAutourListe[mx_pos].posX
            posYPointeur = casesAutourListe[mx_pos].posY


            compteurFois += 1
            print(compteurFois)
            if (compteurFois == 10000):
                break
        
        return grille


