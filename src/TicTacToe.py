class TicTacToe:
    def __init__(self):
        self.board = [[" "]*3 for _ in range(3)]
        self.current_player = "X"

    def print_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
        else:
            print("Invalid move! Try again.")

    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return row[0]

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return self.board[0][col]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]

        # Check for draw
        if all(self.board[i][j] != " " for i in range(3) for j in range(3)):
            return "Draw"

        return None

    def play(self):
        while True:
            self.print_board()
            print(f"It's {self.current_player}'s turn.")
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            self.make_move(row, col)
            winner = self.check_winner()
            if winner:
                if winner == "Draw":
                    print("It's a draw!")
                else:
                    print(f"{winner} wins!")
                break

class Main:
    def main():
        tic_tac_toe = TicTacToe()
        tic_tac_toe.play()

if __name__ == '__main__':
    Main.main()
