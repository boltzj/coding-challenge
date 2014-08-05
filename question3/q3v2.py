#!/usr/bin/python

__author__ = 'boltz_j'

import os.path
import sys
import re

if len(sys.argv) < 2:
    print('Usage: \'' + sys.argv[0], 'log_file\'')
    sys.exit(1)

if not os.path.isfile(sys.argv[1]):
    print(sys.argv[1], 'is not a valid file')
    sys.exit(2)

# Dictionary to store aggregate data from the log file
data = dict()

# Log line example :
#   Dec 10 07:17:01 ip-10-198-43-75 CRON[19220]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
re_line = re.compile("^\S{3}\s.*?\s[0-9:]*?\s.*?\s(.*?)\[.*?\]:\s\((.*?)\)\s(.*?)\s.*?$")

for line in open(sys.argv[1]):

    # Match line with regex and grab groups
    result = re_line.match(line)

    # Extract information from regex matching
    service = result.group(1)
    user = result.group(2)
    command = result.group(3)

    # Save extracted data in dict
    if (service, user, command) not in data:
        data[(service, user, command)] = 1
    else:
        data[(service, user, command)] += 1

# Print results
for elt in data:
    print(elt[0], elt[1], elt[2], data[elt])