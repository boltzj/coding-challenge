__author__ = 'boltz_j'

import re

data = dict()

# for line in open('test-100M.log'):
for line in open('test-2G.log'):
    # Split the line with space char
    buffer = line.split()

    # Grab the information
    service = re.search("^(.*?)\[(.*?)\]", buffer[4]).group(1)
    user = re.search("^\((.*?)\)", buffer[5]).group(1)
    command = buffer[6]

    if (service, user, command) not in data:
        data[(service, user, command)] = 1
    else:
        data[(service, user, command)] += 1


for elt in data:
    print(elt[0], elt[1], elt[2], data[elt])