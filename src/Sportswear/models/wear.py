class Wear():
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

    def print_deta(self):
        print("ウェアのメーカーは{}です。色は{}で、サイズは{}です。".format(
            self.name, self.color, self.size))
