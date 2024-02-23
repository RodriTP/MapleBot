#!/usr/bin/env pybricks-micropython
from pybricks.messaging import BluetoothMailboxServer, Mailbox
from sensors import Sensors

class Bluetooth :
    s = Sensors()

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