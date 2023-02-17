class Dinosaur:

    def __init__(self, name, attack_power):
        self.name = name 
        self.attack_power = attack_power
        self.health = 100
        # print(f"Your dinosaur's name is {self.name} and they have an attack power of {self.attack_power}.")

    def attack(self, robot):
        # self.robot = robot
        robot.health -= self.attack_power
        print(f"{self.name} attacks {robot.name}.")
        print(f"{robot.name} loses {self.attack_power} health and now has {robot.health} health remaining.")
        print()
        # decrease robot's health by dinosaur attack power
        # print statement to let user know what happened 

# dinosaur = Dinosaur("Littlefoot", 50)
