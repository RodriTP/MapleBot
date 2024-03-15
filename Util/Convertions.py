import math

class Convertions :
    def degreesToRadians(degrees : float):
        return degrees*(math.pi/float(180))
    
    def radiansToDegrees(radians : float):
        return radians*(float(180/math.pi))
