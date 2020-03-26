from models.wear import Wear
from models.shoes import Shoes


nike = Wear("Nike", "黒", "M")
nike.print_deta()

puma = Wear("Puma", "白", "L")
puma.print_deta()

adidas = Wear("Adidas", "紫", "LL")
adidas.print_deta()

under_armor = Shoes("Under_armor", "黒", "S", "白", "27")
under_armor.print_deta()
under_armor = Shoes("Mizuno", "黄色", "M", "オレンジ", "28")
under_armor.print_deta()
