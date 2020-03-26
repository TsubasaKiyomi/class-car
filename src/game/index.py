from models.mob import Chance
from models.cara import Player


import random
num = random.randint(1, 6)
# print(num)
num2 = random.randint(1, 6)

suzuki = Player("鈴木", num, num)
suzuki.print_deta()
satou = Player("佐藤", num2, num2)
satou.print_deta()

tanaka = Chance("田中", num, num2, num + num2)
tanaka.print_deta()
