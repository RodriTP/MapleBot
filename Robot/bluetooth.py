#!/usr/bin/env pybricks-micropython
from pybricks.messaging import BluetoothMailboxServer, Mailbox
from sensors import Sensors
from Drivebase import Drivebase
from autonomousMoving import AutonomousMoving
from Point2D import Point2D

class Bluetooth :
    server = BluetoothMailboxServer()
    mbox = Mailbox('greeting', server)
    # The server must be started before the client!
    print('waiting for connection...')
    server.wait_for_connection()
    print('connected!')
    
    lastWallSent = 0

    # In this program, the server waits for the client to send the first message
    # and then sends a reply.
    mbox.wait()
    print(mbox.read())
    mbox.send('hello to you!')

    def sendPositionAndSensor(self, s:Sensors, d:Drivebase):
        data = d._pos.__str__()
        data += ";UL:" + str(s.getLeftDistance())
        data += ";UR:" + str(s.getRightDistance())
        self.mbox.send(data)
        self.mbox.wait()
        print(data)

    def sendPositionAndWalls(self, d:Drivebase, a:AutonomousMoving):
        data = d._pos.__str__()
        if(len(a.points)-self.lastWallSent>0):
            print("dans la boucle")
            for i in range(len(a.points) - self.lastWallSent):
                pointTemp = a.points[self.lastWallSent + i]
                print(pointTemp)
                temp = Point2D(pointTemp[0]/1000, pointTemp[1]/1000)
                data += ";"+ temp.__str__()
        self.lastWallSent = len(a.points)
        self.mbox.send(data)
        #print("avant wait")
        self.mbox.wait()
        print(data)
        print("exited")
    
    def sendOtherData(self, text:str):
        self.mbox.send(text)
        self.mbox.wait()