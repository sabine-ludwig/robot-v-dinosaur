from weapon import Weapon

class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("laser", 40)
        # print(f"Your robot's name is {self.name} and they will be using a {self.active_weapon.name} in this battle.")

    def attack(self, dinosaur):
        # self.dinosaur = dinosaur
        dinosaur.health -= self.active_weapon.attack_power
        print(f"{self.name} attacks {dinosaur.name}.")
        print(f"{dinosaur.name} takes {self.active_weapon.name} attack and now has {dinosaur.health} health remaining.")
        print()
        # decrease robot's health by dinosaur attack power
        # print statement to let user know what happened 



