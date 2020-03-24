class Sofa():
    def __init__(self, size, color, type):
        self.size = size
        self.color = color
        self.type = type

    def print_data(self):
        print("{}人掛けのソファーです。色は{}です。{}です。".format(
            self.size, self.color, self.type))


sofa1 = Sofa(2, "赤", "布タイプ")
sofa1.print_data()

sofa2 = Sofa(3, "茶", "本革タイプ")
sofa2.print_data()

sofa3 = Sofa(2, "黒", "合成革タイプ")
sofa3.print_data()
