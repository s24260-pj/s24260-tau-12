import random


class Board:
    def __init__(self, rows=5, cols=5, obstacle_prob=0.2):
        self.rows = rows
        self.cols = cols
        self.grid = [[' ' for _ in range(cols)] for _ in range(rows)]

        self.obstacle_prob = obstacle_prob

        self.start = self._place_start_stop('A')
        self.stop = self._place_start_stop('B')

        self._place_obstacles()

    def _place_start_stop(self, symbol):
        positions = self._get_edge_positions()
        pos = random.choice(positions)
        self.grid[pos[0]][pos[1]] = symbol
        return pos

    def _get_edge_positions(self):
        positions = []
        for i in range(self.rows):
            positions.append((i, 0))
            positions.append((i, self.cols - 1))
        for j in range(1, self.cols - 1):
            positions.append((0, j))
            positions.append((self.rows - 1, j))
        return positions

    def _place_obstacles(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == ' ' and random.random() < self.obstacle_prob:
                    self.grid[i][j] = 'X'

    def display(self):
        for row in self.grid:
            print(' '.join(row))
