import unittest
from domineering.possible_moves_safe_moves_evaluation import SafeRealPossibleMovesEvaluation


class TestSafeRealPossibleMovesEval(unittest.TestCase):
    def test_evaluation_empty_board(self):
        board = [[None, None, None] for _ in range(3)]
        testee = SafeRealPossibleMovesEvaluation()
        result = testee(board)
        self.assertEqual(result, 0)

    def test_evaluation_hor_line_board(self):
        board = [[None, None, None],
                 [2, 2, 2], [None, None, None]]
        testee = SafeRealPossibleMovesEvaluation()
        result = testee(board)
        self.assertEqual(result, -6)

    def test_evaluation_vert_line_board(self):
        board = [[None, 1, None],
                 [None, 1, None], [None, 1, None]]
        testee = SafeRealPossibleMovesEvaluation()
        result = testee(board)
        self.assertEqual(result, 6)

    def test_evaluation_mixed_board(self):
        board = [[None, 1, None],
                 [None, 1, None], [None, None, None]]
        testee = SafeRealPossibleMovesEvaluation()
        result = testee(board)
        self.assertEqual(result, 5)
