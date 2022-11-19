class CarNotEnoughFuel(Exception):
    def __init__(self, message="Not Enough Fuel"):
        Exception.__init__(self, message)


class CarNegativeDistance(Exception):
    def __init__(self, message="You Can't Break The Laws Of Physics"):
        Exception.__init__(self, message)


class Car:
    fuel = 20
    rate = 0.1
    traveled = 0

    def __init__(self, fuel=20, rate=0.1):
        self.fuel = fuel
        self.rate = rate


    def __str__(self):
        return f"Fuel = {self.fuel}\n " \
               f"Rate = {self.rate}\n " \
               f"Traveled = {self.traveled}"

    def drive(self, distance):
        if self.fuel < distance * self.rate:
            raise CarNotEnoughFuel("Not Enough Fuel")
        else:
            if distance < 0:
                raise CarNegativeDistance()
            else:
                self.traveled += distance
                self.fuel -= distance * self.rate


car1 = Car(30, 5)
print(car1)
try:
    car1.drive(-3)
except CarNotEnoughFuel:
    print("You Don't Have Enough Fuel")
except CarNegativeDistance:
    print("You Can't Travel Negative Distance")
print(car1)