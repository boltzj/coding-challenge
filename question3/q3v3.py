#!/usr/bin/python

__author__ = 'boltz_j'

import os.path
import sys

if len(sys.argv) < 2:
    print('Usage: \'' + sys.argv[0], 'log_file\'')
    sys.exit(1)

if not os.path.isfile(sys.argv[1]):
    print(sys.argv[1], 'is not a valid file')
    sys.exit(2)

# Dictionary to store aggregate data from the log file
data = dict()

for line in open(sys.argv[1]):

    # Split the line with space char
    buffer = line.split()

    # Extract data
    service = buffer[4].split('[')[0]
    user = buffer[5][1:-1]
    command = buffer[6]

    # Save extracted data in dict
    if (service, user, command) not in data:
        data[(service, user, command)] = 1
    else:
        data[(service, user, command)] += 1

# Print results
for elt in data:
    print(elt[0], elt[1], elt[2], data[elt])