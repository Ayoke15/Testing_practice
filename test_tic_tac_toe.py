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

    def test_is_cell_empty(self):
        game = TicTacToe()
        self.assertTrue(game.is_cell_empty(0, 0))
        game.add_X(0, 0)
        self.assertFalse(game.is_cell_empty(0, 0))

    def test_switch_turn(self):
        game = TicTacToe()
        self.assertEqual(game.turn, "X")
        game.switch_turn()
        self.assertEqual(game.turn, "O")

if __name__ == "__main__":
    unittest.main()
