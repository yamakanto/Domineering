from src.DomineeringPlayer import DomineeringPlayer
from src.board import Board


class FirstChoiceAI(DomineeringPlayer):
    def __init__(self, vertical):
        super().__init__(vertical)

    def get_turn(self, board):
        possible_moves = self.compute_possible_moves(board, self.vertical)
        return possible_moves[0]
