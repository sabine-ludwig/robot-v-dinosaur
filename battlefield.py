from robot import Robot
from dinosaur import Dinosaur

class Battlefield:

    def __init__(self):
        self.robot = Robot("Wall-E")
        self.dinosaur = Dinosaur("Littlefoot", 50)
        self.run_game()

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print()
        print("Welcome to the battlefield!")
        print()

    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            if self.robot.health > 0:
                self.robot.attack(self.dinosaur)
                # print(f"{self.robot} is defeated.")
            # else:
            #     print("Robot has been defeated.")
            if self.dinosaur.health > 0:
                self.dinosaur.attack(self.robot)
            # else:
            #     print("Dinosaur has been defeated.")
                
        print("The battle has officially ended!")

    def display_winner(self):
        if self.robot.health > self.dinosaur.health:
            print(f"{self.robot.name} is the winner!")
        else:
            print(f"{self.dinosaur.name} is the winner!")




