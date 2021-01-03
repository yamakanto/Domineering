from utils.pattern_search import Pattern, PatternSearch
from src.real_possible_moves_evaluation import RealPossibleMovesEvaluation


class SafeRealPossibleMovesEvaluation(RealPossibleMovesEvaluation):

    def __call__(self, board):
        possible_moves_diff = self._compute_possible_moves_diff(board)
        safe_moves_diff = self._compute_safe_move_diff(board)
        return 2*safe_moves_diff + possible_moves_diff

    def _compute_safe_move_diff(self, board):
        return self.__count_vertical_safe_moves(board)-self.__count_horizontal_safe_moves(board)

    def __count_vertical_safe_moves(self, board):
        vertical_safe_moves_pattern_left = Pattern(
            [{0: {None}, 1: {1, 2}}, {0: {None}, 1: {1, 2}}], row_nr=2, col_nr=2, vertical=True)
        vertical_safe_moves_pattern_right = Pattern(
            [{0: {1, 2}, 1: {None}}, {0: {1, 2}, 1: {None}}], 2, 2, True)
        vertical_safe_moves_pattern_middle = Pattern(
            [{0: {1, 2}, 1: {None}, 2: {1, 2}}, {0: {1, 2}, 1: {1, 2}, 2: {None}}], 2, 3, True)
        count = 0
        count += self.pattern_search.count_occurrences_of_pattern(board,
                                                                  vertical_safe_moves_pattern_left, True, {'col': (0, 2)})
        count += self.pattern_search.count_occurrences_of_pattern(board,
                                                                  vertical_safe_moves_pattern_middle, True)
        count += self.pattern_search.count_occurrences_of_pattern(board,
                                                                  vertical_safe_moves_pattern_right, True, {'col': (len(board[0])-2, len(board[0]))})
        return count

    def __count_horizontal_safe_moves(self, board):
        horizontal_safe_moves_pattern_top = Pattern(
            [{0: {None}, 1: {None}}, {0: {1, 2}, 1: {1, 2}}], row_nr=2, col_nr=2, vertical=False)
        horizontal_safe_moves_pattern_bottom = Pattern(
            [{0: {1, 2}, 1: {1, 2}}, {0: {None}, 1: {None}}], 2, 2, False)
        horizontal_safe_moves_pattern_middle = Pattern(
            [{0: {1, 2}, 1: {1, 2}}, {0: {None}, 1: {None}}, {0: {1, 2}, 1: {1, 2}}], 3, 2, True)
        count = 0
        count += self.pattern_search.count_occurrences_of_pattern(board,
                                                                  horizontal_safe_moves_pattern_top, True, {'row': (0, 2)})
        count += self.pattern_search.count_occurrences_of_pattern(board,
                                                                  horizontal_safe_moves_pattern_middle, True)
        count += self.pattern_search.count_occurrences_of_pattern(board,
                                                                  horizontal_safe_moves_pattern_bottom, True, {'row': (len(board)-2, len(board))})
        return count
