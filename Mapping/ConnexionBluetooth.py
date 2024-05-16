#!/usr/bin/env python3
from pcPybricks.messaging import BluetoothMailboxClient, TextMailbox

#L'exemple parlé ci-dessous a été grandement modifié pour pouvoir fonctionner pour ce qu'on veuille faire

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
    """
    Objet qui gère et effectue l'envoie et la réception de données avec le ev3
    Utilise le Bluetooth comme moyen de communication
    """
    #Données qui seront reçues et envoyés
    dataToSend = []
    dataRecieved = []

    #L'adresse bluetooth du EV3
    SERVER = "00:17:ec:f4:9d:c8"

    #Initialisation des classes nécessaires pour créer la connexion
    client = BluetoothMailboxClient()
    mbox = TextMailbox("greeting", client)

    def __init__(self):
        """
        Initialise la connexion Bluetooth au robot
        """
        print("établissement connexion...")
        self.client.connect(self.SERVER)
        print("connecté!")

        # Au début, l'ordinateur envoie un message et attend la réponse du ev3
        self.mbox.send("bonjour!")
        self.mbox.wait()
        #exemple de truc à recevoir
        print(self.mbox.read())

    nombreDechangeBluetooth = 1

    #L'échange de donnés qui doit se faire tout le temps
    def dataExchange(self):
        self.mbox.wait()
        self.dataRecieved.append(self.mbox.read())
        if(len(self.dataToSend)==0):
            self.mbox.send('NULL'+ str(connexionBluetooth.nombreDechangeBluetooth))
        else:
            self.mbox.send(self.dataToSend)
            self.addDataToSend.clear()
        connexionBluetooth.nombreDechangeBluetooth +=1

    def addDataToSend(self, dataToSend):
        """
        Ajoute des données qui vont être transmises au robot
        """
        self.dataToSend.append(dataToSend)
    
    def getData(self):
        """
        Retourne toutes les données obtenues dans l'échange
        """
        return self.dataRecieved
    
    def resetData(self):
        """
        Reset les données obtenues, à faire après les getter
        """
        self.dataRecieved.clear()

    def separateData(self):
        """
        Sépare une ligne de donnée reçue dans un tableau séparér en case pour le cas général (x, y, angle, autre)
        Le cas spécifique est soit (x, y, angle, xMur, yMur, xMur, yMur,...) ou (x, y, angle, distance mur droite, distance mur gauche)
        Retourne le tableau avec les données
        """
        tableauTemporaire = self.dataRecieved[0].split(";")
        self.dataRecieved.remove(0)
        return self.dataRecieved[0]
    
    def getNumData(data : str):
        """
        prend ce que reçois l'ordi (x:200.2902) pour le séparer pour juste avoir 200.2902
        """
        return float(data.split(":")[1])