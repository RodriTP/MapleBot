from ConnexionBluetooth import connexionBluetooth

b = connexionBluetooth()

while True:
    b.dataExchange()
    #print(b.getData())
    print(b.separateData(b.getData))
    #b.resetData()
    #print("recieved")