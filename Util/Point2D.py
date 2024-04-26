import math

class Point2D:
    """
    Classe modélisant un point 2D (x,y) par rapport à l'origine un plan
    """
    _x = float(0)
    _y = float(0)

    def __init__(self, x : float, y : float):
        """
        Params
            x (float): coordonnée en x du point sur le plan
            y (float): coordonnée en y du point sur le plan
        """
        self._x = x
        self._y = y
    
    def __str__(self):
        """
        Return : (string) la valeur de x et y en mètres (m)
            Ex : "x:1.0;y:2.0" 
        """
        return "x:" + str(self._x/1000) + ";y:" + str(self._y/1000)

    #getters: always return a float
    def getX(self):
        """Return : (float) valeur en x du point"""
        return self._x
    def getY(self):
        """Return : (float) valeur en y du point"""
        return self._y
    
    #setters
    def setX(self, x : float):
        """Params : (float) valeur en x du point"""
        self._x = x
    
    def setY(self, y : float):
        """Params : (float) valeur en y du point"""
        self._y = y
    
    def set(self, x : float, y : float):
        """
        Params
            x (float): coordonnée en x du point sur le plan
            y (float): coordonnée en y du point sur le plan
        """
        self._x = x
        self._y = y
