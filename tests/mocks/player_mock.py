from domineering.DomineeringPlayer import DomineeringPlayer


class PlayerMock(DomineeringPlayer):
    def __init__(self, turns):
        self.turns = turns
        self.pos = 0
        self.get_turn_call_count = 0

    def get_turn(self, board):
        self.get_turn_call_count += 1
        turn = self.turns[self.pos]
        self.pos += 1
        return turn
