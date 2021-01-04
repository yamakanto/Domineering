import unittest

from domineering.board import Board
from domineering.board_analyzer import *


class TestBoardAnalyzer(unittest.TestCase):

    def test_can_make_move_horizontal(self):
        board = Board.from_string('EEV;EVV;VEE')
        self.assertTrue(can_make_move(board, (0, 0), False))
        self.assertTrue(can_make_move(board, (2, 1), False))
        self.assertFalse(can_make_move(board, (0, 1), False))
        self.assertFalse(can_make_move(board, (1, 1), False))
        self.assertFalse(can_make_move(board, (2, 0), False))

    def test_can_make_move_vertical(self):
        board = Board.from_string('EEV;EVV;VEE')
        self.assertTrue(can_make_move(board, (0, 0), True))
        self.assertFalse(can_make_move(board, (2, 1), True))
        self.assertFalse(can_make_move(board, (0, 1), True))
        self.assertFalse(can_make_move(board, (1, 1), True))
        self.assertFalse(can_make_move(board, (2, 0), True))

    def test_count_horizontal_moves_empty_skip(self):
        board = Board.from_string('EEE;EEE;EEE')
        count = count_moves_horizontal(board, True)
        self.assertEqual(count, 3)

    def test_count_horizontal_moves_empty(self):
        board = Board.from_string('EEE;EEE;EEE')
        count = count_moves_horizontal(board, False)
        self.assertEqual(count, 6)

    def test_count_vertical_moves_empty_skip(self):
        board = Board.from_string('EEE;EEE;EEE')
        count = count_moves_vertical(board, True)
        self.assertEqual(count, 3)

    def test_count_vertical_moves_empty(self):
        board = Board.from_string('EEE;EEE;EEE')
        count = count_moves_vertical(board, False)
        self.assertEqual(count, 6)

    def test_is_safe_move_horizontal(self):
        board = Board.from_string('EEEE;HHEE;EEEE')
        self.assertTrue(is_safe_move(board, (0, 0), False))
        self.assertFalse(is_safe_move(board, (0, 1), False))
        self.assertFalse(is_safe_move(board, (0, 2), False))

    def test_count_safe_moves_horizontal_skip(self):
        board = Board.from_string('EEEE;HHHE;EEEE')
        count = count_safe_moves_horizontal(board, True)
        self.assertEqual(count, 2)

    def test_count_safe_moves_horizontal(self):
        board = Board.from_string('EEEE;HHHE;EEEE')
        count = count_safe_moves_horizontal(board, False)
        self.assertEqual(count, 4)

    def test_count_safe_moves_vertical_skip(self):
        board = Board.from_string('EVE;EVE;EVE;EEE')
        count = count_safe_moves_vertical(board, True)
        self.assertEqual(count, 2)

    def test_count_safe_moves_vertical(self):
        board = Board.from_string('EVE;EVE;EVE;EEE')
        count = count_safe_moves_vertical(board, False)
        self.assertEqual(count, 4)
