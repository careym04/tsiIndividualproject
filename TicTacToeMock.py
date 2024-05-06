import unittest
from unittest.mock import patch
from src.TicTacToe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    
    
    
    XwinsScenarion = ['0', '0', '1', '1', '2', '2', '0', '0', '1', '1', '2', '2', '1', '0', '1', '2', '0', '2', '1', '2', '2', '1', '0', '1', '2', '0']
    knoughtsWinsScenario = ['0', '0', '2', '2', '0', '1', '2', '1', '1', '0', '2', '0']
    
    
    @patch('builtins.input', side_effect=XwinsScenarion)
    def test_play_game_XWins(self, mock_input):
        tic_tac_toe = TicTacToe()
        tic_tac_toe.play()
        print("MOCK RAN *****")
       
    @patch('builtins.input', side_effect=knoughtsWinsScenario)
    def test_play_game_knoughtsWins(self,mock_input):
         tic_tac_toe = TicTacToe()
         tic_tac_toe.play()
         print(" MOCK RAN ****")
if __name__ == '__main__':
    unittest.main()