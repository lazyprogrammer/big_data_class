#!/usr/bin/env python

# book url: https://www.amazon.com/dp/B01KH9YWSY
import sys
import json

for line in sys.stdin:
  line = line.strip()
  j = json.loads(line)
  print "%s\t%s" % (j['user_id'], line)
