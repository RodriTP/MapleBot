#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from drivebase import Drivebase
from sensors import Sensors

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
s = Sensors()
d = Drivebase()
d._init_()
# Write your program here.

#d.setSpeed(200)
#20.6  2 rotations
#9.745    1 rotation
#40.4  10 rotations
#d.turn(90, 100)
#d.turn(-180, 100)
d.moveAuto(s)
while True:
    s.update()
    
    #print(d._kGyro.angle())
    #d._kLeftMotor.run(200)
    #d._kRightMotor.run(-200)
    #if d._kLeftMotor.angle() >= 360*float(9.745):
    #    d.stop()