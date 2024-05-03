#!/usr/bin/env python3
from pcPybricks.messaging import BluetoothMailboxClient, TextMailbox


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

class connexionBluetooth:
    #Données qui seront reçues et envoyés
    dataToSend = []
    dataRecieved = []

    #L'adresse bluetooth du EV3
    SERVER = "00:17:ec:f4:9d:c8"
    #Initilisation de la connection Bluetooth
    client = BluetoothMailboxClient()
    mbox = TextMailbox("greeting", client)

    def __init__(self):
        print("establishing connection...")
        self.client.connect(self.SERVER)
        print("connected!")

        # In this program, the client sends the first message and then waits for the
        # server to reply.
        #Envoie de message
        self.mbox.send("hello!")
        self.mbox.wait()
        #exemple de truc à recevoir
        print(self.mbox.read())

    #L'échange de donnés qui doit se faire tout le temps
    def dataExchange(self):
        self.mbox.wait()
        print("gay")
        self.dataRecieved.append(self.mbox.read())
        #if(len(self.dataToSend)==0):
        #    self.mbox.send('NULL')
        #    print("send return")
        #else:
        self.mbox.send("NULL")
        #    print("WHYYYYYYY")
        print("send return")

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
        return self.dataRecieved[0].split(";")
    #prend ce que reçois l'ordi (x:200.2902) pour le séparer pour juste avoir 200.2902
    def getNumData(data : str):
        return float(data.split(":")[1])