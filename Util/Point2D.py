import math

class Point2D:
    _x = float(0)
    _y = float(0)

    def __init__(self, x : float, y : float):
        self._x = x
        self._y = y
    
    def __str__(self):
        return "x:" + str(self._x/1000) + ";y:" + str(self._y/1000) #x et y en metres

    #getters: always return a float
    def getX(self):
        return self._x
    def getY(self):
        return self._y
    
    #setters
    def setX(self, x : float):
        self._x = x
    def setY(self, y : float):
        self._y = y
    def set(self, x : float, y : float):
        self._x = x
        self._y = y
