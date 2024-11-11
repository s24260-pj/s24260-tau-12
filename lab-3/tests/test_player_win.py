import unittest
from game.board import Board
from game.player import Player


class TestPlayerWin(unittest.TestCase):
    def setUp(self):
        self.board = Board(5, 5, 3)
        self.player = Player(self.board, start=self.board.start)

    def test_player_wins_when_reaches_stop(self):
        self.player.position = (self.board.stop[0] - 1, self.board.stop[1])
        self.assertTrue(self.player.move('down'))

        self.assertEqual(self.player.position, self.board.stop)


if __name__ == '__main__':
    unittest.main()
