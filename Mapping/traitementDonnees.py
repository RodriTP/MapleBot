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
    

    # --- DÉTERMINE OÙ SONT LES MURS ---
    def determinerMur(grille, data):
        
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

        
        #case en haut à gauche
        casesAutourListe[0].posX = posXPointeur-1
        casesAutourListe[0].posY = posYPointeur-1
        casesAutourListe[0].quantite = grille[posXPointeur-1][posYPointeur-1].quantite

        #case en haut
        casesAutourListe[1].posX = posXPointeur
        casesAutourListe[1].posY = posYPointeur-1
        casesAutourListe[1].quantite = grille[posXPointeur][posYPointeur-1].quantite

        #case en haut à droite
        casesAutourListe[2].posX = posXPointeur+1
        casesAutourListe[2].posY = posYPointeur-1
        casesAutourListe[2].quantite = grille[posXPointeur+1][posYPointeur-1].quantite

        #case à gauche
        casesAutourListe[3].posX = posXPointeur-1
        casesAutourListe[3].posY = posYPointeur
        casesAutourListe[3].quantite = grille[posXPointeur-1][posYPointeur].quantite

        #case à droite
        casesAutourListe[4].posX = posXPointeur+1
        casesAutourListe[4].posY = posYPointeur
        casesAutourListe[4].quantite = grille[posXPointeur+1][posYPointeur].quantite

        #case en bas à gauche
        casesAutourListe[5].posX = posXPointeur-1
        casesAutourListe[5].posY = posYPointeur+1
        casesAutourListe[5].quantite = grille[posXPointeur-1][posYPointeur+1].quantite

        #case en bas
        casesAutourListe[6].posX = posXPointeur
        casesAutourListe[6].posY = posYPointeur+1
        casesAutourListe[6].quantite = grille[posXPointeur][posYPointeur+1].quantite

        #case en bas à droite
        casesAutourListe[7].posX = posXPointeur+1
        casesAutourListe[7].posY = posYPointeur+1
        casesAutourListe[7].quantite = grille[posXPointeur+1][posYPointeur+1].quantite


        # code pris d'en ligne : https://www.geeksforgeeks.org/python-program-to-find-second-largest-number-in-a-list/
        mx = max(casesAutourListe[0].quantite, casesAutourListe[1].quantite) # case autour avec le max de donées 
        secondmax = min(casesAutourListe[0].quantite, casesAutourListe[1].quantite) # case autour avec le 2e max de donées 
        mx_pos = 0  # Position du max
        secondmax_pos = 1 # Position du 2e max
        n = len(casesAutourListe)
        for i in range(2,n): 
            if casesAutourListe[i].quantite > mx: 
                secondmax = mx
                secondmax_pos = mx_pos
                mx = casesAutourListe[i].quantite
            elif casesAutourListe[i].quantite > secondmax and mx != casesAutourListe[i].quantite: 
                secondmax = casesAutourListe[i].quantite
                secondmax_pos = i
            elif mx == secondmax and secondmax != casesAutourListe[i].quantite:
                secondmax = casesAutourListe[i].quantite
                secondmax_pos = i
        #fin du code pris en ligne
         
        for i in range(len(casesAutourListe)): #trouve la position de la case avec le max dans le tableau grille 
            if casesAutourListe[i].quantite == mx:
                mx_pos = i

       
        grille[casesAutourListe[mx_pos].posX][casesAutourListe[mx_pos].posY].mur = True
        grille[casesAutourListe[secondmax_pos].posX][casesAutourListe[secondmax_pos].posY].mur = True
    
        posXPointeur = casesAutourListe[mx_pos].posX
        posYPointeur = casesAutourListe[mx_pos].posY




        #À ENLEVER
        print("Second highest number is : ",\
            str(secondmax))
        
        print("Second Highest number position is : ",\
            str(secondmax_pos))
        
        print("Highest number is : ",\
            str(mx))
         
        print("Highest number pos  is : ",\
            str(mx_pos))
        
        return grille
    
    #def finMur(grille):


