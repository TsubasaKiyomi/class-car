class Robot():
    def arm(self):
        print("arm")


class Dog(Robot):
    def bark(self):
        print("bark")


class Cat(Robot):
    def crows(self):
        print("crows")


class Human(Robot):
    def bipedal_walking(self):
        print("bipedal_walking")


dog = Dog()
dog.arm()
dog.bark()

cat = Cat()
cat.arm()
cat.crows()

human = Human()
human.arm()
human.bipedal_walking()
