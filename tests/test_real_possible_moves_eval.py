import unittest
from domineering.real_possible_moves_evaluation import RealPossibleMovesEvaluation


class TestPossibleMovesEval(unittest.TestCase):
    def test_evaluation_empty_board(self):
        board = [[None, None, None] for _ in range(3)]
        testee = RealPossibleMovesEvaluation()
        result = testee(board)
        self.assertEqual(result, 0)

    def test_evaluation_hor_line_board(self):
        board = [[None, None, None],
                 [2, 2, 2], [None, None, None]]
        testee = RealPossibleMovesEvaluation()
        result = testee(board)
        self.assertEqual(result, -2)

    def test_evaluation_vert_line_board(self):
        board = [[None, 1, None],
                 [None, 1, None], [None, 1, None]]
        testee = RealPossibleMovesEvaluation()
        result = testee(board)
        self.assertEqual(result, 2)

    def test_evaluation_mixed_board(self):
        board = [[None, 1, None],
                 [None, 1, None], [None, None, None]]
        testee = RealPossibleMovesEvaluation()
        result = testee(board)
        self.assertEqual(result, 1)
