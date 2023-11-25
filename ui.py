from Service.service import service


class ui:
    def __init__(self, serv: service):
        self.serv = serv

    @staticmethod
    def player_wins():
        print("You win!")

    @staticmethod
    def computer_win():
        print("Computer wins!")

    @staticmethod
    def wrong_input():
        print("Please enter valid input!")

    @staticmethod
    def tie():
        print("Tie!")

    def start_game(self):
        board = self.serv.generate_empty_board()
        n = 0
        print(self.serv.str_board(board))
        while True:
            print("Player's turn:")
            while True:
                try:
                    n = int(input(">"))
                except ValueError:
                    self.wrong_input()
                    continue
                if 1 <= n <= 7 and self.serv.valid_move(n - 1) is True:
                    break
                else:
                    self.wrong_input()

            player_move = n - 1
            new_board = self.serv.new_player_move(player_move)
            self.serv.add_board(new_board)
            print(self.serv.str_board(new_board))
            if self.serv.check_win(new_board):
                self.player_wins()
                break

            print("Computer's turn!")
            new_board = self.serv.new_computer_move()
            self.serv.add_board(new_board)
            print(self.serv.str_board(new_board))
            if self.serv.check_win(new_board):
                self.computer_win()
                break

            if self.serv.check_tie():
                self.tie()
                break
