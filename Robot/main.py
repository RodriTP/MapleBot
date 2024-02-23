#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import BluetoothMailboxServer, TextMailbox
from drivebase import Drivebase
from sensors import Sensors

ev3 = EV3Brick()

server = BluetoothMailboxServer()
mbox = TextMailbox('greeting', server)

d = Drivebase()
d._init_()
# Write your program here.
#ev3.speaker.beep()

# The server must be started before the client!
print('waiting for connection...')
server.wait_for_connection()
print('connected!')

# In this program, the server waits for the client to send the first message
# and then sends a reply.
mbox.wait()
print(mbox.read())
mbox.send('hello to you!')

#d.setSpeed(200)
#20.6  2 rotations
#9.745    1 rotation
#40.4  10 rotations
#d.turn(90, 100)
#d.turn(-180, 100)

while True:
    b.sendSensorData()
    #print(d._kGyro.angle())
    #d._kLeftMotor.run(200)
    #d._kRightMotor.run(-200)
    #if d._kLeftMotor.angle() >= 360*float(9.745):
    #d.stop()