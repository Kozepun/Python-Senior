from Character import  Character

player1 = Character()
player2 = Character(name = "Tarakan", health= 1, damage= 0)
player3 = Character(name = "Nadya", health= 1000, damage= 100, defence= 1000)
player1.attack(player3)
print(player1)
print(player2)
print(player3)