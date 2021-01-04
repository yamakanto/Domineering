from domineering.DomineeringPlayer import DomineeringPlayer
from domineering.board import Board


class FirstChoiceAI(DomineeringPlayer):
    def __init__(self, vertical):
        super().__init__(vertical)

    def get_turn(self, board):
        possible_moves = self.compute_possible_moves(board, self.vertical)
        if not possible_moves:
            raise RuntimeError('No possible move left!')
        return possible_moves[0]
