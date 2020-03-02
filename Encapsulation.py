class Car:
    def __init__(self):
        self.__updatesoftware()

    def drive(self):
        print("driving")

    def __updatesoftware(self):
        print("updating software")

redCar = Car()
redCar.drive()
