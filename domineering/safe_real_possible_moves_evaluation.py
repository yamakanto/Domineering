from domineering.real_possible_moves_evaluation import RealPossibleMovesEvaluation
from domineering.board import Board
from domineering.board_analyzer import count_safe_moves_horizontal, count_safe_moves_vertical


class SafeRealPossibleMovesEvaluation(RealPossibleMovesEvaluation):

    def __call__(self, board, possible_moves_dict=None, safe_moves_dict=None):
        if possible_moves_dict:
            possible_moves_diff = len(
                possible_moves_dict[True]) - len([possible_moves_dict[False]])
        else:
            possible_moves_diff = self._compute_possible_moves_diff(board)
        if safe_moves_dict:
            safe_moves_diff = len(
                safe_moves_dict[True]) - len([safe_moves_dict[False]])
        else:
            safe_moves_diff = self._compute_safe_move_diff(board)

        return 2 * safe_moves_diff + possible_moves_diff

    def _compute_safe_move_diff(self, board):
        return count_safe_moves_vertical(board) - count_safe_moves_horizontal(board)
