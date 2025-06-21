class Vehical:
    def start(self):
        print("Vehcal is starting")

class Car(Vehical):
    def start(self):
        print ("Car is starting")

v1=Vehical()
v1.start()

c1=Car()
c1.start() 