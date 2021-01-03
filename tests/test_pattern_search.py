from utils.pattern_search import *
import unittest


class TestPatternSearch(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestPatternSearch, self).__init__(*args, **kwargs)
        self.vert_pattern = Pattern([{0: {None}},
                                     {0: {None}}], 2, 1, True)
        self.hor_pattern = Pattern([{0: {None}, 1: {None}}], 1, 2, False)
        self.empty_board = [[None, None, None] for _ in range(3)]
        self.pattern_search = PatternSearch()

    def test_horizontal_pattern_empty_board(self):
        count = self.pattern_search.count_occurrences_of_pattern(
            self.empty_board, self.hor_pattern)
        self.assertEqual(count, 6)

    def test_vertical_pattern_empty_board(self):
        count = self.pattern_search.count_occurrences_of_pattern(
            self.empty_board, self.vert_pattern)
        self.assertEqual(count, 6)

    def test_pattern_non_empty_board_vert(self):
        board = [[None, 1, None],
                 [None, 1, None], [None, 1, None]]
        count = self.pattern_search.count_occurrences_of_pattern(
            board, self.vert_pattern)
        self.assertEqual(count, 4)

    def test_pattern_non_empty_board_vert_skips(self):
        board = [[None, 1, None],
                 [None, 1, None], [None, 1, None]]
        count = self.pattern_search.count_occurrences_of_pattern(
            board, self.vert_pattern, True)
        self.assertEqual(count, 2)

    def test_pattern_non_empty_board_hor(self):
        board = [[None, None, None],
                 [2, 2, None], [None, None, None]]
        count = self.pattern_search.count_occurrences_of_pattern(
            board, self.hor_pattern)
        self.assertEqual(count, 4)

    def test_pattern_non_empty_board_hor_skips(self):
        board = [[None, None, None],
                 [2, 2, None], [None, None, None]]
        count = self.pattern_search.count_occurrences_of_pattern(
            board, self.hor_pattern, skip_ahead=True)
        self.assertEqual(count, 2)
