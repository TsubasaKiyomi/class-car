from .wear import Wear


class Shoes(Wear):
    def __init__(self, name, color, size, shoes, sho_size):
        super().__init__(name, color, size)
        self.shoes = shoes
        self.sho_size = sho_size

    def print_deta(self):
        print("ウェアのメーカーは{}です。色は{}で、サイズは{}です。シューズは、{}色で、サイズは{}cmです。".format(
            self.name, self.color, self.size, self.shoes, self.sho_size))
