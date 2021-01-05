import unittest
from domineering.possible_moves_evaluation import PossibleMovesEvaluation
from domineering.board import Board


class TestPossibleMovesEval(unittest.TestCase):
    def test_evaluation_empty_board(self):
        board = Board.from_string('EEE;EEE;EEE')
        testee = PossibleMovesEvaluation()
        result = testee(board)
        self.assertEqual(result, 0)

    def test_evaluation_hor_line_board(self):
        board = Board.from_string('EEE;HHH;EEE')
        testee = PossibleMovesEvaluation()
        result = testee(board)
        self.assertEqual(result, -4)

    def test_evaluation_vert_line_board(self):
        board = Board.from_string('EVE;EVE;EVE')
        testee = PossibleMovesEvaluation()
        result = testee(board)
        self.assertEqual(result, 4)

    def test_evaluation_mixed_board(self):
        board = Board.from_string('EVE;EVE;EEE')
        testee = PossibleMovesEvaluation()
        result = testee(board)
        self.assertEqual(result, 2)
