__author__ = 'boltz_j'

directions = "NESW"

def parse_input_file(filename):
    # Open the input file
    file = open(filename)

    # Read the first line and get the size of the board
    line = file.readline()
    x, y = map(int, line.split(' '))

    line = file.readline()
    while line:

        # Get the Robot position
        x_, y_, direction = line.split()
        print(int(x_), int(y_), directions.find(direction))

        line = file.readline()

        if line:
            # Add commands to robot
            print("robot commands : ", line)

            robot = Robot(int(x_), int(y_), directions.find(direction), line)
            robot.action()
        line = file.readline()


class Robot:
    def __init__(self, x, y, direction, command):
        self.x = x
        self.y = y
        self.direction = direction
        self.command = command
        self.cmd_index = 0

    def action(self):
        # Get command
        cmd = self.command[self.cmd_index]
        self.cmd_index += 1

        print(cmd)



directions = "NESW"

parse_input_file('test_input.txt')