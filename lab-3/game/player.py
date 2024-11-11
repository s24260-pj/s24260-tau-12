class Player:
    def __init__(self, board, start):
        self.board = board
        self.position = start

    def move(self, direction):
        directions = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }
        if direction not in directions:
            return False

        new_position = (
            self.position[0] + directions[direction][0],
            self.position[1] + directions[direction][1]
        )

        if self._can_move(new_position):
            self.position = new_position
            return True

        return False

    def _can_move(self, position):
        x, y = position

        if 0 <= x < self.board.rows and 0 <= y < self.board.cols:
            return self.board.grid[x][y] != 'X'

        return False
