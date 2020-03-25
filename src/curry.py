class Curry:
    def pot(self):
        print("pot", "に")


class Onion(Curry):
    def onion(self):
        print("onion", "を入れました")


class Carrot(Curry):
    def carrot(self):
        print("carrot", "を入れました")


class Potato(Curry):
    def potato(self):
        print("potato", "を入れました")


class Meat(Curry):
    def meat(self):
        print("meat", "を入れました")


onion = Onion()
onion.pot()
onion.onion()

carrot = Carrot()
carrot.pot()
carrot.carrot()

potato = Potato()
potato.pot()
potato.potato()

meat = Meat()
meat.pot()
meat.meat()
