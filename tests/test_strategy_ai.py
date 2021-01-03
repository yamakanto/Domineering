import unittest
from src.DomineeringGame import board_from_string
from src.strategy_ai import StrategyAI
from src.possible_moves_safe_moves_evaluation import SafeRealPossibleMovesEvaluation


class TestStrategyAI(unittest.TestCase):
    def test_simple_move_lookahead_one(self):
        board_string = '  1 \n221 \n  1 \n  1 '
        board = board_from_string(board_string)
        evaluation = SafeRealPossibleMovesEvaluation()
        ai = StrategyAI(False, evaluation, 1)
        move = ai.get_turn(board)
        self.assertTrue(move in [(2, 0), (3, 0)])

    def test_simple_move_lookahead_two(self):
        board_string = '  1 \n221 \n  1 \n  1 '
        board = board_from_string(board_string)
        evaluation = SafeRealPossibleMovesEvaluation()
        ai = StrategyAI(False, evaluation, 2)
        move = ai.get_turn(board)
        self.assertTrue(move in [(2, 0), (3, 0)])
