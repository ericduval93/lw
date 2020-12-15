import string
import random
import requests

class GameFlask:
    def __init__(self):
        self.grid = self.random_grid()
    def random_grid(self):
        return ''.join(random.choice(string.ascii_uppercase) for i in range(3))
    def is_valid(self, word):
        if self.grid == word:
            return True
        else:
            return False
    def is_dico(self,word):
        return requests.get(f"https://wagon-dictionary.herokuapp.com/AZERTY").json()['found']

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
    def is_dico(self,word):
        return requests.get(f"https://wagon-dictionary.herokuapp.com/AZERTY").json()['found']


if __name__ == "__main__":
    gg = Game()
    if gg.is_valid():
        print("{} is the same {}".format(gg.word, gg.grid))
    else:
        print("{} is NOT the same {}".format(gg.word, gg.grid))

    if gg.is_dico( gg.word ):
        print("{} is in dico".format(gg.word))
    else:
        print("{} is NOT in dico".format(gg.word))

