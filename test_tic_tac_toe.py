import unittest
from tic_tac_toe import TicTacToe

class TestTicTacToe(unittest.TestCase):

    def test_add_X(self):
        game = TicTacToe()
        game.add_X(0, 0)
        self.assertEqual(game.board[0][0], "X")

    def test_add_O(self):
        game = TicTacToe()
        game.add_O(0, 1)
        self.assertEqual(game.board[0][1], "O")

    def test_check_winner(self):
        game = TicTacToe()
        game.board = [["X", "X", "X"], [" ", " ", " "], [" ", " ", " "]]
        self.assertEqual(game.check_winner(), "X")

    def test_check_draw(self):
        game = TicTacToe()
        game.board = [["X", "O", "X"], ["X", "X", "O"], ["O", "X", "O"]]
        self.assertEqual(game.check_winner(), "Draw")

if __name__ == "__main__":
    unittest.main()
