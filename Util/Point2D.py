import math

class Point2D:
    """
    Classe modélisant un point 2D (x,y) par rapport à l'origine un plan
    """
    _x = float(0)
    _y = float(0)
    _dir = float(0)

    def __init__(self, *args):
        """
        Params
            x (float): coordonnée en x du point sur le plan
            y (float): coordonnée en y du point sur le plan
            (facultatif) dir (float) : orientation vers où le point fait face
        """
        if len(args) == 2:
            self.set(args[0], args[1])
        
        if len(args) == 3:
            self.set(args[0], args[1], args[2])
    
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
    def getDir(self):
        """return : (float) direction où le point fait face"""
        return self._dir
    
    #setters
    def setX(self, x : float):
        """Params : (float) valeur en x du point"""
        self._x = x
    
    def setY(self, y : float):
        """Params : (float) valeur en y du point"""
        self._y = y
    def setDir(self, dir : float):
        """Params : (float) direction où le point fait face"""
        self._dir = dir

    def set(self, x : float, y : float, dir = None):
        """
        Params
            x (float): coordonnée en x du point sur le plan
            y (float): coordonnée en y du point sur le plan
            dir (float) : orientation vers où le point fait face
        """
        self._x = x
        self._y = y
        self._dir = dir
