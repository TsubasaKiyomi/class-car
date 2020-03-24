class Car(object):
    def run(self):
        print("run")


class ToyotaCar(Car):
    pass


class NissanCar(Car):
    def aut_run(self):
        print("aut_run")


class SuzukiCar(Car):
    def conpact_car(self):
        print("conpact_car")


car = Car()
car.run

toyota_car = ToyotaCar()
toyota_car.run()

nissan_car = NissanCar()
nissan_car.run()
nissan_car.aut_run()

suzuki_car = SuzukiCar()
suzuki_car.run()
suzuki_car.conpact_car()
