import unittest
from domineering.first_choice_ai import FirstChoiceAI
from domineering.board import Board
from tests.test_ai import TestAI


class TestFirstChoiceAI(TestAI):
    def test_valid_move_empty_board_horizontal(self):
        board = Board.from_string('EEE;EEE;EEE')
        ai = FirstChoiceAI(False)
        move = ai.get_turn(board)
        possible_moves = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
        self.assert_move_in(move, possible_moves)

    def test_valid_move_mixed_board_horizontal(self):
        board = Board.from_string('VEE;EEV;EVE')
        ai = FirstChoiceAI(False)
        move = ai.get_turn(board)
        possible_moves = [(0, 1), (1, 0)]
        self.assert_move_in(move, possible_moves)

    def test_valid_move_empty_board_vertical(self):
        board = Board.from_string('EEE;EEE;EEE')
        ai = FirstChoiceAI(True)
        move = ai.get_turn(board)
        possible_moves = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
        self.assert_move_in(move, possible_moves)

    def test_valid_move_mixed_board_vertical(self):
        board = Board.from_string('VEE;EEV;EVE')
        ai = FirstChoiceAI(True)
        move = ai.get_turn(board)
        possible_moves = [(0, 1), (1, 0)]
        self.assert_move_in(move, possible_moves)
