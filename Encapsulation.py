class Car:
    def __init__(self):
        self.__updatesoftware()

    def drive(self):
        print("driving")

    def __updatesoftware(self):
        print("updating software")

# The following is an object created outside the class
redCar = Car()
redCar.drive()

# The first method is private
# The second method is public and the last method is private
# Note that if you call a private method outside the class for example redCar.__updatesoftware() then an error will show
