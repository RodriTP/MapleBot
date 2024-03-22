from Data import Data

class grilleSalle: #Classe du grillage pour que chaque case ait les variables suivantes
    mur = False #sert à déteminer s'il y a présence d'un mur
    dataGrille = [] #grillage
    quantite = 0  #la quantité de données dans chaque case

    #On commence la séparation en haut à gauche des données
    limiteSuppX = 0 #la valeur maximale en X acceptée dans la case
    limiteInfX = 0 #la valeur minimale en X acceptée dans la case
    limiteSuppY = Data.trouverMaxY(Data.data) #la valeur maximale en Y acceptée dans la case 
    limiteInfY = Data.trouverMaxY(Data.data) #la valeur minimale en Y acceptée dans la case