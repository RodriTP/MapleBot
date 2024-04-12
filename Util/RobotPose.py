from Point2D import Point2D

class RobotPose(Point2D):
    """Classe modélisant la position (x,y,yaw) du robot par rapport à l'origine d'un plan"""
    _yaw = float(0)
    
    #x : x pose, y : y pose, orientation : angle of the gyro (meters, meters, degrees)
    def __init__(self, x: float, y: float, yaw : float):
        """
        Params
            x (float): coordonnée en x du point sur le plan
            y (float): coordonnée en y du point sur le plan
            yaw (float): rotation du robot par rapport au heading initial du robot
        """
        super().__init__(x, y)
        self._yaw = yaw
    
    def __str__(self):        
        """
        Return : (string) la valeur de x et y en mètres (m)
            Ex : "x:1.0;y:2.0;a:15.2" 
        """
        return super().__str__() + ";a:"+str(self._yaw)
    #returns degrees
    def getOrientation(self):
        """return : (float) yaw du robot"""
        return self._yaw
    
    def setOrientation(self, yaw : float):
        """
        Param
            yaw (float) : yaw du robot en degré
        """
        self._yaw = yaw
    
    def set(self, x: float, y: float, yaw : float):
        """
        Params
            x (float): coordonnée en x du point sur le plan
            y (float): coordonnée en y du point sur le plan
            yaw (float) : yaw du robot en degré
        """
        super().set(x, y)
        self._yaw = yaw