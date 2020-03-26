from .cara import Player


class Chance(Player):
    def __init__(self, name, dais, susumu, saikoro):
        super().__init__(name, dais, susumu)
        self.saikoro = saikoro

    def print_deta(self):
        print("{}は、2つサイコロを振った。{}と{}の目が出た。{}歩進んだ。".format(
            self.name, self.dais, self.susumu, self.saikoro))
