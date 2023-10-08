class TicTacToe:

    def __init__(self):
        self.board = [[" ", " ", " "] for _ in range(3)]
        self.turn = "X"

    def add_X(self, row, col):
        self.board[row][col] = "X"

    def add_O(self, row, col):
        self.board[row][col] = "O"

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != " ":
                return row[0]
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != " ":
                return self.board[0][col]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != " ":
            return self.board[0][2]
        if all(cell != " " for row in self.board for cell in row):
            return "Draw"
        return None

    def is_cell_empty(self, row, col):
        return self.board[row][col] == " "

    def switch_turn(self):
        self.turn = "O" if self.turn == "X" else "X"

    def display_board(self):
        print("  1 2 3")
        for i, row in enumerate(self.board):
            print(f"{i + 1} {' '.join(row)}")

if __name__ == "__main__":
    game = TicTacToe()

    while True:
        game.display_board()
        row = int(input(f"Player {game.turn}, enter the row (1-3): ")) - 1
        col = int(input(f"Player {game.turn}, enter the column (1-3): ")) - 1

        if game.is_cell_empty(row, col):
            if game.turn == "X":
                game.add_X(row, col)
            else:
                game.add_O(row, col)
        else:
            print("Cell is already occupied. Try again.")
            continue

        winner = game.check_winner()
        if winner:
            print(f"The winner is {winner}!")
            break

        game.switch_turn()
