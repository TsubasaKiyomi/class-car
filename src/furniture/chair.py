class Sofa():
    def __init__(self, size, color, type):
        self.size = size
        self.color = color
        self.type = type

    def print_data(self):
        print("{}人掛けのソファーです。色は{}です。{}です。".format(
            self.size, self.color, self.type))
