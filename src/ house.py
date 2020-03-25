class House():
    def room(self):
        print("room")


class Kitchen(House):
    def kitchen_room(self):
        print("kitchen_room", "料理するところ。")


class Shower(House):
    def shower_room(self):
        print("shower_room", "お風呂に入れます。")


class Bed(House):
    def bed_room(self):
        print("bed_room", "ベッドが１つ置いてあります。")


class Living(House):
    def living_room(self):
        print("living_room", "テレビがあります。")


class Dining(House):
    def dining_room(self):
        print("dining_room", "ソファーがあります。")


kitchen = Kitchen()
kitchen.room()
kitchen.kitchen_room()

shower = Shower()
shower.room()
shower.shower_room()

bed = Bed()
bed.room()
bed.bed_room()

living = Living()
living.room()
living.living_room()

dining = Dining()
dining.room()
dining.dining_room()
