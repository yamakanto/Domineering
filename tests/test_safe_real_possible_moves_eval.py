import unittest
from domineering.safe_real_possible_moves_evaluation import SafeRealPossibleMovesEvaluation
from domineering.board import Board


class TestSafeRealPossibleMovesEval(unittest.TestCase):
    def test_evaluation_empty_board(self):
        board = Board.from_string('EEE;EEE;EEE')
        testee = SafeRealPossibleMovesEvaluation()
        result = testee(board)
        self.assertEqual(result, 0)

    def test_evaluation_hor_line_board(self):
        board = Board.from_string('EEE;HHH;EEE')
        testee = SafeRealPossibleMovesEvaluation()
        result = testee(board)
        self.assertEqual(result, -6)

    def test_evaluation_vert_line_board(self):
        board = Board.from_string('EVE;EVE;EVE')
        testee = SafeRealPossibleMovesEvaluation()
        result = testee(board)
        self.assertEqual(result, 6)

    def test_evaluation_mixed_board(self):
        board = Board.from_string('EVE;EVE;EEE')
        testee = SafeRealPossibleMovesEvaluation()
        result = testee(board)
        self.assertEqual(result, 5)

    def test_prefers_better_board(self):
        board1 = Board.from_string(
            'EVHHEVE;EVHHEVE;VEEVEVE;VHHVEVE;EVEEEHH;EVHHHHV;HHEEEEV')
        evaluation = SafeRealPossibleMovesEvaluation()
        score1 = evaluation(board1)
        board2 = Board.from_string(
            'EVEHHVE;EVHHEVE;VEEVEVE;VHHVEVE;EVEEEHH;EVHHHHV;HHEEEEV')
        score2 = evaluation(board2)
        self.assertTrue(score1 > score2)
