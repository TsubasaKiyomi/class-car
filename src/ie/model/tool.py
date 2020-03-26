from .house import House


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
