import unittest
from domineering.possible_moves_evaluation import PossibleMovesEvaluation


class TestPossibleMovesEval(unittest.TestCase):
    def test_evaluation_empty_board(self):
        board = [[None, None, None] for _ in range(3)]
        testee = PossibleMovesEvaluation()
        result = testee(board)
        self.assertEqual(result, 0)

    def test_evaluation_non_empty_board_hor(self):
        board = [[None, None, None],
                 [2, 2, 2], [None, None, None]]
        testee = PossibleMovesEvaluation()
        result = testee(board)
        self.assertEqual(result, -4)

    def test_evaluation_non_empty_board_vert(self):
        board = [[None, 1, None],
                 [None, 1, None], [None, 1, None]]
        testee = PossibleMovesEvaluation()
        result = testee(board)
        self.assertEqual(result, 4)

    def test_evaluation_non_empty_board_mixed(self):
        board = [[None, 1, None],
                 [None, 1, None], [None, None, None]]
        testee = PossibleMovesEvaluation()
        result = testee(board)
        self.assertEqual(result, 2)
