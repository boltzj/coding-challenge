__author__ = 'boltz_j'

class Cell:
    status = 'Unknown'

    def __init__(self):
        self.status = '?'

    def __repr__(self):
        return self.status

    def explore(self):
        self.status('X')

class Board:
    x = 0
    y = 0

    def __init__(self, x_size, y_size):
        self.board = [[Cell() for i in range(x_size)] for j in range(y_size)]
        self.x = x_size
        self.y = y_size
        self.robots = []

    def add_robot(self, x, y, direction):
        robot = Robot(x, y, direction)
        self.robots.append(robot)

        # FIXME: Check if there is already something ???
        self.board[x][y] = robot

    def print_board(self):
        for row in self.board:
            print(row)
        print()


class Robot:
    x = 0
    y = 0
    direction = 'N'

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def __repr__(self):
        return 'R'

    def move(self):
        if self.direction == 'N':
            self.y += 1

board = Board(10, 10)

board.print_board()

board.add_robot(0, 0, 'N')

board.print_board()