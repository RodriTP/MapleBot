from bluetooth import Bluetooth

b = Bluetooth()

while True:
    b.dataExchange()
    print(b.getData())
    b.resetData()