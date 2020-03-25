import random


class Fukubiki:
    def garagara(self):
        return random.randint(1, 10)

    num = random.randint(1, 10)
    if num == 1:
        print("特賞")

    elif num == 2:
        print("副賞")
    else:
        print("残念")


atare = Fukubiki()
print(atare.garagara())
