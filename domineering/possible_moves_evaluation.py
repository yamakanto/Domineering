from domineering.evaluation_function import EvaluationFunction
from domineering.board import Board
from domineering.board_analyzer import count_moves_horizontal, count_moves_vertical


class PossibleMovesEvaluation(EvaluationFunction):

    def __call__(self, board):
        return self._compute_possible_moves_diff(board)

    def _compute_possible_moves_diff(self, board):
        vert_move_count = self._count_vert_moves(board)
        hor_move_count = self._count_hor_moves(board)
        return vert_move_count - hor_move_count

    def _count_hor_moves(self, board):
        return count_moves_horizontal(board, False)

    def _count_vert_moves(self, board):
        return count_moves_vertical(board, False)
