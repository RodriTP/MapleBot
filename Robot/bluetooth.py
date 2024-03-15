#!/usr/bin/env pybricks-micropython
from pybricks.messaging import BluetoothMailboxServer, Mailbox
from sensors import Sensors
from drivebase import Drivebase

class Bluetooth :
    server = BluetoothMailboxServer()
    mbox = Mailbox('greeting', server)
    # The server must be started before the client!
    print('waiting for connection...')
    server.wait_for_connection()
    print('connected!')

    # In this program, the server waits for the client to send the first message
    # and then sends a reply.
    mbox.wait()
    print(mbox.read())
    mbox.send('hello to you!')

    def sendPositionAndSensor(self, s:Sensors, b:Drivebase):
        #Position X et Y du robot dans un string (en attente de l'odométrie)
        #data += "x" + str(d.positionX)
        #data += ",y" + str(d.positionY)
        data = " , "
        data += ",G" + str(s.degrés)
        data += ",UL" + str(s.getLeftDistance)
        data += ",UR" + str(s.getRightDistance)

    def sendSensorData(self):
        self.mbox.send('U1:' + str(self.s.getLeftDistance()))
        self.mbox.wait()
        self.mbox.send('U2 :' + str(self.s.getRightDistance()))
        self.mbox.wait()
        self.mbox.send('IR:' + str(self.s.getFrontDistance()))
        self.mbox.wait()
    
    def sendOtherData(self, text:str):
        self.mbox.send(text)
        self.mbox.wait()