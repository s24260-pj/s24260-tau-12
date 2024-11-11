import unittest
from game.board import Board
from game.player import Player


class TestPlayerMovement(unittest.TestCase):
    def setUp(self):
        self.board = Board(5, 5, 0)
        self.player = Player(self.board, start=self.board.start)

    def test_move_left_normal(self):
        self.player.position = (2, 2)
        initial_position = self.player.position

        self.player.move('left')
        self.assertEqual(self.player.position, (initial_position[0], initial_position[1] - 1))

    def test_move_left_with_obstacle(self):
        self.board.grid[2][1] = 'X'
        self.player.position = (2, 2)
        initial_position = self.player.position

        self.assertFalse(self.player.move('left'))
        self.assertEqual(self.player.position, initial_position)

    def test_move_left_out_of_bounds(self):
        self.player.position = (2, 0)
        initial_position = self.player.position

        self.assertFalse(self.player.move('left'))
        self.assertEqual(self.player.position, initial_position)

    def test_move_right_normal(self):
        self.player.position = (2, 2)
        initial_position = self.player.position

        self.player.move('right')
        self.assertEqual(self.player.position, (initial_position[0], initial_position[1] + 1))

    def test_move_right_with_obstacle(self):
        self.board.grid[2][3] = 'X'
        self.player.position = (2, 2)
        initial_position = self.player.position

        self.assertFalse(self.player.move('right'))
        self.assertEqual(self.player.position, initial_position)

    def test_move_right_out_of_bounds(self):
        self.player.position = (2, 4)
        initial_position = self.player.position

        self.assertFalse(self.player.move('right'))
        self.assertEqual(self.player.position, initial_position)

    def test_move_up_normal(self):
        self.player.position = (2, 2)
        initial_position = self.player.position

        self.player.move('up')
        self.assertEqual(self.player.position, (initial_position[0] - 1, initial_position[1]))

    def test_move_up_with_obstacle(self):
        self.board.grid[1][2] = 'X'
        self.player.position = (2, 2)
        initial_position = self.player.position

        self.assertFalse(self.player.move('up'))
        self.assertEqual(self.player.position, initial_position)

    def test_move_up_out_of_bounds(self):
        self.player.position = (0, 2)
        initial_position = self.player.position

        self.assertFalse(self.player.move('up'))
        self.assertEqual(self.player.position, initial_position)

    def test_move_down_normal(self):
        self.player.position = (2, 2)
        initial_position = self.player.position

        self.player.move('down')
        self.assertEqual(self.player.position, (initial_position[0] + 1, initial_position[1]))

    def test_move_down_with_obstacle(self):
        self.board.grid[3][2] = 'X'
        self.player.position = (2, 2)
        initial_position = self.player.position

        self.assertFalse(self.player.move('down'))
        self.assertEqual(self.player.position, initial_position)

    def test_move_down_out_of_bounds(self):
        self.player.position = (4, 2)
        initial_position = self.player.position

        self.assertFalse(self.player.move('down'))
        self.assertEqual(self.player.position, initial_position)


if __name__ == '__main__':
    unittest.main()
