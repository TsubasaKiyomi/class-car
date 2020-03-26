class Player:
    def __init__(self, name, dais, susumu):
        self.name = name
        self.dais = dais
        self.susumu = susumu

    def print_deta(self):
        print("{}はサイコロを振った。{}の目が出た。{}歩進んだ。".format(
            self.name, self.dais, self.susumu))
