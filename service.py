from tabulate import tabulate
from Repository.repo import repo
import random
import numpy as np


class service:
    def __init__(self, rep: repo):
        self.rep = rep

    '''
        Method that creates an empty 6x7 board.
    '''
    def generate_empty_board(self):
        board = []
        for i in range(6):
            row = ['   ', '   ', '   ', '   ', '   ', '   ', '   ']
            board.append(row)
        self.rep.add_board(board)
        return board

    '''
        Method that creates a table in order to display the board in the console.
    '''
    @staticmethod
    def str_board(board):
        headers = ['1', '2', '3', '4', '5', '6', '7']
        return tabulate(board, headers, tablefmt="rounded_grid", stralign='center')

    '''
        Method that adds a new board to the board list in the repository.
    '''
    def add_board(self, board):
        self.rep.add_board(board)

    '''
        Checks if the current move is a valid one.
        A move is valid if there is at least one empty slot on that specific row.
    '''
    def valid_move(self, move):
        board = self.rep.current_board()
        if board[0][move] != '   ':
            return False
        return True

    '''
        Inserts an 'X' on the board based on the input given by the player.
    '''
    def new_player_move(self, move):
        board = self.rep.current_board()
        for i in range(5, -1, -1):
            if board[i][move] == '   ':
                board[i][move] = ' X '
                break
        return board

    '''
        Inserts an 'O' based on the current status of the game.
            - If the player is one move away from winning, the computer picks a move in order to stop him if possible.
            - If the computer is one move away from winning, it will pick the winning move.
            - Else the computer picks a random valid move.
    '''
    def new_computer_move(self):
        board = self.current_board()
        boarded_board = np.pad(board, pad_width=4, mode='constant',
                               constant_values=0)
        move = -1
        i, j, direction = self.check_computer_move_stop_win()
        I, J, Direction = self.computer_move_win()
        # print(Direction)
        # print(direction)
        if I != -1 and J != -1:
            move = J - 4
        elif i != -1 and j != -1:
            move = j - 4

        if move == -1:
            while True:
                move_random = random.randint(0, 6)
                if self.valid_move(move_random):
                    break
            move = move_random

        board = self.rep.current_board()
        for i in range(5, -1, -1):
            if board[i][move] == '   ':
                board[i][move] = ' O '
                break
        return board

    '''
        Method that checks if there is a possible move that will stop the player from winning and returns that move.
        Iterates through the matrix and checks if there are 3 X's in a row (for any direction) .
    '''
    def check_computer_move_stop_win(self):
        board = self.current_board()
        boarded_board = np.pad(board, pad_width=4, mode='constant',
                               constant_values=0)
        for i in range(4, 10):
            for j in range(4, 11):
                x = boarded_board[i][j]
                if x == boarded_board[i][j + 1] == boarded_board[i][j + 2] \
                        and x == ' X ' and boarded_board[i][j + 3] == '   ' and boarded_board[i + 1][j + 3] != '   ':
                    return i, j + 3, 'd'
                if x == boarded_board[i][j + 1] == boarded_board[i][j + 3] \
                        and x == ' X ' and boarded_board[i][j + 2] == '   ' and boarded_board[i + 1][j + 2] != '   ':
                    return i, j + 2, 'd'
                if x == boarded_board[i][j + 2] == boarded_board[i][j + 3] \
                        and x == ' X ' and boarded_board[i][j + 1] == '   ' and boarded_board[i + 1][j + 1] != '   ':
                    return i, j + 1, 'd'
                if boarded_board[i][j + 1] == boarded_board[i][j + 2] == boarded_board[i][j + 3] == ' X ' \
                        and x == '   ' and boarded_board[i + 1][j] != '   ':
                    return i, j, 'd'

                if x == boarded_board[i - 1][j] == boarded_board[i - 2][j] and boarded_board[i - 3][j] == '   ' \
                        and x == ' X ':
                    return i - 3, j, 'w'

                if x == boarded_board[i + 1][j + 1] == boarded_board[i + 2][j + 2] and boarded_board[i + 3][
                    j + 3] == '   ' \
                        and x == ' X ' and boarded_board[i + 4][j + 3] != '   ':
                    return i + 3, j + 3, 'c'
                if x == boarded_board[i + 1][j + 1] == boarded_board[i + 3][j + 3] and boarded_board[i + 2][
                    j + 2] == '   ' \
                        and x == ' X ' and boarded_board[i + 3][j + 2] != '   ':
                    return i + 2, j + 2, 'c'
                if x == boarded_board[i + 2][j + 2] == boarded_board[i + 3][j + 3] and boarded_board[i + 1][
                    j + 1] == '   ' \
                        and x == ' X ' and boarded_board[i + 2][j + 1] != '   ':
                    return i + 1, j + 1, 'c'
                if boarded_board[i + 1][j + 1] == boarded_board[i + 2][j + 2] == boarded_board[i + 3][
                    j + 3] and x == '   ' \
                        and boarded_board[i + 1][j + 1] == ' X ' and boarded_board[i + 1][j] != '   ':
                    return i, j, 'c'

                if x == boarded_board[i - 1][j + 1] == boarded_board[i - 2][j + 2] and boarded_board[i - 3][
                    j + 3] == '   ' and x == ' X ' and boarded_board[i - 2][j + 3] != '   ':
                    return i - 3, j + 3, 'e'
                if x == boarded_board[i - 1][j + 1] == boarded_board[i - 3][j + 3] and boarded_board[i - 2][
                    j + 2] == '   ' and x == ' X ' and boarded_board[i - 1][j + 2] != '   ':
                    return i - 2, j + 2, 'e'
                if x == boarded_board[i - 2][j + 2] == boarded_board[i - 3][j + 3] and boarded_board[i - 1][
                    j + 1] == '   ' and x == ' X ' and boarded_board[i][j + 1] != '   ':
                    return i - 1, j + 1, 'e'
                if boarded_board[i - 1][j + 1] == boarded_board[i - 2][j + 2] == boarded_board[i - 3][j + 3] and \
                        boarded_board[i - 1][j + 1] == ' X ' and x == '   ' \
                        and boarded_board[i + 1][j] != '   ':
                    return i, j, 'e'

        return -1, -1, 'no'

    '''
        Method that checks if there is a possible winning move for the computer.
        Returns that move if it exists.
    '''
    def computer_move_win(self):
        board = self.current_board()
        boarded_board = np.pad(board, pad_width=4, mode='constant',
                               constant_values=0)
        for i in range(4, 10):
            for j in range(4, 11):
                x = boarded_board[i][j]
                if x == boarded_board[i][j + 1] == boarded_board[i][j + 2] \
                        and x == ' O ' and boarded_board[i][j + 3] == '   ' and boarded_board[i + 1][j + 3] != '   ':
                    return i, j + 3, 'D'
                if x == boarded_board[i][j + 1] == boarded_board[i][j + 3] \
                        and x == ' O ' and boarded_board[i][j + 2] == '   ' and boarded_board[i + 1][j + 2] != '   ':
                    return i, j + 2, 'D'
                if x == boarded_board[i][j + 2] == boarded_board[i][j + 3] \
                        and x == ' O ' and boarded_board[i][j + 1] == '   ' and boarded_board[i + 1][j + 1] != '   ':
                    return i, j + 1, 'D'
                if boarded_board[i][j + 1] == boarded_board[i][j + 2] == boarded_board[i][j + 3] == ' O ' \
                        and x == '   ' and boarded_board[i + 1][j] != '   ':
                    return i, j, 'D'

                if x == boarded_board[i - 1][j] == boarded_board[i - 2][j] and boarded_board[i - 3][j] == '   ' \
                        and x == ' O ':
                    return i - 3, j, 'W'

                if x == boarded_board[i + 1][j + 1] == boarded_board[i + 2][j + 2] and boarded_board[i + 3][
                    j + 3] == '   ' \
                        and x == ' O ' and boarded_board[i + 4][j + 3] != '   ':
                    return i + 3, j + 3, 'C'
                if x == boarded_board[i + 1][j + 1] == boarded_board[i + 3][j + 3] and boarded_board[i + 2][
                    j + 2] == '   ' \
                        and x == ' O ' and boarded_board[i + 3][j + 2] != '   ':
                    return i + 2, j + 2, 'C'
                if x == boarded_board[i + 2][j + 2] == boarded_board[i + 3][j + 3] and boarded_board[i + 1][
                    j + 1] == '   ' \
                        and x == ' O ' and boarded_board[i + 2][j + 1] != '   ':
                    return i + 1, j + 1, 'C'
                if boarded_board[i + 1][j + 1] == boarded_board[i + 2][j + 2] == boarded_board[i + 3][
                    j + 3] and x == '   ' \
                        and boarded_board[i + 1][j + 1] == ' O ' and boarded_board[i + 1][j] != '   ':
                    return i, j, 'C'

                if x == boarded_board[i - 1][j + 1] == boarded_board[i - 2][j + 2] and boarded_board[i - 3][
                    j + 3] == '   ' and x == ' O ' and boarded_board[i - 2][j + 3] != '   ':
                    return i - 3, j + 3, 'E'
                if x == boarded_board[i - 1][j + 1] == boarded_board[i - 3][j + 3] and boarded_board[i - 2][
                    j + 2] == '   ' and x == ' O ' and boarded_board[i - 1][j + 2] != '   ':
                    return i - 2, j + 2, 'E'
                if x == boarded_board[i - 2][j + 2] == boarded_board[i - 3][j + 3] and boarded_board[i - 1][
                    j + 1] == '   ' and x == ' O ' and boarded_board[i][j + 1] != '   ':
                    return i - 1, j + 1, 'E'
                if boarded_board[i - 1][j + 1] == boarded_board[i - 2][j + 2] == boarded_board[i - 3][j + 3] and \
                        boarded_board[i - 1][j + 1] == ' O ' and x == '   ' \
                        and boarded_board[i + 1][j] != '   ':
                    return i, j, 'E'

        return -1, -1, 'no'

    '''
    Method that checks if the game is over. Creates a new board that has a border filled with '0's. Returns True 
    if there is a row, column, or a diagonal line that has length 4 and all the elements have the same symbol, else 
    Returns False. 
    '''
    @staticmethod
    def check_win(board):
        boarded_board = np.pad(board, pad_width=4, mode='constant',
                               constant_values=0)
        for i in range(4, 10):
            for j in range(4, 11):
                x = boarded_board[i][j]
                if x == boarded_board[i][j + 1] == boarded_board[i][j + 2] == boarded_board[i][j + 3] and x != '   ' \
                        and x != '0':
                    return True
                elif x == boarded_board[i][j - 1] == boarded_board[i][j - 2] == boarded_board[i][j - 3] and x != '   ' \
                        and x != '0':
                    return True
                elif x == boarded_board[i + 1][j] == boarded_board[i + 2][j] == boarded_board[i + 3][j] and x != '   ' \
                        and x != '0':
                    return True
                elif x == boarded_board[i - 1][j] == boarded_board[i - 2][j] == boarded_board[i - 3][j] and x != '   ' \
                        and x != '0':
                    return True
                elif x == boarded_board[i + 1][j + 1] == boarded_board[i + 2][j + 2] == boarded_board[i + 3][j + 3] \
                        and x != '   ' and x != '0':
                    return True
                elif x == boarded_board[i - 1][j - 1] == boarded_board[i - 2][j - 2] == boarded_board[i - 3][j - 3] \
                        and x != '   ' and x != '0':
                    return True
                elif x == boarded_board[i - 1][j + 1] == boarded_board[i - 2][j + 2] == boarded_board[i - 3][j + 3] \
                        and x != '   ' and x != '0':
                    return True
                elif x == boarded_board[i + 1][j - 1] == boarded_board[i + 2][j - 2] == boarded_board[i + 3][j - 3] \
                        and x != '   ' and x != '0':
                    return True
        return False

    '''
        Returns the current board.
    '''
    def current_board(self):
        return self.rep.current_board()

    '''
        Method that checks if the game board is full.
        If the board is full the game ends in a tie.
    '''
    def check_tie(self):
        board = self.rep.current_board()
        for i in range(0, 7):
            if board[0][i] == '   ':
                return False
        return True
