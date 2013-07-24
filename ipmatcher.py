#!/usr/bin/env python

# irc-ip-nick-matcher 
# version: 0.1
# Author: Stuart Banks (JFreegman@gmail.com)

import re
import sys

LOGPATHFILE = open("logpath", 'r')

def match_IP(ipCheck):
    PATH = open("".join(L for L in LOGPATHFILE).strip())

    # find lines from log in which a user's IP is displayed
    IP_Lines = [line.strip() for line in PATH if re.search(r'( \*.* \(.*\@.*\))', line)]

    # get unique nick matches
    nickMatches = set()
    for line in IP_Lines:
        start, end = line.find('@')+1, line.find(')')
        IP = line[start:end]
        if IP in ipCheck:
            start, end = line.find('*')+2, line.find('(')-1
            nick = line[start:end]
            if nick[0] in '@+%':    # remove special chars from nick
                nick = nick[1:]
            nickMatches.add(nick)

    if not nickMatches:
        print "No matches for: " + ipCheck
    else:
        print 'Nick matches for ' + ipCheck + ':'
        for nick in nickMatches:
            print nick

    PATH.close()
    LOGPATHFILE.close()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: Match an IP Address to its associated nicks"
        sys.exit(1)
    match_IP(sys.argv[1])
