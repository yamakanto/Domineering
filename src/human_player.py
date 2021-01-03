from src.DomineeringPlayer import DomineeringPlayer


class HumanPlayer(DomineeringPlayer):
    def __init__(self, vertical):
        super().__init__(vertical)

    def get_turn(self, board):
        while True:
            human_input = input('Please enter a turn (format: row,col):')
            if human_input == 'poss_moves':
                print(self.compute_possible_moves(board))
            try:
                row, col = human_input.split(',')
                row = int(row)-1
                col = int(col)-1
                if self._can_move_to_pos(row, col, board):
                    return row, col
            except:
                continue
