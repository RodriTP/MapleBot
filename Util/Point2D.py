import math

class Point2D:
    _x = float(0)
    _y = float(0)

    def __init__(self, x : float, y : float):
        self._x = x
        self._y = y
    
    def __str__(self):
        return "x:{self._x};y:{self._y}"

    #getters: always return a float
    def getX(self):
        return self._x
    def getY(self):
        return self._y
    
    #setters
    def setX(self, x : float):
        self._x = x
    def getY(self, y : float):
        self._y = y
    def set(self, x : float, y : float):
        self._x = x
        self._y = y

class RobotPose(Point2D):
    _orientation = float(0)
    
    #x : x pose, y : y pose, orientation : angle of the gyro
    def __init__(self, x: float, y: float, orientation : float):
        super().__init__(x, y)
        self._orientation = orientation
    
    def __str__(self):
        return super().__str__() + self._orientation
    
    def getOrientation(self):
        return self._orientation
    
    def setOrientation(self, orientation : float):
        self._orientation = orientation
    
    def set(self, x: float, y: float, orientation : float):
        super().set(x, y)
        self._orientation = orientation