import unittest
from TicTacToe import TicTacToe
class TestTicTacToe(unittest.TestCase):
    def test_make_move_valid(self):
        tic_tac_toe = TicTacToe()
        tic_tac_toe.make_move(0, 0)
        self.assertEqual(tic_tac_toe.board[0][0], "X")
        self.assertEqual(tic_tac_toe.current_player, "O")

    def test_make_move_invalid(self):
        tic_tac_toe = TicTacToe()
        tic_tac_toe.make_move(0, 0)
        tic_tac_toe.make_move(0, 0)  
        self.assertEqual(tic_tac_toe.current_player, "O")  

    def test_check_winner_row(self):
        tic_tac_toe = TicTacToe()
        tic_tac_toe.board = [["X", "X", "X"],
                             [" ", " ", " "],
                             [" ", " ", " "]]
        winner = tic_tac_toe.check_winner()
        self.assertEqual(winner, "X")

if __name__ == '__main__':
    unittest.main()
