import unittest

from domineering.human_player import HumanPlayer
from domineering.board import Board
from tests.mocks.input_mock import InputMock


class TestHumanPlayer(unittest.TestCase):
    def test_empty_board_valid_vertical(self):
        board = Board.from_string('EEE;EEE;EEE')
        mock_input = InputMock(['2,1'])
        player = HumanPlayer(True, mock_input)
        move = player.get_turn(board)
        self.assertEqual(move, (1, 0))
        self.assertEqual(mock_input.call_count, 1)

    def test_empty_board_valid_horizontal(self):
        board = Board.from_string('EEE;EEE;EEE')
        mock_input = InputMock(['2,1'])
        player = HumanPlayer(False, mock_input)
        move = player.get_turn(board)
        self.assertEqual(move, (1, 0))
        self.assertEqual(mock_input.call_count, 1)

    def test_invalid_horizontal_asks_again(self):
        board = Board.from_string('EEE;EHH;EEE')
        mock_input = InputMock(['2,1', '3,1'])
        player = HumanPlayer(False, mock_input)
        move = player.get_turn(board)
        self.assertEqual(move, (2, 0))
        self.assertEqual(mock_input.call_count, 2)

    def test_invalid_input_horizontal_asks_again(self):
        board = Board.from_string('EEE;EHH;EEE')
        mock_input = InputMock(['wrong', '3,1'])
        player = HumanPlayer(False, mock_input)
        move = player.get_turn(board)
        self.assertEqual(move, (2, 0))
        self.assertEqual(mock_input.call_count, 2)

    def test_invalid_vertical_asks_again(self):
        board = Board.from_string('EEE;EHH;EEE')
        mock_input = InputMock(['2,2', '2,1'])
        player = HumanPlayer(True, mock_input)
        move = player.get_turn(board)
        self.assertEqual(move, (1, 0))
        self.assertEqual(mock_input.call_count, 2)

    def test_invalid_input_vertical_asks_again(self):
        board = Board.from_string('EEE;EHH;EEE')
        mock_input = InputMock(['wrong', '2,1'])
        player = HumanPlayer(True, mock_input)
        move = player.get_turn(board)
        self.assertEqual(move, (1, 0))
        self.assertEqual(mock_input.call_count, 2)

    def test_input_is_poss_moves_vertical_asks_again(self):
        board = Board.from_string('EEE;EHH;EEE')
        mock_input = InputMock(['poss_moves', '2,1'])
        player = HumanPlayer(True, mock_input)
        move = player.get_turn(board)
        self.assertEqual(move, (1, 0))
        self.assertEqual(mock_input.call_count, 2)
