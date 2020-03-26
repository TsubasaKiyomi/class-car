from models.car_type import Car
from models.car_type import ToyotaCar
from models.car_type import NissanCar
from models.car_type import SuzukiCar


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
