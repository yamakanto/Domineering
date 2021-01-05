from domineering.real_possible_moves_evaluation import RealPossibleMovesEvaluation
from domineering.board import Board
from domineering.board_analyzer import count_safe_moves_horizontal, count_safe_moves_vertical


class SafeRealPossibleMovesEvaluation(RealPossibleMovesEvaluation):

    def __call__(self, board):
        possible_moves_diff = self._compute_possible_moves_diff(board)
        safe_moves_diff = self._compute_safe_move_diff(board)
        return 2*safe_moves_diff + possible_moves_diff

    def _compute_safe_move_diff(self, board):
        return count_safe_moves_vertical(board) - count_safe_moves_horizontal(board)
