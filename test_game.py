# tests/test_game.py
import unittest
import string
from unittest.mock import patch
from game import Game

class TestGame(unittest.TestCase):
    mystr = "AZERTYUIO"
    @patch('builtins.input', return_value=mystr)
    def test_game_initialization(self, mock_input):
        new_game = Game()
        grid = new_game.grid
        word = new_game.word
        foo = new_game.is_valid()
        self.assertEqual(foo, False)

if __name__ == '__main__':
    unittest.main()
