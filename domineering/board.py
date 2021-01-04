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
        if move in self.occupied_positions:
            raise ValueError(f'Position {move} is already occupied!')
        if new_move in self.occupied_positions:
            raise ValueError(f'Position {new_move} is already occupied!')
        self.occupied_positions.add(move)
        self.occupied_positions.add(new_move)
        if vertical:
            self.vertical_moves.add(move)
            self.vertical_moves.add(new_move)
        else:
            self.horizontal_moves.add(move)
            self.horizontal_moves.add(new_move)

    def remove_move(self, move, vertical):
        if vertical:
            self.__remove_move_vertical(move)
        else:
            self.__remove_move_horizontal(move)

    def __remove_move_vertical(self, move):
        add_move = move[0] + 1, move[1]
        if not self.__positions_are_occupied_vertical([move, add_move]):
            raise ValueError(f'Positions are not all occupied!')
        self.vertical_moves.remove(move)
        self.vertical_moves.remove(add_move)
        self.occupied_positions.remove(move)
        self.occupied_positions.remove(add_move)

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
        if not 0 <= pos[0] < self.__height or not 0 <= pos[1] < self.__width:
            return False
        return pos not in self.occupied_positions

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
            line = f'{row+1:2d}|'
            for col in range(self.__width):
                if (row, col) in self.vertical_moves:
                    line_symbols.append(self.player_to_symb[True])
                    line += self.player_to_symb[True]
                elif (row, col) in self.horizontal_moves:
                    line_symbols.append(self.player_to_symb[False])
                    line += self.player_to_symb[False]
                else:
                    line_symbols.append(' ')
                    line += self.empty_symb
                line += ' '
            # rows.append(line)
            rows.append(' '.join(line_symbols))
        return '\n'.join(rows)

    def get_parseable_text(self):
        rows = []
        for row in range(self.__height):
            line = ''
            for col in range(self.__width):
                if (row, col) in self.vertical_moves:
                    line += self.player_to_symb[True]
                elif (row, col) in self.horizontal_moves:
                    line += self.player_to_symb[False]
                else:
                    line += 'E'
            rows.append(line)
        return ';'.join(rows)

    @staticmethod
    def from_string(text, empty_symb=' ', player_to_symb={True: 'V', False: 'H'}):
        lines = text[:-1].split(';')
        board = Board(empty_symb, player_to_symb, len(lines[0]), len(lines))
        symb_to_player = {val: key for key, val in player_to_symb.items()}
        for row, line in enumerate(lines):
            for col, symbol in enumerate(line):
                pos = row, col
                if not board.positions_are_occupied([pos]):
                    if symbol in symb_to_player:
                        board.add_move(pos, symb_to_player[symbol])
        return board
