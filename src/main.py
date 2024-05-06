from LogIn import LogIn

class Main:
    def main():
        log_in = LogIn()
        log_in.log_in()
        
        game_choice = log_in.get_game_choice()
        
        if game_choice == "tic_tac_toe":
            from TicTacToe import TicTacToe
            tic_tac_toe = TicTacToe()
            tic_tac_toe.play()
        else:
            print("Sorry, the selected game is not available.")


if __name__ == '__main__':
    Main.main()

