from src.evaluation_function import EvaluationFunction
from src.possible_moves_evaluation import PossibleMovesEvaluation
from utils.pattern_search import Pattern, PatternSearch


class RealPossibleMovesEvaluation(PossibleMovesEvaluation):

    def _count_hor_moves(self, board):
        count = self.pattern_search.count_occurrences_of_pattern(
            board, PossibleMovesEvaluation.hor_move_pattern, True)
        return count

    def _count_vert_moves(self, board):
        count = self.pattern_search.count_occurrences_of_pattern(
            board, PossibleMovesEvaluation.vert_move_pattern, True)
        return count
