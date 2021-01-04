from domineering.evaluation_function import EvaluationFunction
from utils.pattern_search import Pattern, PatternSearch
from domineering.board import Board
from domineering.board_analyzer import count_moves_horizontal, count_moves_vertical


class PossibleMovesEvaluation(EvaluationFunction):
    hor_move_pattern = Pattern([{0: {None}, 1: {None}}], 1, 2, False)
    vert_move_pattern = Pattern([{0: {None}},
                                 {0: {None}}], 2, 1, True)

    def __init__(self):
        self.pattern_search = PatternSearch()

    def __call__(self, board):
        return self._compute_possible_moves_diff(board)

    def _compute_possible_moves_diff(self, board):
        if isinstance(board, Board):
            return count_moves_vertical(board, False) - count_moves_horizontal(board, False)
        vert_move_count = self._count_vert_moves(board)
        hor_move_count = self._count_hor_moves(board)
        return vert_move_count - hor_move_count

    def _count_hor_moves(self, board):
        count = self.pattern_search.count_occurrences_of_pattern(
            board, PossibleMovesEvaluation.hor_move_pattern)
        return count

    def _count_vert_moves(self, board):
        count = self.pattern_search.count_occurrences_of_pattern(
            board, PossibleMovesEvaluation.vert_move_pattern)
        return count
