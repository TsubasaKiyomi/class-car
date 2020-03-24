class Clothes():
    def wear(self):
        print("wear")


class Lower_body(Clothes):
    def pants(self):
        print("pants")


class Foot(Clothes):
    def socks(self):
        print("socks")


class Outerwear(Clothes):
    def outet(self):
        print("outer")


class Neck(Clothes):
    def muffler(self):
        print("muffler")


class Hand(Clothes):
    def gloves(self):
        print("gloves")


lower_body = Lower_body()
# lower_body.wear()
lower_body.pants()

foot = Foot()
# foot.wear()
foot.socks()

outerwear = Outerwear()
# outerwear.wear()
outerwear.outet()

neck = Neck()
# neck.wear()
neck.muffler()

hand = Hand()
# hand.wear()
hand.gloves()
