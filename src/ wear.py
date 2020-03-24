class Wear():
    def __init__(self, set_name, set_color, set_size):
        self.name = set_name
        self.color = set_color
        self.size = set_size

    def print_deta(self):
        print("メーカーは{}です。色は{}で、サイズは{}です。".format(
            self.name, self.color, self.size))


wear1 = Wear("Nike", "黒", "M")
wear1.print_deta()

wear2 = Wear("Puma", "白", "L")
wear2.print_deta()

wear3 = Wear("Adidas", "紫", "LL")
wear3.print_deta()


class Shoes(Wear):
    def __init__(self, name, color, size, sho):
        super().__init__(name, color, size)
        self.sho = sho

    def socks(self):
        print("{}{}".format(self.name, self.sho))


test1 = Shoes("Under_armor", "黒", "S", "靴の色は青")
# test1 = socks()
test1.print_deta()
