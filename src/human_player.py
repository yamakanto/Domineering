from src.DomineeringPlayer import DomineeringPlayer


class HumanPlayer(DomineeringPlayer):
    def __init__(self, vertical, input_func=input):
        super().__init__(vertical)
        self.input_func = input_func

    def get_turn(self, board):
        while True:
            human_input = self.input_func(
                'Please enter a turn (format: row,col):')
            if human_input == 'poss_moves':
                print(self.compute_possible_moves(board, self.vertical))
            try:
                row, col = human_input.split(',')
                row = int(row)-1
                col = int(col)-1
                if self._can_move_to_pos(row, col, board, self.vertical):
                    return row, col
            except:
                continue
