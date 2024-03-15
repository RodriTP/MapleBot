#!/usr/bin/env python3
from pybricks.messaging import BluetoothMailboxClient, TextMailbox

# This demo makes your PC talk to an EV3 over Bluetooth.
#
# This is identical to the EV3 client example in ../bluetooth_client
#
# The only difference is that it runs in Python3 on your computer, thanks to
# the Python3 implementation of the messaging module that is included here.
# As far as the EV3 is concerned, it thinks it just talks to an EV3 client.
#
# So, the EV3 server example needs no further modifications. The connection
# procedure is also the same as documented in the messaging module docs:
# https://docs.pybricks.com/en/latest/messaging.html
#
# So, turn Bluetooth on on your PC and the EV3. You may need to make Bluetooth
# visible on the EV3. You can skip pairing if you already know the EV3 address.

# This is the address of the server EV3 we are connecting to.

class Bluetooth:
    #Données qui seront reçues et envoyés
    dataToSend = []
    dataRecieved = []

    #L'adresse bluetooth du EV3
    SERVER = "00:17:ec:f4:9d:c8"

    #Initilisation de la connection Bluetooth
    client = BluetoothMailboxClient()
    mbox = TextMailbox("greeting", client)

    print("establishing connection...")
    client.connect(SERVER)
    print("connected!")

    # In this program, the client sends the first message and then waits for the
    # server to reply.
    #Envoie de message
    mbox.send("hello!")
    mbox.wait()
    #exemple de truc à recevoir
    print(mbox.read())

    #L'échange de donnés qui doit se faire tout le temps
    def dataExchange(self):
        self.mbox.wait()
        self.dataRecieved.append(self.mbox.read())
        if(len(self.dataToSend)==0):
            self.mbox.send('0')
        else:
            self.mbox.send(dataToSend[0])
        
    #Ajoute des données qui vont être transmises
    def addDataToSend(self, dataToSend):
        self.dataToSend.append(dataToSend)
    
    #Retourne toutes les données obtenues
    def getData(self):
        return self.dataRecieved
    
    #Reset les données obtenues, à faire après les getter
    def resetData(self):
        self.dataRecieved.clear()

    def separateData(self):
        return self.dataRecieved[0].split(",")