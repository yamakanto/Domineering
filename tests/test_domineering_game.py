import unittest
from src.DomineeringGame import DomineeringGame
from tests.mocks.player_mock import PlayerMock


class TestDomineeringGame(unittest.TestCase, DomineeringGame):
    def test_init(self):
        player1 = PlayerMock([(0, 0), ])
        player2 = PlayerMock([(1, 1)])
        game = DomineeringGame(3, player1, player2)
        self.assertFalse(game._finished())
        self.assertEqual(game._get_board_parse_string(), 'EEE;EEE;EEE')
        self.assertEqual(player1.get_turn_call_count, 0)
        self.assertEqual(player2.get_turn_call_count, 0)

    def test_full_game(self):
        player1 = PlayerMock([(0, 0), ])
        player2 = PlayerMock([(1, 1)])
        game = DomineeringGame(3, player1, player2)
        game._play_turn()
        self.assertEqual(player1.get_turn_call_count, 1)
        self.assertEqual(game._get_board_parse_string(), 'VEE;VEE;EEE')
        game._play_turn()
        self.assertEqual(player2.get_turn_call_count, 1)
        self.assertEqual(game._get_board_parse_string(), 'VEE;VHH;EEE')
        self.assertTrue(game._finished())

    def test_play_full_game(self):
        player1 = PlayerMock([(0, 0), ])
        player2 = PlayerMock([(1, 1)])
        game = DomineeringGame(3, player1, player2)
        game.play()
        self.assertEqual(game._get_board_parse_string(), 'VEE;VHH;EEE')
        self.assertTrue(game._finished())
        self.assertEqual(player1.get_turn_call_count, 1)
        self.assertEqual(player2.get_turn_call_count, 1)

    def test_play_full_game_player1_wins(self):
        player1 = PlayerMock([(0, 0), (1, 1)])
        player2 = PlayerMock([(0, 1)])
        game = DomineeringGame(3, player1, player2)
        game.play()
        self.assertEqual(game._get_board_parse_string(), 'VHH;VVE;EVE')
        self.assertTrue(game._finished())
        self.assertEqual(player1.get_turn_call_count, 2)
        self.assertEqual(player2.get_turn_call_count, 1)

    def test_play_turn_invalid_move(self):
        player1 = PlayerMock([(5, 5), (0, 0), ])
        player2 = PlayerMock([])
        game = DomineeringGame(3, player1, player2)
        game._play_turn()
        self.assertEqual(player1.get_turn_call_count, 2)
