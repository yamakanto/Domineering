import unittest
from domineering.board import Board
from utils.string_utils import underline


class TestBoard(unittest.TestCase):
    def test_from_string_empty(self):
        board_string = 'EEE;EEE;EEE'
        board = Board.from_string(board_string)
        self.assertEqual(board_string, board.get_parseable_text())
        positions = [(x, y) for x in range(3) for y in range(3)]
        self.assertTrue(board.positions_are_empty(positions))

    def test_from_string_mixed(self):
        board_string = 'EEEE;HHEV;EEEV'
        board = Board.from_string(board_string)
        self.assertTrue(board.positions_are_empty(
            [(0, 0), (0, 1), (0, 2), (0, 3), (1, 2), (2, 0), (2, 1), (2, 2)]))
        self.assertTrue(board.positions_are_occupied(
            [(1, 0), (1, 1), (1, 3), (2, 3)]))

    def test_from_string_mixed2(self):
        board = Board.from_string('EEEE;HHHE;EEEE')
        self.assertTrue(board.positions_are_empty(
            [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)]))
        self.assertTrue(board.positions_are_occupied(
            [(1, 0), (1, 1), (1, 2)]))

    def test_add_move_vertical(self):
        board_string = 'EEE;EEE;EEE'
        board = Board.from_string(board_string)
        board.add_move((0, 0), True)
        expected_state = 'VEE;VEE;EEE'
        self.assertEqual(expected_state, board.get_parseable_text())

    def test_add_move_vertical_occupied(self):
        board_string = 'VEE;VEE;EEE'
        board = Board.from_string(board_string)
        with self.assertRaises(ValueError):
            board.add_move((0, 0), True)

    def test_add_move_horizontal_occupied(self):
        board_string = 'VEE;VEV;EEV'
        board = Board.from_string(board_string)
        with self.assertRaises(ValueError):
            board.add_move((1, 0), False)
        with self.assertRaises(ValueError):
            board.add_move((2, 1), False)

    def test_add_move_horizontal(self):
        board_string = 'EEE;EEE;EEE'
        board = Board.from_string(board_string)
        board.add_move((0, 0), False)
        expected_state = 'HHE;EEE;EEE'
        self.assertEqual(expected_state, board.get_parseable_text())

    def test_remove_move_vertical(self):
        board = Board.from_string('EVE;EVE;HHE')
        board.remove_move((0, 1), True)
        self.assertEqual(board.get_parseable_text(), 'EEE;EEE;HHE')

    def test_remove_move_vertical_empty(self):
        board = Board.from_string('EVE;EVE;HHE')
        with self.assertRaises(ValueError):
            board.remove_move((0, 0), True)

    def test_remove_move_horizontal(self):
        board = Board.from_string('EVE;EVE;HHE')
        board.remove_move((2, 0), False)
        self.assertEqual(board.get_parseable_text(), 'EVE;EVE;EEE')

    def test_remove_move_horizontal_empty(self):
        board = Board.from_string('EVE;EVE;HHE')
        with self.assertRaises(ValueError):
            board.remove_move((0, 0), False)

    def test_str(self):
        board = Board.from_string('EVE;EVE;HHE')
        exp_string = underline('    1 2 3')+'\n 1|   V  \n 2|   V  \n 3| H H  '
        self.assertEqual(exp_string, str(board))
