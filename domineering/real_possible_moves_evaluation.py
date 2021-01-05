from domineering.possible_moves_evaluation import PossibleMovesEvaluation
from domineering.board import Board
from domineering.board_analyzer import count_moves_horizontal, count_moves_vertical


class RealPossibleMovesEvaluation(PossibleMovesEvaluation):

    def __init__(self):
        super().__init__()
        self._skip_ahead = True
