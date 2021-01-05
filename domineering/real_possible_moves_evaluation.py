from domineering.possible_moves_evaluation import PossibleMovesEvaluation
from domineering.board import Board
from domineering.board_analyzer import count_moves_horizontal, count_moves_vertical


class RealPossibleMovesEvaluation(PossibleMovesEvaluation):

    def _count_hor_moves(self, board):
        return count_moves_horizontal(board)

    def _count_vert_moves(self, board):
        return count_moves_vertical(board)
