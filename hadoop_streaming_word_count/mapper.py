#!/usr/bin/env python

# book url: https://www.amazon.com/dp/B01KH9YWSY
import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        print '%s\t%s' % (word, 1)
