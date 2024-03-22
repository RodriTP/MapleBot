from Point2D import Point2D

class RobotPose(Point2D):
    _orientation = float(0)
    
    #x : x pose, y : y pose, orientation : angle of the gyro (meters, meters, degrees)
    def __init__(self, x: float, y: float, orientation : float):
        super().__init__(x, y)
        self._orientation = orientation
    
    def __str__(self):
        return super().__str__() + ";a:"+str(self._orientation)
    #returns degrees
    def getOrientation(self):
        return self._orientation
    
    def setOrientation(self, orientation : float):
        self._orientation = orientation
    
    def set(self, x: float, y: float, orientation : float):
        super().set(x, y)
        self._orientation = orientation