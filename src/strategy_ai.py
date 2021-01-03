from src.DomineeringPlayer import DomineeringPlayer


class StrategyAI(DomineeringPlayer):
    def __init__(self, vertical, evaluation, lookahead_depth=1):
        self.vertical = vertical
        self.__evaluation = evaluation
        self.__lookahead_depth = lookahead_depth

    def get_turn(self, board):
        '''
        possible_moves = self.compute_possible_moves(board)
        boards = [self._board_after_move(board, move)
                  for move in possible_moves]
        scores = [self.__evaluation(b) for b in boards]
        '''
        '''
        possible_moves, scores = self.__explore_possible_moves(
            board, self.vertical)
        if self.vertical:
            return possible_moves[scores.index(max(scores))]
        else:
            return possible_moves[scores.index(min(scores))]
        '''
        best_move, _ = self.__explore_possible_moves(board, 1, self.vertical)
        return best_move

    def __explore_possible_moves(self, board, depth, vertical):
        possible_moves = self.compute_possible_moves(board, vertical)
        #scores = self.__explore_possible_moves_scores(board, 1, self.vertical)
        best_move = None
        score = self.__get_initial_score(vertical)
        for move in possible_moves:
            board_after_move = self._board_after_move(board, move, vertical)
            if depth < self.__lookahead_depth:
                _, score_after_move = self.__explore_possible_moves(
                    board_after_move, 2, not vertical)
            else:
                score_after_move = self.__evaluation(board_after_move)
            if self.__score_is_better(score_after_move, score, vertical):
                best_move = move
                score = score_after_move
        return best_move, score

    def __get_initial_score(self, vertical):
        if vertical:
            return -10000
        else:
            return 10000

    def __score_is_better(self, new_score, old_score, vertical):
        if vertical:
            return new_score > old_score
        else:
            return new_score < old_score