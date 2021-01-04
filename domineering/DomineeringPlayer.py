from copy import deepcopy
from abc import ABC, abstractmethod
from domineering.board import Board


class DomineeringPlayer(ABC):
    def __init__(self, vertical):
        self.vertical = vertical

    @abstractmethod
    def get_turn(self, board):
        pass

    def compute_possible_moves(self, board, vertical):
        if isinstance(board, Board):
            return self.compute_possible_moves_new_board(board, vertical)
        possible_moves = []
        for row in range(len(board)):
            for col in range(len(board[row])):
                if self._can_move_to_pos(row, col, board, vertical):
                    possible_moves.append((row, col))
        return possible_moves

    def _can_move_to_pos(self, row, col, board, vertical):
        if isinstance(board, Board):
            return self._can_move_to_pos_new_board((row, col), board, vertical)
        if not row in range(len(board)) or col not in range(len(board[0])):
            return False
        if vertical:
            if not row + 1 < len(board):
                return False
            if not board[row][col] and not board[row+1][col]:
                return True
        else:
            if not col+1 < len(board[row]):
                return False
            if not board[row][col] and not board[row][col+1]:
                return True
        return False

    def _board_after_move(self, board, move, vertical):
        if isinstance(board, Board):
            return board.get_after_move(move, vertical)
        new_board = deepcopy(board)
        x, y = move
        if vertical:
            new_board[x][y] = 1
            new_board[x+1][y] = 1
        else:
            new_board[x][y] = 2
            new_board[x][y+1] = 2
        return new_board

    def compute_possible_moves_new_board(self, board, vertical):
        possible_moves = []
        for row in range(board.get_height()):
            for col in range(board.get_width()):
                if self._can_move_to_pos_new_board((row, col), board, vertical):
                    possible_moves.append((row, col))
        return possible_moves

    def _can_move_to_pos_new_board(self, pos, board, vertical):
        row, col = pos
        if vertical:
            add_pos = row+1, col
        else:
            add_pos = row, col + 1
        return board.position_is_empty(pos) and board.position_is_empty(add_pos)
