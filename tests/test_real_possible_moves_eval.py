import unittest
from domineering.real_possible_moves_evaluation import RealPossibleMovesEvaluation
from domineering.board import Board


class TestPossibleMovesEval(unittest.TestCase):
    def test_evaluation_empty_board(self):
        board = Board.from_string('EEE;EEE;EEE')
        testee = RealPossibleMovesEvaluation()
        result = testee(board)
        self.assertEqual(result, 0)

    def test_evaluation_hor_line_board(self):
        board = Board.from_string('EEE;HHH;EEE')
        testee = RealPossibleMovesEvaluation()
        result = testee(board)
        self.assertEqual(result, -2)

    def test_evaluation_vert_line_board(self):
        board = Board.from_string('EVE;EVE;EVE')
        testee = RealPossibleMovesEvaluation()
        result = testee(board)
        self.assertEqual(result, 2)

    def test_evaluation_mixed_board(self):
        board = Board.from_string('EVE;EVE;EEE')
        testee = RealPossibleMovesEvaluation()
        result = testee(board)
        self.assertEqual(result, 1)
