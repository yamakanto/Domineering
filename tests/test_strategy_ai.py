import unittest
#from src.DomineeringGame import board_from_string
from src.strategy_ai import StrategyAI
from src.possible_moves_safe_moves_evaluation import SafeRealPossibleMovesEvaluation
from src.board import Board


class TestStrategyAI(unittest.TestCase):
    def test_simple_move_lookahead_one(self):
        board_string = 'EEVE;HHVE;EEVE;EEVE'
        board = Board.from_string(board_string)
        evaluation = SafeRealPossibleMovesEvaluation()
        ai = StrategyAI(False, evaluation, 1)
        move = ai.get_turn(board)
        self.assert_move_in(move, [(2, 0), (3, 0)])

    def assert_move_in(self, move, move_list):
        if move in move_list:
            message = 'OK'
            result = True
        else:
            message = f'move {move} not in {move_list}'
            result = False
        self.assertTrue(result, message)

    def test_simple_move_lookahead_two(self):
        board_string = 'EEVE;HHVE;EEVE;EEVE'
        board = Board.from_string(board_string)
        evaluation = SafeRealPossibleMovesEvaluation()
        ai = StrategyAI(False, evaluation, 2)
        move = ai.get_turn(board)
        self.assert_move_in(move, [(2, 0), (3, 0)])

    def test_bug01_invalid_move_chosen(self):
        '''
         ̲ ̲1̲ ̲2̲ ̲3̲ ̲4̲ ̲5̲
        1|V V V V
        2|V V V V
        3|      H H
        4|H H   H H
        5|
        '''
        board_string = 'VVVVE;VVVVE;EEEHH;HHEHH;EEEEE'
        board = Board.from_string(board_string)
        evaluation = SafeRealPossibleMovesEvaluation()
        ai = StrategyAI(False, evaluation, 2)
        move = ai.get_turn(board)
        self.assertTrue(
            move in [(2, 0), (2, 1), (4, 0), (4, 1), (4, 2), (4, 3)])
