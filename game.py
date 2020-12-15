import string
import random

class Game:
    def __init__(self):
        self.grid = self.random_grid()
        print("To cheat -- grid = [{}]".format(self.grid))
        self.word = input("Choice your word? ")
        print("To run with test_game.py -- word = [{}]".format(self.word))
    def random_grid(self):
        return ''.join(random.choice(string.ascii_uppercase) for i in range(9))
    def is_valid(self):
        if self.grid == self.word:
            return True
        else:
            return False

if __name__ == "__main__":
    gg = Game()
    if gg.is_valid():
        print("{} is the same {}".format(gg.word, gg.grid))
    else:
        print("{} is NOT the same {}".format(gg.word, gg.grid))

