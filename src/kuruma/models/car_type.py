from .car import Car


class ToyotaCar(Car):
    pass


class NissanCar(Car):
    def aut_run(self):
        print("aut_run")


class SuzukiCar(Car):
    def conpact_car(self):
        print("conpact_car")
