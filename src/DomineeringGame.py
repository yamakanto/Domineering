class DomineeringGame:
    def __init__(self, width, player1, player2):
        self.width = width
        self.player1 = player1
        self.player2 = player2
        self.__init_board()
        self.__active_player = 0
        self.__num_to_player = {0: player1, 1: player2}

    def __init_board(self):
        self.board = []
        for _ in range(self.width):
            self.board.append([None for _ in range(self.width)])

    def play(self):
        while not self.__finished():
            print(self)
            self.__request_turn_from_active_player()
            self.__switch_active_player()
        self.__print_finished_state()

    def __request_turn_from_active_player(self):
        player = self.__num_to_player[self.__active_player]
        turn = player.get_turn(self.board)
        while not self.__turn_valid(turn):
            turn = player.get_turn(self.board)
        self.__perform_turn(turn)

    def __finished(self):
        if self.__active_player == 0 and len(self.player1.compute_possible_moves(self.board, True)) == 0:
            return True
        if self.__active_player == 1 and len(self.player2.compute_possible_moves(self.board, False)) == 0:
            return True
        return False

    def __switch_active_player(self):
        self.__active_player = 1-self.__active_player

    def __turn_valid(self, turn):
        row, col = turn
        if self.__active_player == 0:
            if self.board[row][col] is None and self.board[row+1][col] is None:
                return True
        else:
            if self.board[row][col] is None and self.board[row][col+1] is None:
                return True
        return False

    def __perform_turn(self, turn):
        row, col = turn
        if self.__active_player == 0:
            self.board[row][col] = 1
            self.board[row+1][col] = 1
        else:
            self.board[row][col] = 2
            self.board[row][col+1] = 2

    def __print_finished_state(self):
        print('finished')
        if self.__active_player == 0 and len(self.player1.compute_possible_moves(self.board, True)) == 0:
            print('Player 2 won')
        if self.__active_player == 1 and len(self.player2.compute_possible_moves(self.board, False)) == 0:
            print('Player 1 won')
        print('board state at the end:')
        print(self.__get_board_state_string())

    def __str__(self):
        player_line = f'Player {self.__active_player+1}'
        board_state = self.__get_board_state_string()

        return player_line+'\n' + board_state

    def __get_board_state_string(self):
        rows = []
        first_line = '  ' + \
            ''.join([f'{x+1:2d}' for x in range(len(self.board))])
        rows.append(first_line)
        rows.append('-' * len(first_line))

        for index, row in enumerate(self.board):
            line = f'{index+1:2d}|'
            for x in row:
                if x in [1, 2]:
                    line += str(x)
                else:
                    line += ' '
                line += ' '
            rows.append(line)
        return '\n'.join(rows)


def board_from_string(s):
    def char_to_symb(c):
        if c == ' ':
            return None
        return int(c)
    lines = s.split('\n')
    board = [[char_to_symb(c) for c in l] for l in lines]
    return board
