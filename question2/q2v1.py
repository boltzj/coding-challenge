#!/usr/bin/python

__author__ = 'boltz_j'

import sys
import os.path

directions = "NESW"


class Robot:
    def __init__(self, x, y, direction, board_width, board_height):
        """
        Initialize a robot with position, direction and board limits
        :param x: Initial X position
        :param y: Initial Y position
        :param direction: Initial direction
        :param board_width: Board width
        :param board_height: Board height
        :return:
        """
        self.x = x
        self.y = y
        self.direction = direction
        self.board_width = board_width
        self.board_height = board_height

    def run(self, command):
        """
        Run a robot, the robot follow the command string instruction and print his final position
        :param command:
        :return:
        """
        # Iterate on every char of the command string
        for cmd in command:
            # Left
            if cmd == "L":
                self.left()
            # Right
            elif cmd == "R":
                self.right()
            # Move
            elif cmd == "M":
                self.move()

        # Print Final position
        print(self.x, self.y, directions[self.direction])

    def left(self):
        """
        Turn Left
        :return:
        """
        self.direction = (self.direction + 3) % 4

    def right(self):
        """
        Turn right
        :return:
        """
        self.direction = (self.direction + 1) % 4

    def move(self):
        """
        Move straight
        :return:
        """
        # North
        if self.direction == 0:
            # Check not going out of the board
            if self.y < self.board_height:
                self.y += 1
        # East
        elif self.direction == 1:
            # Check not going out of the board
            if self.x < self.board_width:
                self.x += 1
        # South
        elif self.direction == 2:
            # Check not going out of the board
            if self.y > 0:
                self.y -= 1
        # West
        elif self.direction == 3:
            # Check not going out of the board
            if self.x > 0:
                self.x -= 1


def main(argv):

    if len(sys.argv) < 2:
        print('Usage: \'' + sys.argv[0], 'input_file\'')
        sys.exit(1)

    if not os.path.isfile(sys.argv[1]):
        print(sys.argv[1], 'is not a valid file')
        sys.exit(2)

    # Open the input file
    file = open(sys.argv[1])

    # Read the first line and get the size of the board
    line = file.readline()
    board_width, board_height = map(int, line.split(' '))

    line = file.readline()
    while line:

        # Get the Robot position
        x_, y_, direction = line.split()
        robot = Robot(int(x_), int(y_), directions.find(direction), board_width, board_height)

        # Read commands
        line = file.readline()
        if line:
            # Give commands to the robot
            robot.run(line)

        line = file.readline()

    sys.exit(0)

if __name__ == "__main__":
   main(sys.argv[1:])