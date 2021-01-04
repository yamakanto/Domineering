import unittest


class TestAI(unittest.TestCase):
    def assert_move_in(self, move, move_list):
        if move in move_list:
            message = 'OK'
            result = True
        else:
            raise AssertionError(f'move {move} not in {move_list}')
        self.assertTrue(result, message)
