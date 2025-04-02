from exercices_XP import Dog
import random

class Petdog(Dog):
    def __init__(self, dog_name, dog_age, dog_weight, trained = False):
        super().__init__(self, dog_name, dog_age, dog_weight)
        
        def train(self):
            print(self.bark())
            self.trained = True

        def play(self, *dog_names):
            print(f"{self.dog_names} all play together")

        def do_a_trick(slef):
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]
            if self.trained:
                print(random.choice(tricks))
            



