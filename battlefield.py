from robot import Robot
from dinosaur import Dinosaur

class Battlefield:

    def __init__(self):
        self.robot = Robot
        self.dinosaur = Dinosaur

    def run_game(self):
        self.display_welcome
        self.battle_phase

    def display_welcome(self):
        print(f"Welcome to the battlefield! Our matchup today is {Robot} vs {Dinosaur}.")
        print()

    def battle_phase(self):
        while self.robot.health > 0 or self.dinosaur.health > 0:
            self.dinosaur.attack
            print(self.robot.health)
            print()
            self.robot.attack
            print(self.dinosaur.health)
            print()
        print("The battle has officially ended!")

    def display_winner(self):
        if self.robot.health <= 0:
            print(f"{Dinosaur} is the winner!")
        elif self.dinosaur.health <= 0:
            print(f"{Robot} is the winner!")


robot_1 = Robot("Wall-E")
dinosaur_1 = Dinosaur("Littlefoot", 50) 

