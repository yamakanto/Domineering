from copy import deepcopy
from abc import ABC, abstractmethod
from domineering.board import Board
from domineering.board_analyzer import can_make_move


class DomineeringPlayer(ABC):
    def __init__(self, vertical):
        self.vertical = vertical

    @abstractmethod
    def get_turn(self, board):
        pass

    def compute_possible_moves(self, board, vertical):
        possible_moves = []
        for row in range(board.get_height()):
            for col in range(board.get_width()):
                move = row, col
                if can_make_move(board, move, vertical):
                    possible_moves.append((row, col))
        return possible_moves

    def _can_move_to_pos(self, row, col, board, vertical):
        move = row, col
        return can_make_move(board, move, vertical)

    def _board_after_move(self, board, move, vertical):
        return board.get_after_move(move, vertical)
