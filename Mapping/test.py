#from bluetooth import Bluetooth
import sys
sys.path.append('Util')
from Point2D import RobotPose
from Convertions import Convertions
#b = Bluetooth()

print(RobotPose(0,0,0))
print(Convertions.radiansToDegrees(3.14))
#while True:
    #b.dataExchange()
 #   print(b.getData())
  #  b.resetData()
   # print("recieved")