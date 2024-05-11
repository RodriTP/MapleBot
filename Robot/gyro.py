#ev3 imports
from pybricks.parameters import Port, Color, Button, Direction, Stop

#gyro imports
from pybricks.iodevices import DCMotor, UARTDevice, LUMPDevice, I2CDevice
from pybricks.iodevices import I2CDevice
from pybricks.iodevices import UARTDevice
#others import
import _thread
 
class Gyro :
    """
    Classe qui sert à lire les valeurs du gyro.\n
    Gyro est un singleton pour éviter de faire planter le gyroscope physique\n
    en créant multiples instances de celui-ci.
    """
    _angle = 0.0
    _gyroOffset = None

    ser = UARTDevice(Port.S2, baudrate=9600, timeout=None)
    line = []
    c='a'

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Gyro, cls).__new__(cls)
        return cls.instance
    
    def __init__(self) -> None:
        pass

    def periodic(self):
        """
        Mettre ici les fonctions de gyro qui doivent être loop infiniment.\n
        Cette fonction va être appelé dans une boucle infinie dans le main (while True)
        """
        self.getDegrés()

    def getDegrés(self):
        """
        Permet d'obtenir la rotation du gyro en degrés\n
            Si le gyro crash, returne 0 et affiche un message d'erreur
        
        Return : [0,360[ degré(s) en sens horaire
        """
        #print("in the loop (Gyro)")
        line = []
        bool = True
        while bool == True: 
            try :
                for self.c in self.ser.read(1):
                    if (chr(self.c) != '\n') and (chr(self.c) != '\r'):
                        line.append(chr(self.c))
                    if chr(self.c) == '\n':
                        strline=''.join(str(v) for v in line) 
                        #print("line : "+strline)
                        line = []
                        bool = False
                        if self._gyroOffset == None:
                            self._gyroOffset = float(strline)
                            print("gyro offset : "+str(self._gyroOffset))
                        else :
                            #print("angle : "+str((float(strline)-self._gyroOffset)%float(360)))
                            Gyro._angle = (float(strline)-self._gyroOffset)%float(360)
            except :
                print("Erreur, à lu : "+str(strline))
                return float(0)
