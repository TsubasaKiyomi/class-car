class Character:
    def __init__(self, set_name, set_age, set_sex):
        self.name = set_name
        self.age = set_age
        self.sex = set_sex

    def print_data(self):
        print("名前は、{}です。年齢は{}歳です。{}です。".format(self.name, self.age, self.sex))


chara1 = Character("佐藤", 17, "男")
chara1.print_data()

chara2 = Character("鈴木", 16, "女")
chara2.print_data()


class Mob(Character):
    def __init__(self, name, age, sex, line):
        super().__init__(name, age, sex)
        self.line = line

    def speak(self):
        print("{}「{}」".format(self.name, self.line))


mob1 = Mob("先生", 40, "男", "テストに出るよ")
mob1.print_data()
mob1.speak()

mob2 = Mob("生徒「小泉」", 15, "女", "テストは嫌だ")
mob2.print_data()
mob2.speak()
