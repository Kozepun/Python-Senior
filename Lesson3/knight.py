from Lesson2.Character import Character
import random
class Knight(Character):
    def __init__(self, name = "Iarik", health = 100, damage = 1, defence = 0):
        Character.__init__(self, name, health, damage, defence)
    def take_damage(self, damage):
        roll_defence = random.randint(0, self.defence)
        self.health -= max(damage - roll_defence, 0)
