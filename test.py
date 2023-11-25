import unittest
from Service.service import service
from Repository.repo import repo


class Test(unittest.TestCase):
    repo = repo()
    serv = service(repo)

    def test_board(self):
        board = self.serv.generate_empty_board()
        self.repo.add_board(board)

        # Test if the board is empty.
        for col in range(0, 6):
            for row in range(0, 7):
                self.assertEqual(board[col][row], '   ')

        # Make some moves on the board.
        self.serv.new_player_move(0)
        self.assertEqual(board[5][0], ' X ')

        self.serv.new_player_move(2)
        self.assertEqual(board[5][2], ' X ')

        board = self.serv.generate_empty_board()
        self.repo.add_board(board)
        self.serv.new_computer_move()
        self.assertIn(' O ', board[5])

        # Test board repository
        self.assertEqual(board, self.repo.current_board())

        # Test if the move is valid
        board = self.serv.generate_empty_board()
        self.repo.add_board(board)
        for i in range(0, 6):
            self.serv.new_player_move(0)

        self.assertNotEqual(True, self.serv.valid_move(0))

        # Test the win condition.
        board = self.serv.generate_empty_board()
        self.repo.add_board(board)
        self.serv.new_player_move(0)
        self.serv.new_player_move(1)
        self.serv.new_player_move(2)
        self.serv.new_player_move(3)

        self.assertEqual(True, self.serv.check_win(board))

        # Test if the computer makes the right move
        board = self.serv.generate_empty_board()
        self.repo.add_board(board)

        # Test if the computer will stop the player from winning
        self.serv.new_player_move(0)
        self.serv.new_player_move(1)
        self.serv.new_player_move(2)
        self.serv.new_computer_move()
        self.assertEqual(' O ', board[5][3])
