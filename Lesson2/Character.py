class Character:
    name = ""
    health = 100
    damage = 1
    defence = 0

    def __init__(self, name = "Iarik", health = 100, damage = 1, defence = 0):
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence
    def __str__(self):
        return f"-=[{self.name}]=-\n" \
               f"Health -> {self.health}\n" \
               f"Damage -> {self.damage}\n" \
               f"Defence -> {self.defence}"
    def take_damage(self, damage):
        self.health -= max(damage, 0)
    def attack(self, target):
        target.take_damage(self.damage)
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
