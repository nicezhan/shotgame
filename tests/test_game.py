import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

from game.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from game.states import GameState

class TestGameConstants(unittest.TestCase):
    def test_screen_dimensions(self):
        self.assertEqual(SCREEN_WIDTH, 800)
        self.assertEqual(SCREEN_HEIGHT, 600)

    def test_fps(self):
        self.assertEqual(FPS, 60)

class TestGameStates(unittest.TestCase):
    def test_states_exist(self):
        self.assertTrue(hasattr(GameState, 'MENU'))
        self.assertTrue(hasattr(GameState, 'PLAYING'))
        self.assertTrue(hasattr(GameState, 'PAUSED'))
        self.assertTrue(hasattr(GameState, 'GAME_OVER'))

if __name__ == '__main__':
    unittest.main()