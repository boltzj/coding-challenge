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
        robot = Robot(int(x_), int(y_), directions.find(direction))

        # Read commands
        line = file.readline()
        if line:
            # Give commands to the robot
            robot.action(line)

        line = file.readline()


class Robot:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def action(self, command):
        # Iterate on every char
        for cmd in command:
            if cmd == "L":
                self.left()

            elif cmd == "R":
                self.right()

            elif cmd == "M":
                self.move()

        print(self.x, self.y, directions[self.direction])

    def left(self):
        self.direction = (self.direction + 3) % 4

    def right(self):
        self.direction = (self.direction + 1) % 4

    def move(self):
        # North
        if self.direction == 0:
            self.y += 1
        # East
        elif self.direction == 1:
            self.x += 1
        # South
        elif self.direction == 2:
            self.y -= 1
        # West
        elif self.direction == 3:
            self.x -= 1


parse_input_file('test_input.txt')