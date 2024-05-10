from Point2D import Point2D

def estEntreVals(self, point1 : Point2D, point2 : Point2D, range  : float):
        """
        Vérifie si deux points sont égaux selon une certaine marge d'erreur\n
        Params 
            point1 (Point2D) : premier point qu'on veut comparer\n
            point2 (Point2D) : deuxième point qu'on veux comparer\n
            range (float) : marge d'erreur accepté
        """

        if(point1.getX() > point2.getX() - self._RANGE and point1.getX() < point2.getX() + range
           and point1.getY() > point2.getY() - self._RANGE and point1.getY() < point2.getY() + range):
            return True
        else : 
            return False

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
            (facultatif) dir (float) : orientation vers où le point fait face (angle en degré)
        """
        print(args)
        if len(args) == 2:
            self.setX(args[0])
            self.setY(args[1])
        
        if len(args) == 3:
            self.setX(args[0])
            self.setY(args[1])
            self.setDir(args[2])
    
    def __str__(self):
        """
        Return : (string) la valeur de x et y en mètres (m)
            Ex : "x:1.0;y:2.0" 
        """
        return "x:" + str(self._x/1000) + ";y:" + str(self._y/1000)

    #getters: always return a float
    def getX(self) -> float:
        """Return : (float) valeur en x du point"""
        return self._x
    def getY(self) -> float:
        """Return : (float) valeur en y du point"""
        return self._y
    def getDir(self) -> float:
        """return : (float) direction où le point fait face (angle en degré)"""
        return self._dir
    
    #setters
    def setX(self, x : float):
        """Params : (float) valeur en x du point"""
        self._x = x
    
    def setY(self, y : float):
        """Params : (float) valeur en y du point"""
        self._y = y
    def setDir(self, dir : float):
        """Params : (float) direction où le point fait face (angle en degré)"""
        self._dir = dir

    def set(self, x : float, y : float, dir = None):
        """
        Params
            x (float): coordonnée en x du point sur le plan
            y (float): coordonnée en y du point sur le plan
            dir (float) : direction vers où le point fait face (angle en degré)
        """
        self._x = x
        self._y = y
        self._dir = dir

    def deltaX(self, autrePt : Point2D) -> float:
        """
        Calcule la différence en x avec un autre point (autrePt).\n
        Formule : X de pointActuel - X de autrePt\n
        Param
            autrePt (float) : Point avec lequel on veut calculer la différence de x
        """
        return self._x - autrePt._x
    
    def deltaY(self, autrePt : Point2D) -> float:
        """
        Calcule la différence en Y avec un autre point (autrePt).\n
        Formule : Y de pointActuel - Y de autrePt\n
        Param
            autrePt (float) : Point avec lequel on veut calculer la différence de Y
        """
        return self._y - autrePt._y
    
    def deltaDir(self, autrePt : Point2D) -> float:
        """
        Calcule la différence d'angle entre la direction du point avec la direction d'un autre point (autrePt).\n
        Formule : angle de pointActuel - angle de autrePt\n
        Param
            autrePt (float) : Point avec lequel on veut calculer la différence d'angle (en degré)
        """
        if self._dir == None or autrePt._dir == None :
            print("Impossible de calculer la différence d'angle entre les directions des points. La direction d'un des points est nulle")
            return 0.0
        else :
            return self._dir - autrePt._dir