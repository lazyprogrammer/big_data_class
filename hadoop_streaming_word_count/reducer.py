#!/usr/bin/env python

# book url: https://www.amazon.com/dp/B01KH9YWSY
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue

    if current_word == word:
        # this works because lines are sorted before hitting reducer
        current_count += count
    else:
        if current_word:
            print '%s\t%s' % (current_word, current_count)
        current_count = count
        current_word = word

# print the last word
if current_word == word:
    print '%s\t%s' % (current_word, current_count)
