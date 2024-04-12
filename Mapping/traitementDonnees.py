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
        # | x-1, y   |  x, y   | x+1, j   |
        # |__________|_________|__________|
        # | x-1, y+1 | x, y+1  | x+1, j+1 |
        # |__________|_________|__________|
        # 
        # la case du milieu (x,y) sert de référence  

        casesAutour = [grille[posXPointeur-1][posYPointeur-1], #case en haut à gauche
                       grille[posXPointeur][posYPointeur-1], #case en haut
                       grille[posXPointeur+1][posYPointeur-1], #case en haut à droite
                       grille[posXPointeur-1][posYPointeur], #case à gauche
                       grille[posXPointeur+1][posYPointeur], #case à droite
                       grille[posXPointeur-1][posYPointeur+1], #case en bas à gauche
                       grille[posXPointeur][posYPointeur+1], #case en bas
                       grille[posXPointeur+1][posYPointeur+1] #case en bas à droite
                       ]


        liste = [casesAutour[0].quantite, 
                 casesAutour[1].quantite,
                 casesAutour[2].quantite,
                 casesAutour[3].quantite,
                 casesAutour[4].quantite,
                 casesAutour[5].quantite,
                 casesAutour[6].quantite,
                 casesAutour[7].quantite]
                
        # code pris d'en ligne : https://www.geeksforgeeks.org/python-program-to-find-second-largest-number-in-a-list/
        mx = max(liste[0], liste[1]) # case autour avec le max de donées 
        secondmax = min(liste[0], liste[1]) # case autour avec le 2e max de donées 
        mx_pos = 0  # Position du max
        secondmax_pos = 1 # Position du 2e max
        n = len(liste)
        for i in range(2,n): 
            if liste[i] > mx: 
                secondmax = mx
                secondmax_pos = mx_pos
                mx = liste[i] 
            elif liste[i] > secondmax and \
                mx != liste[i]: 
                secondmax = liste[i]
                secondmax_pos = i
            elif mx == secondmax and \
                secondmax != liste[i]:
                secondmax = liste[i]
                secondmax_pos = i
    
        for i in range(len(liste)):
            if liste[i] == mx:
                mx_pos = i
        
        casesAutour[mx_pos].mur = True
        casesAutour[secondmax_pos].mur = True

        if (mx_pos == 0):
            posXPointeur = posXPointeur-1
            posYPointeur = posYPointeur-1
        elif (mx_pos == 1):
            posXPointeur = posXPointeur
            posYPointeur = posYPointeur-1
        elif (mx_pos == 2):
            posXPointeur = posXPointeur+1
            posYPointeur = posYPointeur-1
        elif (mx_pos == 3):
            posXPointeur = posXPointeur-1
            posYPointeur = posYPointeur
        elif (mx_pos == 4):
            posXPointeur = posXPointeur+1
            posYPointeur = posYPointeur
        elif (mx_pos == 5):
            posXPointeur = posXPointeur-1
            posYPointeur = posYPointeur+1
        elif (mx_pos == 6):
            posXPointeur = posXPointeur
            posYPointeur = posYPointeur+1
        elif (mx_pos == 7):
            posXPointeur = posXPointeur+1
            posYPointeur = posYPointeur+1



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

