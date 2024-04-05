import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from  GrilleSalle import grilleSalle
##################Début classe mainTraitementDonnees (sert de main) #######################
#### creer une grille la remplis avec la date et affiche la grille (modifier ce commentaire si mauvaise description)
_x = []
_y = []
fig, ax = plt.subplots()
class mainTraitementDonnees :

    def __init__(self):
        return
    
    def ajouterPoint(self, x:float, y:float):
        global _x
        global _y
        _x.append(x)
        _y.append(y)

    def update(frame):
        global ax
        global fig
        global _x
        global _y
        ax.clear()  # clearing the axes
        ax.scatter(_x, _y)  # creating new scatter chart with updated data
        fig.canvas.draw()  # forcing the artist to redraw itself


"""
    def afficherGrille(self):
        plt.scatter(x,y) # Ajoute le nuage de point, c-à-d les données que le robot à collecter, au plot 

        #stats = linregress(data[:][0], data[:][1]) # Régression linéaire

        #plt.xlim([0, 25])
        #plt.ylim([10, 15])

        plt.show() # afficher le tout
"""
######################################################################