from copy import deepcopy
from utils.string_utils import underline


class Board:
    def __init__(self, empty_symb, player_to_symb, width, height):
        self.empty_symb = empty_symb
        self.occupied_positions = set()
        self.vertical_moves = set()
        self.horizontal_moves = set()
        self.__width = width
        self.__height = height
        self.player_to_symb = player_to_symb

    def get_after_move(self, move, vertical):
        board = deepcopy(self)
        board.add_move(move, vertical)
        return board

    def add_move(self, move, vertical):
        if vertical:
            new_move = move[0]+1, move[1]
        else:
            new_move = move[0], move[1]+1
        self.__add_positions([move, new_move], vertical)

    def remove_move(self, move, vertical):
        if vertical:
            self.__remove_move_vertical(move)
        else:
            self.__remove_move_horizontal(move)

    def __remove_move_vertical(self, move):
        second_move = move[0] + 1, move[1]
        if not self.__positions_are_occupied_vertical([move, second_move]):
            raise ValueError(f'Positions are not all occupied!')
        self.vertical_moves.remove(move)
        self.vertical_moves.remove(second_move)
        self.occupied_positions.remove(move)
        self.occupied_positions.remove(second_move)

    def __positions_are_occupied_vertical(self, positions):
        pos_in_occupied = self.positions_are_occupied(positions)
        pos_in_vertical = all(
            [pos in self.vertical_moves for pos in positions])
        return pos_in_occupied and pos_in_vertical

    def __remove_move_horizontal(self, move):
        add_move = move[0], move[1] + 1
        if not self.__positions_are_occupied_horizontal([move, add_move]):
            raise ValueError(f'Positions are not all occupied!')
        self.horizontal_moves.remove(move)
        self.horizontal_moves.remove(add_move)
        self.occupied_positions.remove(move)
        self.occupied_positions.remove(add_move)

    def __positions_are_occupied_horizontal(self, positions):
        pos_in_occupied = self.positions_are_occupied(positions)
        pos_in_horizontal = all(
            [pos in self.horizontal_moves for pos in positions])
        return pos_in_occupied and pos_in_horizontal

    def position_is_empty(self, pos):
        if not self.__pos_within_boundary(pos):
            return False
        return pos not in self.occupied_positions

    def __pos_within_boundary(self, pos):
        return 0 <= pos[0] < self.__height and 0 <= pos[1] < self.__width

    def positions_are_empty(self, positions):
        return all([self.position_is_empty(pos) for pos in positions])

    def positions_are_occupied(self, positions):
        return all([not self.position_is_empty(pos) for pos in positions])

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def __str__(self):
        rows = []
        first_line = '   ' + \
            ''.join(
                [f'{x+1:2d}' for x in range(self.__width)])
        rows.append(underline(first_line))
        for row in range(self.__height):
            line_symbols = [f'{row+1:2d}|']
            for col in range(self.__width):
                line_symbols.append(self.__get_symbol_for_pos((row, col)))
            rows.append(' '.join(line_symbols))
        return '\n'.join(rows)

    def __get_symbol_for_pos(self, pos, empty_symb=None):
        if not empty_symb:
            empty_symb = self.empty_symb
        if pos in self.vertical_moves:
            return self.player_to_symb[True]
        elif pos in self.horizontal_moves:
            return self.player_to_symb[False]
        else:
            return empty_symb

    def get_parseable_text(self):
        rows = []
        for row in range(self.__height):
            line = ''
            for col in range(self.__width):
                line += self.__get_symbol_for_pos((row, col), 'E')
            rows.append(line)
        return ';'.join(rows)

    def __add_pos(self, pos, vertical):
        self.__add_positions([pos], vertical)

    def __add_positions(self, positions, vertical):
        player_set = self.__get_player_set(vertical)
        if any([(pos in player_set or pos in self.occupied_positions) for pos in positions]):
            raise ValueError(
                f'Some position from {positions} are already occupied!')
        for pos in positions:
            player_set.add(pos)
            self.occupied_positions.add(pos)

    def __get_player_set(self, vertical):
        if vertical:
            return self.vertical_moves
        else:
            return self.horizontal_moves

    @staticmethod
    def from_string(text, empty_symb=' ', player_to_symb={True: 'V', False: 'H'}):
        lines = text.split(';')
        board = Board(empty_symb, player_to_symb, len(lines[0]), len(lines))
        symb_to_player = {val: key for key, val in player_to_symb.items()}
        for row, line in enumerate(lines):
            for col, symbol in enumerate(line):
                pos = row, col
                if symbol in symb_to_player:
                    board.__add_pos(pos, symb_to_player[symbol])
        return board
