from Character import Character

player1 = Character()
player2 = Character(name = "Tarakan", health= 20000, damage= 1)
player3 = Character(name = "Nadya", health= 1000, damage= 100, defence= 1000)
while player3.is_alive() & player2.is_alive():
    player2.attack(player3)
    player3.attack(player2)
    print(player2)
    print(player3)