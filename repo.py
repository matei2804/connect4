class repo:
    def __init__(self):
        self.boards = []

    '''
        Method that adds a new board to the board list.
    '''
    def add_board(self, board):
        self.boards.append(board)

    '''
        Method that returns the current board.
    '''
    def current_board(self):
        return self.boards[-1]
