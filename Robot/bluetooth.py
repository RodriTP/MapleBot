#!/usr/bin/env pybricks-micropython
from pybricks.messaging import BluetoothMailboxServer, Mailbox
from sensors import Sensors
from Drivebase import Drivebase

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

    def sendPositionAndSensor(self, s:Sensors, d:Drivebase):
        data = d._pos.__str__()
        data += ";UL:" + str(s.getLeftDistance())
        data += ";UR:" + str(s.getRightDistance())
        self.mbox.send(data)
        self.mbox.wait()
        print(data)
    
    def sendOtherData(self, text:str):
        self.mbox.send(text)
        self.mbox.wait()