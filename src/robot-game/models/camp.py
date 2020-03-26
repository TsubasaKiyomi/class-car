from .RobotModel import Robot


class Dog(Robot):
    def bark(self):
        print("bark")


class Cat(Robot):
    def crows(self):
        print("crows")


class Human(Robot):
    def bipedal_walking(self):
        print("bipedal_walking")
