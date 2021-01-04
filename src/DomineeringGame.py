from src.board import Board
from src.board_analyzer import can_make_move


class DomineeringGame:
    def __init__(self, width, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.__active_player = 0
        self.__num_to_player = {0: player1, 1: player2}
        self._repr_board = Board(' ', {True: 'V', False: 'H'}, width, width)
        self.__player_num_to_vertical = {0: True, 1: False}

    def play(self):
        while not self._finished():
            self._play_turn()
        self.__print_finished_state()

    def _play_turn(self):
        print(self)
        self.__request_turn_from_active_player()
        self.__switch_active_player()

    def __request_turn_from_active_player(self):
        player = self.__num_to_player[self.__active_player]
        turn = player.get_turn(self._repr_board)
        while not self.__turn_valid(turn):
            turn = player.get_turn(self._repr_board)
        self.__perform_turn(turn)

    def _finished(self):
        if self.__active_player == 0 and len(self.player1.compute_possible_moves(self._repr_board, True)) == 0:
            return True
        if self.__active_player == 1 and len(self.player2.compute_possible_moves(self._repr_board, False)) == 0:
            return True
        return False

    def __switch_active_player(self):
        self.__active_player = 1-self.__active_player

    def __turn_valid(self, turn):
        vertical = self.__player_num_to_vertical[self.__active_player]
        return can_make_move(self._repr_board, turn, vertical)

    def __perform_turn(self, turn):
        self._repr_board.add_move(turn, self.__active_player == 0)

    def __print_finished_state(self):
        print('finished')
        if self.__active_player == 0 and len(self.player1.compute_possible_moves(self._repr_board, True)) == 0:
            print('Player 2 won')
        if self.__active_player == 1 and len(self.player2.compute_possible_moves(self._repr_board, False)) == 0:
            print('Player 1 won')
        print('board state at the end:')
        print(self._repr_board)

    def __str__(self):
        vert_string = 'vertical'
        hor_string = 'horizontal'
        player_line = f'Player {self.__active_player+1} ({vert_string if self.__active_player==0 else hor_string})'
        board_state = str(self._repr_board)
        return player_line+'\n' + board_state + '\n'+self._repr_board.get_parseable_text()+'\n'

    def _get_board_parse_string(self):
        return self._repr_board.get_parseable_text()
