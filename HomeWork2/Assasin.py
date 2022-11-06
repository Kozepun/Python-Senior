from Lesson2.Character import Character
import random
class Assasin(Character):
    def __init__(self, name = "Iarik", health = 100, damage = 1, defence = 0):
        Character.__init__(self, name, health, damage, defence)
    def attack(self, target):
        if(random.randint(1, 10) == 1):
            target.take_damage(1000)
        else:
            target.take_damage(self.damage)