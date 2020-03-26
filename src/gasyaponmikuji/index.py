from Garagara import Omikuji


import random
num = random.randint(1, 10)

if num == 1:
    print("特賞！おめでとう！")

elif num == 2:
    print("副賞。おめでと。")
else:
    print("残念、また次回挑戦。")

atare = Omikuji()
print(num)
