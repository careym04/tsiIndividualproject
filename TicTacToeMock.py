import unittest
from unittest.mock import patch
from src.TicTacToe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    
    
    
    XwinsScenarion = ['0', '0', '1', '1', '2', '2', '0', '0', '1', '1', '2', '2', '1', '0', '1', '2', '0', '2', '1', '2', '2', '1', '0', '1', '2', '0']
    
    @patch('builtins.input', side_effect=XwinsScenarion)
    def test_play_game(self, mock_input):
        tic_tac_toe = TicTacToe()
        tic_tac_toe.play()
        # Add assertions to verify the expected behavior based on the mock input

if __name__ == '__main__':
    unittest.main()