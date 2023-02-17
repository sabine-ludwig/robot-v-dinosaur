from weapon import Weapon

class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon

    def attack(self, dinosaur):
        self.dinosaur = dinosaur
        self.dinosaur.health -= self.active_weapon.attack_power

weapon_1 = Weapon("laser", 40)

