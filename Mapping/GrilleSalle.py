from Data import Data

class grilleSalle: #Classe du grillage pour que chaque case ait les variables suivantes
    def __init__(self):
        self.mur = False #sert à déteminer s'il y a présence d'un mur
        self.dataGrille = [] #grillage
        self.quantite = 0  #la quantité de données dans chaque case

        #On commence la séparation en haut à gauche des données
        self.limiteSuppX = 0 #la valeur maximale en X acceptée dans la case
        self.limiteInfX = 0 #la valeur minimale en X acceptée dans la case
        self.limiteSuppY = Data.trouverMaxY(Data.data) #la valeur maximale en Y acceptée dans la case 
        self.limiteInfY = Data.trouverMaxY(Data.data) #la valeur minimale en Y acceptée dans la case

    # def set_limiteSuppX (self,valeur):
    #     self.limiteSuppX = valeur

    # def set_limiteInfX (self,valeur):
    #     self.limiteInfX = valeur

    # def set_limiteSuppY (self,valeur):
    #     self.limiteSuppY = valeur

    # def set_limiteInfY (self,valeur):
    #     self.limiteInfY = valeur