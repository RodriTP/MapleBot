#ev3 imports
from pybricks.parameters import Port, Color, Button, Direction, Stop

#gyro imports
from pybricks.iodevices import DCMotor, UARTDevice, LUMPDevice, I2CDevice
from pybricks.iodevices import I2CDevice
from pybricks.iodevices import UARTDevice
#others import
import _thread

# Initialize sensor port 2 as a uart device
# https://pybricks.com/ev3-micropython/iodevices.html#uart-device
#  class UARTDevice(port, baudrate, timeout=None(ms))
ser = UARTDevice(Port.S2, baudrate=9600, timeout=None)
line = []
# Write some data
#ser.write(b'\r\nHello, world!\r\n')

# Play a sound while we wait for some data
# for i in range(3):
# #    ev3.speaker.play_file(SoundFile.HELLO)
# #    ev3.speaker.play_file(SoundFile.GOOD)
# #    ev3.speaker.play_file(SoundFile.MORNING)
#     print("Bytes waiting to be read:", ser.waiting())

# Read all data received while the sound was playing
c='a'
# while True:
#     # data = ser.read_all()

# # read until we see the "newLine" character and print the line
#     for c in ser.read(1):
#         if (chr(c) != '\n') and (chr(c) != '\r'):
#             line.append(chr(c))
#         if chr(c) == '\n':
#             strline=''.join(str(v) for v in line)
#             # print(''.join(str(v) for v in line))
#             # print(line)
            
#             heading = float(strline)
#             print(heading)
#             # print(heading + 400)
#             line = []
#             break    
#     # print(c)
 
class Gyro :
    _angle = 0.0
    _gyroOffset = None

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
        self.degrés()

    def getDegrés(self):
        """
        Permet d'obtenir la rotation du gyro en degrés\n
            Si le gyro crash, returne 0 et affiche un message d'erreur
        
        Return : [0,360[ degré(s)
        """
        #print("in the loop (Gyro)")
        line = []
        bool = True
        while bool == True: 
            try :
                for c in ser.read(1):
                    if (chr(c) != '\n') and (chr(c) != '\r'):
                        line.append(chr(c))
                    if chr(c) == '\n':
                        strline=''.join(str(v) for v in line) 
                        #print(strline)
                        line = []
                        bool = False
                        if self._gyroOffset == None:
                            self._gyroOffset = float(strline)
                            return self._gyroOffset
                        else :
                            self._angle = (float(strline)-self._gyroOffset)%float(360)
            except :
                print("Erreur, à lu : "+str(strline))
                return float(0)
