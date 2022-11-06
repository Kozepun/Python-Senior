from Character import Character
from Lesson3.berserk import Berserk
from Lesson3.knight import Knight
from HomeWork2.Assasin import Assasin
player1 = Character()
player2 = Berserk("y", 100, 10 , 0)
player3 = Knight("UUU", 100, 10, 10)
player4 = Assasin("UWU", 100, 1, 0)
'''
print(player2)
player1.attack(player2)
print(player2)

print(player2.count_additional_damage())
player2.attack(player1)
print(player1)

player2.attack(player3)
print(player3)
'''
player4.attack(player3)
print(player3)

'''
player2 = Character(name = "Tarakan", health= 20000, damage= 1)
player3 = Character(name = "Nadya", health= 1000, damage= 100, defence= 1000)
while player3.is_alive() & player2.is_alive():
    player2.attack(player3)
    player3.attack(player2)
    print(player2)
    print(player3)
'''