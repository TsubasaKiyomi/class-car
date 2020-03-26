from .haori import Clothes


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
