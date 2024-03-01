from bluetooth import Bluetooth

b = Bluetooth()

while True:
    b.dataExchange()
    b.dataExchange()
    b.dataExchange()
    print(b.getData())
    b.resetData()