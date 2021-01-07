from domineering.DomineeringPlayer import DomineeringPlayer
from domineering.board_analyzer import can_make_move, is_border_move, is_safe_move
from domineering.lookahead_depth import ConstantLookaheadDepth, ProgressiveLookaheadDepth


class StrategyAI(DomineeringPlayer):
    def __init__(self, vertical, evaluation, lookahead_depth=1):
        self.vertical = vertical
        self.__evaluation = evaluation
        if isinstance(lookahead_depth, int):
            self.__lookahead_depth_func = ConstantLookaheadDepth(
                lookahead_depth)
        elif isinstance(lookahead_depth, ConstantLookaheadDepth) or isinstance(lookahead_depth, ProgressiveLookaheadDepth):
            self.__lookahead_depth_func = lookahead_depth
        else:
            raise ValueError('Invalid lookahead')
        self.possible_moves_cache = {self.vertical: None, not vertical: None}
        self.safe_moves_cache = {self.vertical: None, not vertical: None}
        self.try_opt = True
        self.num_turns = 0

    def get_turn(self, board):
        self.__update_lookahead()
        if self.try_opt:
            if self.possible_moves_cache[self.vertical] is not None:
                self.__update_moves_cache(board)
            else:
                self.__init_caches(board)

            if len(self.safe_moves_cache[self.vertical]) == len(self.possible_moves_cache[self.vertical]):
                return self.__choose_best_safe_move(board)

        self.num_turns += 1
        best_move, _ = self.__explore_possible_moves(board, 1, self.vertical)
        return best_move

    def __choose_best_safe_move(self, board):
        best_move = None
        best_score = self.__get_initial_score(self.vertical)
        for move in self.safe_moves_cache[self.vertical]:
            board_after_move = self._board_after_move(
                board, move, self.vertical)
            score = self.__evaluation(board_after_move)
            if self.__score_is_better(score, best_score, self.vertical):
                best_move = move
                best_score = score
        return best_move

    def __update_moves_cache(self, board):
        for vertical in [True, False]:
            self.possible_moves_cache[vertical] = self.__get_potential_moves(
                board, vertical)
            self.safe_moves_cache[vertical] = self.__get_safe_moves(
                board, vertical)

    def __init_caches(self, board):
        self.possible_moves_cache[True] = set(self.compute_possible_moves(
            board, True))
        self.possible_moves_cache[False] = set(self.compute_possible_moves(
            board, False))
        self.safe_moves_cache[True] = set(self.compute_safe_moves(
            board, True))
        self.safe_moves_cache[False] = set(self.compute_safe_moves(
            board, False))

    def __update_lookahead(self):
        self.__lookahead_depth = self.__lookahead_depth_func(self.num_turns)

    def __explore_possible_moves(self, board, depth, vertical):
        moves = self.__compute_sensible_moves(board, vertical)
        best_move = None
        score = self.__get_initial_score(vertical)
        for move in moves:
            score_after_move = self.__score_after_move(
                board, move, vertical, depth)
            if self.__score_is_better(score_after_move, score, vertical):
                best_move = move
                score = score_after_move
        return best_move, score

    def __get_initial_score(self, vertical):
        if vertical:
            return float('-inf')
        else:
            return float('inf')

    def __score_after_move(self, board, move, vertical, depth):
        board_after_move = self._board_after_move(board, move, vertical)
        if depth < self.__lookahead_depth:
            _, score_after_move = self.__explore_possible_moves(
                board_after_move, 2, not vertical)
        else:
            score_after_move = self.__evaluation(board_after_move)
        return score_after_move

    def __score_is_better(self, new_score, old_score, vertical):
        if vertical:
            return new_score > old_score
        else:
            return new_score < old_score

    def __compute_sensible_moves(self, board, vertical):
        possible_moves = self.__get_potential_moves(board, vertical)
        sensible_moves = possible_moves - self.safe_moves_cache[vertical]

        if not sensible_moves:
            return possible_moves
        return sensible_moves

    def __get_potential_moves(self, board, vertical):
        return {move for move in self.possible_moves_cache[vertical] if can_make_move(board, move, vertical)}

    def __get_safe_moves(self, board, vertical):
        return {move for move in self.possible_moves_cache[vertical] if is_safe_move(board, move, vertical)}

    def __get_border_moves(self, board, vertical, moves):
        border_moves = set()
        for move in moves:
            if not is_border_move(board, move, vertical):
                border_moves.add(move)
        return border_moves
